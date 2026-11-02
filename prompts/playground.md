# Prompt playground

A place to practise turning a vague prompt into a specific one. Every pair below shows a **weak prompt**, a **strong prompt**, and **why the strong one works**. No model output is shown here: responses vary by model, version and context, so any output printed in a guide like this would be invented. Run the prompts yourself against your own assistant and compare.

> The prompts here are **illustrative teaching material**. The maintained, tested prompts are in the [prompt library](README.md).

## The anatomy of a strong prompt

| Part | Question it answers | Example |
| --- | --- | --- |
| **Role and skill** | Which discipline should the assistant apply? | "Apply the TDD Engineer skill." |
| **Context** | What does it need to know that it cannot see? | Requirement, scenario IDs, versions, conventions, a file to imitate |
| **Task** | What exactly should it do, and how much? | "Implement scenario SC-03 only." |
| **Constraints** | What must it not do? | "Do not edit existing tests. No new dependencies. Do not invent defaults." |
| **Unknowns rule** | What if information is missing? | "List unspecified behaviour as questions. Do not guess." |
| **Output format** | What shape should the answer take? | "A table: ID, input, expected, source." |
| **Evidence rule** | How will claims be checked? | "Quote output only from commands you ran." |

Not every prompt needs every part. A prompt that asks the assistant to do something consequential (change code, claim tests pass, review security) needs all of them.

## Pair 1: Implementing a rule

**Weak**

```text
Write a function to calculate the shipping fee.
```

**Strong**

```text
Implement the shipping fee rule below in Python 3.12 using pytest, following the style of tests/test_pricing.py.

Rule (REQ-12, confirmed by the product owner):
- Domestic (country "DE") orders of 100.00 EUR or more ship free.
- Domestic orders under 100.00 EUR pay 4.99 EUR.
- All other countries pay 14.99 EUR regardless of total.
Money is integer cents. Negative totals and unknown country formats are invalid.

Do this in order, one scenario at a time:
1. Write a failing test for "domestic, exactly 10000 cents". Run it and show the failure output.
2. Make the smallest change that passes. Run the suite and show the output.
3. Repeat for: 9999, 10001, non domestic, negative total.
If the rule does not say what to do for a case, list it as a question and stop. Do not invent a default.
Do not modify existing tests. Report only output from commands you actually ran.
```

**Why it works:** concrete rule with boundaries and units, a test-first order with evidence, an explicit rule for unknowns, and a scope limit. The weak prompt leaves the boundary, currency handling and invalid input for the assistant to guess.

## Pair 2: Generating tests

**Weak**

```text
Write unit tests for this class.
```

**Strong**

```text
Write unit tests for the `LateFee` class below using JUnit 5.

Requirement (not derived from the code): 3 grace days, then 50 cents per day beyond the grace period, capped at 2000 cents.

Rules for the tests:
- Expected values come from the requirement, written as literals, not recomputed with the same formula as the code.
- Boundaries: 0, 3 (last free day), 4 (first charged day), the day the cap is first reached, one more, and a very large value.
- Negative days: ask me what is intended; do not assume.
- Assert exact values. No assertions that only check "greater than zero" or "no exception".
After writing them, name three one-character changes to the implementation that your tests would catch, and show that they do by running the tests against each change.
```

**Why it works:** it separates the requirement from the implementation (avoiding mirror tests), forces boundary thinking, bans weak assertions and asks the assistant to prove strength. See the runnable demonstration in [scenario S7](../examples/scenarios.md#s7-weak-assertions-and-mutation-testing).

## Pair 3: Reviewing code

**Weak**

```text
Review this code and tell me if it looks good.
```

**Strong**

```text
You are reviewing a change you did not write. The requirement is below. Find defects; do not summarise or praise.

Requirement: [REQUIREMENT]
Diff: [DIFF]

Report each finding as: severity (blocker, major, minor), file and line, what is wrong, the input that triggers it, and the consequence. Only report a finding if you can point to the line and a triggering input; otherwise list it under "questions".
Check specifically for: unhandled values in conditionals, null and empty input, comparison operators at boundaries, boolean precedence, swallowed exceptions, missing timeouts, resources not closed on error paths, and tests with weak or missing assertions.
End with the list of things you did not check.
```

**Why it works:** it asks for defects instead of approval (which avoids confirmation bias), demands evidence for every finding, targets known defect classes and makes the limits of the review explicit. Full version: [Independent code review](code_review/independent-code-review.md).

## Pair 4: Debugging

**Weak**

```text
Why is this throwing an exception? Fix it.
```

**Strong**

```text
Help me find the root cause. Do not propose a fix yet.

Symptom: [WHAT HAPPENS, EXPECTED VS ACTUAL, SINCE WHEN]
Stack trace: [TRACE, secrets and personal data removed]
Recent changes: [DEPLOYS, CONFIG, FLAGS]

1. List the three most likely hypotheses, each with one cheap test that would confirm or reject it.
2. State what evidence I should collect first and the exact command or query.
3. For each hypothesis, say what result would make you drop it.
I will run the tests and report back. Do not assume a hypothesis is true until I give you evidence.
```

**Why it works:** it prevents jumping to a plausible fix, structures investigation around falsifiable hypotheses and keeps the human in the loop. See [Hypothesis driven debugging](debugging/hypothesis-driven-debugging.md).

## Pair 5: Refactoring

**Weak**

```text
Clean up this code and make it better.
```

**Strong**

```text
Refactor `price_order` for readability without changing behaviour.

Step 1: write characterisation tests for the current behaviour, including odd cases. Do not fix oddities; list them as questions.
Step 2: run them and show they pass on the unchanged code.
Step 3: propose a list of small refactoring steps (rename, extract function, replace magic number with a named constant). Wait for my approval.
Step 4: apply one step at a time. After each, run the tests and show the result.
Constraints: public signatures unchanged; no new dependencies; integer cents stay integer cents; do not change error behaviour.
```

**Why it works:** pins behaviour first, proceeds in verifiable steps and names the semantics that tidy-up commonly alters. See [Behaviour preserving refactoring](development/refactoring.md) and [scenario S9](../examples/scenarios.md#s9-refactoring-exercise).

## Pair 6: Requirements

**Weak**

```text
Write user stories for a discount feature.
```

**Strong**

```text
Here is a one line request: "Give loyal customers a discount."

Do not write stories yet. Produce:
1. Questions I must answer before this can be built, grouped by owner (product, legal, finance, engineering).
2. The business rules you are inferring, each labelled STATED or INFERRED. Treat inferred rules as proposals.
3. Edge cases: boundaries, invalid tiers, stacking with other discounts, refunds, rounding.
Mark any behaviour the request does not define as UNSPECIFIED. Do not choose for me.
```

**Why it works:** it converts the assistant from author to interrogator. The cheapest defects to fix are the ones found before code exists. See [Requirement clarification](requirements/requirement-clarification.md).

## Exercise: build your own pair

1. Take a real task from this week and write the prompt you would normally write.
2. Score it with the rubric below.
3. Rewrite it to fix every zero.
4. Run both against your assistant. Compare the answers on three questions: Did it ask about unknowns? Did it stay in scope? Could you verify its claims without trusting it?

### Scoring rubric

| Question | Yes = 1 |
| --- | --- |
| Does it include the requirement or rule, not only a topic? | |
| Does it state the scope (which files or which scenario)? | |
| Does it say what *not* to do? | |
| Does it say what to do when information is missing? | |
| Does it specify the output format? | |
| Does it demand evidence from real runs for claims? | |
| Could a different developer run it and get a comparable result? | |

A score below 4 usually means the assistant will fill the gaps with plausible guesses.

## Things this playground does not claim

- That any prompt gives better results on every model. Results differ by model, version and context window.
- That longer is better. Specific is better. Remove words that add nothing.
- That a good prompt replaces review. The output still needs the checks in the validation steps of each library prompt.

## Next

- [Prompt library](README.md)
- [Prompt template](../templates/prompt_template.md) to contribute your own
- [Chapter 4: AI Assisted Development](../handbook/04_ai_assisted_development/README.md)

[Back to the repository README](../README.md)
