# Software factory (the system behind the skill)

Emperor Time is a **system disguised as a skill**. The skill file is the
front door. The job is **make software**, not emit code.

## Standing order

Given a repo and a loose task (or no task):

1. Resume from disk (`PLAN.md` / `PROGRESS.md` / `.emperor/state.md`) — do not restate.
   Load L0 super-context first (`scripts/emperor context l0` / `references/super-context.md`) before mass-grep. Inverted workspace: SOT fetch-only under `.emperor/sot/` (+ `plugins/`); PR work in `.emperor/artifacts/`; sandbox/runtime/env/secrets stubs — workspace≠repo.
2. If no task: `scripts/emperor queue next` (Python core `scripts/lib/queue.py`; WIP=1 via `--reject-multi-wip` / `--check-wip`; GitHub issues → Linear → `.emperor/queue.md`).
3. Scope it (G0/G1). Write DONE probes *before* code.
4. Design on disk. Build the smallest shippable change. TDD.
5. Verify with quoted tails. `scripts/emperor done` must exit 0.
6. Open a PR **only** with client consent (`EMPEROR_CONSENT_PR=1` or quoted yes).
7. Pick the next item. Stop when the queue is empty or the client says rest.

Steal consent-protocol: `scripts/emperor consent <task-dir>` — Python core `scripts/lib/consent.py` (`--reject-no-consent` / `--check-consent`; thin `consent.sh` / `consent.ps1`) refuses enlistment without CONSENT record. G4 calls it when steal activity is present.
Heal-and-verify: `scripts/emperor heal-verify <task-dir>` — Python core `scripts/lib/heal_verify.py` (`--reject-no-triad` / `--reject-no-postmortem` / `--check-heal`) refuses heal-done without triad + postmortem.
Super-context / thoughttrail: `scripts/emperor context` — Python cores `md_graph.py` / `context_store.py` / `thoughttrail.py` / `context.py` (+ `super_context.py` stubs). HARD-GATE `--reject-no-graph` / `--reject-no-trail` / `--check-context` / `--check-trail`. Aliases: thoughttrail, sandbox, sot, runtime, env, secrets.

Hetero-critique isolation: `scripts/emperor review-pack --check-isolation <task-dir>` — Python core `scripts/lib/review_pack.py` (`--reject-unisolated` / `--reject-author-diary` / `--check-isolation`) refuses unisolated / author-diary packs. G4 calls it when review-pack activity is present.

Forge (consent PR): `scripts/emperor forge <task-dir>` — Python core `scripts/lib/forge.py` (thin `forge.sh` / `forge.ps1`) owns consent, DONE probes, title/G1 PR body. Never invent a public PR without consent.

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

Compare to other SDLC models → `references/sdlc-comparison.md`.
