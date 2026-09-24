#!/usr/bin/env bash
# Structural evals for Emperor Time. Does not spawn a model.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
fail=0

need() {
  local f="$1"
  if [[ ! -e "$ROOT/$f" ]]; then
    echo "EVAL FAIL: missing $f"
    fail=1
  fi
}

echo "== presence =="
for f in \
  SKILL.md \
  chains/dowsing-chain/SKILL.md \
  chains/chain-jail/SKILL.md \
  chains/judgment-chain/SKILL.md \
  chains/steal-chain/SKILL.md \
  chains/holy-chain/SKILL.md \
  templates/work-order.md \
  templates/review-pack.md \
  templates/task-ledger.md \
  templates/claim-ledger.md \
  templates/critique.md \
  references/scientific-method.md \
  references/micro-waterfall.md \
  references/work-order.md \
  references/mechanical-gates.md \
  scripts/gate.sh \
  scripts/review-pack.sh \
  evals/evals.json \
  evals/triggers.json \
  skills/emperor-scope/SKILL.md \
  skills/emperor-require-design/SKILL.md \
  skills/emperor-build/SKILL.md \
  skills/emperor-verify/SKILL.md \
  skills/emperor-dispatch/SKILL.md \
  skills/emperor-heal/SKILL.md \
  skills/emperor-capture/SKILL.md
do
  need "$f"
done

echo "== vows + five chains still named in master skill =="
grep -q "Vow of Evidence" "$ROOT/SKILL.md" || { echo "EVAL FAIL: vows missing"; fail=1; }
for c in "Dowsing Chain" "Chain Jail" "Judgment Chain" "Steal Chain" "Holy Chain"; do
  grep -q "$c" "$ROOT/SKILL.md" || { echo "EVAL FAIL: $c unnamed in SKILL.md"; fail=1; }
done

echo "== gate script syntax =="
bash -n "$ROOT/scripts/gate.sh" || { echo "EVAL FAIL: gate.sh syntax"; fail=1; }
bash -n "$ROOT/scripts/review-pack.sh" || { echo "EVAL FAIL: review-pack.sh syntax"; fail=1; }

echo "== fixture: unquoted VERIFIED must fail g4 =="
TMP="$(mktemp -d)"
mkdir -p "$TMP/.gates"
date -u +"%Y-%m-%dT%H:%M:%SZ" > "$TMP/.gates/g0"
date -u +"%Y-%m-%dT%H:%M:%SZ" > "$TMP/.gates/g1"
date -u +"%Y-%m-%dT%H:%M:%SZ" > "$TMP/.gates/g2"
date -u +"%Y-%m-%dT%H:%M:%SZ" > "$TMP/.gates/g3"
cat > "$TMP/ledger.md" <<'EOF'
# Task Ledger
## G0
## G1 Acceptance criteria
## G2
## G3
## G4
- Verdict:
EOF
cat > "$TMP/claims.md" <<'EOF'
| # | Claim | Status | Prediction | Experiment | Evidence | Date |
| 1 | tests pass | VERIFIED | pass | pytest | tests pass | 2026-01-01 |
EOF
cat > "$TMP/critique.md" <<'EOF'
self-critique filed
EOF
if bash "$ROOT/scripts/gate.sh" g4 "$TMP"; then
  echo "EVAL FAIL: unquoted VERIFIED was allowed"
  fail=1
else
  echo "EVAL PASS: unquoted VERIFIED rejected"
fi
rm -rf "$TMP"

echo "== trigger file present =="
grep -q "emperor time" "$ROOT/evals/triggers.json" || { echo "EVAL FAIL: triggers"; fail=1; }

if [[ "$fail" -ne 0 ]]; then
  echo "EVALS FAILED"
  exit 1
fi
echo "EVALS PASSED"
