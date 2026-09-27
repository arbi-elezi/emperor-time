# Emperor Time - bash convenience layer (Linux / macOS bash / Git Bash on Windows).
#
# Install (~/.bashrc):
#   source /path/to/emperor-time/scripts/emperor-time.bash
#
# Set EMPEROR_TIME_HOME to override where the repo/skill lives.

if [ -z "${EMPEROR_TIME_HOME:-}" ]; then
  _et_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
  if [ -n "$_et_dir" ] && [ -f "$_et_dir/../SKILL.md" ]; then
    EMPEROR_TIME_HOME="$(cd "$_et_dir/.." && pwd)"
  else
    for _et_c in \
      "$HOME/.claude/skills/emperor-time" \
      "$HOME/.config/agents/skills/emperor-time" \
      "$HOME/.agents/skills/emperor-time" \
      "$HOME/.kimi/skills/emperor-time" \
      "$HOME/.codex/skills/emperor-time" \
      "$HOME/.opencode/skills/emperor-time"; do
      if [ -f "$_et_c/SKILL.md" ]; then
        EMPEROR_TIME_HOME="$_et_c"
        break
      fi
    done
    unset _et_c
  fi
  unset _et_dir
  export EMPEROR_TIME_HOME
fi

emperor() {
  if [ -z "${EMPEROR_TIME_HOME:-}" ] || [ ! -f "$EMPEROR_TIME_HOME/SKILL.md" ]; then
    echo "emperor: skill not found - set EMPEROR_TIME_HOME to the emperor-time directory" >&2
    return 1
  fi
  local cmd="${1:-help}"
  if [ "$#" -gt 0 ]; then shift; fi
  case "$cmd" in
    dowse)   bash "$EMPEROR_TIME_HOME/scripts/dowse.sh" "$@" ;;
    install) bash "$EMPEROR_TIME_HOME/scripts/install.sh" "$@" ;;
    core)    cat "$EMPEROR_TIME_HOME/adapters/generic/EMPEROR_TIME.core.md" ;;
    skill)   cat "$EMPEROR_TIME_HOME/SKILL.md" ;;
    home)    echo "$EMPEROR_TIME_HOME" ;;
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

complete -W "dowse install core skill home help" emperor 2>/dev/null || true
