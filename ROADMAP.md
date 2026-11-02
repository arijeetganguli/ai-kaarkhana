# Roadmap

This is a statement of direction, not a promise or a schedule. It is a volunteer project; priorities follow what contributors need and what readers tell us is useful. Items are grouped by how close they are, not by date. To influence it, open an issue or send a pull request.

For what exists today, and how each part was verified, see the [implementation status](docs/implementation_status.md).

## Now: make the first release solid

- Observe the [GitHub Actions workflows](.github/workflows/README.md) running on GitHub and fix anything that only shows up there. They were written and their commands were run locally, but not yet observed on GitHub.
- Render Mermaid diagrams in CI. Today they are structurally linted and parsed with the real Mermaid parser, but not rendered.
- Collect feedback from first readers on the skills and prompts: which were used, which misled, which are missing.
- Check the adapter conventions for GitHub Copilot, Cursor and Claude Code again before each release, because tools change (last verified 2026-11-02; see [Tool adapters](tools/README.md)).
- Execute the fast-check and jqwik snippets in the property testing page, or keep them clearly labelled as illustrative.

## Next: broaden the material

- **More languages** for the examples: for example Go, C# and Kotlin, using the same nine scenarios so they can be compared.
- **More Broken Code Lab exercises** in Java and TypeScript, and further defect classes (time zones and daylight saving, floating point money, pagination off by one, cache invalidation).
- **More skills and prompts**, proposed through the issue forms. Candidates: accessibility review, observability design, data migration verification, dependency upgrade planning.
- **Worked case studies** with real, redacted before and after pull requests, contributed by people who have done the work.
- **Translations** of the handbook, starting with the introduction and the glossary.

## Later: tooling

- An **interactive maturity assessment**: a small static web page that scores the [assessment](docs/maturity_assessment.md) in the browser, with nothing sent to a server.
- A **skill linter** that goes further than structure: flags vague instructions, missing validation steps and overlapping skills.
- **Prompt regression checks**: a way to record a prompt's expected qualities and re-check them when models change, without claiming deterministic output.
- Adapters for **further tools**, added only after their conventions have been verified against the vendor's documentation.

## Not planned

- Vendor specific forks of the content. One canonical source plus generated adapters is deliberate.
- Productivity benchmarks or leaderboards. The project does not publish statistics it cannot stand behind.
- Replacing your organisation's security, privacy or legal guidance.

## How items move

An idea becomes an issue, an issue gets a short design discussion, and a pull request implements it with its own validation. Items that nobody picks up for a long time are removed from this page rather than left to mislead.

See [CONTRIBUTING.md](CONTRIBUTING.md) to take one on, and the [changelog](CHANGELOG.md) for what has shipped.
