# Task Ledger — emperor-time self-application (zsh silent-boot parity)

- **Task:** Close zsh↔bash silent-boot twin drift in `scripts/emperor.zsh` — host.env auto-boot, host/boot/identify/excavate special-cases match bash `scripts/emperor` (and the PS silent-boot contract).
- **Client quote:** Soft-ET consented Worthy Spend after v0.4.21 done.py. Survey A–E: real drift in emperor.zsh vs bash (missing silent-boot + identify/excavate specials); emperor.py still not a clear win; heal/excavate wrappers already thin Python/alias; embeddings beyond JSON not justified; no new archaeology toolchain leaf without a language pin.
- **Origin:** assigned
- **Size:** standard
- **Governing files:** SKILL.md → AGENTS.md silent boot → emperor.zsh twin of emperor / emperor.ps1
- **Tip at spend:** v0.4.22 (branch `et-manager/zsh-silent-boot-parity`)

## G0
Quoted ask above. Ambiguity resolved: ship A (zsh silent-boot parity). Skip B–E this turn.

## G1 Acceptance criteria
1. SKILL.md version ≥ 0.4.22 and names five chains + six vows.
2. `zsh scripts/emperor.zsh boot` writes `.emperor/host.env` silently; verbose only when `EMPEROR_BOOT_VERBOSE=1`.
3. `identify` with no args is silent; with path surveys; `excavate` aliases identify.
4. Plugin/marketplace/SKILL lockstep 0.4.22.
5. Eval locks silent-boot zsh contract + Cursor adapter path; suite green.
6. Live defect-rate vs Superpowers stays **UNVERIFIABLE**.

## Out of scope
- emperor.py single dispatcher / route embeddings / capture|heal|excavate Python redo
- done/eval/identify/finish/gate/route redo
- Live multi-vendor bake-off numbers

## G2
Rejected alternative: emperor.py dispatcher (still hand-wire win unclear) or another archaeology leaf without toolchain pin.
Why: Cursor adapter already claimed bash/zsh silent-boot parity while emperor.zsh still printed host report only for `host` and skipped auto-boot — real twin drift after PS parity (v0.4.4 / PR #18).

## G3
emperor.zsh on `et-manager/zsh-silent-boot-parity`. See git log.

## G4
Claims:

| Claim | Status | Evidence |
|---|---|---|
| SKILL.md is 0.4.22 orchestrator | TESTED | frontmatter `version: 0.4.22` on branch HEAD |
| zsh silent-boot writes host.env | TESTED | `zsh scripts/emperor.zsh boot` → host.env; identify no-args silent |
| excavate via zsh surveys fixture | TESTED | excavate lost-f90 shows `.f90` fossil |
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
- emperor.zsh missing silent-boot / identify / excavate specials vs bash. Remediation: this leaf (v0.4.22).
