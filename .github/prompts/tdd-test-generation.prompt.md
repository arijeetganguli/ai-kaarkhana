---
description: "TDD Test Generation: Tests written after the code mirror the implementation instead of specifying behaviour."
---
Write failing tests first for these scenarios. Do not write production code except the minimal stub needed to compile.

Scenarios:
[SCENARIO ROWS]

Framework: [JUnit 5 | pytest | Vitest]
Style reference: [EXISTING TEST FILE]
Signature under test: [SIGNATURE]

Rules:
- One behaviour per test, named after the behaviour.
- Assert exact expected values and error types. Never assert only 'no exception' or 'not null'.
- Boundary scenarios use exact boundary values.
- Use no mocks for pure logic. Mock only external boundaries.
- Run the tests and show that each fails for the intended reason (assertion failure, not compile error or missing import).
- Do not implement the behaviour in this step.
Report only test and tool results from commands you actually ran, quoting the relevant output.

---
Generated from [prompts/testing/tdd-test-generation.md](../../prompts/testing/tdd-test-generation.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
