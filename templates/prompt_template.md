---
id: <kebab-case-id-matching-the-file-name>
title: "<Title Case Title>"
category: <requirements | development | testing | debugging | code_review | architecture | delivery>
skills: [<skill-folder-name>, <skill-folder-name>]
---

# <Title Case Title>

> Template for a new prompt. Save as `prompts/<category>/<id>.md`, delete this note, and replace every `<...>`. Add the prompt to the category README and to `prompts/README.md`. Read the quality bar at the bottom first.

## Problem it solves

<One or two sentences: the specific failure this prompt prevents. "Write clean code" is not a problem; "the assistant adds an else that invents a default" is.>

## When to use

<The situation that triggers this prompt.>

## Required context

- <What the user must have ready: code, requirement, logs, versions.>

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
<The prompt text. Be specific and actionable.

Include: the task; the inputs as [BRACKETED PLACEHOLDERS]; the constraints (what not to do);
the required output format; how to handle unknowns (list them, do not guess);
and the evidence rule: report only results from commands actually run, quoting the output.>
```

## Expected AI output

- <What a good answer contains.>

## Validation steps

- [ ] <A check the human performs that does not rely on the assistant's claim.>
- [ ] <A second check.>

## Related skills

- <Skill title, linked with a relative path to its SKILL.md>

Back to <category> prompts and the prompt library (link both with relative paths).

## Quality bar for a prompt

A prompt is ready to merge when it:

- Names a concrete problem and a concrete trigger.
- Lists the context it needs, and says what to do when context is missing.
- Constrains the assistant: scope, forbidden actions, no invented behaviour.
- Specifies the output format.
- Demands evidence from real runs for any claim about tests or behaviour.
- Has validation steps a human can perform independently.
- Is tool agnostic: it works pasted into any assistant.
- Is not generic ("review this code", "find bugs", "write clean code").
