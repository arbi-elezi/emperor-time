# Executing-plans checklist — inline plan execution HARD-GATE

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/executing-plans/SKILL.md
- source-hash: sha256:f38e8f2ddcf079f65493adc713c1fed78421dfaf5f4dbf6b3a6b2b1d95466e71
- heading: Continuous execution + Four stops + Rulings not stalls + The Task Loop + Completion contract (adapted)
- license: MIT
- issue-context: emperor-build had per-task TDD/iso/work-order but no enforceable continuous-execution card when the client chose inline plan run (no check-in theater, four stops only, ledgered rulings); Chain Jail extract-aspect names that HARD-GATE only (not whole executing-plans, not subagent-driven-development, not SDD workspace scripts)

**Contract:** when executing a work-order / plan *inline* in this session (client chose inline, or no subagent tool), complete the executing-plans checklist. Setup once. Task loop without pause-for-permission between tasks. Ledger every ruling. Stop only for the four named stops. Finish with whole-branch review then `emperor finish`. Emperor Time stays the orchestrator via emperor-build + TDD + evidence + finish; do **not** announce or load whole `executing-plans`.

Mechanical card: `scripts/emperor execute` (Python: `scripts/lib/execute.py`).
Companion leaves: `skills/emperor-tdd/red-green-refactor.md`, `skills/emperor-verify/verification-checklist.md`, `skills/emperor-forge/finish-menu.md`.

## HARD-GATE — The Iron Law

```
NO CHECK-IN THEATER — FOUR STOPS ONLY
```

Pause between tasks to ask "should I continue?" after the client chose inline? **Stop.**
That burns their time. Execute the plan. Ledger rulings. Only the four stops halt you.

## Four stops (only these ask the client)

1. Irreversible or destructive operation.
2. Security-sensitive action.
3. Side effect outside this worktree that norms say you ask about first (merge, push to a shared branch, publish).
4. Plan so broken that every path forward is a guess.

Everything else: decide, ledger `Ruling: <what> — <why> — <cost if wrong>`, continue.

## Execute steps

Complete each step before the next for the overall run. Mechanical `--advance` rejects skips.
`--reject-checkin` always fails (hard gate when pausing between tasks for permission theater).

### Step 1: SETUP — Workspace, ledger, plan, TDD, pre-flight

Isolated worktree (`emperor iso`) unless client consented to work on main.
Ledger on disk (not only harness todos) — compaction forgets; the ledger does not.
Read plan once + Spec if named. Load TDD iron-law before Task 1.
Pre-flight shared interfaces; ledger rows or `Pre-flight: no shared interfaces`.

ET: `emperor iso` + task ledger under `.emperor/` + `emperor tdd` card loaded.

### Step 2: TASK — Brief + BASE; read the brief

Take the next incomplete task. Read its brief (exact values, not memory of setup).
Mark in progress. BASE is the commit the task range starts from.

ET: open **current work-order task only**; do not reload sibling aspects.

### Step 3: WORK — Steps in TDD order; compare every Expected

Plan steps are RED-GREEN order. Write/run failing probe first. Watch it fail.
Every command with `Expected:` — run, read output, compare. Three outcomes:
- Matches → next step.
- Code wrong → `emperor heal` (systematic debug); never symptom-patch.
- Plan wrong → Step 4 ruling, then continue.

ET: `emperor tdd` + `emperor heal` + Vow of Evidence (quote tails).

### Step 4: RULE — Ledger rulings; do not stall

Conflicts, ambiguities, plan defects: decide with Spec as authority.
Ledger `Task <N>: Ruling: <finding> — <decision and why> — <cost if wrong>`.
Unledgered deviation is a decision made in secret. Keep going.

### Step 5: COMPLETE — Completion contract + task-done line

Before the ledger completion line, all true with evidence in this session:
- Every test the brief names ran; you read the output.
- Final task test run passed (command + result in the ledger line).
- Every `Expected:` compared against real output.
- Every deviation has a `Ruling:` line.

If any item missing: finish the task; do not mark complete.
Then take the next task (back to Step 2) without asking permission.

ET: `emperor evidence` / verification-before-completion still gates the claim.

### Step 6: FINAL — Whole-branch review, then finish menu

After all tasks: whole-branch review (fresh reviewer if available; else self-review ledgered as weaker).
Re-grade findings by effect. Critical/Important → ONE fix pass (each RED→GREEN + green suite).
Minors → ledger deferred; do not expand scope.
Collect every `Ruling:` and deferred minor into the final message.
Then `emperor finish` (integration menu). Do not assume they want a PR.

## Rationalizations (refuse)

| Excuse | Reality |
|---|---|
| "Let me check in before the next task" | Client chose inline to spend less. Only the four stops stop you. |
| "I remember what Task N says" | Memory is a summary. Read the brief. |
| "Skip watching the test fail; plan code is right" | A test you never saw fail proves nothing. |
| "Plan is wrong; I'll just do the right thing" | Do it and ledger the ruling. |
| "I'll write ledger lines after a few tasks" | Compaction does not wait. One line per task with the commit. |
| "I read my own diff; final review is redundant" | Same author, same blind spots. |

## ET mapping

| Step | ET home |
|---|---|
| 1 SETUP | emperor-worktree iso + ledger + tdd |
| 2 TASK | emperor-build current work-order task |
| 3 WORK | emperor-tdd + emperor-heal |
| 4 RULE | ledger Ruling lines |
| 5 COMPLETE | emperor-verify evidence |
| 6 FINAL | emperor-verify review + emperor-forge finish |

## Forbidden

- Vendor whole `executing-plans` or `subagent-driven-development` into always-on prompt.
- Check-in theater between tasks after inline was chosen.
- Unledgered plan deviation.
- Claiming task complete without the completion contract.
- Skipping whole-branch review and jumping straight to merge.
