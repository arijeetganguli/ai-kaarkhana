---
description: "Missing Condition Detection: A branch exists for some cases and silently ignores others."
---
Find missing conditions in this code.

Code: [CODE]
Domain values or state machine: [ENUM VALUES / STATES / TRANSITIONS]

For each if/else chain, switch, match and ternary list: the values or states it handles, the values or states it does not handle (from the domain list above, including null and values added in future), and what the code does for them today (falls through, returns null, returns a default, throws).
For each unhandled case recommend one of: explicit handling with defined behaviour, exhaustive match so the compiler flags new values, rejection with a specific error, or DECISION NEEDED. Explain why simply adding an else block would or would not be correct.
Provide a failing test for each case you recommend handling. Cite the file and symbol for every claim you make about the code.

---
Generated from [prompts/code_review/missing-condition-detection.md](../../prompts/code_review/missing-condition-detection.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
