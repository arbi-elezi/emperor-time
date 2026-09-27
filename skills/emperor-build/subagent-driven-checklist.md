# Subagent-driven checklist — subagent-driven-development HARD-GATE

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md
- source-hash: sha256:8dde5589ee083fb4999106d116f01c8fdaf3116a8a9813fdedeb80329de49046
- heading: Fresh subagent per task + Task review after each + Fix loop (R of 5) + Final whole-branch review (adapted)
- license: MIT
- issue-context: emperor-build had inline executing-plans HARD-GATE but no enforceable fresh-subagent / per-task-review card when the client has a subagent tool and tasks are independent; Chain Jail extract-aspect names that HARD-GATE only (not whole subagent-driven-development, not implementer/reviewer prompt templates, not Superpowers review-package scripts)

**Contract:** when executing a work-order / plan with *independent tasks* and a subagent tool is available (client did **not** choose inline), complete the subagent-driven checklist. Fresh implementer per task. Task review (spec + quality) before the next task. Fix loop capped at 5. Controller coordinates; does not implement or skip review. Four stops still apply (same as `executing-plans-checklist.md`). Finish with whole-branch review then `emperor finish`. Emperor Time stays the orchestrator via emperor-build + dispatch + verify + finish; do **not** announce or load whole `subagent-driven-development`.

Mechanical card: `scripts/emperor subagent` (Python: `scripts/lib/subagent.py`).
Companion leaves: `skills/emperor-build/executing-plans-checklist.md` (inline path), `skills/emperor-verify/request-review-checklist.md`, `skills/emperor-forge/finish-menu.md`.
Steal-chain enlistment of *external* CLIs stays `skills/emperor-dispatch/SKILL.md` — different door.

## HARD-GATE — The Iron Law

```
FRESH SUBAGENT PER TASK — REVIEW BEFORE NEXT TASK
```

Implement the next task in the controller session, or skip the task review because "self-review was enough"? **Stop.**
That is context pollution and unverified churn. Dispatch a fresh implementer. Review. Then continue.

## When to use (vs `emperor execute`)

| Situation | Path |
|---|---|
| Client chose inline, or no subagent tool | `emperor execute` (executing-plans leaf) |
| Tasks tightly coupled (shared mutable state) | Manual / grill first — not this leaf |
| Independent tasks + subagent tool available | **This leaf** (`emperor subagent`) |

## Four stops (same as execute — only these ask the client)

1. Irreversible or destructive operation.
2. Security-sensitive action.
3. Side effect outside this worktree that norms say you ask about first (merge, push to a shared branch, publish).
4. Plan so broken that every path forward is a guess.

Everything else: decide, ledger `Ruling: <what> — <why> — <cost if wrong>`, continue. No check-in theater between tasks.

## Subagent steps

Complete each step before the next for the overall run. Mechanical `--advance` rejects skips.
`--reject-skip-review` always fails (hard gate when moving to the next task without a clean or parked task review).

### Step 1: SETUP — Gate, workspace, ledger, plan, pre-flight

Confirm When-to-use (table above). Isolated worktree (`emperor iso`) unless client consented to work on main.
Ledger on disk. Read plan once + Spec if named. Pre-flight shared interfaces; ledger rows or `Pre-flight: no shared interfaces`.
Do **not** start Task 1 in the controller.

ET: `emperor iso` + task ledger under `.emperor/` + When-to-use gate ledgered.

### Step 2: DISPATCH — Fresh implementer; brief as a file

Take the next incomplete task. Extract its brief to a uniquely named file (exact values live only there).
Record BASE (`git rev-parse HEAD`) before dispatch.
Dispatch prompt carries: (1) one line of project fit, (2) brief path as requirements, (3) interfaces/decisions prior tasks own that the brief cannot know, (4) your resolution of brief ambiguity, (5) report-file path + status contract.
Never paste session history or "state after Tasks 1–N". Never dispatch multiple implementers in parallel.
Implementer never spawns reviewers or helpers — review arrives from you after the report.
Record implementer agent id (fix rounds 1–3 resume it).

ET: brief + report under `.emperor/runs/<task>/`; harness subagent tool (not Steal-chain CLI unless client consented).

### Step 3: REPORT — Status triage

Handle exactly one of: DONE → build review package and go to Step 4.
DONE_WITH_CONCERNS → read concerns; correctness/scope first, then review.
NEEDS_CONTEXT → answer, re-dispatch.
BLOCKED → change something (context, model, split task, or ledgered plan ruling) then re-dispatch.
Never ignore an escalation or force the same model to retry unchanged.

### Step 4: REVIEW — Spec + quality; never skip

Task-scoped gate. Hand the reviewer a **diff file** for BASE..HEAD (not `HEAD~1`).
Inputs: brief path, report path, diff package, binding global constraints (verbatim from plan/spec).
Both verdicts required: spec compliance AND task quality. Implementer self-review never replaces this.
Do not pre-judge ("do not flag X"). Do not re-run tests the report already evidenced without cause.
Confirm ⚠️ "Cannot verify from diff" items yourself before marking the task complete.

ET: `emperor review` / review-pack for packaging; keep controller context clean.

### Step 5: FIX — Loop R of 5; controller never fixes

Trigger: spec ❌, Critical/Important, or confirmed ⚠️ gap.
Minors → ledger deferred; never enter the loop.
Plan conflicts → you rule with Spec as authority; ledger before acting.
Rounds 1–3: resume original implementer with open findings verbatim.
Rounds 4–5: fresh implementer on a more capable model; point at the report file.
Every round: fix + covering tests + command + output in the report, then scoped re-review of the fix range only.
After each round ledger: `Task <N>: fix round <R>/5 (...)`.
**Breaker at R=5:** stop dispatching; adjudicate (park with ruling, or rule load-bearing and carry forward). Adjudicate only at the cap.
Never fix findings yourself in the controller session.

### Step 6: COMPLETE — Task-done, next task, final review, finish

Ledger `Task <N>: complete (...)` only when review is clean or every open finding is parked-with-ruling at the cap.
Next incomplete task → back to Step 2 without asking permission.
After all tasks: whole-branch review (fresh reviewer; diff package from merge-base). ONE fix wave + one scoped re-review; adjudicate residuals.
Collect every `Ruling:` into the final message. Then `emperor finish`. Do not assume they want a PR.

## Rationalizations (refuse)

| Excuse | Reality |
|---|---|
| "I'll just do this small task in the controller" | Controller context is for coordination. Fresh implementer. |
| "Self-review was thorough; skip task review" | Same author, same blind spots. Both verdicts required. |
| "Dispatch two implementers to go faster" | Parallel implementers conflict. One at a time. |
| "I'll paste Tasks 1–3 summary so it has context" | That is session pollution. Brief + interfaces only. |
| "Fix it myself; the loop is slow" | Controller fixes skip review. Dispatch a fix round. |
| "Close enough on spec" | Spec ❌ = not done. Fix or hit the breaker and adjudicate. |
| "Let me check in before the next task" | Client chose execution. Only the four stops stop you. |
