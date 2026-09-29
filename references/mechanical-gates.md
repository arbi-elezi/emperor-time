# Mechanical gates

Judgment Chain is the *law*. These scripts are the *lock on the door*.
A model writing "G4 PASS" in markdown is not a gate. An exit code is.

## Scripts

| Script | Gate | Fails when |
|---|---|---|
| `scripts/gate.sh g0` (Python core) | G0 | no task dir, no client quote in ledger; ask→spec missing/incomplete (`ask_spec.py --require-spec` — never vacuous) |
| `scripts/gate.sh g1` | G1 | no acceptance criteria |
| `scripts/gate.sh g2` | G2 | non-trivial task missing work-order or Expected: lines |
| `scripts/gate.sh g3` | G3 | impact-map paths missing from `git diff --stat` (when in a git repo) |
| `scripts/gate.sh g4` | G4 | incomplete eight-count critique (via `critique.py`); missing CLAIM AUDIT / unfinished HYPOTHESIS\|TESTED (via `claim_audit.py`); steal no-consent (via `consent.py`); steal unquarantined (via `quarantine.py`); steal sign-in/dispatch/swarm (via `steal_flow.py`); Jail pin+consent (via `pin_consent.py`); over-verify thrash (via `proportionality.py`); unisolated / author-diary review-pack (via `review_pack.py`); VERIFIED without quote |
| `scripts/gate.sh g5` | G5 | verdict soft/missing citations / FAIL delivered; empty or theater Breach Register rows (via `verdict.py`); forge no-PR-consent when forge/PR claimed (via `forge.py`) |
| `scripts/review-pack.sh` (Python core) | G4 hetero isolation | cannot emit isolated pack; pack missing when hetero claimed; author diary / forbidden files / CoT in pack (`review_pack.py --reject-unisolated` / `--reject-author-diary` / `--check-isolation`) |
| `scripts/finish.sh` (Python core) | finish menu / suite-green | red suite / missing DONE probes (`finish.py --reject-red-suite` / `--require-green`; no menu until green) |
| `scripts/grill.sh` (Python core) | grill path taxonomy | path type missing / stage skipped / impl before stage approval (`grill.py --reject-no-path` / `--reject-stage-skip` / `--reject-impl-before-approval` / `--check-path`) |
| `scripts/diagnose.sh` (Python core) | diagnose report skeleton | missing report / theater problem / missing sessions / uncited findings (`diagnose.py --reject-no-report` / `--check-report`) |
| `scripts/queue.sh` (Python core) | queue multi-WIP | >1 in-progress / active `[~]` (`queue.py --reject-multi-wip` / `--check-wip`) |
| `scripts/consent.sh` (Python core) | Steal consent-protocol | missing CONSENT / header theater / uncovered enlisted agent (`consent.py --reject-no-consent` / `--check-consent`) |
| `scripts/steal-flow.sh` (Python core) | Steal sign-in / dispatch / swarm | missing SIGN-IN HANDOFF / runs layout / unbounded swarm (`steal_flow.py --reject-no-signin` / `--reject-no-dispatch-layout` / `--reject-unbounded-swarm` / `--check-signin` / `--check-dispatch` / `--check-swarm`) |
| `scripts/pin-and-consent.sh` (Python core) | Jail pin-and-consent | missing provenance pin / named-skill consent (`pin_consent.py --reject-unpinned` / `--reject-no-skill-consent` / `--check-pin-consent`) |
| `scripts/ask-spec.sh` (Python core) | ask→spec | missing goal/done-when/out-of-scope/effort_class (`ask_spec.py --reject-no-spec` / `--require-spec` always-on at G0+thrash; `--check-ask-spec` idle SKIP) |
| `scripts/proportionality.sh` (Python core) | proportionality / anti-loop | verify/critique/gate cycles exceed effort_class caps (`proportionality.py --reject-over-verify` / `--check-proportionality` / `--record-cycle`); missing class → tiny hard cap (`ensure_effort_class` / `bump_and_check` / `MISSING_CLASS_DEFAULTS_TINY`) |
| `scripts/heal-verify.sh` (Python core) | heal-and-verify triad + postmortem | missing Cure/No-new-wounds/Mechanism or postmortem (`heal_verify.py --reject-no-triad` / `--reject-no-postmortem` / `--check-heal`) |
| `scripts/reproduce.sh` (Python core) | reproduce-and-bisect fingerprint + combat ledger | missing fingerprint or combat ledger (`reproduce.py --reject-no-repro` / `--reject-no-combat-ledger` / `--check-reproduce`) |
| `scripts/triage.sh` (Python core) | holy triage block + snapshot | missing triage block or snapshot (`triage.py --reject-no-triage` / `--reject-no-snapshot` / `--check-triage`) |
| `scripts/process-heal.sh` (Python core) | holy process-healing register + re-entry | missing register or RE-ENTERED seam (`process_heal.py --reject-no-register` / `--reject-no-reentry` / `--check-process-heal`) |
| `scripts/context.sh` (Python core) | super-context + thoughttrail | missing graph/L0 or trail when claimed (`context.py --reject-no-graph` / `--reject-no-trail` / `--check-context` / `--check-trail`) |
| `scripts/forge.sh` (Python core) | G5 deliver / consent PR HARD-GATE | no PR consent (`forge.py --reject-no-pr-consent` / `--check-pr-consent`); DONE fail; gh missing → DRY |
| `scripts/eval.sh` (Python core) | harness health | an eval fixture fails |

Python core: `scripts/lib/gate.py` owns G0–G5. Thin twins: `scripts/gate.sh`,
`scripts/gate.ps1` (same exits). G2 still calls `work_order.py` for the plan
header **and** Task-N structure (`--reject-tbd` / `--reject-no-tasks` /
`--check-tasks`; thin `work-order.sh` / `work-order.ps1`). G4 calls
`critique.py` for the Judgment eight-count self-critique
(`--reject-incomplete-critique` / `--check-critique`; thin `critique.sh` /
`critique.ps1` + `self-critique` alias / `emperor critique`) — critique file
presence ≠ eight-count completeness. G4 calls `claim_audit.py` for the
Judgment claim-audit sweep (`--reject-unaudited` / `--check-audit`; thin
`claim-audit.sh` / `claim-audit.ps1` + `judgment-audit` alias / `emperor
claim-audit`). G4 also calls `consent.py` for Steal consent-protocol
(`--reject-no-consent` / `--check-consent`; thin `consent.sh` /
`consent.ps1` + `steal-consent` alias / `emperor consent`) — SKIP (vacuous) when no worker runs. G4 also calls `quarantine.py` for Steal quarantine
admission (`--reject-unquarantined` / `--check-quarantine`; thin
`quarantine.sh` / `quarantine.ps1` + `steal-quarantine` alias /
`emperor quarantine`) — SKIP (vacuous) when no worker runs. G4 also calls
`steal_flow.py` for Steal sign-in / dispatch / swarm (`--check-signin` /
`--check-dispatch` / `--check-swarm`; thin `steal-flow.sh` / `steal-flow.ps1`
+ aliases / `emperor steal-flow`) — SKIP (vacuous) when no matching markers.
G4 also calls
`review_pack.py` for hetero-critique isolation (`--reject-unisolated` /
`--reject-author-diary` / `--check-isolation`; thin `review-pack.sh` /
`review-pack.ps1` / `emperor review-pack`) — SKIP (vacuous) when no pack.
G5 calls `verdict.py` for Judgment verdict + Breach Register honesty
(`--reject-hidden-breach` / `--check-verdict`; thin `verdict.sh` /
`verdict.ps1` + `breach` alias / `emperor verdict`) — PASS-substring +
Breach Register header alone with blank/TBD rows is hidden-breach theater.
G5 also calls `forge.py` for forge PR-consent (`--reject-no-pr-consent` /
`--check-pr-consent`; thin `forge.sh` / `forge.ps1` / `emperor forge`) —
SKIP (vacuous) when no forge / public-PR markers (merge-locally OK). Steal
`--reject-no-consent` remains a different gate.

Review-pack Python core: `scripts/lib/review_pack.py` owns meta SHAs +
acceptance-criteria extract + diff **and** hetero-critique isolation HARD-GATE
(`--reject-unisolated` / `--reject-author-diary` / `--check-isolation`; thin
`review-pack.sh` / `review-pack.ps1`). G4 calls `--check-isolation` when
review-pack / hetero activity is present (SKIP vacuous otherwise). Closes
bash↔ps1 drift on criteria (ps1 used to dump the full work-order).

Dowse Python core: `scripts/lib/dowse.py` owns PATH detect + bounded version/auth probes + table/`--as-json` richer roster (thin `dowse.sh` / `dowse.ps1`). Closes bash↔ps1 drift on AsJson + Headless/SignIn metadata.

Finish Python core (`--check-suite` read-only probe — no effort-cycles stamp; `--require-green` still bumps verify for default-tiny): `scripts/lib/finish.py` owns ENV/MENU detect **and** suite-green HARD-GATE (`--reject-red-suite` / `--require-green` / `--check-suite`; thin `finish.sh` / `finish.ps1`) — integrates `done.py` probes and/or `eval.py`; menu-only finish without green is soft theater (Superpowers finishing Step 1).

Grill Python core (`--check-path` read-only probe — no effort-cycles stamp; `--advance` bumps critique when task markers present): `scripts/lib/grill.py` owns the brainstorm checklist card **and** path-taxonomy HARD-GATE (`--reject-no-path` / `--reject-stage-skip` / `--reject-impl-before-approval` / `--check-path`; thin `grill.sh` / `grill.ps1`) — spike | bounded | architectural + stage approval; questions-before-impl without path/stage lock is soft theater (Superpowers brainstorming HARD-GATE).

Diagnose Python core: `scripts/lib/diagnose.py` owns the diagnosing checklist card **and** cite-or-fail report skeleton HARD-GATE (`--reject-uncited` / `--reject-skip-intake` / `--reject-no-report` / `--check-citation` / `--check-report`; thin `diagnose.sh` / `diagnose.ps1`) — problem statement + session(s) + findings with path:line (or honest none-found); intake+cite without a report path is soft theater (Superpowers diagnosing Report step — not 7-analyst templates).

Queue Python core: `scripts/lib/queue.py` owns the work picker **and** multi-WIP HARD-GATE (`--reject-multi-wip` / `--check-wip`; thin `queue.sh` / `queue.ps1`) — WIP=1 on `[~]` active lines; `queue next` refuse alone is soft theater when agents skip the script.

Consent Python core: `scripts/lib/consent.py` owns Steal consent-protocol HARD-GATE (`--reject-no-consent` / `--check-consent`; thin `consent.sh` / `consent.ps1` + `steal-consent` alias / `emperor consent`) — CONSENT-header theater without `agent → role` is soft; forge `EMPEROR_CONSENT_PR` is not Steal enlistment consent.

Steal-flow Python core: `scripts/lib/steal_flow.py` owns Steal sign-in / dispatch / swarm HARD-GATE (`--reject-no-signin` / `--reject-no-dispatch-layout` / `--reject-unbounded-swarm` / `--check-signin` / `--check-dispatch` / `--check-swarm`; thin `steal-flow.sh` / `steal-flow.ps1` + aliases / `emperor steal-flow`) — silent/missing handoff, incomplete runs layout, or unbounded swarm is soft; G4 calls it when matching activity is present.

Blind secrets + workspace env Python cores: `scripts/lib/secrets_broker.py` + `workspace_env.py` (wired from `super_context.py`) own blind credentials HARD-GATE (`--reject-secret-leak` / `--check-env-redacted`; thin `secrets.sh` / `env.sh` + `emperor secrets` / `emperor env`) — agent sees names+status only; env show redacted; env sync merges SOT plugin overlays without echoing secrets.

Super-context Python core: `scripts/lib/context.py` (+ `md_graph.py` / `context_store.py` / `thoughttrail.py` / `super_context.py` stubs) owns graph-over-grep + thoughttrail HARD-GATE (`--reject-no-graph` / `--reject-no-trail` / `--check-context` / `--check-trail`; thin `context.sh` / `context.ps1` + aliases). Load L0 before mass-grep. No embeddings; no Graphify copy.

Heal-verify Python core: `scripts/lib/heal_verify.py` owns heal-and-verify HARD-GATE (`--reject-no-triad` / `--reject-no-postmortem` / `--check-heal`; thin `heal-verify.sh` / `heal-verify.ps1` + `heal-and-verify` alias / `emperor heal-verify`) — triad theater or missing postmortem is soft; entry still `emperor heal` four-phase.

Reproduce Python core: `scripts/lib/reproduce.py` owns reproduce-and-bisect HARD-GATE (`--reject-no-repro` / `--reject-no-combat-ledger` / `--check-reproduce`; thin `reproduce.sh` / `reproduce.ps1` + `reproduce-and-bisect` alias / `emperor reproduce`) — cause-isolated theater without fingerprint or combat ledger is soft; hands off to heal-verify for the close.

Triage Python core: `scripts/lib/triage.py` owns holy triage HARD-GATE (`--reject-no-triage` / `--reject-no-snapshot` / `--check-triage`; thin `triage.sh` / `triage.ps1` + `holy-triage` alias / `emperor triage`) — investigation theater without triage block or snapshot is soft; hands off to reproduce for cause isolation.

Process-heal Python core: `scripts/lib/process_heal.py` owns holy process-healing HARD-GATE (`--reject-no-register` / `--reject-no-reentry` / `--check-process-heal`; thin `process-heal.sh` / `process-heal.ps1` + `process-healing` alias / `emperor process-heal`) — process-heal theater without register entry or RE-ENTERED seam is soft; code damage left behind still routes triage → reproduce → heal-verify.

Forge Python core: `scripts/lib/forge.py` owns consent + DONE gate + title/G1 PR body **and** forge PR-consent HARD-GATE (`--reject-no-pr-consent` / `--check-pr-consent`; thin `forge.sh` / `forge.ps1`) — refuse-without-consent alone was soft theater vs card-style peers; Steal `--reject-no-consent` is separate. Closes bash↔ps1 drift on title extraction and ledger dump.

Harness health Python core: `scripts/lib/eval.py` owns the structural assertion
suite. Thin twins: `scripts/eval.sh`, `scripts/eval.ps1` (same exits 0/1).

## Activity-scoped vs always-on

Not every HARD-GATE runs on every task. Quoting a bare `PASS` from an idle
activity-scoped check is honesty theater — the gate was never exercised.

| Kind | Gates | Idle outcome |
|---|---|---|
| **Always-on** (when that G* runs) | G0 task/quote + ask→spec (`--require-spec`); G1 acceptance; G2 work-order; G3 impact-map; G4 critique eight-count + claim-audit; G5 verdict + Breach Register; ask→spec at G0 | No vacuous path — missing evidence FAILS |
| **Activity-scoped** (Steal / Jail / Holy + peers) | Steal consent / quarantine / sign-in / dispatch / swarm; Jail pin-and-consent; Holy triage / reproduce / heal-verify / process-healing; ask→spec `--check-ask-spec` idle honesty / proportionality; forge PR-consent; review-pack isolation; super-context / thoughttrail | No matching activity → **`SKIP (vacuous — no activity)`** (exit 0). Exercised green → **`PASS`**. Soft missing evidence while activity claimed → **`FAIL`**. |

Mechanical reporter: `scripts/lib/check_report.py` (`report_check`). Eval fixtures
force the label (`vacuous.md` / `task-vacuous` → SKIP; `*-ok` → PASS). Agents
must quote the SKIP/PASS line — do not paraphrase idle SKIP as "gate PASS".

## Vow mapping

- Vow of Evidence → G4 claim lint (VERIFIED rows need a quoted evidence cell) + claim-audit HARD-GATE (CLAIM AUDIT line; no HYPOTHESIS/TESTED)
- Steal Chain quarantine → G4 quarantine HARD-GATE (runs layout + CONJECTURE start + ADMITTED|REJECTED)
- Vow of Phases → gate order; `gate.sh g4` refuses if g2 never passed
- Vow of the Ledger → missing ledger is a hard fail
- Vow of Critique → G4 critique eight-count HARD-GATE (all eight axes + Checked evidence; file presence alone fails) + hetero-critique isolation HARD-GATE (review pack only; no author diary)
- Vow of Consent → Steal consent-protocol HARD-GATE (CONSENT + agent → role / EMPEROR_CONSENT_AGENTS / solo; G4 calls consent.py) + Steal sign-in/dispatch/swarm HARD-GATE (SIGN-IN HANDOFF + runs layout + bound swarm; G4 calls steal_flow.py) + Jail pin-and-consent HARD-GATE (source-url+hash + named-skill consent; G4 calls pin_consent.py) + ask→spec HARD-GATE (goal/done-when/out-of-scope/effort_class; G0 calls ask_spec.py `--require-spec`) + proportionality HARD-GATE (effort caps + cycle ledger; G4 calls proportionality.py) + forge PR-consent HARD-GATE (`--reject-no-pr-consent` / `--check-pr-consent`; G5 calls forge.py)
- Vow of Worthy Spend → lifespan section with empty "bought" is a warning, not a pass decoration
- Verdict / Stake of Retribution → G5 verdict + Breach Register HARD-GATE (deliverable Verdict with citations; no empty/theater Stake rows)

## What the agent must do

Before claiming a gate open, **run the script and paste the tail**.
Do not paraphrase `exit 0`. Quote it.
