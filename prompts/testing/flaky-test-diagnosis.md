---
id: flaky-test-diagnosis
title: "Flaky Test Diagnosis"
category: testing
skills: [debugging-specialist, integration-test-engineer]
---

# Flaky Test Diagnosis

## Problem it solves

A test fails intermittently and the team retries instead of fixing.

## When to use

A test passes and fails without code changes.

## Required context

- Test code and failure logs from failing and passing runs.
- How CI runs tests (parallelism, order).

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Diagnose this flaky test. Do not add retries or increase sleeps.

Test: [TEST CODE]
Failure output: [FAILING LOGS]
Passing output: [PASSING LOGS]
CI details: [PARALLEL? RANDOM ORDER? SHARED SERVICES?]

Check each cause class and say which are supported by evidence: shared mutable state or leaked data between tests, test order dependence, time or time-zone dependence, randomness without a seed, concurrency and missing synchronisation, real network or external service, resource leaks and timeouts, unstable ordering of collections.
Propose the cheapest experiments to confirm (for example run alone, run repeated 50 times, randomise order, fix the clock) and give the commands. After confirmation propose the fix that removes the nondeterminism. Do not claim the root cause until an experiment confirms it. Report only test and tool results from commands you actually ran, quoting the relevant output.
```

## Expected AI output

- Ranked causes with evidence.
- Experiments with commands.
- A fix after confirmation.

## Validation steps

- [ ] The failure is reproduced on demand.
- [ ] The fix removes nondeterminism, not just timing.
- [ ] The test passes 50 runs in random order.

## Related skills

- [Debugging Specialist](../../skills/debugging-specialist/SKILL.md)
- [Integration Test Engineer](../../skills/integration-test-engineer/SKILL.md)

Back to [Testing prompts](README.md) · [Prompt library](../README.md)
