# Prompt library

Fifty copy-ready prompts for concrete engineering situations. Every prompt follows the same structure, names the skill it pairs with, and says how to validate the answer.

How to use a prompt:

1. Pick the prompt for the situation. Read **When to use** and **Required context**.
2. Prepare the context. Replace each `[BRACKETED PLACEHOLDER]` or attach the files.
3. Paste the prompt into your assistant. Prefer a fresh session for review prompts.
4. Run the **Validation steps**. The answer is a draft; you are accountable for the result.

See also: [Prompt playground](playground.md) (how prompt quality changes results), [Skills](../skills/README.md), [Workflows](../workflows/README.md).

## Requirements

Understand and specify before building: clarification, acceptance criteria, business rules, edge cases and traceability.

- [Requirement Clarification](requirements/requirement-clarification.md): A requirement is vague or incomplete and is about to be implemented on guesses.
- [Acceptance Criteria Generation](requirements/acceptance-criteria-generation.md): Acceptance criteria are missing, vague or not testable.
- [Business Rule Discovery](requirements/business-rule-discovery.md): Business rules live only inside code or in people's heads, and are about to be changed or reimplemented.
- [Edge Case Discovery](requirements/edge-case-discovery.md): Edge cases are discovered in production instead of during design.
- [Scenario Matrix Generation](requirements/scenario-matrix-generation.md): Tests are written ad hoc, so nobody can say which requirements are covered.
- [Requirement Traceability Check](requirements/requirement-traceability-check.md): A change claims to implement a requirement but nobody has checked that every criterion is implemented and tested.

## Development

Plan and change code safely: exploration, planning, generation, modification, refactoring and defensive coding.

- [Repository Exploration](development/repository-exploration.md): You must change code you do not know, and the assistant is guessing at structure and conventions.
- [Implementation Planning](development/implementation-planning.md): Large AI edits are hard to review and break things because nothing was planned in small steps.
- [Code Generation From a Plan](development/code-generation.md): Generated code ignores the plan, over-builds and arrives without evidence that it works.
- [Existing Code Modification](development/existing-code-modification.md): Changing legacy code without understanding its current behaviour causes regressions.
- [Behaviour Preserving Refactoring](development/refactoring.md): Refactoring requests turn into rewrites that change behaviour.
- [Defensive Coding Pass](development/defensive-coding.md): Code handles the happy path only and fails unpredictably on missing data, bad input or dependency failure.
- [Dependency Analysis](development/dependency-analysis.md): Adding or upgrading a dependency without understanding its cost, risk and blast radius.
- [Documentation Update](development/documentation-update.md): Documentation lags the code, or is AI-written with invented behaviour.

## Testing

Test first and test well: TDD, unit, integration, contract, boundary, negative, mutation and regression tests.

- [TDD Test Generation](testing/tdd-test-generation.md): Tests written after the code mirror the implementation instead of specifying behaviour.
- [Unit Test Generation](testing/unit-test-generation.md): Existing code has weak or no unit tests.
- [Integration Test Generation](testing/integration-test-generation.md): Mocked unit tests pass while the real database query or HTTP call is wrong.
- [Contract Testing](testing/contract-testing.md): API changes break consumers because the contract is implicit.
- [Boundary Testing](testing/boundary-testing.md): Off by one and comparison errors survive because only typical values are tested.
- [Negative Testing](testing/negative-testing.md): Only success paths are tested, so invalid input behaviour is accidental.
- [Mutation Testing Analysis](testing/mutation-testing.md): Tests pass but would not catch real defects.
- [Regression Test Generation](testing/regression-test-generation.md): A fixed bug returns, or changed code silently alters behaviour.
- [Test Data Builder Design](testing/test-data-builder-design.md): Tests are cluttered with large object setup, hiding what matters.
- [Flaky Test Diagnosis](testing/flaky-test-diagnosis.md): A test fails intermittently and the team retries instead of fixing.

## Debugging and operations

Diagnose with evidence: hypotheses, stack traces, incidents, root cause, logs and performance.

- [Hypothesis Driven Debugging](debugging/hypothesis-driven-debugging.md): Trial-and-error fixing hides the root cause.
- [Stack Trace Analysis](debugging/stack-trace-analysis.md): A stack trace is long and the actual failing frame is not obvious.
- [Production Incident Analysis](debugging/production-incident-analysis.md): During an incident, teams jump to causes and lose track of facts.
- [Root Cause Analysis](debugging/root-cause-analysis.md): Post-incident reviews stop at the proximate cause and miss systemic gaps.
- [Log Analysis](debugging/log-analysis.md): Logs are voluminous and patterns are missed or hallucinated.
- [Performance Bottleneck Analysis](debugging/performance-bottleneck-analysis.md): Performance work starts with guesses rather than measurements.

## Code review

Review independently and precisely: control flow, missing conditions, null and exception handling, security, performance and PR readiness.

- [Control Flow Review](code_review/control-flow-review.md): Branching logic hides missing branches, precedence mistakes and boundary errors.
- [Missing Condition Detection](code_review/missing-condition-detection.md): A branch exists for some cases and silently ignores others.
- [Null Handling Review](code_review/null-handling-review.md): Null or absent values cause crashes or silent wrong results far from their source.
- [Exception Handling Review](code_review/exception-handling-review.md): Exceptions are swallowed, over-caught or lose context, so failures are invisible or mishandled.
- [Security Review](code_review/security-review.md): Security defects are introduced in generated or hand-written code and not noticed.
- [Performance Review](code_review/performance-review.md): A change introduces performance regressions that are invisible in small tests.
- [Independent Code Review](code_review/independent-code-review.md): The same assistant that wrote the code reviews it and shares its blind spots.
- [PR Readiness Assessment](code_review/pr-readiness-assessment.md): Pull requests arrive for review incomplete, wasting reviewer time.
- [PR Description Drafting](code_review/pr-description-drafting.md): PR descriptions restate the diff and omit intent, risk and verification.

## Architecture

Review designs and decisions: architecture, ADRs, APIs, schemas, resilience and threat models.

- [Architecture Review](architecture/architecture-review.md): Designs are accepted without examining trade-offs, failure modes or alternatives.
- [Architecture Decision Record Drafting](architecture/adr-drafting.md): Architectural decisions are lost, and future engineers do not know why.
- [API Design Review](architecture/api-design-review.md): APIs are designed from the implementation outward and break consumers over time.
- [Database Schema Review](architecture/database-schema-review.md): Schema changes cause data integrity problems, downtime or slow queries.
- [Resilience Review](architecture/resilience-review.md): Services fail badly when dependencies are slow or down.
- [Threat Modelling](architecture/threat-modelling.md): Security design is ad hoc and threats are found after release.

## Delivery

Release with evidence: deployment risk, rollback, readiness, observability and release notes.

- [Deployment Risk Analysis](delivery/deployment-risk-analysis.md): Changes reach production without a clear view of what could go wrong.
- [Rollback Planning](delivery/rollback-planning.md): Rollback is assumed to be easy until it is needed and turns out to be impossible.
- [Release Readiness Check](delivery/release-readiness-check.md): Releases happen on feeling rather than evidence.
- [Observability Gap Analysis](delivery/observability-gap-analysis.md): Failures cannot be detected or diagnosed because the right signals are missing.
- [Changelog and Release Notes](delivery/changelog-and-release-notes.md): Release notes are copied commit messages that users cannot use.

## Contributing a prompt

Use [templates/prompt_template.md](../templates/prompt_template.md) and follow [CONTRIBUTING.md](../CONTRIBUTING.md). The validation script checks structure.
