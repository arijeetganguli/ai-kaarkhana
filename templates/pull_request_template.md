# <Short, specific title>

> Template for pull request descriptions. Fill every section or write "n/a" with a reason. Do not claim anything you did not do.

## Summary

<What changed and why, in two or three sentences. Link the requirement or issue.>

Closes: <issue or requirement ID>

## Approach and trade offs

<Key decisions. Alternatives considered and why they were rejected.>

## Scope

**Included:** <...>

**Deliberately not included:** <...>

## Risk and impact

| Question | Answer |
| --- | --- |
| Who or what is affected? | <users, services, data> |
| Is any API, event or schema changed? | <yes or no; compatibility> |
| Is a migration involved? | <yes or no; staged how> |
| Blast radius if wrong | <description> |

## Test evidence

| Command run | Result |
| --- | --- |
| `<command>` | <e.g. 14 passed, 0 failed, 0 skipped> |

- New tests: <names and the scenarios they cover>
- Existing tests changed or removed: <none, or which and why>
- Edge cases covered: <list or link to the scenario matrix>
- **Not tested:** <gaps, stated honestly>

## Rollback

<How to undo this change. Is it safe? Point of no return, if any.>

## AI assistance

- [ ] No AI assistance was used.
- [ ] An assistant helped. Where: <e.g. first draft of tests and implementation>
- What I verified myself: <e.g. rewrote boundary tests from the requirement, ran the full suite, read every changed line>

## Checklist

- [ ] I can explain every changed line without the assistant.
- [ ] Tests were written or updated and fail without the change.
- [ ] No assertion was weakened, skipped or deleted without explanation.
- [ ] Failure behaviour (nulls, empty input, boundaries, errors, timeouts) was considered.
- [ ] No secrets, credentials or personal data in code, tests, logs or this description.
- [ ] New dependencies were checked: they exist, are maintained and are the intended packages.
- [ ] Documentation and changelog updated where needed.
- [ ] Self review completed; no debug code or unrelated edits.

## Screenshots or samples

<For user visible changes, or example requests and responses.>
