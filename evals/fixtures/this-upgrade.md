# Task Ledger — emperor-time self-application (session-discovery Python core)

- **Task:** Add session-discovery Python core + thin twins + heal leaf + reference + route/eval lockstep so diagnosing can later HARD-GATE on verified transcript paths without vendoring whole diagnosing-superpowers.
- **Client quote:** Soft-ET consented Worthy Spend after v0.4.35 archaeology VHDL. Superpowers method leaves mostly closed. Remaining Superpowers gap: diagnosing-superpowers, blocked on session-discovery. Ship session-discovery Python core (v0.4.36).
- **Origin:** assigned
- **Size:** standard
- **Governing files:** SKILL.md → emperor-heal → session-discovery.md → session_discovery.py → references/session-discovery.md
- **Tip at spend:** v0.4.36 (branch `et-manager/session-discovery-python-core`)

## G0
Quoted ask above. Ambiguity resolved: ship session-discovery Python core. Skip full diagnosing-emperor skill, embeddings, emperor.py dispatcher this turn. Do not re-announce or re-ship #33–#52 leaves (gate/identify/finish/eval/done/queue/forge/review-pack/dowse/receive/execute/subagent/parallel/install/boot.py/host.py/worktree.py/excavate thin-alias/archaeology VHDL/…).

## G1 Acceptance criteria
1. SKILL.md version ≥ 0.4.36; `scripts/lib/session_discovery.py` prints SESSION / PATH / STATUS / MUST card.
2. Thin `scripts/session-discovery.sh` / `session-discovery.ps1` exec the Python core; emperor peers dispatch `session-discovery`.
3. Honesty: VERIFIED only when path exists; ABSENT/UNVERIFIABLE otherwise; `--reject-guess` HARD-GATE exit non-zero.
4. Skill leaf `skills/emperor-heal/session-discovery.md` + `references/session-discovery.md` cite obra/superpowers MIT locate aspect (URL + access date 2026-09-27).
5. Route triggers include session transcript locate phrases → emperor-heal; `route.py` matches.
6. Plugin/marketplace/SKILL lockstep 0.4.36; bakeoff + honesty name session_discovery.py; CHANGELOG has 0.4.36.
7. Eval locks new files/version/triggers; suite green.
8. Live defect-rate vs Superpowers stays **UNVERIFIABLE**.

## Out of scope
- Full diagnosing-emperor / diagnosing-superpowers skill (analyst prompts, case/report templates, bundles)
- emperor.py dispatcher / route embeddings
- Mutating or scrubbing session transcript files
- Rewriting resume / activate SessionStart paths
- Live multi-vendor bake-off numbers
- Redo of #33–#52 (including VHDL archaeology / excavate thin-alias / worktree.py / boot.py / …)

## G2
Rejected alternative: vendor whole diagnosing-superpowers under skills/.
Why: standing rule — extract locate HARD-GATE only; full skill is prompts+templates ET does not need yet.

Rejected alternative: emperor.py unified dispatcher.
Why: larger surface than one locate leaf; portability twins still required; out of scope.

Rejected alternative: another archaeology Jail pin.
Why: VHDL just closed; diagnosing is the named remaining Superpowers gap and session-discovery unblocks it.

## G3
session_discovery.py + thin twins + heal leaf + reference + triggers/eval/honesty/bakeoff lockstep on `et-manager/session-discovery-python-core`. See git log.

## G4
Claims:

| Claim | Status | Evidence |
|---|---|---|
| SKILL.md is 0.4.36 orchestrator | TESTED | frontmatter `version: 0.4.36` on branch HEAD |
| session_discovery.py prints checklist card | TESTED | `SESSION checklist=yes` + PATH/STATUS/MUST |
| --reject-guess hard-gates | TESTED | exit non-zero + `REJECT GUESS:` line |
| Thin twins call Python core | TESTED | session-discovery.sh/ps1 contain session_discovery.py |
| Route session discovery → heal | TESTED | route.py + triggers.json |
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
- diagnosing-superpowers blocked: ET lacked a mechanical session-discovery locate card with verified-path honesty. Remediation: this leaf (v0.4.36).
