---
applyTo: "skills/**/SKILL.md"
---

# Editing a skill

`skills/<name>/SKILL.md` is the **canonical** source. Do not edit `.github/skills/` (generated).

- Front matter: `name` equals the folder name (lowercase letters, digits, single hyphens), `description` states what the skill does and when to use it (at most 1024 characters), `license: MIT`, and a `metadata` map whose values are all strings: `activity`, `difficulty`, `frameworks`, `version`.
- Sections in order: Purpose, When to invoke, Required input, Execution instructions, Expected output, Validation checklist, Example usage, Sample prompts, Common mistakes, Related skills, Related resources.
- Execution instructions are numbered, imperative and verifiable. The skill must refuse to guess missing input.
- Any example output that is not captured from a real run must be labelled illustrative.
- Keep the skill tool agnostic. Tool specific notes belong in `tools/`.
- Links to other repository content use `../../<path>` (the skill folder is two levels below the root); links to other skills use `../<skill>/SKILL.md`.
- After editing run `python scripts/build_registry.py`, `python scripts/sync_adapters.py` and `python scripts/validate_docs.py`.
