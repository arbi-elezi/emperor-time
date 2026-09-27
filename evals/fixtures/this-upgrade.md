# Task Ledger — emperor-time self-application (executing-plans HARD-GATE)

- **Task:** Extract Superpowers `executing-plans` Continuous execution / Four stops / Rulings / Task Loop / Completion contract as a Chain Jail HARD-GATE leaf under emperor-build: checklist + `scripts/lib/execute.py` + thin twins + emperor peer + eval/bakeoff locks. Also backfill CHANGELOG 0.4.27 (missed on #44) and peer `receive` on emperor.cmd.
- **Client quote:** Soft-ET consented Worthy Spend after v0.4.27 receive-review. NEXT: close Superpowers executing-plans gap (writing-plans/work_order landed; finish landed; inline continuous-execution card was never extracted). Ship Python core + thin twins + eval + version lockstep.
- **Origin:** assigned
- **Size:** standard
- **Governing files:** SKILL.md → emperor-build → executing-plans-checklist.md → execute.py
- **Tip at spend:** v0.4.28 (branch `et-manager/execute-plans-hard-gate`)

## G0
Quoted ask above. Ambiguity resolved: ship executing-plans HARD-GATE leaf. Skip install.py / host unify / capture.py / embeddings / archaeology / subagent-driven-development this turn. Do not re-announce or re-ship #33–#44 leaves.

## G1 Acceptance criteria
1. SKILL.md version ≥ 0.4.28 and names five chains + six vows.
2. `skills/emperor-build/executing-plans-checklist.md` exists with HARD-GATE + Four stops + Task Loop steps; provenance names executing-plans.
3. `scripts/lib/execute.py` owns EXECUTE / STEP / MUST card; `--advance` rejects skips; `--reject-checkin` exits 1; thin `execute.sh` / `execute.ps1`.
4. `emperor` / `emperor.zsh` / `emperor.ps1` / `emperor.cmd` peer `execute` (cmd also gains missed `receive`).
5. Plugin/marketplace/SKILL lockstep 0.4.28; extract-aspect + skill-catalog + bakeoff + honesty name the leaf; CHANGELOG has 0.4.27 + 0.4.28.
6. Eval locks compile + thin twins + iron token + suite green.
7. Live defect-rate vs Superpowers stays **UNVERIFIABLE**.

## Out of scope
- emperor.py dispatcher / route embeddings
- heal/excavate/boot/host unify redo / install.py
- capture.py HARD-GATE
- Whole executing-plans or subagent-driven-development vendored into always-on prompt
- Live multi-vendor bake-off numbers
- Redo of #33–#44 (gate/identify/finish/eval/done/queue/forge/review-pack/dowse/receive/…)

## G2
Rejected alternative: host.sh/ps1 Python core or subagent-driven-development leaf.
Why: executing-plans is the remaining Superpowers method gap named in navigation (Fat executable plan); writing-plans and finish already landed; continuous-execution / four-stops card was never extracted.

## G3
execute.py + checklist + thin twins on `et-manager/execute-plans-hard-gate`. See git log.

## G4
Claims:

| Claim | Status | Evidence |
|---|---|---|
| SKILL.md is 0.4.28 orchestrator | TESTED | frontmatter `version: 0.4.28` on branch HEAD |
| execute --reject-checkin hard-gates | TESTED | exit 1 + REJECT CHECKIN |
| bash and ps1 thin twins call execute.py | TESTED | both contain `lib/execute.py` |
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
- CHANGELOG missed 0.4.27 entry on #44; emperor.cmd missed receive peer. Remediation: this PR.
- executing-plans continuous-execution card never extracted after writing-plans/finish. Remediation: this leaf (v0.4.28).
