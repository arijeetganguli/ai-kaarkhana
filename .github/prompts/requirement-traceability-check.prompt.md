---
description: "Requirement Traceability Check: A change claims to implement a requirement but nobody has checked that every criterion is implemented and tested."
---
Check traceability between the requirement, the implementation and the tests.

Acceptance criteria:
[PASTE AC LIST]

Diff (code and tests):
[PASTE DIFF]

For each acceptance criterion report: implemented where (file and symbol), tested by (test name), test would fail if the behaviour were removed (YES, NO, UNSURE and why), and status (COVERED, WEAK, MISSING).
Then list: behaviour in the diff that no criterion asks for (scope creep or undocumented rules), and criteria that are implemented but untested.
Cite the file and symbol for every claim you make about the code. Do not mark a criterion COVERED unless you read the test and its assertions.

---
Generated from [prompts/requirements/requirement-traceability-check.md](../../prompts/requirements/requirement-traceability-check.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
