# Task Dowsing — finding your own work

**Contract:** run the probe sweep → distill evidence into candidates → score →
pitch. Output is one ranked candidate table. You may not invent work; you may
only surface what evidence shows.

## Step 1 — Establish the frame (2 minutes, before any probe)

- What does the client value right now? (Stated goals, recent asks, the
  ledger's dowsing pool from prior tasks.) Ranking is impact-per-effort *in
  their frame*, not yours.
- What is off-limits? (Frozen areas, "don't touch" notes, release windows.)
  Off-limits findings are still recorded — as candidates marked `blocked`.

## Step 2 — The probe sweep

Run what applies; declare what you skip. Capture actual output tails — they
are the evidence column. Suggested concrete forms (adapt to the stack; check
a tool exists before invoking it — tripwire rule):

### Universal probes (any project)

| Probe | Concrete form |
|---|---|
| Test suite | project's test command; note failures, error tails, runtime |
| Confessions | `grep -rn -E "TODO|FIXME|HACK|XXX|WORKAROUND" --exclude-dir={.git,node_modules,dist,vendor} .` |
| Docs drift | run the README quickstart literally, as a new user would; note the first place it breaks |
| Error hygiene | grep for swallowed errors: empty `catch`, `except: pass`, ignored `err` returns |
| Churn hotspots | `git log --since=3.months --name-only --pretty=format: \| sort \| uniq -c \| sort -rn \| head -20` |
| Recent breakage | `git log --oneline -20` scanned for revert/fix/hotfix clusters |
| Large-file smell | files > ~800 lines touched by many commits (churn list ∩ size) |

### Stack-specific probes (run the matching set)

| Stack | Probes |
|---|---|
| JS/TS | `npx tsc --noEmit` · lint script · `npm audit --omit=dev` · `npx depcheck` (unused deps) · lockfile vs manifest drift |
| Python | `ruff check .` (or flake8) · `mypy` if configured · `pip list --outdated` · `pip-audit` if present |
| Rust | `cargo check` · `cargo clippy -- -D warnings` tail · `cargo audit` if installed |
| Go | `go vet ./...` · `go build ./...` · `govulncheck ./...` if installed |
| Other | compiler warnings at max verbosity; the ecosystem's audit tool if present |

Probe budget: the sweep is minutes, not hours. Prefer breadth (all cheap
probes) over depth (one probe exhaustively) — depth belongs to the task that
gets picked.

## Step 3 — Distill findings into candidates

A finding becomes a candidate only if it passes all three filters:

1. **Evidence** — quoted output / file:line exists in your capture.
2. **Actionable** — a plausible task shape exists ("fix the 3 failing tests in
   auth/", not "improve quality").
3. **Non-duplicate** — check the dowsing pool (prior ledgers' PASS-WITH-CONDITIONS
   follow-ups and pooled critique notes) before minting a new candidate.

## Step 4 — Score and rank

| Field | Scale | Meaning |
|---|---|---|
| Impact | 1–5 | value in the client's frame if done (5 = unblocks work / user-facing breakage) |
| Effort | S/M/L | S ≤ 1h, M ≤ half day, L = needs decomposition at G2 |
| Confidence | 1–3 | 3 = evidence directly shows the problem; 2 = evidence suggests, cause unconfirmed; 1 = smell only |
| Risk note | free | what could make this bigger than it looks |

Rank by impact-per-effort, confidence as tiebreak. Low-confidence high-impact
items may be pitched as **spike candidates** ("30-minute investigation to
confirm X") — honest framing beats inflated certainty.

## Step 5 — The pitch

One table, presented to the client:

```markdown
| # | Candidate | Evidence | Impact | Effort | Conf | Notes |
|---|-----------|----------|--------|--------|------|-------|
| 1 | Fix 3 failing auth tests | `npm test` tail: "3 failed — auth/session.spec" | 5 | M | 3 | failures predate HEAD~5 |
Probes skipped: cargo/* (not a Rust project), npm audit (offline).
```

- Client picks → that candidate enters the micro-waterfall; this pitch **is**
  its G0 artifact.
- Standing auto-pick authority → take #1, state that you did and why, proceed.
- No candidate survives the filters → say exactly that, with the probe list as
  proof of diligence. "Nothing worth doing" backed by evidence is a legitimate,
  deliverable dowsing result.

## Failure modes to refuse

- **Manufactured urgency** — promoting a `note`-grade smell to a task because
  the sweep "should" find something.
- **Pet-project gravity** — ranking refactors you'd enjoy over breakage the
  client feels. The frame from Step 1 governs.
- **Sweeping forever** — the sweep has a budget; hitting it with partial
  coverage and declared skips beats a complete sweep nobody asked to fund.
