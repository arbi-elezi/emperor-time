# Software factory (the system behind the skill)

Emperor Time is a **system disguised as a skill**. The skill file is the
front door. The job is **make software**, not emit code.

## Standing order

Given a repo and a loose task (or no task):

1. Resume from disk (`PLAN.md` / `PROGRESS.md` / `.emperor/state.md`) — do not restate.
2. If no task: `scripts/emperor queue next` (GitHub issues → Linear → `.emperor/queue.md`).
3. Scope it (G0/G1). Write DONE probes *before* code.
4. Design on disk. Build the smallest shippable change. TDD.
5. Verify with quoted tails. `scripts/emperor done` must exit 0.
6. Open a PR **only** with client consent (`EMPEROR_CONSENT_PR=1` or quoted yes).
7. Pick the next item. Stop when the queue is empty or the client says rest.

A comment on the PR is a process failure. Prevent it: small diff, tests that
would fail if reverted, no drive-by refactors, no agent trailers, no leftover
TODOs in the shipped path.

## Not Claude-specific

Drop `AGENTS.md` (this repo's copy) into any harness. Codex, Cursor, Copilot,
OpenCode, Gemini, Kimi, Grok — same loop. Claude plugin.json is one adapter.

## Self-build adapters

If `gh` is missing and the client consented to network tools, add the thinnest
wrapper that lists issues. If Linear is the tracker and `LINEAR_API_KEY` is
set by the *client*, use it. Never invent a tracker when `.emperor/queue.md`
works. Never store tokens in the repo.
