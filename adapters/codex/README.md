# Codex / AGENTS.md adapter

Emperor Time is not a Claude plugin. Drop the repo-root `AGENTS.md` where Codex
reads standing orders (`AGENTS.md` in the project root).

Then: `scripts/emperor queue next` or hand a loose task.

Same files work for Copilot CLI, Gemini CLI, OpenCode, and Cursor
(as project rules). Grok Build has its own rich playbook: `adapters/grok/`
(skills under `~/.grok/skills/` and `./.grok/skills/`, plus this AGENTS.md
path). Do not fork the doctrine per vendor.

## Session boot (host-agnostic)

Codex has no Claude `SessionStart` hook. Do not ask the client their OS,
shell, or language. After clone (or when `.emperor/` is missing), run silent
boot once, then read what it wrote:

```bash
bash scripts/boot.sh   # or: scripts/emperor boot
# Windows: pwsh -NoProfile -File scripts/boot.ps1
```

Then open:

- `.emperor/host.env` — os, shell, wsl, encoding
- `.emperor/survey.md` — artifact classes (do not ask the client their stack)
- `.emperor/eval.log` — when this tree *is* Emperor Time

Resume from STATE.md / `scripts/emperor queue next`. Do not tell the client
to run `identify` or `eval`. Those are internals.
Foreign/lost tree: `scripts/emperor identify <path>`.

## MUST-route (before creative work)

Silent boot is not enough. Before clarifying questions, exploring, or writing
code, open one governing file from the `SKILL.md` tables, or run
`scripts/emperor route "<utterance>"` / `scripts/emperor activate` and open
`ACTIVATION next=`. Same bite as Claude SessionStart MUST-route; Emperor Time
stays the orchestrator (no foreign master router).

