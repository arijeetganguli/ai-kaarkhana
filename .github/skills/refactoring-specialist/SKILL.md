---
name: refactoring-specialist
description: "Plans and performs behaviour-preserving refactoring in small, test-protected steps, starting with characterisation tests for untested code. Use when improving structure without changing behaviour."
license: MIT
metadata:
  activity: quality
  difficulty: intermediate
  frameworks: "any"
  version: "1.0"
---

# Refactoring Specialist

## Purpose

Improve design safely. Refactoring changes structure, never behaviour, and proves it with tests at each step.

## When to invoke

- Code is hard to change because of size, nesting, duplication or coupling.
- Before adding a feature to code that resists it.
- AI proposes a large rewrite instead of incremental change.

## Required input

- The code to refactor and the structural problem to solve.
- Existing tests, and the command to run them.
- Constraints: public API compatibility, performance, deadline.

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. Define the structural goal and the non-goals. State that behaviour must not change.
2. Check test protection. If coverage of the behaviour is weak, write characterisation tests that pin current behaviour, including quirks, and record suspicious quirks as questions.
3. Choose small named refactorings (extract function, rename, introduce parameter object, replace conditional with polymorphism, inline) and order them.
4. Apply one refactoring at a time. Run the tests after each step and report results.
5. Keep commits small so each step can be reverted independently.
6. Do not mix behaviour changes or bug fixes into refactoring commits. Log them for separate work.
7. Finish by reviewing the result against the goal and cleaning up dead code.

## Expected output

- Goal, non-goals and risk assessment.
- Characterisation tests added.
- Ordered list of refactorings with test results after each.
- Bugs or quirks discovered, logged separately.

## Validation checklist

- [ ] Tests passed before the first step.
- [ ] Tests passed after every step, with results reported.
- [ ] No behaviour change is hidden in the refactoring.
- [ ] Public API is unchanged, or the change is explicit and reviewed.
- [ ] Steps are small enough to review.

## Example usage

Input:

> `calculatePrice` has 4 nested ifs mixing tier, quantity and promotion logic.

Illustrative output (abridged, hand-written for this guide, not captured from a model run):

```text
1. Characterisation tests for 12 combinations (all pass on current code).
2. Extract `tierDiscount`. Tests: green.
3. Extract `quantityDiscount`. Tests: green.
4. Replace nested ifs by sequential discount application. Tests: green.
Quirk found: promotions apply after tier discount rounding; logged as question, behaviour preserved.
```

## Sample prompts

```text
Act as the Refactoring Specialist. Goal: [GOAL]. Behaviour must not change. First add characterisation tests for the current behaviour, then propose an ordered list of small refactorings. Apply one at a time and show the test run after each. Log any bug you notice instead of fixing it. Code: [CODE]
```

## Common mistakes

- Rewriting whole modules in one step.
- Fixing bugs in the same commit as refactoring.
- Refactoring without running tests between steps.
- Removing tests that cover quirks because they look odd.

## Related skills

- [Code Quality Reviewer](../code-quality-reviewer/SKILL.md)
- [Regression Analyst](../regression-analyst/SKILL.md)
- [TDD Engineer](../tdd-engineer/SKILL.md)

## Related resources

Handbook:

- [Chapter 7: Code Quality](../../../handbook/07_code_quality/README.md)
- [Chapter 4: AI Assisted Development](../../../handbook/04_ai_assisted_development/README.md)

Prompts:

- [Behaviour Preserving Refactoring](../../../prompts/development/refactoring.md)
- [Regression Test Generation](../../../prompts/testing/regression-test-generation.md)

Workflows:

- [Refactor an existing service](../../../workflows/03_service_refactoring.md)

Examples:

- [examples/python/README.md](../../../examples/python/README.md) scenario S9 (refactoring exercise)
