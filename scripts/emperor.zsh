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
  print -u2 "usage: $0 <done|gate|eval|review-pack|dowse|install|worktree|queue|forge|finish|activate|boot|identify|route|heal|grill|tdd|iso|review|author|evidence|receive|execute|subagent|parallel|excavate|session-discovery|diagnose|trace|defense|wait|polluter|pressure|good-tests|skill-test|persuasion|sdo|brief|task-brief|task-start|task-done|sdd-workspace|sdd-review-pack|work-order|claim-audit|judgment-audit|quarantine|steal-quarantine|consent|steal-consent|heal-verify|heal-and-verify|reproduce|reproduce-and-bisect|triage|holy-triage|process-heal|process-healing|steal-flow|sign-in-handoff|steal-dispatch|swarm-emulate|pin-and-consent|jail-pin|critique|self-critique|verdict|breach|context|thoughttrail|super-context|sandbox|sot|runtime|env|secrets> [args]"
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
# wait: first-class alias → condition-wait HARD-GATE card
if [[ "$TOOL" == wait ]]; then
  exec bash "$ROOT/condition-wait.sh" "$@"
fi
# polluter: first-class alias → find-polluter HARD-GATE card
if [[ "$TOOL" == polluter ]]; then
  exec bash "$ROOT/find-polluter.sh" "$@"
fi
# brief: first-class alias → task-brief (SDD lifecycle)
if [[ "$TOOL" == brief ]]; then
  exec bash "$ROOT/task-brief.sh" "$@"
fi
# judgment-audit: first-class alias → claim-audit HARD-GATE
if [[ "$TOOL" == judgment-audit ]]; then
  exec bash "$ROOT/claim-audit.sh" "$@"
fi
# steal-quarantine: first-class alias → quarantine HARD-GATE
if [[ "$TOOL" == steal-quarantine ]]; then
  exec bash "$ROOT/quarantine.sh" "$@"
fi
# steal-consent: first-class alias → consent HARD-GATE
if [[ "$TOOL" == steal-consent ]]; then
  exec bash "$ROOT/consent.sh" "$@"
fi
# heal-and-verify: first-class alias → heal-verify HARD-GATE
if [[ "$TOOL" == heal-and-verify ]]; then
  exec bash "$ROOT/heal-verify.sh" "$@"
fi
# reproduce-and-bisect: first-class alias → reproduce HARD-GATE
if [[ "$TOOL" == reproduce-and-bisect ]]; then
  exec bash "$ROOT/reproduce.sh" "$@"
fi
# holy-triage: first-class alias → triage HARD-GATE
if [[ "$TOOL" == holy-triage ]]; then
  exec bash "$ROOT/triage.sh" "$@"
fi
# process-healing: first-class alias → process-heal HARD-GATE
if [[ "$TOOL" == process-healing ]]; then
  exec bash "$ROOT/process-heal.sh" "$@"
fi
# sign-in-handoff / steal-dispatch / swarm-emulate → steal-flow HARD-GATE
if [[ "$TOOL" == sign-in-handoff || "$TOOL" == steal-dispatch || "$TOOL" == swarm-emulate ]]; then
  exec bash "$ROOT/steal-flow.sh" "$@"
fi
# jail-pin → pin-and-consent HARD-GATE
if [[ "$TOOL" == jail-pin ]]; then
  exec bash "$ROOT/pin-and-consent.sh" "$@"
fi
# self-critique: first-class alias → critique eight-count HARD-GATE
if [[ "$TOOL" == self-critique ]]; then
  exec bash "$ROOT/critique.sh" "$@"
fi
# breach: first-class alias → verdict + Breach Register HARD-GATE
if [[ "$TOOL" == breach ]]; then
  exec bash "$ROOT/verdict.sh" "$@"
fi
# pressure: first-class alias → pressure/academic HARD-GATE card
if [[ "$TOOL" == pressure ]]; then
  exec bash "$ROOT/pressure.sh" "$@"
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
