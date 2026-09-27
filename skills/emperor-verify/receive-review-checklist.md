# Receive-review checklist — receiving-code-review HARD-GATE

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/receiving-code-review/SKILL.md
- source-hash: sha256:091df1629510af1b92fc4abd6f96732ebedb4cb2c0f3457e8f2740b0504a2438
- heading: The Response Pattern + Forbidden Responses + When To Push Back
- license: MIT
- issue-context: emperor-verify had request-review + ACT severity gates but no enforceable READ→UNDERSTAND→VERIFY→EVALUATE→RESPOND→IMPLEMENT card when *receiving* review feedback; Chain Jail extract-aspect names Response Pattern HARD-GATE only (not whole receiving-code-review skill, not performative-agreement essays, not YAGNI catalogs)

**Contract:** before implementing code-review feedback (from a human partner, external reviewer, or hetero-critique), complete the receive-review checklist. Read fully. Restate. Verify against this codebase. Evaluate soundness. Respond technically (or push back with evidence). Only then implement one item at a time with tests. Emperor Time stays the orchestrator via emperor-verify + Judgment; do **not** announce or load whole `receiving-code-review`.

Mechanical card: `scripts/emperor receive` (Python: `scripts/lib/receive.py`).
Companion leaf (request side): `skills/emperor-verify/request-review-checklist.md` / `emperor review`.

## HARD-GATE — The Iron Law

```
NO IMPLEMENT WITHOUT VERIFYING REVIEW FEEDBACK
```

Skip verify/evaluate and jump to "You're absolutely right — implementing now"? **Stop.**
That is performative agreement, not engineering. Restate, check the tree, then act.

## Receive steps (Response Pattern)

Complete each step before the next. Mechanical `--advance` rejects skips.
`--reject-blind-implement` always fails (hard gate when implementing before verify).

### Step 1: READ — Complete feedback without reacting

Read every item end-to-end. Do not start coding mid-read. Do not performatively agree.

ET: ledger `receive: read` with item count before UNDERSTAND.

### Step 2: UNDERSTAND — Restate or ask

Restate each requirement in your own words, or ask. If any item is unclear: **STOP** — do not implement anything yet. Partial understanding of a multi-item batch is wrong implementation.

ET: ledger restatements or clarifying questions; unclear items block IMPLEMENT.

### Step 3: VERIFY — Check against codebase reality

Confirm the feedback against files, tests, and history on *this* tree. Quote paths or commands. Memory of "how it usually works" is rumor (Vow of Evidence).

ET: at least one quoted path, test, or command per batch before EVALUATE.

### Step 4: EVALUATE — Sound for THIS codebase?

Technically correct here? Breaks existing behavior? Reviewer missing context? YAGNI / unused surface? Stack or platform mismatch?

IF wrong or unverifiable: prepare reasoned pushback (Step 5), do not silent-implement.

### Step 5: RESPOND — Technical acknowledgment or pushback

Technical restatement, clarifying ask, or pushback with evidence. Forbidden: "You're absolutely right!", "Great point!", "Let me implement that now" before Steps 3–4.

Push back when: breaks existing behavior; reviewer lacks context; unused/YAGNI; technically incorrect for this stack; conflicts with client prior decisions (stop and ask client).

### Step 6: IMPLEMENT — One item at a time, test each

Only after Steps 1–5 for the items you will touch. Order: blocking (breaks/security) → simple fixes → complex. Test each fix. No batch blind apply.

ET: TDD / evidence leaves still apply per item; reopen request-review when the batch was itself a review gate.

## Rationalizations (refuse)

| Excuse | Reality |
|---|---|
| "Reviewer is senior; just implement" | Verify against *this* tree first. |
| "I'll clarify item 4 after shipping 1–3" | Unclear items block the whole related batch. |
| "Performative thanks keeps the peace" | Technical restatement or pushback. Actions > praise. |
| "External review is gospel" | Skeptical verify; push back with evidence when wrong. |

## ET mapping

| Step | ET home |
|---|---|
| 1 READ | emperor-verify + ledger |
| 2 UNDERSTAND | G1 restatement / ask |
| 3 VERIFY | Vow of Evidence / quoted paths |
| 4 EVALUATE | Judgment claim-audit |
| 5 RESPOND | hetero-critique ACT / pushback with evidence |
| 6 IMPLEMENT | emperor-build + tdd + evidence |

## Forbidden

- Vendor whole `receiving-code-review` into always-on prompt.
- Implement before VERIFY/EVALUATE.
- Performative agreement ("You're absolutely right!") as a substitute for Steps 3–5.
- Batch-apply multi-item feedback with unclear items still open.
