# Diagnosing (intake + citation HARD-GATE)

Emperor Time owned guidance for session diagnosis honesty.
Adapted from the Core principle and Intake before analysis Hard rule of
[obra/superpowers](https://github.com/obra/superpowers)
`skills/diagnosing-superpowers/SKILL.md` (MIT), accessed 2026-09-27.
ET + emperor-heal remain the orchestrator; do not load whole
diagnosing-superpowers.

Mechanical card: `scripts/emperor diagnose`
(`scripts/lib/diagnose.py`). Skill leaf:
`skills/emperor-heal/diagnosing.md`.
Locate companion: `references/session-discovery.md`.

## Iron laws

1. **No finding without a `path:line` citation.**
2. **Intake before analysis** — partner-answered problem statement first.

## Intake (before locate)

Write a statement naming:

- session(s) (id and/or VERIFIED path)
- expected outcome
- what happened
- the observable the partner cares about

One question at a time. Complaints ("it took too long") need an observable.
If the partner is away: write the questions and stop.

## Citation

Every finding cites `path:line`. Every number comes from a transcript or a
command you ran in this turn. Discard findings without citations.

## HARD-GATE helpers

```bash
scripts/emperor diagnose --reject-uncited        # always exit 1
scripts/emperor diagnose --reject-skip-intake    # always exit 1
scripts/emperor diagnose --check-citation "..."  # exit 0 only with path:line
```

Invoke `--reject-uncited` when about to emit a finding without citation.
Invoke `--reject-skip-intake` when about to analyze before partner answers.

## Out of scope here

- Full diagnosing-superpowers skill (analyst prompts, case/report templates, bundles, GitHub issues, scrub)
- Embeddings / emperor.py dispatcher
- Mutating session files
