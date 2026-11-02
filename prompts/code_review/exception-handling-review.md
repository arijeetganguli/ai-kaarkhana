---
id: exception-handling-review
title: "Exception Handling Review"
category: code_review
skills: [defensive-programming-reviewer]
---

# Exception Handling Review

## Problem it solves

Exceptions are swallowed, over-caught or lose context, so failures are invisible or mishandled.

## When to use

Reviewing try/catch blocks, error returns, retries and resource cleanup.

## Required context

- Code.
- Error handling convention.
- Transaction and resource boundaries.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Review exception and error handling.

Code: [CODE]
Convention (error types, logging, translation at boundaries): [CONVENTION]

For each try/catch, error return and retry report:
- What can fail inside it, and what the handler does.
- Problems: swallowed exception, catch of overly broad type, lost cause or stack trace, logging and rethrowing (duplicate noise), error converted to success, partial updates left without transaction or compensation, resources not released on error paths, retry of non idempotent operations, retry without limit or backoff, sensitive data in messages.
- The intended behaviour: propagate, translate to a domain error, retry (with limit and idempotency), compensate, or fail the whole operation. Explain why.
Provide tests that trigger each failure (inject the fault) and assert the exact outcome including side effects.
Cite the file and symbol for every claim you make about the code.
```

## Expected AI output

- Per-handler analysis.
- Recommended behaviour.
- Fault injection tests.

## Validation steps

- [ ] Each test fails against the original handler.
- [ ] No broad catch remains without a reason.
- [ ] Cleanup verified on the error path.

## Related skills

- [Defensive Programming Reviewer](../../skills/defensive-programming-reviewer/SKILL.md)

Back to [Code review prompts](README.md) · [Prompt library](../README.md)
