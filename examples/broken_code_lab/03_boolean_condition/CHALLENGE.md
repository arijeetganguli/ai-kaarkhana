# 03 Incorrect boolean condition

**Defect class:** operator precedence and wrong logical connective. **Difficulty:** intermediate.

## Scenario

A coupon is valid only if **all three** conditions hold. The implementation returns `True` for expired coupons and for coupons below the minimum total, because of how the expression groups.

## Your task

1. Run the tests. The failing parameter combinations form a decision table; read them.
2. Fix the expression so that all 16 combinations match the rule.
3. Make the code read like the rule (names for the three conditions).

## Suggested AI prompt

[Control Flow Review](../../../prompts/code_review/control-flow-review.md). Insist that the assistant **traces the actual outcome per row before comparing with the rule**.

## Hints

<details><summary>Hint 1</summary>

Write the expression with explicit parentheses the way Python groups it: `(a and b) or c or d`. Is that what the rule says?

</details>

## Expected corrections

<details><summary>Spoiler: reference solution notes</summary>

- Replace the mixed `and` / `or` with a conjunction of three named conditions.
- `not (single_use and used)` is the readable form of "not single use, or not used yet".
- Dates are inclusive: a coupon expiring today is valid today.

</details>

## Verify

```bash
pytest examples/broken_code_lab/03_boolean_condition
pytest examples/broken_code_lab/03_boolean_condition --target=solution
```

Related: [Control Flow Analyst](../../../skills/control-flow-analyst/SKILL.md), [Edge Case Hunter](../../../skills/edge-case-hunter/SKILL.md).
