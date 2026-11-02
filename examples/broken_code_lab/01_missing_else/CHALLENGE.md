# 01 Missing else branch

**Defect class:** incomplete conditional. **Difficulty:** beginner.

## Scenario

`size_class(weight_kg)` classifies parcels. The requirement says: S up to 2 kg, M up to 10 kg, L up to 30 kg, and **parcels over 30 kg are not accepted**. Weights that are not positive numbers are invalid.

## Your task

1. Run `pytest examples/broken_code_lab/01_missing_else` and read the failures.
2. Fix `broken.py` until all tests pass.
3. Decide deliberately what the code should do for every input, including the ones the requirement is silent about.

## Suggested AI prompt

Use [Missing Condition Detection](../../../prompts/code_review/missing-condition-detection.md) on `broken.py`, then ask the assistant to explain why `else: return "XL"` would be wrong before accepting any fix.

## Hints

<details><summary>Hint 1</summary>

What does a Python function return when no branch executes? Where would that value end up?

</details>

<details><summary>Hint 2</summary>

The requirement defines what happens above 30 kg. It does not define a default size class. Do not invent one.

</details>

## Expected corrections

<details><summary>Spoiler: reference solution notes (see solution.py)</summary>

- Reject weights above 30 kg with a specific error that names the limit.
- Reject non-numeric, boolean, zero and negative weights at the boundary.
- Keep the three size boundaries inclusive on the upper side, as the tests pin.
- Do not add a catch-all size class: it would silently ship parcels the service must refuse.

</details>

## Verify

```bash
pytest examples/broken_code_lab/01_missing_else                      # your fix
pytest examples/broken_code_lab/01_missing_else --target=solution    # reference
```

Related: [Defensive Programming Reviewer](../../../skills/defensive-programming-reviewer/SKILL.md), [handbook chapter 6](../../../handbook/06_defensive_programming/README.md).
