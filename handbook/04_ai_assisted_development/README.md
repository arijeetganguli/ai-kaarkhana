# Chapter 4: AI Assisted Development

> Ask for small changes, in a codebase the assistant has read, under rules you have written down.

## What you will learn

- How to generate code under constraints, and how to analyse an existing codebase with AI.
- How to write repository level instructions that make every session better.
- How to manage architecture awareness, context, multi file changes and dependencies.
- How to implement incrementally, refactor safely and debug with evidence.
- What this looks like in Java, Python and TypeScript.

## 1. Code generation

Generated code is best when the task is **specified, small and verifiable**.

| Give | Why |
| --- | --- |
| The behaviour as scenarios or failing tests | The assistant has a target it can check against |
| One slice at a time | The diff stays reviewable |
| The files that may change | Prevents sprawl |
| An existing example to follow | Matches naming, structure and error handling |
| The "do not" list | No new dependencies, no changes to unrelated files, no weakened tests |

Use [Code generation](../../prompts/development/code-generation.md): it requires the test first, the minimal change, the actual test run and a list of decisions and limitations.

**Review checklist for generated code**

- Does it do what the scenario says, and nothing more?
- Is every branch intentional, including the input nobody mentioned ([Chapter 6](../06_defensive_programming/README.md))?
- Does it follow local conventions (naming, error handling, logging, layering)?
- Did it add dependencies, configuration or files you did not ask for?
- Do you understand every line?

## 2. Existing codebase analysis

Before changing code, build a **verified map**. Ask the assistant to explore and report, then check its claims.

1. **Orientation:** language, build tool, test framework, commands, directory layout.
2. **Path:** from entry point (route, handler, job, consumer) to data store and external calls, as a table of file, symbol and responsibility.
3. **Tests:** which tests cover the path, how they are written, what is missing.
4. **Conventions:** two similar features and what they have in common.
5. **Risk:** shared code with many callers, code with no tests, generated code, configuration and feature flags.

[Repository Explorer](../../skills/repository-explorer/SKILL.md) · [Repository exploration](../../prompts/development/repository-exploration.md) · [Dependency analysis](../../prompts/development/dependency-analysis.md)

When the question is "what could this change break?", use the [Regression Analyst](../../skills/regression-analyst/SKILL.md): list callers, map behaviours to tests, write characterisation tests for the gaps, and only then change the code ([Existing code modification](../../prompts/development/existing-code-modification.md)).

### Repository level instructions

Repository level instructions teach the assistant what a new colleague would learn in the first week. They are loaded automatically into the context of every session, so they are the cheapest and most effective context you can write.

A good instruction file contains:

- **Architecture overview:** layers, modules, dependency directions, where things live.
- **Build and test commands**, exactly as typed in a terminal.
- **Conventions:** naming, error handling, logging, validation, formatting.
- **Working rules:** analyse requirements first; never invent business rules; test first; run the tests and report real results; do not weaken tests; no new dependencies without asking.
- **A "never do" list:** secrets in code, catch-all exception handlers, edits to generated files.
- **Pointers** to deeper documents, so that the file itself stays short.

This repository ships a reusable set: [`.github/copilot-instructions.md`](../../.github/copilot-instructions.md) and [`AGENTS.md`](../../AGENTS.md). The tool specific file names and formats are documented, with the date they were verified, in [`tools/`](../../tools/README.md). Keep instruction files short and specific; contradictory or bloated instructions are followed worse than none.

## 3. Architecture awareness

Assistants happily generate code that works and violates your architecture: a controller that calls the database, a domain object that imports a framework, a shared table written by two services.

- **Write the rules down** (dependency direction, module boundaries, allowed integrations) in the instruction file.
- **Enforce them with tools** where possible (architecture tests, linters with import rules), because rules that are only prose are only sometimes followed.
- **Ask for an architecture check of the plan** before the code: [Architecture review](../../prompts/architecture/architecture-review.md).
- **Prefer extending existing structure** to introducing new patterns. A new pattern needs an ADR ([Chapter 8](../08_architecture_and_design/README.md)).

## 4. Context management

Detailed guidance is in [Chapter 2](../02_developer_ways_of_working/README.md#5-context-engineering). The short version for coding sessions:

- One task per session. New task, new session.
- Pin the plan and constraints at the top; restate them when the session is long.
- Point to files rather than pasting whole directories.
- When the assistant starts to contradict earlier decisions, summarise the decisions and restart.

## 5. Multi file changes

Edits that span files are where agents save the most time and cause the most damage.

- **Plan first**, with the list of files and the reason for each. Review it.
- **Order the work** from the inside out: tests, domain logic, then adapters, then wiring.
- **Keep every intermediate state buildable**, so that you can bisect and revert.
- **Review by behaviour, not by file.** Read the tests first, then the production diff.
- **Scan for unrequested changes:** formatting sweeps, renamed symbols, edited configuration, touched tests.
- **Cap the size.** If the diff is too big to review in one sitting, split the task. The [split workflow](../../workflows/09_pull_request_review.md) describes how reviewers should push back.

## 6. Dependency management

An assistant adds dependencies cheaply. You pay for them for years.

Before accepting a new dependency, check: is the same thing available in the standard library or an existing dependency? Licence compatibility? Maintenance activity? Known vulnerabilities? Transitive footprint? Can you remove it later?

- Ask with the [Dependency analysis](../../prompts/development/dependency-analysis.md) prompt, and **verify its factual claims** (versions, licences, vulnerabilities) in the primary source. Assistants may state outdated or invented version facts.
- Pin versions, use lock files and run the dependency scanner in CI ([Chapter 9](../09_security_engineering/README.md)).
- For upgrades: read the project's changelog, then run the full test suite on a branch.

## 7. Incremental implementation

The unit of work is a **slice**: one behaviour, one failing test, minimal code, refactor, commit.

Example: scenario *"customers aged 65 or older are eligible for the senior discount"*. Work proceeds in three slices, each one starting with a test. This is the complete, tested result of the last slice in all three languages ([scenario S3](../../examples/scenarios.md#s3-incorrect-boundary-condition)).

**Java** (JUnit 5): [`SeniorDiscount.java`](../../examples/java/src/main/java/io/kaarkhana/examples/s03/SeniorDiscount.java)

```java
public static boolean isSenior(int age) {
    if (age < 0) {
        throw new IllegalArgumentException("age must not be negative, got " + age);
    }
    return age >= SENIOR_AGE;
}
```

```java
@ParameterizedTest
@CsvSource({"0,false", "64,false", "65,true", "66,true", "100,true"})
void eligibilityBelowAtAndAboveTheBoundary(int age, boolean expected) {
    assertEquals(expected, SeniorDiscount.isSenior(age));
}
```

**Python** (pytest): [`improved.py`](../../examples/python/src/kaarkhana/s03_boundary/improved.py)

```python
def is_senior(age):
    if isinstance(age, bool) or not isinstance(age, int):
        raise ValueError(f"age must be a whole number, got {age!r}")
    if age < 0:
        raise ValueError(f"age must not be negative, got {age}")
    return age >= SENIOR_AGE
```

```python
@pytest.mark.parametrize("age,expected", [(0, False), (64, False), (65, True), (66, True), (100, True)])
def test_eligibility_below_at_and_above_the_boundary(age, expected):
    assert improved.is_senior(age) is expected
```

**TypeScript** (Vitest): [`improved.ts`](../../examples/typescript/src/s03_boundary/improved.ts)

```typescript
export function isSenior(age: unknown): boolean {
  if (typeof age !== "number" || !Number.isInteger(age)) {
    throw new RangeError(`age must be a whole number, got ${JSON.stringify(age)}`);
  }
  if (age < 0) {
    throw new RangeError(`age must not be negative, got ${age}`);
  }
  return age >= SENIOR_AGE;
}
```

```typescript
it.each([[0, false], [64, false], [65, true], [66, true], [100, true]])("age %i -> %s", (age, expected) => {
  expect(improved.isSenior(age)).toBe(expected);
});
```

What the slices looked like: (1) a test for 66 passes with any implementation, so it is not a useful first test; (2) the test for exactly 65 fails against `age > 65` and forces `>=`; (3) invalid ages are rejected because the scenario matrix lists them, and the error message names the value. Each step is a commit.

## 8. Refactoring

Refactoring changes structure, never behaviour, and is safe only under test.

1. Run the existing tests. They must be green.
2. If protection is weak, write **characterisation tests** that pin current behaviour, quirks included.
3. Apply one small named refactoring at a time (extract function, rename, introduce parameter object, replace conditional with a table or polymorphism, inline).
4. Run the tests after each step.
5. Log bugs you notice. **Do not fix them in the same commit.**

A worked example is [scenario S9](../../examples/scenarios.md#s9-refactoring-exercise) in all three languages: nested conditionals refactored into one function per rule, with an equivalence test over 150 inputs. Use the [Refactoring Specialist](../../skills/refactoring-specialist/SKILL.md) and the [Refactoring](../../prompts/development/refactoring.md) prompt. Assistants tend to propose rewrites; insist on steps.

## 9. Debugging

Debugging with an assistant works when you keep the scientific method and use the assistant to widen the set of hypotheses and to read code fast.

1. **Reproduce** the problem, ideally as an automated failing test.
2. **Hypothesise.** Ask for two to four falsifiable hypotheses, each with the cheapest check ([Hypothesis driven debugging](../../prompts/debugging/hypothesis-driven-debugging.md)).
3. **Test** the hypotheses with evidence: read the path, add temporary logging, inspect data, bisect.
4. **Identify the root cause**, not just the line that changes the symptom.
5. **Fix** with the smallest change, with the failing test now passing.
6. **Search for siblings:** the same defect pattern elsewhere.

Be careful of the "fix" that adds a null check or a try/catch around the symptom. It often hides a data or design problem ([Chapter 6](../06_defensive_programming/else_is_not_always_the_answer.md)). The [Broken Code Lab](../../examples/broken_code_lab/README.md) is a safe place to practise this.

Related prompts: [Stack trace analysis](../../prompts/debugging/stack-trace-analysis.md), [Log analysis](../../prompts/debugging/log-analysis.md), [Root cause analysis](../../prompts/debugging/root-cause-analysis.md).

## Practice

- Write the instruction file for a repository you work in. Remove every sentence the assistant could not act on.
- Ask an assistant for the call path of a feature, then verify three of its claims.
- Take one scenario of the [catalogue](../../examples/scenarios.md) in a language you do not use, and read the three implementations side by side.

## Related

**Skills:** [Repository Explorer](../../skills/repository-explorer/SKILL.md), [Implementation Planner](../../skills/implementation-planner/SKILL.md), [Regression Analyst](../../skills/regression-analyst/SKILL.md), [Refactoring Specialist](../../skills/refactoring-specialist/SKILL.md), [Debugging Specialist](../../skills/debugging-specialist/SKILL.md)

**Prompts:** [Code generation](../../prompts/development/code-generation.md), [Existing code modification](../../prompts/development/existing-code-modification.md), [Refactoring](../../prompts/development/refactoring.md), [Defensive coding](../../prompts/development/defensive-coding.md), [Dependency analysis](../../prompts/development/dependency-analysis.md)

**Workflows:** [Build a new feature](../../workflows/01_feature_development.md), [Refactor an existing service](../../workflows/03_service_refactoring.md), [Fix a defect](../../workflows/02_defect_fix.md)

**Examples:** [Java](../../examples/java/README.md), [Python](../../examples/python/README.md), [TypeScript](../../examples/typescript/README.md)

**Further reading** (external):

- [Refactoring catalogue](https://refactoring.com/catalog/) by Martin Fowler.
- [Agent Skills open standard](https://agentskills.io).

---

Previous: [Chapter 3](../03_requirement_engineering/README.md) · Next: [Chapter 5: Test Driven Development](../05_test_driven_development/README.md) · [Handbook index](../README.md)
