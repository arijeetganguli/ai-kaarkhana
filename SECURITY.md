# Security policy

## What this repository contains

AI Kaarkhana is mostly documentation: Markdown, SVG images, prompt and skill text. It also contains small runnable examples (`examples/`), deliberately defective teaching code (`examples/broken_code_lab/`), helper scripts (`scripts/`) and GitHub Actions workflows (`.github/workflows/`).

## Intentionally insecure code

The **Broken Code Lab** and the `initial` versions of the examples contain defects on purpose, such as SQL injection and race conditions. They exist for teaching and are not vulnerabilities in the project. **Do not copy them into production.** Reports that an intentionally defective teaching file is defective will be closed, but suggestions to make the explanation clearer are welcome as ordinary issues.

## What to report privately

Please report privately if you find:

- A vulnerability in `scripts/` (for example path traversal or arbitrary file writes in the adapter installer).
- A weakness in the GitHub Actions workflows (for example unsafe use of untrusted input or excessive permissions).
- A vulnerable dependency in `examples/` that affects people who run the examples as documented.
- Guidance in the handbook, a skill or a prompt that would lead readers to introduce a security vulnerability, or that recommends an unsafe practice.
- Secrets, credentials or personal data committed to the repository.

## How to report

Use GitHub's **private vulnerability reporting** for this repository (the *Security* tab, then *Report a vulnerability*). If that is not available, contact the maintainers privately through the contact method on the repository's profile. **Do not open a public issue** for a security problem.

Please include:

- What you found and where (file and line if possible).
- Steps to reproduce or a short proof of concept.
- The impact you believe it has.
- A suggested fix, if you have one.

## What to expect

This is a volunteer maintained project, so there is no guaranteed response time. Maintainers will aim to acknowledge a report, assess it, fix confirmed issues and credit you if you wish. Please allow a reasonable time to fix a problem before you disclose it publicly.

## Supported versions

Only the latest state of the default branch is maintained. Releases, when tagged, are listed in the [changelog](CHANGELOG.md).

## Using the guidance safely

The handbook's advice on AI assisted engineering is not a substitute for your organisation's security, privacy and legal requirements. In particular:

- Never paste secrets, credentials or personal data into an AI assistant.
- Treat AI generated code as untrusted until reviewed and tested.
- Combine AI review with static analysis, dependency scanning and expert review; never replace them.

See [Chapter 9: Security Engineering](handbook/09_security_engineering/README.md) for more.
