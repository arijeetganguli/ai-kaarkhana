---
name: tdd-engineer
description: "Drives implementation through Red, Green, Refactor cycles: writes one failing test from a scenario, makes it pass with the simplest change, then refactors, reporting actual test results at every step. Use when implementing new behaviour."
license: MIT
metadata:
  activity: testing
  difficulty: intermediate
  frameworks: "JUnit 5, pytest, Vitest"
  version: "1.0"
---

# TDD Engineer

## Purpose

Keep AI-assisted implementation small, specified by tests and verifiably correct, by enforcing the test-first loop and honest evidence of failure and success.

## When to invoke

- Implementing a function, class or endpoint whose behaviour is specified.
- Fixing a defect: first reproduce it as a failing test.
- An AI agent tends to generate large implementations with after-the-fact tests.

## Required input

- Scenario matrix or acceptance criteria with expected behaviours.
- Test framework, run command and an example of existing test style.
- The code under change, if any.

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. Pick the next scenario from the matrix, starting with the simplest behaviour.
2. RED: write one test that expresses the behaviour. Run it. Report the failure output and confirm it fails for the intended reason, not a compile error or missing import.
3. GREEN: write the smallest production change that passes. Run the whole relevant suite and report the result.
4. REFACTOR: improve names and structure without changing behaviour. Run the suite again.
5. Add the next scenario. Do not implement behaviour that no test requires.
6. When scenarios are done, review the tests for weak assertions and add boundary and negative cases from the matrix.
7. Report the final suite result with counts, and list scenarios not covered.

## Expected output

- For each cycle: test name, red output excerpt, change summary, green output excerpt.
- Final test run with command and pass/fail counts.
- Scenario coverage table: scenario ID -> test name.
- Remaining gaps and known limitations.

## Validation checklist

- [ ] Each test was seen failing for the right reason before the change.
- [ ] Test results quoted are from actually executed commands.
- [ ] No production code exists that no test demands.
- [ ] Assertions check behaviour, not just that code ran.
- [ ] Existing tests were not weakened or deleted to make things pass.

## Example usage

Input:

> Scenario SC-02: total of exactly 100.00 ships free.

Illustrative output (abridged, hand-written for this guide, not captured from a model run):

```text
RED: `shipping_is_free_at_threshold` fails: expected 0.00 but was 4.99.
GREEN: change `total > 100` to `total >= 100`. Suite: 6 passed.
REFACTOR: extract `FREE_SHIPPING_THRESHOLD`. Suite: 6 passed.
```

## Sample prompts

```text
Use the TDD Engineer skill with [pytest | JUnit 5 | Vitest]. Implement scenario [ID] from the matrix: write the test, run it and show the failure, make the minimal change, run the suite and show the result, then refactor. One scenario only. Matrix: [MATRIX]. Code: [CODE]
```

## Common mistakes

- Writing all tests and the full implementation in one step and calling it TDD.
- Claiming tests pass without running them.
- A red test that fails because of a typo, so it proves nothing.
- Modifying a failing test to match buggy behaviour.

## Related skills

- [Unit Test Engineer](../unit-test-engineer/SKILL.md)
- [Edge Case Hunter](../edge-case-hunter/SKILL.md)
- [Mutation Testing Specialist](../mutation-testing-specialist/SKILL.md)
- [Refactoring Specialist](../refactoring-specialist/SKILL.md)

## Related resources

Handbook:

- [Chapter 5: Test Driven Development](../../../handbook/05_test_driven_development/README.md)

Prompts:

- [TDD Test Generation](../../../prompts/testing/tdd-test-generation.md)
- [Unit Test Generation](../../../prompts/testing/unit-test-generation.md)
- [Regression Test Generation](../../../prompts/testing/regression-test-generation.md)

Workflows:

- [Build a new feature](../../../workflows/01_feature_development.md)
- [Fix a defect](../../../workflows/02_defect_fix.md)
- [Write unit and integration tests](../../../workflows/07_unit_and_integration_testing.md)

Examples:

- [examples/python/README.md](../../../examples/python/README.md) scenario S6 (TDD from requirement to passing tests)
