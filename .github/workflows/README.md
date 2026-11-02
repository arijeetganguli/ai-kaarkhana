# GitHub Actions workflows

Two workflows run on pull requests. Their configuration is in this folder; GitHub only runs files with a `.yml` or `.yaml` extension, so this README is not a workflow.

| Workflow | Runs | What it checks |
| --- | --- | --- |
| [`docs.yml`](docs.yml) | Every pull request and push to `main` | `scripts/validate_docs.py` (internal links and anchors, image existence, front matter and section structure of skills and prompts, SVG validity, Mermaid structure, placeholders and empty files), `scripts/build_registry.py --check`, `scripts/sync_adapters.py --check`, and `scripts/check_mermaid.mjs` (Mermaid syntax with the real parser) |
| [`examples.yml`](examples.yml) | Pull requests and pushes that touch `examples/` | Python examples with pytest, the Broken Code Lab via `scripts/verify_lab.py`, TypeScript examples (`npm ci`, type check, Vitest), Java examples (`mvn test` on Java 17) |

## About these workflows

- They use only the official, widely used actions `actions/checkout@v4`, `actions/setup-python@v5`, `actions/setup-node@v4` and `actions/setup-java@v4`, with read only repository permissions. Review and pin actions according to your organisation's policy.
- **Status claims:** these workflows have not been observed running on GitHub at the time of writing, so this repository makes no claim about their status and shows no status badge. Run the same commands locally (listed in [AGENTS.md](../../AGENTS.md)) to reproduce what CI does.
- **External links** are not checked, because remote availability makes such checks flaky. `validate_docs.py` verifies internal links and anchors only.

## Run the same checks locally

```bash
python scripts/validate_docs.py
python scripts/build_registry.py --check
python scripts/sync_adapters.py --check
python scripts/verify_lab.py
npm install --no-save mermaid jsdom && node scripts/check_mermaid.mjs .
(cd examples/python && pytest)
(cd examples/typescript && npm ci && npm run typecheck && npm test)
(cd examples/java && mvn test)
```
