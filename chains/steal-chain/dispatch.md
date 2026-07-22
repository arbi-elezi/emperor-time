# Dispatch — sending work to an enlisted agent

**Contract:** consented assignment in, captured raw output out. Everything in
between — prompt file, invocation, scoping, timeout — leaves an audit trail
in `.emperor/runs/`. Output never merges here; that is quarantine's job.

## The run directory (fixed layout)

```
.emperor/runs/<task-id>/<agent>/
├── prompt.md      # exactly what was sent
├── out.txt        # stdout (+ stderr interleaved or as err.txt)
└── meta.md        # invocation line, start/end time, exit code, timeout used
```

One directory per agent per task; repeat dispatches append numbered pairs
(`prompt-2.md`, `out-2.txt`). The trail answers, forever: who was asked what,
and what came back.

## Step 1 — Write the worker prompt (prompt.md)

Anatomy — every section present, most one line:

```markdown
OBJECTIVE: <one sentence, one deliverable>
SCOPE: files/dirs you may touch: <list>. Everything else is read-only to you.
CONSTRAINTS: <conventions to follow, things not to do, "do not commit">
CONTEXT: <the minimum needed: the diff, the failing test, the spec excerpt>
OUTPUT FORM: <exactly what to return — diff / file list / findings table>
EPISTEMICS: End with two lists: VERIFIED (what you ran/observed, with the
command and its output tail) and ASSUMED (what you did not verify). An
"all done, everything works" report with empty lists will be rejected.
```

Prompt rules:
- **Scoped small**: one objective per dispatch. Two objectives = two
  dispatches (or one agent doing sequential tasks with separate records).
- **Minimum context**, not the whole repo: enough to do the job; a worker
  drowning in context hallucinates connections. Local models especially
  (window limits — `routing.md`).
- **Vow card for skill-less workers**: prepend the Vow card from
  `adapters/generic/EMPEROR_TIME.core.md` when the worker's harness has no
  Emperor Time installed — it makes the EPISTEMICS section enforceable in
  spirit, not just requested.
- **No secrets. Ever.** Also no client-private material the agent's vendor
  shouldn't see — consent covered this agent, for this task; re-check the
  data actually being sent matches what the client understood (the diff, or
  the whole file? the schema, or the data?).

## Step 2 — Invoke (headless, bounded, captured)

Forms come from `references/agent-registry.md` — **re-verified against
`--help` at dowse time**, not trusted from the page. Canonical shapes:

```bash
claude -p "$(cat prompt.md)" --output-format json  > out.txt 2>&1
codex exec "$(cat prompt.md)"                      > out.txt 2>&1
copilot -p "$(cat prompt.md)" -s --no-ask-user     > out.txt 2>&1
opencode run "$(cat prompt.md)"                    > out.txt 2>&1
ollama run <model> "$(cat prompt.md)"              > out.txt 2>&1
# kimi: no documented headless flag (2026-07-22) — agent-sdk / ACP / interactive
```

Mechanics:
- **Timeout on every invocation** — scale to the work (minutes for a scoped
  edit; never unbounded). Record it in meta.md.
- **Working directory**: the narrowest dir that contains the scope. Harness
  supports read-only / plan / sandbox modes and the task allows → use them
  (least authority is free insurance).
- **Permission flags**: grant the minimum toolset the objective needs
  (e.g. Claude Code's `--allowedTools`), per the observed `--help`.

## Step 3 — Parallel dispatch rules

- Parallelize only **disjoint scopes** — two agents whose SCOPE lists share a
  file is a merge conflict you scheduled. Check the lists before launching,
  not after.
- Shared read-only context is fine; shared writable anything is not.
- Bound the fleet: more concurrent workers than you can quarantine properly
  means unverified output queuing up — admission (quarantine) is the
  bottleneck to plan around, not launch capacity.

## Step 4 — Collect

- Record exit code + wall time in meta.md. Nonzero exit or empty out.txt is a
  *result* (goes to quarantine as evidence of failure), not a thing to hide.
- **Retry policy (Vow 6):** one retry per failure, and only with something
  changed — sharpened prompt (quote the failure back), tightened scope, or
  different agent. Second failure → reassign or do it yourself; note the
  agent's miss in the roster's notes column (routing input for next time).
- Hand `out.txt` to `quarantine.md`. Even beautiful-looking output.
  *Especially* beautiful-looking output.
