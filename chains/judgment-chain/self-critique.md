# Self-Critique — the prosecutor protocol

**Contract:** switch roles explicitly and try to get the work thrown out.
Eight counts, each showing *what was examined* (commands run, paths read) —
findings or no findings. Output: a completed `templates/critique.md` recorded
in the ledger.

The role-switch line goes in the critique header: *"Prosecution opens: I am no
longer the author of this work."* Theatrical — and functional: the sentence
marks where advocacy ends. From here, every sentence either attacks the work
or certifies that an attack was attempted and failed.

## The eight counts — with the sub-checks that make them real

### 1. Requirements coverage
- Walk G1's criteria one by one against the deliverable — no batching
  ("criteria 1–4 look fine" is advocacy, not examination).
- Hunt the *silent extras*: features/changes present that G1 never asked for.
  Extras are scope drift even when good (the out-of-scope list exists to be
  checked against the diff, line by line).

### 2. Correctness at the edges
Per changed function/behavior, interrogate the classic five: **empty** (zero
items, empty string, null), **huge** (limits, pagination, timeouts),
**unicode/encoding** (names, paths, CRLF — this repo already ate one of
those), **concurrent** (two callers, re-entry, partial state), **error paths**
(what does the caller see when the dependency fails?). Not every edge applies
to every change — but each gets a verdict: exercised, reasoned-safe (with the
reasoning stated), or **exposed** (finding).

### 3. Hidden assumptions
List what must be true of the environment for the change to work: versions,
OS, daemon up, env vars, network, file layout, locale. For each: checked in
code? ledgered as an assumption? or unstated (finding — the severity scales
with how silently it fails when false).

### 4. Evidence quality
The prosecutor's version of the claim audit's near-evidence check, aimed at
tests: for each test that "covers" the change, would it **fail if the change
were reverted**? Mentally revert (or actually revert, cheaply) — a test that
passes both ways certifies nothing (finding: "test tautological").

### 5. Regression surface
- Who else calls/reads/depends on what changed? (grep the symbol, the config
  key, the endpoint — quote the call-site list into the critique.)
- Were *those* paths re-verified, or only the new one?
- Shared state, caches, serialized formats: does anything persisted change
  shape?

### 6. Security and safety
- Input that reaches a shell, query, path join, or template — quoted/escaped?
- Secrets: in code, in logs, in error messages, in the ledger itself?
- Destructive operations (delete, overwrite, force-push, migrations): guarded,
  confirmed, reversible?
- Captured/enlisted content: did anything from outside (skill, worker diff)
  get admitted without its quarantine record?

### 7. Simpler alternative
State the halving question honestly: *could half this diff satisfy G1?* If a
simpler shape exists and was rejected, the reason should already be in G2's
rejected-alternative line — missing reason is itself a finding (design
decision made silently). Complexity is spend (Vow 6); unjustified complexity
is waste wearing engineering's clothes.

### 8. Honesty of the report
Read the delivery draft against the audited Claim Ledger: every confident
sentence backed by a VERIFIED row? Every assumption and UNVERIFIABLE labeled
*in the draft* (not only in the ledger — the client reads the draft)?
Calibration language per the mapping table in
`references/scientific-method.md`?

## Severity and disposition

| Severity | Meaning | Effect |
|---|---|---|
| blocker | would mislead the client, lose data, or ship a falsehood | gate FAILS → `verdicts-and-breaches.md` |
| should-fix | real defect, contained | fix now or become a PASS condition |
| note | improvement opportunity | dowsing pool |

Every finding gets a disposition line; "acknowledged" is not a disposition.

## The suspicious clean pass

Eight counts, zero findings? State, per count, what was examined and survived
— named commands, named files. A clean pass that can't name what it checked
is an unexamined pass, and re-runs with the counts done individually. (Clean
passes on trivial tasks are normal; on multi-file changes they are rare
enough to warrant their own second look.)

Hand the completed critique to `hetero-critique.md` (if an agent is
available) or directly to `verdicts-and-breaches.md`.
