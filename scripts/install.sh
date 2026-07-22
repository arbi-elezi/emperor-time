#!/usr/bin/env bash
# Deploy Emperor Time into a harness's skill directory.
#
# Usage: ./install.sh <harness> [scope] [project-path] [--with-chain-skills] [--dry-run]
#   harness: claude-code | kimi | codex | opencode | generic-agents
#   scope:   user (default) | project
#
# Examples:
#   ./install.sh claude-code user
#   ./install.sh claude-code project ~/repos/myapp
#   ./install.sh generic-agents user --with-chain-skills

set -eu

HARNESS="${1:?usage: install.sh <harness> [scope] [project-path] [flags]}"
SCOPE="${2:-user}"
PROJECT="${3:-.}"
WITH_CHAINS=0
DRY_RUN=0
for arg in "$@"; do
  case "$arg" in
    --with-chain-skills) WITH_CHAINS=1 ;;
    --dry-run)           DRY_RUN=1 ;;
  esac
done
case "$SCOPE" in --*) SCOPE=user ;; esac
case "$PROJECT" in --*) PROJECT=. ;; esac

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

case "$HARNESS" in
  claude-code)    USER_DIR="$HOME/.claude/skills";        PROJ_DIR=".claude/skills" ;;
  kimi)           USER_DIR="$HOME/.kimi/skills";          PROJ_DIR=".kimi/skills" ;;
  codex)          USER_DIR="$HOME/.codex/skills";         PROJ_DIR=".codex/skills" ;;
  opencode)       USER_DIR="$HOME/.opencode/skills";      PROJ_DIR="" ;;
  generic-agents) USER_DIR="$HOME/.config/agents/skills"; PROJ_DIR=".agents/skills" ;;
  *) echo "unknown harness: $HARNESS" >&2; exit 2 ;;
esac

if [ "$SCOPE" = "project" ]; then
  if [ -z "$PROJ_DIR" ]; then
    echo "harness '$HARNESS' has no documented project-level skills dir - use scope 'user'" >&2
    exit 2
  fi
  DEST_ROOT="$(cd "$PROJECT" && pwd)/$PROJ_DIR"
else
  DEST_ROOT="$USER_DIR"
fi
DEST="$DEST_ROOT/emperor-time"

echo
echo '=== EMPEROR TIME :: install ==='
echo "  source : $REPO_ROOT"
echo "  target : $DEST"
if [ "$HARNESS" = "claude-code" ] && [ "$SCOPE" = "user" ]; then
  echo '  note   : Kimi CLI reads ~/.claude/skills/ too - this install covers both.'
fi
if [ "$DRY_RUN" -eq 1 ]; then
  echo '  (dry run - nothing copied)'
  exit 0
fi

mkdir -p "$DEST"
for item in SKILL.md README.md chains references templates adapters scripts; do
  if [ -e "$REPO_ROOT/$item" ]; then
    cp -R "$REPO_ROOT/$item" "$DEST/"
  fi
done

if [ "$WITH_CHAINS" -eq 1 ]; then
  for c in dowsing-chain chain-jail judgment-chain steal-chain holy-chain; do
    if [ -d "$REPO_ROOT/chains/$c" ]; then
      cp -R "$REPO_ROOT/chains/$c" "$DEST_ROOT/$c"
      echo "  chain  : $DEST_ROOT/$c"
    fi
  done
fi

echo
echo 'Installed.'
case "$HARNESS" in
  claude-code)    echo 'Activate: say "emperor time" in Claude Code (or let the description auto-trigger).' ;;
  kimi)           echo 'Activate: /skill:emperor-time inside a kimi session.' ;;
  codex)          echo 'Activate: per Codex skill activation - verify with `codex --help`.' ;;
  opencode)       echo 'Activate: opencode run --skill emperor-time (verify flag; see adapters/opencode/).' ;;
  generic-agents) echo 'Activate: any Agent-Skills-compatible harness reading ~/.config/agents/skills/.' ;;
esac
echo 'First run: execute scripts/dowse.sh to build the agent roster.'
