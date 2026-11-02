---
description: "Hypothesis Driven Debugging: Trial-and-error fixing hides the root cause."
---
Help me debug using hypotheses. Do not propose a fix yet.

Symptom: [ACTUAL vs EXPECTED]
Reproduction or evidence: [STEPS / LOGS / STACK TRACE]
Relevant code: [CODE]
Recent changes: [COMMITS OR DEPLOYS]

1. Restate the symptom precisely.
2. Give 2 to 4 hypotheses. For each: the mechanism, a prediction that would prove it false, and the cheapest check.
3. Rank by likelihood and cost of checking.
4. Tell me what to run or inspect first. After I report the result, update the ranking.
5. When one hypothesis survives, state the root cause, how it differs from the trigger and the symptom, and propose a failing test that reproduces it.
Cite the file and symbol for every claim you make about the code.

---
Generated from [prompts/debugging/hypothesis-driven-debugging.md](../../prompts/debugging/hypothesis-driven-debugging.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
