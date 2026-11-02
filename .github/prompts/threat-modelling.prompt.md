---
description: "Threat Modelling: Security design is ad hoc and threats are found after release."
---
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

---
Generated from [prompts/architecture/threat-modelling.md](../../prompts/architecture/threat-modelling.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
