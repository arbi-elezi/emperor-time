# Cursor adapter

Point Cursor project rules at repo-root `AGENTS.md` and `SKILL.md`.
The factory loop is identical to Codex and Claude. No Cursor-only religion.

## SessionStart equivalent (after clone)

Cursor has no Claude `SessionStart` hook. After clone (or when `.emperor/`
is missing), the agent should run silent boot once, then read what it wrote:

```bash
bash scripts/boot.sh   # or: pwsh -NoProfile -File scripts/boot.ps1
```

Then open:

- `.emperor/host.env` — os, shell, wsl, encoding
- `.emperor/survey.md` — artifact classes (do not ask the client their stack)
- `.emperor/eval.log` — when this tree *is* Emperor Time

Do not tell the client to run `identify` or `eval`. Those are internals.
Foreign/lost tree: `scripts/emperor identify <path>`.
