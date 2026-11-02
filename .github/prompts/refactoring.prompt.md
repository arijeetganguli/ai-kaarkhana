---
description: "Behaviour Preserving Refactoring: Refactoring requests turn into rewrites that change behaviour."
---
Refactor the code below without changing behaviour.

Goal: [WHAT SHOULD BE EASIER AFTER THE REFACTORING]
Public API that must not change: [SIGNATURES]
Code: [CODE OR FILE PATHS]

Process:
1. Run the existing tests and show the result. If coverage of this code is weak, write characterisation tests first, run them and show they pass on the unchanged code.
2. Propose an ordered list of small named refactorings (extract function, rename, introduce parameter object, replace conditional, inline).
3. Apply one refactoring at a time. After each, run the tests and show the result.
4. If you notice a bug or odd behaviour, do not fix it. Log it under "Observations".
5. Stop when the goal is met. Do not add features.

Finish with the list of refactorings, test results after each step, and observations. Report only test and tool results from commands you actually ran, quoting the relevant output.

---
Generated from [prompts/development/refactoring.md](../../prompts/development/refactoring.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
