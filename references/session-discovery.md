# Session discovery (locate card)

Emperor Time owned locate guidance for harness session transcripts.
Adapted from the locate aspect of [obra/superpowers](https://github.com/obra/superpowers)
`skills/diagnosing-superpowers/references/session-discovery.md` (MIT),
accessed 2026-09-27. ET + emperor-heal remain the orchestrator; do not load
whole diagnosing-superpowers.

Mechanical card: `scripts/emperor session-discovery`
(`scripts/lib/session_discovery.py`). Skill leaf:
`skills/emperor-heal/session-discovery.md`.

## Iron law

**No session claim without a VERIFIED absolute filesystem path.**

## How to locate

1. Take what the human partner named: session id, path, cwd, or timestamp window.
2. Prefer a supplied usable path — expand `~` and env vars; verify it exists.
3. Otherwise probe known harness roots (read-only):
   - Claude Code: `~/.claude/projects/` (cwd often encoded with `/` → `-`)
   - Cursor / agent: `$AGENT_TRANSCRIPTS`, `~/.cursor/projects/<name>/agent-transcripts`,
     `~/sand-data/agent-transcripts` (box layouts vary; mark ABSENT when missing)
4. Confirm identity with id + cwd + timestamps or matching conversation content.
   Recency alone is not confirmation. Distinguish parent sessions from children.
5. If history is missing, inaccessible, or ambiguous: state the specific
   limitation and ask for the missing path, export, or identifying detail.

## Honesty

| Status | Meaning |
|---|---|
| VERIFIED | File or directory exists on this host at the stated absolute path |
| ABSENT | Candidate path constructed but does not exist |
| UNVERIFIABLE | No candidate could be constructed (missing id/env/docs) |

Never invent transcript contents, token totals, or line counts. Establish
field meanings from observed records or documentation before calculating.

## HARD-GATE helper

```bash
scripts/emperor session-discovery --reject-guess   # always exit 1
```

Invoke when about to cite a session without a verified path.

## Out of scope here

- Full diagnosing-superpowers skill (analyst prompts, case/report templates, bundles)
- Embeddings / emperor.py dispatcher
- Mutating session files
