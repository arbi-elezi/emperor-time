# lost-yacc fixture

Synthetic lost yacc / bison tree for Emperor Time archaeology drills.

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
`evals/fixtures/lost-dc/`, and `evals/fixtures/lost-lex/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.Y` | DOS-era 8.3 caps filename; bison→gcc print `EMPEROR-TIME-YACC-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a yacc system runs)

**Named era+dialect from evidence alone:**

- Extension `.Y` / `.y` + 8.3 uppercase name → yacc grammar file culture
  (GNU Bison / POSIX yacc consumers of the same
  `%{ … %}` / `%%` rules surface).
- Source uses only a trivial empty rule + `main` print — dialect-honest (generator
  invoke probe, not a full POSIX Yacc / Berkeley Yacc / Bison++ claim).
- No tradenames beyond the filename culture — deliberately minimal.
- Fossils deliberately use `*.y`.

Until `bison` / `yacc` / another parser generator runs against this
file, the dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running yacc
generator + C toolchain. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-yacc
# or: bash scripts/identify.sh evals/fixtures/lost-yacc
```
