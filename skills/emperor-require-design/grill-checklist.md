# Grill checklist — Socratic design before code

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md
- source-hash: sha256:a32d2255354775aa124855aa7100cf276bea096fff4ebb3a0edf57be216e6c72
- heading: "HARD-GATE"
- license: MIT
- issue-context: require-design lacked an enforceable questions-before-code grill; Chain Jail extract-aspect names HARD-GATE only (not whole brainstorming, not visual companion, not writing-plans)

**Contract:** before any implementation action (product code, scaffolding, product deps, external project, or invoking a BUILD skill), complete the grill checklist and get partner approval for the design artifact actually presented. Emperor Time stays the orchestrator via require-design + Judgment; do **not** announce or load whole `brainstorming`.

Mechanical card: `scripts/emperor grill` (Python: `scripts/lib/grill.py`).

**HARD-GATE (mechanical):** `scripts/lib/grill.py` refuses missing path type,
skipped stage, or impl before stage approval (`--reject-no-path` /
`--reject-stage-skip` / `--reject-impl-before-approval` always fail;
`--check-path <task-dir>` validates `Path:` + `Stage approval:` against
spike | bounded | architectural). Questions-before-impl alone is soft theater
without path taxonomy + stage-approval lock.

## HARD-GATE

Before taking any implementation action, complete the selected path's
prerequisites and obtain approval for the stage actually presented:

- **Spike:** partner approves the question and probe (output is an answer; throwaway probes stay labeled).
- **Bounded:** partner approves the short in-chat design. Present, then STOP until an explicit yes.
- **Architectural:** partner reviews and approves the written work order / spec (G2). Conversational design approval only permits writing the work order; work-order approval only permits BUILD.

A reply approves the stage actually presented. Approval of an idea or feature
scope does not approve artifacts that do not exist yet. Resume at the earliest
incomplete stage. Read-only exploration is allowed while prerequisites remain
incomplete.

## Grill steps (questions before code)

Complete each step before the next. Mechanical `--advance` rejects skips.

### Step 1: Classify the path

Announce out loud: spike | bounded | architectural (partner may override).
When in doubt, take the heavier path. Hidden complexity mid-task upgrades —
stop, say so, step up. Nothing downgrades mid-task.

ET: record `Path: spike|bounded|architectural` and later
`Stage approval: …` in the task ledger (mechanical `--check-path` reads these).

### Step 2: Grill intent (Socratic)

Ask **one** focused question at a time about purpose, constraints, or success.
Do not propose features or an approach until intent is clear. Knowing the app
genre does not tell you why the partner wants it.

ET: Dowsing / `emperor-scope` may already hold G0/G1 — grill only the gaps.

### Step 3: Write-back understanding

Summarize intended outcome, constraints, and success criteria. Separate what
they said from assumptions. Invite correction before treating this as the
design brief.

ET: G1 acceptance lines must match the write-back.

### Step 4: Present design (path-scaled)

- Spike: question + probe plan (2–3 sentences).
- Bounded: short in-chat design (approach, files touched, testing).
- Architectural: sectioned design → fill `templates/work-order.md` (Plan header
  via `work_order.py` / G2). No product code yet.

### Step 5: Get approval — then STOP

Wait for an explicit yes on the artifact presented. Presenting the design and
starting implementation in the same breath is skipping the gate. Only after
approval may BUILD / `emperor-tdd` / forge proceed.

## Quick reference

| Step | Key | Success | ET hook |
|------|-----|---------|---------|
| 1. Classify | Announce path; heavier when unsure | Partner can override | ledger / Size |
| 2. Grill intent | One question at a time | Purpose + success clear | scope / Dowsing gaps |
| 3. Write-back | Said vs assumptions | Partner corrects or confirms | G1 match |
| 4. Present design | Path-scaled artifact | Design exists to approve | work-order / chat |
| 5. Approval | Explicit yes; STOP | Gate open for BUILD | G2 → BUILD |

## MUST

| Thought | Reality |
|---|---|
| "Too simple to need a design" | Bounded still gets a short chat design + yes. |
| "I'll start while they read it" | Gate is approval, not design length. STOP. |
| "Call it bounded to skip the work order" | Doubt → heavier path. |
| "They approved the idea, so code is fine" | Idea ≠ design artifact. Resume earliest incomplete stage. |
| "Load Superpowers brainstorming" | Forbidden — leaf only; ET + require-design orchestrate. |

## MUST-NOT

- Vendor whole `brainstorming` (visual companion, companion server, writing-plans handoff router) into always-on prompt.
- Jump to implementation, scaffolding, or product deps before Step 5 approval.
- Announce a foreign master router.
- Turn one approval into permission to skip later stages.

## Related

- `skills/emperor-require-design/SKILL.md` — design entry; MUST open this leaf
- `scripts/lib/grill.py` — mechanical checklist card + path-taxonomy HARD-GATE
  (`--check-path` / `--reject-no-path` / `--reject-stage-skip` /
  `--reject-impl-before-approval`)
- `scripts/lib/work_order.py` — Plan header lock (G2) after grill for architectural
- `chains/chain-jail/extract-aspect.md` — "brainstorming → only HARD-GATE"
- `chains/chain-jail/navigation.md` — Socratic design gap → this leaf
