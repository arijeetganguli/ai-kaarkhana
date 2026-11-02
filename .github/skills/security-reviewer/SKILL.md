---
name: security-reviewer
description: "Use when reviewing code or a design for security defects: injection, broken authentication and authorisation, secrets, unsafe deserialisation, sensitive data exposure, dependency risk and prompt injection. Complements, never replaces, SAST, DAST and expert review."
license: MIT
metadata:
  activity: security
  difficulty: intermediate
  frameworks: "any"
  version: "1.0"
---

# Security Reviewer

## Purpose

Find likely security defects early with specific evidence and remediation, and identify what needs specialist or tool-based verification.

## When to invoke

- Code handles user input, authentication, authorisation, files, queries, secrets or external content.
- AI-generated code touches security-sensitive paths.
- A feature adds a new trust boundary or an LLM that reads untrusted content.

## Required input

- Code or diff, and the data flow: where input enters, where it is used.
- Authentication and authorisation model, roles and resource ownership rules.
- Output of SAST, dependency and secret scanners, if available.

If a required input is missing, ask for it. Do not guess.

## Execution instructions

1. Identify trust boundaries and entry points: HTTP parameters, headers, files, messages, environment, LLM inputs and tool outputs.
2. Trace each untrusted value to sinks: queries, shell commands, file paths, templates, deserialisers, redirects, logs, model prompts.
3. Check authentication and authorisation at each operation, including object-level ownership checks (can user A read user B's record?).
4. Check secrets and configuration: hard-coded credentials, keys in logs or error messages, overly broad permissions.
5. Check cryptography and data protection: use of vetted libraries, no custom crypto, sensitive data minimised and masked in logs.
6. Check dependencies and build: known vulnerable versions, unpinned or untrusted sources.
7. For LLM features: check prompt injection paths, tool permissions, output handling and data leakage.
8. Report findings with severity, exploit scenario, location and remediation, and list what must be verified by tools or a security specialist.

## Expected output

- Findings table: severity, category (e.g. OWASP Top 10 item), location, exploit scenario, fix.
- Fix proposals with a regression test per finding.
- Items requiring SAST, DAST, dependency scan or specialist review.
- Assumptions about the deployment and threat model.

## Validation checklist

- [ ] Each finding has a plausible exploit scenario, not just a pattern match.
- [ ] Object-level authorisation was considered, not only login.
- [ ] Untrusted data was traced to sinks.
- [ ] No claim of 'secure' or 'no vulnerabilities'; limits of the review are stated.
- [ ] Fixes include tests that fail before and pass after.

## Example usage

Input:

> `cursor.execute("SELECT * FROM users WHERE name = '" + name + "'")`

Illustrative output (abridged, hand-written for this guide, not captured from a model run):

```text
High, injection (OWASP A03): `name` reaches SQL by concatenation. Payload `' OR '1'='1` returns all users.
Fix: parameterised query `cursor.execute("SELECT ... WHERE name = ?", (name,))`.
Test: lookup with the payload returns no rows.
Needs tooling: run SAST over the repo for other concatenated queries.
```

## Sample prompts

```text
Act as the Security Reviewer. Identify trust boundaries and untrusted inputs in this change, trace each to its sinks, and check authentication, object-level authorisation, secrets and data exposure. For each finding give severity, exploit scenario, location, fix and a regression test. State what you could not verify and which tools should. Code: [CODE]. Auth model: [AUTH MODEL]
```

## Common mistakes

- Declaring code secure without tools or a threat model.
- Checking that users are logged in but not that they own the object.
- Recommending a fix that merely blocks the demo payload (denylist) rather than the class of defect.
- Pasting secrets or production data into an AI prompt while investigating.

## Related skills

- [Defensive Programming Reviewer](../defensive-programming-reviewer/SKILL.md)
- [API Contract Reviewer](../api-contract-reviewer/SKILL.md)
- [Architecture Reviewer](../architecture-reviewer/SKILL.md)

## Related resources

Handbook:

- [Chapter 9: Security Engineering](../../../handbook/09_security_engineering/README.md)

Prompts:

- [Security Review](../../../prompts/code_review/security-review.md)
- [Threat Modelling](../../../prompts/architecture/threat-modelling.md)

Workflows:

- [Build a new feature](../../../workflows/01_feature_development.md)
- [Introduce a new API](../../../workflows/04_new_api.md)
- [Review a pull request](../../../workflows/09_pull_request_review.md)

Examples:

- [examples/broken_code_lab/07_sql_injection/CHALLENGE.md](../../../examples/broken_code_lab/07_sql_injection/CHALLENGE.md)
