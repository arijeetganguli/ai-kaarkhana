---
description: "Defensive Coding Pass: Code handles the happy path only and fails unpredictably on missing data, bad input or dependency failure."
---
Review the code below for unhandled cases and propose intentional behaviour for each.

Code:
[CODE]

Error handling convention of this project:
[CONVENTION OR FILE PATH]

For every input, dependency result, conditional, switch and exception handler, list the cases that are not handled: null, empty, wrong type, out of range, unexpected enum value, error, timeout, malformed response, repeated call, concurrent call.
For each, choose one intended behaviour and explain why: reject early with a specific error, safe default (only if the requirement defines it), retry with limit (only if the operation is idempotent), degrade, or fail loudly.
Rules:
- Do not add empty else blocks, catch-all handlers or silent defaults.
- Validate at the boundary, not deep inside.
- If the right behaviour is a business decision, mark it DECISION NEEDED instead of choosing.
- For each handled case write the test that proves it.
Report only test and tool results from commands you actually ran, quoting the relevant output.

---
Generated from [prompts/development/defensive-coding.md](../../prompts/development/defensive-coding.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
