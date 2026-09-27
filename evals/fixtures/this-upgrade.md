# Task Ledger — emperor-time self-application (eval.py Python core)

- **Task:** Port structural eval assertion suite to Python core (`scripts/lib/eval.py`); thin `eval.sh`/`eval.ps1` twins; close bash↔ps1 twin drift (ps1 was a ~35-line presence stub); eval-lock self; keep bake-off honesty.
- **Client quote:** Soft-ET consented Worthy Spend — pick strongest twin-drift or capability win after finish.py (v0.4.18).
- **Origin:** assigned
- **Size:** standard
- **Governing files:** SKILL.md → emperor-verify → mechanical-gates
- **Tip at eval.py spend:** v0.4.19 (branch `et-manager/eval-python-core`)

## G0
Quoted ask above. Ambiguity resolved: port eval (real twin drift — bash ~600 locks vs ps1 stub) over boot.py (already parity) / emperor.py dispatcher / route enrichment beyond JSON MVP. Skipped identify/finish/gate redo.

## G1 Acceptance criteria
1. SKILL.md version ≥ 0.4.19 and names five chains + six vows.
2. `scripts/eval.sh` / `scripts/lib/eval.py` print EVALS PASSED on green; exit 1 on FAIL.
3. eval.py owns the full suite; thin twins call it (ps1 stub drift closed).
4. Plugin/marketplace/SKILL lockstep 0.4.19.
5. Mechanism leaves incl. eval.py + finish.py + identify.py + gate.py eval-locked; bakeoff honesty OK.
6. Live defect-rate vs Superpowers stays **UNVERIFIABLE**.

## Out of scope
- emperor.py single dispatcher / route embeddings / boot.py / archaeology language five
- Live multi-vendor bake-off numbers
- identify/finish/gate redo

## G2
Rejected alternative: leave eval.sh as the only real suite and eval.ps1 as a stub.
Why: twin drift was the largest remaining bash↔ps1 gap; Python-first doctrine already landed for finish/identify/gate/route/… — eval is the harness lock.

## G3
eval.py Python core on `et-manager/eval-python-core`. See git log.

## G4
Claims:

| Claim | Status | Evidence |
|---|---|---|
| SKILL.md is 0.4.19 orchestrator | TESTED | frontmatter `version: 0.4.19` on branch HEAD |
| eval.py thin twins + full suite | TESTED | `bash scripts/eval.sh` → EVALS PASSED; thin-twin grep lock |
| Finish/identify/gate cores still green | TESTED | eval finish + identify + gate sections PASS |
| Bakeoff + this fixture refuse fake live defect-rate numbers | TESTED | both files contain `UNVERIFIABLE` for live defect-rate vs Superpowers |
| Live defect-rate vs Superpowers | UNVERIFIABLE | no shared-task three-vendor bake-off run in this session |

## Verdict
PASS-WITH-CONDITIONS: local mechanism TESTED; live bake-off numbers UNVERIFIABLE.

## Breach Register
- bash/ps1 gate twins drifted (CONJECTURE warn). Remediation: gate.py (v0.4.16).
- bash/ps1 identify twins drifted (shebangs). Remediation: identify.py (v0.4.17).
- bash/ps1 finish twins drifted (origin/HEAD). Remediation: finish.py (v0.4.18).
- bash/ps1 eval twins drifted (ps1 stub). Remediation: eval.py (v0.4.19).
