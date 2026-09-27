#!/usr/bin/env bash
# Mechanical gates for Emperor Time. Law is Judgment Chain; this is the lock.
set -euo pipefail

usage() {
  echo "usage: $0 g0|g1|g2|g3|g4|g5 <task-dir>" >&2
  exit 2
}

GATE="${1:-}"
TASK="${2:-}"
[[ -n "$GATE" && -n "$TASK" ]] || usage

fail() { echo "GATE $GATE FAIL: $*" >&2; exit 1; }
ok() { echo "GATE $GATE PASS: $*"; }

LEDGER="$TASK/ledger.md"
ORDER="$TASK/work-order.md"
CLAIMS="$TASK/claims.md"
CRITIQUE="$TASK/critique.md"
STAMP="$TASK/.gates"

[[ -d "$TASK" ]] || fail "missing task dir $TASK"
mkdir -p "$STAMP"

need_ledger() { [[ -f "$LEDGER" ]] || fail "missing $LEDGER"; }

has() {
  grep -qiE "$1" "$2" 2>/dev/null
}

mark() { date -u +"%Y-%m-%dT%H:%M:%SZ" > "$STAMP/$GATE"; }

require_prior() {
  local prior="$1"
  [[ -f "$STAMP/$prior" ]] || fail "prior gate $prior never passed mechanically"
}

case "$GATE" in
  g0)
    need_ledger
    has "G0" "$LEDGER" || fail "ledger has no G0 section"
    has "quoted|Origin|Task:" "$LEDGER" || fail "ledger missing origin/task line"
    mark; ok "$LEDGER"
    ;;
  g1)
    require_prior g0
    need_ledger
    has "Acceptance criteria" "$LEDGER" || fail "no acceptance criteria"
    has "Out of scope" "$LEDGER" || fail "no out-of-scope"
    mark; ok "requirements present"
    ;;
  g2)
    require_prior g1
    need_ledger
    if has "Size:.*trivial" "$LEDGER" || has "Size:.*trivial" "$ORDER" 2>/dev/null; then
      has "G2" "$LEDGER" || fail "trivial task still needs a G2 line"
      mark; ok "trivial G2"
      exit 0
    fi
    [[ -f "$ORDER" ]] || fail "non-trivial task missing work-order.md"
    has "Expected:" "$ORDER" || fail "work-order has no Expected: lines"
    has "Acceptance criteria" "$ORDER" || fail "work-order missing acceptance criteria"
    mark; ok "$ORDER"
    ;;
  g3)
    require_prior g2
    need_ledger
    has "G3" "$LEDGER" || fail "no G3 section"
    if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
      git diff --stat > "$TASK/diffstat.txt" || true
    fi
    mark; ok "build section present"
    ;;
  g4)
    require_prior g3
    need_ledger
    [[ -f "$CRITIQUE" ]] || has "Self-critique" "$LEDGER" || fail "no critique artifact"
    if [[ -f "$CLAIMS" ]]; then
      if grep -E '\|.*\| *CONJECTURE *\|' "$CLAIMS" | grep -vqE 'UNVERIFIABLE|carried|labeled'; then
        echo "GATE G4 WARN: unterminated CONJECTURE rows in $CLAIMS" >&2
      fi
      if grep -E '\|.*\| *VERIFIED *\|' "$CLAIMS" | grep -vqE '\"|`'; then
        fail "VERIFIED row without quoted evidence"
      fi
    fi
    has "Verdict" "$LEDGER" || fail "ledger missing Verdict line"
    mark; ok "verify artifacts present"
    ;;
  g5)
    require_prior g4
    need_ledger
    has "PASS" "$LEDGER" || fail "no PASS / PASS-WITH-CONDITIONS on ledger"
    has "Breach Register" "$LEDGER" || fail "breach register missing (must exist even if empty)"
    mark; ok "deliverable artifacts present"
    ;;
  *)
    usage
    ;;
esac
