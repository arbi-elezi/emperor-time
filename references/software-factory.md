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
Steal sign-in / dispatch / swarm: `scripts/emperor steal-flow <task-dir>` — Python core `scripts/lib/steal_flow.py` (`--reject-no-signin` / `--reject-no-dispatch-layout` / `--reject-unbounded-swarm` / `--check-signin` / `--check-dispatch` / `--check-swarm`; thin `steal-flow.sh` / aliases) refuses silent login / incomplete runs layout / unbounded swarm. G4 calls it when matching activity is present.

Ask→spec + proportionality: `scripts/emperor ask-spec --emit "<ask>" --write <task>/ask-spec.md` then `scripts/emperor proportionality --check-proportionality <task-dir>` — Python cores `scripts/lib/ask_spec.py` (`--reject-no-spec` / `--check-ask-spec / require-spec`) and `scripts/lib/proportionality.py` (`--reject-over-verify` / `--check-proportionality` / `--record-cycle` / `bump_and_check`; thin `ask-spec` / `proportionality` / `anti-loop`). G0 calls ask-spec `--require-spec`; G4 records a gate cycle and checks effort_class caps. Missing effort_class on critique/finish/grill defaults to tiny hard caps (`MISSING_CLASS_DEFAULTS_TINY`). Idle activity-scoped checks (Steal/Jail/Holy + forge/isolation/context/ask-spec/proportionality + SOT/sandbox) emit SKIP (vacuous — no activity), not bare PASS (see mechanical-gates activity-scoped table). SOT/sandbox: `emperor context --check-sot|--check-sandbox` / `--reject-mutated-sot` / `--reject-no-sandbox-plan`. Harness tool+force: `scripts/emperor harness-plan --emit --from <task> --write <task>/harness-plan.md` — Python core `scripts/lib/harness_plan.py` (`--reject-no-plan` / `--require-plan` / `--check-harness-plan` / `--check-forbidden` / `--reject-forbidden-used` / `--check-allowed` / `--reject-extra-tools` / `--check-caps` / `--reject-over-plan-caps` / `--check-class-tools` / `--reject-over-class-tools` / `--check-ask-class` / `--reject-class-mismatch` / `FORCE_TABLE`; thin `harness-plan` / `tool-force`). G0 calls `--require-plan` after ask→spec; G4 calls `--check-forbidden` / `--check-allowed` / `--check-caps` / `--check-class-tools` / `--check-ask-class` after proportionality (`FORBIDDEN_TOOLS_NEVER_RUN` / `ALLOWED_TOOLS_ONLY` / `PLAN_CAPS_BIND` / `CLASS_TOOLS_BIND` / `ASK_CLASS_BIND`); tiny → few tools + low caps + forbidden heavy paths. Harness owns selection — agent does not invent 20 verifications, thrash forbidden/unlisted tools, exceed plan Caps, upgrade force by rewriting a tiny plan to list tdd/work-order, or rewrite plan effort_class tiny→large to dodge CLASS_TOOLS_BIND. G4 critique/claim-audit/review-pack follow `g4_check_mode` (`HARNESS_DRIVES_G4_CHECKS`) so tiny does not force the eight-count or isolation museum; medium Tools require an isolated pack. G5 verdict citations follow the same `g4_check_mode` — tiny bare `Verdict: PASS` OK; Tools refuse `*: absent`.

Jail pin-and-consent: `scripts/emperor pin-and-consent <task-dir>` — Python core `scripts/lib/pin_consent.py` (`--reject-unpinned` / `--reject-no-skill-consent` / `--check-pin-consent`; thin `pin-and-consent.sh` / `pin-and-consent.ps1` + `jail-pin` alias) refuses bind/fire/adapt without provenance pin (source-url+hash) and named-skill client consent. G4 calls it when Jail pin activity is present.
Heal-and-verify: `scripts/emperor heal-verify <task-dir>` — Python core `scripts/lib/heal_verify.py` (`--reject-no-triad` / `--reject-no-postmortem` / `--check-heal`) refuses heal-done without triad + postmortem.
Reproduce-and-bisect: `scripts/emperor reproduce <task-dir>` — Python core `scripts/lib/reproduce.py` (`--reject-no-repro` / `--reject-no-combat-ledger` / `--check-reproduce`) refuses cause-isolated without fingerprint + combat ledger.
Holy triage: `scripts/emperor triage <task-dir>` — Python core `scripts/lib/triage.py` (`--reject-no-triage` / `--reject-no-snapshot` / `--check-triage`) refuses investigation without triage block + snapshot.
Holy process-healing: `scripts/emperor process-heal <task-dir>` — Python core `scripts/lib/process_heal.py` (`--reject-no-register` / `--reject-no-reentry` / `--check-process-heal`) refuses process-heal close without register entry + RE-ENTERED seam.
Super-context / thoughttrail: `scripts/emperor context` — Python cores `md_graph.py` / `context_store.py` / `thoughttrail.py` / `context.py` (+ `super_context.py` stubs). HARD-GATE `--reject-no-graph` / `--reject-no-trail` / `--check-context` / `--check-trail`. Aliases: thoughttrail, sandbox, sot, runtime, env, secrets.

Hetero-critique isolation: `scripts/emperor review-pack --check-isolation <task-dir>` — Python core `scripts/lib/review_pack.py` (`--reject-unisolated` / `--reject-author-diary` / `--check-isolation`) refuses unisolated / author-diary packs; follows `g4_check_mode` (`HARNESS_DRIVES_G4_CHECKS`) so Tools require pack, forbidden/unlisted SKIP, no plan → legacy activity-scoped. G4 calls `_run_review_isolation`.

Forge (consent PR) HARD-GATE: `scripts/emperor forge <task-dir>` — Python core `scripts/lib/forge.py` (`--reject-no-pr-consent` / `--check-pr-consent`; thin `forge.sh` / `forge.ps1`) owns consent, DONE probes, title/G1 PR body. G5 calls `--check-pr-consent`. Never invent a public PR without consent. Steal `--reject-no-consent` is separate.

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
