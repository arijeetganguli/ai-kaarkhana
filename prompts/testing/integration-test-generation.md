---
id: integration-test-generation
title: "Integration Test Generation"
category: testing
skills: [integration-test-engineer]
---

# Integration Test Generation

## Problem it solves

Mocked unit tests pass while the real database query or HTTP call is wrong.

## When to use

Code touches a database, HTTP service, queue or filesystem.

## Required context

- The boundary code.
- How to run a realistic dependency locally.
- Existing integration test setup.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
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
```

## Expected AI output

- Integration tests with setup and teardown.
- Run command.
- Executed results.
- What remains untested at the boundary.

## Validation steps

- [ ] Tests fail if you break the SQL or mapping.
- [ ] They pass in a random order.
- [ ] They do not depend on shared infrastructure.

## Related skills

- [Integration Test Engineer](../../skills/integration-test-engineer/SKILL.md)

Back to [Testing prompts](README.md) · [Prompt library](../README.md)
