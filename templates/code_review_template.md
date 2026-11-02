# Code review: <pull request title or ID>

> Use this to record a review, whether done by a person, an assistant, or both. Findings need evidence (file and line). Silence is not approval: say what you did not review.

| Field | Value |
| --- | --- |
| **Reviewer** | <name> |
| **Author** | <name> |
| **Requirement** | <ID or link> |
| **Date** | <YYYY-MM-DD> |
| **Review type** | Human / AI assisted / Independent AI pass |

## 1. Scope of this review

**Reviewed:** <files, areas, aspects such as tests, security, performance>

**Not reviewed:** <what you did not look at, and why>

## 2. Summary verdict

Approve / Approve with minor comments / Request changes / Decline (too large to review)

<Two or three sentences.>

## 3. Gate status

| Gate | Status | Notes |
| --- | --- | --- |
| Build and unit tests | | |
| Lint, format, types | | |
| Security and dependency scans | | |
| No gate disabled or suppressed | | |

## 4. Test assessment

| Question | Answer |
| --- | --- |
| Do the tests specify the requirement (scenarios traced)? | |
| Are assertions exact (values, errors, side effects)? | |
| Were any assertions weakened, skipped or deleted? | |
| Could each important test fail? (checked by breaking the code or mutation testing) | |
| Is every real boundary exercised by an integration test? | |

## 5. Findings

| # | Severity | Location | Problem and consequence | Suggested direction | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | Blocker | <file:line> | <what is wrong and what it causes> | <direction or question> | Open |
| 2 | Major | | | | |
| 3 | Minor | | | | |
| 4 | Nit | | | | |
| 5 | Question | | | | |

Severity guide: **Blocker** incorrect behaviour, security flaw, data loss, broken contract. **Major** likely defect or serious gap. **Minor** real but low risk. **Nit** taste. **Question** needs an answer.

## 6. Areas checked

- [ ] Behaviour matches the requirement and scenarios
- [ ] Failure behaviour: nulls, empty, boundaries, exceptions, timeouts, resources
- [ ] Security: input, authorisation, secrets, dependencies
- [ ] Data and transactions
- [ ] API and schema compatibility
- [ ] Operability: logging, metrics, configuration, rollback
- [ ] Design and readability
- [ ] Documentation

## 7. Author explanations requested

| Question | Answer | Satisfactory? |
| --- | --- | --- |
| <e.g. why is this retried three times?> | | |

## 8. AI assistance in this review

- Assistant used for: <e.g. independent defect pass in a fresh session with requirement and diff>
- Findings from the assistant that I verified: <list>
- Findings I discarded for lack of evidence: <list>

## 9. Decision and conditions

<What must happen before merge. Who verifies. What was explicitly accepted as a known gap.>
