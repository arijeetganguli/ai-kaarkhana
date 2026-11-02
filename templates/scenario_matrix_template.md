# Scenario matrix: <feature or rule>

> One row per distinguishable behaviour. The matrix is the test plan. Expected results come from the requirement, never from the implementation. If you cannot state the expected result, write `UNSPECIFIED` and raise a question.

| Field | Value |
| --- | --- |
| **Requirement** | REQ-<number> |
| **Owner** | <name> |
| **Approved by** | <name, date> |

## Scenarios

| ID | Category | Given (inputs and state) | When | Then (exact expected result) | Source | Test level | Test name | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SC-01 | Happy path | <concrete values> | <action> | <exact output or effect> | BR-1 | Unit | <test name> | Planned |
| SC-02 | Boundary: below | <value just below the limit> | <action> | <result> | BR-1 | Unit | | Planned |
| SC-03 | Boundary: at | <value at the limit> | <action> | <result> | BR-1 | Unit | | Planned |
| SC-04 | Boundary: above | <value just above the limit> | <action> | <result> | BR-1 | Unit | | Planned |
| SC-05 | Invalid input | <null, empty, wrong type, negative> | <action> | <specified error> | <who decided> | Unit | | Planned |
| SC-06 | Dependency failure | <timeout, 5xx, malformed> | <action> | <specified behaviour> | | Integration | | Planned |
| SC-07 | Duplicate or retry | <same request twice> | <action> | <idempotent result> | | Integration | | Planned |
| SC-08 | Unspecified | <situation> | <action> | `UNSPECIFIED` | Q1 | | | Blocked |

## Categories to consider

Use this list to check the matrix for gaps. Delete rows that do not apply, and say why.

- Typical values and the simplest case
- Boundaries: below, at, above each limit
- Empty, null, missing, whitespace only
- Wrong type, malformed, too long, special characters, encodings
- Negative, zero, very large numbers, overflow, rounding
- Collections: empty, one element, many, duplicates, order
- States and transitions: allowed and forbidden
- Time: time zones, daylight saving, leap days, clock skew, expiry
- Permissions: not signed in, wrong role, wrong owner, wrong tenant
- Concurrency: simultaneous requests, retries, duplicate delivery
- Dependencies: slow, down, wrong answer, unexpected status
- Resources: cleanup after failure, partial results
- Data: existing data that violates new rules

## Open questions

| # | Question | Blocks scenarios | Needed from | Answer |
| --- | --- | --- | --- | --- |
| Q1 | <question> | SC-08 | <person> | |

## Coverage check

| Requirement or rule | Scenarios | Gaps |
| --- | --- | --- |
| BR-1 | SC-01 to SC-04 | <none or description> |
