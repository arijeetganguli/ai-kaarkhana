# Scripts

Small, dependency free Python scripts (standard library only, except `verify_lab.py`, which needs `pytest`), plus one Node script for Mermaid. They keep the repository consistent and are run by [CI](../.github/workflows/README.md). Run all of them from the repository root.

| Script | What it does | Run when |
| --- | --- | --- |
| [`validate_docs.py`](validate_docs.py) | Checks Markdown content, links and anchors, tables, Mermaid blocks, SVGs, skill and prompt structure, indexes and required files | Before every pull request |
| [`build_registry.py`](build_registry.py) | Builds [`skills/REGISTRY.md`](../skills/REGISTRY.md) and [`skills/registry.json`](../skills/registry.json) from skill front matter | After changing a skill's front matter |
| [`sync_adapters.py`](sync_adapters.py) | Generates `.github/skills`, `.github/prompts` and the principles blocks; installs adapters into other projects | After changing a skill, a prompt or the principles |
| [`verify_lab.py`](verify_lab.py) | Proves each Broken Code Lab exercise fails on `broken.py` and passes on `solution.py` | After changing a lab exercise |
| [`check_mermaid.mjs`](check_mermaid.mjs) | Parses every Mermaid block with the real Mermaid parser (syntax only, no rendering); needs `npm install --no-save mermaid jsdom` | Before a pull request that changes diagrams |
| [`generate_svgs.py`](generate_svgs.py) | Generates the SVG logo, hero and diagrams under [`assets/`](../assets/README.md) | After changing a visual |

## Commands

```bash
python scripts/validate_docs.py            # all documentation checks; add -q to show only problems
python scripts/build_registry.py           # write the registry
python scripts/build_registry.py --check   # fail if the registry is out of date
python scripts/sync_adapters.py            # regenerate generated copies
python scripts/sync_adapters.py --check    # fail if generated copies are out of date
python scripts/sync_adapters.py install --target github-copilot --dest ../my-project --prompts
python scripts/verify_lab.py               # all exercises; pass prefixes such as "04 07" to select some
python scripts/generate_svgs.py            # regenerate SVG assets
npm install --no-save mermaid jsdom && node scripts/check_mermaid.mjs .   # parse Mermaid blocks
```

All scripts exit with a non zero status when a check fails, so they can be used in CI and in a pre commit hook.

## What `validate_docs.py` checks

| Area | Rules |
| --- | --- |
| Markdown | File is not empty and not only headings; no placeholder wording; every relative link and image resolves; every `#anchor` matches a heading (GitHub slug rules); no remote images; no absolute paths in links |
| Tables | Every row has as many cells as the header. A `\|` inside a code span in a table must be escaped |
| Mermaid | Known diagram type; brackets, quotes and `subgraph`/`end` balanced |
| SVG | Well formed XML; `svg` root with a `viewBox`; no scripts or remote references |
| Skills | `name` equals the folder, valid characters, description at most 1024 characters, string `metadata`, allowed activity and difficulty, all eleven sections in order |
| Prompts | `id` equals the file name, `category` equals the folder, skills exist, seven sections in order, a `text` block under `Prompt`, listed in the prompt index |
| Workflows and handbook | Required sections, a Mermaid diagram per workflow, twelve chapters, each listed in its index |
| Indexes | Every skill, prompt, workflow, template and example folder is linked from its index |
| Repository | README in each documented directory; required root files exist; registry JSON is consistent |

The Mermaid check in `validate_docs.py` is a **structural lint**. For a stronger check, `check_mermaid.mjs` runs the real Mermaid parser over every diagram. Neither renders the diagrams, so layout problems are only visible when you preview them on GitHub.

## Design notes

- **No dependencies** (apart from pytest for the lab), so the scripts run anywhere Python 3.10 or newer is installed.
- **Generated files are checked, not trusted.** `--check` modes recompute the output in memory and compare it with the committed files.
- **Scripts never touch files outside the repository** unless you pass `--dest` to the installer, and the installer does not overwrite existing skill and rule files without `--force`.

Back to the [repository README](../README.md).
