---
description: "Negative Testing: Only success paths are tested, so invalid input behaviour is accidental."
---
Write negative tests for the code below.

Code: [CODE]
Contract and error conventions: [CONTRACT / ERROR TYPES]

Cover: null, empty and whitespace values; wrong types or formats; out of range numbers; oversized input; invalid state transitions (for example shipping a cancelled order); repeated calls; unauthorised callers; dependency errors.
For each, assert the exact error type and message or status, and assert that no side effect occurred (nothing stored, nothing sent).
If the contract does not define the expected error, list UNSPECIFIED and ask. Do not invent error types.
Run the tests and report results. Report only test and tool results from commands you actually ran, quoting the relevant output.

---
Generated from [prompts/testing/negative-testing.md](../../prompts/testing/negative-testing.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
