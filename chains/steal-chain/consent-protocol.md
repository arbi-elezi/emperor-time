# Consent Protocol — roster, assignments, standing policies

**Contract:** convert a dowsed roster into client-approved assignments —
per-task asks by default, a recorded standing policy when granted. Output: the
consent record in the ledger. Nothing dispatches without a line here.

## Step 1 — Present the roster

Show the dowsed roster (from `chains/dowsing-chain/system-dowsing.md`)
compactly: agent, state, version, one-line strength. Include NEEDS SIGN-IN
agents (the client may want them enough to log in) and NOT INSTALLED only if
relevant to the task shape.

## Step 2 — The ask

Per task (default mode), ask one concrete question with a recommendation —
never an open-ended "which agents do you want?":

> Task: *write characterization tests for the parser module.*
> Recommendation: **codex** (test authoring, exec mode) with **you** judging;
> alternative: solo. Codex needs sign-in first. Proceed with codex, solo, or
> other?

Rules for the ask:
- Recommendation comes from `routing.md`, stated with its one-line reason.
- Cost/privacy notes surface *in the ask* when relevant ("this sends the diff
  to <vendor>"; "ollama keeps it local"). Consent to an agent is consent to
  where its data goes — make that visible, don't bury it.
- In harnesses with a question tool, use it; in plain chat, ask in one short
  message. Autonomous/background runs with no reachable client: **no new
  enlistments** — solo is the only self-grantable mode (record: "client
  unreachable; proceeded solo").

## Step 3 — Standing policies (the client may pre-approve)

A standing policy replaces per-task asks for its scope. Record verbatim in
the ledger; quote it at each use.

```
STANDING POLICY (granted 2026-07-22, client's words quoted):
  "use ollama for bulk mechanical edits without asking; ask me before
   anything leaves the machine"
Scope: ollama = auto for mechanical edits; cloud agents = ask each time.
Revoked/amended: (append here — policy changes are ledger events)
```

Interpretation rules:
- Policies are read **narrowly**: "use ollama for tests" does not cover using
  ollama for refactors. Outside the literal scope → per-task ask.
- Conflict between policy and today's instruction → today's instruction wins,
  and note the apparent conflict so the client can amend the policy.
- Policies expire with the client's trust, not with time — but re-confirm any
  policy not exercised recently ("still operating under: <quote> — say stop
  to revoke").

## Step 4 — Record

```
CONSENT: task <task-id>
  codex → test authoring        (per-task approval, client msg <date/quote>)
  ollama/qwen3 → bulk renames   (standing policy: "bulk mechanical edits")
  hetero-critique → opencode    (per-task approval)
Declined/limited: client declined gemini ("not that one") — recorded, not re-asked this task.
```

A declined agent stays declined for the task; re-asking the same question in
new words is consent-shopping, and it's the kind of thing the register exists
for.

## What consent does NOT cover (always separate asks)

- **Installs and model pulls** (`ollama pull`, installing a CLI) — disk/state
  changes; own ask.
- **Sign-ins** — approving an agent's use is not approving an account login;
  the handoff aspect (`sign-in-handoff.md`) owns that exchange.
- **Scope expansion** — an agent approved for task A is not approved for task
  B; per-task means per-task.
