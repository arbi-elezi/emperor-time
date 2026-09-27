# Diagnosing — intake + citation HARD-GATE

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/diagnosing-superpowers/SKILL.md
- source-hash: sha256:5a652f8132cc901eb5ca61f89157839f87a2f20aed037fc7a2b51051bc37cd19
- heading: Core principle + Hard rules → Intake before analysis
- license: MIT
- access-date: 2026-09-27
- issue-context: session-discovery locate card landed (v0.4.36); diagnosing still lacked mechanical intake-before-analysis and path:line citation iron laws. Chain Jail extract-aspect names those two HARD-GATEs only (not whole diagnosing-superpowers, not analyst prompts, not case/report/bundle/issue templates).

**Contract:** when a human partner wants to know why a session went wrong (or wants evidence for a bug report), finish **intake** before locate/triage/report, and cite every finding as `path:line`. Numbers come from a transcript or a command you ran, never from memory. Locate paths with `emperor session-discovery` first. Emperor Time stays the orchestrator via emperor-heal; do **not** announce or load whole `diagnosing-superpowers`.

Mechanical card: `scripts/emperor diagnose` (Python: `scripts/lib/diagnose.py`).
Companion reference: `references/diagnosing.md`.
Locate companion: `skills/emperor-heal/session-discovery.md`.
Full diagnosing skill folder (analyst prompts, templates, bundles) is **out of scope**.

## HARD-GATE — Citation Iron Law

```
NO FINDING WITHOUT PATH:LINE CITATION
```

No citation? **Drop the finding.** Do not invent token totals, wall-clock, or line counts from memory.

## HARD-GATE — Intake before analysis

```
INTAKE BEFORE ANALYSIS
```

Nothing in locate / triage / report starts until the human partner has answered. If they are away, write the questions and **stop**. A statement you reconstructed for them is not an answer. "It took too long" is a complaint, not a problem statement.

## Intake fields (required)

1. **Session(s)** — id and/or VERIFIED path via `emperor session-discovery`
2. **Expected** — what the partner expected
3. **Happened** — what was observed
4. **Observable** — wall-clock, tokens, repeated actions, or one specific action

Ask one question at a time until you can write that statement.

## Cite rules

1. Every finding cites `path:line`.
2. Every number comes from the transcript or a command you ran.
3. Discard any returned finding (including from a subagent) without `path:line`.

## Rationalizations (refuse)

| Excuse | Reality |
|---|---|
| "The problem is obvious, skip intake" | The problem statement scopes everything. Ask. |
| "They're away, so I'll reconstruct the statement" | Write the questions and stop. |
| "I'll sweep everything now and ask at the end" | Unscoped sweeps spend budget on the wrong question. |
| "The price per token is well known" | Numbers you did not compute are invented. Cite or drop. |
| "Load diagnosing-superpowers" | Forbidden — leaf only; ET + Holy Chain orchestrate. |

## ET mapping

| Step | ET home |
|---|---|
| Intake + citation HARD-GATEs | emperor-heal + `emperor diagnose` |
| Locate / verify path | emperor-heal + `emperor session-discovery` |
| Debug after evidence | emperor-heal debug-four-phases |
| Evidence claims | emperor-verify / evidence |

## MUST-NOT

- Vendor or load whole diagnosing-superpowers
- Analyst prompts, case/report/bundle/issue templates
- Modify, move, or delete session files (read-only)
- Invent findings, numbers, or partner answers
