# lost-mod fixture

Synthetic lost Modula-2 tree for Emperor Time archaeology drills.

Sister probe to `evals/fixtures/lost-pas/`, `evals/fixtures/lost-asm/`,
`evals/fixtures/lost-cbl/`, `evals/fixtures/lost-f90/`,
`evals/fixtures/lost-vhd/`, `evals/fixtures/lost-ada/`,
`evals/fixtures/lost-fs/`, `evals/fixtures/lost-lisp/`,
`evals/fixtures/lost-prolog/`, `evals/fixtures/lost-tcl/`,
`evals/fixtures/lost-erl/`, and `evals/fixtures/lost-rex/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.MOD` | DOS-era 8.3 caps filename; `WriteString` prints `EMPEROR-TIME-MOD-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a Modula-2 compiler runs)

**Named era+dialect from evidence alone:**

- Extension `.MOD` / `.mod` / `.def` + 8.3 uppercase name → Modula-2
  implementation module culture (GNU Modula-2 / gm2 PIM family *or* any
  ISO/IEC 10514-1 compiler consuming the same `WriteString` surface).
- Source uses only `MODULE` / `FROM StrIO IMPORT WriteString, WriteLn` /
  `BEGIN` / `END` — dialect-honest (string-print probe, not a DEFINITION
  MODULE or SYSTEM claim).
- No `DEFINITION MODULE`, no `SYSTEM`, no coroutines — deliberately
  minimal.

Until `gm2` / another Modula-2 compiler runs against this file, the dialect
label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running `gm2` binary or
emulator trace. See `references/archaeology.md` and prior ET lost-tree loop:
survey → name era+dialect → Jail-hunt one manual heading → boot probe →
characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-mod
# or: bash scripts/identify.sh evals/fixtures/lost-mod
```
