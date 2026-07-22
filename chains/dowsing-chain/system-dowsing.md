# System Dowsing — scanning the machine for counterpart agents

**Contract:** detect → profile → classify → hand a roster to Steal Chain.
Read-only throughout: no installs, no logins, no credential access, no config
reads. The roster is the single artifact.

## Step 1 — Detect

Preferred: the bundled scripts (they encode these rules):

```
Windows :  scripts\dowse.ps1        [-CheckAuth] [-AsJson] [-SkipVersions]
POSIX   :  scripts/dowse.sh         [--check-auth] [--skip-versions]
```

Manual fallback (per binary in `references/agent-registry.md`):

```
Windows :  Get-Command <bin> -ErrorAction SilentlyContinue
POSIX   :  command -v <bin>
then    :  <bin> --version        (bounded — never let a probe hang the scan)
```

Probe hygiene learned the hard way: **every probe gets a timeout** (~8s). A
blocked probe (e.g. `ollama list` with the daemon down) must degrade to a
`TIMEOUT` roster note, not a hung scan.

## Step 2 — Profile (the verify-at-dowse ritual)

For each detected binary, before it may be dispatched to:

1. Capture `<bin> --help` (and the relevant subcommand's `--help`).
2. Record the **observed** forms, not the remembered ones:
   - non-interactive / print-mode invocation
   - auth *status* command (status only — never the login command run by you)
   - version string
3. Diff against `references/agent-registry.md`. Registry disagrees with the
   terminal → **terminal wins**; update the registry entry with today's date
   (that update is a ledger-worthy observation).
4. Unknown agent (not in the registry) → full extension ritual in the registry
   file's last section; add the entry you observed.

## Step 3 — Classify

| State | Criteria | Roster action |
|---|---|---|
| `AVAILABLE` | binary present + auth confirmed via harmless status command (`gh auth status`, `codex login status`, `ollama list`) | eligible for consent + dispatch |
| `NEEDS SIGN-IN` | binary present, status command reports unauthenticated / exits nonzero | hand to client with the exact login command **they** run in **their own** new terminal |
| `TIMEOUT` | status probe exceeded its bound | note likely cause (daemon down?); re-probe once after client action, else treat as NEEDS SIGN-IN |
| `NO STATUS CMD` | binary present, no safe status command known | verify via `--help`; if none exists, first dispatch doubles as the auth probe (expect failure, say so) |
| `NOT INSTALLED` | absent | list install command from registry *for the client to run* if they want it |

## Step 4 — The roster artifact

```markdown
| Agent | State | Version | Observed headless form | Sign-in (client-run) | Notes |
|-------|-------|---------|------------------------|----------------------|-------|
| kimi  | NEEDS SIGN-IN | 0.27.0 | none documented — SDK/ACP routes | run `kimi`, then /login | shares ~/.claude/skills |
Scan date: <date>. Probes skipped/timed out: <list>.
```

Record it in the ledger, hand to `chains/steal-chain/SKILL.md` (consent is
Steal Chain's job, not yours). Re-scan triggers: client says an agent was
added/signed in; a dispatch fails with auth-shaped errors; scan older than the
session.

## The privacy floor (absolute, inherited by every later step)

- Detection reads PATH and versions — nothing else.
- Auth state is inferred **only** from status-command exit/output; never from
  reading `~/.config/**`, keychains, env vars, or token files.
- If a status command's output contains anything token-shaped, it is not
  quoted into the roster — summarize as "authenticated as <account>" and move on.
