# CI mode — botified Steal (Fugu-shaped, not Fugu)

**Contract:** same Steal laws (consent, quarantine, no credential files),
different *profile*. Interactive CLI keeps the human-in-the-loop roster.
CI / bot / headless runners use this file.

Sakana Fugu (2026) is a learned orchestrator behind one API: one request in,
internal scaffold over a pool of frontier workers, one answer out. Emperor Time
does not vendor Fugu and does not call Sakana unless the client put that
endpoint in the standing policy. We steal the *shape*: one entrypoint, no
TTY theater, workers as an env-declared pool, artifacts + exit codes.

## Detect profile

CI if any of: `CI=true`, `GITHUB_ACTIONS`, `GITLAB_CI`, `BUILDKITE`,
`EMPEROR_PROFILE=ci`, no TTY on stdin.

Otherwise CLI profile (`consent-protocol.md` + `sign-in-handoff.md`).

## CI standing policy (replaces per-task chat consent)

Consent in CI is **declared**, not conversational:

```
EMPEROR_CONSENT_AGENTS=codex,claude,opencode   # comma list or "none"
EMPEROR_CONSENT_CAPTURE=0|1
EMPEROR_REMOTE_POOL=                    # optional OpenAI-compatible base URLs
```

Missing `EMPEROR_CONSENT_AGENTS` → Steal Chain is dark. Do not invent a roster.
Secrets live in the runner's secret store / OIDC. You never print them.
Sign-in handoff does **not** run in CI. If an agent needs a login, the job
fails with a quoted auth-probe tail and a non-zero exit.

## Bot loop (one entrypoint)

```
issue context → work-order on disk → dispatch workers from the pool
  → quarantine each out.txt → gate.sh → exit 0 or 1
```

No "which execution approach would you prefer?" prompts. No visual companions.
No browser login. Timeouts on every invoke. One retry with a changed prompt,
then fail the job.

## Pool beyond the local machine

CLI profile: local binaries (`claude`, `codex`, `kimi`, `copilot`, `opencode`,
`ollama`) as today.

CI profile may add **remote OpenAI-compatible workers** listed in
`EMPEROR_REMOTE_POOL` (base URL + model name; key from env). Examples of
shapes, not endorsements: a vendor Chat Completions endpoint, a self-hosted
vLLM, a coordinator API the client already pays for. Re-verify the endpoint
with a no-op prompt before real work. Output still lands in
`.emperor/runs/<task>/<worker>/` and starts at CONJECTURE.

Do not hardcode Sakana / OpenAI / Anthropic as required infrastructure.

## CI artifacts

Always write:

- `.emperor/tasks/<id>/ledger.md`
- `.emperor/tasks/<id>/work-order.md` (non-trivial)
- `.emperor/runs/.../out.txt` + `meta.md` (exit code, ms, model)
- job summary: gate tails quoted

`gate.sh g4` or `g5` non-zero fails the pipeline. That is the bot's voice.

## What stays identical to CLI

Quarantine. Vow of Evidence. No worker "done" is G4. No secrets on argv.
Judgment is not delegated.
