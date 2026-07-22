# Task Ledger — <task-id>

- **Task:** <one line>
- **Origin:** assigned (client's words, quoted: "…") | dowsed (evidence: …)
- **Started / closed:** <date> / <date>
- **Standing policies in effect:** <none | auto-pick authority | dispatch policy …>

## G0 — Dowse
<what the task is; ambiguities surfaced; client's pick if dowsed>

## G1 — Require
- **Acceptance criteria:**
  1. <checkable statement>
- **Out of scope:** <list>
- **Assumptions (labeled):** <list — each also appears in Claim Ledger>

## G2 — Design
- **Approach:** <paragraph>
- **Rejected alternative:** <one line + why>
- **Impact map:** <files/systems; blast radius; rollback story if stateful>
- **Test plan:** <criterion → probe that proves it>
- **Planned dispatches (if any):** <agent → work item, consented at gate>

## G3 — Build
- **Change summary:** <what was changed, where>
- **Design divergences:** <none | recorded + re-judged>
- **Tripwires observed:** <flags/APIs/paths checked before use>

## G4 — Verify (the Trial)
- **Test plan execution:** <probe → quoted output tail>
- **Claim audit:** all rows terminated? <yes/no + link to claim ledger below>
- **Self-critique:** <link/paste of critique.md outcome>
- **Hetero-critique:** <agent used + outcome | unavailable (noted)>
- **Verdict:** PASS | PASS-WITH-CONDITIONS (<follow-ups → dowsing pool>) | FAIL → <phase>

## G5 — Deliver
- **Delivered as:** <commit/PR/patch/report + where>
- **Report given:** <the calibrated summary the client received>

## Claim Ledger
(embed the `claim-ledger.md` table here, or split claims into their own file
beside this ledger and point to it)

## Provenance (enlisted agents)
| Work item | Agent | Prompt file | Output file | Verified by |
|---|---|---|---|---|

## Lifespan Ledger
| Phase | Spend (rough tokens/time) | What it bought |
|---|---|---|
| Dowse | | |
| Require | | |
| Design | | |
| Build | | |
| Verify | | |
| Deliver | | |

*An empty "What it bought" cell is a Vow 6 finding — record it below.*

## Breach Register
| Vow | What happened | Discovered | Remediation | Lesson (one line) |
|---|---|---|---|---|

## Postmortems (if Holy Chain engaged)
`BROKE: … | CAUSE: … | HEAL: … | CAUGHT-BY: … | WOULD-HAVE-CAUGHT-SOONER: …`
