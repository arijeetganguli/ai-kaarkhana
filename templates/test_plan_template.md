# Test plan: <feature or change>

> Plan the evidence before you generate the tests. A plan is not paperwork: it is the answer to "how will we know this works, and how will we know the tests are any good?".

| Field | Value |
| --- | --- |
| **Owner** | <name> |
| **Requirement and scenario matrix** | REQ-<number>, scenario matrix <location> |
| **Date** | <YYYY-MM-DD> |

## 1. Scope

**In scope:** <behaviour and components under test>

**Out of scope:** <what is not tested here and why>

## 2. Risk assessment

| Area | Risk | Likelihood | Impact | Test emphasis |
| --- | --- | --- | --- | --- |
| <e.g. discount calculation> | <wrong rounding> | | | Boundary and property tests |
| <e.g. payment call> | <duplicate charge on retry> | | | Idempotency integration test |

## 3. Test levels

| Level | Purpose | Scenarios covered | Tooling | Run when |
| --- | --- | --- | --- | --- |
| Unit | Logic and rules in isolation | SC-01 to SC-07 | <JUnit 5 / pytest / Vitest> | Every commit |
| Integration | Real boundaries: database, HTTP, messaging | SC-08 to SC-12 | <test containers, local stub server> | Every pull request |
| Contract | Shape and semantics shared with other services | <list> | <tool> | Every pull request |
| End to end | A few critical journeys | <list> | <tool> | Before release |
| Non functional | Performance, security, resilience | <list> | <tools> | Scheduled |

## 4. Test data

| Need | Source | Notes |
| --- | --- | --- |
| Valid baseline entities | Builders with valid defaults | No production data |
| Invalid and edge data | Builder overrides | Listed per scenario |
| Time and randomness | Injected clock and seed | No sleeping |

## 5. Environments and dependencies

| Dependency | How it is provided in tests | Fidelity limit |
| --- | --- | --- |
| <database> | <container of the same engine and version> | <differences from production> |
| <third party API> | <local stub server> | <behaviour not covered> |

## 6. Test strength checks

| Check | Method | Target |
| --- | --- | --- |
| Tests can fail | Break the code on purpose and confirm red | Each critical rule |
| Assertion quality | Review; mutation testing on changed critical code | <survivors triaged> |
| Coverage of changed code | Coverage report | <threshold chosen by the team> |
| Flakiness | Repeat and shuffle | No failures |

## 7. Entry and exit criteria

**Entry:** requirement clarified, scenario matrix approved, environments available.

**Exit:**

- [ ] Every scenario is covered or recorded as deferred with a reason.
- [ ] Suite passes, output attached.
- [ ] No test weakened or deleted without a stated reason.
- [ ] Mutation survivors on critical logic triaged.
- [ ] Known gaps listed below.

## 8. Known gaps and risks accepted

| Gap | Reason | Accepted by |
| --- | --- | --- |
| <not tested> | <why> | <name> |

## 9. Results

| Date | Command | Result (counts) | Notes |
| --- | --- | --- | --- |
| <YYYY-MM-DD> | <command run> | <passed / failed / skipped> | <link to output> |

Record real results only.
