# Skill discovery / SDO (HARD-GATE)

Chain Jail leaf aspect from obra/superpowers
`skills/writing-skills/SKILL.md` (MIT), heading
Skill Discovery Optimization (SDO) / CRITICAL: Description =
When to Use, NOT What the Skill Does, accessed 2026-09-27.

https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md

sha256 (SKILL.md):
`bbdfe742f853562e643a3d40d64476359d47881e39cef80a189283fa26d11ab9`

Mechanical card: `scripts/emperor sdo`
(`scripts/lib/sdo.py`). Skill leaf:
`chains/chain-jail/skill-discovery.md`.

## Iron

```
DESCRIPTION TRIGGERS NOT WORKFLOW
```

1. **Trigger-only** — when-to-use conditions only.
2. **No workflow summary** — never put process steps in description.
3. **Use when** — start with Use when...
4. **Concrete symptoms** — problem / situation, not a step list.
5. **Third person** — no "I can help you...".

## Flags

```
scripts/emperor sdo --reject-workflow-summary
scripts/emperor sdo --reject-no-trigger
scripts/emperor sdo --check-description "Use when creating or editing skills and the YAML description might summarize the workflow"
```

`--check-description` needs Use when / trigger signals and
no workflow-summary tokens.

## Out of scope (not this leaf)

- Whole `writing-skills` skill vendoring
- Authoring iron-law / skill RGR (sibling leaf `authoring-checklist.md`)
- Testing-skills combined pressure (sibling leaf `testing-skills.md`)
- Persuasion-principles wording (sibling leaf `persuasion-principles.md`)
- Keyword-coverage / token-efficiency essay dump
- graphviz / anthropic-best-practices dumps
- embeddings / emperor.py dispatcher
