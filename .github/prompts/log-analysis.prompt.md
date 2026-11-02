---
description: "Log Analysis: Logs are voluminous and patterns are missed or hallucinated."
---
Analyse these logs to answer one question.

Question: [E.G. WHY DID REQUESTS FAIL BETWEEN 10:02 AND 10:09?]
Log format: [FIELDS]
Logs (sanitised; no secrets or personal data):
[PASTE LOGS]

1. Group entries by error signature and show counts and first and last occurrence. Count only what is present in the excerpt, and say the excerpt may be incomplete.
2. Build a timeline of the key events and correlate by request or trace ID.
3. Identify the earliest anomaly and what changed immediately before it.
4. List patterns suggested by the data and what additional queries would confirm them. Provide the exact queries for [LOG SYSTEM].
5. Separate observations from hypotheses.
Do not extrapolate beyond the supplied lines.

---
Generated from [prompts/debugging/log-analysis.md](../../prompts/debugging/log-analysis.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
