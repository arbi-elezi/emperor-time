# Debug four phases — systematic checklist for heal

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md
- source-hash: sha256:808fc5717aa88ad65efff312b11c186294d3e6ee301afb584e2f86599b137787
- heading: "The Four Phases"
- license: MIT
- issue-context: heal path lacked an enforceable 4-phase order before proposing fixes; Chain Jail extract-aspect names this leaf only

**Contract:** when breakage is detected (red build, regression, unexpected behavior), complete each phase **before** the next. No fixes without Phase 1. Emperor Time stays the orchestrator via Holy Chain; do **not** announce or load whole `systematic-debugging`.

Mechanical card: `scripts/emperor heal` (Python: `scripts/lib/debug_phases.py`).

## The Four Phases

You MUST complete each phase before proceeding to the next.

### Phase 1: Root Cause Investigation

**BEFORE attempting ANY fix:**

1. Read error messages carefully (stack traces, line numbers, codes — do not skip warnings).
2. Reproduce consistently. If not reproducible → gather more data, do not guess.
3. Check recent changes (diff, commits, deps, config, environment).
4. In multi-component systems: add diagnostic instrumentation at each boundary **before** proposing fixes; run once; identify *where* it breaks.
5. Trace data flow backward to the source of the bad value; fix at source, not symptom (mechanical card: `scripts/emperor trace` / `skills/emperor-heal/root-cause-tracing.md`).

Holy Chain: start at `chains/holy-chain/triage.md`, then `reproduce-and-bisect.md`.

### Phase 2: Pattern Analysis

**Find the pattern before fixing:**

1. Find working examples of similar code in the same tree.
2. Compare against a reference implementation completely (do not skim).
3. List every difference between working and broken — however small.
4. Understand dependencies (settings, config, environment, assumptions).

Holy Chain: still `reproduce-and-bisect.md` (evidence before hypothesis).

### Phase 3: Hypothesis and Testing

**Scientific method:**

1. Form a **single** hypothesis: "I think X is the root cause because Y" — write it down.
2. Test minimally — smallest change, **one variable**.
3. Verify before continuing: worked → Phase 4; failed → **new** hypothesis (do not stack fixes).
4. When you do not know: say so; research; do not pretend.

Holy Chain: combat ledger in `reproduce-and-bisect.md` (prediction before probe).

### Phase 4: Implementation

**Fix the root cause, not the symptom:**

1. Create a failing test / minimal reproduction **before** the fix (`emperor-tdd` / G2).
2. Implement a **single** fix — no riders, no bundled refactor.
3. Verify: cure + no new wounds + mechanism (`heal-and-verify.md` triad).
4. If the fix fails: STOP. Count attempts. If < 3 → return to Phase 1. If ≥ 3 → stop and question architecture with the client (process-healing when the *process* is the wound).

Holy Chain: `heal-and-verify.md`; process wounds → `process-healing.md`.

## Quick reference

| Phase | Key activities | Success criteria | Holy aspect |
|-------|----------------|------------------|-------------|
| 1. Root Cause | Read errors, reproduce, check changes, gather evidence | Understand WHAT and WHY | triage → reproduce-and-bisect |
| 2. Pattern | Working examples, compare | Identify differences | reproduce-and-bisect |
| 3. Hypothesis | One theory, minimal test | Confirmed or new hypothesis | reproduce-and-bisect (combat ledger) |
| 4. Implementation | Failing test, single fix, verify | Bug resolved; triad green | heal-and-verify |

## MUST

| Thought | Reality |
|---|---|
| "Quick fix now, investigate later" | Forbidden. Phase 1 first. |
| "Just try changing X" | That is Phase 4 without 1–3. STOP. |
| "Multiple fixes at once saves time" | Cannot isolate what worked. One variable. |
| "Skip the test, I'll manually verify" | Failing repro/test before fix (Phase 4.1). |
| "Load Superpowers systematic-debugging" | Forbidden — leaf only; ET + Holy Chain orchestrate. |

## MUST-NOT

- Vendor whole `systematic-debugging` (red flags, rationalizations, supporting technique files) into always-on prompt.
- Skip phases under time pressure.
- Propose fixes before Phase 1 is complete.
- Announce a foreign master router.

## Related

- `skills/emperor-heal/SKILL.md` — heal entry; MUST open this leaf
- `chains/holy-chain/SKILL.md` — aspect router
- `scripts/lib/debug_phases.py` — mechanical checklist card
- `chains/chain-jail/extract-aspect.md` — "systematic-debugging → only the 4-phase list"
