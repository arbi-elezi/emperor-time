#!/usr/bin/env bash
# Open a PR only with consent. Refuses if done probes fail.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TASK="${1:-}"
[[ -n "$TASK" && -d "$TASK" ]] || { echo "usage: $0 <task-dir>" >&2; exit 2; }
CONSENT="${EMPEROR_CONSENT_PR:-0}"
if grep -qiE 'consent.*pr|open a pr|yes.*pr' "$TASK/ledger.md" 2>/dev/null; then
  CONSENT=1
fi
if [[ "$CONSENT" != 1 ]]; then
  echo "FORGE REFUSED: no EMPEROR_CONSENT_PR=1 and no quoted PR consent in ledger.md" >&2
  exit 3
fi
bash "$ROOT/scripts/done.sh" "$TASK"
TITLE=$(grep -m1 -E '^# |Task:' "$TASK/ledger.md" 2>/dev/null | head -n1 | sed 's/^# //;s/^.*Task: //')
TITLE=${TITLE:-emperor-time change}
BODY="$TASK/PR.md"
{
  echo "## G1"
  sed -n '/G1/,/G2/p' "$TASK/ledger.md" 2>/dev/null || true
  echo
  echo "## DONE probes"
  cat "$TASK/DONE.md" 2>/dev/null || true
} > "$BODY"
if ! command -v gh >/dev/null 2>&1; then
  echo "FORGE DRY: gh not installed. Client runs:"
  echo "  gh pr create --title $(printf %q "$TITLE") --body-file $(printf %q "$BODY")"
  exit 0
fi
gh pr create --title "$TITLE" --body-file "$BODY"
