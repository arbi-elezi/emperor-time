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
for pair in "done" gate eval review-pack dowse install worktree queue forge finish activate identify boot route excavate heal grill tdd iso review; do
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


echo "== route.py Python core =="
need "scripts/lib/route.py"
python3 -m py_compile "$ROOT/scripts/lib/route.py" || { echo "EVAL FAIL: route.py compile"; fail=1; }
grep -q 'lib/route.py' "$ROOT/scripts/route.sh" || { echo "EVAL FAIL: route.sh does not call route.py"; fail=1; }
grep -q 'lib/route.py' "$ROOT/scripts/route.ps1" || { echo "EVAL FAIL: route.ps1 does not call route.py"; fail=1; }
ROUT_PY=$(python3 "$ROOT/scripts/lib/route.py" "finish the branch" 2>/dev/null || true)
echo "$ROUT_PY" | grep -q "emperor-forge" || { echo "EVAL FAIL: route.py finish the branch → forge"; fail=1; }
if python3 "$ROOT/scripts/lib/route.py" "what is 2+2" >/dev/null 2>&1; then
  echo "EVAL FAIL: route.py should miss trivia"
  fail=1
else
  echo "EVAL PASS: route.py misses trivia"
fi

echo "== MUST-route doctrine + adapters =="
grep -q 'MUST: pick one governing' "$ROOT/SKILL.md" || { echo "EVAL FAIL: SKILL Load law missing MUST governing"; fail=1; }
grep -q 'MUST-route (standing order)' "$ROOT/AGENTS.md" || { echo "EVAL FAIL: AGENTS missing MUST-route standing order"; fail=1; }
grep -q 'MUST-route' "$ROOT/hooks/hooks.json" || { echo "EVAL FAIL: SessionStart prompt missing MUST-route"; fail=1; }
for ad in cursor codex kimi-cli ollama opencode generic; do
  grep -q 'MUST-route (before creative work)' "$ROOT/adapters/$ad/README.md" \
    || { echo "EVAL FAIL: adapters/$ad missing MUST-route note"; fail=1; }
done
grep -q 'scripts/lib/route.py' "$ROOT/references/sdlc-comparison.md" \
  || { echo "EVAL FAIL: sdlc-comparison missing route.py"; fail=1; }
grep -q 'eval.yml' "$ROOT/references/sdlc-comparison.md" \
  || { echo "EVAL FAIL: sdlc-comparison missing eval.yml honesty"; fail=1; }


echo "== heal four-phase debug leaf =="
need "skills/emperor-heal/debug-four-phases.md"
need "scripts/lib/debug_phases.py"
need "scripts/heal.sh"
need "scripts/heal.ps1"
bash -n "$ROOT/scripts/heal.sh" || { echo "EVAL FAIL: heal.sh syntax"; fail=1; }
python3 -m py_compile "$ROOT/scripts/lib/debug_phases.py" || { echo "EVAL FAIL: debug_phases.py compile"; fail=1; }
grep -q 'debug_phases.py' "$ROOT/scripts/heal.sh" || { echo "EVAL FAIL: heal.sh does not call debug_phases.py"; fail=1; }
grep -q 'debug_phases.py' "$ROOT/scripts/heal.ps1" || { echo "EVAL FAIL: heal.ps1 does not call debug_phases.py"; fail=1; }
grep -q 'heal|' "$ROOT/scripts/emperor" || { echo "EVAL FAIL: emperor bash missing heal"; fail=1; }
grep -q "'heal'" "$ROOT/scripts/emperor.ps1" || { echo "EVAL FAIL: emperor.ps1 missing heal"; fail=1; }
grep -q 'debug-four-phases.md' "$ROOT/skills/emperor-heal/SKILL.md" || { echo "EVAL FAIL: heal skill missing four-phase leaf"; fail=1; }
grep -q 'The Four Phases' "$ROOT/skills/emperor-heal/debug-four-phases.md" || { echo "EVAL FAIL: four-phase leaf missing provenance heading"; fail=1; }
grep -q 'systematic-debugging' "$ROOT/skills/emperor-heal/debug-four-phases.md" || { echo "EVAL FAIL: four-phase leaf missing source skill"; fail=1; }
grep -q 'debug-four-phases.md' "$ROOT/chains/holy-chain/SKILL.md" || { echo "EVAL FAIL: holy-chain missing four-phase MUST"; fail=1; }
HEAL_OUT=$(python3 "$ROOT/scripts/lib/debug_phases.py" 2>&1) || true
echo "$HEAL_OUT" | grep -q '^DEBUG four_phases=yes' || { echo "EVAL FAIL: debug_phases missing four_phases=yes"; fail=1; }
echo "$HEAL_OUT" | grep -q '^PHASE 1 ' || { echo "EVAL FAIL: debug_phases missing PHASE 1"; fail=1; }
echo "$HEAL_OUT" | grep -q '^PHASE 4 ' || { echo "EVAL FAIL: debug_phases missing PHASE 4"; fail=1; }
echo "$HEAL_OUT" | grep -q '^MUST:' || { echo "EVAL FAIL: debug_phases missing MUST line"; fail=1; }
if python3 "$ROOT/scripts/lib/debug_phases.py" --advance 1 3 >/dev/null 2>&1; then
  echo "EVAL FAIL: debug_phases should reject phase skip 1→3"
  fail=1
else
  echo "EVAL PASS: debug_phases rejects skip 1→3"
fi
ADV_OK=$(python3 "$ROOT/scripts/lib/debug_phases.py" --advance 2 3 2>&1) || true
echo "$ADV_OK" | grep -q '^ADVANCE OK' || { echo "EVAL FAIL: debug_phases 2→3 should OK"; fail=1; }
HEAL_SH=$(bash "$ROOT/scripts/heal.sh" 2>&1) || true
echo "$HEAL_SH" | grep -q '^DEBUG four_phases=yes' || { echo "EVAL FAIL: heal.sh missing four_phases card"; fail=1; }

echo "== grill brainstorm HARD-GATE leaf =="
need "skills/emperor-require-design/grill-checklist.md"
need "scripts/lib/grill.py"
need "scripts/grill.sh"
need "scripts/grill.ps1"
bash -n "$ROOT/scripts/grill.sh" || { echo "EVAL FAIL: grill.sh syntax"; fail=1; }
python3 -m py_compile "$ROOT/scripts/lib/grill.py" || { echo "EVAL FAIL: grill.py compile"; fail=1; }
grep -q 'grill.py' "$ROOT/scripts/grill.sh" || { echo "EVAL FAIL: grill.sh does not call grill.py"; fail=1; }
grep -q 'grill.py' "$ROOT/scripts/grill.ps1" || { echo "EVAL FAIL: grill.ps1 does not call grill.py"; fail=1; }
grep -q 'grill|' "$ROOT/scripts/emperor" || { echo "EVAL FAIL: emperor bash missing grill"; fail=1; }
grep -q "'grill'" "$ROOT/scripts/emperor.ps1" || { echo "EVAL FAIL: emperor.ps1 missing grill"; fail=1; }
grep -q 'grill-checklist.md' "$ROOT/skills/emperor-require-design/SKILL.md" || { echo "EVAL FAIL: require-design missing grill leaf"; fail=1; }
grep -q 'HARD-GATE' "$ROOT/skills/emperor-require-design/grill-checklist.md" || { echo "EVAL FAIL: grill leaf missing HARD-GATE heading"; fail=1; }
grep -q 'brainstorming' "$ROOT/skills/emperor-require-design/grill-checklist.md" || { echo "EVAL FAIL: grill leaf missing source skill"; fail=1; }
GRILL_OUT=$(python3 "$ROOT/scripts/lib/grill.py" 2>&1) || true
echo "$GRILL_OUT" | grep -q '^GRILL checklist=yes' || { echo "EVAL FAIL: grill missing checklist=yes"; fail=1; }
echo "$GRILL_OUT" | grep -q '^STEP 1 ' || { echo "EVAL FAIL: grill missing STEP 1"; fail=1; }
echo "$GRILL_OUT" | grep -q '^STEP 5 ' || { echo "EVAL FAIL: grill missing STEP 5"; fail=1; }
echo "$GRILL_OUT" | grep -q '^MUST:' || { echo "EVAL FAIL: grill missing MUST line"; fail=1; }
if python3 "$ROOT/scripts/lib/grill.py" --advance 1 3 >/dev/null 2>&1; then
  echo "EVAL FAIL: grill should reject step skip 1→3"
  fail=1
else
  echo "EVAL PASS: grill rejects skip 1→3"
fi
ADV_OK=$(python3 "$ROOT/scripts/lib/grill.py" --advance 2 3 2>&1) || true
echo "$ADV_OK" | grep -q '^ADVANCE OK' || { echo "EVAL FAIL: grill 2→3 should OK"; fail=1; }
if python3 "$ROOT/scripts/lib/grill.py" --reject-impl >/dev/null 2>&1; then
  echo "EVAL FAIL: grill --reject-impl should exit non-zero"
  fail=1
else
  REJECT=$(python3 "$ROOT/scripts/lib/grill.py" --reject-impl 2>&1) || true
  echo "$REJECT" | grep -q '^REJECT IMPL:' || { echo "EVAL FAIL: reject-impl missing REJECT IMPL line"; fail=1; }
  echo "EVAL PASS: grill --reject-impl hard-gates impl"
fi
GRILL_SH=$(bash "$ROOT/scripts/grill.sh" 2>&1) || true
echo "$GRILL_SH" | grep -q '^GRILL checklist=yes' || { echo "EVAL FAIL: grill.sh missing checklist card"; fail=1; }

echo "== tdd iron-law / RGR HARD-GATE leaf =="
need "skills/emperor-tdd/red-green-refactor.md"
need "scripts/lib/tdd.py"
need "scripts/tdd.sh"
need "scripts/tdd.ps1"
bash -n "$ROOT/scripts/tdd.sh" || { echo "EVAL FAIL: tdd.sh syntax"; fail=1; }
python3 -m py_compile "$ROOT/scripts/lib/tdd.py" || { echo "EVAL FAIL: tdd.py compile"; fail=1; }
grep -q 'tdd.py' "$ROOT/scripts/tdd.sh" || { echo "EVAL FAIL: tdd.sh does not call tdd.py"; fail=1; }
grep -q 'tdd.py' "$ROOT/scripts/tdd.ps1" || { echo "EVAL FAIL: tdd.ps1 does not call tdd.py"; fail=1; }
grep -q 'tdd|' "$ROOT/scripts/emperor" || { echo "EVAL FAIL: emperor bash missing tdd"; fail=1; }
grep -q "'tdd'" "$ROOT/scripts/emperor.ps1" || { echo "EVAL FAIL: emperor.ps1 missing tdd"; fail=1; }
grep -q 'red-green-refactor.md' "$ROOT/skills/emperor-tdd/SKILL.md" || { echo "EVAL FAIL: emperor-tdd missing RGR leaf"; fail=1; }
grep -q 'HARD-GATE' "$ROOT/skills/emperor-tdd/red-green-refactor.md" || { echo "EVAL FAIL: tdd leaf missing HARD-GATE heading"; fail=1; }
grep -q 'test-driven-development' "$ROOT/skills/emperor-tdd/red-green-refactor.md" || { echo "EVAL FAIL: tdd leaf missing source skill"; fail=1; }
TDD_OUT=$(python3 "$ROOT/scripts/lib/tdd.py" 2>&1) || true
echo "$TDD_OUT" | grep -q '^TDD checklist=yes' || { echo "EVAL FAIL: tdd missing checklist=yes"; fail=1; }
echo "$TDD_OUT" | grep -q '^STEP 1 ' || { echo "EVAL FAIL: tdd missing STEP 1"; fail=1; }
echo "$TDD_OUT" | grep -q '^STEP 5 ' || { echo "EVAL FAIL: tdd missing STEP 5"; fail=1; }
echo "$TDD_OUT" | grep -q '^MUST:' || { echo "EVAL FAIL: tdd missing MUST line"; fail=1; }
echo "$TDD_OUT" | grep -q 'NO_PRODUCTION_CODE_WITHOUT_FAILING_PROBE_FIRST' || { echo "EVAL FAIL: tdd missing iron law token"; fail=1; }
if python3 "$ROOT/scripts/lib/tdd.py" --advance 1 3 >/dev/null 2>&1; then
  echo "EVAL FAIL: tdd should reject step skip 1→3"
  fail=1
else
  echo "EVAL PASS: tdd rejects skip 1→3"
fi
ADV_OK=$(python3 "$ROOT/scripts/lib/tdd.py" --advance 2 3 2>&1) || true
echo "$ADV_OK" | grep -q '^ADVANCE OK' || { echo "EVAL FAIL: tdd 2→3 should OK"; fail=1; }
if python3 "$ROOT/scripts/lib/tdd.py" --reject-prod >/dev/null 2>&1; then
  echo "EVAL FAIL: tdd --reject-prod should exit non-zero"
  fail=1
else
  REJECT=$(python3 "$ROOT/scripts/lib/tdd.py" --reject-prod 2>&1) || true
  echo "$REJECT" | grep -q '^REJECT PROD:' || { echo "EVAL FAIL: reject-prod missing REJECT PROD line"; fail=1; }
  echo "EVAL PASS: tdd --reject-prod hard-gates prod"
fi
TDD_SH=$(bash "$ROOT/scripts/tdd.sh" 2>&1) || true
echo "$TDD_SH" | grep -q '^TDD checklist=yes' || { echo "EVAL FAIL: tdd.sh missing checklist card"; fail=1; }


echo "== worktree isolation HARD-GATE leaf =="
need "skills/emperor-worktree/isolation-checklist.md"
need "scripts/lib/worktree_iso.py"
need "scripts/iso.sh"
need "scripts/iso.ps1"
bash -n "$ROOT/scripts/iso.sh" || { echo "EVAL FAIL: iso.sh syntax"; fail=1; }
python3 -m py_compile "$ROOT/scripts/lib/worktree_iso.py" || { echo "EVAL FAIL: worktree_iso.py compile"; fail=1; }
grep -q 'worktree_iso.py' "$ROOT/scripts/iso.sh" || { echo "EVAL FAIL: iso.sh does not call worktree_iso.py"; fail=1; }
grep -q 'worktree_iso.py' "$ROOT/scripts/iso.ps1" || { echo "EVAL FAIL: iso.ps1 does not call worktree_iso.py"; fail=1; }
grep -q 'iso|' "$ROOT/scripts/emperor" || { echo "EVAL FAIL: emperor bash missing iso"; fail=1; }
grep -q "'iso'" "$ROOT/scripts/emperor.ps1" || { echo "EVAL FAIL: emperor.ps1 missing iso"; fail=1; }
grep -q 'isolation-checklist.md' "$ROOT/skills/emperor-worktree/SKILL.md" || { echo "EVAL FAIL: emperor-worktree missing isolation leaf"; fail=1; }
grep -q 'HARD-GATE' "$ROOT/skills/emperor-worktree/isolation-checklist.md" || { echo "EVAL FAIL: iso leaf missing HARD-GATE heading"; fail=1; }
grep -q 'using-git-worktrees' "$ROOT/skills/emperor-worktree/isolation-checklist.md" || { echo "EVAL FAIL: iso leaf missing source skill"; fail=1; }
ISO_OUT=$(python3 "$ROOT/scripts/lib/worktree_iso.py" 2>&1) || true
echo "$ISO_OUT" | grep -q '^WORKTREE checklist=yes' || { echo "EVAL FAIL: iso missing checklist=yes"; fail=1; }
echo "$ISO_OUT" | grep -q '^STEP 1 ' || { echo "EVAL FAIL: iso missing STEP 1"; fail=1; }
echo "$ISO_OUT" | grep -q '^STEP 5 ' || { echo "EVAL FAIL: iso missing STEP 5"; fail=1; }
echo "$ISO_OUT" | grep -q '^MUST:' || { echo "EVAL FAIL: iso missing MUST line"; fail=1; }
echo "$ISO_OUT" | grep -q 'NO_MUTATE_WITHOUT_ISOLATION_DETECT' || { echo "EVAL FAIL: iso missing iron law token"; fail=1; }
if python3 "$ROOT/scripts/lib/worktree_iso.py" --advance 1 3 >/dev/null 2>&1; then
  echo "EVAL FAIL: iso should reject step skip 1→3"
  fail=1
else
  echo "EVAL PASS: iso rejects skip 1→3"
fi
ADV_OK=$(python3 "$ROOT/scripts/lib/worktree_iso.py" --advance 2 3 2>&1) || true
echo "$ADV_OK" | grep -q '^ADVANCE OK' || { echo "EVAL FAIL: iso 2→3 should OK"; fail=1; }
if python3 "$ROOT/scripts/lib/worktree_iso.py" --reject-blind-create >/dev/null 2>&1; then
  echo "EVAL FAIL: iso --reject-blind-create should exit non-zero"
  fail=1
else
  REJECT=$(python3 "$ROOT/scripts/lib/worktree_iso.py" --reject-blind-create 2>&1) || true
  echo "$REJECT" | grep -q '^REJECT BLIND-CREATE:' || { echo "EVAL FAIL: reject-blind-create missing REJECT line"; fail=1; }
  echo "EVAL PASS: iso --reject-blind-create hard-gates blind create"
fi
ISO_SH=$(bash "$ROOT/scripts/iso.sh" 2>&1) || true
echo "$ISO_SH" | grep -q '^WORKTREE checklist=yes' || { echo "EVAL FAIL: iso.sh missing checklist card"; fail=1; }

echo "== request-review HARD-GATE leaf =="
need "skills/emperor-verify/request-review-checklist.md"
need "scripts/lib/review_req.py"
need "scripts/review.sh"
need "scripts/review.ps1"
bash -n "$ROOT/scripts/review.sh" || { echo "EVAL FAIL: review.sh syntax"; fail=1; }
python3 -m py_compile "$ROOT/scripts/lib/review_req.py" || { echo "EVAL FAIL: review_req.py compile"; fail=1; }
grep -q 'review_req.py' "$ROOT/scripts/review.sh" || { echo "EVAL FAIL: review.sh does not call review_req.py"; fail=1; }
grep -q 'review_req.py' "$ROOT/scripts/review.ps1" || { echo "EVAL FAIL: review.ps1 does not call review_req.py"; fail=1; }
grep -q 'review|' "$ROOT/scripts/emperor" || { echo "EVAL FAIL: emperor bash missing review"; fail=1; }
grep -q "'review'" "$ROOT/scripts/emperor.ps1" || { echo "EVAL FAIL: emperor.ps1 missing review"; fail=1; }
grep -q 'request-review-checklist.md' "$ROOT/skills/emperor-verify/SKILL.md" || { echo "EVAL FAIL: emperor-verify missing request-review leaf"; fail=1; }
grep -q 'HARD-GATE' "$ROOT/skills/emperor-verify/request-review-checklist.md" || { echo "EVAL FAIL: review leaf missing HARD-GATE heading"; fail=1; }
grep -q 'requesting-code-review' "$ROOT/skills/emperor-verify/request-review-checklist.md" || { echo "EVAL FAIL: review leaf missing source skill"; fail=1; }
REV_OUT=$(python3 "$ROOT/scripts/lib/review_req.py" 2>&1) || true
echo "$REV_OUT" | grep -q '^REVIEW checklist=yes' || { echo "EVAL FAIL: review missing checklist=yes"; fail=1; }
echo "$REV_OUT" | grep -q '^STEP 1 ' || { echo "EVAL FAIL: review missing STEP 1"; fail=1; }
echo "$REV_OUT" | grep -q '^STEP 5 ' || { echo "EVAL FAIL: review missing STEP 5"; fail=1; }
echo "$REV_OUT" | grep -q '^MUST:' || { echo "EVAL FAIL: review missing MUST line"; fail=1; }
echo "$REV_OUT" | grep -q 'NO_PROCEED_WITHOUT_REQUESTED_REVIEW' || { echo "EVAL FAIL: review missing iron law token"; fail=1; }
if python3 "$ROOT/scripts/lib/review_req.py" --advance 1 3 >/dev/null 2>&1; then
  echo "EVAL FAIL: review should reject step skip 1→3"
  fail=1
else
  echo "EVAL PASS: review rejects skip 1→3"
fi
ADV_OK=$(python3 "$ROOT/scripts/lib/review_req.py" --advance 2 3 2>&1) || true
echo "$ADV_OK" | grep -q '^ADVANCE OK' || { echo "EVAL FAIL: review 2→3 should OK"; fail=1; }
if python3 "$ROOT/scripts/lib/review_req.py" --reject-self-review >/dev/null 2>&1; then
  echo "EVAL FAIL: review --reject-self-review should exit non-zero"
  fail=1
else
  REJECT=$(python3 "$ROOT/scripts/lib/review_req.py" --reject-self-review 2>&1) || true
  echo "$REJECT" | grep -q '^REJECT SELF-REVIEW:' || { echo "EVAL FAIL: reject-self-review missing REJECT line"; fail=1; }
  echo "EVAL PASS: review --reject-self-review hard-gates self-review"
fi
REV_SH=$(bash "$ROOT/scripts/review.sh" 2>&1) || true
echo "$REV_SH" | grep -q '^REVIEW checklist=yes' || { echo "EVAL FAIL: review.sh missing checklist card"; fail=1; }

if [[ "$fail" -ne 0 ]]; then
  echo "EVALS FAILED"
  exit 1
fi
echo "EVALS PASSED"
