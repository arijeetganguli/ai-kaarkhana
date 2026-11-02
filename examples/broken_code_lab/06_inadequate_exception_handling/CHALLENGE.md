# 06 Inadequate exception handling

**Defect class:** bare `except`, swallowed errors, lost cause. **Difficulty:** intermediate.

## Scenario

`load_settings` returns the defaults for **every** failure: a missing file (intended), but also a corrupt file, a wrong type or an unreadable file. A broken deployment config is silently replaced by defaults, and the service runs with the wrong timeout for weeks.

## Your task

1. Read the tests: they separate "missing file" (fine) from the failures that must be reported.
2. Catch only what you can actually handle. Raise a specific error for the rest, with the file name and the original error as the cause.
3. Validate the two numeric settings.

## Suggested AI prompt

[Exception Handling Review](../../../prompts/code_review/exception-handling-review.md). Ask it for a table: which exception types can occur at each line and what the intended behaviour is.

## Hints

<details><summary>Hint 1</summary>

`FileNotFoundError` is one specific thing. What other exceptions can `open` and `json.load` raise?

</details>

<details><summary>Hint 2</summary>

Use `raise NewError(...) from original` so the cause is preserved.

</details>

## Expected corrections

<details><summary>Spoiler: reference solution notes</summary>

- Catch `FileNotFoundError` (use defaults) and `json.JSONDecodeError` (raise `SettingsError` `from` it) only.
- Permission errors and directories propagate: they are not "no file".
- Validate shape and values after loading, with messages naming the file and key.

</details>

## Verify

```bash
pytest examples/broken_code_lab/06_inadequate_exception_handling
pytest examples/broken_code_lab/06_inadequate_exception_handling --target=solution
```

Related: [Defensive Programming Reviewer](../../../skills/defensive-programming-reviewer/SKILL.md).
