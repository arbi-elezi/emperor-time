# Mechanical gates

Judgment Chain is the *law*. These scripts are the *lock on the door*.
A model writing "G4 PASS" in markdown is not a gate. An exit code is.

## Scripts

| Script | Gate | Fails when |
|---|---|---|
| `scripts/gate.sh g0` (Python core) | G0 | no task dir, no client quote in ledger |
| `scripts/gate.sh g1` | G1 | no acceptance criteria |
| `scripts/gate.sh g2` | G2 | non-trivial task missing work-order or Expected: lines |
| `scripts/gate.sh g3` | G3 | impact-map paths missing from `git diff --stat` (when in a git repo) |
| `scripts/gate.sh g4` | G4 | no critique; missing CLAIM AUDIT / unfinished HYPOTHESIS\|TESTED (via `claim_audit.py`); VERIFIED without quote |
| `scripts/gate.sh g5` | G5 | verdict not PASS/PASS-WITH-CONDITIONS; breach hidden empty-header |
| `scripts/review-pack.sh` (Python core) | G4 hetero | cannot emit isolated pack |
| `scripts/forge.sh` (Python core) | G5 deliver / consent PR | no consent; DONE fail; gh missing → DRY |
| `scripts/eval.sh` (Python core) | harness health | an eval fixture fails |

Python core: `scripts/lib/gate.py` owns G0–G5. Thin twins: `scripts/gate.sh`,
`scripts/gate.ps1` (same exits). G2 still calls `work_order.py` for the plan
header **and** Task-N structure (`--reject-tbd` / `--reject-no-tasks` /
`--check-tasks`; thin `work-order.sh` / `work-order.ps1`). G4 calls
`claim_audit.py` for the Judgment claim-audit sweep (`--reject-unaudited` /
`--check-audit`; thin `claim-audit.sh` / `claim-audit.ps1` + `judgment-audit`
alias / `emperor claim-audit`).

Review-pack Python core: `scripts/lib/review_pack.py` owns meta SHAs +
acceptance-criteria extract + diff (thin `review-pack.sh` / `review-pack.ps1`).
Closes bash↔ps1 drift on criteria (ps1 used to dump the full work-order).

Dowse Python core: `scripts/lib/dowse.py` owns PATH detect + bounded version/auth probes + table/`--as-json` richer roster (thin `dowse.sh` / `dowse.ps1`). Closes bash↔ps1 drift on AsJson + Headless/SignIn metadata.

Forge Python core: `scripts/lib/forge.py` owns consent + DONE gate + title/G1 PR body (thin `forge.sh` / `forge.ps1`). Closes bash↔ps1 drift on title extraction and ledger dump.

Harness health Python core: `scripts/lib/eval.py` owns the structural assertion
suite. Thin twins: `scripts/eval.sh`, `scripts/eval.ps1` (same exits 0/1).

## Vow mapping

- Vow of Evidence → G4 claim lint (VERIFIED rows need a quoted evidence cell) + claim-audit HARD-GATE (CLAIM AUDIT line; no HYPOTHESIS/TESTED)
- Vow of Phases → gate order; `gate.sh g4` refuses if g2 never passed
- Vow of the Ledger → missing ledger is a hard fail
- Vow of Critique → missing critique file is a hard fail at G4
- Vow of Consent → Steal/Jail scripts refuse without a CONSENT line in the ledger
- Vow of Worthy Spend → lifespan section with empty "bought" is a warning, not a pass decoration

## What the agent must do

Before claiming a gate open, **run the script and paste the tail**.
Do not paraphrase `exit 0`. Quote it.
