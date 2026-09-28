# Diagnosing — intake + citation + cite-or-fail report HARD-GATE

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/diagnosing-superpowers/SKILL.md
- source-hash: sha256:5a652f8132cc901eb5ca61f89157839f87a2f20aed037fc7a2b51051bc37cd19
- heading: Core principle + Hard rules → Intake before analysis + Workflow step 4 Report (path + cited findings only)
- license: MIT
- access-date: 2026-09-27
- issue-context: diagnosing HARD-GATE landed intake+cite (v0.4.37); report step was still soft theater (claim done after intake+cite without a written report path). Chain Jail extract-aspect names citation + intake + cite-or-fail report skeleton only (not whole diagnosing-superpowers, not 7-analyst prompts, not SP case/report/bundle/issue templates).

**Contract:** when a human partner wants to know why a session went wrong (or wants evidence for a bug report), finish **intake** before locate/triage/report, cite every finding as `path:line`, and write a **cite-or-fail report file** (problem statement + session(s) + findings) to a workspace path before claiming diagnosis done. Numbers come from a transcript or a command you ran, never from memory. Locate paths with `emperor session-discovery` first. Emperor Time stays the orchestrator via emperor-heal; do **not** announce or load whole `diagnosing-superpowers`.

Mechanical card: `scripts/emperor diagnose` (Python: `scripts/lib/diagnose.py`).
Companion reference: `references/diagnosing.md`.
Locate companion: `skills/emperor-heal/session-discovery.md`.
Full diagnosing skill folder (analyst prompts, 7-dimension templates, bundles) is **out of scope**.

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

## HARD-GATE — Cite-or-fail report skeleton

```
CITE_OR_FAIL_REPORT
```

Intake+cite alone is not a finished diagnosis. Write a report file to a workspace path, show it, and give the path. Mechanical skeleton (ET-owned; **not** Superpowers `templates/report.md` / 7-analyst dimensions):

1. **Problem statement** — partner-answered (sessions + expected + happened + observable)
2. **Session(s)** — VERIFIED path(s) and/or session id(s)
3. **Findings** — each finding cites `path:line`, or honest `none found — checked: …`

Run `scripts/emperor diagnose --check-report <path>` before claiming done. Missing report / theater / uncited findings → exit 1.

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
| "Intake+cite is enough; skip the report file" | Soft theater. Write the cite-or-fail report path. |
| "Load diagnosing-superpowers / 7 analysts" | Forbidden — leaf only; ET + Holy Chain orchestrate. |

## ET mapping

| Step | ET home |
|---|---|
| Intake + citation + report HARD-GATEs | emperor-heal + `emperor diagnose` |
| Locate / verify path | emperor-heal + `emperor session-discovery` |
| Debug after evidence | emperor-heal debug-four-phases |
| Evidence claims | emperor-verify / evidence |

## MUST-NOT

- Vendor or load whole diagnosing-superpowers
- Analyst prompts, 7-dimension case/report/bundle/issue templates
- Claim diagnosis done without a `--check-report` path
- Modify, move, or delete session files (read-only)
- Invent findings, numbers, or partner answers
