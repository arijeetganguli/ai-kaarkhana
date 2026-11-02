---
description: "Unit Test Generation: Existing code has weak or no unit tests."
---
Write unit tests for the code below.

Code: [CODE]
Framework: [FRAMEWORK]
Style reference: [EXISTING TEST FILE]
Behaviour rules: [RULES OR 'infer from code and mark inferred behaviour']

Requirements:
1. List the observable behaviours first (returns, state changes, errors, collaborator calls).
2. Write one test per behaviour, named after it. Use parameterised tests for tables of inputs.
3. Cover each branch, boundary values below/at/above each limit, null and empty inputs, and each error.
4. Assert exact values. No 'is not None', no 'does not throw' alone.
5. Mock only boundaries (network, clock, randomness, database).
6. If behaviour looks like a bug, write the test for the intended behaviour, mark it and report it instead of pinning the bug.
7. Run the tests and report results. Then name one change to the code that your tests would NOT detect.
Report only test and tool results from commands you actually ran, quoting the relevant output.

---
Generated from [prompts/testing/unit-test-generation.md](../../prompts/testing/unit-test-generation.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
