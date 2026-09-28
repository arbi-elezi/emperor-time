# lost-m4 fixture

Synthetic lost m4 tree for Emperor Time archaeology drills.

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
and `evals/fixtures/lost-sed/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.M4` | DOS-era 8.3 caps filename; `define`/`dnl` prints `EMPEROR-TIME-M4-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until an m4 system runs)

**Named era+dialect from evidence alone:**

- Extension `.M4` / `.m4` + 8.3 uppercase name → m4 macro file culture
  (GNU m4 / other m4 consumers of the same `define`/`dnl`
  surface).
- Source uses only a single define + expansion — dialect-honest (print probe,
  not a full POSIX m4 / traditional AT&T m4 / Autoconf
  claim).
- No tradenames beyond the filename culture — deliberately minimal.
- Fossils deliberately use `*.m4` only.

Until `m4` / another macro processor runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running m4
system. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-m4
# or: bash scripts/identify.sh evals/fixtures/lost-m4
```
