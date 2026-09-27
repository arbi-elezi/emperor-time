# Bake-off — 2026-09-25 (honesty refresh 2026-09-27)

Three closed tasks on this repo. One agent. Not three isolated vendor sessions
(that would be a different experiment). Lenses: Emperor Time (executed),
Superpowers process-from-public-names (not executed as a plugin),
naked (what we would have shipped without a rite).

## Tasks (G1)

1. Steal router selection table names `ci-mode.md` and `swarm-emulate.md`.
2. SessionStart hook treats `emperor.cmd` as a peer, not “No cmd.exe shim”.
3. `scripts/eval.sh` fails if (1) or (2) regress.

Out of scope: spawning Claude with the Superpowers plugin; Windows live pwsh;
live multi-vendor defect-rate numbers.

## ET path (executed)

probe: grep -q ci-mode.md chains/steal-chain/SKILL.md && grep -q swarm-emulate.md chains/steal-chain/SKILL.md && echo STEAL_ROWS_OK
expect: STEAL_ROWS_OK

probe: grep -q emperor.cmd hooks/hooks.json && echo HOOK_PEER_OK
expect: HOOK_PEER_OK

probe: bash scripts/eval.sh
expect: EVALS PASSED

Babysitting: one standing order (“do it”). No mid-flight questions.

## Superpowers lens (not executed — CONJECTURE)

Would announce using-superpowers → writing-plans → TDD on eval.sh first.
Would likely fix the same holes. Would not add claim-ledger states.
Would ask design questions before the three-line patch (Socratic cost).
Activation advantage *at the 2026-09-25 cut*: marketplace hook would have
fired without this chat. That activation gap is **closing** on disk (below);
live agent open-without-tell remains a re-run, not a number invented here.

## Naked lens (not executed — CONJECTURE)

Would patch the router and stop. Would not grow eval.sh. Hook wording would
stay stale. Regression next week.

## Mechanism inventory on main (local — TESTED / VERIFIED)

Local structural eval (`scripts/lib/eval.py` via thin twins) owns these leaves. Status labels
mean **disk + eval**, not live multi-vendor win rates.

| Leaf | Path / command | Local status |
|---|---|---|
| plans (Plan Document Header) | `scripts/lib/work_order.py` + `evals/fixtures/plans-header/` | TESTED |
| finish menu (Python core) | `scripts/lib/finish.py` + thin `finish.sh`/`finish.ps1` + `finish-menu.md` | TESTED |
| activate / MUST-route | `skills/emperor-resume/must-route.md` + `scripts/lib/activate.py` | TESTED |
| grill (brainstorm HARD-GATE) | `skills/emperor-require-design/grill-checklist.md` + `emperor grill` | TESTED |
| debug four phases | `skills/emperor-heal/debug-four-phases.md` + `emperor heal` | TESTED |
| TDD iron-law / RGR | `skills/emperor-tdd/red-green-refactor.md` + `emperor tdd` | TESTED |
| worktree isolation | `skills/emperor-worktree/isolation-checklist.md` + `emperor iso` | TESTED |
| request-review | `skills/emperor-verify/request-review-checklist.md` + `emperor review` | TESTED |
| receive-review | `skills/emperor-verify/receive-review-checklist.md` + `emperor receive` | TESTED |
| executing-plans | `skills/emperor-build/executing-plans-checklist.md` + `emperor execute` | TESTED |
| subagent-driven | `skills/emperor-build/subagent-driven-checklist.md` + `emperor subagent` | TESTED |
| parallel-dispatch | `skills/emperor-dispatch/parallel-dispatch-checklist.md` + `emperor parallel` | TESTED |
| authoring iron-law | `chains/chain-jail/authoring-checklist.md` + `emperor author` | TESTED |
| evidence / verification-before-completion | `skills/emperor-verify/verification-checklist.md` + `emperor evidence` | TESTED |
| archaeology Pascal | `evals/fixtures/lost-pas/` + Jail pin | TESTED |
| archaeology ASM | `evals/fixtures/lost-asm/` + Jail pin | TESTED |
| archaeology COBOL | `evals/fixtures/lost-cbl/` + Jail pin | TESTED |
| archaeology Fortran | `evals/fixtures/lost-f90/` + Jail pin | TESTED |
| archaeology VHDL | `evals/fixtures/lost-vhd/` + Jail pin | TESTED |
| archaeology Ada | `evals/fixtures/lost-ada/` + Jail pin | TESTED |
| archaeology Forth | `evals/fixtures/lost-fs/` + Jail pin | TESTED |
| archaeology Common Lisp | `evals/fixtures/lost-lisp/` + Jail pin | TESTED |
| archaeology Prolog | `evals/fixtures/lost-prolog/` + Jail pin | TESTED |
| archaeology Tcl | `evals/fixtures/lost-tcl/` + Jail pin | TESTED |
| archaeology Erlang | `evals/fixtures/lost-erl/` + Jail pin | TESTED |
| archaeology REXX | `evals/fixtures/lost-rex/` + Jail pin | TESTED |
| mechanical gates (Python core) | `scripts/lib/gate.py` + thin `gate.sh`/`gate.ps1` | TESTED |
| identify survey (Python core) | `scripts/lib/identify.py` + thin `identify.sh`/`identify.ps1` | TESTED |
| structural eval (Python core) | `scripts/lib/eval.py` + thin `eval.sh`/`eval.ps1` | TESTED |
| DONE probes (Python core) | `scripts/lib/done.py` + thin `done.sh`/`done.ps1` + `evals/fixtures/done-probes/` | TESTED |
| route MVP (Fortran/VHDL/Ada/Forth/Lisp/Prolog/Tcl/Erlang/REXX excavate) | `scripts/lib/route.py` + thin `route.sh`/`route.ps1` + triggers `.f90`/`fortran`/`gfortran`/`.vhd`/`vhdl`/`ghdl`/`.adb`/`ada`/`gnat`/`gnatmake`/`.fs`/`pforth`/`gforth`/`.fth`/`.lisp`/`clisp`/`sbcl`/`.pro`/`swipl`/`gprolog`/`.tcl`/`tclsh`/`.erl`/`escript`/`erlc`/`.rex`/`regina`/`rexx` | TESTED |
| silent-boot zsh parity | `scripts/emperor.zsh` host.env auto-boot + host/boot/identify/excavate specials (bash twin) | TESTED |
| queue picker (Python core) | `scripts/lib/queue.py` + thin `queue.sh`/`queue.ps1` (WIP=1, placeholder skip, gh/Linear/local) | TESTED |
| forge PR (Python core) | `scripts/lib/forge.py` + thin `forge.sh`/`forge.ps1` (consent, DONE, title/G1 body, DRY) | TESTED |
| review-pack (Python core) | `scripts/lib/review_pack.py` + thin `review-pack.sh`/`review-pack.ps1` (meta SHAs, acceptance criteria extract, diff) | TESTED |
| dowse scan (Python core) | `scripts/lib/dowse.py` + thin `dowse.sh`/`dowse.ps1` (AsJson + Binary/Headless/SignIn roster) | TESTED |
| install deploy (Python core) | `scripts/lib/install.py` + thin `install.sh`/`install.ps1` (harness map, dry-run, chain expose) | TESTED |
| silent-boot (Python core) | `scripts/lib/host.py` + `scripts/lib/boot.py` + thin `boot.sh`/`boot.ps1` (host.env report + survey + optional eval.log) | TESTED |
| worktree create (Python core) | `scripts/lib/worktree.py` + thin `worktree.sh`/`worktree.ps1` (`.worktrees/<id>`, `emperor/<id>`) | TESTED |
| excavate thin alias | thin `excavate.sh`/`excavate.ps1` → `identify.py` (no hop through identify twins) | TESTED |
| session-discovery (Python core) | `scripts/lib/session_discovery.py` + thin twins + `skills/emperor-heal/session-discovery.md` + `emperor session-discovery` | TESTED |
| diagnose (intake+cite HARD-GATE) | `scripts/lib/diagnose.py` + thin twins + `skills/emperor-heal/diagnosing.md` + `emperor diagnose` | TESTED |
| root-cause tracing (HARD-GATE) | `scripts/lib/root_cause.py` + thin twins + `skills/emperor-heal/root-cause-tracing.md` + `emperor trace` | TESTED |
| defense-in-depth (HARD-GATE) | `scripts/lib/defense.py` + thin twins + `skills/emperor-heal/defense-in-depth.md` + `emperor defense` | TESTED |
| condition-based-waiting (HARD-GATE) | `scripts/lib/condition_wait.py` + thin twins + `skills/emperor-heal/condition-based-waiting.md` + `emperor wait` | TESTED |
| find-polluter (HARD-GATE) | `scripts/lib/polluter.py` + thin twins + `skills/emperor-heal/find-polluter.md` + `emperor polluter` | TESTED |
| pressure/academic (HARD-GATE) | `scripts/lib/pressure.py` + thin twins + `skills/emperor-heal/pressure-academic.md` + `emperor pressure` | TESTED |
| writing-good-tests (HARD-GATE) | `scripts/lib/good_tests.py` + thin twins + `skills/emperor-tdd/writing-good-tests.md` + `emperor good-tests` | TESTED |
| testing-skills (HARD-GATE) | `scripts/lib/skill_test.py` + thin twins + `chains/chain-jail/testing-skills.md` + `emperor skill-test` | TESTED |
| persuasion-principles (HARD-GATE) | `scripts/lib/persuasion.py` + thin twins + `chains/chain-jail/persuasion-principles.md` + `emperor persuasion` | TESTED |
| skill-discovery / SDO (HARD-GATE) | `scripts/lib/sdo.py` + thin twins + `chains/chain-jail/skill-discovery.md` + `emperor sdo` | TESTED |

Honesty helper: `scripts/lib/bakeoff_honesty.py` fails if this inventory
drifts from disk or if live-defect-rate is mislabeled.

## Claim ledger (bake-off axes)

| Claim | Status | Evidence |
|---|---|---|
| Local mechanism leaves above exist and are eval-locked | TESTED | `bash scripts/eval.sh` (eval.py) → EVALS PASSED; honesty helper exit 0 |
| Activation MUST-route fires from SessionStart without waiting for “emperor time” (hook + card contract) | TESTED | hooks.json → activate; `activate.py` prints `ACTIVATION next=` |
| Agents *in the wild* open `ACTIVATION next=` without being told | UNVERIFIABLE | no marketplace re-run bakeoff in this session |
| Live defect-rate vs Superpowers (shared tasks, isolated vendor sessions) | UNVERIFIABLE | no three-vendor third-repo bake-off run; **no fake numbers** |
| ET wins *mechanical lock-in* on the 2026-09-25 slice (eval owns Steal rows + hook peer) | VERIFIED | STEAL_ROWS_OK + HOOK_PEER_OK + EVALS PASSED quoted in session |

## Verdict

ET wins this slice on *mechanical lock-in* (eval owns the rows; leaf gates
above are on disk and eval-locked through v0.4.53).
Activation *mechanism* is closed on disk (v0.4.5–0.4.6); wild-agent
activation without a tell stays **UNVERIFIABLE** until a marketplace re-run.
Live defect-rate vs Superpowers stays **UNVERIFIABLE** — do not invent %.
Naked loses on (3).
This is not a substitute for three isolated vendor sessions on a third repo.
