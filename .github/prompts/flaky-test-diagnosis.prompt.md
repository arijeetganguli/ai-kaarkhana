---
description: "Flaky Test Diagnosis: A test fails intermittently and the team retries instead of fixing."
---
Diagnose this flaky test. Do not add retries or increase sleeps.

Test: [TEST CODE]
Failure output: [FAILING LOGS]
Passing output: [PASSING LOGS]
CI details: [PARALLEL? RANDOM ORDER? SHARED SERVICES?]

Check each cause class and say which are supported by evidence: shared mutable state or leaked data between tests, test order dependence, time or time-zone dependence, randomness without a seed, concurrency and missing synchronisation, real network or external service, resource leaks and timeouts, unstable ordering of collections.
Propose the cheapest experiments to confirm (for example run alone, run repeated 50 times, randomise order, fix the clock) and give the commands. After confirmation propose the fix that removes the nondeterminism. Do not claim the root cause until an experiment confirms it. Report only test and tool results from commands you actually ran, quoting the relevant output.

---
Generated from [prompts/testing/flaky-test-diagnosis.md](../../prompts/testing/flaky-test-diagnosis.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
