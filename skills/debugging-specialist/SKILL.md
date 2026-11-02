---
name: debugging-specialist
description: "Diagnoses defects with a hypothesis-driven method: reproduce, isolate, form falsifiable hypotheses, test them with evidence, fix the root cause with a failing test first. Use for bugs, failing tests and unexpected behaviour."
license: MIT
metadata:
  activity: debugging
  difficulty: intermediate
  frameworks: "any"
  version: "1.0"
---

# Debugging Specialist

## Purpose

Replace trial-and-error edits with a disciplined loop so that the root cause is found, the fix is minimal and the defect cannot silently return.

## When to invoke

- A bug report, failing test, stack trace or incorrect output needs diagnosis.
- An AI assistant has proposed a fix without explaining the cause.
- A fix "worked" but nobody knows why.

## Required input

- Observed behaviour versus expected behaviour.
- Steps, inputs, environment and version that reproduce it, or logs and stack trace.
- Relevant code and recent changes.

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. Write the symptom precisely: input, actual output, expected output, environment.
2. Reproduce it reliably, ideally as an automated failing test. If you cannot reproduce it, say so and list what evidence is missing.
3. List two to four hypotheses, each with a prediction that would prove it false.
4. Test hypotheses with the cheapest evidence first: read the code path, add temporary logging, inspect data, bisect commits, minimise the input.
5. Identify the root cause and distinguish it from the symptom and the trigger.
6. Write or finalise the failing test, make the smallest fix, run the full relevant suite.
7. Check for the same defect pattern elsewhere and add regression tests for neighbouring cases.
8. Remove temporary instrumentation and record the cause in the PR.

## Expected output

- Symptom statement and reproduction.
- Hypotheses with predictions and the evidence that decided each.
- Root cause explanation.
- Failing test, fix and test run results.
- Search for similar defects.

## Validation checklist

- [ ] The defect was reproduced, or the lack of reproduction is stated.
- [ ] The root cause is explained, not just the changed line.
- [ ] A test failed before the fix and passes after.
- [ ] Hypotheses were falsifiable and evidence is recorded.
- [ ] Temporary debugging code was removed.

## Example usage

Input:

> Intermittent `NullPointerException` in `InvoiceService.total` after deploy.

Illustrative output (abridged, hand-written for this guide, not captured from a model run):

```text
H1: `customer.region` is null for imported customers. Prediction: failing rows have null region. Evidence: query shows 312 imported rows with null region -> confirmed.
Root cause: import job skips region; `total()` assumes non-null.
Fix: validate at import and handle absent region explicitly in `total()`. Tests for both. Search for other uses of `region`: 2 found.
```

## Sample prompts

```text
Act as the Debugging Specialist. Symptom: [SYMPTOM]. Evidence: [LOGS/STACK TRACE]. Propose 2-4 hypotheses with a prediction that would falsify each, rank them by cheapest evidence, and tell me what to run or inspect first. Do not propose a fix until the root cause is confirmed. Code: [CODE]
```

## Common mistakes

- Changing code until the symptom disappears.
- Accepting an AI-suggested null check that hides the underlying data problem.
- Fixing without a failing test.
- Leaving debug output or feature toggles in place.

## Related skills

- [Regression Analyst](../regression-analyst/SKILL.md)
- [TDD Engineer](../tdd-engineer/SKILL.md)
- [Performance Analyst](../performance-analyst/SKILL.md)

## Related resources

Handbook:

- [Chapter 4: AI Assisted Development](../../handbook/04_ai_assisted_development/README.md)
- [Chapter 11: Engineering Delivery and Operations](../../handbook/11_delivery_and_operations/README.md)

Prompts:

- [Hypothesis Driven Debugging](../../prompts/debugging/hypothesis-driven-debugging.md)
- [Stack Trace Analysis](../../prompts/debugging/stack-trace-analysis.md)
- [Root Cause Analysis](../../prompts/debugging/root-cause-analysis.md)
- [Log Analysis](../../prompts/debugging/log-analysis.md)

Workflows:

- [Fix a defect](../../workflows/02_defect_fix.md)
- [Handle a production incident](../../workflows/08_production_incident.md)

Examples:

- [examples/broken_code_lab/README.md](../../examples/broken_code_lab/README.md)
