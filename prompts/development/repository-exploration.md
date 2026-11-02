---
id: repository-exploration
title: "Repository Exploration"
category: development
skills: [repository-explorer]
---

# Repository Exploration

## Problem it solves

You must change code you do not know, and the assistant is guessing at structure and conventions.

## When to use

At the start of any task in unfamiliar code, before planning.

## Required context

- The task description.
- Repository access for the assistant.
- Known entry points, if any.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Explore this repository to prepare for the task below. Do not modify any file.

Task:
[TASK]

Known entry points or names (optional):
[CLASS / ENDPOINT / TABLE / EVENT]

Report:
1. Language, build tool, test framework and the exact commands to build and run the tests (run the tests if feasible and report the result).
2. The call path for the task as a table: step | file | symbol | responsibility. Follow it to the data store and external calls.
3. Existing tests for that path, their style, and gaps.
4. Two similar existing features and the conventions they show (validation, error handling, logging, naming).
5. Configuration, feature flags, database objects and contracts touched.
6. Unknowns and anything you could not verify.

Cite the file and symbol for every claim you make about the code. If you did not open a file, do not describe its contents.
```

## Expected AI output

- Tooling and test commands.
- Call path table.
- Test and convention summary.
- Unknowns.

## Validation steps

- [ ] Open three cited files and confirm the claims.
- [ ] The test command works on your machine.
- [ ] Unknowns are real questions, not filler.

## Related skills

- [Repository Explorer](../../skills/repository-explorer/SKILL.md)

Back to [Development prompts](README.md) · [Prompt library](../README.md)
