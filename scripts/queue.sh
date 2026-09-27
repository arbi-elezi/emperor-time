#!/usr/bin/env bash
# Local / GitHub / Linear work picker. Read-only unless EMPEROR_CONSENT_TRACKER=1.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CMD="${1:-next}"
QUEUE="${EMPEROR_QUEUE_FILE:-$ROOT/.emperor/queue.md}"
mkdir -p "$(dirname "$QUEUE")"
[[ -f "$QUEUE" ]] || printf '# Emperor queue\n\n- [ ] (empty — add a line or connect gh/Linear)\n' > "$QUEUE"

list_local() {
  grep -E '^- \[ \]' "$QUEUE" 2>/dev/null || true
}

case "$CMD" in
  list)
    echo "== local $QUEUE =="
    list_local || true
    if command -v gh >/dev/null 2>&1 && git -C "$ROOT" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
      echo "== gh issues (open, limit 10) =="
      gh issue list --state open --limit 10 2>/dev/null || echo "gh issue list failed (auth or no remote)"
    fi
    if [[ -n "${LINEAR_API_KEY:-}" ]]; then
      echo "== Linear key present (not listing unless EMPEROR_QUEUE_SOURCE=linear) =="
    fi
    ;;
  next)
    src="${EMPEROR_QUEUE_SOURCE:-auto}"
    if [[ "$src" == gh || "$src" == auto ]] && command -v gh >/dev/null 2>&1; then
      item=$(gh issue list --state open --limit 1 --json number,title --jq '.[] | "#\(.number) \(.title)"' 2>/dev/null || true)
      if [[ -n "${item:-}" ]]; then
        echo "NEXT gh: $item"
        exit 0
      fi
    fi
    if [[ "$src" == linear || ( "$src" == auto && -n "${LINEAR_API_KEY:-}" ) ]]; then
      echo "NEXT linear: key present — agent must query Linear with client consent; script will not ship tokens."
      exit 0
    fi
    item=$(list_local | head -n1 || true)
    if [[ -n "${item:-}" && "$item" != *'(empty'* ]]; then
      echo "NEXT local: $item"
      exit 0
    fi
    echo "NEXT none: queue empty. Add a line to $QUEUE or pass a task."
    exit 2
    ;;
  add)
    shift || true
    [[ -n "${1:-}" ]] || { echo "usage: queue.sh add <text>" >&2; exit 2; }
    printf -- '- [ ] %s\n' "$*" >> "$QUEUE"
    echo "QUEUED: $*"
    ;;
  done)
    shift || true
    pat="${1:-}"
    [[ -n "$pat" ]] || { echo "usage: queue.sh done <substring>" >&2; exit 2; }
    tmp=$(mktemp)
    awk -v p="$pat" 'BEGIN{done=0} /- \[ \]/ && index($0,p) && !done {$0=gensub(/- \[ \]/,"- [x]",1); done=1} {print}' "$QUEUE" > "$tmp"
    mv "$tmp" "$QUEUE"
    echo "CHECKED: $pat"
    ;;
  *)
    echo "usage: $0 list|next|add|done" >&2
    exit 2
    ;;
esac
