---
name: unit-test-engineer
description: "Designs and writes fast, deterministic unit tests that assert behaviour, cover boundaries and negative cases, and fail when the code is wrong. Use when adding or improving unit tests for existing or new code."
license: MIT
metadata:
  activity: testing
  difficulty: beginner
  frameworks: "JUnit 5, Mockito, pytest, Vitest"
  version: "1.0"
---

# Unit Test Engineer

## Purpose

Produce unit tests that catch defects, not tests that merely execute lines. Strong assertions, minimal mocking and clear naming.

## When to invoke

- Existing code has little or no unit test coverage.
- Tests pass but mutation or review shows weak assertions.
- New code needs tests in the style of the project.

## Required input

- Code under test and its documented behaviour.
- Existing test files for style and fixtures.
- Scenario matrix, if available.

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. Read the code and list its observable behaviours: return values, state changes, thrown errors, calls to collaborators.
2. Name each test after the behaviour, for example `rejects_negative_quantity` rather than `test1`.
3. Structure tests as arrange, act, assert. One behaviour per test.
4. Cover boundaries (below, at, above), negative inputs, empty and null inputs, and each branch.
5. Assert on specific values and error types, never only `is not None` or `no exception`.
6. Mock only true boundaries (network, clock, randomness, database). Prefer real collaborators or fakes for pure logic.
7. Use parameterised tests for input tables. Keep test data minimal and meaningful.
8. Run the tests, report results. Check that at least one assertion would fail if the logic were inverted.

## Expected output

- Test file(s) in the project style.
- Table mapping behaviours and scenarios to tests.
- Executed test run output.
- Behaviours deliberately not tested, with reasons.

## Validation checklist

- [ ] Tests are deterministic: no sleeping, real clock or network.
- [ ] Each assertion checks an exact expected value or error.
- [ ] Boundary values appear on both sides of each limit.
- [ ] Mocks are limited to external boundaries.
- [ ] Deliberately breaking the code (invert a condition) makes a test fail.

## Example usage

Input:

> Function: `discount_for_tier(tier)` returns 0.0, 0.05, 0.10 for BASIC, SILVER, GOLD.

Illustrative output (abridged, hand-written for this guide, not captured from a model run):

```text
Parameterised test: BASIC -> 0.0, SILVER -> 0.05, GOLD -> 0.10 (exact values).
`unknown_tier_is_rejected`: asserts `ValueError` with the tier in the message.
`none_tier_is_rejected`.
Not tested: formatting of the log line (no behaviour contract).
```

## Sample prompts

```text
Write unit tests for the code below using [framework]. Follow the style of [EXISTING TEST FILE]. Cover each branch, boundary values below/at/above each limit, null/empty inputs and error cases. Assert exact values. Mock only [BOUNDARIES]. Run them and report the output. Code: [CODE]
```

```text
Review these tests for weak assertions and missing boundaries. For each weakness show a mutation of the code that the test would not catch, then propose a stronger assertion: [TESTS]
```

## Common mistakes

- Asserting that a mock was called with the arguments the code already passes (tests the implementation, not behaviour).
- Mocking the class under test or pure logic.
- Chasing coverage percentage with assertion-free tests.
- Sharing mutable fixtures across tests.

## Related skills

- [TDD Engineer](../tdd-engineer/SKILL.md)
- [Mutation Testing Specialist](../mutation-testing-specialist/SKILL.md)
- [Integration Test Engineer](../integration-test-engineer/SKILL.md)

## Related resources

Handbook:

- [Chapter 5: Test Driven Development](../../../handbook/05_test_driven_development/README.md)

Prompts:

- [Unit Test Generation](../../../prompts/testing/unit-test-generation.md)
- [Boundary Testing](../../../prompts/testing/boundary-testing.md)
- [Negative Testing](../../../prompts/testing/negative-testing.md)
- [Test Data Builder Design](../../../prompts/testing/test-data-builder-design.md)

Workflows:

- [Write unit and integration tests](../../../workflows/07_unit_and_integration_testing.md)
- [Build a new feature](../../../workflows/01_feature_development.md)

Examples:

- [examples/python/README.md](../../../examples/python/README.md) scenario S7 (weak assertions)
