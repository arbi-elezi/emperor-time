# lost-rex fixture

Synthetic lost REXX tree for Emperor Time archaeology drills.

Sister probe to `evals/fixtures/lost-pas/`, `evals/fixtures/lost-asm/`,
`evals/fixtures/lost-cbl/`, `evals/fixtures/lost-f90/`,
`evals/fixtures/lost-vhd/`, `evals/fixtures/lost-ada/`,
`evals/fixtures/lost-fs/`, `evals/fixtures/lost-lisp/`,
`evals/fixtures/lost-prolog/`, `evals/fixtures/lost-tcl/`,
and `evals/fixtures/lost-erl/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.REX` | DOS-era 8.3 caps filename; `SAY` prints `EMPEROR-TIME-REX-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a REXX runs)

**Named era+dialect from evidence alone:**

- Extension `.REX` / `.rex` / `.rexx` + 8.3 uppercase name → REXX script
  culture (Regina 3.9.x family *or* any Classic Rexx / ANSI interpreter
  consuming the same `SAY` surface).
- Source uses only shebang + block comment + `SAY` — dialect-honest
  (string-print probe, not an ADDRESS host or ooRexx claim).
- No `PARSE ARG`, no `ADDRESS`, no external functions — deliberately
  minimal.

Until `rexx` / `regina` / another REXX runs against this file, the dialect
label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running `rexx` or
emulator trace. See `references/archaeology.md` and prior ET lost-tree loop:
survey → name era+dialect → Jail-hunt one manual heading → boot probe →
characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-rex
# or: bash scripts/identify.sh evals/fixtures/lost-rex
```
