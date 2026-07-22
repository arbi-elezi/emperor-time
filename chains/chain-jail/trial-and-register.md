# Trial and Register — Zetsu ends here, or the capture is released

**Contract:** every captured/authored skill passes a trial before first real
use, then gets installed with provenance and recorded. Fail twice → release.
Output: trial record + installed skill (or a recorded rejection).

## Part 1 — The trial (Judgment presides)

### Design the toy case

- **Smallest realistic input** that exercises the skill's main path — real
  enough to catch real failure, small enough to be disposable. (A migration
  skill trials on a 2-table toy schema, not on production DDL.)
- Run **in quarantine**: a scratch dir or `.emperor/captured-skills/<name>/trial/`;
  the skill gets no access to real task artifacts on its first execution.
- **Prediction before run** (scientific method, no exemptions for skills):
  write what correct output looks like *before* invoking. "I'll know it when I
  see it" is how plausible garbage gets admitted.

### Execute and judge

| Check | Pass condition |
|---|---|
| Main path | observed output matches prediction (quoted into the trial record) |
| Failure behavior | feed one malformed input — does it fail the way its body claims? |
| Tripwires | every `(verify at first use)` marker in the skill resolved against this machine (`--help`, path checks) |
| Containment | it touched only quarantine paths; no unexpected writes, no network calls beyond those declared |
| Routing (if installable) | its description fires on the phrasing of the originating task — dry-check by re-reading, or live-check after install |

### Verdicts

- **PASS** → Part 2.
- **FAIL, diagnosable** → back to `adaptation.md` (or one authoring revision).
  Re-trial with a *new prediction* — never re-run unchanged (Vow 6).
- **FAIL twice** → **release the capture**: record what was tried and why it
  failed (the record saves the next hunter from the same candidate), and
  return the unmet need to the parent task as an open constraint — the honest
  state, not a papered-over one.

## Part 2 — Register

### Install location (decide deliberately)

| Scope | Where | When |
|---|---|---|
| This project only | `.emperor/captured-skills/<name>/` (stays put) or project skills dir (`.claude/skills/<name>/` etc.) | capability is project-specific |
| This user, all projects | user skills dir per harness — the deployment matrix in `references/portability.md` | general capability |
| An enlisted agent's harness | *that* harness's directory | the capture was for a worker (that agent runs the trial; you judge its output) |

One location. Installing to several at once creates shadow-copy drift — the
same defect the absence check exists to catch.

### The ledger record

```
CHAIN JAIL: "<capability sentence>"  → BOUND
Source: <URL | authored> (license: <L>)   Trial: PASS <date> (record: .emperor/captured-skills/<name>/trial/)
Installed: <path>   Changes: see provenance header
```

(Released captures get the same record with `→ RELEASED: <reason>`.)

### After registration

- The parent task resumes at the phase that was blocked, now holding the new
  ability — the trial does not substitute for the parent task's own G4; the
  skill proved itself on a toy, the task still proves itself on the real thing.
- First real use doubles as the skill's integration probe: any surprise gets
  appended to its trial record (living document), and a bad enough surprise
  re-opens the trial verdict.
