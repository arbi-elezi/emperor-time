#!/usr/bin/env bash
# Dowsing Chain, Mode 2 - scan this machine for enlistable coding agents.
# READ-ONLY (Vow of Consent): detects binaries and probes --version only.
# Never installs, never logs in, never reads credential/config files.
# Auth probes run ONLY with --check-auth, using harmless status commands.
#
# Usage: ./dowse.sh [--check-auth] [--skip-versions]

set -u
CHECK_AUTH=0
SKIP_VERSIONS=0
for arg in "$@"; do
  case "$arg" in
    --check-auth)    CHECK_AUTH=1 ;;
    --skip-versions) SKIP_VERSIONS=1 ;;
    *) echo "unknown arg: $arg" >&2; exit 2 ;;
  esac
done

# Probes must never hang the scan (e.g. `ollama list` blocks when the daemon
# is down). GNU timeout where present (Linux, Git Bash); background watchdog
# otherwise (stock macOS ships no `timeout`).
PROBE_TIMEOUT="${EMPEROR_PROBE_TIMEOUT:-8}"
run_with_timeout() {
  _rt_secs="$1"; shift
  if command -v timeout >/dev/null 2>&1; then
    timeout "$_rt_secs" "$@" 2>/dev/null
  else
    "$@" 2>/dev/null &
    _rt_pid=$!
    ( sleep "$_rt_secs"; kill "$_rt_pid" 2>/dev/null ) &
    _rt_watch=$!
    wait "$_rt_pid" 2>/dev/null
    _rt_rc=$?
    kill "$_rt_watch" 2>/dev/null
    wait "$_rt_watch" 2>/dev/null
    return "$_rt_rc"
  fi
}

# name|binary|safe-auth-cmd(or -)|sign-in hint
AGENTS='Claude Code|claude|-|run `claude` interactively (first-run login)
Kimi CLI|kimi|-|run `kimi`, then /login
Codex CLI|codex|login status|codex login  (headless: codex login --device-auth)
Copilot CLI|copilot|-|see `copilot --help` login flow
opencode|opencode|-|see `opencode --help` / auth subcommand
Ollama|ollama|list|none (local); daemon must be running
GitHub CLI|gh|auth status|gh auth login
Aider|aider|-|API key env vars (client sets)
Gemini CLI|gemini|-|see `gemini --help`
Goose|goose|-|see `goose --help`
Qwen Code|qwen|-|see `qwen --help`'

echo
echo '=== EMPEROR TIME :: DOWSING CHAIN :: machine scan ==='
echo '(read-only: no installs, no logins, no credential access)'
echo
printf '%-14s %-15s %-28s %s\n' 'AGENT' 'STATUS' 'VERSION' 'AUTH'
printf '%-14s %-15s %-28s %s\n' '-----' '------' '-------' '----'

DETECTED=0
while IFS='|' read -r name bin authcmd login; do
  status='NOT INSTALLED'; version=''; auth='unchecked'
  if command -v "$bin" >/dev/null 2>&1; then
    status='DETECTED'; DETECTED=$((DETECTED+1))
    if [ "$SKIP_VERSIONS" -eq 0 ]; then
      version=$(run_with_timeout "$PROBE_TIMEOUT" "$bin" --version | head -n 1)
      [ -n "$version" ] || version='(no version output)'
    fi
    if [ "$CHECK_AUTH" -eq 1 ]; then
      if [ "$authcmd" != '-' ]; then
        # capture without a pipe so the status command's own exit code decides
        # shellcheck disable=SC2086  # intentional word-split of the safe status cmd
        if out=$(run_with_timeout "$PROBE_TIMEOUT" "$bin" $authcmd); then
          auth="OK: $(printf '%s\n' "$out" | head -n 1)"
        else
          auth="NEEDS SIGN-IN (status cmd failed or hung >${PROBE_TIMEOUT}s)"
        fi
      else
        auth="no safe status cmd known - verify via \`$bin --help\`"
      fi
    fi
  fi
  printf '%-14s %-15s %-28.28s %s\n' "$name" "$status" "$version" "$auth"
done <<EOF
$AGENTS
EOF

echo
echo "Detected: $DETECTED agent(s)."
echo
echo 'Next steps (Steal Chain protocol):'
echo '  1. Verify each invocation syntax against reality:  <binary> --help'
echo '  2. Agents needing sign-in: the CLIENT logs in, in a NEW terminal they'
echo '     open themselves (never the orchestrator'"'"'s shell).'
echo '  3. Re-run with --check-auth to confirm via harmless status commands only.'
echo '  4. Hand the roster to chains/steal-chain/SKILL.md for consent + dispatch.'
