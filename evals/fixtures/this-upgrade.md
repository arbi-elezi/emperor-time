# Task Ledger — emperor-time self-application (condition-based-waiting HARD-GATE)

- **Task:** Add condition-based-waiting HARD-GATE leaf for emperor-heal (Wait for the actual condition / not a guess about timing): Python card + thin twins + skill/reference + route/eval/honesty lockstep. Companion for flaky/timing waits (heal Phase 4).
- **Client quote:** Soft-ET consented Worthy Spend after v0.4.40 defense-in-depth. Ship condition-based-waiting leaf (v0.4.41). Chain Jail leaf only; do not vendor foreign whole skills.
- **Origin:** assigned
- **Size:** standard
- **Governing files:** SKILL.md → emperor-heal → condition-based-waiting.md → condition_wait.py → route/triggers → eval
- **Tip at spend:** v0.4.41 (branch `et-manager/condition-based-waiting`)

## G0
Quoted ask above. Ambiguity resolved: ship condition-based-waiting HARD-GATE only. Skip embeddings, emperor.py dispatcher, full systematic-debugging vendoring, find-polluter, pressure packs, other archaeology pins this turn. Do not re-announce or re-ship #33–#57 leaves.

## G1 Acceptance criteria
1. SKILL.md version ≥ 0.4.41; `scripts/lib/condition_wait.py` prints WAIT / COND / MUST card.
2. Thin `condition-wait.sh` / `condition-wait.ps1` call `condition_wait.py`; emperor peers (bash/ps1/cmd/zsh) gain `wait`.
3. `--reject-sleep` and `--reject-unguessed` always exit non-zero; `--check-condition` accepts real condition waits and rejects bare sleeps.
4. Skill leaf `skills/emperor-heal/condition-based-waiting.md` + `references/condition-based-waiting.md` cite obra/superpowers systematic-debugging condition-based-waiting.md (URL + access date 2026-09-27 + sha256).
5. Route triggers include CBW phrases → emperor-heal; extract-aspect names the leaf.
6. Catalog + heal SKILL + debug-four-phases link the card; bakeoff + honesty name condition_wait.py / wait.
7. Plugin/marketplace/SKILL lockstep 0.4.41; CHANGELOG has 0.4.41.
8. Eval locks new files/version/triggers; suite green.
9. Live defect-rate vs Superpowers stays **UNVERIFIABLE**.

## Out of scope
- embeddings / emperor.py unified dispatcher
- Full systematic-debugging skill vendoring (find-polluter, pressure tests)
- Other people's PRs
- Another archaeology language pin this turn
- Live multi-vendor bake-off numbers
- Redo of #33–#57

## G2
Rejected alternative: vendor whole systematic-debugging under skills/.
Why: standing rule — Chain Jail leaf only (HARD-GATE card + one aspect heading + route/eval locks).

Rejected alternative: emperor.py unified dispatcher.
Why: larger surface than one heal leaf; out of scope.

Rejected alternative: find-polluter.sh or pressure/academic packs this turn.
Why: explicitly deferred; CBW is the named deferred companion after defense-in-depth.

## G3
condition_wait.py + condition-wait twins + condition-based-waiting.md + references + route/eval/honesty/bakeoff lockstep on `et-manager/condition-based-waiting`. See git log.

## G4
Claims:

| Claim | Status | Evidence |
|---|---|---|
| SKILL.md is 0.4.41 orchestrator | TESTED | frontmatter `version: 0.4.41` on branch HEAD |
| condition_wait.py prints WAIT checklist | TESTED | `WAIT checklist=yes` + COND / MUST lines |
| --reject-sleep / --reject-unguessed hard-gate | TESTED | exit non-zero + REJECT lines |
| --check-condition needs real condition signal | TESTED | CONDITION OK / CONDITION FAIL paths |
| Jail leaf cites Superpowers condition-based-waiting | TESTED | condition-based-waiting.md URL + 2026-09-27 + sha256 |
| Route CBW phrases → heal | TESTED | route.py + triggers.json |
| Eval suite still green | TESTED | `bash scripts/eval.sh` → EVALS PASSED |
| Live defect-rate vs Superpowers | UNVERIFIABLE | no shared-task three-vendor bake-off run in this session |

## Verdict
PASS-WITH-CONDITIONS: local mechanism TESTED; live bake-off numbers UNVERIFIABLE.

## Breach Register
- bash/ps1 gate twins drifted. Remediation: gate.py (v0.4.16).
- bash/ps1 identify twins drifted. Remediation: identify.py (v0.4.17).
- bash/ps1 finish twins drifted. Remediation: finish.py (v0.4.18).
- bash/ps1 eval twins drifted. Remediation: eval.py (v0.4.19).
- route missed Fortran extensions. Remediation: triggers + thin twins (v0.4.20).
- bash/ps1 done twins duplicated probe runner. Remediation: done.py (v0.4.21).
- emperor.zsh missing silent-boot / identify / excavate specials vs bash. Remediation: v0.4.22.
- bash/ps1 queue twins reimplemented picker (list Linear/git guard drift). Remediation: queue.py (v0.4.23).
- bash/ps1 forge twins drifted (title hardcoded; full ledger dump). Remediation: forge.py (v0.4.24).
- bash/ps1 review-pack twins drifted (criteria full work-order dump). Remediation: review_pack.py (v0.4.25).
- bash/ps1 dowse twins drifted (AsJson + richer roster on ps1 only). Remediation: dowse.py (v0.4.26).
- receiving-code-review companion never extracted after request-review. Remediation: receive.py (v0.4.27).
- CHANGELOG missed 0.4.27 entry on #44; emperor.cmd missed receive peer. Remediation: v0.4.28 hygiene.
- executing-plans continuous-execution card never extracted after writing-plans/finish. Remediation: execute.py (v0.4.28).
- subagent-driven-development fresh-subagent / per-task-review card never extracted after executing-plans. Remediation: subagent.py (v0.4.29).
- dispatching-parallel-agents independent-domains card never extracted after subagent-driven. Remediation: parallel.py (v0.4.30).
- bash/ps1 install twins drifted (chain preview order; dowse.sh vs dowse.ps1 tip). Remediation: install.py (v0.4.31).
- bash/ps1 silent-boot host report drifted (encoding + WSL interop probes). Remediation: host.py + boot.py (v0.4.32).
- bash/ps1 worktree create twins reimplemented mutate path. Remediation: worktree.py (v0.4.33).
- excavate thin aliases hopped identify.sh/ps1 instead of identify.py. Remediation: v0.4.34.
- archaeology.md named `.vhd` and identify listed `*.vhd`/`*.vhdl` without fixture, Jail pin, route triggers, or eval lock. Remediation: v0.4.35.
- diagnosing-superpowers blocked: ET lacked a mechanical session-discovery locate card with verified-path honesty. Remediation: session_discovery.py (v0.4.36).
- diagnosing-superpowers blocked: ET lacked mechanical intake-before-analysis + path:line citation HARD-GATEs after locate. Remediation: diagnose.py (v0.4.37).
- archaeology.md / identify lacked Ada (lost-ada fixture) (`.adb`/`.ads`) fixture, Jail pin, route triggers, or eval lock after five prior language pins. Remediation: v0.4.38.
- heal Phase 1 named "trace data flow" without a mechanical backward-chain HARD-GATE (symptom fixes still easy to ship). Remediation: root_cause.py (v0.4.39).
- after source fix, single-layer guards still shipped as the whole invalid-data cure. Remediation: defense.py (v0.4.40).
- flaky tests still guessed at timing with arbitrary sleep/setTimeout after defense-in-depth. Remediation: this leaf (v0.4.41).
