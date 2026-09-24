#!/usr/bin/env bash
# Emit an isolated review pack: SHAs + diff + criteria. No author CoT.
set -euo pipefail

TASK="${1:-}"
BASE="${2:-HEAD~1}"
HEAD="${3:-HEAD}"
[[ -n "$TASK" ]] || { echo "usage: $0 <task-dir> [base] [head]" >&2; exit 2; }
[[ -d "$TASK" ]] || { echo "missing $TASK" >&2; exit 1; }

OUT="$TASK/review-pack"
mkdir -p "$OUT"

{
  echo "# Isolated review pack"
  echo "- task: $TASK"
  echo "- generated: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo "- base: $(git rev-parse "$BASE")"
    echo "- head: $(git rev-parse "$HEAD")"
  else
    echo "- base/head: not a git repo"
  fi
} > "$OUT/meta.md"

if [[ -f "$TASK/work-order.md" ]]; then
  awk '/^## Acceptance criteria/,/^## /{if(/^## / && !/^## Acceptance/){exit} print}' \
    "$TASK/work-order.md" > "$OUT/criteria.md" || cp "$TASK/work-order.md" "$OUT/criteria.md"
fi

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git diff "$BASE".."$HEAD" > "$OUT/diff.patch" || true
  git diff --stat "$BASE".."$HEAD" > "$OUT/diffstat.txt" || true
fi

[[ -f "$TASK/claims.md" ]] && cp "$TASK/claims.md" "$OUT/claims.md" || true

echo "REVIEW PACK: $OUT"
ls -la "$OUT"
