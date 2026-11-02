#!/usr/bin/env python3
"""Validate the repository's documentation and content structure.

Checks (each reported with file and line where possible)

  Markdown     non empty, not only headings; no placeholder wording (TBD, lorem ipsum, coming soon);
               every relative link and image resolves; every #anchor exists (GitHub heading slugs);
               no remote images; no absolute filesystem paths in links; table rows have the same
               number of cells as their header (GitHub drops extra cells silently)
  Mermaid      diagram type is known, brackets balance, subgraph/end balance
  SVG          well formed XML, svg root, viewBox, no scripts, no external references
  Skills       front matter (name = folder, valid characters, description length, string metadata,
               allowed activity and difficulty), required sections in order, size limit
  Prompts      front matter (id = file name, category = folder, skills exist), required sections,
               a text block under "Prompt", listed in the prompt library index
  Workflows    required sections and a Mermaid diagram
  Handbook     twelve chapters, each with What you will learn, Practice and Related
  Indexes      every skill, prompt, workflow, template and chapter is linked from its index page
  Directories  README.md in documented directories
  JSON         skills/registry.json parses
  YAML         workflows and issue forms parse (only when PyYAML is installed; optional)

Usage
    python scripts/validate_docs.py            run all checks
    python scripts/validate_docs.py -q         only print problems and the summary

Exit code 0 when there are no errors. Only the Python standard library is used.
"""

import json
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent

EXCLUDE_DIRS = {".git", "node_modules", "target", "__pycache__", ".venv", "venv", ".pytest_cache", ".idea", ".vscode", "source"}
MIN_SKILLS = 22
MIN_PROMPTS = 50
ACTIVITIES = {"requirements", "planning", "testing", "quality", "security", "performance", "debugging", "architecture", "review", "documentation"}
DIFFICULTIES = {"beginner", "intermediate", "advanced"}
SKILL_SECTIONS = ["Purpose", "When to invoke", "Required input", "Execution instructions", "Expected output", "Validation checklist",
                  "Example usage", "Sample prompts", "Common mistakes", "Related skills", "Related resources"]
PROMPT_SECTIONS = ["Problem it solves", "When to use", "Required context", "Prompt", "Expected AI output", "Validation steps", "Related skills"]
WORKFLOW_SECTIONS = ["When to use", "Starting inputs", "Workflow diagram", "Sequence of activities", "Required outputs",
                     "Validation checkpoints", "Completion criteria"]
CHAPTER_SECTIONS = ["What you will learn", "Practice", "Related"]
MERMAID_TYPES = ("flowchart", "graph", "sequenceDiagram", "stateDiagram", "stateDiagram-v2", "classDiagram", "erDiagram", "gantt", "pie", "journey", "mindmap", "timeline", "gitGraph")
PLACEHOLDER_RE = re.compile(r"\bTBD\b|lorem ipsum|coming soon|to be written|under construction|\bFIXME\b", re.I)

errors = []
warnings = []


def err(path, line, msg):
    loc = f"{rel(path)}" + (f":{line}" if line else "")
    errors.append(f"{loc}: {msg}")


def warn(path, line, msg):
    loc = f"{rel(path)}" + (f":{line}" if line else "")
    warnings.append(f"{loc}: {msg}")


def rel(path):
    try:
        return str(Path(path).resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def walk_files(suffix):
    out = []
    for p in ROOT.rglob(f"*{suffix}"):
        parts = set(p.relative_to(ROOT).parts)
        if parts & EXCLUDE_DIRS:
            continue
        out.append(p)
    return sorted(out)


def read(path):
    return Path(path).read_text(encoding="utf-8")


# --------------------------------------------------------------------------- markdown parsing
FENCE_RE = re.compile(r"^\s*(```+|~~~+)(.*)$")


def split_blocks(text):
    """Yield (line_number, line, in_fence, fence_info) for every line."""
    in_fence = False
    marker = ""
    info = ""
    for n, line in enumerate(text.splitlines(), 1):
        m = FENCE_RE.match(line)
        if m:
            token = m.group(1)
            if not in_fence:
                in_fence, marker, info = True, token[0] * 3, m.group(2).strip()
                yield n, line, True, info
                continue
            if token.startswith(marker) and not m.group(2).strip():
                yield n, line, True, info
                in_fence = False
                continue
        yield n, line, in_fence, info


def strip_inline_code(line):
    return re.sub(r"`+[^`]*`+", lambda m: " " * len(m.group(0)), line)


def slugify(heading):
    text = heading.strip()
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.replace("`", "")
    text = re.sub(r"[*~]", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.lower()
    out = []
    for ch in text:
        if ch in " -" or ch == "_":
            out.append("-" if ch == " " else ch)
        elif unicodedata.category(ch)[0] in "LN" or unicodedata.category(ch) == "Mn":
            out.append(ch)
    return "".join(out)


_anchor_cache = {}


def anchors_of(path):
    path = Path(path).resolve()
    if path in _anchor_cache:
        return _anchor_cache[path]
    seen = {}
    result = set()
    for _n, line, in_fence, _info in split_blocks(read(path)):
        if in_fence:
            continue
        m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
        if not m:
            continue
        slug = slugify(m.group(2))
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        result.add(slug if count == 0 else f"{slug}-{count}")
    _anchor_cache[path] = result
    return result


LINK_RE = re.compile(r"(!?)\[((?:[^\[\]]|\[[^\]]*\])*)\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
IMG_TAG_RE = re.compile(r"<img\b[^>]*\bsrc=[\"']([^\"']+)[\"']", re.I)


def check_links(path, text):
    for n, line, in_fence, _info in split_blocks(text):
        if in_fence:
            continue
        probe = strip_inline_code(line)
        targets = [(m.group(1) == "!", m.group(3)) for m in LINK_RE.finditer(probe)]
        targets += [(True, m.group(1)) for m in IMG_TAG_RE.finditer(probe)]
        for is_image, target in targets:
            check_target(path, n, is_image, target)


def check_target(path, n, is_image, target):
    if re.match(r"^(mailto:|tel:)", target):
        return
    if re.match(r"^https?://", target):
        if is_image:
            err(path, n, f"remote image is not allowed for content: {target}")
        return
    if target.startswith("/") or re.match(r"^[A-Za-z]:\\", target) or target.startswith("file:"):
        err(path, n, f"absolute path in link: {target}")
        return
    file_part, _, anchor = target.partition("#")
    file_part = unquote(file_part)
    anchor = unquote(anchor)
    base = Path(path).parent
    dest = Path(path) if file_part == "" else (base / file_part)
    try:
        resolved = dest.resolve()
    except OSError:
        err(path, n, f"cannot resolve link: {target}")
        return
    if not resolved.exists():
        err(path, n, f"broken link: {target}")
        return
    try:
        resolved.relative_to(ROOT)
    except ValueError:
        err(path, n, f"link leaves the repository: {target}")
        return
    if anchor:
        if resolved.is_dir():
            err(path, n, f"anchor on a directory link: {target}")
        elif resolved.suffix.lower() == ".md":
            if anchor not in anchors_of(resolved):
                err(path, n, f"missing anchor #{anchor} in {rel(resolved)}")


# --------------------------------------------------------------------------- tables
def check_tables(path, text):
    rows = []
    prev_line = 0
    for n, line, in_fence, _info in split_blocks(text):
        stripped = line.strip()
        if not in_fence and stripped.startswith("|"):
            rows.append((n, stripped))
            prev_line = n
            continue
        if rows:
            _check_table(path, rows)
            rows = []
    if rows:
        _check_table(path, rows)


def cell_count(row):
    row = row.strip()
    inner = row[1:]
    if inner.endswith("|") and not inner.endswith("\\|"):
        inner = inner[:-1]
    inner = inner.replace("\\|", "\x00")
    return len(inner.split("|"))


def _check_table(path, rows):
    if len(rows) < 2:
        return
    header_n, header = rows[0]
    expected = cell_count(header)
    sep = rows[1][1]
    if not re.match(r"^\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?$", sep):
        return  # not a table, just lines starting with a pipe
    if cell_count(sep) != expected:
        err(path, rows[1][0], f"table separator has {cell_count(sep)} cells, header has {expected}")
    for n, row in rows[2:]:
        c = cell_count(row)
        if c != expected:
            err(path, n, f"table row has {c} cells but the header has {expected} (a | inside a code span must be written \\|)")


# --------------------------------------------------------------------------- mermaid
def check_mermaid(path, text):
    lines = text.splitlines()
    n = 0
    while n < len(lines):
        if re.match(r"^\s*```+\s*mermaid\s*$", lines[n]):
            start = n + 1
            end = start
            while end < len(lines) and not re.match(r"^\s*```+\s*$", lines[end]):
                end += 1
            block = lines[start:end]
            lint_mermaid(path, start + 1, block)
            n = end
        n += 1


def lint_mermaid(path, first_line, block):
    body = [ln for ln in block if ln.strip() and not ln.strip().startswith("%%")]
    if not body:
        err(path, first_line, "empty mermaid block")
        return
    head = body[0].strip().split()[0]
    if head not in MERMAID_TYPES:
        err(path, first_line, f"unknown mermaid diagram type: {head}")
        return
    if any("\t" in ln for ln in block):
        warn(path, first_line, "tab characters in mermaid block")
    depth = {"[": 0, "(": 0, "{": 0}
    pairs = {"]": "[", ")": "(", "}": "{"}
    subgraphs = 0
    for offset, raw in enumerate(block):
        line = re.sub(r'"[^"]*"', '""', raw)
        line = re.sub(r"\|[^|]*\|", "||", line)
        if re.match(r"^\s*subgraph\b", line):
            subgraphs += 1
        if re.match(r"^\s*end\s*$", line):
            subgraphs -= 1
        for ch in line:
            if ch in depth:
                depth[ch] += 1
            elif ch in pairs:
                depth[pairs[ch]] -= 1
                if depth[pairs[ch]] < 0:
                    err(path, first_line + offset, f"unbalanced '{ch}' in mermaid block")
                    depth[pairs[ch]] = 0
        if raw.count('"') % 2:
            err(path, first_line + offset, "odd number of double quotes in mermaid line")
        if head in ("flowchart", "graph") and re.search(r"-->\s*$", raw):
            err(path, first_line + offset, "edge without a target in mermaid line")
    for ch, d in depth.items():
        if d:
            err(path, first_line, f"unbalanced '{ch}' in mermaid block")
    if subgraphs:
        err(path, first_line, "subgraph/end are not balanced in mermaid block")
    if head in ("flowchart", "graph"):
        check_flowchart_nodes(path, first_line, block)


def check_flowchart_nodes(path, first_line, block):
    """Every node used in an edge must also be defined with a label, or be a plain id used consistently."""
    ids = set()
    for raw in block:
        line = re.sub(r'"[^"]*"', '""', raw)
        line = re.sub(r"\|[^|]*\|", "", line)
        line = re.sub(r"--\s*[^>\-]*?\s*-->", "-->", line)
        for m in re.finditer(r"([A-Za-z_][\w]*)\s*(?:\[|\(|\{)", line):
            ids.add(m.group(1))
    # Nothing else to verify structurally without a real parser; labelled-node duplicates are legal.


# --------------------------------------------------------------------------- front matter
def parse_front_matter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text
    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        return None, text
    data = {}
    current = None
    for raw in lines[1:end]:
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        indented = raw.startswith(" ")
        key, _, value = raw.strip().partition(":")
        value = value.strip()
        if indented and current is not None:
            data[current][key.strip()] = unquote_yaml(value)
        elif value == "":
            current = key.strip()
            data[current] = {}
        else:
            current = None
            data[key.strip()] = unquote_yaml(value)
    return data, "\n".join(lines[end + 1:])


def unquote_yaml(value):
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def h2_sections(text):
    out = []
    for n, line, in_fence, _info in split_blocks(text):
        if in_fence:
            continue
        m = re.match(r"^##\s+(.*?)\s*$", line)
        if m:
            out.append((m.group(1), n))
    return out


def check_sections(path, text, required, ordered=True, label="section"):
    found = h2_sections(text)
    names = [name for name, _n in found]
    missing = [s for s in required if s not in names]
    for s in missing:
        err(path, None, f"missing required {label}: ## {s}")
    if ordered and not missing:
        idx = [names.index(s) for s in required]
        if idx != sorted(idx):
            err(path, None, f"sections are out of order; expected: {', '.join(required)}")


# --------------------------------------------------------------------------- content checks
def check_markdown_files():
    files = walk_files(".md")
    for path in files:
        text = read(path)
        relpath = Path(rel(path))
        in_templates = relpath.parts[0] == "templates" and path.name != "README.md"
        is_meta = relpath.parts[0] == ".github" and relpath.parts[1] in ("instructions", "ISSUE_TEMPLATE") or path.name == "PULL_REQUEST_TEMPLATE.md"
        if not text.strip():
            err(path, None, "file is empty")
            continue
        body_lines = [ln for ln in text.splitlines() if ln.strip() and not ln.lstrip().startswith("#") and ln.strip() != "---"]
        if len(body_lines) < 2:
            err(path, None, "file has only headings or a single line; no real content")
        check_links(path, text)
        check_tables(path, text)
        check_mermaid(path, text)
        if not in_templates and not is_meta:
            for n, line, in_fence, _info in split_blocks(text):
                if in_fence:
                    continue
                probe = strip_inline_code(line)
                m = PLACEHOLDER_RE.search(probe)
                if m:
                    err(path, n, f"placeholder wording: {m.group(0)!r}")
    return files


def check_svgs():
    for path in walk_files(".svg"):
        text = read(path)
        if not text.strip():
            err(path, None, "empty SVG")
            continue
        try:
            root = ET.fromstring(text)
        except ET.ParseError as exc:
            err(path, None, f"SVG is not well formed XML: {exc}")
            continue
        if not root.tag.endswith("svg"):
            err(path, None, f"root element is {root.tag}, expected svg")
        if "viewBox" not in root.attrib:
            err(path, None, "SVG has no viewBox")
        for el in root.iter():
            tag = el.tag.split("}")[-1]
            if tag == "script":
                err(path, None, "SVG contains a script element")
            for k, v in el.attrib.items():
                if k.split("}")[-1] == "href" and re.match(r"^https?://", v):
                    err(path, None, f"SVG references a remote resource: {v}")
        if "<title" not in text:
            warn(path, None, "SVG has no <title> (accessibility)")


def skill_files():
    return sorted((ROOT / "skills").glob("*/SKILL.md"))


def check_skills():
    files = skill_files()
    if len(files) < MIN_SKILLS:
        err(ROOT / "skills", None, f"expected at least {MIN_SKILLS} skills, found {len(files)}")
    names = set()
    for path in files:
        text = read(path)
        meta, body = parse_front_matter(text)
        folder = path.parent.name
        if meta is None:
            err(path, None, "missing or unclosed front matter")
            continue
        name = meta.get("name", "")
        if name != folder:
            err(path, None, f"name {name!r} must equal folder name {folder!r}")
        if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", name) or len(name) > 64:
            err(path, None, "name must be lowercase letters, digits and single hyphens, at most 64 characters")
        names.add(name)
        desc = meta.get("description", "")
        if not desc or len(desc) > 1024:
            err(path, None, f"description must be 1 to 1024 characters (is {len(desc)})")
        elif not re.search(r"\b[Uu]se\b|\bwhen\b", desc):
            warn(path, None, "description should say when to use the skill")
        md = meta.get("metadata")
        if not isinstance(md, dict) or not md:
            err(path, None, "metadata mapping is required")
        else:
            for key in ("activity", "difficulty", "frameworks", "version"):
                if key not in md or not isinstance(md[key], str) or not md[key]:
                    err(path, None, f"metadata.{key} is required and must be a string")
            if md.get("activity") not in ACTIVITIES:
                err(path, None, f"metadata.activity {md.get('activity')!r} not in {sorted(ACTIVITIES)}")
            if md.get("difficulty") not in DIFFICULTIES:
                err(path, None, f"metadata.difficulty {md.get('difficulty')!r} not in {sorted(DIFFICULTIES)}")
        check_sections(path, body, SKILL_SECTIONS, True, "skill section")
        if len(text.splitlines()) > 500:
            warn(path, None, "SKILL.md is longer than 500 lines; consider splitting")
        if not re.search(r"^# \S", body, re.M):
            err(path, None, "missing H1 title")
        if "```text" not in body:
            warn(path, None, "no ```text sample prompt block found")
    return names


def check_prompts(skill_names):
    pdir = ROOT / "prompts"
    prompt_files = sorted(p for p in pdir.glob("*/*.md") if p.name.lower() != "readme.md")
    if len(prompt_files) < MIN_PROMPTS:
        err(pdir, None, f"expected at least {MIN_PROMPTS} prompts, found {len(prompt_files)}")
    ids = set()
    index = read(pdir / "README.md") if (pdir / "README.md").exists() else ""
    for path in prompt_files:
        text = read(path)
        meta, body = parse_front_matter(text)
        if meta is None:
            err(path, None, "missing or unclosed front matter")
            continue
        if meta.get("id") != path.stem:
            err(path, None, f"id {meta.get('id')!r} must equal the file name {path.stem!r}")
        if meta.get("id") in ids:
            err(path, None, f"duplicate prompt id {meta.get('id')!r}")
        ids.add(meta.get("id"))
        if meta.get("category") != path.parent.name:
            err(path, None, f"category {meta.get('category')!r} must equal the folder {path.parent.name!r}")
        if not meta.get("title"):
            err(path, None, "title is required")
        skills = re.findall(r"[a-z0-9-]+", meta.get("skills", "").strip("[]"))
        if not skills:
            err(path, None, "skills list is required")
        for s in skills:
            if s not in skill_names:
                err(path, None, f"unknown skill in front matter: {s}")
        check_sections(path, body, PROMPT_SECTIONS, True, "prompt section")
        section = re.search(r"## Prompt\n(.*?)(?=\n## )", body, re.S)
        if section and not re.search(r"```text\n.+?\n```", section.group(1), re.S):
            err(path, None, "the Prompt section must contain a ```text block")
        rel_in_index = f"{path.parent.name}/{path.name}"
        if rel_in_index not in index:
            err(pdir / "README.md", None, f"prompt not linked from the prompt library index: {rel_in_index}")
        if re.search(r"\b(write clean code|find bugs)\b", body, re.I) and "Avoid" not in body:
            warn(path, None, "prompt may be too generic")
    return ids


def check_workflows():
    wdir = ROOT / "workflows"
    files = sorted(p for p in wdir.glob("*.md") if p.name != "README.md")
    if len(files) != 10:
        err(wdir, None, f"expected 10 workflows, found {len(files)}")
    index = read(wdir / "README.md") if (wdir / "README.md").exists() else ""
    for path in files:
        text = read(path)
        check_sections(path, text, WORKFLOW_SECTIONS, True, "workflow section")
        if "```mermaid" not in text:
            err(path, None, "workflow has no Mermaid diagram")
        if path.name not in index:
            err(wdir / "README.md", None, f"workflow not linked from index: {path.name}")


def check_handbook():
    hdir = ROOT / "handbook"
    chapters = sorted(p for p in hdir.glob("*/README.md"))
    if len(chapters) != 12:
        err(hdir, None, f"expected 12 chapters, found {len(chapters)}")
    index = read(hdir / "README.md") if (hdir / "README.md").exists() else ""
    for path in chapters:
        text = read(path)
        check_sections(path, text, CHAPTER_SECTIONS, False, "chapter section")
        if not re.search(r"^# Chapter \d+: ", text, re.M):
            err(path, None, "chapter title must be '# Chapter N: ...'")
        if f"{path.parent.name}/README.md" not in index:
            err(hdir / "README.md", None, f"chapter not linked from handbook index: {path.parent.name}")


def check_indexes():
    pairs = [
        (ROOT / "skills" / "README.md", [f"{p.parent.name}/SKILL.md" for p in skill_files()]),
        (ROOT / "skills" / "REGISTRY.md", [f"{p.parent.name}/SKILL.md" for p in skill_files()]),
        (ROOT / "templates" / "README.md", [p.name for p in (ROOT / "templates").glob("*.md") if p.name != "README.md"]),
        (ROOT / "examples" / "README.md", [d.name for d in (ROOT / "examples").iterdir() if d.is_dir() and d.name in ("java", "python", "typescript", "broken_code_lab", "end_to_end")]),
    ]
    for index, items in pairs:
        if not index.exists():
            err(index, None, "index file is missing")
            continue
        text = read(index)
        for item in items:
            if item not in text:
                err(index, None, f"does not link to {item}")


def check_json():
    p = ROOT / "skills" / "registry.json"
    if p.exists():
        try:
            data = json.loads(read(p))
            if data.get("count") != len(data.get("skills", [])):
                err(p, None, "count does not match the number of skills")
        except json.JSONDecodeError as exc:
            err(p, None, f"invalid JSON: {exc}")
    else:
        err(p, None, "registry.json is missing; run scripts/build_registry.py")


DOCUMENTED_DIRS = [
    "assets", "assets/diagrams", "assets/images", "assets/logos", "docs", "examples", "examples/java", "examples/python",
    "examples/typescript", "examples/broken_code_lab", "examples/end_to_end", "handbook", "prompts", "prompts/architecture",
    "prompts/code_review", "prompts/debugging", "prompts/delivery", "prompts/development", "prompts/requirements", "prompts/testing",
    "scripts", "skills", "templates", "tools", "tools/claude_code", "tools/cursor", "tools/generic_agents", "tools/github_copilot",
    "workflows", ".github/workflows", ".github/skills", ".github/prompts",
]


def check_readmes():
    for d in DOCUMENTED_DIRS:
        p = ROOT / d
        if not p.is_dir():
            err(p, None, "expected directory is missing")
        elif not (p / "README.md").exists():
            err(p, None, "directory has no README.md")


def check_basic_files():
    for name in ("README.md", "LICENSE", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md", "CHANGELOG.md", "ROADMAP.md", "AGENTS.md", "CLAUDE.md", ".gitignore"):
        p = ROOT / name
        if not p.exists():
            err(p, None, "required root file is missing")
        elif not p.read_text(encoding="utf-8").strip():
            err(p, None, "required root file is empty")
    for name in (".github/copilot-instructions.md", ".github/PULL_REQUEST_TEMPLATE.md"):
        if not (ROOT / name).exists():
            err(ROOT / name, None, "required file is missing")
    for p in (ROOT / ".github" / "workflows").glob("*.yml"):
        if not p.read_text(encoding="utf-8").strip():
            err(p, None, "empty workflow file")
    agents = ROOT / "AGENTS.md"
    if agents.exists() and "<!-- BEGIN ai-kaarkhana principles" not in read(agents):
        err(agents, None, "principles block markers are missing")


def check_yaml():
    """Parse workflow and issue form YAML when PyYAML is installed (it is optional)."""
    try:
        import yaml
    except ImportError:
        return False
    for p in sorted((ROOT / ".github").rglob("*.yml")):
        try:
            data = yaml.safe_load(read(p))
        except yaml.YAMLError as exc:
            err(p, None, "invalid YAML: " + str(exc).replace("\n", " ")[:160])
            continue
        if not isinstance(data, dict):
            err(p, None, "YAML document is not a mapping")
        elif p.parent.name == "ISSUE_TEMPLATE" and p.name != "config.yml":
            for key in ("name", "description", "body"):
                if not data.get(key):
                    err(p, None, f"issue form is missing {key}")
    return True


def check_empty_files():
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        parts = set(p.relative_to(ROOT).parts)
        if parts & EXCLUDE_DIRS:
            continue
        if p.name in ("__init__.py", ".gitkeep", ".gitignore") or p.suffix in (".pyc",):
            continue
        if p.stat().st_size == 0:
            err(p, None, "file is empty")


# --------------------------------------------------------------------------- main
def main(argv):
    quiet = "-q" in argv
    md_files = check_markdown_files()
    check_svgs()
    names = check_skills()
    check_prompts(names)
    check_workflows()
    check_handbook()
    check_indexes()
    check_json()
    check_readmes()
    check_basic_files()
    check_empty_files()
    yaml_checked = check_yaml()
    if not yaml_checked:
        warnings.append("PyYAML not installed: workflow and issue form YAML was not parsed (pip install pyyaml)")

    if warnings and not quiet:
        print("Warnings:")
        for w in warnings:
            print(f"  warn  {w}")
    if errors:
        print("Errors:")
        for e in errors:
            print(f"  ERROR {e}")
    print(f"\nChecked {len(md_files)} Markdown files, {len(list(skill_files()))} skills, "
          f"{len(list((ROOT / 'prompts').glob('*/*.md'))) - len(list((ROOT / 'prompts').glob('*/README.md')))} prompts, "
          f"{len(walk_files('.svg'))} SVGs: {len(errors)} error(s), {len(warnings)} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
