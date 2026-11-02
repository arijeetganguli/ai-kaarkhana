# Claude Code

How to use AI Kaarkhana with Claude Code. Conventions verified against the Claude Code documentation on **2026-11-02**; see [what was verified](../README.md#what-was-verified-and-when). Behaviour depends on the Claude Code version, so check the documentation if something differs.

## What Claude Code reads

| Mechanism | Location | Notes |
| --- | --- | --- |
| **`CLAUDE.md`** | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Read at the start of every session. Supports `@path/to/file` imports; relative paths resolve from the file containing the import. |
| **`AGENTS.md`** | Repository root | Per the documentation, read as project instructions only when no `CLAUDE.md` applies, and requires a recent Claude Code version. If a `CLAUDE.md` imports `AGENTS.md`, it is included through the import. |
| **Skills** | `.claude/skills/<name>/SKILL.md` (project), `~/.claude/skills/` (personal) | The skill's body loads when it is used. A skill can also be invoked by name with `/`. |

## Use it in this repository

This repository's [`CLAUDE.md`](../../CLAUDE.md) contains a single import, `@AGENTS.md`, so Claude Code receives the same shared principles and repository rules as every other tool. It does not commit a copy of the skills under `.claude/skills/`; the canonical skills are in `skills/`.

To use a skill here, ask Claude Code to read the canonical file and apply it, for example: *"Read skills/tdd-engineer/SKILL.md and apply it to scenario SC-03."* Do not run the installer with `--dest .` in this repository: it would add a second, installed copy of files that already exist here.

## Use it in your own project

```bash
python scripts/sync_adapters.py install --target claude-code --dest ../my-project
```

This writes:

- `.claude/skills/<name>/SKILL.md` for all skills (links to this repository's handbook turned into plain text),
- a principles block in `CLAUDE.md` between marker comments. An existing `CLAUDE.md` keeps your content; the block is appended or updated in place.

If your project already has an `AGENTS.md` for other tools, prefer this instead: keep the principles in `AGENTS.md` (use `--target generic`) and make your `CLAUDE.md` a one line import:

```markdown
@AGENTS.md
```

## Notes and limits

- **Keep `CLAUDE.md` short.** The documentation suggests targeting under 200 lines per file; imported files load with the file that imports them, so imports organise content but do not reduce its cost.
- **Skills load on demand**, so they are a better home than `CLAUDE.md` for procedures that apply only to some tasks.
- **Imports from outside the project** trigger an approval prompt the first time; this repository's import is a sibling file and is not external.
- **Project skill folders** are not committed in this repository, to avoid duplicates of the canonical files. In your own project, commit the output of the installer in `.claude/skills/` and treat it as generated.
- **`metadata` values must be strings.** The skills here comply with the Agent Skills specification.

## Verify it works

1. Start Claude Code in the project and check which instruction files your version reports as loaded.
2. Ask: *"Summarise the rules you must follow about tests and unspecified requirements."*
3. Run a skill by name or ask for the task it covers, and check that it follows the steps and asks for missing input.

## Sources

- [Skills](https://code.claude.com/docs/en/skills)
- [Memory (CLAUDE.md and AGENTS.md)](https://code.claude.com/docs/en/memory)

[Back to tool adapters](../README.md)
