# MUST-route — silent activation without being told

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/using-superpowers/SKILL.md
- heading: "If you think there is even a 1% chance a skill might apply… MUST invoke"
- license: MIT
- issue-context: bakeoff — Superpowers wins *activation* (marketplace fires without "do it"); ET had to be told

**Contract:** at SessionStart (and whenever a new user turn arrives with no governing skill open), Emperor Time **auto-routes**. Do not wait for the client to say `emperor time` or `maximum rigor`.

Emperor Time stays the orchestrator. Do **not** announce or load `using-superpowers` (or any foreign master router). Steal this leaf only.

## Mechanical path

1. Silent boot already wrote `.emperor/host.env` + `survey.md` (hooks / `emperor boot`).
2. Run `scripts/emperor activate` (Python: `scripts/lib/activate.py`). Quote the `ACTIVATION next=` line.
3. Open that skill **before** clarifying questions, exploring, or answering.
4. If the user utterance is available: `scripts/emperor route "<utterance>"` may refine the target; prefer route hit over disk default.
5. Before setup thrash: `scripts/emperor ask-spec --emit "<ask>" --write .emperor/tasks/<id>/ask-spec.md`. G0 `--require-spec` FAILS without a written scoped brief.
6. Subagents dispatched with an explicit task may skip this card (they already have a governing file).

## MUST

| Thought | Reality |
|---|---|
| "They didn't say emperor time" | SessionStart + activate already fired. Open the skill. |
| "I need context first" | Skill check comes *before* clarifying questions. |
| "This is a simple ask" | Still name the situation and open one phase file. |
| "I'll just explore the repo" | Resume / queue / excavate tell you *how* to look. |
| "Load Superpowers activation" | Forbidden — leaf only; ET orchestrates. |

## MUST-NOT

- Vendor whole `using-superpowers` into always-on prompt.
- Skip activate because boot already ran.
- Ask the client their OS/language (read host.env / survey).

## Related

- `skills/emperor-resume/SKILL.md` — resume-from-disk steps after activation picks resume
- `scripts/emperor route` — utterance → skill MVP
- `evals/bakeoff.md` — activation gap this leaf closes
