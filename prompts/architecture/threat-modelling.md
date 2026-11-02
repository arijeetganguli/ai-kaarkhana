---
id: threat-modelling
title: "Threat Modelling"
category: architecture
skills: [security-reviewer, architecture-reviewer]
---

# Threat Modelling

## Problem it solves

Security design is ad hoc and threats are found after release.

## When to use

Designing a feature that adds a trust boundary, handles sensitive data or integrates an LLM.

## Required context

- Feature description and data flows.
- Assets and actors.
- Existing controls.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Create a threat model for this feature. This is a starting point for a workshop with security specialists, not a certification.

Feature and data flow: [DESCRIPTION]
Assets (data, functions): [ASSETS]
Actors (including malicious ones): [ACTORS]
Existing controls: [CONTROLS]

1. List trust boundaries and data flows.
2. For each flow and component apply STRIDE (spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege). If an LLM is involved, include prompt injection, data exfiltration through tools, excessive agent permissions and unsafe output handling.
3. For each threat give: scenario, likelihood and impact (H/M/L with reasons, no invented numbers), existing control, gap and recommended mitigation.
4. Prioritise and mark which mitigations need tests, which need tooling (SAST, DAST) and which need a specialist.
5. List assumptions.
```

## Expected AI output

- Boundaries and flows.
- Threat table.
- Prioritised mitigations.
- Assumptions.

## Validation steps

- [ ] Security specialist review.
- [ ] Threats are traced to flows.
- [ ] Mitigations have owners and tests.

## Related skills

- [Security Reviewer](../../skills/security-reviewer/SKILL.md)
- [Architecture Reviewer](../../skills/architecture-reviewer/SKILL.md)

Back to [Architecture prompts](README.md) · [Prompt library](../README.md)
