# Session discovery — locate transcript paths HARD-GATE

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/diagnosing-superpowers/references/session-discovery.md
- source-hash: sha256:6d1dced083e5d978448a78df298cf515531b0eb39b2854a4a2afbffeb69a7435
- heading: Discover the session history (locate / verify-path aspect)
- license: MIT
- access-date: 2026-09-27
- issue-context: diagnosing-superpowers needs verified transcript paths before analysis; ET lacked a mechanical locate card. Chain Jail extract-aspect names locate+honesty only (not whole diagnosing-superpowers, not analyst prompts, not GitHub issue templates).

**Contract:** before citing session history or starting a diagnosis that needs transcripts, resolve each session to a **VERIFIED** absolute filesystem path. Expand home-directory shorthand and env vars. Confirm identity with session id, working directory, timestamps, or matching content — recency alone is not confirmation. Emperor Time stays the orchestrator via emperor-heal; do **not** announce or load whole `diagnosing-superpowers`.

Mechanical card: `scripts/emperor session-discovery` (Python: `scripts/lib/session_discovery.py`).
Companion reference: `references/session-discovery.md`.
Full diagnosing skill folder is **out of scope** until this locate core is solid.

## HARD-GATE — The Iron Law

```
NO SESSION CLAIM WITHOUT VERIFIED PATH
```

No path on disk? **Stop.** Ask for the missing path, export, or identifying detail. Do not invent transcript contents or numbers.

## Locate steps

1. **Accept identifiers** — session id, explicit path, and/or cwd hint from the human partner.
2. **Probe harness roots (read-only)** — Claude Code `~/.claude/projects`, Cursor / agent transcript roots (`AGENT_TRANSCRIPTS`, `~/.cursor/projects/*/agent-transcripts`, `~/sand-data/agent-transcripts`), plus `--path` override.
3. **Mark honesty** — `VERIFIED` only when the file/dir exists; otherwise `ABSENT` or `UNVERIFIABLE` with a concrete reason.
4. **Reject guesses** — `scripts/emperor session-discovery --reject-guess` always fails (HARD-GATE when about to claim a session without a verified path).
5. **Record** — ledger the exact sources, rejected candidates, and unresolved gaps. Subsequent readers reuse that record.

## Rationalizations (refuse)

| Excuse | Reality |
|---|---|
| "The latest session is probably it" | Recency alone is not confirmation. |
| "I remember what happened" | Memory is rumor; quote a VERIFIED path. |
| "Missing field means zero tokens" | Do not invent numbers; state UNVERIFIABLE. |
| "I'll diagnose first, find paths later" | Locate before analysis. |

## ET mapping

| Step | ET home |
|---|---|
| Locate / verify path | emperor-heal + `emperor session-discovery` |
| Debug after locate | emperor-heal debug-four-phases |
| Resume from disk state (not transcripts) | emperor-resume |
| Evidence claims | emperor-verify / evidence |

## MUST-NOT

- Vendor or load whole diagnosing-superpowers
- Modify, move, or delete session files (read-only)
- Invent transcript contents, line counts, or token totals
