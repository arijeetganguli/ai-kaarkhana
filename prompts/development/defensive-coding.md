---
id: defensive-coding
title: "Defensive Coding Pass"
category: development
skills: [defensive-programming-reviewer, edge-case-hunter]
---

# Defensive Coding Pass

## Problem it solves

Code handles the happy path only and fails unpredictably on missing data, bad input or dependency failure.

## When to use

Implementing or reviewing code that handles external input or calls dependencies.

## Required context

- The code.
- The project's error handling convention.
- Rules about expected behaviour on invalid input.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Review the code below for unhandled cases and propose intentional behaviour for each.

Code:
[CODE]

Error handling convention of this project:
[CONVENTION OR FILE PATH]

For every input, dependency result, conditional, switch and exception handler, list the cases that are not handled: null, empty, wrong type, out of range, unexpected enum value, error, timeout, malformed response, repeated call, concurrent call.
For each, choose one intended behaviour and explain why: reject early with a specific error, safe default (only if the requirement defines it), retry with limit (only if the operation is idempotent), degrade, or fail loudly.
Rules:
- Do not add empty else blocks, catch-all handlers or silent defaults.
- Validate at the boundary, not deep inside.
- If the right behaviour is a business decision, mark it DECISION NEEDED instead of choosing.
- For each handled case write the test that proves it.
Report only test and tool results from commands you actually ran, quoting the relevant output.
```

## Expected AI output

- A table of unhandled cases with chosen behaviour and reasoning.
- Code changes.
- Tests per decision.
- DECISION NEEDED list.

## Validation steps

- [ ] No catch-all or silent default was added.
- [ ] Each decision has a test that fails without the change.
- [ ] Business decisions were escalated.

## Related skills

- [Defensive Programming Reviewer](../../skills/defensive-programming-reviewer/SKILL.md)
- [Edge Case Hunter](../../skills/edge-case-hunter/SKILL.md)

Back to [Development prompts](README.md) · [Prompt library](../README.md)
