# lost-lex fixture

Synthetic lost lex / flex tree for Emperor Time archaeology drills.

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
and `evals/fixtures/lost-dc/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.L` | DOS-era 8.3 caps filename; flex→gcc print `EMPEROR-TIME-LEX-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a lex system runs)

**Named era+dialect from evidence alone:**

- Extension `.L` / `.l` / `.lex` + 8.3 uppercase name → lex input file culture
  (GNU flex / AT&T lex consumers of the same
  `%{ … %}` / `%%` rules surface).
- Source uses only a trivial rule set + `main` print — dialect-honest (generator
  invoke probe, not a full AT&T lex / POSIX lex / Flex++ claim).
- No tradenames beyond the filename culture — deliberately minimal.
- Fossils deliberately use `*.l` and `*.lex`.

Until `flex` / `lex` / another lexical analyzer generator runs against this
file, the dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running lex
generator + C toolchain. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-lex
# or: bash scripts/identify.sh evals/fixtures/lost-lex
```
