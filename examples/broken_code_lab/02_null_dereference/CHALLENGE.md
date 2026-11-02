# 02 Null dereference

**Defect class:** null and absent value handling. **Difficulty:** beginner.

## Scenario

`format_address(order)` builds a one line shipping address. `line2` is optional. An order with no shipping address is a caller error and must say so clearly. Today it fails with `TypeError` or `AttributeError` somewhere inside the function.

## Your task

1. Run the tests and see which inputs crash.
2. Fix `broken.py` so that optional means optional, required means validated with a message that names the field, and nothing crashes with an unrelated exception.

## Suggested AI prompt

[Null Handling Review](../../../prompts/code_review/null-handling-review.md). Provide the nullability facts from the scenario above, otherwise the assistant will guess which fields are optional.

## Hints

<details><summary>Hint 1</summary>

List every value the function dereferences. For each, is `None` possible according to the scenario?

</details>

<details><summary>Hint 2</summary>

Converting `None` to an empty string is fine for `line2` because the requirement says it is optional. Doing the same for `line1` would hide bad data.

</details>

## Expected corrections

<details><summary>Spoiler: reference solution notes</summary>

- Validate the whole path (`shipping`, `address`) first and fail with `shipping address is required`.
- Validate required fields with their names in the message; treat `line2` as optional and skip it when blank.
- No default values for required fields.

</details>

## Verify

```bash
pytest examples/broken_code_lab/02_null_dereference
pytest examples/broken_code_lab/02_null_dereference --target=solution
```

Related: [Defensive Programming Reviewer](../../../skills/defensive-programming-reviewer/SKILL.md).
