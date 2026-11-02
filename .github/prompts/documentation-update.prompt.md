---
description: "Documentation Update: Documentation lags the code, or is AI-written with invented behaviour."
---
Update the documentation affected by this change.

Audience: [NEW CONTRIBUTOR | API CONSUMER | OPERATOR]
Diff: [DIFF]
Existing docs: [FILES]

Rules:
- Find every document that mentions changed behaviour, configuration or commands and update or remove outdated statements.
- Verify each statement and command against the code. Run commands where possible and use their real output.
- Include prerequisites, steps, expected result and troubleshooting.
- Mark anything you could not verify as UNVERIFIED instead of guessing defaults or configuration keys.
- Do not add marketing language.
List the documents changed and the statements you verified versus those marked UNVERIFIED.

---
Generated from [prompts/development/documentation-update.md](../../prompts/development/documentation-update.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
