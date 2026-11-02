---
name: integration-test-engineer
description: "Designs and writes integration tests that exercise real boundaries such as database queries, HTTP clients and message handlers, including failure and timeout behaviour. Use when unit tests with mocks cannot prove the integration works."
license: MIT
metadata:
  activity: testing
  difficulty: intermediate
  frameworks: "JUnit 5, pytest, Vitest"
  version: "1.0"
---

# Integration Test Engineer

## Purpose

Prove that components work together against real or realistic dependencies. Catch what mocks hide: wrong SQL, serialisation mismatches, status code handling and timeouts.

## When to invoke

- Code talks to a database, HTTP service, queue or filesystem.
- A bug escaped even though unit tests with mocks were green.
- You are adding or changing a public API or persistence mapping.

## Required input

- The boundary under test and how to run a realistic dependency (in-memory database, local container, stub server).
- Existing integration test conventions and tooling.
- Scenario matrix rows for dependency failure and data variations.

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. Identify the seam: the smallest unit that includes the real boundary code (repository, client, controller).
2. Choose a realistic dependency: real database engine or embedded equivalent, local stub server that speaks real HTTP, test container.
3. Create isolated, repeatable setup and teardown. Each test owns its data.
4. Write the happy path through the real boundary, asserting stored or returned data exactly.
5. Add failure paths: not found, constraint violation, 4xx and 5xx responses, malformed body, timeout, connection refused.
6. Verify side effects: rows written, messages emitted, transaction rollback on failure.
7. Keep them fast and deterministic. Tag them so they can run separately from unit tests.
8. Run them and report results. State what remains untested at the boundary.

## Expected output

- Integration test files with setup, teardown and tagging.
- Instructions to run them locally and in CI.
- List of dependency behaviours covered and not covered.

## Validation checklist

- [ ] The real boundary code runs, not a mock of it.
- [ ] Tests are isolated and can run in any order.
- [ ] Failure and timeout paths are covered, not only success.
- [ ] No dependency on shared external environments.
- [ ] Run time is acceptable and documented.

## Example usage

Input:

> `PriceClient` calls a pricing service over HTTP; unit tests mock the HTTP client.

Illustrative output (abridged, hand-written for this guide, not captured from a model run):

```text
Starts a local stub server. Tests: 200 with valid JSON, 404 -> `PriceNotFound`, 500 -> `PriceServiceUnavailable`, malformed JSON -> `InvalidPriceResponse`, slow response -> timeout error within the configured limit.
```

## Sample prompts

```text
Write integration tests for [CLASS] against a real [database engine | local stub HTTP server]. Cover success, not found, constraint or 5xx errors, malformed responses and timeouts. Isolate data per test, tag the tests as integration, and tell me the command to run them. Report actual results. Code: [CODE]
```

## Common mistakes

- Calling a test with a mocked HTTP client an integration test.
- Using a different database dialect than production without noting the gap.
- Sharing state between tests so that they fail in a different order.
- Testing only success responses.

## Related skills

- [Unit Test Engineer](../unit-test-engineer/SKILL.md)
- [API Contract Reviewer](../api-contract-reviewer/SKILL.md)
- [Database Design Reviewer](../database-design-reviewer/SKILL.md)

## Related resources

Handbook:

- [Chapter 5: Test Driven Development](../../../handbook/05_test_driven_development/README.md)
- [Chapter 6: Defensive Programming and Edge Case Engineering](../../../handbook/06_defensive_programming/README.md)

Prompts:

- [Integration Test Generation](../../../prompts/testing/integration-test-generation.md)
- [Contract Testing](../../../prompts/testing/contract-testing.md)
- [Flaky Test Diagnosis](../../../prompts/testing/flaky-test-diagnosis.md)

Workflows:

- [Write unit and integration tests](../../../workflows/07_unit_and_integration_testing.md)
- [Introduce a new API](../../../workflows/04_new_api.md)
- [Change a database schema](../../../workflows/05_database_schema_change.md)

Examples:

- [examples/python/README.md](../../../examples/python/README.md) scenario S8; [examples/java/README.md](../../../examples/java/README.md) scenario S8
