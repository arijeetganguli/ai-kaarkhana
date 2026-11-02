---
description: "Existing Code Modification: Changing legacy code without understanding its current behaviour causes regressions."
---
I need to change existing code. First protect current behaviour, then change it.

Intended change:
[CHANGE]

Code:
[CODE OR FILE PATHS]

Do the following in order:
1. List the current observable behaviours of this code (inputs, outputs, errors, side effects) and every caller you can find. Cite the file and symbol for every claim you make about the code.
2. Map each behaviour to an existing test. For behaviour with no test, write characterisation tests that pin the current behaviour, including quirks. Run them against the unchanged code and show they pass.
3. Write the failing test for the intended change. Show it failing.
4. Make the smallest change that passes. Run the full relevant suite.
5. List each existing test you changed and why. Changing an existing assertion needs an explicit behaviour change in the requirement.

Do not invent business rules, APIs, fields or behaviour. If something is not specified, write UNSPECIFIED and list it as a question. Report only test and tool results from commands you actually ran, quoting the relevant output.

---
Generated from [prompts/development/existing-code-modification.md](../../prompts/development/existing-code-modification.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
