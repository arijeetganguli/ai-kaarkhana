# Skill of the week

A lightweight habit for teams: **one skill per week, one small real task, ten minutes to share what happened.** Over 22 weeks everyone has tried every skill in this repository on their own code, and the team knows which ones help and which need tuning.

## How it works

1. **Monday:** the team picks (or the rotation assigns) the week's skill. Everyone reads its `SKILL.md`. It takes five minutes.
2. **During the week:** each person uses the skill once on a real task they were going to do anyway. Do not invent work for it.
3. **Check the output:** use the skill's own **Validation checklist** and decide what you would keep, change or throw away.
4. **Friday, ten minutes:** each person shares one thing the skill got right and one thing it got wrong or missed.
5. **Capture improvements:** if a skill missed something that generalises, open an issue or pull request to improve the skill (see the [contribution guide](../CONTRIBUTING.md)).

Rules that keep it useful:

- Use real, non sensitive work. Follow your organisation's data rules; see [Chapter 9](../handbook/09_security_engineering/README.md#7-sensitive-information-handling).
- Share failures as readily as successes. A skill that misleads is a finding.
- Verify with tests and by reading the output, not by the assistant's confidence.
- Skip a week when the skill does not apply to what the team is doing; do not force it.

## The rotation

The order moves from understanding the problem, to building, to reviewing and delivering. Start anywhere that fits your team. Each row gives a **starter task** and where to find practice material.

| Week | Skill | Starter task | Practice material |
| --- | --- | --- | --- |
| 1 | [Requirement Analyst](../skills/requirement-analyst/SKILL.md) | Run next week's most ambiguous ticket through the skill and count the open questions it finds | [Clarification prompt](../prompts/requirements/requirement-clarification.md) |
| 2 | [Edge Case Hunter](../skills/edge-case-hunter/SKILL.md) | Build a scenario matrix for a function you are about to write | [Scenario matrix template](../templates/scenario_matrix_template.md) |
| 3 | [Business Rule Analyst](../skills/business-rule-analyst/SKILL.md) | Extract the rules from one pricing, eligibility or validation module | [Business rule discovery](../prompts/requirements/business-rule-discovery.md) |
| 4 | [Repository Explorer](../skills/repository-explorer/SKILL.md) | Map a part of the codebase you have never touched | [Repository exploration](../prompts/development/repository-exploration.md) |
| 5 | [Implementation Planner](../skills/implementation-planner/SKILL.md) | Plan a change in steps of under an hour each, test first | [Implementation planning](../prompts/development/implementation-planning.md) |
| 6 | [TDD Engineer](../skills/tdd-engineer/SKILL.md) | Implement one small function with visible red and green runs | [End to end example](../examples/end_to_end/README.md) |
| 7 | [Unit Test Engineer](../skills/unit-test-engineer/SKILL.md) | Add tests for boundaries and negative cases of an existing function | [Unit test generation](../prompts/testing/unit-test-generation.md) |
| 8 | [Mutation Testing Specialist](../skills/mutation-testing-specialist/SKILL.md) | Hand mutate one function and see which mutants your tests miss | [Scenario S7](../examples/scenarios.md#s7-weak-assertions-and-mutation-testing) |
| 9 | [Integration Test Engineer](../skills/integration-test-engineer/SKILL.md) | Replace one mock heavy test with a real boundary test | [Lab 08](../examples/broken_code_lab/08_missing_integration_test/CHALLENGE.md) |
| 10 | [Control Flow Analyst](../skills/control-flow-analyst/SKILL.md) | Enumerate the conditions of a branching function and find the gap | [Lab 01](../examples/broken_code_lab/01_missing_else/CHALLENGE.md) and [Lab 03](../examples/broken_code_lab/03_boolean_condition/CHALLENGE.md) |
| 11 | [Defensive Programming Reviewer](../skills/defensive-programming-reviewer/SKILL.md) | Review one external facing function for null, empty and failure cases | [Lab 02](../examples/broken_code_lab/02_null_dereference/CHALLENGE.md) and [Lab 06](../examples/broken_code_lab/06_inadequate_exception_handling/CHALLENGE.md) |
| 12 | [Debugging Specialist](../skills/debugging-specialist/SKILL.md) | Take the next defect from reproduction to a regression test | [Hypothesis driven debugging](../prompts/debugging/hypothesis-driven-debugging.md) |
| 13 | [Regression Analyst](../skills/regression-analyst/SKILL.md) | List what could break before you merge your next change | [Regression test generation](../prompts/testing/regression-test-generation.md) |
| 14 | [Refactoring Specialist](../skills/refactoring-specialist/SKILL.md) | Pin an untested function with characterisation tests, then simplify it | [Scenario S9](../examples/scenarios.md#s9-refactoring-exercise) |
| 15 | [Code Quality Reviewer](../skills/code-quality-reviewer/SKILL.md) | Review a module you own and agree which findings are worth fixing | [Chapter 7](../handbook/07_code_quality/README.md) |
| 16 | [Security Reviewer](../skills/security-reviewer/SKILL.md) | Review one endpoint that handles user input | [Lab 07](../examples/broken_code_lab/07_sql_injection/CHALLENGE.md) |
| 17 | [API Contract Reviewer](../skills/api-contract-reviewer/SKILL.md) | Review an existing or planned API for compatibility and error semantics | [API design review](../prompts/architecture/api-design-review.md) |
| 18 | [Database Design Reviewer](../skills/database-design-reviewer/SKILL.md) | Review a pending migration for safe rollout and rollback | [Database schema review](../prompts/architecture/database-schema-review.md) |
| 19 | [Architecture Reviewer](../skills/architecture-reviewer/SKILL.md) | Review a design and record the decision as an ADR | [ADR template](../templates/adr_template.md) |
| 20 | [Performance Analyst](../skills/performance-analyst/SKILL.md) | Measure before you optimise: profile one slow path | [Performance bottleneck analysis](../prompts/debugging/performance-bottleneck-analysis.md) |
| 21 | [PR Readiness Reviewer](../skills/pr-readiness-reviewer/SKILL.md) | Run it on your own pull request before asking for review | [AI code review checklist](../templates/ai_code_review_checklist.md) |
| 22 | [Documentation Engineer](../skills/documentation-engineer/SKILL.md) | Update a README or runbook from the code and verify each claim | [Documentation update](../prompts/development/documentation-update.md) |

## A retrospective after the rotation

After a full rotation, spend an hour on:

- Which three skills did people reach for again without being asked?
- Which skills produced output nobody trusted? Why?
- What should change in the skills, the prompts or your repository instruction files?
- Where does the [maturity assessment](maturity_assessment.md) now put each practice area?

Turn answers into pull requests, not into a document that nobody reads.

## Make it your own

The rotation is a suggestion. You might run it every second week, group two related skills, or focus on one role: QA engineers might spend four weeks on weeks 2, 7, 8 and 9. The point is a regular rhythm of small, real experiments.

Back to [documentation index](README.md).
