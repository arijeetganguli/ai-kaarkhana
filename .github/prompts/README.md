# Generated prompt files for GitHub Copilot

The `*.prompt.md` files here are **generated** from the 50 prompts in [`prompts/`](../../prompts/README.md), in the location and format that GitHub Copilot prompt files use (`.github/prompts`; see [tools](../../tools/github_copilot/README.md)). Each file's front matter holds a `description`; the body is the prompt text from the canonical file.

**Do not edit these files.** Edit `prompts/<category>/<id>.md`, then run:

```bash
python scripts/sync_adapters.py
```

CI runs `python scripts/sync_adapters.py --check` and fails if anything here differs from its source.

Replace each `[BRACKETED PLACEHOLDER]` before sending. Prompt files were described as public preview in IDEs when this was last checked; availability depends on your IDE and version. The canonical prompts, with context requirements, expected output and validation steps, are in the [prompt library](../../prompts/README.md).
