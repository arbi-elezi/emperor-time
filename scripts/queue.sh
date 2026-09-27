#!/usr/bin/env bash
# Local / GitHub / Linear work picker. Read-only unless EMPEROR_CONSENT_TRACKER=1.
# Kanban statuses (WIP=1): [ ] ready · [~] active · [x] done · [!] blocked
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CMD="${1:-next}"
QUEUE="${EMPEROR_QUEUE_FILE:-$ROOT/.emperor/queue.md}"
mkdir -p "$(dirname "$QUEUE")"
[[ -f "$QUEUE" ]] || printf '%s\n' \
  '# Emperor queue' \
  '# WIP=1 — one [~] active at a time. Statuses: [ ] ready · [~] active · [x] done · [!] blocked' \
  '#' \
  '# Empty — add: - [ ] <task>  (or connect gh/Linear). Placeholder/parentheses-empty lines are ignored.' \
  '' \
  'Local backlog when GitHub issues / Linear are not connected.' \
  > "$QUEUE"

# True when a checkbox line is an empty-queue placeholder, not real work.
# Matches: "(empty…)", bare "- [ ]", or parentheses-only titles like "- [ ] (…)" .
is_placeholder() {
  local line="$1"
  [[ "$line" == *'(empty'* ]] && return 0
  [[ "$line" =~ ^-\ \[[\ ~!]\]\ *$ ]] && return 0
  [[ "$line" =~ ^-\ \[[\ ~!]\]\ +\(.*\)\ *$ ]] && return 0
  return 1
}

# Incomplete local rows: ready, active, blocked (not done). Skips placeholders.
list_open() {
  local line
  while IFS= read -r line || [[ -n "$line" ]]; do
    is_placeholder "$line" && continue
    printf '%s\n' "$line"
  done < <(grep -E '^- \[([ ~!])\]' "$QUEUE" 2>/dev/null || true)
}

list_ready() {
  local line
  while IFS= read -r line || [[ -n "$line" ]]; do
    is_placeholder "$line" && continue
    printf '%s\n' "$line"
  done < <(grep -E '^- \[ \]' "$QUEUE" 2>/dev/null || true)
}

list_active() {
  local line
  while IFS= read -r line || [[ -n "$line" ]]; do
    is_placeholder "$line" && continue
    printf '%s\n' "$line"
  done < <(grep -E '^- \[~\]' "$QUEUE" 2>/dev/null || true)
}

promote_first_ready() {
  # Promote first non-placeholder [ ] → [~]. Prints the new active line on stdout.
  local tmp out
  tmp=$(mktemp)
  out=$(mktemp)
  awk '
    function is_ph(s) {
      if (s ~ /\(empty/) return 1
      if (s ~ /^- \[[ ~!]\] *$/) return 1
      if (s ~ /^- \[[ ~!]\] +\(.*\) *$/) return 1
      return 0
    }
    BEGIN { promoted = 0 }
    /^- \[ \]/ && !is_ph($0) && !promoted {
      sub(/^- \[ \]/, "- [~]")
      promoted = 1
      print > outf
    }
    { print }
  ' outf="$out" "$QUEUE" > "$tmp"
  mv "$tmp" "$QUEUE"
  if [[ -s "$out" ]]; then
    cat "$out"
    rm -f "$out"
    return 0
  fi
  rm -f "$out"
  return 1
}

case "$CMD" in
  list)
    echo "== local $QUEUE =="
    list_open || true
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
    # WIP=1: if an active task exists, return it — refuse a second active.
    active=$(list_active | head -n1 || true)
    if [[ -n "${active:-}" ]]; then
      echo "NEXT local (active): $active"
      echo "WIP=1: refuse second active — finish current or: queue done <substring>"
      exit 0
    fi
    item=$(list_ready | head -n1 || true)
    if [[ -n "${item:-}" ]]; then
      promoted=$(promote_first_ready) || true
      if [[ -n "${promoted:-}" ]]; then
        echo "NEXT local: $promoted"
        exit 0
      fi
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
    awk -v p="$pat" 'BEGIN{done=0} /- \[[ ~!]\]/ && index($0,p) && !done { sub(/- \[[ ~!]\]/, "- [x]"); done=1 } {print}' "$QUEUE" > "$tmp"
    mv "$tmp" "$QUEUE"
    echo "CHECKED: $pat"
    ;;
  *)
    echo "usage: $0 list|next|add|done" >&2
    exit 2
    ;;
esac
