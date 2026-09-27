# Verification-before-completion checklist — evidence HARD-GATE

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md
- source-hash: sha256:2befe7fc55bcadaa3d97dd9e8efeb633d2561c0ebe74c5a8b17c4d9e7e4520b3
- heading: The Iron Law + The Gate Function
- license: MIT
- issue-context: emperor-verify / Judgment had claim-audit + gate g4 unquoted-VERIFIED reject but no enforceable identify→run→read→verify→claim card before completion language; Chain Jail extract-aspect names Iron Law / Gate Function only (not whole verification-before-completion skill, not rationalization essays, not red-flag catalogs)

**Contract:** before claiming tests pass, bug fixed, build green, requirements met, agent done, or any satisfaction/completion phrasing — and before commit/PR/deliver — complete the evidence checklist. Identify the proving command. Run it fresh. Read the full output. Confirm the claim. Only then assert, with quoted evidence. Emperor Time stays the orchestrator via emperor-verify + Judgment; do **not** announce or load whole `verification-before-completion`.

Mechanical card: `scripts/emperor evidence` (Python: `scripts/lib/evidence.py`).
G4 still owns ledger shape: `scripts/gate.sh g4 <task-dir>`.

## HARD-GATE — The Iron Law

```
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

If you have not run the proving command in **this** message, you cannot claim
it passes. Prior greens, confidence, and agent "success" reports are rumor
(Vow of Evidence).

Skip identify/run/read/verify and say "done" / "fixed" / "passing"? **Stop.**
That is lying, not verifying. Delete the claim; replay the gate.

## Evidence steps (Gate Function)

Complete each step before the next. Mechanical `--advance` rejects skips.
`--reject-unverified` always fails (hard gate when jumping to a completion claim).

### Step 1: IDENTIFY — Name the proving command

One concrete command that would prove **this** claim:

| Claim | Requires |
|-------|----------|
| Tests pass | Exact test command; 0 failures in output |
| Linter clean | Exact linter; 0 errors |
| Build succeeds | Exact build; exit 0 |
| Bug fixed | Command that reproduced the symptom; now passes |
| Regression test works | Red→green cycle quoted |
| Agent completed | VCS diff / probe you ran, not the agent report |
| Requirements met | Line-by-line G1 checklist with evidence |
| Eval / G4 green | `scripts/eval.sh` or `scripts/gate.sh g4 <task-dir>` |

ET: ledger the command argv **before** running (claim HYPOTHESIS → experiment).

### Step 2: RUN — Execute the FULL command fresh

Run it in this turn. Complete output. No reuse of a prior session green.
No "should pass after that edit."

### Step 3: READ — Full output, exit, failure count

Read end-to-end. Note exit code and failure count (or the PASS tail you will quote).
Partial scrolls and "looks good" are not READ.

### Step 4: VERIFY — Does output confirm the claim?

- If **NO**: state actual status with evidence. Do not claim.
- If **YES**: proceed to Step 5 with the quote ready.

### Step 5: CLAIM — Assert only with quoted evidence

Write the claim **with** the quoted command output (or two independent sources).
Then hand to claim-audit / `scripts/gate.sh g4` as usual. Unquoted VERIFIED
rows still fail g4.

## Quick reference

| Step | Key | Success | ET hook |
|------|-----|---------|---------|
| 1. IDENTIFY | Exact proving command | Argv ledgered | Vow of Evidence |
| 2. RUN | Fresh this turn | Exit captured | experiment row |
| 3. READ | Full output | Failures counted | quote candidate |
| 4. VERIFY | Match claim? | YES/NO with evidence | honest status |
| 5. CLAIM | Quote in claim | VERIFIED-shaped row | g4 / deliver |

## MUST

| Thought | Reality |
|---|---|
| "Should work now" | RUN the proving command |
| "I'm confident" | Confidence ≠ evidence |
| "Just this once" | No exceptions |
| "Agent said success" | Verify independently (diff / probe) |
| "Partial check is enough" | Partial proves nothing |
| "Load Superpowers verification-before-completion wholesale" | Forbidden — leaf only; ET + emperor-verify orchestrate |

## MUST-NOT

- Vendor whole `verification-before-completion` (red-flag essays, full excuse tables) into always-on prompt.
- Claim completion / satisfaction before Step 4 YES with a quote from Step 2–3.
- Reuse a prior-run green as "fresh."
- Call g4 VERIFIED without a quote (mechanical gate already rejects; this leaf is the pre-claim rite).

## Related

- `skills/emperor-verify/SKILL.md` — VERIFY entry; MUST open this leaf before completion claims
- `scripts/lib/evidence.py` — mechanical checklist card
- `chains/judgment-chain/claim-audit.md` — spot-check VERIFIED rows
- `scripts/gate.sh` g4 — unquoted VERIFIED reject
- `chains/chain-jail/extract-aspect.md` — verification-before-completion → Iron Law / Gate Function
- `chains/chain-jail/navigation.md` — evidence gap → this leaf
