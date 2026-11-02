# 05 Missing transaction rollback

**Defect class:** transaction boundary. **Difficulty:** intermediate.

## Scenario

`transfer` debits one account and credits another. It commits after the debit "to save progress". If the credit fails (unknown target), the debit is already committed and the money has disappeared.

## Your task

1. Run the tests and read which scenario loses money.
2. Make the transfer atomic: either both updates are committed, or neither.
3. Decide what should happen for an unknown **source** account, a zero amount and a transfer to oneself, and pin those decisions with tests.

## Suggested AI prompt

[Exception Handling Review](../../../prompts/code_review/exception-handling-review.md): ask the assistant to list "partial updates left without a transaction".

## Hints

<details><summary>Hint 1</summary>

What is the state of the database at the moment `LookupError` is raised?

</details>

<details><summary>Hint 2</summary>

A transaction boundary should wrap the whole business operation, including the checks that depend on what was read.

</details>

## Expected corrections

<details><summary>Spoiler: reference solution notes</summary>

- Use one transaction (`with conn:` in `sqlite3` commits on success and rolls back on exception).
- Read and check the balance inside the same transaction. In a multi-user database also lock the row or use an atomic conditional update to avoid lost updates.
- Reject non-positive amounts and self transfers at the boundary.

</details>

## Verify

```bash
pytest examples/broken_code_lab/05_missing_transaction_rollback
pytest examples/broken_code_lab/05_missing_transaction_rollback --target=solution
```

Related: [Database Design Reviewer](../../../skills/database-design-reviewer/SKILL.md), [handbook chapter 6](../../../handbook/06_defensive_programming/README.md).
