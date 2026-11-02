---
id: code-generation
title: "Code Generation From a Plan"
category: development
skills: [tdd-engineer, implementation-planner]
---

# Code Generation From a Plan

## Problem it solves

Generated code ignores the plan, over-builds and arrives without evidence that it works.

## When to use

Executing one slice of an approved plan, test first.

## Required context

- The slice from the approved plan.
- Failing test(s) already written, or the scenario to test.
- Style reference file.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
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
```

## Expected AI output

- Failing test with output.
- Minimal change.
- Passing suite output.
- Decisions and limitations.

## Validation steps

- [ ] Run the tests yourself.
- [ ] Diff only touches the listed files.
- [ ] No existing assertion was weakened.
- [ ] You can explain every changed line.

## Related skills

- [TDD Engineer](../../skills/tdd-engineer/SKILL.md)
- [Implementation Planner](../../skills/implementation-planner/SKILL.md)

Back to [Development prompts](README.md) · [Prompt library](../README.md)
