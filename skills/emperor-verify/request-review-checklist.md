# Request-review checklist — HARD-GATE

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/requesting-code-review/SKILL.md
- source-hash: sha256:cfcee1b06774e7c0517f1e09be1a11f2d5680257072723e709ddbcf7e08b795a
- heading: When to Request Review + How to Request + Act on feedback
- license: MIT
- issue-context: emperor-verify had review-pack + Judgment hetero-critique but no enforceable WHEN→SHAS→PACK→DISPATCH→ACT card; Chain Jail extract-aspect names request-review HARD-GATE only (not whole requesting-code-review skill, not receiving-code-review companion, not rationalization essays)

**Contract:** before merge to main, after each major feature, and after each subagent-driven task, complete the request-review checklist. Confirm WHEN. Resolve SHAs. Emit an isolated pack (no author CoT). Dispatch a fresh reviewer. Act on Critical/Important before proceed. Emperor Time stays the orchestrator via emperor-verify + Judgment; do **not** announce or load whole `requesting-code-review`.

Mechanical card: `scripts/emperor review` (Python: `scripts/lib/review_req.py`).
Pack helper (Step 3): `scripts/emperor review-pack <task-dir> <base> <head>` — Python core `scripts/lib/review_pack.py` (thin `review-pack.sh` / `review-pack.ps1`).
Companion leaf (receive side): `skills/emperor-verify/receive-review-checklist.md` / `emperor receive`.

## HARD-GATE — Requested review before proceed

```
NO PROCEED WITHOUT REQUESTED REVIEW
```

Skip dispatch and "just review the diff myself"? **Stop.** That burns the
coordinator context and correlates the verdict with the author. Dispatch.
Ignore Critical / proceed with unfixed Important? **Stop.** Fix first.

Trivial typo/doc-only commits may record `review: skipped (trivial)` in the
ledger after quoting Step 1 WHEN = not-mandatory. Major feature and before-merge
are never trivial.

## Request-review steps

Complete each step before the next. Mechanical `--advance` rejects skips.
`--reject-self-review` always fails (hard gate when author self-reviews).

### Step 1: WHEN — Confirm mandatory trigger

Name one:

| Trigger | Mandatory? |
|---------|------------|
| After each task in subagent-driven development | Yes |
| After completing a major feature | Yes |
| Before merge to main | Yes |
| Stuck / need fresh perspective | Optional but valuable |
| Before refactoring (baseline) | Optional but valuable |
| After fixing a complex bug | Optional but valuable |

ET: ledger `review-trigger: <name>` before SHAs.

### Step 2: SHAS — Resolve BASE and HEAD

```bash
BASE_SHA=$(git merge-base origin/main HEAD)   # or HEAD~n / prior task SHA
HEAD_SHA=$(git rev-parse HEAD)
```

Ledger both SHAs. The product under review is the range, not the session.

### Step 3: PACK — Emit isolated review pack

```bash
scripts/emperor review-pack <task-dir> "$BASE_SHA" "$HEAD_SHA"
```

Expect `review-pack/meta.md`, diff, criteria. No author chain-of-thought.
The pack is the only context the reviewer should need beyond DESCRIPTION + PLAN.

### Step 4: DISPATCH — Fresh reviewer context

Dispatch a **different** context (Steal Chain worker or fresh subagent) with:

- DESCRIPTION — brief summary of what was built
- PLAN_OR_REQUIREMENTS — work-order / G1 criteria / plan path
- BASE_SHA / HEAD_SHA — from Step 2
- The pack from Step 3 (or `git diff BASE..HEAD` instructions)

Rules borrowed and adapted:

- Read-only review on this checkout (no mutate HEAD)
- Reviewer does not spawn further reviewers
- Builder does **not** write the hetero verdict
- Never hand session history

See `chains/judgment-chain/hetero-critique.md` for critic selection and
verification-before-acting.

### Step 5: ACT — Severity-gated response

| Severity | Action |
|----------|--------|
| Critical (Must Fix) | Fix immediately before any further work |
| Important (Should Fix) | Fix before proceed / merge |
| Minor (Nice to Have) | Note for later; do not block if justified |
| Pushback | Only with technical evidence (quoted tests/code) |

Every critic finding starts CONJECTURE — reproduce before acting
(hetero-critique anti-capitulation). Hand the combined critique to
`verdicts-and-breaches.md` for the G4 ruling.

## Quick reference

| Step | Key | Success | ET hook |
|------|-----|---------|---------|
| 1. WHEN | Name the trigger | Trigger ledgered | G4 / finish / major feature |
| 2. SHAS | Bound the product | BASE + HEAD ledgered | git merge-base |
| 3. PACK | Isolated; no CoT | review-pack/ present | `emperor review-pack` |
| 4. DISPATCH | Fresh context | Reviewer returns Strengths/Issues/Assessment | hetero-critique |
| 5. ACT | Severity gates | Critical+Important cleared or evidenced pushback | claim ledger / G4 |

## MUST

| Thought | Reality |
|---|---|
| "I'll just review the diff myself" | Coordinator context must drive, not prosecute. Dispatch. |
| "Reviewer needs my whole session" | Hand crafted context only — product, not thought process. |
| "It's simple; skip review" | Simple diffs ship bugs. Before-merge is mandatory. |
| "Important can wait until after merge" | Important blocks proceed. Fix or evidenced deferral in ledger. |
| "Load Superpowers requesting-code-review wholesale" | Forbidden — leaf only; ET + emperor-verify orchestrate. |

## MUST-NOT

- Vendor whole `requesting-code-review` (receiving-code-review companion, full template essays) into always-on prompt.
- Self-review in place of Step 4 dispatch.
- Announce a foreign master router.
- Call Step 5 done while Critical or Important remain unfixed without ledgered pushback evidence.

## Related

- `skills/emperor-verify/SKILL.md` — VERIFY entry; MUST open this leaf
- `scripts/lib/review_req.py` — mechanical checklist card
- `scripts/lib/review_pack.py` — Step 3 pack emitter (thin `review-pack.sh` / `review-pack.ps1`)
- `chains/judgment-chain/hetero-critique.md` — dispatch + verify findings
- `chains/judgment-chain/gatekeeping.md` — G4 sequence
- `chains/chain-jail/extract-aspect.md` — "requesting-code-review → When/How/Act"
- `chains/chain-jail/navigation.md` — review gap → this leaf
