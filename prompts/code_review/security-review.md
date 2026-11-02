---
id: security-review
title: "Security Review"
category: code_review
skills: [security-reviewer]
---

# Security Review

## Problem it solves

Security defects are introduced in generated or hand-written code and not noticed.

## When to use

Code handles untrusted input, authentication, authorisation, secrets or data exposure.

## Required context

- Code or diff.
- Authentication and authorisation model.
- Scanner output if any.

## Prompt

Replace every `[BRACKETED PLACEHOLDER]` with real content (or attach the files and refer to them) and paste into your coding assistant.

```text
Review this change for security defects. This does not replace SAST, DAST, dependency scanning or specialist review.

Code or diff: [CODE]
Auth model (roles, resource ownership): [MODEL]
Scanner output (optional): [OUTPUT]

1. List trust boundaries and entry points. For each untrusted value, trace it to sinks: queries, shell commands, file paths, templates, deserialisers, redirects, logs, prompts to an LLM.
2. Check authentication on every operation and object-level authorisation (can user A access user B's resource by changing an ID?).
3. Check secrets, tokens and keys in code, config, logs and error messages; sensitive data exposure; insecure defaults.
4. Check cryptography use (vetted libraries only), randomness for security purposes, and password handling.
5. Check dependency and build risk only from the manifests provided.
6. For each finding give: severity, category (OWASP Top 10 item where applicable), location, a concrete exploit scenario, the fix and a regression test.
7. List what you could not verify and which tools or specialists should.
Do not claim the code is secure.
```

## Expected AI output

- Findings with exploit scenarios.
- Fixes and tests.
- Unverified areas.

## Validation steps

- [ ] Reproduce the exploit scenario against the old code.
- [ ] Run SAST and dependency scans.
- [ ] Specialist review for high-risk areas.

## Related skills

- [Security Reviewer](../../skills/security-reviewer/SKILL.md)

Back to [Code review prompts](README.md) · [Prompt library](../README.md)
