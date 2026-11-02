# Claude Code instructions

@AGENTS.md

## Claude Code notes

- The skills in `skills/` are the canonical copies. Claude Code discovers project skills in `.claude/skills/`; this repository does not commit a copy there. To use the skills in a project, install them with `python scripts/sync_adapters.py install --target claude-code --dest <project>` (see `tools/claude_code/README.md`).
- Import syntax verified against the Claude Code memory documentation on 2026-11-02; check the current documentation if behaviour differs in your version.
