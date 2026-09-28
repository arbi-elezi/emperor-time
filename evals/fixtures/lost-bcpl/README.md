# lost-bcpl fixture

Synthetic lost BCPL tree for Emperor Time archaeology drills.

Sister probe to `evals/fixtures/lost-pas/`, `evals/fixtures/lost-asm/`,
`evals/fixtures/lost-cbl/`, `evals/fixtures/lost-f90/`,
`evals/fixtures/lost-vhd/`, `evals/fixtures/lost-ada/`,
`evals/fixtures/lost-fs/`, `evals/fixtures/lost-lisp/`,
`evals/fixtures/lost-prolog/`, `evals/fixtures/lost-tcl/`,
`evals/fixtures/lost-erl/`, `evals/fixtures/lost-rex/`,
`evals/fixtures/lost-mod/`, `evals/fixtures/lost-a68/`,
`evals/fixtures/lost-a60/`, `evals/fixtures/lost-alw/`,
`evals/fixtures/lost-icn/`, `evals/fixtures/lost-obn/`,
`evals/fixtures/lost-sno/`, `evals/fixtures/lost-cim/`,
and `evals/fixtures/lost-apl/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.B` | DOS-era 8.3 caps filename; `writef` prints `EMPEROR-TIME-BCPL-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a BCPL system runs)

**Named era+dialect from evidence alone:**

- Extension `.B` / `.b` + 8.3 uppercase name → BCPL culture
  (Martin Richards Cintcode / classic Cambridge BCPL family consuming
  the same `GET "libhdr"` / `writef` print surface).
- Source uses only `GET "libhdr"` + `LET start() = VALOF { writef(…); RESULTIS 0 }` —
  dialect-honest (print probe, not a full Tripos / native-code / floating-point claim).
- No tradenames beyond the filename culture — deliberately minimal.
- Fossils deliberately use `*.b` and `*.bcpl` (not bare English keywords;
  bare `.b` refused as a **route** tag for short-extension collision).

Until `cintsys` / another BCPL implementation runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running BCPL
compiler/interpreter or emulator trace. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-bcpl
# or: bash scripts/identify.sh evals/fixtures/lost-bcpl
```
