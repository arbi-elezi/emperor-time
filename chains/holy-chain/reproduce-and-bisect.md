# Reproduce and Bisect — isolating the cause

**Contract:** turn "it's broken" into "THIS breaks it, demonstrably". Output:
a minimal on-demand reproduction plus the isolated cause, both evidenced in
the combat ledger. No reproduction → no healing claims, only labeled
mitigation.

## Part 1 — Reproduce

1. **Make it fail on demand.** Start from the trigger captured at triage; strip
   it to the smallest invocation that still fails. Quote the actual failure
   output into the ledger — the exact text is the fingerprint that tells you
   later whether you fixed *this* bug or a lookalike.
2. **Minimize deliberately**: fewer files, smaller input, fewer steps, no
   background services that aren't implicated. Each removal is a micro-probe
   ("still fails without X → X is not required for the failure") — you are
   already learning causes while minimizing.
3. **Determinism check**: run the reproduction 3 times. 3/3 fail →
   deterministic, proceed. Intermittent → the flake *is* the finding: switch
   to evidence capture (loop the repro with logging, `--repeat` flags, stress
   until the rate is measured) — a failure rate is a reproduction too, just a
   statistical one, and bisection below still works with "rate changed" as
   the signal (more runs per probe).

### If it will not reproduce

Say so — that is a real and reportable state. Then: add instrumentation at
the suspected seam, set the tripwire (what to capture when it next fires),
and deliver *that* as the honest outcome. Guessing a fix for an
irreproducible failure and claiming victory is a Vow 1 breach with a delay
timer attached.

## Part 2 — Bisect (one hypothesis per step)

**The combat ledger** — one line per probe, written *before* running it:

```
H3: cause in the serializer change (HEAD~4) | predict: revert-it → repro passes | ran: <cmd> | saw: still fails | H3 REFUTED
```

The prediction column is not paperwork — it is the thing that stops
motivated reading of ambiguous output. Refuted lines stay; they are the map
of where the cause isn't (and the proof you aren't re-testing dead ends —
Vow 6's retry rule is enforced by this ledger being visible).

### Choose the bisector by wound shape

| Shape | Method |
|---|---|
| Worked at ref A, broken at ref B (history available) | `git bisect start B A` + the reproduction as the test — `git bisect run <script>` when the repro is scriptable; manual good/bad marking when it needs judgment |
| Breakage inside one large uncommitted change | binary-search the diff: apply half the hunks (`git apply` on a split diff, or stage-by-hunk), test, recurse into the failing half |
| No usable history | component isolation: disable/stub suspects one at a time (feature flags, config toggles, commenting a subsystem out in the toy repro) — one variable per probe, always |
| Environment-shaped (works there, fails here) | diff the environments as data: versions, env vars, locale, line endings, PATH order; each difference is a hypothesis, tested by transplanting it alone |
| Emerged after an agent-merge | bisect over admission boundaries: `.emperor/runs/` records what was admitted when; revert to each boundary until green — the culprit contribution then gets its own inner bisection |

### Bisection discipline

- **One variable per probe.** Changing two things and seeing green teaches
  nothing durable — which one healed it becomes the next bug's mystery.
- **Verify the bisector itself**: before trusting `git bisect run`, confirm
  the test script fails on the known-bad and passes on the known-good
  endpoint (a broken oracle bisects to a random commit with full confidence).
- **The cause must explain the fingerprint.** When bisection lands on a
  commit/hunk, articulate *why* that change produces exactly the observed
  failure text. "Bisect said so" without the mechanism is a correlation —
  the mechanism claim gets its own probe if it doesn't fall out obviously
  (this is what stops off-by-one bisections and coincidental flake landings).

## Exit

Cause isolated + mechanism articulated + reproduction in hand → hand all
three to `heal-and-verify.md`. The combat ledger goes into the task ledger
as-is (refuted lines included — they are paid-for knowledge).
