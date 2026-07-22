# Triage — securing the scene

**Contract:** freeze the situation before investigation touches it. Output:
the triage block in the ledger (what broke, how noticed, last-known-good,
snapshot location) and a stabilized workspace. Minutes, not hours.

## Step 1 — Stop

- Halt in-flight edits — including your own half-formed "quick fix" (the
  urge to fix before understanding is the digging the prime directive bans).
- Halt dispatched agents whose scope touches the affected area (let disjoint
  ones finish; their output waits in quarantine).
- Note the exact trigger: what command/event surfaced the breakage, verbatim.

## Step 2 — Snapshot (by environment)

| Environment | Snapshot procedure |
|---|---|
| Git repo, dirty tree | `git status` captured, then `git stash push -u -m "holy-chain <task-id>"` — or a WIP commit on a rescue branch (`git switch -c rescue/<task-id>` + commit) if the state is worth keeping addressable. Record which you did and the stash/commit ref |
| Git repo, clean tree | record `git rev-parse HEAD`; nothing else to freeze |
| No VCS | copy the affected tree aside: `cp -R <dir> <dir>.holy-<date>` / `Copy-Item -Recurse` — record the copy's path |
| Runtime/state breakage (DB, daemon, config) | export/dump what's exportable *read-only*; record service states observed (`systemctl status`, process lists) — do not restart anything yet: restarts destroy evidence and are themselves state changes with their own evidence bar |
| Agent mid-flight left partial edits | quarantine boundary is your friend: `.emperor/runs/` says what came from whom; snapshot the working tree, then diff against the last admission record |

The snapshot is the reversibility law made concrete: after this step, every
investigative action has an undo.

## Step 3 — Bracket last-known-good

Establish the interval `[last demonstrably worked, first observed broken]`:

- **Demonstrably** = evidence exists (a green CI run, a ledger G4 quote, a
  dated terminal output) — not "I'm sure it worked yesterday" (memory is a
  rumor here exactly as everywhere else).
- Shrink the left edge cheaply *now* if a probe is instant (the version tag
  that shipped, the commit CI blessed). Serious shrinking is bisection's job,
  not triage's.
- No demonstrable last-good exists? Record that honestly — it changes
  bisection strategy (component isolation instead of history bisection) and
  it is itself a process lesson (evidence of working states was never being
  kept — postmortem material).

## Step 4 — Classify severity (it changes who you tell, not what you do)

| Class | Criteria | Extra duty |
|---|---|---|
| Local | broke your in-progress task only | none — proceed |
| Shared | breaks the build/tests for whoever pulls | tell the client now, one line, before investigating further |
| Shipped | the breakage is in something already delivered | disclosure rules apply — `process-healing.md` owns the client-facing part; investigation continues in parallel |

## Step 5 — Write the triage block

```
TRIAGE <date/time>
Broke: <symptom, one line>          Noticed by: <trigger, verbatim>
Last-good: <ref/date + evidence>    First-bad: <ref/date>
Snapshot: <stash ref | rescue branch | copy path | HEAD>
Class: local|shared|shipped         Agents halted: <list|none>
```

Hand to `reproduce-and-bisect.md`. Do not skip ahead to fixing — a fix
without a reproduction can only be believed, never verified, and belief is
not in the vocabulary here.
