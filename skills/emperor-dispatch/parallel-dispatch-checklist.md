# Parallel-dispatch checklist — dispatching-parallel-agents HARD-GATE

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/dispatching-parallel-agents/SKILL.md
- source-hash: sha256:1968923066f3b707eb01d1992cdf4c42284c3855f70253b9cd5000ff45fca13c
- heading: Identify Independent Domains + Focused Agent Tasks + Parallel Dispatch + Review and Integrate (adapted)
- license: MIT
- issue-context: emperor-dispatch / Steal Chain had consent + capture + quarantine for enlisted CLIs, and emperor-build had sequential subagent-driven HARD-GATE, but no enforceable card for when 2+ *independent* problem domains should run concurrently with disjoint writable scopes; Chain Jail extract-aspect names that HARD-GATE only (not whole dispatching-parallel-agents, not Superpowers agent prompt examples as always-on, not a second master router)

**Contract:** when facing 2+ independent tasks / failures / subsystems that can be worked without shared writable state or sequential dependence, complete the parallel-dispatch checklist. One agent per independent domain. Focused self-contained briefs. All dispatches in the same response for true parallelism. Review and integrate before claiming done. Emperor Time stays the orchestrator via emperor-dispatch + steal-chain + verify; do **not** announce or load whole `dispatching-parallel-agents`.

Mechanical card: `scripts/emperor parallel` (Python: `scripts/lib/parallel.py`).
Companion leaves: `skills/emperor-build/subagent-driven-checklist.md` (sequential plan tasks, one implementer at a time), `chains/steal-chain/dispatch.md` (CLI enlistment mechanics), `skills/emperor-verify/request-review-checklist.md`.
External CLI consent still `skills/emperor-dispatch/SKILL.md` + `consent-protocol.md` — different door from harness subagents.

## HARD-GATE — The Iron Law

```
ONE AGENT PER INDEPENDENT DOMAIN — NO SHARED WRITABLE SCOPE
```

Launch parallel agents whose writable SCOPE lists share a file, or whose failures share a root cause? **Stop.**
That is a merge conflict you scheduled. Disjoint scopes first. Related work: investigate together or `emperor subagent` sequentially.

## When to use (vs sequential paths)

| Situation | Path |
|---|---|
| Related failures (fix A likely fixes B) or shared writable state | Single agent / investigate together — not this leaf |
| Sequential plan tasks, one implementer at a time | `emperor subagent` (subagent-driven leaf) |
| Inline plan, no subagent tool | `emperor execute` (executing-plans leaf) |
| 2+ independent domains + agents available | **This leaf** (`emperor parallel`) |

**Use when:** 3+ test files failing with different root causes; multiple subsystems broken independently; each problem understood without context from the others; no shared writable state.

**Do not use when:** failures are related; you need full system state first; exploratory debugging (you do not know what is broken yet); agents would edit the same files.

## Parallel steps

Complete each step before the next for the overall run. Mechanical `--advance` rejects skips.
`--reject-shared-scope` always fails (hard gate when attempting parallel with overlapping writable scopes or related root causes).

### Step 1: GATE — When-to-use vs sequential / related

Confirm the table above. Ledger the choice. If external CLIs: Steal Chain consent first.
Do not parallelize "to go faster" when domains are related.

ET: When-to-use line in the ledger; `consent-protocol.md` if enlisting outside the harness.

### Step 2: DOMAINS — Group by independent problem domain

Group failures / tasks by what is broken (file, subsystem, root-cause guess).
Each domain gets a disjoint writable SCOPE list. Shared read-only context is fine.
Check SCOPE lists before launch, not after.

ET: domain table in the ledger; SCOPE lists compared for intersection (empty = proceed).

### Step 3: BRIEFS — Focused self-contained agent prompts

Each agent gets: specific scope, clear goal, constraints (what not to touch), expected output (summary of findings/fixes).
Write `prompt.md` under `.emperor/runs/<task>/<agent>/` (steal-chain layout) or the harness brief file.
Never paste session history. Reject briefs that are too broad, context-free, unconstrained, or vague about output.

ET: `chains/steal-chain/dispatch.md` anatomy (OBJECTIVE / SCOPE / CONSTRAINTS / CONTEXT / OUTPUT FORM / EPISTEMICS).

### Step 4: DISPATCH — Issue all agents in one response

Record BASE (`git rev-parse HEAD`) before launch.
Issue every independent dispatch in the **same** response so they run concurrently.
One dispatch per response is sequential — do not call that parallel.
Ledger agent ids. Bound the fleet to what you can quarantine.

ET: harness subagent tool and/or steal-chain invoke forms from `references/agent-registry.md` (re-verified at dowse).

### Step 5: INTEGRATE — Review summaries, conflicts, full suite

Read each summary. Check for conflicting edits (same files touched despite SCOPE promises).
Run the full project suite on this tree. Spot-check for systematic agent errors.
Output is CONJECTURE until Judgment + `scripts/gate.sh g4` / quarantine.

ET: `quarantine.md` then `emperor quarantine <task-dir>` (HARD-GATE) then Judgment; `emperor review` / evidence as needed.

### Step 6: COMPLETE — Ledger, next, or finish

Ledger domains closed or parked-with-ruling. Resolve conflicts before done claims.
If branch work is complete and suite is green: `emperor finish` (menu; do not assume PR).

## Common mistakes (reject these)

- Too broad: "Fix all the tests" → Specific: one file or subsystem per agent
- No context: "Fix the race" → Paste failing names + error tails into the brief
- No constraints: agent refactors everything → "Do NOT change production code outside SCOPE"
- Vague output: "Fix it" → "Return root cause + files changed + commands run"
- Shared writable SCOPE → `--reject-shared-scope` / stop

## Verification (after agents return)

1. Review each summary — understand what changed
2. Check for conflicts — did agents edit the same code?
3. Run full suite — verify fixes work together
4. Spot check — agents can make systematic errors

## Out of this leaf

- Whole `dispatching-parallel-agents` skill or its long session examples as always-on prompt
- Replacing Steal Chain consent / quarantine / capture
- Replacing `emperor subagent` for sequential plan tasks (that leaf forbids parallel implementers on the same plan)
- `using-superpowers` / diagnosing-superpowers / second master router
