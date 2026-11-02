---
name: <kebab-case-name-matching-the-folder>
description: "<What the skill does and when to use it, in one or two sentences. Written so an assistant can decide to load it.>"
license: MIT
metadata:
  activity: <requirements | planning | testing | quality | security | performance | debugging | architecture | review | documentation>
  difficulty: <beginner | intermediate | advanced>
  frameworks: "<comma separated, or any>"
  version: "1.0"
---

# <Skill Title>

> Template for a new skill. Create `skills/<name>/SKILL.md`, delete this note, and replace every `<...>`. The `name` must equal the folder name and use lowercase letters, digits and hyphens. After adding it, run `python scripts/build_registry.py` and `python scripts/sync_adapters.py`, then `python scripts/validate_docs.py`.

## Purpose

<What the skill achieves, in one or two sentences, and what failure it prevents.>

## When to invoke

- <A situation that triggers the skill.>
- <Another.>

## Required input

- <Input one.>
- <Input two.>

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. <Numbered, imperative steps, each verifiable.>
2. <Step two.>
3. <Final step: report evidence and what was not done.>

## Expected output

- <Concrete artefacts and their format.>

## Validation checklist

- [ ] <Check the human can perform.>
- [ ] <Claims about test results come from commands that were run.>

## Example usage

Input:

<A short, realistic input.>

Illustrative output (state clearly if it is hand written and not captured from a model run):

```text
<A short example of good output.>
```

## Sample prompts

```text
<A prompt that invokes the skill, with [BRACKETED PLACEHOLDERS].>
```

## Common mistakes

- <A way the skill is misused or the assistant goes wrong.>

## Related skills

- <Skill title linked with a relative path.>

## Related resources

Handbook, prompts, workflows and examples that relate to this skill, each linked with a relative path.

## Quality bar for a skill

- The `description` says both *what* and *when*.
- Instructions are steps, not advice.
- Output is specified well enough to review.
- It refuses to guess missing inputs.
- It is tool agnostic. Tool specific copies are generated, not hand written.
- Every relative link resolves (`scripts/validate_docs.py` checks it).
