# Testing skills — Combined Pressure / Watch Baseline Fail HARD-GATE

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/writing-skills/testing-skills-with-subagents.md
- source-hash: sha256:c711346852c911b24a84aa161e0cff06a4cd7f4e2fa9e9c0a266cead5afcbade
- heading: Combined Pressure / Watch Baseline Fail / Verbatim Rationalizations / Explicit Negation / Stay Green (Testing Checklist)
- license: MIT
- access-date: 2026-09-27
- issue-context: after authoring iron-law / skill RGR, agents still ship skills tested only academically or without watching a baseline FAIL; Chain Jail extract-aspect names testing-skills-with-subagents companion only (not whole writing-skills, persuasion-principles is a sibling leaf; not graphviz). Sibling leaf: authoring-checklist.

**Contract:** before deploying or registering a discipline-enforcing skill, **face it with combined pressure** (3+) and **watch the baseline FAIL without the skill**. Capture rationalizations verbatim. Plug each loophole with an explicit negation. Stay green under max pressure. Emperor Time stays the orchestrator via Chain Jail authoring + emperor-capture; do **not** announce or load whole `writing-skills`.

Mechanical card: `scripts/emperor skill-test` (Python: `scripts/lib/skill_test.py`).
Companion reference: `references/testing-skills.md`.
Authoring RGR companion: `chains/chain-jail/authoring-checklist.md` + `emperor author`.

## HARD-GATE — Every skill faces combined pressure

```
EVERY SKILL FACES COMBINED PRESSURE
```

"What does the skill say?" academic quiz / single-pressure prompt? **Not enough.** Stack three pressures. Watch the agent fail without the skill. Quote the excuses.

## Principles (adapted)

1. **Combined pressure (3+)** — time + sunk cost + exhaustion / authority / economic; single-pressure and academic quizzes do not count.
2. **Watch baseline FAIL without skill** — if you did not watch it fail, you do not know what to prevent.
3. **Capture rationalizations verbatim** — word-for-word excuses; "agent was wrong" is not a baseline.
4. **Explicit negation per loophole** — "Don't keep as reference" not "Don't cheat"; update rationalization table + red flags.
5. **Stay green under max pressure** — re-test after each REFACTOR; one green ≠ bulletproof.

## Gate Function (before deploy / register)

```
BEFORE trial-and-register or marketplace ship:
  Create 3+ combined-pressure scenarios with concrete A/B/C choices.
  Run WITHOUT the skill — quote FAIL + rationalizations verbatim.
  Write the minimal skill addressing those failures.
  Re-run WITH the skill — agent must comply under pressure.
  For each NEW rationalization: explicit negation + table + red flag.
  Re-verify under maximum pressure. Then hand to trial.

  Academic quiz only           → not a skill test
  Skill written before RED     → delete; run baseline first
  Vague counter ("don't cheat")→ write the specific negation
  One green pass               → continue REFACTOR
```

## Mechanical flags

```
scripts/emperor skill-test --reject-academic-only
scripts/emperor skill-test --reject-skip-red
scripts/emperor skill-test --check-pressure-baseline "Combined pressure: time + sunk cost + exhaustion. Watch baseline FAIL without the skill. Capture rationalizations verbatim. Explicit negation per loophole."
```

`--reject-academic-only` / `--reject-skip-red` always exit non-zero.
`--check-pressure-baseline` needs combined-pressure + watch-baseline plus verbatim / explicit-negation / stay-green signals.
