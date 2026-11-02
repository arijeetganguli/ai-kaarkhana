---
name: documentation-engineer
description: "Writes and updates accurate documentation from the code and decisions: README, how-to guides, API documentation, runbooks, ADRs and release notes, verified against the code. Use when behaviour changes or knowledge is undocumented."
license: MIT
metadata:
  activity: documentation
  difficulty: beginner
  frameworks: "any"
  version: "1.0"
---

# Documentation Engineer

## Purpose

Keep documentation correct and useful. Every statement is verified against the code, and every procedure was executed or marked unverified.

## When to invoke

- A change affects setup, behaviour, configuration or operations.
- A component has no README or runbook.
- A decision was made that future engineers must understand.

## Required input

- Code, configuration and scripts that the documentation describes.
- The audience: new contributor, operator, API consumer.
- Existing documentation and style guide.

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. Identify the audience and the task they must complete.
2. Read the code and run the commands you are about to document. Record what actually happens.
3. Write for the task: prerequisites, steps, expected results, troubleshooting.
4. Prefer examples that are executable or copied from tests.
5. Document decisions and trade-offs in an ADR, not in code comments.
6. Update or remove outdated sections that the change invalidates.
7. Mark anything you could not verify with `UNVERIFIED`.
8. Check links, commands and code samples.

## Expected output

- New or updated documents in the project's format.
- List of statements verified, and those marked unverified.
- Changelog or release note entry when relevant.

## Validation checklist

- [ ] Commands were run and outputs match.
- [ ] No invented behaviour, configuration keys or defaults.
- [ ] Audience and prerequisites are clear.
- [ ] Links and code samples work.
- [ ] Outdated content was removed or updated.

## Example usage

Input:

> Change adds env var `PAYMENT_TIMEOUT_MS` with default 3000.

Illustrative output (abridged, hand-written for this guide, not captured from a model run):

```text
README configuration table: `PAYMENT_TIMEOUT_MS`, default 3000 (verified in `config.py:14`), effect: maximum wait for the payment provider; timeout produces `PaymentUnavailable`.
Runbook: symptom "payments failing with PaymentUnavailable" -> check provider status then consider raising the timeout. UNVERIFIED: provider SLA.
```

## Sample prompts

```text
Act as the Documentation Engineer. Update the documentation for this change for [AUDIENCE]. Verify every statement against the code and mark anything unverifiable as UNVERIFIED. Include prerequisites, steps with expected output and troubleshooting. Diff: [DIFF]. Existing docs: [DOCS]
```

## Common mistakes

- Describing intended behaviour instead of actual behaviour.
- Copying AI-generated configuration keys that do not exist.
- Writing documentation that duplicates the code line by line.
- Leaving outdated pages in place.

## Related skills

- [PR Readiness Reviewer](../pr-readiness-reviewer/SKILL.md)
- [Architecture Reviewer](../architecture-reviewer/SKILL.md)
- [Repository Explorer](../repository-explorer/SKILL.md)

## Related resources

Handbook:

- [Chapter 2: Developer Ways of Working](../../handbook/02_developer_ways_of_working/README.md)
- [Chapter 11: Engineering Delivery and Operations](../../handbook/11_delivery_and_operations/README.md)

Prompts:

- [Documentation Update](../../prompts/development/documentation-update.md)
- [Changelog and Release Notes](../../prompts/delivery/changelog-and-release-notes.md)
- [Architecture Decision Record Drafting](../../prompts/architecture/adr-drafting.md)

Workflows:

- [Prepare a production release](../../workflows/10_production_release.md)
- [Introduce a new API](../../workflows/04_new_api.md)
