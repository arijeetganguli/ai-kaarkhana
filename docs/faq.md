# Frequently asked questions

## About the project

### What is AI Kaarkhana?

An open source handbook and developer toolkit for engineering with AI assistants: twelve handbook chapters, 22 reusable skills, 50 prompts, 10 workflows, runnable examples in Java, Python and TypeScript, and a Broken Code Lab. "Kaarkhana" is Hindi/Urdu for a workshop or factory. The idea is a workshop where engineers build software with AI as one of the tools. See the [repository README](../README.md).

### Is this a tutorial for using a particular AI tool?

No. Skills, prompts and workflows are plain Markdown and do not depend on one vendor. [Adapters](../tools/README.md) copy them into the places that GitHub Copilot, Cursor and Claude Code read, and the generic output works with any assistant that accepts pasted instructions.

### Who is it for?

Developers, engineering leads, architects, QA engineers and engineering managers. The [README](../README.md#start-here) has a reading list for each, and [learning paths](learning_paths.md) cover beginner to advanced.

### Does it claim that AI makes teams faster?

No. The repository makes no productivity claims and quotes no statistics. It is about **quality of outcomes** and **who is accountable**. Where measurement is discussed (see [Chapter 12](../handbook/12_engineering_leadership/README.md)), it tells you how to measure for yourself.

## Using skills and prompts

### What is the difference between a skill, a prompt and a workflow?

| | What it is | Where |
| --- | --- | --- |
| Skill | A reusable capability the assistant loads (purpose, inputs, steps, output, checklist) | [`skills/`](../skills/README.md) |
| Prompt | A ready to paste request for one specific task | [`prompts/`](../prompts/README.md) |
| Workflow | An ordered, gated sequence of skills and prompts for a kind of work | [`workflows/`](../workflows/README.md) |

### Which skill should I use?

Find one by activity, difficulty or framework in the [skill registry](../skills/REGISTRY.md). When unsure, start with [Requirement Analyst](../skills/requirement-analyst/SKILL.md) for new work and [Debugging Specialist](../skills/debugging-specialist/SKILL.md) for defects.

### Do I have to use all 22 skills?

No. Most changes need three or four. The [workflows](../workflows/README.md) show which combination fits which kind of work.

### My assistant does not pick up the skills. What now?

1. Check the folder the tool reads. The [tool adapters](../tools/README.md#what-was-verified-and-when) page lists the locations that were verified, and the date.
2. Check the tool's own documentation: file locations and supported front matter change between versions.
3. As a fallback, open the `SKILL.md` and paste it, or reference it in the chat, together with your task.

### Can I edit a skill for my team?

Yes, it is MIT licensed. Change the skill in your own project's copy. If you are working inside this repository, edit the canonical file in `skills/`, then run `python scripts/sync_adapters.py` and `python scripts/build_registry.py` so generated copies and the registry stay in sync. CI checks both.

### Are the prompts guaranteed to give the expected output?

No. Model output varies. Each prompt page has **Expected AI output** (what a good answer contains) and **Validation steps** (how you check it). Judge an answer against those, not against how confident it sounds.

## Working with AI safely

### Can I paste company code into an assistant?

Only if your organisation's policy allows it for that tool. See [Chapter 9](../handbook/09_security_engineering/README.md#7-sensitive-information-handling) and the [security review prompt](../prompts/code_review/security-review.md). Never paste secrets, credentials or personal data.

### What if the assistant says the tests pass?

Run them yourself. A statement is not evidence. Skills in this repository ask the assistant to report actual command output, and the workflows require you to see the red and green results.

### Who is responsible for AI generated code?

The engineer who commits it, and the reviewers who approve it. See [developer accountability](../handbook/01_ai_native_engineering/README.md#3-developer-accountability).

## Examples and the Broken Code Lab

### The examples have failing tests. Is that a bug?

The example suites are designed to pass. Tests named `initial_defect` assert the defective behaviour of the `initial` code, so they pass and document the problem.

The **Broken Code Lab** is different: tests fail against `broken.py` on purpose, and pass once you fix it (or with `--target=solution`). `python scripts/verify_lab.py` checks that every exercise behaves like that.

### Why Python for the lab, and not Java or TypeScript?

Python keeps the exercises short and the setup minimal. The same defect classes are shown in Java and TypeScript in the [examples](../examples/README.md).

### Do the property-based and mutation testing examples run?

The Hypothesis example in [Chapter 5](../handbook/05_test_driven_development/property_based_and_mutation_testing.md) was run against its mutants, and the recorded outcome is in that page. The fast-check and jqwik snippets are illustrative and were not executed.

## Contributing

### How do I add a skill, prompt, example or chapter?

Follow the [contribution guide](../CONTRIBUTING.md). Templates are in [`templates/`](../templates/README.md), and `python scripts/validate_docs.py` checks structure and links before you open a pull request.

### Can I contribute content produced with AI?

Yes, if you have read, verified and can stand behind it. Disclose AI assistance in the pull request, as the [pull request template](../.github/PULL_REQUEST_TEMPLATE.md) asks.

Back to [documentation index](README.md).
