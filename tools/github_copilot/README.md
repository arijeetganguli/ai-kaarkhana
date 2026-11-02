# GitHub Copilot

How to use AI Kaarkhana with GitHub Copilot. Conventions verified against GitHub and VS Code documentation on **2026-11-02**; see [what was verified](../README.md#what-was-verified-and-when).

## What this repository provides for Copilot

| File or folder | Purpose | Source of truth |
| --- | --- | --- |
| [`.github/copilot-instructions.md`](../../.github/copilot-instructions.md) | Repository wide instructions: shared principles plus repository rules | Hand written part plus a generated principles block |
| [`.github/instructions/`](../../.github/instructions/markdown-content.instructions.md) | Path specific instructions with `applyTo` globs (Markdown, skills, prompts, each example language) | Hand written |
| [`AGENTS.md`](../../AGENTS.md) | Agent instructions; Copilot reads the nearest `AGENTS.md` | Hand written part plus a generated principles block |
| [`.github/skills/`](../../.github/skills/README.md) | The 22 skills, in a location Copilot discovers | **Generated** from `skills/` |
| [`.github/prompts/`](../../.github/prompts/README.md) | The 50 library prompts as prompt files | **Generated** from `prompts/` |

## Use it in this repository

1. Open the repository in your IDE with Copilot enabled. Repository instructions are used automatically for requests in this repository.
2. For a skill, ask in chat for the task and name the skill, for example: *"Use the tdd-engineer skill to implement scenario SC-03."* Copilot loads project skills from `.github/skills/` when they are relevant to the request; the skill's `description` is what it uses to decide.
3. For a prompt file, type `/` in Copilot Chat in a supported IDE and choose the prompt, for example `/boundary-testing`. Replace each `[BRACKETED PLACEHOLDER]` with real content.

Prompt files were described as **public preview** in IDEs when this was checked, so availability and behaviour may differ by IDE and version.

## Use it in your own project

```bash
python scripts/sync_adapters.py install --target github-copilot --dest ../my-project --prompts
```

This writes:

- `.github/skills/<name>/SKILL.md` for all skills (links to this repository's handbook turned into plain text),
- a principles block in `.github/copilot-instructions.md` (created if missing; an existing file keeps your content and gets the block appended or updated between markers),
- with `--prompts`, `.github/prompts/<id>.prompt.md`.

Commit the result so your whole team and Copilot cloud agent see it.

## Notes and limits

- **Path specific instructions**: GitHub documents these as supported on GitHub.com for Copilot cloud agent and Copilot code review. Support in IDE chat depends on the product and version; check the [Copilot feature matrix](https://docs.github.com/en/copilot).
- **Code review**: GitHub documents that Copilot code review reads instructions and skills from the pull request's head branch, so you can test changes to them in the same pull request.
- **Do not edit generated files** in `.github/skills/` and `.github/prompts/`. Edit `skills/` and `prompts/`, then run `python scripts/sync_adapters.py`.
- **Keep instructions short.** Long instruction files dilute adherence. The shared principles block is short on purpose.
- **Skills are not a security boundary.** Review any skill before enabling it, including skills you install from elsewhere.

## Verify it works

Instructions are used only if the tool loads them. A cheap check:

1. Ask Copilot Chat: *"What rules do you follow in this repository about weakening existing tests?"* The answer should reflect `.github/copilot-instructions.md`. In Copilot Chat on GitHub.com, the references list for a response shows when the instructions file was used.
2. Ask it to apply a named skill to a small input and check that it follows the skill's numbered steps and asks for missing input.

If the answers ignore the instructions, check the Copilot settings for custom instructions, your product version and the documentation linked above.

## Sources

- [About agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
- [Repository custom instructions](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions)
- [Prompt files](https://docs.github.com/en/copilot/concepts/prompting-and-context/prompt-files)

[Back to tool adapters](../README.md)
