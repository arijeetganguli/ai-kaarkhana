---
applyTo: "prompts/**/*.md"
---

# Editing a prompt

`prompts/<category>/<id>.md` is the **canonical** source. `.github/prompts/` is generated from it; do not edit that folder.

- Front matter: `id` (equals the file name without `.md`), `title`, `category` (equals the folder), `skills` (existing skill folder names).
- The prompt text is the first fenced `text` block under `## Prompt`. The generator copies exactly that block, so write it to stand alone.
- A prompt must be specific: it names the task, the inputs as `[BRACKETED PLACEHOLDERS]`, the constraints, the output format, how to treat unknowns (list them, do not guess) and the evidence rule (report only results from commands actually run).
- Reject generic prompts such as "write clean code", "find bugs" or "review this code".
- Include validation steps that a person can perform without trusting the assistant.
- After editing run `python scripts/sync_adapters.py` and `python scripts/validate_docs.py`.
