---
description: "Exception Handling Review: Exceptions are swallowed, over-caught or lose context, so failures are invisible or mishandled."
---
Review exception and error handling.

Code: [CODE]
Convention (error types, logging, translation at boundaries): [CONVENTION]

For each try/catch, error return and retry report:
- What can fail inside it, and what the handler does.
- Problems: swallowed exception, catch of overly broad type, lost cause or stack trace, logging and rethrowing (duplicate noise), error converted to success, partial updates left without transaction or compensation, resources not released on error paths, retry of non idempotent operations, retry without limit or backoff, sensitive data in messages.
- The intended behaviour: propagate, translate to a domain error, retry (with limit and idempotency), compensate, or fail the whole operation. Explain why.
Provide tests that trigger each failure (inject the fault) and assert the exact outcome including side effects.
Cite the file and symbol for every claim you make about the code.

---
Generated from [prompts/code_review/exception-handling-review.md](../../prompts/code_review/exception-handling-review.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
