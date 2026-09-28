# lost-pli fixture

Synthetic lost PL/I tree for Emperor Time archaeology drills.

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
`evals/fixtures/lost-apl/`, and `evals/fixtures/lost-bcpl/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.PLI` | DOS-era 8.3 caps filename; `PUT SKIP LIST` prints `EMPEROR-TIME-PLI-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a PL/I system runs)

**Named era+dialect from evidence alone:**

- Extension `.PLI` / `.pli` / `.pl1` + 8.3 uppercase name → PL/I culture
  (Iron Spring / IBM-family PL/I consuming the same `PROCEDURE OPTIONS(MAIN)` /
  `PUT SKIP LIST` print surface).
- Source uses only `procedure options(main)` + `put skip list(…)` —
  dialect-honest (print probe, not a full IBM MVS/VM / Enterprise / STREAM EDIT claim).
- No tradenames beyond the filename culture — deliberately minimal.
- Fossils deliberately use `*.pli` and `*.pl1` (not bare English keywords).

Until `plic` / another PL/I implementation runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running PL/I
compiler or emulator trace. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-pli
# or: bash scripts/identify.sh evals/fixtures/lost-pli
```
