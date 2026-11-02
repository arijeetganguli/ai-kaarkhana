---
description: "Contract Testing: API changes break consumers because the contract is implicit."
---
Create contract tests for this API change.

Contract (OpenAPI or schema): [CONTRACT]
Previous contract: [OLD CONTRACT OR 'none']
Consumers: [NAMES AND WHAT THEY RELY ON]

1. Diff old and new contract, classify each change as compatible or breaking and why.
2. For each operation write tests for: success shape, each documented error status and error body, required and optional fields, unknown-field tolerance, and idempotency of unsafe operations that clients may retry.
3. Write at least one test per consumer expectation as a consumer-driven check.
4. State what the tests cannot verify (for example runtime performance or semantics not in the schema).
Do not invent business rules, APIs, fields or behaviour. If something is not specified, write UNSPECIFIED and list it as a question. Report only test and tool results from commands you actually ran, quoting the relevant output.

---
Generated from [prompts/testing/contract-testing.md](../../prompts/testing/contract-testing.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
