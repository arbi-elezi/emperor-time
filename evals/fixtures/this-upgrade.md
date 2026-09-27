# Task Ledger — emperor-time self-application (review-pack Python core)

- **Task:** Port isolated review-pack emitter to `scripts/lib/review_pack.py` so bash↔ps1 cannot drift on G4 hetero criteria (ps1 copied entire work-order; bash awk kept only `## Acceptance criteria`); thin twins; factory dogfood locks.
- **Client quote:** Soft-ET consented Worthy Spend after v0.4.24 forge.py. NEXT: survey review-pack / dowse twin drift. If real drift, ship Python core + thin twins + eval + version lockstep. Else pick next best twin-drift or capability gap (not embeddings unless justified; not archaeology without VERIFIED toolchain).
- **Origin:** assigned
- **Size:** standard
- **Governing files:** SKILL.md → mechanical-gates.md → emperor-verify → review_pack.py
- **Tip at spend:** v0.4.25 (branch `et-manager/review-pack-python-core`)

## G0
Quoted ask above. Ambiguity resolved: ship review-pack Python core. Skip cmd redo / embeddings / archaeology / host unify / capture.py / dowse this turn. Do not re-announce or re-ship forge.

## G1 Acceptance criteria
1. SKILL.md version ≥ 0.4.25 and names five chains + six vows.
2. `scripts/lib/review_pack.py` owns meta SHAs + acceptance-criteria extract + diff/diffstat + claims; thin `review-pack.sh` / `review-pack.ps1`.
3. criteria.md contains `## Acceptance criteria` body and does **not** leak Plan header / Out of scope / Approach (ps1 twin used to dump the full work-order).
4. Plugin/marketplace/SKILL lockstep 0.4.25; mechanical-gates + emperor-verify + request-review checklist point at review_pack.py.
5. Eval locks compile + thin twins + criteria extract + meta SHAs; suite green.
6. Live defect-rate vs Superpowers stays **UNVERIFIABLE**.

## Out of scope
- emperor.cmd host special / emperor.py dispatcher / route embeddings
- heal/excavate/boot/host unify redo
- dowse.py / capture.py HARD-GATE
- New archaeology toolchain leaf
- Live multi-vendor bake-off numbers
- Redo of forge / queue / done / #33–#41 leaves

## G2
Rejected alternative: dowse AsJson unify (ps1 has `-AsJson` + richer roster metadata; bash table-only).
Why: review-pack is the load-bearing G4 hetero / request-review Step 3 PACK lock; criteria dump is a live correctness bug on Windows peers. Dowse feature asymmetry remains a secondary candidate.

## G3
review_pack.py + thin twins on `et-manager/review-pack-python-core`. See git log.

## G4
Claims:

| Claim | Status | Evidence |
|---|---|---|
| SKILL.md is 0.4.25 orchestrator | TESTED | frontmatter `version: 0.4.25` on branch HEAD |
| review_pack extracts Acceptance criteria only | TESTED | criteria.md has section; no Plan header / Out of scope leak |
| meta.md carries base/head SHAs in a git repo | TESTED | `git rev-parse` lines in meta.md |
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
- bash/ps1 review-pack twins drifted (criteria full work-order dump). Remediation: this leaf (v0.4.25).
