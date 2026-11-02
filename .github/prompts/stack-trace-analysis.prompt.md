---
description: "Stack Trace Analysis: A stack trace is long and the actual failing frame is not obvious."
---
Analyse this stack trace.

Trace:
[PASTE FULL STACK TRACE]

Source (if available): [FILES]

1. Identify the root exception (deepest cause) and the first frame in our own code.
2. Explain what the code at that frame was doing and which value or state could cause this exception. Cite the file and symbol for every claim you make about the code.
3. List what we cannot determine from the trace alone and what data (logs, inputs, state) would settle it.
4. Give two or three hypotheses with the check for each. Do not propose a fix until one is supported by evidence.
5. Say whether the exception is a symptom of a deeper design problem (for example an unhandled null or a swallowed earlier exception).

---
Generated from [prompts/debugging/stack-trace-analysis.md](../../prompts/debugging/stack-trace-analysis.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
