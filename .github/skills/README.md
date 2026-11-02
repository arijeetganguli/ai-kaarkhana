# Generated skill copies for GitHub Copilot

The folders here are **generated** copies of the canonical skills in [`skills/`](../../skills/README.md), placed where GitHub Copilot discovers project skills (`.github/skills`; see [tools](../../tools/github_copilot/README.md)).

**Do not edit these files.** Edit `skills/<name>/SKILL.md`, then run:

```bash
python scripts/sync_adapters.py
```

CI runs `python scripts/sync_adapters.py --check` and fails if anything here differs from its source. Links inside the copies are rewritten for the extra directory depth, so they still resolve.

Browse the skills in the [registry](../../skills/REGISTRY.md).
