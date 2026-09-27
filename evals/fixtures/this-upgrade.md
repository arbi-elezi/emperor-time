# Task Ledger — emperor-time self-application (boot/host Python core)

- **Task:** Close bash↔ps1 silent-boot twin drift by extracting host detect + boot sequence into `scripts/lib/host.py` + `scripts/lib/boot.py` + thin boot twins; host report helpers delegate to Python; eval + version lockstep.
- **Client quote:** Soft-ET consented Worthy Spend after v0.4.31 install-python-core. Superpowers method leaves closed on disk. NEXT: crank ET strength — boot.py/host.py silent-boot unify (deferred on install spend; diagnosing-superpowers still waits on session-discovery).
- **Origin:** assigned
- **Size:** standard
- **Governing files:** SKILL.md → scripts/lib/host.py → scripts/lib/boot.py → thin boot.sh/boot.ps1 → portability.md
- **Tip at spend:** v0.4.32 (branch `et-manager/boot-host-python-core`)

## G0
Quoted ask above. Ambiguity resolved: ship host.py + boot.py Python core. Skip diagnosing-superpowers / embeddings / archaeology / emperor.py dispatcher this turn. Do not re-announce or re-ship #33–#48 leaves.

## G1 Acceptance criteria
1. SKILL.md version ≥ 0.4.32 and names five chains + six vows.
2. `scripts/lib/host.py` owns host detect + host.env report line (`os`/`shell`/`wsl`/`win_interop`/`encoding`/`mnt`/`win_root`) and `--as-json`.
3. `scripts/lib/boot.py` writes `.emperor/host.env` + survey.md (+ optional eval.log); supports `--skip-eval` / `--skip-identify`.
4. Thin `boot.sh` / `boot.ps1` call boot.py; `emperor_host_report` / `Write-EmperorHostReport` delegate to host.py.
5. Plugin/marketplace/SKILL lockstep 0.4.32; bakeoff + honesty name the leaf; CHANGELOG has 0.4.32.
6. Eval locks compile + thin twins + report keys + boot smoke + suite green.
7. Live defect-rate vs Superpowers stays **UNVERIFIABLE**.

## Out of scope
- emperor.py dispatcher / route embeddings
- diagnosing-superpowers session diagnosis leaf (needs transcript-discovery infra)
- Whole Superpowers diagnosing skill vendored into always-on prompt
- Rewriting shell EMPEROR_* sourceable helpers / WSL path converters (stay in host.sh/ps1)
- Live multi-vendor bake-off numbers
- Redo of #33–#48 (gate/identify/finish/eval/done/queue/forge/review-pack/dowse/receive/execute/subagent/parallel/install/…)

## G2
Rejected alternative: slim diagnosing-emperor HARD-GATE (citation iron law + intake-before-analysis).
Why: Superpowers diagnosing still needs session-discovery paths ET lacks this turn; boot/host twins already drifted (encoding + WSL interop probes); Python preference + twin-drift remediation pattern after install.py.

## G3
host.py + boot.py + thin boot twins on `et-manager/boot-host-python-core`. See git log.

## G4
Claims:

| Claim | Status | Evidence |
|---|---|---|
| SKILL.md is 0.4.32 orchestrator | TESTED | frontmatter `version: 0.4.32` on branch HEAD |
| host.py --report prints canonical keys | TESTED | exit 0 + os=/shell=/wsl=/win_interop=/encoding= |
| boot.py --skip-eval writes host.env + survey.md | TESTED | tempfile smoke in eval |
| bash and ps1 thin boot twins call boot.py | TESTED | both contain `lib/boot.py` |
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
- bash/ps1 silent-boot host report drifted (encoding + WSL interop probes). Remediation: this leaf (v0.4.32).
