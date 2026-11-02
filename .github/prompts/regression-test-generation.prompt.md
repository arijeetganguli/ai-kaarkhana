---
description: "Regression Test Generation: A fixed bug returns, or changed code silently alters behaviour."
---
Create regression tests.

Mode: [DEFECT FIX | CHARACTERISATION BEFORE CHANGE]
Defect description or code to be changed: [TEXT / CODE]
Fix (if any): [DIFF]

For a defect fix: write the smallest test that reproduces the original defect; run it against the code before the fix (use git stash or checkout of the previous commit) and show it fails; run it with the fix and show it passes. Then add tests for two neighbouring inputs that share the root cause.
For characterisation: write tests that pin current behaviour for each branch and caller-visible output, run them on the unchanged code and show they pass. Mark behaviours that look wrong with SUSPECT.
Report only test and tool results from commands you actually ran, quoting the relevant output.

---
Generated from [prompts/testing/regression-test-generation.md](../../prompts/testing/regression-test-generation.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
