# AI code review checklist

> A checklist for reviewing any change, with extra attention to code that an assistant produced. Use it as a human reviewer, or give it to an assistant for an independent pass (with the requirement and the diff, in a fresh session). Copy it into the pull request and tick what you checked. **Unticked means not checked, not "fine".**

## How to use

1. Read the requirement and the test diff first.
2. Work through the sections that match what the change touches. Skip sections that do not apply and say so.
3. Record each finding with a severity (blocker, major, minor, nit, question) and a file and line.
4. A finding without evidence is a question, not a finding.

## A. Intent and scope

- [ ] The change does what the requirement says, and only that.
- [ ] Scenarios from the requirement are traceable to tests.
- [ ] No unrelated files changed; no reformatting noise.
- [ ] The pull request is small enough to review carefully, or a split was requested.
- [ ] Behaviour not defined by the requirement was raised as a question, not decided by the code.

## B. Tests

- [ ] There are tests for new and changed behaviour, and they fail without the change.
- [ ] Assertions are exact: values, exception types, messages, side effects. No `is not None`, `> 0` or "no exception" as the only check.
- [ ] **No existing assertion was weakened, skipped, commented out or deleted** (check the deleted lines).
- [ ] Boundaries have below, at and above cases.
- [ ] Invalid input, empty, null and error paths are tested, including that nothing was saved or sent.
- [ ] Each real boundary (database, HTTP, queue, file) has an integration test; mocks do not stand in for it everywhere.
- [ ] Tests do not depend on order, wall clock, randomness, network or shared state.
- [ ] Expected values come from the requirement, not from recomputing the implementation's formula.
- [ ] Test names describe behaviour.

## C. Control flow and conditions

- [ ] Every `if` chain and `switch` handles or deliberately rejects every possible value.
- [ ] No `else` or `default` that invents a business default the requirement does not state.
- [ ] Comparison operators are right at the boundaries (`<` vs `<=`).
- [ ] Boolean expressions with several operators are parenthesised and tested as a decision table; De Morgan and precedence are checked.
- [ ] New enum values or states are handled everywhere they matter.

## D. Null, empty and invalid input

- [ ] Possibly absent values are modelled explicitly or validated at the boundary.
- [ ] Empty collections, empty strings and whitespace behave as specified.
- [ ] Numeric limits, negative values, rounding and overflow are considered; money is not binary floating point.
- [ ] Parsing is strict; trailing garbage and partial matches are not silently accepted.

## E. Exceptions and failure handling

- [ ] No catch-all handlers that swallow errors or return a made up value.
- [ ] Specific exception types; the original cause is preserved; messages say what and which input.
- [ ] No secrets or personal data in messages or logs.
- [ ] Every remote call has a timeout; retries are bounded, backed off and only for transient and idempotent operations.
- [ ] Resources are released on every path (`with`, try-with-resources, `finally`).
- [ ] Multi step writes share a transaction, or have a compensating step; zero row updates are checked where they matter.

## F. Concurrency and state

- [ ] Check then act sequences on shared state are atomic or protected (lock, conditional update, constraint).
- [ ] Operations that may be retried or delivered twice are idempotent.
- [ ] No shared mutable global state introduced.

## G. Security

- [ ] All external input is validated at the boundary (type, length, range, format).
- [ ] Queries and commands are parameterised; no string concatenation of input.
- [ ] Every endpoint authenticates **and** authorises, including object ownership and tenant.
- [ ] No hard coded secrets, tokens or keys; no secrets in tests or examples.
- [ ] No disabled verification (`verify=False`, `rejectUnauthorized: false`) and no weakened security configuration.
- [ ] Secure randomness and standard crypto; no custom schemes.
- [ ] Errors reveal nothing sensitive to the client.
- [ ] New dependencies exist, are maintained, are the intended package (not a look-alike), and are scanned.
- [ ] Output is encoded for its context (HTML, SQL, shell, URL).
- [ ] Model output or tool output is not passed unvalidated into a shell, query, template or file path.

## H. Data and compatibility

- [ ] Schema changes are backward compatible at each stage (expand and contract) and have a rollback.
- [ ] API and event changes are non breaking, or versioned and communicated.
- [ ] Existing data that might violate new constraints is considered.

## I. Performance and resources

- [ ] No obvious N+1 queries, unbounded loops, unbounded result sets or memory growth.
- [ ] Indexes and query plans were checked for new queries on large tables.
- [ ] Performance claims are measured, not assumed.

## J. Operability

- [ ] Meaningful logs with correlation IDs, at the right level, without sensitive data.
- [ ] Metrics or alerts exist for new failure modes that matter.
- [ ] Configuration is externalised; defaults are safe.
- [ ] A rollback or feature flag path exists for risky changes.

## K. Design and readability

- [ ] Names are clear and consistent with the codebase.
- [ ] No duplicated logic where a helper already exists in the repository.
- [ ] No over engineering: no interface, factory or configuration without a present need.
- [ ] Comments explain why, and match what the code actually does.
- [ ] No dead code, commented out code or leftover debug output.

## L. Signs of unreviewed AI generated code

- [ ] The author can explain every changed line, including how it fails.
- [ ] No invented APIs, methods or packages; the code compiles and runs.
- [ ] No claims in comments or the description that the code does not support ("sanitised", "thread safe", "handles all cases").
- [ ] Style matches the repository, not a generic tutorial.
- [ ] Test results quoted in the description are from real runs.
- [ ] Suppressions (`@SuppressWarnings`, `eslint-disable`, `noqa`, `type: ignore`) are justified individually.
- [ ] Nothing was added "just in case".

## M. Documentation and communication

- [ ] README, API docs, changelog and runbooks updated where users or operators are affected.
- [ ] The description includes risk, test evidence, rollback and AI assistance disclosure.

## Result

| Section | Checked | Findings |
| --- | --- | --- |
| A. Intent and scope | | |
| B. Tests | | |
| C. Control flow | | |
| D. Null and input | | |
| E. Failure handling | | |
| F. Concurrency | | |
| G. Security | | |
| H. Data and compatibility | | |
| I. Performance | | |
| J. Operability | | |
| K. Design | | |
| L. AI generated code | | |
| M. Documentation | | |

**Not reviewed:** <state it>

**Decision:** Approve / Request changes / Decline
