---
id: contract-testing
title: "Contract Testing"
category: testing
skills: [api-contract-reviewer, integration-test-engineer]
---

# Contract Testing

## Problem it solves

API changes break consumers because the contract is implicit.

## When to use

Introducing or changing an HTTP API or event schema.

## Required context

- Old and new contract.
- Known consumers.
- Existing tests.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Create contract tests for this API change.

Contract (OpenAPI or schema): [CONTRACT]
Previous contract: [OLD CONTRACT OR 'none']
Consumers: [NAMES AND WHAT THEY RELY ON]

1. Diff old and new contract, classify each change as compatible or breaking and why.
2. For each operation write tests for: success shape, each documented error status and error body, required and optional fields, unknown-field tolerance, and idempotency of unsafe operations that clients may retry.
3. Write at least one test per consumer expectation as a consumer-driven check.
4. State what the tests cannot verify (for example runtime performance or semantics not in the schema).
Do not invent business rules, APIs, fields or behaviour. If something is not specified, write UNSPECIFIED and list it as a question. Report only test and tool results from commands you actually ran, quoting the relevant output.
```

## Expected AI output

- Compatibility classification.
- Contract tests.
- Limits of the checks.

## Validation steps

- [ ] Tests fail when a field is removed or renamed.
- [ ] Breaking changes have a migration plan.
- [ ] Errors are tested, not only success.

## Related skills

- [API Contract Reviewer](../../skills/api-contract-reviewer/SKILL.md)
- [Integration Test Engineer](../../skills/integration-test-engineer/SKILL.md)

Back to [Testing prompts](README.md) · [Prompt library](../README.md)
