# shellcheck shell=bash
# Emperor Time host detect. Source from bash OR zsh (not zsh-only).
# Sets: EMPEROR_OS EMPEROR_SHELL EMPEROR_WSL EMPEROR_WIN_INTEROP
#       EMPEROR_ENCODING EMPEROR_WIN_ROOT EMPEROR_MNT
# Helpers: emperor_to_win <posix>  emperor_to_posix <win>  emperor_win_ps  emperor_win_cmd

# Encoding: honor the host, default UTF-8. Do not force a locale the box lacks.
if [ -z "${EMPEROR_ENCODING:-}" ]; then
  if [ -n "${LC_ALL:-}" ]; then EMPEROR_ENCODING="$LC_ALL"
  elif [ -n "${LANG:-}" ]; then EMPEROR_ENCODING="$LANG"
  else EMPEROR_ENCODING="C.UTF-8"
  fi
fi
case "$EMPEROR_ENCODING" in
  *UTF-8*|*utf8*|*utf-8*) : ;;
  C|POSIX|"") EMPEROR_ENCODING="C.UTF-8" ;;
esac
export EMPEROR_ENCODING
if [ -z "${LC_ALL:-}" ] && [ -z "${LANG:-}" ]; then
  export LANG="$EMPEROR_ENCODING" LC_ALL="$EMPEROR_ENCODING"
fi

EMPEROR_OS=unknown
_uname="$(uname -s 2>/dev/null || echo unknown)"
case "$_uname" in
  Darwin) EMPEROR_OS=macos ;;
  Linux) EMPEROR_OS=linux ;;
  MINGW*|MSYS*) EMPEROR_OS=gitbash ;;
  CYGWIN*) EMPEROR_OS=cygwin ;;
  *) EMPEROR_OS=$(printf '%s' "$_uname" | tr '[:upper:]' '[:lower:]') ;;
esac
[ "${OS:-}" = "Windows_NT" ] && EMPEROR_OS=gitbash

EMPEROR_WSL=0
EMPEROR_WIN_INTEROP=0
EMPEROR_MNT=""
EMPEROR_WIN_ROOT=""
if [ -n "${WSL_DISTRO_NAME:-}" ] || [ -n "${WSL_INTEROP:-}" ]; then
  EMPEROR_WSL=1
  EMPEROR_OS=wsl
elif [ -r /proc/version ] && grep -qiE 'microsoft|wsl' /proc/version 2>/dev/null; then
  EMPEROR_WSL=1
  EMPEROR_OS=wsl
fi

if [ "$EMPEROR_WSL" -eq 1 ]; then
  if [ -d /mnt/c ]; then EMPEROR_MNT=/mnt; EMPEROR_WIN_ROOT=/mnt/c
  elif [ -d /mnt/wslg ]; then EMPEROR_MNT=/mnt
  fi
  if command -v cmd.exe >/dev/null 2>&1 || command -v powershell.exe >/dev/null 2>&1 || command -v pwsh.exe >/dev/null 2>&1; then
    EMPEROR_WIN_INTEROP=1
  fi
fi

if [ -n "${ZSH_VERSION:-}" ]; then EMPEROR_SHELL="zsh"
elif [ -n "${BASH_VERSION:-}" ]; then EMPEROR_SHELL="bash"
else EMPEROR_SHELL="sh"
fi
export EMPEROR_OS EMPEROR_SHELL EMPEROR_WSL EMPEROR_WIN_INTEROP EMPEROR_MNT EMPEROR_WIN_ROOT

emperor_to_win() {
  if command -v wslpath >/dev/null 2>&1; then wslpath -w "$1"; return; fi
  printf '%s\n' "$1"
}
emperor_to_posix() {
  if command -v wslpath >/dev/null 2>&1; then wslpath -u "$1"; return; fi
  printf '%s\n' "$1"
}
emperor_win_ps() {
  if command -v pwsh.exe >/dev/null 2>&1; then printf '%s\n' pwsh.exe; return; fi
  if command -v powershell.exe >/dev/null 2>&1; then printf '%s\n' powershell.exe; return; fi
  return 1
}
emperor_win_cmd() {
  if command -v cmd.exe >/dev/null 2>&1; then printf '%s\n' cmd.exe; return; fi
  return 1
}
emperor_host_report() {
  # Canonical report line lives in host.py (closes bash↔ps1 drift).
  # Resolve path without zsh-only expansions (file is shellcheck shell=bash).
  _et_host_py=""
  if [ -n "${BASH_SOURCE[0]:-}" ] && [ -f "${BASH_SOURCE[0]}" ]; then
    _et_host_py="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/host.py"
  fi
  if [ -z "$_et_host_py" ] || [ ! -f "$_et_host_py" ]; then
    for _cand in \
      "./scripts/lib/host.py" \
      "$(dirname "$0")/lib/host.py" \
      "$(dirname "$0")/host.py"
    do
      if [ -f "$_cand" ]; then
        _et_host_py="$(cd "$(dirname "$_cand")" && pwd)/host.py"
        break
      fi
    done
  fi
  if [ -n "$_et_host_py" ] && [ -f "$_et_host_py" ] && command -v python3 >/dev/null 2>&1; then
    python3 "$_et_host_py" --report
    return
  fi
  printf 'os=%s shell=%s wsl=%s win_interop=%s encoding=%s mnt=%s win_root=%s\n' \
    "$EMPEROR_OS" "$EMPEROR_SHELL" "$EMPEROR_WSL" "$EMPEROR_WIN_INTEROP" \
    "$EMPEROR_ENCODING" "${EMPEROR_MNT:-}" "${EMPEROR_WIN_ROOT:-}"
}
