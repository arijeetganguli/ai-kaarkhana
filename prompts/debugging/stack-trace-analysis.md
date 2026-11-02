---
id: stack-trace-analysis
title: "Stack Trace Analysis"
category: debugging
skills: [debugging-specialist]
---

# Stack Trace Analysis

## Problem it solves

A stack trace is long and the actual failing frame is not obvious.

## When to use

An exception or crash with a trace.

## Required context

- Full stack trace including 'caused by' chains.
- Source of the relevant frames.
- Version or commit.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Analyse this stack trace.

Trace:
[PASTE FULL STACK TRACE]

Source (if available): [FILES]

1. Identify the root exception (deepest cause) and the first frame in our own code.
2. Explain what the code at that frame was doing and which value or state could cause this exception. Cite the file and symbol for every claim you make about the code.
3. List what we cannot determine from the trace alone and what data (logs, inputs, state) would settle it.
4. Give two or three hypotheses with the check for each. Do not propose a fix until one is supported by evidence.
5. Say whether the exception is a symptom of a deeper design problem (for example an unhandled null or a swallowed earlier exception).
```

## Expected AI output

- Root exception and first own frame.
- Explanation tied to code.
- Hypotheses with checks.

## Validation steps

- [ ] Open the cited frame.
- [ ] Reproduce with the suspected input.
- [ ] Confirm no earlier swallowed exception exists.

## Related skills

- [Debugging Specialist](../../skills/debugging-specialist/SKILL.md)

Back to [Debugging and operations prompts](README.md) · [Prompt library](../README.md)
