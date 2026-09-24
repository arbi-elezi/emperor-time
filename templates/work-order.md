# Work Order — <task-id>

> Fat G2 artifact. A worker with **zero session context** must be able to
> execute Task N from this file alone. The Task Ledger remains the audit
> trail; this file is the *handoff*.
>
> Trivial tasks (one file, one obvious change) may shrink each section to
> one line. They may not omit sections. Skipping this file on a non-trivial
> task is a Vow of Phases breach.

- **Task:** <one line>
- **Client quote:** "<verbatim ask>"
- **Origin:** assigned | dowsed (evidence: …)
- **Work-order SHA / path:** `.emperor/tasks/<id>/work-order.md`
- **Governing aspect files:** <router + one aspect per step already taken>
- **Size:** trivial | standard | heavy

## Contract (interfaces between tasks)

State what Task N may assume Task N-1 left on disk. No TBD. If unknown,
write a probe that will make it known before BUILD.

- **Inputs on disk:** <paths + expected shape>
- **Outputs on disk:** <paths + expected shape>
- **Forbidden:** <files/systems this order must not touch>

## Acceptance criteria (checkable)

1. <statement that can fail a command>
2. …

## Out of scope

- …

## Approach

<one paragraph>

**Rejected alternative:** <one line + why>

## Impact map

| Path | Why touched | Blast radius | Rollback |
|---|---|---|---|

## Tasks (bite-sized, executable)

Each task is a closed unit: files, exact commands, expected fail/pass
strings, commit message. Do not write "implement the feature". Write the
failing probe first.

### Task 1 — <name>

**Files:**
- Create: `<path>`
- Modify: `<path>`

**Step 1 — write the probe that must fail**

```text
<exact test or command source, pasted — not described>
```

```bash
<exact command>
```

Expected: FAIL
Quoted signal: `<string that proves the probe saw the bug/absence>`

**Step 2 — smallest change that makes the probe pass**

```text
<implementation sketch with real names, not pseudocode>
```

```bash
<exact command>
```

Expected: PASS
Quoted signal: `<string that proves it>`

**Commit:** `<type>: <message>`

### Task 2 — <name>

…

## Dispatch plan (Steal Chain, consent required)

| Work item | Agent | Why this agent | Prompt file | Quarantine dir |
|---|---|---|---|---|
| none | — | — | — | — |

Standing policy: workers receive **this work order + the named files**,
never the author's chain of thought. Their output starts at CONJECTURE.

## Isolated review pack (Judgment / hetero-critique)

Reviewer receives only:

1. This work order's acceptance criteria + impact map
2. `git diff <base>..<head>` (or `scripts/review-pack.sh` output)
3. Claim ledger rows that the author marked VERIFIED
4. `templates/critique.md`

Reviewer does **not** receive: design rationalizations, Steal Chain worker
"done" reports, or the author's self-critique conclusions.

## G4 probes (must be runnable by gate.sh)

```bash
# listed so scripts/gate.sh can exec them
<cmd-1>
<cmd-2>
```

## Done when

- [ ] Every task box above has quoted PASS tails in the ledger
- [ ] `scripts/gate.sh g4 .emperor/tasks/<id>` exits 0
- [ ] Self-critique eight-count filed
- [ ] Hetero-critique filed **or** UNAVAILABLE recorded with reason
- [ ] No claim row remains bare CONJECTURE unless labeled UNVERIFIABLE
