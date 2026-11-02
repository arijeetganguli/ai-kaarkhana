# Contributing to AI Kaarkhana

Thank you for helping. This project works best when practising engineers add what they have learned the hard way: a sharper skill, a prompt that actually worked, an example of a real defect, a correction to a chapter.

By taking part you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md). By contributing you agree that your contribution is licensed under the [MIT License](LICENSE).

## Ways to contribute

| You want to | Do this |
| --- | --- |
| Report a mistake or something unclear | Open an issue using the *docs improvement* form |
| Suggest a skill or a prompt | Open an issue using the *new skill* or *new prompt* form, then discuss before writing |
| Fix a typo or a broken link | Open a pull request directly |
| Add a skill, prompt, example or chapter | Follow the matching section below |
| Report a security problem in this repository's scripts or workflows | See [SECURITY.md](SECURITY.md); do not open a public issue |

Small, focused pull requests are reviewed faster than large ones. For anything bigger than a fix, please open an issue first so we can agree on scope.

## Ground rules

These apply to every contribution. They are also checked by [`scripts/validate_docs.py`](scripts/README.md) where a machine can check them.

1. **Be accurate and verifiable.** Do not invent statistics, benchmarks, results, quotes or tool capabilities. If you ran something, include the real output. If you did not, say that the snippet is illustrative.
2. **Label what can go stale.** Tool behaviour, versions and standards change. Say *what* was true and *when* you checked it, and link to the source.
3. **No copied material.** Do not paste proprietary text, copyrighted documentation or third party prompts without permission. Write in your own words and cite sources.
4. **Be tool agnostic.** Skills, prompts and handbook text must not depend on one vendor. Tool specific material belongs in [`tools/`](tools/README.md).
5. **Be actionable.** Every page should help someone do something. Prefer a checklist, a table or a worked example to general advice.
6. **No placeholders.** Pages must contain real content. The exception is templates in [`templates/`](templates/README.md), where `<angle bracket>` markers show what to fill in.
7. **Use relative links** for everything inside the repository, and make sure each one resolves. Images are local files; essential content never relies on remote images.
8. **Plain, direct language.** Short sentences, concrete examples, no hype. Use British or American spelling consistently within a page (the repository mostly uses British).
9. **Disclose AI assistance** in the pull request. AI generated content is welcome if you have read it, verified it and can stand behind it.

## Before you open a pull request

```bash
python scripts/validate_docs.py          # links, anchors, structure, SVGs, Mermaid, placeholders
python scripts/build_registry.py         # after changing a skill's front matter
python scripts/sync_adapters.py          # after changing a skill, a prompt or the principles
python scripts/build_registry.py --check
python scripts/sync_adapters.py --check
```

If you touched code under `examples/`, also run its tests (see [examples](examples/README.md)), and for the lab run `python scripts/verify_lab.py`.

CI runs the same checks. Generated files (`skills/REGISTRY.md`, `skills/registry.json`, `.github/skills/`, `.github/prompts/`, and the principles blocks in `AGENTS.md` and `.github/copilot-instructions.md`) are **never edited by hand**: change the canonical source and run the scripts.

## Add a skill

1. Copy [`templates/skill_template.md`](templates/skill_template.md) to `skills/<skill-name>/SKILL.md`.
2. The folder name and the `name` field must match, use lowercase letters, digits and single hyphens, and be at most 64 characters.
3. Write a `description` of at most 1024 characters that says **what the skill does and when to use it**. Assistants use this text to decide when to load the skill.
4. Fill in `metadata`: `activity`, `difficulty`, `frameworks` and `version`, all as strings. Allowed values are checked by the validator.
5. Keep all eleven sections, in order: Purpose, When to invoke, Required input, Execution instructions, Expected output, Validation checklist, Example usage, Sample prompts, Common mistakes, Related skills, Related resources.
6. Make the execution instructions concrete: numbered steps an assistant can follow, a defined output format, and a validation checklist a person can use to check the result.
7. Link to related skills, prompts and handbook chapters with relative links.
8. Run `python scripts/build_registry.py` and `python scripts/sync_adapters.py`, then add the skill to the table in [`skills/README.md`](skills/README.md). The validator fails if a skill is not linked there.

A good skill is narrow. If it needs "and" in its name, it is probably two skills.

## Add a prompt

1. Copy [`templates/prompt_template.md`](templates/prompt_template.md) to `prompts/<category>/<prompt-id>.md`. The file name without `.md` must equal the `id`, and the category must be the folder name.
2. List the skills it relates to in the front matter; they must exist.
3. Write a **complete prompt** in the first `text` code block under `## Prompt`. It must be usable after filling in the `[BRACKETED PLACEHOLDERS]`, without further rewriting.
4. Describe the **expected AI output** and give **validation steps**: how a person checks that the answer is good.
5. Add the prompt to the category README and to [`prompts/README.md`](prompts/README.md), then run `python scripts/sync_adapters.py` to generate the `.github/prompts` file.

## Add an example

- Put code under `examples/<language>/` using the existing scenario layout, with an `initial` version that has a real defect, an `improved` version, and tests for both.
- **Tests must pass.** Defect documenting tests assert the defective behaviour on purpose and are named so.
- Do not claim test counts or results you have not produced. Run the suite and report what it printed.
- For a new Broken Code Lab exercise, include `broken.py`, `solution.py`, tests that fail on `broken.py` and pass on `solution.py`, and a `CHALLENGE.md`. `python scripts/verify_lab.py` enforces this.
- Add the example to the matching README and to the [scenario catalogue](examples/scenarios.md) if it is a new scenario.

## Add or change a handbook chapter

1. Start from [`templates/handbook_chapter_template.md`](templates/handbook_chapter_template.md).
2. Keep the structure: title `# Chapter N: ...`, `## What you will learn`, numbered sections, `## Practice` and `## Related` (skills, prompts, workflows, examples, further reading).
3. Add or update the entry in [`handbook/README.md`](handbook/README.md).
4. Prefer a diagram, table or worked example to long prose. Mermaid diagrams must have quoted labels.
5. If you rename a heading, search for links to its anchor: `python scripts/validate_docs.py` reports broken anchors.

## Add a workflow

Use the structure of the existing files in [`workflows/`](workflows/README.md): when to use, starting inputs, a Mermaid diagram with gates, a sequence table (skill, prompts, developer responsibility, output), required outputs, validation checkpoints and completion criteria.

## Commit and pull request conventions

- One logical change per pull request. Describe *what* and *why*, and how you verified it.
- Use clear commit messages in the imperative: "Add edge case example for date ranges".
- Fill in the [pull request template](.github/PULL_REQUEST_TEMPLATE.md), including the AI disclosure.
- Respond to review comments by changing the work or explaining why not. Reviews are about the content, never about you.

## What reviewers look for

- Is it true, and can the reader verify it?
- Does it help someone make a better engineering decision, or do something concretely?
- Is it consistent with existing guidance, or does it contradict it? If it contradicts, which is right?
- Does it fit the repository structure and pass the validation checks?

## Questions

Open an issue with your question. If you are unsure whether something belongs here, ask before investing the time.
