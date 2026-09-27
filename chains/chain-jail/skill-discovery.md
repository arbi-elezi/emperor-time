# Skill discovery (SDO) — description triggers HARD-GATE

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md
- source-hash: sha256:bbdfe742f853562e643a3d40d64476359d47881e39cef80a189283fa26d11ab9
- heading: Skill Discovery Optimization (SDO) / CRITICAL: Description = When to Use, NOT What the Skill Does
- license: MIT
- access-date: 2026-09-27
- issue-context: after authoring iron-law / persuasion wording / testing-skills pressure, agents still ship YAML descriptions that summarize the skill workflow ("dispatches X then Y"), so future agents follow the shortcut and skip the body; Chain Jail extract-aspect names SDO description-trigger companion only (not whole writing-skills, not keyword-coverage essay, not token-efficiency dump, not graphviz, not anthropic-best-practices). Sibling leaves: authoring-checklist, testing-skills, persuasion-principles.

**Contract:** when authoring skill frontmatter, **description = when to use** (triggers / symptoms / situations). Do **not** summarize the skill process or workflow in the description. Emperor Time stays the orchestrator via Chain Jail authoring + emperor-capture; do **not** announce or load whole `writing-skills`.

Mechanical card: `scripts/emperor sdo` (Python: `scripts/lib/sdo.py`).
Companion reference: `references/skill-discovery.md`.
Authoring RGR companion: `chains/chain-jail/authoring-checklist.md` + `emperor author`.
Persuasion companion: `chains/chain-jail/persuasion-principles.md` + `emperor persuasion`.
Pressure-test companion: `chains/chain-jail/testing-skills.md` + `emperor skill-test`.

## HARD-GATE — Description triggers, not workflow

```
DESCRIPTION TRIGGERS NOT WORKFLOW
```

Description that lists the skill's steps ("dispatches subagent per task with code review between")? **Rewrite.** Missing "Use when..." / trigger conditions? **Same violation.**

## Principles (adapted)

1. **Trigger-only** — description answers "Should I read this skill right now?" with when-to-use only.
2. **No workflow summary** — NEVER put the process (dispatches X then Y / write test first watch it fail) in description; agents take the shortcut.
3. **Use when** — start with "Use when..." focusing on triggering conditions.
4. **Concrete symptoms** — name the problem / situation, not a step list.
5. **Third person** — harness injects into system prompt; avoid "I can help you...".

## Gate Function (before shipping description)

```
BEFORE shipping skill YAML description:
  Write Use when... + symptoms / situations (triggers only).
  Reject workflow summary (dispatches / then Y / write test first / step lists).
  Reject missing trigger signals and first-person help blurbs.
  Capability surface may name the hole; process stays in the body.
  Then hand to persuasion wording + skill-test pressure + trial.

  Workflow summary in description → rewrite to Use when triggers
  No Use when / trigger                 → add when-to-use conditions
  First-person I can help               → third-person Use when
```

## Mechanical flags

```
scripts/emperor sdo --reject-workflow-summary
scripts/emperor sdo --reject-no-trigger
scripts/emperor sdo --check-description "Use when creating or editing skills and the YAML description might summarize the workflow"
```

`--reject-workflow-summary` / `--reject-no-trigger` always exit non-zero.
`--check-description` needs Use when / trigger signals and zero workflow-summary tokens.
