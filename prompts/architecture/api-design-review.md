---
id: api-design-review
title: "API Design Review"
category: architecture
skills: [api-contract-reviewer]
---

# API Design Review

## Problem it solves

APIs are designed from the implementation outward and break consumers over time.

## When to use

Designing or changing an HTTP or event API.

## Required context

- Proposed API description.
- Consumers.
- Conventions.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Review this API design.

API (OpenAPI, examples or description): [API]
Consumers and constraints: [CONSUMERS]
Organisation conventions: [CONVENTIONS]

Check and report findings with severity: resource and naming consistency; HTTP method semantics, safety and idempotency (including idempotency keys for retried POSTs); status codes and a consistent machine-readable error model; pagination, filtering and ordering; field types and formats (money, time with zone, identifiers); null versus absent; versioning and deprecation; authentication and per-operation authorisation; rate limiting and input size limits; backwards compatibility and unknown field handling.
Then propose contract tests for each rule. Do not invent business rules, APIs, fields or behaviour. If something is not specified, write UNSPECIFIED and list it as a question.
```

## Expected AI output

- Findings by severity.
- Recommended changes.
- Contract test list.

## Validation steps

- [ ] Examples validate against the schema.
- [ ] Consumers reviewed breaking changes.
- [ ] Errors specified for every operation.

## Related skills

- [API Contract Reviewer](../../skills/api-contract-reviewer/SKILL.md)

Back to [Architecture prompts](README.md) · [Prompt library](../README.md)
