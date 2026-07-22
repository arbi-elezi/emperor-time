# Emperor Time - zsh convenience layer (macOS default shell; oh-my-zsh compatible).
#
# Install, pick one:
#   plain zsh  (~/.zshrc):
#     source /path/to/emperor-time/scripts/emperor-time.plugin.zsh
#   oh-my-zsh:
#     ln -s /path/to/emperor-time/scripts \
#           ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/emperor-time
#     then add emperor-time to plugins=(...) in ~/.zshrc
#
# Set EMPEROR_TIME_HOME to override where the repo/skill lives.

# Resolve the repo root. This file lives in <repo>/scripts/; ${0:A} follows
# symlinks, so the oh-my-zsh symlink install resolves correctly too.
if [[ -z "${EMPEROR_TIME_HOME:-}" ]]; then
  typeset _et_dir="${0:A:h}"
  if [[ -f "${_et_dir:h}/SKILL.md" ]]; then
    export EMPEROR_TIME_HOME="${_et_dir:h}"
  else
    typeset _et_c
    for _et_c in \
      "$HOME/.claude/skills/emperor-time" \
      "$HOME/.config/agents/skills/emperor-time" \
      "$HOME/.agents/skills/emperor-time" \
      "$HOME/.kimi/skills/emperor-time" \
      "$HOME/.codex/skills/emperor-time" \
      "$HOME/.opencode/skills/emperor-time"; do
      if [[ -f "$_et_c/SKILL.md" ]]; then
        export EMPEROR_TIME_HOME="$_et_c"
        break
      fi
    done
    unset _et_c
  fi
  unset _et_dir
fi

emperor() {
  emulate -L zsh
  if [[ -z "${EMPEROR_TIME_HOME:-}" || ! -f "$EMPEROR_TIME_HOME/SKILL.md" ]]; then
    print -u2 "emperor: skill not found - set EMPEROR_TIME_HOME to the emperor-time directory"
    return 1
  fi
  local cmd="${1:-help}"
  (( $# > 0 )) && shift
  case "$cmd" in
    dowse)   bash "$EMPEROR_TIME_HOME/scripts/dowse.sh" "$@" ;;
    install) bash "$EMPEROR_TIME_HOME/scripts/install.sh" "$@" ;;
    core)    cat "$EMPEROR_TIME_HOME/adapters/generic/EMPEROR_TIME.core.md" ;;
    skill)   cat "$EMPEROR_TIME_HOME/SKILL.md" ;;
    home)    print -r -- "$EMPEROR_TIME_HOME" ;;
    *)       cat <<'EOF'
emperor - Emperor Time shell layer
  emperor dowse [--check-auth]          scan this machine for enlistable agents (read-only)
  emperor install <harness> [scope]     deploy the skill: claude-code|kimi|codex|opencode|generic-agents
  emperor core                          print the distilled system prompt (pipe to pbcopy / xclip)
  emperor skill                         print the master SKILL.md
  emperor home                          print the resolved skill path
EOF
    ;;
  esac
}

# Completion (only if compinit has run)
if (( ${+functions[compdef]} )); then
  _emperor() { _arguments '1:command:(dowse install core skill home help)' }
  compdef _emperor emperor
fi
