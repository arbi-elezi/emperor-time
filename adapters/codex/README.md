# Codex / AGENTS.md adapter

Emperor Time is not a Claude plugin. Drop the repo-root `AGENTS.md` where Codex
reads standing orders (`AGENTS.md` in the project root).

Then: `scripts/emperor queue next` or hand a loose task.

**Claim bar:** this path is **structure-clear** (AGENTS drop + silent boot +
MUST-route). **Equal-UX is HOLD** unless a dated field receipt shows the Codex
binary path green on a foreign ask. AGENTS.md+scripts alone is **not**
equal-UX-proven.

**Sibling hosts (not this thin drop):**
- OpenCode rich playbook: `adapters/opencode/` (ORI live stranger contract:
  `adapters/opencode/ORI-REGRESSION.md`)
- Cursor rich playbook: `adapters/cursor/`
- Grok rich playbook: `adapters/grok/`

Copilot CLI / Gemini CLI may still use the same root `AGENTS.md` as a thin
project-rules drop. Do not treat that as OpenCode/Cursor depth, and do not
fork the doctrine per vendor.

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

## Mid-model live (ORI)

When the ask needs a mid/flash live model route (not Codex equal-UX), use the
canonical stranger contract:
[`adapters/opencode/ORI-REGRESSION.md`](../opencode/ORI-REGRESSION.md)
(TTY-as-gate, named slug, no silent swap). Scope greed:
[`references/kill-hold.md`](../../references/kill-hold.md).
