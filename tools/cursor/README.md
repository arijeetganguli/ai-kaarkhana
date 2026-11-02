# Cursor

How to use AI Kaarkhana with Cursor. Conventions verified against the Cursor documentation on **2026-11-02**; see [what was verified](../README.md#what-was-verified-and-when).

## What Cursor reads

| Mechanism | Location | Notes |
| --- | --- | --- |
| **`AGENTS.md`** | Repository root and subdirectories | Plain Markdown, no front matter. Nested files apply to their directory; more specific instructions take precedence. This repository's [`AGENTS.md`](../../AGENTS.md) works in Cursor as is. |
| **Project rules** | `.cursor/rules/*.mdc` | Front matter `description`, `globs`, `alwaysApply`. A plain `.md` file in that folder is ignored. |
| **Skills** | `.agents/skills/`, `.cursor/skills/` (also `.claude/skills/`, `.codex/skills/` for compatibility) | A folder per skill with `SKILL.md`. The agent chooses a skill from its `description`; you can also invoke one by typing `/` and the skill name. |

## Use it in this repository

- **Instructions:** open the repository in Cursor. `AGENTS.md` is picked up from the root, so no extra setup is needed.
- **Skills:** the canonical skills live in `skills/`, which Cursor does not scan. Attach one to a chat by `@`-mentioning the file, for example `@skills/tdd-engineer/SKILL.md`, or install the skills into a project as described below.
- **Prompts:** open a file in `prompts/`, copy the fenced `text` block, replace placeholders, and paste it into Agent chat.

## Use it in your own project

```bash
python scripts/sync_adapters.py install --target cursor --dest ../my-project
```

This writes:

- `.cursor/skills/<name>/SKILL.md` for all skills (links to this repository's handbook turned into plain text),
- `.cursor/rules/ai-kaarkhana-principles.mdc`, an always applied rule containing the shared principles.

Commit them so your team gets the same behaviour. Existing files are skipped unless you pass `--force`.

### The rule file the installer writes

```markdown
---
description: Engineering principles for AI assisted work
alwaysApply: true
---

(contents of tools/generic_agents/principles.md)
```

If you prefer a single instruction file, copy [`principles.md`](../generic_agents/principles.md) into your own `AGENTS.md` instead and skip the rule.

## Scoping a skill to files

Cursor skills support optional front matter such as `paths` (glob patterns) and `disable-model-invocation` (explicit invocation only). The canonical skills here do not set them, to stay portable. You can add them to your installed copy if you want a skill to apply only to certain files, for example test skills for `**/*test*`. Check the [Cursor skills documentation](https://cursor.com/docs/context/skills) for the current fields.

## Notes and limits

- Keep rules short and focused. Cursor's documentation recommends keeping rules under 500 lines and splitting large ones.
- Reference files in rules instead of copying their contents.
- Rules do not affect Cursor Tab or other non-agent features, per the documentation.
- Team rules, if you use them, take precedence over project rules.
- Do not edit installed copies if you want to receive updates; edit the canonical skills and re-run the installer with `--force`.

## Verify it works

1. Open a new Agent chat and ask: *"What do you do when a requirement is ambiguous?"* The answer should reflect the principles (ask, list unspecified behaviour, do not guess).
2. Type `/` and look for the installed skills in the list.
3. Ask it to apply `edge-case-hunter` to a small rule and check that it follows the numbered steps.

If a rule is not applied, check its type (always, intelligently, by file pattern) and that the file has the `.mdc` extension.

## Sources

- [Agent Skills](https://cursor.com/docs/context/skills)
- [Rules](https://cursor.com/docs/context/rules)

[Back to tool adapters](../README.md)
