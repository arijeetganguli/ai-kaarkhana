---
id: edge-case-discovery
title: "Edge Case Discovery"
category: requirements
skills: [edge-case-hunter]
---

# Edge Case Discovery

## Problem it solves

Edge cases are discovered in production instead of during design.

## When to use

Before writing tests for a function, endpoint or feature.

## Required context

- Requirement or function signature.
- Known rules and ranges.
- Dependencies the code calls.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
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
```

## Expected AI output

- A scenario table with IDs and risk.
- UNSPECIFIED behaviours as questions.
- Top five risky scenarios.

## Validation steps

- [ ] All eight categories are addressed or explicitly skipped with a reason.
- [ ] Boundary values are exact numbers.
- [ ] Expected behaviour is sourced or UNSPECIFIED.
- [ ] Scenarios are concrete enough to become test names.

## Related skills

- [Edge Case Hunter](../../skills/edge-case-hunter/SKILL.md)

Back to [Requirements prompts](README.md) · [Prompt library](../README.md)
