# Task Ledger — emperor-time self-application (honesty refresh)

- **Task:** Make Emperor Time beat Superpowers on method axes; crank unique strengths; ignore adoption. Keep bake-off labels honest.
- **Client quote:** "use emperor-time yourself to do this task"
- **Origin:** assigned
- **Size:** heavy
- **Governing files:** SKILL.md → emperor-scope → emperor-require-design → emperor-tdd → emperor-verify
- **Tip at honesty spend:** v0.4.14 (`05bb5dc`, PR #30)

## G0
Quoted ask above. Ambiguity resolved: method axes only, not stars. Live
multi-vendor defect-rate numbers are out of scope for any single session
that did not run them.

## G1 Acceptance criteria
1. SKILL.md version ≥ 0.4.14 and names five chains + six vows.
2. Phase skills exist for scope/design/build/tdd/worktree/verify/dispatch/heal/capture (+ resume/queue/excavate/forge).
3. `scripts/gate.sh g4` rejects unquoted VERIFIED.
4. Jail pin-and-consent file exists.
5. Plugin lists TDD and worktree skills; marketplace version matches plugin.
6. Mechanism / activation / leaf gates present and eval-locked: plans, finish,
   activate/must-route, grill, debug phases, TDD, worktree iso, review, author,
   evidence, archaeology pas/asm/cbl.
7. `evals/bakeoff.md` + this fixture label local mechanism TESTED/VERIFIED and
   live defect-rate vs Superpowers **UNVERIFIABLE** (no fake numbers).

## Out of scope
- Marketing / star count
- Rewriting chain aspect files wholesale
- Live multi-model bake-off numbers (UNVERIFIABLE unless a third-repo
  three-vendor session is actually run and quoted)
- Version bump for honesty-only doc lock (lockstep unchanged at 0.4.14)

## G2
Rejected alternative: claim “ET beats Superpowers on defect rate” from local
eval alone. Why: Vow of Evidence — structural TESTED ≠ live defect-rate.
Work-order: `evals/bakeoff.md` inventory + this fixture + optional
`scripts/lib/bakeoff_honesty.py` lock.

## G3
Honesty refresh on `et-manager/bakeoff-honesty`. See git log.

## G4
Claims:

| Claim | Status | Evidence |
|---|---|---|
| SKILL.md is 0.4.14 orchestrator | TESTED | frontmatter `version: 0.4.14` on branch HEAD |
| Five chains still present | TESTED | `chains/*/SKILL.md` paths exist |
| Leaf gates (plans/finish/activate/grill/debug/TDD/iso/review/author/evidence) on disk + eval-locked | TESTED | `bash scripts/eval.sh` → EVALS PASSED; paths in bakeoff inventory |
| Archaeology fixtures pas/asm/cbl identify | TESTED | eval identify smokes on `lost-pas` / `lost-asm` / `lost-cbl` |
| Bakeoff + this fixture refuse fake live defect-rate numbers | TESTED | both files contain `UNVERIFIABLE` for live defect-rate vs Superpowers |
| Live defect-rate vs Superpowers | UNVERIFIABLE | no shared-task three-vendor bake-off run in this session |

## Verdict
PASS-WITH-CONDITIONS: mechanism parity and activation *mechanism* claimed as
TESTED/VERIFIED locally; bake-off *numbers* and wild-agent activation without
tell remain UNVERIFIABLE.

## Breach Register
- Earlier turns asserted "most complete skill ever" without bake-off — Vow of Evidence. Remediation: this ledger + `evals/bakeoff.md` label that CONJECTURE / keep live rate UNVERIFIABLE.
- Incremental bakeoff notes (activation close, evidence lock) risked implying a finished live bake-off. Remediation: full inventory table + explicit UNVERIFIABLE rows (2026-09-27 honesty spend).
