# 07 SQL injection

**Defect class:** injection (OWASP Top 10: Injection). **Difficulty:** beginner.

## Scenario

Both functions build SQL by string concatenation. A name such as `' OR '1'='1` returns every user, `O'Brien` raises a syntax error, and a "numeric" id of `"1 OR 1=1"` deletes everything.

## Your task

1. Run the tests and read each payload that succeeds.
2. Fix both functions at the **root cause**, not by filtering the demo payloads.
3. Decide what to do with an id that is not an integer.

## Suggested AI prompt

[Security Review](../../../prompts/code_review/security-review.md). Then ask: "Would a denylist of quote characters fix this? Why not?"

## Hints

<details><summary>Hint 1</summary>

What is the difference between data and code in a SQL statement, and who decides where one ends?

</details>

## Expected corrections

<details><summary>Spoiler: reference solution notes</summary>

- Parameterised queries (`?` placeholders): the driver keeps data and SQL separate.
- Validate the type of `user_id` at the boundary as defence in depth.
- Do **not** escape quotes manually or filter keywords: that is a denylist and will be bypassed.
- Dynamic identifiers (table or column names) cannot be parameterised; they must come from an allowlist.

</details>

## Verify

```bash
pytest examples/broken_code_lab/07_sql_injection
pytest examples/broken_code_lab/07_sql_injection --target=solution
```

Related: [Security Reviewer](../../../skills/security-reviewer/SKILL.md), [handbook chapter 9](../../../handbook/09_security_engineering/README.md).
