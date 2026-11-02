---
id: negative-testing
title: "Negative Testing"
category: testing
skills: [unit-test-engineer, defensive-programming-reviewer]
---

# Negative Testing

## Problem it solves

Only success paths are tested, so invalid input behaviour is accidental.

## When to use

Code accepts external input or can be called in invalid states.

## Required context

- The code and its contract.
- Error handling convention.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Write negative tests for the code below.

Code: [CODE]
Contract and error conventions: [CONTRACT / ERROR TYPES]

Cover: null, empty and whitespace values; wrong types or formats; out of range numbers; oversized input; invalid state transitions (for example shipping a cancelled order); repeated calls; unauthorised callers; dependency errors.
For each, assert the exact error type and message or status, and assert that no side effect occurred (nothing stored, nothing sent).
If the contract does not define the expected error, list UNSPECIFIED and ask. Do not invent error types.
Run the tests and report results. Report only test and tool results from commands you actually ran, quoting the relevant output.
```

## Expected AI output

- Negative tests with exact error assertions.
- Side-effect checks.
- UNSPECIFIED error behaviours.

## Validation steps

- [ ] Tests fail if validation is removed.
- [ ] No test passes merely because 'something' was thrown.
- [ ] Side effects verified.

## Related skills

- [Unit Test Engineer](../../skills/unit-test-engineer/SKILL.md)
- [Defensive Programming Reviewer](../../skills/defensive-programming-reviewer/SKILL.md)

Back to [Testing prompts](README.md) · [Prompt library](../README.md)
