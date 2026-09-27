#!/usr/bin/env bash
# Agent-defined DONE. Exit 0 only if every probe in DONE.md matches.
set -euo pipefail
DIR="${1:-}"
[[ -n "$DIR" && -d "$DIR" ]] || { echo "usage: $0 <task-dir>" >&2; exit 2; }
DONE="$DIR/DONE.md"
[[ -f "$DONE" ]] || { echo "DONE FAIL: no $DONE (agent must define DONE)" >&2; exit 1; }
grep -q '^probe:' "$DONE" || { echo "DONE FAIL: no probes in DONE.md" >&2; exit 1; }
fail=0
cmd=""
expect=""
flush() {
  [[ -z "$cmd" ]] && return 0
  out="$(bash -lc "$cmd" 2>&1 || true)"
  if grep -Fq -- "$expect" <<<"$out"; then
    echo "DONE PASS: $cmd"
  else
    echo "DONE FAIL: $cmd"
    echo "  expected substring: $expect"
    echo "  got tail: $(echo "$out" | tail -n 8)"
    fail=1
  fi
}
while IFS= read -r line || [[ -n "$line" ]]; do
  case "$line" in
    probe:*)
      flush
      cmd="${line#probe:}"
      cmd="${cmd# }"
      expect=""
      ;;
    expect:*)
      expect="${line#expect:}"
      expect="${expect# }"
      ;;
  esac
done < "$DONE"
flush
[[ "$fail" -eq 0 ]] || exit 1
echo "DONE OK"
