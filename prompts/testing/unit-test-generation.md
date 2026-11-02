---
id: unit-test-generation
title: "Unit Test Generation"
category: testing
skills: [unit-test-engineer]
---

# Unit Test Generation

## Problem it solves

Existing code has weak or no unit tests.

## When to use

Adding tests to existing code, or after review found weak tests.

## Required context

- The code.
- Existing tests for style.
- Known behaviour rules.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Write unit tests for the code below.

Code: [CODE]
Framework: [FRAMEWORK]
Style reference: [EXISTING TEST FILE]
Behaviour rules: [RULES OR 'infer from code and mark inferred behaviour']

Requirements:
1. List the observable behaviours first (returns, state changes, errors, collaborator calls).
2. Write one test per behaviour, named after it. Use parameterised tests for tables of inputs.
3. Cover each branch, boundary values below/at/above each limit, null and empty inputs, and each error.
4. Assert exact values. No 'is not None', no 'does not throw' alone.
5. Mock only boundaries (network, clock, randomness, database).
6. If behaviour looks like a bug, write the test for the intended behaviour, mark it and report it instead of pinning the bug.
7. Run the tests and report results. Then name one change to the code that your tests would NOT detect.
Report only test and tool results from commands you actually ran, quoting the relevant output.
```

## Expected AI output

- Behaviour list.
- Tests.
- Run output.
- A named undetected mutation.

## Validation steps

- [ ] Break the code by inverting a condition: a test must fail.
- [ ] Tests do not rely on order or time.
- [ ] Suspected bugs were reported not pinned.

## Related skills

- [Unit Test Engineer](../../skills/unit-test-engineer/SKILL.md)

Back to [Testing prompts](README.md) · [Prompt library](../README.md)
