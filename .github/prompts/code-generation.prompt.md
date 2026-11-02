---
description: "Code Generation From a Plan: Generated code ignores the plan, over-builds and arrives without evidence that it works."
---
Implement exactly one slice of the plan using TDD.

Slice:
[SLICE FROM PLAN]

Style reference (follow its conventions):
[REFERENCE FILE]

Steps:
1. Write the failing test(s) for this slice. Run them and show the failure. Confirm it fails for the intended reason.
2. Write the minimal production code to pass. Do not add behaviour no test requires.
3. Run the relevant test suite and show the result.
4. Refactor only if it improves clarity without changing behaviour. Run the suite again.

Constraints:
- Touch only the files listed in the slice.
- Handle null, empty and invalid input at the boundary according to the existing convention. Do not add catch-all exception handlers.
- Do not delete or weaken existing tests.
- Do not invent business rules, APIs, fields or behaviour. If something is not specified, write UNSPECIFIED and list it as a question.

Finish with: files changed, design decisions and why, known limitations, and the final test output. Report only test and tool results from commands you actually ran, quoting the relevant output.

---
Generated from [prompts/development/code-generation.md](../../prompts/development/code-generation.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
