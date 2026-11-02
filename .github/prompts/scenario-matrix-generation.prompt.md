---
description: "Scenario Matrix Generation: Tests are written ad hoc, so nobody can say which requirements are covered."
---
Create a scenario matrix that links requirements to tests.

Acceptance criteria:
[PASTE AC LIST]

Edge cases:
[PASTE EDGE CASES]

Output a Markdown table with columns: Scenario ID (SC-n) | REQ ID | AC ID | Category | Given (state and inputs) | When | Expected result | Test level | Proposed test name | Priority.
Rules:
- Every AC has at least one scenario; every scenario traces to an AC or to an edge case marked as derived.
- Boundary scenarios use exact values.
- Test names describe behaviour, for example ships_free_when_total_equals_threshold.
- Mark scenarios whose expected result is UNSPECIFIED and do not propose a test name for them yet.
- Do not invent business rules, APIs, fields or behaviour. If something is not specified, write UNSPECIFIED and list it as a question.

After the table list: ACs with no scenario, scenarios with no AC, and the scenarios you recommend automating first.

---
Generated from [prompts/requirements/scenario-matrix-generation.md](../../prompts/requirements/scenario-matrix-generation.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
