---
name: mutation-testing-specialist
description: "Uses mutation testing results, or manual mutation reasoning, to find weak or missing assertions and propose tests that kill surviving mutants. Use when tests pass but you doubt they would catch real defects."
license: MIT
metadata:
  activity: testing
  difficulty: advanced
  frameworks: "PIT, Stryker, mutmut"
  version: "1.0"
---

# Mutation Testing Specialist

## Purpose

Measure test effectiveness, not line coverage. Each surviving mutant is a concrete behaviour change that no test notices.

## When to invoke

- Coverage is high but production defects still escape.
- Critical logic (money, access control, eligibility) needs strong tests.
- AI-generated tests look suspiciously easy to pass.

## Required input

- Code under test and its test suite, which must currently pass.
- A mutation tool report if available (PIT for Java, Stryker for TypeScript, mutmut for Python), or willingness to reason manually.
- Scope: files or packages to mutate.

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. Confirm the suite is green before mutating. A failing baseline invalidates results.
2. If a tool is available, run it on the scoped files and collect survived and no-coverage mutants.
3. If not, mutate manually: flip comparison operators (`>` to `>=`), negate conditions, change constants by one, remove statements, swap return values.
4. For each surviving mutant, explain what behaviour changed and why no test noticed.
5. Classify survivors: missing test, weak assertion, equivalent mutant (no observable change), or dead code.
6. Write the smallest test that kills each non-equivalent survivor. Re-run to confirm the mutant is killed.
7. Report the mutation score before and after, and the equivalent mutants left with a justification.

## Expected output

- Surviving mutant table: location, mutation, classification, killing test.
- New or strengthened tests.
- Before and after mutation score, with the tool command used.
- Equivalent mutants and rationale.

## Validation checklist

- [ ] Baseline suite was green.
- [ ] Each killing test was shown failing against the mutant.
- [ ] Equivalent mutants are justified, not dismissed.
- [ ] No production code was changed to make mutants easier to kill without review.
- [ ] Scores quoted come from an actual tool run, not estimation.

## Example usage

Input:

> Test: `assert late_fee(days=5) > 0`. Code: `fee = days * 2`.

Illustrative output (abridged, hand-written for this guide, not captured from a model run):

```text
Mutant: `days * 2` -> `days * 3` survives. The test asserts only `> 0`.
Killing test: `assert late_fee(days=5) == 10`.
Mutant: `if days <= 0` -> `if days < 0` survives. Add `assert late_fee(days=0) == 0`.
```

## Sample prompts

```text
Act as the Mutation Testing Specialist. The tests below pass. Mutate the code manually (operators, constants, removed statements, negated conditions), list which mutants the tests would not detect, and write the smallest additional tests that kill them. Mark equivalent mutants and justify. Code: [CODE]. Tests: [TESTS]
```

## Common mistakes

- Reporting a mutation score without running a tool.
- Writing tests that mirror the implementation so every mutant dies, including legitimate refactors.
- Ignoring equivalent mutants and chasing 100 percent.
- Running mutation testing on the whole repository on every pull request, which is slow.

## Related skills

- [Unit Test Engineer](../unit-test-engineer/SKILL.md)
- [TDD Engineer](../tdd-engineer/SKILL.md)
- [Code Quality Reviewer](../code-quality-reviewer/SKILL.md)

## Related resources

Handbook:

- [Chapter 5: Test Driven Development](../../../handbook/05_test_driven_development/README.md)

Prompts:

- [Mutation Testing Analysis](../../../prompts/testing/mutation-testing.md)
- [Unit Test Generation](../../../prompts/testing/unit-test-generation.md)

Workflows:

- [Write unit and integration tests](../../../workflows/07_unit_and_integration_testing.md)

Examples:

- [examples/python/README.md](../../../examples/python/README.md) scenario S7 (mutation demonstrating weak assertions)
