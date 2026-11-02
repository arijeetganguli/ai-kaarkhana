---
description: "Boundary Testing: Off by one and comparison errors survive because only typical values are tested."
---
Write boundary tests for the rule below.

Rule: [e.g. 'orders of 100.00 or more ship free']
Code: [CODE]
Types: [INT, DECIMAL, DATE WITH TIMEZONE, ETC.]

For every limit produce tests for: just below, exactly at, just above (use the smallest representable step for the type, for example 99.99/100.00/100.01 or one day), plus zero, negative, minimum and maximum of the type, and rounding or overflow cases where the type allows them.
Each test states the expected value from the rule. If the rule does not say what happens at the limit (inclusive or exclusive), do not guess: list it as UNSPECIFIED and write the test as skipped with that reason.
Run the tests and report results. Name the operator mutation (< to <=) that your tests would detect. Report only test and tool results from commands you actually ran, quoting the relevant output.

---
Generated from [prompts/testing/boundary-testing.md](../../prompts/testing/boundary-testing.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
