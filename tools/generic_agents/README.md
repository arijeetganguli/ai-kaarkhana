# Generic agents

For any assistant that is not covered by a dedicated guide, and as the neutral baseline for all of them. Everything here is plain Markdown, so it works with any tool that lets you provide instructions or paste text.

## The canonical principles

[`principles.md`](principles.md) is the **canonical block of shared engineering principles**. It is the only place they are written. The sync script copies it, between marker comments, into:

- [`AGENTS.md`](../../AGENTS.md) in this repository,
- [`.github/copilot-instructions.md`](../../.github/copilot-instructions.md),
- the files that `install` writes into other projects (`AGENTS.md`, `CLAUDE.md`, a Cursor rule, or Copilot instructions).

Edit `principles.md` and run `python scripts/sync_adapters.py`. CI runs `--check` and fails if a copy differs.

The principles cover: accountability and evidence, requirements before code, tests as specification, defensive code, scope discipline, security and privacy, and honest reporting. They are the practical summary of [Chapter 1](../../handbook/01_ai_native_engineering/README.md) and [Chapter 4](../../handbook/04_ai_assisted_development/README.md).

## Option 1: `AGENTS.md`

`AGENTS.md` is a plain Markdown instruction file for coding agents, kept at the repository root (and optionally in subdirectories). Several tools read it; check your tool's documentation. Install the principles into your project with:

```bash
python scripts/sync_adapters.py install --target generic --dest ../my-project
```

This creates or updates `AGENTS.md` (the principles are written between marker comments; your own content around them is preserved) and copies the skills to `.agents/skills/`. The Agent Skills location `.agents/skills/` is documented as discovered by GitHub Copilot and Cursor at the time of checking ([tools](../README.md#what-was-verified-and-when)); other tools may use a different location.

## Option 2: paste

No installation, any tool:

1. Open [`principles.md`](principles.md) and paste it at the start of the conversation, or into your tool's "custom instructions" field.
2. For a task, paste the relevant `SKILL.md` ([skills](../../skills/README.md)) and say what to apply it to.
3. For a prompt, copy the text block from [`prompts/`](../../prompts/README.md), replace the placeholders and send it.

A starting message:

```text
Follow the engineering principles below for this whole conversation.
Then apply the skill that follows to my input. If required input is missing, ask me; do not guess.

[PASTE principles.md]

[PASTE SKILL.md]

My input: [INPUT]
```

## Option 3: a task brief

Use the [AI task template](../../templates/ai_task_template.md) to hand a bounded task to any agent with goal, context, constraints, steps, output format and evidence rules.

## What a tool must support for the principles to work

| Capability | Why it matters |
| --- | --- |
| Reads a project or system instruction file, or lets you paste text | To carry the principles into every task |
| Can run commands or lets you run them and paste output | The evidence rule requires real runs |
| Shows diffs before applying | So the reviewer can check scope |
| Lets you approve commands before they run | Prompt injection and unintended changes ([Chapter 9](../../handbook/09_security_engineering/README.md)) |

If a tool cannot run commands, the principle becomes: *the assistant proposes, you run, you paste the output back*.

## Limits

- Instruction files are **guidance**, not enforcement. Models can ignore them. Enforcement comes from automated checks (tests, lint, CI) and review.
- Different tools weigh instruction files differently, and some truncate long ones. The principles block is short for that reason.
- Nothing here verifies a specific tool beyond what is dated and linked in [tools](../README.md).

[Back to tool adapters](../README.md)
