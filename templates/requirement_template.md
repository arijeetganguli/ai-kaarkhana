# Requirement: <short title>

> Copy this file next to the work (ticket, design folder or pull request) and fill it in. Delete this note. Anything you cannot fill in is a question, not a blank to be guessed by an assistant.

| Field | Value |
| --- | --- |
| **ID** | REQ-<number> |
| **Owner** | <person who can answer questions> |
| **Status** | Draft / Clarified / Approved |
| **Date** | <YYYY-MM-DD> |

## 1. Problem and goal

<Who has what problem, and what outcome do we want? One paragraph. No solution yet.>

## 2. Users and context

| Actor | Goal | Context |
| --- | --- | --- |
| <role> | <what they want> | <when and where> |

## 3. In scope

- <behaviour included>

## 4. Out of scope (non goals)

- <behaviour explicitly excluded, so nobody assumes it>

## 5. Business rules

| ID | Rule | Source | Confirmed by |
| --- | --- | --- | --- |
| BR-1 | <rule stated precisely, with units and boundaries> | <document, person, regulation> | <name, date> |

Write boundaries explicitly: "65 or older" and not "seniors".

## 6. Acceptance criteria

Use Given, When, Then, with concrete values.

```text
Given <precondition with concrete data>
When  <action>
Then  <observable outcome with exact values>
```

## 7. Failure and edge behaviour

| Situation | Required behaviour | Source |
| --- | --- | --- |
| <input is missing, invalid, out of range> | <reject with error X / default Y> | <who decided> |
| <dependency is slow or down> | <timeout, retry, degrade, fail> | |
| <duplicate request> | <idempotent behaviour> | |

Behaviour that is not decided goes in the open questions.

## 8. Non functional requirements

| Area | Requirement | Measure |
| --- | --- | --- |
| Performance | <e.g. response time target at stated load> | <how it will be verified> |
| Security and privacy | <authorisation, data handling> | |
| Availability and recovery | | |
| Compatibility | <API, data, client versions> | |
| Observability | <logs, metrics, alerts needed> | |

## 9. Open questions

| # | Question | Needed from | Status | Answer |
| --- | --- | --- | --- | --- |
| Q1 | <question that changes behaviour> | <person> | Open | |

## 10. Traceability

| Requirement or rule | Scenario ID | Test | Code |
| --- | --- | --- | --- |
| BR-1 | SC-1 | <test name> | <module> |

## 11. Assumptions and risks

- <assumption> (confirmed? yes or no)
- <risk and mitigation>
