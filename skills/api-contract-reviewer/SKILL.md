---
name: api-contract-reviewer
description: "Reviews API and event contracts for correctness, consistency, backward compatibility, error semantics, versioning and testability. Use when introducing or changing an HTTP API, event schema or client library."
license: MIT
metadata:
  activity: architecture
  difficulty: intermediate
  frameworks: "OpenAPI, REST, events"
  version: "1.0"
---

# API Contract Reviewer

## Purpose

Protect consumers. Detect breaking changes, ambiguous semantics and missing error contracts before they ship.

## When to invoke

- Adding or changing an endpoint, event, message schema or SDK.
- Consumers exist that you cannot update simultaneously.
- Writing contract tests or an OpenAPI description.

## Required input

- Old and new contract (OpenAPI document, schema, or code).
- Known consumers and their compatibility expectations.
- Error handling and versioning conventions of the organisation or project.

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. List operations, fields and types in the new contract; diff against the old one.
2. Classify each difference as compatible or breaking (removed or renamed field, type change, new required field, changed semantics, stricter validation, changed status code).
3. Check semantics: HTTP method safety and idempotency, status codes, pagination, filtering, ordering, time zones and formats, null versus absent.
4. Check error model: consistent structure, machine readable codes, no sensitive data in messages.
5. Check security aspects: authentication, authorisation per operation, rate limits, input limits.
6. Check evolution: versioning approach, deprecation path, unknown field tolerance.
7. Define contract tests for each documented behaviour including errors, and consumer-driven checks where relevant.

## Expected output

- Contract diff with compatibility classification.
- Findings: severity, location, issue, recommendation.
- Contract test plan.
- Migration or deprecation plan for breaking changes.

## Validation checklist

- [ ] Every difference between old and new was classified.
- [ ] Error responses are specified, not only success.
- [ ] Idempotency and retries are addressed for unsafe operations.
- [ ] Consumers affected by breaking changes are identified.
- [ ] Contract tests exist or are planned for each rule.

## Example usage

Input:

> Change: `POST /orders` adds required field `deliveryWindow`.

Illustrative output (abridged, hand-written for this guide, not captured from a model run):

```text
Breaking: new required field rejects existing clients. Options: make it optional with a documented default, or introduce `/v2`. Recommend optional with default and a deprecation note.
Contract tests: request without the field -> 201 (compatibility), invalid window -> 422 with `INVALID_DELIVERY_WINDOW`.
```

## Sample prompts

```text
Act as the API Contract Reviewer. Compare old and new contract below. Classify each change as compatible or breaking, review status codes, idempotency, errors, pagination and security, and propose contract tests. Old: [OLD]. New: [NEW]. Known consumers: [CONSUMERS]
```

## Common mistakes

- Treating a new required field as non-breaking.
- Specifying only 200 responses.
- Using 200 for errors with a body flag.
- Changing semantics while keeping the same field names.

## Related skills

- [Integration Test Engineer](../integration-test-engineer/SKILL.md)
- [Security Reviewer](../security-reviewer/SKILL.md)
- [Architecture Reviewer](../architecture-reviewer/SKILL.md)

## Related resources

Handbook:

- [Chapter 8: Architecture and Design](../../handbook/08_architecture_and_design/README.md)

Prompts:

- [API Design Review](../../prompts/architecture/api-design-review.md)
- [Contract Testing](../../prompts/testing/contract-testing.md)

Workflows:

- [Introduce a new API](../../workflows/04_new_api.md)

Examples:

- [examples/typescript/README.md](../../examples/typescript/README.md) scenario S8
