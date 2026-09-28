# lost-expect fixture

Synthetic lost Expect tree for Emperor Time archaeology drills.

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
`evals/fixtures/lost-apl/`, `evals/fixtures/lost-bcpl/`,
`evals/fixtures/lost-pli/`, `evals/fixtures/lost-st/`,
`evals/fixtures/lost-ps/`, `evals/fixtures/lost-bas/`,
`evals/fixtures/lost-scm/`, `evals/fixtures/lost-awk/`,
`evals/fixtures/lost-sed/`, `evals/fixtures/lost-m4/`,
`evals/fixtures/lost-ed/`, `evals/fixtures/lost-make/`,
`evals/fixtures/lost-dc/`, `evals/fixtures/lost-lex/`,
`evals/fixtures/lost-yacc/`, `evals/fixtures/lost-roff/`,
`evals/fixtures/lost-pl/`, and `evals/fixtures/lost-bc/`.

Companion programmed-dialogue leaf to `lost-tcl` (Expect sits on Tcl).

## Artifacts

| File | Role |
|------|------|
| `HELLO.EXP` | DOS-era 8.3 caps filename; `expect HELLO.EXP` prints `EMPEROR-TIME-EXPECT-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until an Expect system runs)

**Named era+dialect from evidence alone:**

- Extension `.EXP` / `.exp` + 8.3 uppercase name → Expect script file culture
  (Don Libes Expect / other Expect consumers of the same `puts`/`exit`
  surface).
- Source uses only puts + exit — dialect-honest (print probe,
  not a full spawn/expect/send dialogue claim).
- No tradenames beyond the filename culture — deliberately minimal.
- Fossils deliberately use `*.exp` only. Prefer `expect` /
  `tcl-expect` / `.exp`.

Until `expect` / another programmed-dialogue tool runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python or shell. Understanding is a running Expect
system. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-expect
# or: bash scripts/identify.sh evals/fixtures/lost-expect
```
