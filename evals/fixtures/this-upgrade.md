# Task Ledger — emperor-time self-application (done.py Python core)

- **Task:** Python core for agent-defined DONE probes — close bash↔ps1 twin drift on the load-bearing Stop-hook / forge gate; eval fixtures + locks; keep bake-off honesty.
- **Client quote:** Soft-ET consented Worthy Spend after v0.4.20 route enrichment. Survey: emperor.py dispatcher still not a clear win vs hand-wire; boot.py already parity; queue twins mostly synced (PromoteFirstReady present both sides). done.sh/done.ps1 still duplicated logic with only presence locks — highest twin-drift / factory-strength win.
- **Origin:** assigned
- **Size:** standard
- **Governing files:** SKILL.md → dogma → emperor done → forge / Stop hook
- **Tip at done.py spend:** v0.4.21 (branch `et-manager/done-python-core`)

## G0
Quoted ask above. Ambiguity resolved: skip emperor.py / boot.py / queue.py / route embeddings. Port DONE probe runner to `scripts/lib/done.py`; thin twins; fixtures ok/fail/no-probes; dogma + bakeoff point at the Python lock.

## G1 Acceptance criteria
1. SKILL.md version ≥ 0.4.21 and names five chains + six vows.
2. `scripts/done.sh evals/fixtures/done-probes/ok` → DONE OK (exit 0); fail/no-probes exit non-zero.
3. Thin `done.sh` / `done.ps1` call `lib/done.py` (≤20 / ≤30 lines).
4. Plugin/marketplace/SKILL lockstep 0.4.21.
5. Eval locks compile + thin twins + fixtures + dogma pointer; bakeoff honesty OK.
6. Live defect-rate vs Superpowers stays **UNVERIFIABLE**.

## Out of scope
- emperor.py single dispatcher / boot.py / queue.py / route embeddings / forge.py title drift
- Live multi-vendor bake-off numbers
- identify/finish/gate/eval/route redo

## G2
Rejected alternative: ship queue.py (larger WIP kanban surface; twins already share PromoteFirstReady / placeholder filters) or emperor.zsh silent-boot only (shell patch, not Python-first).
Why: DONE is the factory exit gate (Stop hook + forge). Duplicated bash/ps1 probe runners with presence-only eval is the clear twin-drift miss after v0.4.20.

## G3
done.py on `et-manager/done-python-core`. See git log.

## G4
Claims:

| Claim | Status | Evidence |
|---|---|---|
| SKILL.md is 0.4.21 orchestrator | TESTED | frontmatter `version: 0.4.21` on branch HEAD |
| done.py ok/fail/no-probes fixtures | TESTED | `bash scripts/done.sh evals/fixtures/done-probes/ok` → DONE OK; fail + no-probes non-zero |
| Thin done twins | TESTED | done.sh ≤20 / done.ps1 ≤30; both call lib/done.py |
| Eval suite still green | TESTED | `bash scripts/eval.sh` → EVALS PASSED |
| Bakeoff + this fixture refuse fake live defect-rate numbers | TESTED | both files contain `UNVERIFIABLE` for live defect-rate vs Superpowers |
| Live defect-rate vs Superpowers | UNVERIFIABLE | no shared-task three-vendor bake-off run in this session |

## Verdict
PASS-WITH-CONDITIONS: local mechanism TESTED; live bake-off numbers UNVERIFIABLE.

## Breach Register
- bash/ps1 gate twins drifted (CONJECTURE warn). Remediation: gate.py (v0.4.16).
- bash/ps1 identify twins drifted (shebangs). Remediation: identify.py (v0.4.17).
- bash/ps1 finish twins drifted (origin/HEAD). Remediation: finish.py (v0.4.18).
- bash/ps1 eval twins drifted (ps1 stub). Remediation: eval.py (v0.4.19).
- route missed Fortran extensions after archaeology-fortran leaf. Remediation: triggers + thin twins (v0.4.20).
- bash/ps1 done twins duplicated probe runner with presence-only locks. Remediation: done.py (v0.4.21).
