#!/usr/bin/env zsh
# zsh peer of scripts/emperor (bash). Same tools. Host encoding + WSL interop.
# Silent-boots when .emperor/host.env is missing (twin of scripts/emperor).
emulate -L zsh
setopt err_exit no_unset
ROOT="${0:A:h}"
# shellcheck disable=SC1091
source "$ROOT/lib/host.sh"
# Host + survey live on disk. Client is never asked to identify the box.
if [[ ! -f .emperor/host.env ]]; then
  bash "$ROOT/boot.sh" >/dev/null 2>&1 || true
fi
TOOL="${1:-}"
if [[ -z "$TOOL" ]]; then
  print -u2 "usage: $0 <done|gate|eval|review-pack|dowse|install|worktree|queue|forge|finish|activate|boot|identify|route|heal|grill|tdd|iso|review|author|evidence|receive|execute|subagent|excavate> [args]"
  exit 2
fi
shift || true
if [[ "$TOOL" == host || "$TOOL" == boot ]]; then
  bash "$ROOT/boot.sh" >/dev/null 2>&1 || true
  [[ "${EMPEROR_BOOT_VERBOSE:-0}" == 1 ]] && cat .emperor/host.env 2>/dev/null || true
  exit 0
fi
# identify: with a path → survey that tree (archaeology). No args → silent
# (boot already wrote .emperor/survey.md). Not a user ritual.
# excavate: first-class alias — always runs the identify survey (path or .).
if [[ "$TOOL" == identify ]]; then
  if [[ $# -gt 0 ]]; then
    exec bash "$ROOT/identify.sh" "$@"
  fi
  bash "$ROOT/boot.sh" >/dev/null 2>&1 || true
  if [[ "${EMPEROR_BOOT_VERBOSE:-0}" == 1 ]]; then
    cat .emperor/survey.md 2>/dev/null || true
  fi
  exit 0
fi
if [[ "$TOOL" == excavate ]]; then
  exec bash "$ROOT/excavate.sh" "$@"
fi

ps1="$ROOT/${TOOL}.ps1"
sh="$ROOT/${TOOL}.sh"

if [[ "$EMPEROR_WSL" -eq 1 && "${EMPEROR_FORCE_WIN:-0}" -eq 1 && -f "$ps1" ]]; then
  _ps=$(emperor_win_ps) || { print -u2 "emperor.zsh: WSL but no Windows PowerShell interop"; exit 127; }
  _winroot=$(emperor_to_win "$ROOT")
  exec "$_ps" -NoProfile -File "${_winroot}\\${TOOL}.ps1" "$@"
fi

win=0
case "$EMPEROR_OS" in gitbash|cygwin) win=1 ;; esac

if [[ "$win" -eq 1 ]]; then
  if command -v pwsh >/dev/null 2>&1 && [[ -f "$ps1" ]]; then
    exec pwsh -NoProfile -File "$ps1" "$@"
  elif command -v powershell >/dev/null 2>&1 && [[ -f "$ps1" ]]; then
    exec powershell -NoProfile -File "$ps1" "$@"
  elif [[ -f "$sh" ]]; then
    exec bash "$sh" "$@"
  fi
else
  if [[ -f "$sh" ]]; then
    exec bash "$sh" "$@"
  elif command -v pwsh >/dev/null 2>&1 && [[ -f "$ps1" ]]; then
    exec pwsh -NoProfile -File "$ps1" "$@"
  fi
fi
print -u2 "emperor.zsh: no runtime for $TOOL on this host"
exit 127
