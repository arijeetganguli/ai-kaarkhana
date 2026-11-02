# Getting started

You can get value from AI Kaarkhana in ten minutes, without installing anything: read one skill, paste one prompt into the assistant you already use, and check the result against the validation steps. This page shows that path first, then the deeper ones.

## Path 1: Ten minutes, no setup

1. Pick a task you are about to do. For example: "add a discount rule to the order service".
2. Open the matching prompt in the [prompt library](../prompts/README.md). For a new requirement start with [Requirement clarification](../prompts/requirements/requirement-clarification.md).
3. Copy the text inside the `Prompt` section, fill in the `[BRACKETED PLACEHOLDERS]` with your real context, and paste it into your assistant.
4. Compare the answer with the **Expected AI output** and **Validation steps** at the bottom of the prompt page. If the answer does not satisfy them, ask again or fix it yourself.
5. Keep the useful parts, and decide yourself what to do next. The assistant proposes; you are accountable.

## Path 2: Use the skills in your assistant

A **skill** is a folder with a `SKILL.md` that your assistant can load when the task matches its description. The 22 skills in [`skills/`](../skills/README.md) follow the open Agent Skills file format (a `SKILL.md` with `name` and `description` front matter), so several assistants can load them.

Install them into one of your own projects:

```bash
git clone <this-repository-url> ai-kaarkhana
cd ai-kaarkhana
python scripts/sync_adapters.py install --target github-copilot --dest ../my-project --prompts
python scripts/sync_adapters.py install --target cursor         --dest ../my-project
python scripts/sync_adapters.py install --target claude-code    --dest ../my-project
python scripts/sync_adapters.py install --target generic        --dest ../my-project
```

Run only the line for the tool you use. Each target writes to the folder that tool reads, plus a short block of engineering principles in that tool's instruction file. Details and the date on which each tool's conventions were last checked are in [Tool adapters](../tools/README.md). Tool conventions change; if something does not load, check your tool's current documentation.

Then ask for a skill by name or by task:

```text
Use the requirement-analyst skill on this ticket before we write any code:
<paste the ticket>
```

## Path 3: Learn the method

Read the [handbook](../handbook/README.md) in order, or use a [learning path](learning_paths.md) matched to your experience. The chapters build on each other:

1. Why AI changes engineering, and what stays the same (Chapters 1 and 2).
2. How to turn a vague request into a testable specification (Chapter 3).
3. How to direct an assistant and verify what it produces (Chapters 4 and 5).
4. How to make code robust, reviewable, secure and shippable (Chapters 6 to 11).
5. How to lead a team through adoption (Chapter 12).

## Path 4: Run the examples

The [examples](../examples/README.md) show nine scenarios in three languages. Every example has an `initial` version with a real defect, tests that expose it, and an `improved` version with tests that pass.

| Language | Prerequisites | Commands, from the folder shown |
| --- | --- | --- |
| Python | Python 3.10 or newer, `pytest` | `cd examples/python`, then `python -m pip install pytest`, then `python -m pytest` |
| Java | JDK 17 or newer, Maven | `cd examples/java`, then `mvn test` |
| TypeScript | Node.js 20 or newer | `cd examples/typescript`, then `npm install`, then `npm test` |

All example tests are expected to pass. Tests marked `initial_defect` assert the *defective* behaviour of the `initial` code on purpose, so that the defect is documented and cannot silently change. See each language's README for the layout.

## Path 5: Practise on broken code

The [Broken Code Lab](../examples/broken_code_lab/README.md) has eight defective programs. Each one comes with failing tests, a challenge and a suggested prompt. Fix the code (with or without an assistant) until the tests pass, then compare with `solution.py`.

```bash
cd examples/broken_code_lab
python -m pip install pytest
python -m pytest 01_missing_else            # red: the defect is exposed
python -m pytest 01_missing_else --target=solution   # green: the reference fix
```

## Your first real workflow

Take the [feature development workflow](../workflows/01_feature_development.md) and apply it to one small change:

1. Clarify the requirement with [Requirement Analyst](../skills/requirement-analyst/SKILL.md).
2. List edge cases with [Edge Case Hunter](../skills/edge-case-hunter/SKILL.md) and record them in a [scenario matrix](../templates/scenario_matrix_template.md).
3. Plan with [Implementation Planner](../skills/implementation-planner/SKILL.md).
4. Implement test first with [TDD Engineer](../skills/tdd-engineer/SKILL.md).
5. Review with [PR Readiness Reviewer](../skills/pr-readiness-reviewer/SKILL.md) and the [AI code review checklist](../templates/ai_code_review_checklist.md).

At each step, run the tests yourself. Treat an assistant's statement that "all tests pass" as a claim, not as evidence.

## Where to go next

- Need vocabulary? See the [glossary](glossary.md).
- Have a question? See the [FAQ](faq.md).
- Want to know where your team stands? Use the [maturity assessment](maturity_assessment.md).
- Want to help? Read the [contribution guide](../CONTRIBUTING.md).

Back to the [repository README](../README.md).
