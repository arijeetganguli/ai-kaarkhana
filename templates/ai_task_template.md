# AI task: <one line goal>

> A structured brief for handing a bounded piece of work to an assistant. The more of the gaps you fill in, the less the assistant invents. Paste it into the chat, or save it in the repository next to the work.

## 1. Goal

<One sentence: the outcome, not the method.>

## 2. Context

- **Requirement:** <paste or reference the clarified requirement and scenario IDs>
- **Repository area:** <paths, modules, or "explore first">
- **Existing conventions to follow:** <naming, error handling, test style, with a file to imitate>
- **Versions:** <language, framework and library versions>

## 3. Inputs the assistant may use

- <files, tests, logs, specifications>

## 4. Constraints

- Touch only: <files or directories>
- Do not change: <public APIs, schemas, existing tests>
- Do not add dependencies unless asked.
- Do not invent behaviour. If something is unspecified, list it as a question and stop.
- Follow the repository instructions.

## 5. Skill or method

<Name the skill to apply, for example `tdd-engineer`, or paste its `SKILL.md`.>

## 6. Steps

1. <first step, for example: list the unspecified behaviour as questions>
2. <second step, for example: write the failing test for SC-01 and run it>
3. <third step>

Work one step at a time and report after each.

## 7. Required output

- <e.g. the test, the change summary, and the quoted test output>
- A list of questions and assumptions.
- A list of anything not done.

## 8. Evidence rules

- Quote output only from commands that were actually run, with the command.
- Do not claim a test passed unless it was run.
- Do not weaken, skip or delete an existing test to make something pass.
- Show failing output before the fix.

## 9. Done when

- [ ] <testable completion criterion>
- [ ] Suite passes and the output is shown.
- [ ] Diff contains only what the task requires.

## 10. Notes for the human

- I will review: <what I will read myself>
- Escalate to me if: <situations that need a decision>
