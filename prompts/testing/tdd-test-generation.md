---
id: tdd-test-generation
title: "TDD Test Generation"
category: testing
skills: [tdd-engineer, unit-test-engineer]
---

# TDD Test Generation

## Problem it solves

Tests written after the code mirror the implementation instead of specifying behaviour.

## When to use

Starting the red phase for a scenario.

## Required context

- Scenario matrix rows to implement now.
- Test framework and an example test.
- Signature of the code under test, or of the function you want created.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Write failing tests first for these scenarios. Do not write production code except the minimal stub needed to compile.

Scenarios:
[SCENARIO ROWS]

Framework: [JUnit 5 | pytest | Vitest]
Style reference: [EXISTING TEST FILE]
Signature under test: [SIGNATURE]

Rules:
- One behaviour per test, named after the behaviour.
- Assert exact expected values and error types. Never assert only 'no exception' or 'not null'.
- Boundary scenarios use exact boundary values.
- Use no mocks for pure logic. Mock only external boundaries.
- Run the tests and show that each fails for the intended reason (assertion failure, not compile error or missing import).
- Do not implement the behaviour in this step.
Report only test and tool results from commands you actually ran, quoting the relevant output.
```

## Expected AI output

- Test file.
- Failing run output with the failure reasons.
- Mapping of scenario ID to test name.

## Validation steps

- [ ] Each test fails for the right reason.
- [ ] Assertions would catch an inverted condition.
- [ ] No production behaviour was implemented.

## Related skills

- [TDD Engineer](../../skills/tdd-engineer/SKILL.md)
- [Unit Test Engineer](../../skills/unit-test-engineer/SKILL.md)

Back to [Testing prompts](README.md) · [Prompt library](../README.md)
