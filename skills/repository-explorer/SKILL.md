---
name: repository-explorer
description: "Builds an evidence-based map of an unfamiliar codebase: structure, entry points, conventions, tests and the code paths relevant to a task. Use before planning or modifying code you do not know well."
license: MIT
metadata:
  activity: planning
  difficulty: beginner
  frameworks: "any"
  version: "1.0"
---

# Repository Explorer

## Purpose

Replace guesswork with a verified map of where the relevant code lives, how it is tested and which conventions to follow, so that later steps change the right files in the right style.

## When to invoke

- You are starting work in a repository or module you have not touched before.
- A change might span several modules and you need the blast radius.
- An AI assistant keeps producing code that does not match local conventions.

## Required input

- The task or question that drives the exploration.
- Read access to the repository, including build files, tests and CI configuration.
- Entry points if known: endpoint, command, event name, class or table.

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. Read the root documentation, build files and CI configuration to find the language, framework, test runner and quality gates.
2. Locate the entry point for the task (route, handler, command, job, event consumer) by searching for names and strings from the task.
3. Follow the call path outward: callers, callees, data access, external calls. Record file and symbol for each hop.
4. Find the existing tests for those files. Note test style, fixtures, naming and how the suite is run.
5. Find similar features and copy their conventions: error handling, logging, validation, naming.
6. List configuration, feature flags, database objects and contracts that the path touches.
7. Record what you could not find or are unsure about. Do not fill gaps with assumptions.

## Expected output

- Tech and tooling summary with the commands to build and run tests.
- Call path table: step, file, symbol, responsibility.
- Existing tests covering the path, and the obvious gaps.
- Conventions to follow, each with a file as evidence.
- Risks and unknowns, including areas with no tests.

## Validation checklist

- [ ] Every claim cites a file path and symbol that was actually read.
- [ ] The test command was identified (and ideally run).
- [ ] At least one comparable existing implementation was found, or its absence is stated.
- [ ] Unknowns are listed rather than guessed.
- [ ] No code was modified.

## Example usage

Input:

> Task: "Add a refund reason to the order cancellation endpoint."

Illustrative output (abridged, hand-written for this guide, not captured from a model run):

```text
Call path: `OrderController.cancel` -> `OrderService.cancel` -> `OrderRepository.markCancelled` -> `orders` table; event `OrderCancelled` published in `OrderEvents`.
Tests: `OrderServiceTest` (JUnit 5 + Mockito), no integration test for `markCancelled`.
Convention: validation via `@Valid` DTOs, errors via `ApiError` (see `ShipmentController`).
Unknown: who consumes `OrderCancelled`. Needs a search of other repositories.
```

## Sample prompts

```text
Use the Repository Explorer skill. Task: [TASK]. Read the code and report the call path, the existing tests, the conventions to follow and the unknowns. Cite file and symbol for every claim. Do not change any file.
```

```text
List every place in this repository that reads or writes [TABLE/EVENT/CONFIG KEY]. For each, give file, symbol and whether a test covers it.
```

## Common mistakes

- Summarising from file names alone without opening the files.
- Stopping at the controller and never reaching data access or external calls.
- Ignoring the tests, then writing tests in a different style.
- Treating a large context dump as understanding. A short, cited map beats a long summary.

## Related skills

- [Implementation Planner](../implementation-planner/SKILL.md)
- [Regression Analyst](../regression-analyst/SKILL.md)
- [Architecture Reviewer](../architecture-reviewer/SKILL.md)

## Related resources

Handbook:

- [Chapter 2: Developer Ways of Working](../../handbook/02_developer_ways_of_working/README.md)
- [Chapter 4: AI Assisted Development](../../handbook/04_ai_assisted_development/README.md)

Prompts:

- [Repository Exploration](../../prompts/development/repository-exploration.md)
- [Dependency Analysis](../../prompts/development/dependency-analysis.md)

Workflows:

- [Build a new feature](../../workflows/01_feature_development.md)
- [Fix a defect](../../workflows/02_defect_fix.md)
- [Refactor an existing service](../../workflows/03_service_refactoring.md)
