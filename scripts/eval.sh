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
  chains/steal-chain/ci-mode.md \
  chains/steal-chain/swarm-emulate.md \
  chains/holy-chain/SKILL.md \
  templates/work-order.md \
  scripts/gate.sh scripts/gate.ps1 \
  scripts/done.sh scripts/done.ps1 \
  scripts/eval.sh scripts/eval.ps1 \
  scripts/emperor scripts/emperor.ps1 scripts/emperor.cmd scripts/emperor.zsh \
  skills/emperor-scope/SKILL.md \
  evals/evals.json \
  evals/triggers.json
do
  need "$f"
done

echo "== vows + five chains still named in master skill =="
grep -q "Vow of Evidence" "$ROOT/SKILL.md" || { echo "EVAL FAIL: vows missing"; fail=1; }
for c in "Dowsing Chain" "Chain Jail" "Judgment Chain" "Steal Chain" "Holy Chain"; do
  grep -q "$c" "$ROOT/SKILL.md" || { echo "EVAL FAIL: $c unnamed in SKILL.md"; fail=1; }
done

echo "== twins =="
for pair in done gate eval review-pack dowse install worktree; do
  need "scripts/${pair}.sh"
  need "scripts/${pair}.ps1"
done

echo "== steal router lists ci + swarm =="
grep -q "ci-mode.md" "$ROOT/chains/steal-chain/SKILL.md" || { echo "EVAL FAIL: steal router missing ci-mode.md"; fail=1; }
grep -q "swarm-emulate.md" "$ROOT/chains/steal-chain/SKILL.md" || { echo "EVAL FAIL: steal router missing swarm-emulate.md"; fail=1; }

echo "== hooks treat cmd as a peer =="
grep -q "emperor.cmd" "$ROOT/hooks/hooks.json" || { echo "EVAL FAIL: hooks do not mention emperor.cmd"; fail=1; }
if grep -q "No cmd.exe shim" "$ROOT/hooks/hooks.json"; then
  echo "EVAL FAIL: hooks still say No cmd.exe shim"
  fail=1
fi

echo "== gate script syntax =="
bash -n "$ROOT/scripts/gate.sh" || { echo "EVAL FAIL: gate.sh syntax"; fail=1; }
bash -n "$ROOT/scripts/emperor" || { echo "EVAL FAIL: emperor syntax"; fail=1; }

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
