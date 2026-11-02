# Implementation status

An honest record of what this repository contains, how each part was verified, the assumptions made, and what is known to be missing. It is updated whenever the contents change materially.

Last full verification run: **2026-11-02**, on macOS, locally. Nothing in this repository claims that anything has been observed running on GitHub. Runtimes used: Python 3.15.0 with pytest 9.2.0, Node.js 26.10.0, OpenJDK 17.0.20, Maven 3.9.9.

## Summary

| Area | Delivered | Where |
| --- | --- | --- |
| Handbook | 12 chapters (17 pages including the index and extra pages in chapters 5 and 6) | [handbook](../handbook/README.md) |
| Skills | 22, Agent Skills format, plus a generated registry (Markdown and JSON) | [skills](../skills/README.md) |
| Prompts | 50 in seven categories, plus a playground | [prompts](../prompts/README.md) |
| Workflows | 10, each with a Mermaid diagram and gates | [workflows](../workflows/README.md) |
| Examples | 9 scenarios each in Python, Java and TypeScript; one end to end walk through | [examples](../examples/README.md) |
| Broken Code Lab | 8 exercises | [lab](../examples/broken_code_lab/README.md) |
| Templates | 11 templates plus the AI code review checklist | [templates](../templates/README.md) |
| Visuals | Logo, mark, hero and 9 diagrams (12 SVG files) | [assets](../assets/README.md) |
| Tool adapters | GitHub Copilot, Cursor, Claude Code, generic | [tools](../tools/README.md) |
| Docs | Getting started, learning paths, maturity assessment, skill of the week, glossary, FAQ | [docs](README.md) |
| Governance | MIT license, contributing guide, code of conduct, security policy, changelog, roadmap, issue forms, pull request template | repository root and `.github/` |
| Automation | Five Python scripts, one Node script, two GitHub Actions workflows | [scripts](../scripts/README.md), [workflows](../.github/workflows/README.md) |

## Verification record

Commands run from the repository root unless stated. Results are what the commands actually printed.

| Check | Command | Result |
| --- | --- | --- |
| Documentation validation | `python scripts/validate_docs.py` | 0 errors, 0 warnings (248 Markdown files, 22 skills, 50 prompts, 12 SVGs) |
| Skill registry current | `python scripts/build_registry.py --check` | passes (22 skills) |
| Adapters current | `python scripts/sync_adapters.py --check` | passes (74 generated or managed files) |
| Mermaid syntax | `node scripts/check_mermaid.mjs .` (Mermaid 12.2.0 parser) | 26 blocks, 0 failures; the parser was also confirmed to reject three deliberately broken diagrams |
| Python examples | `pytest` in `examples/python` | 244 passed |
| TypeScript examples | `tsc --noEmit` and `vitest run` in `examples/typescript` | no type errors; 103 tests passed in 9 files |
| Java examples | `mvn -B -ntp test` in `examples/java` (JDK 17) | 88 tests, 0 failures, BUILD SUCCESS |
| Broken Code Lab | `python scripts/verify_lab.py` | all 8 exercises fail on `broken.py` and pass on `solution.py` |
| Property based testing snippet | Hypothesis run once against five hand written mutants | all five mutants killed by four properties; recorded in [the page](../handbook/05_test_driven_development/property_based_and_mutation_testing.md) |
| GitHub workflow and issue form YAML | parsed with PyYAML | all files parse; issue forms have the required keys |
| SVG rendering | rendered with resvg and inspected | no overlapping text or detached arrows in the final versions |

What `validate_docs.py` covers is listed in the [scripts guide](../scripts/README.md#what-validate_docspy-checks). It checks internal links, anchors, images, tables, structure and placeholders. It does not check external URLs.

## Assumptions

- **Audience:** practising software engineers, leads, architects, QA engineers and managers, with the content in English.
- **Skills format:** the open Agent Skills format (a folder with `SKILL.md`, `name` and `description` front matter, optional `metadata` as string to string). Verified against its published specification on 2026-11-02.
- **Tool conventions** for GitHub Copilot, Cursor and Claude Code were checked against each vendor's documentation on 2026-11-02; sources are in [Tool adapters](../tools/README.md#what-was-verified-and-when). They will change.
- **The maturity model** (five levels from Ad hoc to Optimising) is this handbook's own framework. It is not an industry standard, and there are no benchmarks behind it.
- **External standards** (DORA, SPACE, OWASP, STRIDE) are described briefly and point to their owners for current definitions.
- **Money in examples** is stored as integer cents to avoid floating point errors.
- **Python** is used for the Broken Code Lab for brevity; the defect classes also appear in the Java and TypeScript examples.
- **No statistics or productivity claims** are made. Test counts are the real counts from the runs above.
- **Repository URL and contact details** are not known at build time. Text that would need them points to GitHub features (private vulnerability reporting, the repository profile) instead of inventing addresses.

## Known limitations

1. **GitHub Actions workflows have not been observed running on GitHub.** The workflow files parse, and every command in them was run locally, but action versions, runner images and permissions have not been exercised. There are no status badges for that reason.
2. **Mermaid diagrams are parsed, not rendered.** The real Mermaid parser accepts all 26 blocks, but visual layout was not inspected.
3. **The fast-check (TypeScript) and jqwik (Java) property testing snippets were not executed.** They are labelled illustrative. Only the Hypothesis example was run.
4. **The Broken Code Lab is Python only.**
5. **External links are not validated.** Only internal links, anchors and images are.
6. **Prompts and skills were not evaluated against live models.** Their *expected output* and *validation steps* describe what a good answer contains; model output varies, and no model transcripts are included as evidence. The [prompt playground](../prompts/playground.md) deliberately contains no fabricated outputs.
7. **Adapter behaviour was checked against documentation, not by running each tool.** For example, whether a particular IDE version loads a generated `.prompt.md` file was not tested.
8. **Issue form labels** (`bug`, `documentation`, `enhancement`, `skill`, `prompt`) must exist in the GitHub repository for them to be applied. Create them after publishing.
9. **Enforcement contact for the code of conduct** is described generically. Maintainers should set a real private contact before publishing.
10. **Minimum versions were not tested.** The documents say Python 3.10 or newer, JDK 17 and Node.js 20 or newer. Locally only the runtimes listed at the top were used; CI is configured for Python 3.12, Node.js 22 and JDK 17. Tool conventions and external standards (OWASP, DORA) also age and should be rechecked at each release.
11. **The first push to GitHub has not succeeded.** The local repository exists, with `origin` set to `git@github.com:arijeetganguli/ai-kaarkhana.git`, but `git push` was rejected with `Permission denied (publickey)`. The empty GitHub repository was confirmed through the public API. Create the issue labels after the push succeeds.

## Progress checklist

- [x] Repository structure and original design brief preserved in `docs/source/`
- [x] Brand assets: logo, mark, hero, 9 diagrams, generator script
- [x] Handbook chapters 1 to 12 and index
- [x] 22 skills in a consistent structure
- [x] Skill registry (Markdown and JSON), generated and checked
- [x] 50 prompts in seven categories with indexes
- [x] Prompt playground
- [x] 10 workflows with Mermaid diagrams
- [x] Python, Java and TypeScript examples with tests
- [x] End to end example
- [x] Broken Code Lab, 8 exercises, verified by script
- [x] Templates and AI code review checklist
- [x] `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, path specific instructions
- [x] Generated `.github/skills` and `.github/prompts`, with drift check
- [x] Tool adapter guides and installer for GitHub Copilot, Cursor, Claude Code, generic agents
- [x] Getting started, learning paths, maturity assessment, skill of the week, glossary, FAQ
- [x] Root README with Start Here for five roles
- [x] MIT license, contributing guide, code of conduct, security policy, changelog, roadmap
- [x] Issue forms and pull request template
- [x] Validation script, registry and adapter checks, Mermaid parse check
- [x] GitHub Actions workflows written and commands verified locally
- [ ] Workflows observed on GitHub
- [ ] Mermaid rendering in CI
- [ ] Prompts and skills evaluated with live models
- [ ] Repository published and labels created

## How to keep this page honest

When you add content, update the numbers above only from real command output. When something is verified, record the command and what it printed; when it is not, say so under *Known limitations*.

Back to [documentation index](README.md).
