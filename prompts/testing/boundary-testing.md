---
id: boundary-testing
title: "Boundary Testing"
category: testing
skills: [edge-case-hunter, unit-test-engineer]
---

# Boundary Testing

## Problem it solves

Off by one and comparison errors survive because only typical values are tested.

## When to use

Code has limits, thresholds, ranges, dates, sizes or counts.

## Required context

- The limit rules.
- The code.
- Data types involved.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Write boundary tests for the rule below.

Rule: [e.g. 'orders of 100.00 or more ship free']
Code: [CODE]
Types: [INT, DECIMAL, DATE WITH TIMEZONE, ETC.]

For every limit produce tests for: just below, exactly at, just above (use the smallest representable step for the type, for example 99.99/100.00/100.01 or one day), plus zero, negative, minimum and maximum of the type, and rounding or overflow cases where the type allows them.
Each test states the expected value from the rule. If the rule does not say what happens at the limit (inclusive or exclusive), do not guess: list it as UNSPECIFIED and write the test as skipped with that reason.
Run the tests and report results. Name the operator mutation (< to <=) that your tests would detect. Report only test and tool results from commands you actually ran, quoting the relevant output.
```

## Expected AI output

- Boundary tests.
- UNSPECIFIED limits.
- Run output.

## Validation steps

- [ ] Changing < to <= makes a test fail.
- [ ] Inclusive or exclusive limits were confirmed by the owner.
- [ ] Decimal and date types use exact values.

## Related skills

- [Edge Case Hunter](../../skills/edge-case-hunter/SKILL.md)
- [Unit Test Engineer](../../skills/unit-test-engineer/SKILL.md)

Back to [Testing prompts](README.md) · [Prompt library](../README.md)
