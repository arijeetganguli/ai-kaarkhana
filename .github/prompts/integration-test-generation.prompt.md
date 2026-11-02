---
description: "Integration Test Generation: Mocked unit tests pass while the real database query or HTTP call is wrong."
---
Write integration tests for the boundary code below using a real dependency, not a mock of the boundary.

Code: [CODE]
Dependency: [DATABASE ENGINE | LOCAL STUB HTTP SERVER | TEST CONTAINER]
Framework and conventions: [FRAMEWORK, TAGGING]

Cover:
- Success path with exact stored or returned data.
- Not found, constraint violation, or 4xx and 5xx responses.
- Malformed responses or unexpected schema.
- Timeout or connection failure with the configured limit.
- Transaction behaviour: partial failure leaves no partial data.
Rules: each test owns and cleans its data; tests run in any order; tag them as integration; no shared external environment.
Tell me the command to run them locally and in CI, run them, and report results. Report only test and tool results from commands you actually ran, quoting the relevant output.

---
Generated from [prompts/testing/integration-test-generation.md](../../prompts/testing/integration-test-generation.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
