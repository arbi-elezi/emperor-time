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
for pair in "done" gate eval review-pack dowse install worktree queue forge finish activate identify boot route excavate; do
  need "scripts/${pair}.sh"
  need "scripts/${pair}.ps1"
done

echo "== silent-boot PS twin uses host.ps1 =="
grep -q 'lib/host.ps1' "$ROOT/scripts/boot.ps1" || { echo "EVAL FAIL: boot.ps1 does not source lib/host.ps1"; fail=1; }
grep -q 'Write-EmperorHostReport' "$ROOT/scripts/lib/host.ps1" || { echo "EVAL FAIL: host.ps1 missing Write-EmperorHostReport"; fail=1; }
grep -q 'host.env' "$ROOT/scripts/emperor.ps1" || { echo "EVAL FAIL: emperor.ps1 missing silent-boot host.env check"; fail=1; }
grep -q 'scripts/emperor boot' "$ROOT/adapters/cursor/README.md" || { echo "EVAL FAIL: cursor adapter missing emperor boot path"; fail=1; }

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

echo "== route mvp =="
if [[ -x "$ROOT/scripts/route.sh" || -f "$ROOT/scripts/route.sh" ]]; then
  bash -n "$ROOT/scripts/route.sh" || { echo "EVAL FAIL: route.sh syntax"; fail=1; }
  out=$(bash "$ROOT/scripts/route.sh" "lost pascal tree" 2>/dev/null || true)
  echo "$out" | grep -q "emperor-excavate" || { echo "EVAL FAIL: route lost pascal → excavate"; fail=1; }
  out=$(bash "$ROOT/scripts/route.sh" "queue next" 2>/dev/null || true)
  echo "$out" | grep -q "emperor-queue" || { echo "EVAL FAIL: route queue next → queue"; fail=1; }
  out=$(bash "$ROOT/scripts/route.sh" "blocked task" 2>/dev/null || true)
  echo "$out" | grep -q "emperor-queue" || { echo "EVAL FAIL: route blocked task → queue"; fail=1; }
  out=$(bash "$ROOT/scripts/route.sh" "red build" 2>/dev/null || true)
  echo "$out" | grep -q "emperor-heal" || { echo "EVAL FAIL: route red build → heal"; fail=1; }
  if bash "$ROOT/scripts/route.sh" "what is 2+2" >/dev/null 2>&1; then
    echo "EVAL FAIL: route should miss trivia"
    fail=1
  else
    echo "EVAL PASS: route misses trivia"
  fi
fi


echo "== queue empty UX =="
bash -n "$ROOT/scripts/queue.sh" || { echo "EVAL FAIL: queue.sh syntax"; fail=1; }
QTMP="$(mktemp)"
cat > "$QTMP" <<'QEOF'
# Emperor queue (eval fixture)
# WIP=1 kept in comments only — no checkbox placeholder.
QEOF
if EMPEROR_QUEUE_SOURCE=local EMPEROR_QUEUE_FILE="$QTMP" bash "$ROOT/scripts/queue.sh" next >/tmp/et-queue-empty.out 2>&1; then
  echo "EVAL FAIL: empty comment-only queue should exit non-zero"
  fail=1
else
  grep -q "NEXT none" /tmp/et-queue-empty.out || { echo "EVAL FAIL: empty queue missing NEXT none"; fail=1; }
fi
cat > "$QTMP" <<'QEOF'
# Emperor queue
- [ ] (empty — replace this line with real work or connect gh)
- [ ] ship the widget
QEOF
out=$(EMPEROR_QUEUE_SOURCE=local EMPEROR_QUEUE_FILE="$QTMP" bash "$ROOT/scripts/queue.sh" next 2>&1) || true
echo "$out" | grep -q "ship the widget" || { echo "EVAL FAIL: queue next should promote real task past placeholder"; fail=1; }
echo "$out" | grep -q "(empty" && { echo "EVAL FAIL: queue next promoted placeholder"; fail=1; }
grep -q '^- \[~\] ship the widget' "$QTMP" || { echo "EVAL FAIL: placeholder queue file not promoted correctly"; fail=1; }
grep -q '^- \[ \] (empty' "$QTMP" || { echo "EVAL FAIL: placeholder line should remain untouched"; fail=1; }
rm -f "$QTMP" /tmp/et-queue-empty.out

echo "== fixture: lost-pas identify finds *.pas =="
need "evals/fixtures/lost-pas/HELLO.PAS"
need "evals/fixtures/lost-pas/README.md"
need "evals/fixtures/lost-pas/PROBE.md"
ID_OUT="$(bash "$ROOT/scripts/identify.sh" "$ROOT/evals/fixtures/lost-pas" 2>&1)" || true
echo "$ID_OUT" | grep -E -q '[0-9]+ \*\.pas' || { echo "EVAL FAIL: identify missed *.pas on lost-pas"; fail=1; }

echo "== fixture: lost-asm identify finds *.asm =="
need "evals/fixtures/lost-asm/FOO.ASM"
need "evals/fixtures/lost-asm/README.md"
need "evals/fixtures/lost-asm/PROBE.md"
ID_OUT="$(bash "$ROOT/scripts/identify.sh" "$ROOT/evals/fixtures/lost-asm" 2>&1)" || true
echo "$ID_OUT" | grep -E -q '[0-9]+ \*\.asm' || { echo "EVAL FAIL: identify missed *.asm on lost-asm"; fail=1; }




echo "== plan header (Superpowers leaf) =="
need "scripts/lib/work_order.py"
need "templates/work-order.md"
need "evals/fixtures/plans-header/work-order-missing-header.md"
need "evals/fixtures/plans-header/work-order-complete.md"
grep -q "Review Focus" "$ROOT/templates/work-order.md" || { echo "EVAL FAIL: template missing Review Focus"; fail=1; }
grep -q "Global Constraints" "$ROOT/templates/work-order.md" || { echo "EVAL FAIL: template missing Global Constraints"; fail=1; }
grep -q "work_order.py" "$ROOT/scripts/gate.sh" || { echo "EVAL FAIL: gate.sh does not call work_order.py"; fail=1; }
grep -q "work_order.py" "$ROOT/scripts/gate.ps1" || { echo "EVAL FAIL: gate.ps1 does not call work_order.py"; fail=1; }
if python3 "$ROOT/scripts/lib/work_order.py" "$ROOT/evals/fixtures/plans-header/work-order-missing-header.md" >/tmp/et-wo-miss.out 2>&1; then
  echo "EVAL FAIL: incomplete work-order should fail plan-header check"
  fail=1
else
  grep -qi "Review Focus\|Goal\|Architecture\|plan header\|work_order FAIL" /tmp/et-wo-miss.out \
    || { echo "EVAL FAIL: missing-header failure message unclear"; fail=1; }
  echo "EVAL PASS: incomplete plan header rejected"
fi
if ! python3 "$ROOT/scripts/lib/work_order.py" "$ROOT/evals/fixtures/plans-header/work-order-complete.md" >/tmp/et-wo-ok.out 2>&1; then
  echo "EVAL FAIL: complete work-order should pass plan-header check"
  cat /tmp/et-wo-ok.out
  fail=1
else
  echo "EVAL PASS: complete plan header accepted"
fi
rm -f /tmp/et-wo-miss.out /tmp/et-wo-ok.out

echo "== finish menu (forge aspect) =="
need "skills/emperor-forge/finish-menu.md"
need "scripts/finish.sh"
need "scripts/finish.ps1"
bash -n "$ROOT/scripts/finish.sh" || { echo "EVAL FAIL: finish.sh syntax"; fail=1; }
grep -q "Merge back to" "$ROOT/skills/emperor-forge/finish-menu.md" || { echo "EVAL FAIL: finish-menu missing merge option"; fail=1; }
grep -q "typed word" "$ROOT/skills/emperor-forge/finish-menu.md" || { echo "EVAL FAIL: finish-menu missing discard confirm"; fail=1; }
grep -q "finish-menu.md" "$ROOT/skills/emperor-forge/SKILL.md" || { echo "EVAL FAIL: forge skill missing finish-menu"; fail=1; }
grep -q 'finish|' "$ROOT/scripts/emperor" || { echo "EVAL FAIL: emperor bash missing finish"; fail=1; }
FIN_OUT=$(bash "$ROOT/scripts/finish.sh" 2>&1) || true
echo "$FIN_OUT" | grep -q '^ENV kind=' || { echo "EVAL FAIL: finish.sh missing ENV kind"; fail=1; }
echo "$FIN_OUT" | grep -q '^MENU ' || { echo "EVAL FAIL: finish.sh missing MENU"; fail=1; }
out=$(bash "$ROOT/scripts/route.sh" "finish the branch" 2>/dev/null || true)
echo "$out" | grep -q "emperor-forge" || { echo "EVAL FAIL: route finish the branch → forge"; fail=1; }

echo "== activate MUST-route (SessionStart leaf) =="
need "skills/emperor-resume/must-route.md"
need "scripts/lib/activate.py"
need "scripts/activate.sh"
need "scripts/activate.ps1"
bash -n "$ROOT/scripts/activate.sh" || { echo "EVAL FAIL: activate.sh syntax"; fail=1; }
python3 -m py_compile "$ROOT/scripts/lib/activate.py" || { echo "EVAL FAIL: activate.py compile"; fail=1; }
grep -q 'activate.py' "$ROOT/scripts/activate.sh" || { echo "EVAL FAIL: activate.sh does not call activate.py"; fail=1; }
grep -q 'activate.py' "$ROOT/scripts/activate.ps1" || { echo "EVAL FAIL: activate.ps1 does not call activate.py"; fail=1; }
grep -q 'activate|' "$ROOT/scripts/emperor" || { echo "EVAL FAIL: emperor bash missing activate"; fail=1; }
grep -q 'scripts/activate' "$ROOT/hooks/hooks.json" || { echo "EVAL FAIL: SessionStart missing activate"; fail=1; }
grep -q 'MUST-route' "$ROOT/hooks/hooks.json" || { echo "EVAL FAIL: SessionStart prompt missing MUST-route"; fail=1; }
grep -q 'must-route.md' "$ROOT/skills/emperor-resume/SKILL.md" || { echo "EVAL FAIL: resume skill missing must-route"; fail=1; }
grep -q 'using-superpowers' "$ROOT/skills/emperor-resume/must-route.md" || { echo "EVAL FAIL: must-route missing provenance"; fail=1; }
ACT_OUT=$(python3 "$ROOT/scripts/lib/activate.py" --cwd "$ROOT" 2>&1) || true
echo "$ACT_OUT" | grep -q '^ACTIVATION must_route=yes' || { echo "EVAL FAIL: activate missing must_route=yes"; fail=1; }
echo "$ACT_OUT" | grep -q '^ACTIVATION next=' || { echo "EVAL FAIL: activate missing next="; fail=1; }
echo "$ACT_OUT" | grep -q '^MUST:' || { echo "EVAL FAIL: activate missing MUST line"; fail=1; }
ACT_U=$(python3 "$ROOT/scripts/lib/activate.py" --cwd "$ROOT" -u 'red build' 2>&1) || true
echo "$ACT_U" | grep -q 'emperor-heal' || { echo "EVAL FAIL: activate utterance red build → heal"; fail=1; }

if [[ "$fail" -ne 0 ]]; then
  echo "EVALS FAILED"
  exit 1
fi
echo "EVALS PASSED"
