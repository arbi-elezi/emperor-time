# Task Ledger — emperor-time self-application (dowse Python core)

- **Task:** Port Dowsing Mode 2 machine scan to `scripts/lib/dowse.py` so bash↔ps1 cannot drift on AsJson + richer roster metadata (ps1 had `-AsJson` + Binary/Headless/SignIn; bash table-only); thin twins; factory dogfood locks.
- **Client quote:** Soft-ET consented Worthy Spend after v0.4.25 review_pack.py. NEXT: dowse.py — unify bash↔ps1 (AsJson + richer roster on ps1 only). Ship Python core + thin twins + eval + version lockstep if needed.
- **Origin:** assigned
- **Size:** standard
- **Governing files:** SKILL.md → system-dowsing.md → agent-registry.md → dowse.py
- **Tip at spend:** v0.4.26 (branch `et-manager/dowse-python-core`)

## G0
Quoted ask above. Ambiguity resolved: ship dowse Python core. Skip cmd redo / embeddings / archaeology / host unify / capture.py this turn. Do not re-announce or re-ship #33–#42 leaves.

## G1 Acceptance criteria
1. SKILL.md version ≥ 0.4.26 and names five chains + six vows.
2. `scripts/lib/dowse.py` owns PATH detect + bounded version/auth probes + table + `--as-json` richer roster; thin `dowse.sh` / `dowse.ps1`.
3. `--as-json` / `-AsJson` emits Agent/Binary/Status/Version/Auth/Headless/SignIn on **both** peers (closes bash table-only drift).
4. Plugin/marketplace/SKILL lockstep 0.4.26; system-dowsing + agent-registry + mechanical-gates + bakeoff point at dowse.py.
5. Eval locks compile + thin twins + AsJson richer keys + suite green.
6. Live defect-rate vs Superpowers stays **UNVERIFIABLE**.

## Out of scope
- emperor.cmd host special / emperor.py dispatcher / route embeddings
- heal/excavate/boot/host unify redo
- capture.py HARD-GATE
- New archaeology toolchain leaf
- Live multi-vendor bake-off numbers
- Redo of #33–#42 (gate/identify/finish/eval/done/queue/forge/review-pack/…)

## G2
Rejected alternative: capture.py HARD-GATE or host.sh/ps1 unify.
Why: dowse AsJson asymmetry was the named NEXT after review-pack; Steal Chain orchestrators need machine-readable roster on POSIX too.

## G3
dowse.py + thin twins on `et-manager/dowse-python-core`. See git log.

## G4
Claims:

| Claim | Status | Evidence |
|---|---|---|
| SKILL.md is 0.4.26 orchestrator | TESTED | frontmatter `version: 0.4.26` on branch HEAD |
| dowse --as-json emits richer roster keys | TESTED | JSON has Binary/Headless/SignIn |
| bash and ps1 thin twins call dowse.py | TESTED | both contain `lib/dowse.py`; line caps |
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
- bash/ps1 dowse twins drifted (AsJson + richer roster on ps1 only). Remediation: this leaf (v0.4.26).
