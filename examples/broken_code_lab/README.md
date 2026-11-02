# The Broken Code Lab

Eight deliberately defective implementations. You fix them, with or without an AI assistant, and automated tests tell you whether you really did.

The lab exists to practise the habits that matter when AI writes code: **read the failure, form a hypothesis, understand the defect class, fix the root cause, and prove it with a test**.

| # | Exercise | Defect class | Level |
| --- | --- | --- | --- |
| 01 | [Missing else](01_missing_else/CHALLENGE.md) | Incomplete conditional | Beginner |
| 02 | [Null dereference](02_null_dereference/CHALLENGE.md) | Null and absent values | Beginner |
| 03 | [Boolean condition](03_boolean_condition/CHALLENGE.md) | Operator precedence, wrong connective | Intermediate |
| 04 | [Race condition](04_race_condition/CHALLENGE.md) | Check-then-act race | Advanced |
| 05 | [Missing transaction rollback](05_missing_transaction_rollback/CHALLENGE.md) | Transaction boundary | Intermediate |
| 06 | [Inadequate exception handling](06_inadequate_exception_handling/CHALLENGE.md) | Swallowed errors, lost cause | Intermediate |
| 07 | [SQL injection](07_sql_injection/CHALLENGE.md) | Injection | Beginner |
| 08 | [Missing integration test](08_missing_integration_test/CHALLENGE.md) | Mocks hiding a bug | Intermediate |

## How an exercise works

Each folder contains:

| File | Purpose |
| --- | --- |
| `CHALLENGE.md` | Scenario, task, a suggested AI prompt, hints, and collapsed spoilers. |
| `broken.py` | The defective code. **This is the file you edit.** |
| `test_*.py` | Automated tests. They fail against `broken.py` and pass against a correct fix. |
| `solution.py` | A reference fix. Do not open it first. |

## Run

```bash
python3 -m venv .venv && source .venv/bin/activate && pip install pytest
cd examples/broken_code_lab

pytest 01_missing_else                      # your work: starts red
pytest 01_missing_else --target=solution    # the reference fix: green
pytest                                      # all exercises
```

`--target=solution` points the tests at `solution.py`. CI runs both directions through [`scripts/verify_lab.py`](../../scripts/verify_lab.py): every exercise must be **red** against `broken.py` and **green** against `solution.py`.

## Suggested way to play

1. Read `CHALLENGE.md` down to "Hints", not further.
2. Run the tests. Read the failures. Write down a hypothesis.
3. Try it **without** AI first for one exercise, then with. Compare how long the fix took and how well you understood it.
4. With AI: use the suggested prompt, then *verify the proposed fix yourself*. Ask the assistant why its fix is the root cause.
5. Check your fix against the spoiler notes and the tests of the same folder. Did you handle the cases the requirement is silent about deliberately?

## Ideas for contributors

- Ports of the exercises to Java and TypeScript (keep the same defect and the same tests).
- New defect classes: time zone handling, integer overflow, unbounded retry, resource leak, insecure deserialisation.
- See [CONTRIBUTING.md](../../CONTRIBUTING.md).

Back to [examples](../README.md).
