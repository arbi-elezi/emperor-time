# Sign-In Handoff — the privacy exchange

**Contract:** get a NEEDS-SIGN-IN agent to AVAILABLE without ever touching the
authentication yourself. The client performs the login in a terminal they
opened; you verify afterward by status command only. Output: the roster entry
updated with the verification evidence.

## The invariants (absolute — breaching any is a Vow 5 register entry)

1. You never run a login command, interactive or headless — not even when the
   client says "just do it for me". The refusal is one polite sentence plus
   the exact command *they* can run.
2. You never read credential files, keychains, token stores, or auth-bearing
   env vars — not to "check", not to debug.
3. You never place secrets in prompts, command lines, ledgers, or logs. If a
   client pastes a key into chat: don't echo it, don't store it, tell them to
   rotate it if it's sensitive, and point them to the tool's own secure entry
   flow.
4. Verification is exit-code + first-line summarization of a status command.
   If status output contains anything token-shaped, it is summarized
   ("authenticated as <account>"), never quoted.

## The handoff, step by step

1. **Name the exact command** from `references/agent-registry.md` (verify the
   registry against `<bin> --help` first — a wrong login command wastes the
   client's time and your credibility):

   | Agent | Client runs (their own new terminal) |
   |---|---|
   | Claude Code | `claude` (first-run login flow) |
   | Kimi CLI | `kimi` then `/login` (browser OAuth or API key) |
   | Codex CLI | `codex login` · headless machine: `codex login --device-auth` |
   | Copilot CLI | login flow per `copilot --help` |
   | opencode | provider keys per `opencode --help` auth flow |
   | Ollama | none — local; if daemon down: `ollama serve` (occupies the terminal) |

2. **Say why the new terminal**: the login opens browsers/reads keystrokes/
   writes token files — none of which should pass through an AI agent's
   transcript. One sentence; clients follow reasons better than rules.

3. **Wait.** No polling loops against auth state; the client says "done".

4. **Verify with the status command only** (`codex login status`,
   `gh auth status`, `ollama list`, or the agent's dowsed equivalent), with a
   timeout (a hung status probe is a roster note, not a hung session):

   - exit 0 → roster: `AVAILABLE (verified <date>, status cmd)`
   - nonzero → report the exit/first line, ask the client to retry — never
     "let me try logging in instead".
   - no status command exists → first real dispatch doubles as the probe; say
     so, expect failure gracefully.

5. **Record** in the ledger: `SIGN-IN HANDOFF: codex — client completed
   <date>; verified: "codex login status" exit 0`. The record contains the
   *fact* of authentication, never its material.

## Failure modes

| Situation | Handling |
|---|---|
| Client wants to paste credentials to you | Decline (one sentence), point at the tool's own flow; if pasted anyway: don't echo/store; suggest rotation if sensitive |
| Login "succeeded" but status still fails | Lie-detection reflex: trust the status probe over the memory of success; common causes to suggest — wrong account, expired flow, PATH pointing at an older binary (`<bin> --version` both terminals) |
| Agent has no non-interactive auth story at all | It can still work interactively *driven by the client*; note in roster as `INTERACTIVE-ONLY`; exclude from headless dispatch |
| Client asks you to store a key "for next time" | Config files and env are theirs to set; you may name where the tool reads from (its documented env var), but you never write it |
