# Cursor adapter

Point Cursor project rules at repo-root `AGENTS.md` and `SKILL.md`.
The factory loop is identical to Codex and Claude. No Cursor-only religion.

## Session boot (host-agnostic)

Cursor has no Claude `SessionStart` hook. Do not ask the client their OS,
shell, or language. After clone (or when `.emperor/` is missing), run silent
boot once, then read what it wrote:

```bash
bash scripts/boot.sh   # or: scripts/emperor boot
# zsh:  zsh scripts/emperor.zsh boot   (same silent-boot contract)
# Windows: pwsh -NoProfile -File scripts/boot.ps1
#          (or: pwsh -NoProfile -File scripts/emperor.ps1 boot)
```

Then open:

- `.emperor/host.env` — os, shell, wsl, encoding (+ win_interop/mnt when present)
- `.emperor/survey.md` — artifact classes (do not ask the client their stack)
- `.emperor/eval.log` — when this tree *is* Emperor Time

Resume from STATE.md / `scripts/emperor queue next`. Do not tell the client
to run `identify` or `eval`. Those are internals.
Foreign/lost tree: `scripts/emperor identify <path>`.

On Windows, `scripts/emperor.ps1 <tool>` silent-boots when `.emperor/host.env`
is missing — same contract as `scripts/emperor` (bash) and `scripts/emperor.zsh`.

## MUST-route (before creative work)

Silent boot is not enough. Before clarifying questions, exploring, or writing
code, open one governing file from the `SKILL.md` tables, or run
`scripts/emperor route "<utterance>"` / `scripts/emperor activate` and open
`ACTIVATION next=`. Same bite as Claude SessionStart MUST-route; Emperor Time
stays the orchestrator (no foreign master router).
