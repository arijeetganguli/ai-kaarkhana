---
name: control-flow-analyst
description: "Analyses branching logic for missing branches, unreachable code, contradictory conditions, boolean precedence errors, fall-through and off-by-one comparisons by enumerating the condition space. Use on any non-trivial conditional logic."
license: MIT
metadata:
  activity: quality
  difficulty: intermediate
  frameworks: "any"
  version: "1.0"
---

# Control Flow Analyst

## Purpose

Prove that each combination of conditions leads to an intended outcome by enumerating them, rather than reading the code and hoping.

## When to invoke

- Code has nested conditionals, chained `if / else if`, switches or complex boolean expressions.
- A condition was changed and the impact on other branches is unclear.
- A reviewer says "I think this is right" about logic with more than three conditions.

## Required input

- The function or method under analysis.
- The rules the logic is meant to implement (requirement or business rules).
- Type or enum definitions for the inputs.

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. Extract every atomic condition and the variables it reads.
2. Build a decision table of condition combinations. For more than four conditions, use boundaries and equivalence classes and state which you grouped.
3. For each row, trace the code and record the actual outcome.
4. Compare to the intended outcome from the rules. Mark mismatches and rows with no intended outcome.
5. Look for specific defects: missing else, unreachable branch, always true or false condition, precedence mistakes (`a || b && c`), negation errors, `<` versus `<=`, fall-through, enum values not handled.
6. Propose the smallest correction and the test rows that pin the behaviour.

## Expected output

- Condition inventory.
- Decision table with actual versus intended outcome and mismatches highlighted.
- Defects found, each with the smallest fix and a failing test row.
- Unspecified combinations for a decision.

## Validation checklist

- [ ] Every branch appears in at least one table row.
- [ ] Actual outcomes come from tracing the code, not from the intended rules.
- [ ] Boundary conditions (`<`, `<=`, `==`) were checked explicitly.
- [ ] Unspecified combinations are listed as questions.
- [ ] Fixes preserve all rows that were already correct.

## Example usage

Input:

> `allowed = isAdmin || isOwner && !isLocked`

Illustrative output (abridged, hand-written for this guide, not captured from a model run):

```text
Precedence: `&&` binds tighter, so admins bypass `isLocked`. If the rule says locked resources are immutable for everyone, row (admin=T, locked=T) is a mismatch.
Fix: `!isLocked && (isAdmin || isOwner)`. Tests: admin+locked -> denied, owner+locked -> denied, owner+unlocked -> allowed.
```

## Sample prompts

```text
Act as the Control Flow Analyst. Extract every condition in the function below, build a decision table of combinations, trace the actual outcome for each row, and compare to the rules provided. List mismatches, unreachable branches, precedence and boundary defects, and the failing tests that expose each. Rules: [RULES]. Code: [CODE]
```

## Common mistakes

- Reviewing in reading order and missing combinations.
- Using the intended rule as the "actual" result without tracing.
- Skipping equal-to boundaries.
- Rewriting the logic for style instead of correctness.

## Related skills

- [Defensive Programming Reviewer](../defensive-programming-reviewer/SKILL.md)
- [Edge Case Hunter](../edge-case-hunter/SKILL.md)
- [TDD Engineer](../tdd-engineer/SKILL.md)

## Related resources

Handbook:

- [Chapter 6: Defensive Programming and Edge Case Engineering](../../handbook/06_defensive_programming/README.md)

Prompts:

- [Control Flow Review](../../prompts/code_review/control-flow-review.md)
- [Missing Condition Detection](../../prompts/code_review/missing-condition-detection.md)

Workflows:

- [Fix a defect](../../workflows/02_defect_fix.md)
- [Review a pull request](../../workflows/09_pull_request_review.md)

Examples:

- [examples/python/README.md](../../examples/python/README.md) scenario S5 (boolean logic)
