# Persuasion principles — Authority / Commitment HARD-GATE

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/writing-skills/persuasion-principles.md
- source-hash: sha256:a51bc9bf75189ea73a27b3fb504a2fdfdb966fb1f7f1cdf03203230a216ccc03
- heading: Authority / Commitment / Scarcity / Social Proof / Unity / Reciprocity / Liking (Persuasion Principles for Skill Design)
- license: MIT
- access-date: 2026-09-27
- issue-context: after authoring iron-law / skill RGR and testing-skills pressure, agents still ship critical practices with hedge language ("consider" / "when feasible") or optional framing; Chain Jail extract-aspect names persuasion-principles companion only (not whole writing-skills, not graphviz, not anthropic-best-practices). Sibling leaves: authoring-checklist, testing-skills, skill-discovery.

**Contract:** when authoring **critical / discipline-enforcing** skill practices, **use persuasion principles** so agents comply under pressure. Authority + Commitment are required; add Scarcity, Social Proof, or Unity. Do **not** hedge. Do **not** use Liking for compliance. Emperor Time stays the orchestrator via Chain Jail authoring + emperor-capture; do **not** announce or load whole `writing-skills`.

Mechanical card: `scripts/emperor persuasion` (Python: `scripts/lib/persuasion.py`).
Companion reference: `references/persuasion-principles.md`.
Authoring RGR companion: `chains/chain-jail/authoring-checklist.md` + `emperor author`.
Pressure-test companion: `chains/chain-jail/testing-skills.md` + `emperor skill-test`.
SDO description companion: `chains/chain-jail/skill-discovery.md` + `emperor sdo`.

## HARD-GATE — Critical practice uses persuasion

```
CRITICAL PRACTICE USES PERSUASION
```

Soft "consider when feasible" for a must-follow practice? **Rewrite.** Frame mandatory as optional? **Same violation.**

## Principles (adapted)

1. **Authority** — YOU MUST / Never / Always / No exceptions for discipline and safety-critical practices.
2. **Commitment** — announce skill usage; force A/B/C; track with todos.
3. **Scarcity** — Before proceeding / Immediately after X; block deferral.
4. **Social Proof** — Every time / X without Y = failure; establish norms.
5. **Unity** — our codebase / we both want quality; collaborative judgment.
6. **Reciprocity** — use sparingly or avoid; other principles usually enough.
7. **Liking** — do NOT use for compliance; creates sycophancy.

## Gate Function (before wording critical practices)

```
BEFORE shipping skill body wording for discipline practices:
  Write Authority (MUST/Never/Always/No exceptions).
  Add Commitment (announce / choose A|B|C / tracking).
  Add at least one of Scarcity / Social Proof / Unity.
  Reject hedge ("consider" / "when feasible") and optional framing.
  Reciprocity sparingly. Liking never for compliance.
  Then hand to skill-test pressure + trial.

  Hedge / optional for mandatory → rewrite with Authority
  Authority without Commitment     → add announce / A|B|C / todos
  No scarcity/social/unity boost   → add one boost principle
```

## Mechanical flags

```
scripts/emperor persuasion --reject-hedge
scripts/emperor persuasion --reject-optional
scripts/emperor persuasion --check-persuasion "YOU MUST announce skill usage. Choose A, B, or C. Before proceeding every time."
```

`--reject-hedge` / `--reject-optional` always exit non-zero.
`--check-persuasion` needs authority + commitment plus scarcity / social-proof / unity signals.
