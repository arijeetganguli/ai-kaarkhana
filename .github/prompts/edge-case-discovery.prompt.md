---
description: "Edge Case Discovery: Edge cases are discovered in production instead of during design."
---
Discover edge cases for the following. Do not write implementation code.

Requirement or function:
[PASTE REQUIREMENT / SIGNATURE / CODE]

Known rules:
[RULES, RANGES, STATE MACHINE]

Dependencies:
[DATABASES, HTTP SERVICES, QUEUES]

Walk each category and list concrete scenarios, not generic advice: absent data (null, empty, missing, whitespace), boundaries (below, at, above each limit, zero, negative, maximum, overflow, rounding), invalid input (type, format, size, encoding), invalid state (wrong order, repeated action, already completed), dependency failure (error, empty result, timeout, slow, malformed), time and retries (expiry, time zones, duplicates, idempotency), concurrency (double submit, parallel updates), security (permissions, injection, oversized input).

Output a table: ID | category | input or state | expected behaviour | source (requirement ID or UNSPECIFIED) | risk (H/M/L) | test level.
Do not invent business rules, APIs, fields or behaviour. If something is not specified, write UNSPECIFIED and list it as a question. Finish with the five scenarios most likely to be mishandled and why.

---
Generated from [prompts/requirements/edge-case-discovery.md](../../prompts/requirements/edge-case-discovery.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
