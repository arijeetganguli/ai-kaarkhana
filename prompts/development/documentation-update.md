---
id: documentation-update
title: "Documentation Update"
category: development
skills: [documentation-engineer]
---

# Documentation Update

## Problem it solves

Documentation lags the code, or is AI-written with invented behaviour.

## When to use

After a change that affects setup, configuration, behaviour or operations.

## Required context

- The diff.
- Existing documentation.
- The audience.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Update the documentation affected by this change.

Audience: [NEW CONTRIBUTOR | API CONSUMER | OPERATOR]
Diff: [DIFF]
Existing docs: [FILES]

Rules:
- Find every document that mentions changed behaviour, configuration or commands and update or remove outdated statements.
- Verify each statement and command against the code. Run commands where possible and use their real output.
- Include prerequisites, steps, expected result and troubleshooting.
- Mark anything you could not verify as UNVERIFIED instead of guessing defaults or configuration keys.
- Do not add marketing language.
List the documents changed and the statements you verified versus those marked UNVERIFIED.
```

## Expected AI output

- Updated documents.
- List of verified and UNVERIFIED statements.

## Validation steps

- [ ] Follow the instructions on a clean checkout.
- [ ] Configuration keys exist in the code.
- [ ] UNVERIFIED items are resolved before merge.

## Related skills

- [Documentation Engineer](../../skills/documentation-engineer/SKILL.md)

Back to [Development prompts](README.md) · [Prompt library](../README.md)
