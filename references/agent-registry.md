# Agent Registry

The detect / sign-in / invoke matrix for enlistable coding agents.

**This registry is a cache of observations, not truth.** Entries marked
`[verified 2026-07-22]` were checked against vendor docs on that date; entries
marked `[verify-at-dowse]` are best-effort and MUST be confirmed against
`<tool> --help` on the actual machine before use. When registry and terminal
disagree, the terminal wins — then update this file (that update is itself a
ledger-worthy observation).

**Standing rules (Vow of Consent):**
- Detection is read-only: `Get-Command` / `command -v`, `--version`, `--help`.
- Sign-ins are performed by the client, in a terminal they opened themselves.
- Auth is confirmed only via the harmless status commands listed here.
- Never read credential/config files for auth state; never pass secrets on
  command lines; never echo tokens.

---

## Claude Code (Anthropic) — native harness

- **Detect:** `claude` on PATH → `claude --version`
- **Skills:** `~/.claude/skills/<name>/SKILL.md` (user), `.claude/skills/` (project) [verified 2026-07-22]
- **Sign-in (client's terminal):** run `claude` interactively; it prompts for login on first run. `claude --help` for current auth subcommands [verify-at-dowse]
- **Auth probe:** cheapest is a tiny no-op prompt (below) — it fails fast when unauthenticated. [verify-at-dowse]
- **Headless invoke:**
  `claude -p "<prompt>" --output-format json` (or default text)
  Useful flags: `--append-system-prompt "<extra>"`, `--allowedTools "<list>"`,
  `--permission-mode <mode>`, `--model <model>`, `-c` (continue), `-r <id>` (resume) [verify-at-dowse for exact current forms]
- **Routing strengths:** strongest-model work — design, judgment, hairy debugging, orchestration itself.

## Kimi CLI (Moonshot AI)

- **Detect:** `kimi` on PATH → `kimi --version`
- **Install (client runs):** [verified 2026-07-22]
  - Windows: `Invoke-RestMethod https://code.kimi.com/install.ps1 | Invoke-Expression`
  - Linux/macOS: `curl -LsSf https://code.kimi.com/install.sh | bash`
  - Alt: `uv tool install --python 3.13 kimi-cli` (Python 3.12–3.14 supported)
- **Skills:** open Agent Skills format. Search paths [verified 2026-07-22]:
  - user, brand group: `~/.kimi/skills/`, `~/.claude/skills/`, `~/.codex/skills/`
  - user, generic group: `~/.config/agents/skills/` (recommended), `~/.agents/skills/`
  - project (from nearest `.git`): `.kimi/skills/`, `.claude/skills/`, `.codex/skills/`, `.agents/skills/`
  - `merge_all_available_skills` config defaults to true (all present dirs merge)
  - Invoke in-session: `/skill:<name>`; flow skills: `/flow:<name>` (Kimi extension)
- **Sign-in (client's terminal):** run `kimi`, then `/login` (browser OAuth or API key) [verified 2026-07-22]
- **Headless invoke:** no headless flag documented in the getting-started guide as of 2026-07-22. Options: check `kimi --help` at dowse time; the **kimi-agent-sdk** (github.com/MoonshotAI/kimi-cli ecosystem) provides programmatic access; `kimi acp` exposes Agent Client Protocol for editor/orchestrator integration. [verify-at-dowse]
- **MCP:** `kimi mcp add|list|remove|auth`, `--mcp-config-file <path>`
- **Routing strengths:** capable general worker; shares skill dirs with Claude Code — zero-conversion skill reuse.

## Codex CLI (OpenAI)

- **Detect:** `codex` on PATH → `codex --version`
- **Skills:** `~/.codex/skills/` [corroborated 2026-07-22 via Kimi's brand-path list; verify-at-dowse]
- **Sign-in (client's terminal):** `codex login` (browser); headless machine: `codex login --device-auth`; API key: `printenv OPENAI_API_KEY | codex login --with-api-key` [verified 2026-07-22]
- **Auth probe:** `codex login status` [verified 2026-07-22]
- **Headless invoke:** `codex exec "<prompt>"` — runs one session to completion, events to stdout, exits when done. Non-interactive: approval requests fail unless policy auto-approves — set sandbox/approval flags per `codex exec --help` [verified concept 2026-07-22; exact flags verify-at-dowse]
- **Routing strengths:** implementation and test work; CI-friendly exec mode.

## Copilot CLI (GitHub) — standalone `copilot`

- **Detect:** `copilot` on PATH → `copilot --version`. (The old `gh copilot` extension is retired; the standalone command is the current product, GA since 2026-02-25.) [verified 2026-07-22]
- **Install (client runs):** npm / Homebrew / WinGet / install script — see docs.github.com Copilot CLI pages [verified availability 2026-07-22; exact package name verify-at-dowse]
- **Sign-in (client's terminal):** GitHub auth via the CLI's login flow (`copilot --help`); if `gh` is present, `gh auth status` is a useful adjacent probe [verify-at-dowse]
- **Headless invoke:** `copilot -p "<prompt>"` (programmatic mode); `-s` for quieter output; `--no-ask-user` to prevent interactive pauses; tool-permission flags available for CI [verified 2026-07-22]
- **Extras:** supports skills, custom agents, MCP servers, TypeScript SDK.
- **Routing strengths:** GitHub-context work (PRs, issues, Actions), repo Q&A, implementation.

## opencode (SST)

- **Detect:** `opencode` on PATH → `opencode --version`
- **Skills:** `~/.opencode/skills/` [verified 2026-07-22]; instructions file: `AGENTS.md` is canonical (reads `CLAUDE.md` as fallback) [verified 2026-07-22]
- **Sign-in (client's terminal):** provider keys via opencode's auth flow — `opencode --help` / `opencode auth --help` [verify-at-dowse]
- **Headless invoke:** `opencode run "<prompt>"` (non-interactive); skill-scoped: `opencode run --skill <name>`; server mode: `opencode serve` then `opencode run --attach <url> "<prompt>"` [verified 2026-07-22; flag details verify-at-dowse]
- **Routing strengths:** open-source harness, provider-flexible (can front many models incl. local); good second-vendor critic.

## Ollama (local models)

- **Detect:** `ollama` on PATH → `ollama --version`
- **Liveness/auth probe:** `ollama list` (also shows pulled models). No account needed — local. If the daemon is down, `ollama serve` (client decides; it occupies a terminal) [verified stable behavior]
- **Headless invoke:** `ollama run <model> "<prompt>"` → stdout. HTTP API at `http://localhost:11434` for structured use. Persona baking: Modelfile with `SYSTEM` — see `adapters/ollama/`
- **Model pulls change disk state:** `ollama pull <model>` only with client consent.
- **Routing strengths:** free bulk/mechanical work, privacy-sensitive content that must not leave the machine, hetero-critique diversity. **Not** an orchestrator — small local models judge poorly; they work, you judge.

---

## Others frequently found (all [verify-at-dowse])

`aider`, `gemini` (Gemini CLI), `goose`, `qwen` (Qwen Code), `amp`,
`cursor-agent`, `droid` — the ecosystem breeds monthly. For any of them, run
the extension ritual below rather than guessing.

## Extension ritual (unknown agent)

1. `<tool> --version`, `<tool> --help` — capture both outputs.
2. Identify: non-interactive/print mode flag; auth status command; skill or
   instruction-file mechanism; config location (for documentation only, not
   reading credentials).
3. Ask the client to perform any login (their terminal).
4. Trial with a no-op prompt ("Reply with exactly: ok") before real dispatch.
5. Add the observed entry to this file with today's date.
