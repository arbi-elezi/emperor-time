#!/usr/bin/env zsh
# zsh peer of scripts/emperor (bash). Same tools. Host encoding + WSL interop.
emulate -L zsh
setopt err_exit no_unset
ROOT="${0:A:h}"
# shellcheck disable=SC1091
source "$ROOT/lib/host.sh"
TOOL="${1:-}"
shift || true
if [[ -z "$TOOL" ]]; then
  print -u2 "usage: $0 <done|gate|eval|review-pack|dowse|install|worktree|host> [args]"
  exit 2
fi
if [[ "$TOOL" == host ]]; then emperor_host_report; exit 0; fi

ps1="$ROOT/${TOOL}.ps1"
sh="$ROOT/${TOOL}.sh"

if [[ "$EMPEROR_WSL" -eq 1 && "${EMPEROR_FORCE_WIN:-0}" -eq 1 && -f "$ps1" ]]; then
  _ps=$(emperor_win_ps) || { print -u2 "emperor.zsh: WSL but no Windows PowerShell interop"; exit 127; }
  _winroot=$(emperor_to_win "$ROOT")
  exec "$_ps" -NoProfile -File "${_winroot}\\${TOOL}.ps1" "$@"
fi

if [[ -f "$sh" ]]; then
  exec bash "$sh" "$@"
elif [[ -f "$ps1" ]]; then
  if command -v pwsh >/dev/null; then exec pwsh -NoProfile -File "$ps1" "$@"; fi
fi
print -u2 "emperor.zsh: no runtime for $TOOL"
exit 127
