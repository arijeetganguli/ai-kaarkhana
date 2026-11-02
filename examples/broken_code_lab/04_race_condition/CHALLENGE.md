# 04 Race condition

**Defect class:** check-then-act race (time-of-check to time-of-use). **Difficulty:** advanced.

## Scenario

`Inventory.reserve` checks the stock, then updates it. Between the two steps (a database round trip in real life, a `sleep` here) other threads pass the same check. Fifty threads race for ten units and the shop oversells.

## Your task

1. Run the tests. Note that the failure shows the symptom (negative stock), not the cause.
2. Make the check and the update one atomic step.
3. Keep the code correct for a request of more than one unit.

## Suggested AI prompt

[Hypothesis Driven Debugging](../../../prompts/debugging/hypothesis-driven-debugging.md). Ask for the interleaving of two threads that produces the failure before asking for a fix.

## Hints

<details><summary>Hint 1</summary>

Draw two threads on a timeline. Both read `stock = 1` before either writes.

</details>

<details><summary>Hint 2</summary>

The fix must cover *both* the check and the update. A lock around only the update does not help. In a real system the same problem needs an atomic database statement or optimistic locking, not an in-process lock.

</details>

## Expected corrections

<details><summary>Spoiler: reference solution notes</summary>

- A `threading.Lock` held across check and update.
- Validate `qty >= 1` at the boundary.
- Note the limit: an in-process lock protects one process only. With several instances use `UPDATE ... SET stock = stock - :qty WHERE stock >= :qty` and check the affected row count.

</details>

## Verify

```bash
pytest examples/broken_code_lab/04_race_condition
pytest examples/broken_code_lab/04_race_condition --target=solution
```

Related: [Defensive Programming Reviewer](../../../skills/defensive-programming-reviewer/SKILL.md), [handbook chapter 6](../../../handbook/06_defensive_programming/README.md).
