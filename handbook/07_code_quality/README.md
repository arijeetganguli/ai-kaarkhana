# Chapter 7: Code Quality

> AI makes writing code cheap. It does not make *reading, changing and operating* code cheap. Quality is the discipline that protects the expensive part.

## What you will learn

- What quality means in practice: readable, changeable, correct, observable.
- The smells and principles that predict maintenance pain.
- How to configure static analysis and quality gates in Java, Python and TypeScript projects.
- The quality risks that are specific to AI generated code, and how to counter them.
- How to treat technical debt as a managed decision.

## 1. What "quality" is

Quality code has four properties that matter day to day:

| Property | Question |
| --- | --- |
| **Correct** | Does it do what the requirement says, including failure cases? |
| **Readable** | Can a new colleague explain it in five minutes? |
| **Changeable** | Can a typical change be made in one place, safely? |
| **Operable** | Can we tell what it is doing in production, and recover when it fails? |

A line of code is a liability as well as an asset: it must be read, tested, secured and maintained. The cheapest code to maintain is code that does not exist. With an assistant that can generate hundreds of lines in seconds, **the discipline is saying no to lines**.

## 2. Clean code in practice

| Practice | Do | Avoid |
| --- | --- | --- |
| **Names** | Reveal intent: `overdueInvoices`, `retryDelay` | `data`, `tmp`, `handle2`, abbreviations |
| **Functions** | One level of abstraction, one reason to change | 200 line functions that parse, decide and persist |
| **Parameters** | Few; group related ones in a type | Boolean flags that switch behaviour |
| **Comments** | Explain *why* (constraint, trade off, link to a decision) | Restating *what* the code does |
| **Errors** | Specific, informative ([Chapter 6](../06_defensive_programming/README.md)) | Silent failure |
| **State** | Immutable by default; narrow scope | Shared mutable globals |
| **Structure** | Consistent with the surrounding code | A new style in each file |

### The "before and after" in one picture

**Python**

```python
# before
def p(o, c):
    t = 0
    for i in o["items"]:
        t += i["p"] * i["q"]
    if c == "G":
        t = t - t * 0.1
    return t

# after
def order_total_cents(order, tier):
    subtotal = sum(line.unit_price_cents * line.quantity for line in order.lines)
    return subtotal - discount_cents(subtotal, tier)
```

The change is not cosmetic: the second version has a testable `discount_cents`, integer money and names a reviewer can check against the requirement. The runnable version of this exercise, with tests that prove the behaviour is unchanged, is [scenario S9](../../examples/scenarios.md#s9-refactoring-exercise).

## 3. SOLID, used sparingly

SOLID principles are guidance for managing change, not rules to apply everywhere. Apply them when a real pain exists.

| Principle | In one sentence | A smell that suggests it | Do not over-apply |
| --- | --- | --- | --- |
| **S**ingle responsibility | A module has one reason to change | A class that changes for UI, rules *and* storage reasons | Splitting one cohesive 30 line class into five |
| **O**pen/closed | Add behaviour without editing stable code | Every new tier edits a growing `if` chain | Plugin architectures for two variants |
| **L**iskov substitution | Subtypes honour the parent's contract | Subclass throws on an inherited method | Using inheritance when composition is simpler |
| **I**nterface segregation | Small, role specific interfaces | Implementers stub half the methods | One interface per method |
| **D**ependency inversion | Depend on abstractions you own at boundaries | Business rule imports an HTTP client | Interface for every class |

Rule of thumb: **abstract at boundaries you actually have** (database, network, clock), not at imagined ones.

## 4. Code smells

A smell is a surface symptom that often points to a deeper problem. It is a prompt to *look*, not a verdict.

| Smell | Symptom | Typical remedy |
| --- | --- | --- |
| **Long function** | Scrolls past one screen | Extract functions with names that explain steps |
| **Deep nesting** | Arrow shaped code | Guard clauses, early return |
| **Duplicated logic** | Same rule in two places, one of them wrong | Extract one source of truth ([see below](#7-duplication-and-dependencies)) |
| **Primitive obsession** | Everything is `String` and `int` | Small types: `Email`, `Money`, `Tier` |
| **Long parameter list** | More than four parameters | Parameter object; rethink the function |
| **Feature envy** | A method uses another object's data more than its own | Move the method |
| **Shotgun surgery** | One change touches ten files | Gather the responsibility |
| **God class** | One class everybody edits | Split along responsibilities |
| **Boolean flag parameter** | `process(order, true, false)` | Two functions, or named options |
| **Magic numbers and strings** | `if (age > 65)` | Named constants taken from the requirement |
| **Commented out code** | Dead code in comments | Delete; version control remembers |
| **Dead code** | Unreferenced functions, flags nobody sets | Delete |

The [Code Quality Reviewer](../../skills/code-quality-reviewer/SKILL.md) skill and the [Refactoring Specialist](../../skills/refactoring-specialist/SKILL.md) work through these systematically.

## 5. Complexity and maintainability

**Cyclomatic complexity** counts independent paths through a function (roughly: one plus the number of decision points). A common practice is to flag functions above a threshold (many teams start near 10) and review them. It correlates with the number of tests needed and with defects, but it is only a signal. A flat 15 branch lookup can be fine; a nested 8 branch function with side effects can be dangerous.

Other signals worth watching:

| Signal | What it suggests |
| --- | --- |
| **Cognitive complexity** (nesting and flow breaks) | Hard to read, even if the count is low |
| **File churn plus complexity** | A hot spot: where defects and conflicts cluster |
| **Coupling** (imports, fan out) | Changes will ripple |
| **Test to code ratio of the hot spots** | Are the risky places the protected ones? |

Use these to **choose where to spend refactoring effort**, not to grade people.

## 6. Refactoring with safety

Refactoring is changing structure without changing behaviour. The safety is the tests.

1. **Characterise first.** If tests do not exist, write tests that pin current behaviour ([Chapter 5](../05_test_driven_development/README.md)).
2. **Small steps**, tests green after each. One kind of change per commit.
3. **Do not mix** refactoring and behaviour change in one pull request.
4. **Review the diff for behaviour**, not style. An assistant that "tidies up" may change semantics (integer to float, order of evaluation, error handling).
5. **Stop** when the next step has no test.

Use [Behaviour preserving refactoring](../../prompts/development/refactoring.md) and the [Service refactoring workflow](../../workflows/03_service_refactoring.md). The runnable exercise is [scenario S9](../../examples/scenarios.md#s9-refactoring-exercise).

## 7. Duplication and dependencies

**Duplication** is only a problem when the copies must change together. Two pieces of code that look alike but change for different reasons should stay apart (the cost of the wrong abstraction exceeds the cost of duplication). When the *rule* is duplicated (the discount calculation in the cart and in the invoice), consolidate it.

**Dependencies** are code you did not write and still must maintain.

| Practice | Why |
| --- | --- |
| Prefer the standard library when it is enough | Fewer things to patch |
| Pin versions and commit lock files (`package-lock.json`, `poetry.lock`, resolved Maven versions) | Reproducible builds |
| Verify any package an assistant suggests actually exists and is the intended one | Assistants sometimes suggest non-existent or look-alike package names ("slopsquatting") |
| Check licence, maintenance, size and transitive dependencies | Legal and supply chain risk |
| Update regularly in small steps | Large jumps hurt |
| Scan for known vulnerabilities in CI | See [Chapter 9](../09_security_engineering/README.md) |
| Remove unused dependencies | Smaller attack surface |

Use the [Dependency analysis](../../prompts/development/dependency-analysis.md) prompt before adopting a new library.

## 8. Static analysis

Static analysis finds defect classes without running the code. Use it for the mechanical findings so human reviewers can spend attention on design and correctness.

| Language | Linting and style | Type checking | Bug and security patterns |
| --- | --- | --- | --- |
| **Java** | Checkstyle, PMD | The compiler (plus Error Prone, NullAway) | SpotBugs, SonarQube rules |
| **Python** | Ruff (or flake8, pylint) | mypy or pyright | Bandit, Ruff `S` rules |
| **TypeScript** | ESLint with typescript-eslint | `tsc --strict` | ESLint security plugins, Semgrep |

These are examples of widely used tools; choose by your platform, and **check each project's documentation for current configuration syntax**. The snippets below are illustrative starting points and were not executed as part of this repository.

**Python: `pyproject.toml`**

```toml
[tool.ruff]
line-length = 100

[tool.ruff.lint]
# E/F: basic errors, B: likely bugs, S: security, C90: complexity, SIM: simplifications, UP: modern syntax
select = ["E", "F", "B", "S", "C90", "SIM", "UP"]

[tool.ruff.lint.mccabe]
max-complexity = 10

[tool.mypy]
strict = true
```

**TypeScript: `tsconfig.json` (compiler strictness)**

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true
  }
}
```

**TypeScript: `eslint.config.js`**

```javascript
import js from "@eslint/js";
import tseslint from "typescript-eslint";

export default tseslint.config(
  js.configs.recommended,
  ...tseslint.configs.recommended,
  {
    rules: {
      eqeqeq: "error",
      complexity: ["error", 10],
      "max-lines-per-function": ["warn", 80],
      "no-console": "warn",
    },
  },
);
```

**Java**: enable compiler warnings as errors (`-Xlint:all -Werror` for your own code), add Checkstyle or PMD for style and complexity, and SpotBugs for defect patterns, through the Maven or Gradle plugin of your choice. Add a null-safety checker such as NullAway if your team has a null problem ([scenario S2](../../examples/scenarios.md#s2-missing-null-handling)).

### Handling findings

- **Fix** true positives.
- **Suppress narrowly** (one line, with a reason) false positives. Do not disable rules globally to get a green build.
- **Never** let an assistant silence a finding to make the pipeline pass without a human understanding why.
- **Tune** noisy rules; an ignored linter is worse than none.

## 9. Quality gates

A **quality gate** is an automated pass/fail rule on a pull request or build. A reasonable starting point:

| Gate | Typical rule | Note |
| --- | --- | --- |
| Build and unit tests | Must pass | Non-negotiable |
| Lint and format | No new violations | Format automatically; do not debate it in review |
| Type check | No errors | |
| Test coverage of **changed code** | Threshold chosen by the team | Coverage is a floor on untested code, not proof of quality ([Chapter 5](../05_test_driven_development/property_based_and_mutation_testing.md)) |
| Dependency vulnerability scan | No new high severity without an exception | |
| Secret scan | No secrets in the diff | |
| Complexity | New or changed functions under the threshold | |
| Mutation score on critical modules | Optional, run on changed code or nightly | |
| Human review | At least one reviewer who is accountable | See [Chapter 10](../10_code_review_and_pull_requests/README.md) |

Two principles: **gate the change, not the history** (fail on *new* violations so legacy code does not block you), and **gates are a floor**. Passing every gate means "not obviously bad", not "good".

Thresholds in this table are starting points to adapt, not recommendations backed by a study.

## 10. AI generated code: quality risks

| Risk | What it looks like | Countermeasure |
| --- | --- | --- |
| **Plausible but wrong** | Reads fluent, fails on an edge case | Tests derived from the requirement; [Chapter 6](../06_defensive_programming/README.md) |
| **Over-engineering** | Interfaces, factories and config for a 20 line problem | Ask for the simplest change; delete what is unused |
| **Duplication** | New helper that already exists elsewhere | [Repository exploration](../../prompts/development/repository-exploration.md) first |
| **Style drift** | Different naming, error handling and layout from the repo | Repository instructions ([Chapter 4](../04_ai_assisted_development/README.md#repository-level-instructions)); autoformat |
| **Hallucinated APIs** | Calls methods or packages that do not exist | Compile, run, check docs |
| **Outdated practices** | Deprecated API, old library idioms | State versions in the prompt; check release notes |
| **Weak or mirror tests** | Tests that pass for any implementation | Mutation testing, review of assertions |
| **Large diffs** | Reformatting and unrelated edits | Constrain files; review every changed line |
| **Silent behaviour change in refactors** | Types, ordering or defaults change | Characterisation tests |
| **Hidden coupling to the prompt** | Code only a prompt author understands | The reviewer must be able to explain every line |
| **Comments that lie** | Docstring describes intended, not actual, behaviour | Review comments against code |
| **Secrets and personal data in examples** | Real looking credentials | Secret scanning |

The reviewer's test, from [Chapter 1](../01_ai_native_engineering/README.md): *could I explain and defend this code in a design review without the assistant?*

## 11. Technical debt

**Technical debt** is the future cost of a decision that is cheaper now. Like financial debt it can be a good deal when it is *deliberate, visible and repaid*.

| Kind | Example | Response |
| --- | --- | --- |
| **Deliberate and prudent** | "Ship with a simple in-memory cache, replace before 10k users" | Record it, with a trigger |
| **Deliberate and reckless** | "No time for tests" | Challenge it |
| **Accidental** | We learned a better design | Refactor when touching the area |
| **Bit rot** | Old dependencies, unmaintained code | Schedule updates |

Practical handling:

1. **Make it visible**: a ticket or a `TODO(ID)` with an owner and a trigger, never a bare `TODO`.
2. **Estimate the interest**: what does it cost every sprint? Bugs, slow changes, onboarding.
3. **Pay down where the traffic is**: hot spots first.
4. **Budget** a steady fraction of capacity; do not wait for a "refactoring sprint".
5. **Do not hide it** in generated code: AI makes it easy to add 2000 lines of unreviewed debt in a morning.

## Practice

1. Run the linters and type checker for your language on a repository you own. Pick ten findings and classify them: fix, suppress with reason, or tune the rule.
2. Take the [scenario S9](../../examples/scenarios.md#s9-refactoring-exercise) initial code and refactor it yourself in tiny steps, running the tests after each. Then compare with the improved version.
3. Draft a quality gate for your team on one page. Mark each rule as *blocking* or *informational*.

## Related

**Skills:** [Code Quality Reviewer](../../skills/code-quality-reviewer/SKILL.md), [Refactoring Specialist](../../skills/refactoring-specialist/SKILL.md), [Performance Analyst](../../skills/performance-analyst/SKILL.md), [Documentation Engineer](../../skills/documentation-engineer/SKILL.md)

**Prompts:** [Behaviour preserving refactoring](../../prompts/development/refactoring.md), [Dependency analysis](../../prompts/development/dependency-analysis.md), [Documentation update](../../prompts/development/documentation-update.md), [Performance review](../../prompts/code_review/performance-review.md)

**Workflows:** [Refactor an existing service](../../workflows/03_service_refactoring.md), [Review a pull request](../../workflows/09_pull_request_review.md)

**Examples:** [Scenario S9](../../examples/scenarios.md#s9-refactoring-exercise)

**Further reading** (external): *Clean Code* by Robert C. Martin, *Refactoring* by Martin Fowler, [Ruff documentation](https://docs.astral.sh/ruff/), [typescript-eslint](https://typescript-eslint.io), [SpotBugs](https://spotbugs.github.io), [mypy](https://mypy.readthedocs.io).

---

Previous: [Chapter 6](../06_defensive_programming/README.md) · Next: [Chapter 8: Architecture and Design](../08_architecture_and_design/README.md) · [Handbook index](../README.md)
