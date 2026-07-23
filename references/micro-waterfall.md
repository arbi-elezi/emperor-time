# The Micro-Waterfall

One task, one waterfall, one ledger. Phases are strictly sequential; gates open
only on evidence; sizing scales with the task but **existence of each phase does
not**. Iteration lives *between* tasks (each delivery feeds the next dowsing),
never inside one by skipping ahead.

Create the ledger at task start from `templates/task-ledger.md` →
`.emperor/tasks/<task-id>/ledger.md`. `<task-id>` = short slug + date, e.g.
`fix-login-retry-0722`.

## Phase 0 — DOWSE (intake or discovery)

Establish *what the task even is*.

- Assigned task: restate it; surface ambiguities; collect the constraints the
  client actually said (quote them — don't improve them silently).
- Discovered task: the Dowsing Chain pitch (evidence-backed candidate table)
  and the client's pick (or standing auto-pick authority, noted).

**Gate G0 opens when:** the ledger names the task, its origin (assigned /
dowsed + evidence), and the client's words or pick are on record.

## Phase 1 — REQUIRE

Define *done* before touching *how*.

- Acceptance criteria: checkable statements ("`GET /health` returns 200 within
  50ms", not "should be fast").
- Out-of-scope list: what this task deliberately does not do (scope drift dies
  here, in writing).
- Unknowns become **claims** in the Claim Ledger (CONJECTURE), not silent
  assumptions.
- Ask the client only what evidence cannot answer; dowse the codebase for the
  rest. Working autonomously: choose the defensible default, record it as an
  assumption in the ledger, and flag it in delivery.

**Gate G1 opens when:** acceptance criteria + out-of-scope are written and
every known unknown is either resolved or ledgered as an assumption.

## Phase 2 — DESIGN

Decide *how*, and how you'll *know*.

- The approach, in a paragraph — plus the strongest alternative you rejected
  and why in one line (forces the alternative to actually be considered).
- Impact map: files/systems touched; blast radius; migration/rollback story if
  state is involved.
- **Test plan written now**: which probes/tests will prove each acceptance
  criterion at G4. If a criterion has no plannable test, it isn't a
  criterion — return it to Phase 1.
- Missing capability discovered here → Chain Jail. Work parallelizable across
  agents → plan the Steal Chain dispatch now (assignments proposed at this
  gate, consented before Build).

**Gate G2 opens when:** approach + rejected alternative + test plan exist, and
Judgment's quick pass finds no criterion left untestable.

## Phase 3 — BUILD

The smallest change that satisfies the design.

- Follow the codebase's existing conventions (match, don't impose).
- Tripwire discipline while coding: every flag/API/path you "remember" gets
  observed before use (`references/scientific-method.md`).
- Dispatched agents work here, quarantined (`chains/steal-chain/SKILL.md`);
  their output merges only through Judgment.
- New work discovered mid-build ("while I'm here…") → task candidate for
  Dowsing, not a rider on this task.

**Gate G3 opens when:** the change is complete per design, builds/lints clean,
and diverged not at all from G2's design — or the divergence is recorded and
Judgment re-passed the design delta.

## Phase 4 — VERIFY

The Trial. Judgment Chain presides (`chains/judgment-chain/SKILL.md`).

- Execute the G2 test plan; quote outputs into the ledger.
- Claim audit: every Claim Ledger row terminated (VERIFIED / REFUTED /
  labeled CONJECTURE or UNVERIFIABLE).
- Self-critique (prosecutor protocol) — always. Hetero-critique — when any
  other agent is available.
- Verdict: PASS / PASS-WITH-CONDITIONS (follow-ups → Dowsing) / FAIL → back to
  the earliest wrong phase.

**Gate G4 opens when:** verdict is PASS or PASS-WITH-CONDITIONS, recorded with
the critique artifact.

## Phase 5 — DELIVER

- Ship the change the way this project ships (commit/PR/patch/report — follow
  house rules; commit only if the client's workflow says so).
- **The history belongs to the client**: commit messages follow the repo's own
  conventions and carry **no agent attribution** — no `Co-Authored-By`,
  `Generated-with`, or similar trailers — unless the client explicitly asks
  for them. Provenance lives in the ledger, not in the client's git history.
- The report to the client: outcome first, calibrated language
  (VERIFIED plainly; partial as "likely + evidence"; assumptions and
  CONJECTURE labeled), link/paths to ledger, provenance of enlisted agents,
  conditions from the verdict.
- Close the Lifespan Ledger: per-phase spend → what it bought. Empty "bought"
  cells get a Vow 6 register line.

**Gate G5 (task closes) when:** the client has the report and the ledger is
complete. Then REST: fold follow-ups into the dowsing pool; carry lessons
forward.

## Right-sizing

| Task size | Phase artifact weight |
|---|---|
| Trivial (typo, config flip) | One sentence per phase in the ledger; G4 may be a single quoted probe; whole ledger fits on one screen |
| Normal (bugfix, small feature) | The template as written |
| Heavy (migration, cross-cutting) | Split into multiple tasks at Phase 2 — each gets its own waterfall; the parent task's deliverable is the decomposition |

**Never** right-size by deleting a gate. A one-sentence phase passed its gate;
an absent phase breached Vow 2. The test: someone reading the ledger can see
each gate was consciously opened.

## Fast-path example (trivial task, full compliance)

```
G0 client: "bump copyright year in footer"        (assigned, quoted)
G1 done = footer shows 2026; out-of-scope: other dates in repo
G2 edit Footer.tsx line 41; test: grep rendered output; alt: sed across repo — rejected (out-of-scope)
G3 1-line diff, lint clean
G4 probe: `grep -n "2026" src/Footer.tsx` → quoted hit; prosecutor: checked no other footer variants exist (search quoted); PASS
G5 delivered; lifespan: ~2 min, bought: verified fix + proof it's the only footer
```

Six lines. Every gate opened. That is the discipline at minimum weight.
