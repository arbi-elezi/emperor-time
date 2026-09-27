# Task Ledger — emperor-time self-application (worktree create Python core)

- **Task:** Close bash↔ps1 worktree-create twin drift by extracting create logic into `scripts/lib/worktree.py` + thin worktree twins; eval + version lockstep. Isolation HARD-GATE (`worktree_iso.py` / `emperor iso`) unchanged.
- **Client quote:** Soft-ET consented Worthy Spend after v0.4.32 boot/host Python core. Superpowers method leaves closed on disk. NEXT: crank ET strength — worktree.py twin unify (diagnosing-superpowers still waits on session-discovery; excavate thin-alias polish deferred).
- **Origin:** assigned
- **Size:** standard
- **Governing files:** SKILL.md → scripts/lib/worktree.py → thin worktree.sh/worktree.ps1 → emperor-worktree
- **Tip at spend:** v0.4.33 (branch `et-manager/worktree-python-core`)

## G0
Quoted ask above. Ambiguity resolved: ship worktree.py Python core. Skip diagnosing-superpowers / embeddings / excavate thin-alias / emperor.py dispatcher this turn. Do not re-announce or re-ship #33–#49 leaves.

## G1 Acceptance criteria
1. SKILL.md version ≥ 0.4.33 and names five chains + six vows.
2. `scripts/lib/worktree.py` owns create: `.worktrees/<id>`, branch `emperor/<id>`, EXISTS short-circuit, usage exit 2, not-a-repo exit 1.
3. Thin `worktree.sh` / `worktree.ps1` call worktree.py; preserve exit codes.
4. Plugin/marketplace/SKILL lockstep 0.4.33; bakeoff + honesty name the leaf; CHANGELOG has 0.4.33.
5. Eval locks compile + thin twins + usage/not-repo refuse + tempfile create/EXISTS smoke + suite green.
6. Live defect-rate vs Superpowers stays **UNVERIFIABLE**.

## Out of scope
- emperor.py dispatcher / route embeddings
- diagnosing-superpowers session diagnosis leaf (needs transcript-discovery infra)
- Whole Superpowers diagnosing / using-git-worktrees skill vendored into always-on prompt
- Rewriting worktree_iso.py isolation HARD-GATE card
- excavate thin-alias polish (still hops identify twins; deferred)
- Live multi-vendor bake-off numbers
- Redo of #33–#49 (gate/identify/finish/eval/done/queue/forge/review-pack/dowse/receive/execute/subagent/parallel/install/boot/host/…)

## G2
Rejected alternative: slim diagnosing-emperor HARD-GATE (citation iron law + intake-before-analysis).
Why: Superpowers diagnosing still needs session-discovery paths ET lacks this turn; worktree.sh/ps1 still reimplemented create (last mutate twin without Python core besides excavate alias); Python preference + twin-drift remediation pattern after boot/host.

Rejected alternative: excavate thin-alias polish (call identify.py directly).
Why: excavate is already a 5-line alias; worktree create is the remaining duplicated mutate path and higher Worthy Spend.

## G3
worktree.py + thin worktree twins on `et-manager/worktree-python-core`. See git log.

## G4
Claims:

| Claim | Status | Evidence |
|---|---|---|
| SKILL.md is 0.4.33 orchestrator | TESTED | frontmatter `version: 0.4.33` on branch HEAD |
| worktree.py refuses missing id (exit 2) | TESTED | usage line + exit 2 |
| worktree.py refuses non-git cwd (exit 1) | TESTED | WORKTREE FAIL in tempfile |
| worktree.py create + EXISTS smoke | TESTED | tempfile git init → WORKTREE: / WORKTREE EXISTS: |
| bash and ps1 thin worktree twins call worktree.py | TESTED | both contain `lib/worktree.py` |
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
- bash/ps1 worktree create twins reimplemented mutate path. Remediation: this leaf (v0.4.33).
