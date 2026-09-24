# Mechanical gates

Judgment Chain is the *law*. These scripts are the *lock on the door*.
A model writing "G4 PASS" in markdown is not a gate. An exit code is.

## Scripts

| Script | Gate | Fails when |
|---|---|---|
| `scripts/gate.sh g0` | G0 | no task dir, no client quote in ledger |
| `scripts/gate.sh g1` | G1 | no acceptance criteria |
| `scripts/gate.sh g2` | G2 | non-trivial task missing work-order or Expected: lines |
| `scripts/gate.sh g3` | G3 | impact-map paths missing from `git diff --stat` (when in a git repo) |
| `scripts/gate.sh g4` | G4 | claim rows still CONJECTURE; no critique file; listed probes not run |
| `scripts/gate.sh g5` | G5 | verdict not PASS/PASS-WITH-CONDITIONS; breach hidden empty-header |
| `scripts/review-pack.sh` | G4 hetero | cannot emit isolated pack |
| `scripts/eval.sh` | harness health | an eval fixture fails |

PowerShell twins: `scripts/gate.ps1`, `scripts/review-pack.ps1`.

## Vow mapping

- Vow of Evidence → G4 claim lint (VERIFIED rows need a quoted evidence cell)
- Vow of Phases → gate order; `gate.sh g4` refuses if g2 never passed
- Vow of the Ledger → missing ledger is a hard fail
- Vow of Critique → missing critique file is a hard fail at G4
- Vow of Consent → Steal/Jail scripts refuse without a CONSENT line in the ledger
- Vow of Worthy Spend → lifespan section with empty "bought" is a warning, not a pass decoration

## What the agent must do

Before claiming a gate open, **run the script and paste the tail**.
Do not paraphrase `exit 0`. Quote it.
