# 08 Missing integration test

**Defect class:** inadequate tests (mocks hide the bug). **Difficulty:** intermediate.

## Scenario

`total_spent_cents` has a unit test with a mocked connection. It is green. The query filters on the wrong column (`id` instead of `customer_id`) and returns `None` for customers without orders. The mock cannot know.

## Your task

1. **Before reading `test_08_missing_integration_test.py`**, write your own integration test with a real in-memory SQLite database that fails against `broken.py`. Use the [Integration Test Generation](../../../prompts/testing/integration-test-generation.md) prompt if you like.
2. Compare with the supplied tests, then fix the query.
3. Explain in one sentence why the unit test could never find this.

## Hints

<details><summary>Hint 1</summary>

Choose test data in which the customer id and the order id are different numbers, and one order is not paid.

</details>

## Expected corrections

<details><summary>Spoiler: reference solution notes</summary>

- Filter on `customer_id`, not `id`.
- Use `COALESCE(SUM(...), 0)` so that "no orders" is `0`, as the docstring promises.
- The integration tests use data that distinguishes the columns (order id 7 belongs to customer 9) and a non paid order.

</details>

## Verify

```bash
pytest examples/broken_code_lab/08_missing_integration_test
pytest examples/broken_code_lab/08_missing_integration_test --target=solution
```

Related: [Integration Test Engineer](../../../skills/integration-test-engineer/SKILL.md), [handbook chapter 5](../../../handbook/05_test_driven_development/README.md).
