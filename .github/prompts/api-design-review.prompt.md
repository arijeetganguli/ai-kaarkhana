---
description: "API Design Review: APIs are designed from the implementation outward and break consumers over time."
---
Review this API design.

API (OpenAPI, examples or description): [API]
Consumers and constraints: [CONSUMERS]
Organisation conventions: [CONVENTIONS]

Check and report findings with severity: resource and naming consistency; HTTP method semantics, safety and idempotency (including idempotency keys for retried POSTs); status codes and a consistent machine-readable error model; pagination, filtering and ordering; field types and formats (money, time with zone, identifiers); null versus absent; versioning and deprecation; authentication and per-operation authorisation; rate limiting and input size limits; backwards compatibility and unknown field handling.
Then propose contract tests for each rule. Do not invent business rules, APIs, fields or behaviour. If something is not specified, write UNSPECIFIED and list it as a question.

---
Generated from [prompts/architecture/api-design-review.md](../../prompts/architecture/api-design-review.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
