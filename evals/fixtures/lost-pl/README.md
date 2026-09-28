# lost-pl fixture

Synthetic lost Perl tree for Emperor Time archaeology drills.

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
`evals/fixtures/lost-yacc/`, and `evals/fixtures/lost-roff/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.PL` | DOS-era 8.3 caps filename; `perl HELLO.PL` prints `EMPEROR-TIME-PERL-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a Perl interpreter runs)

**Named era+dialect from evidence alone:**

- Extension `.PL` / `.pl` / `.pm` + 8.3 uppercase name → Perl script culture
  (Larry Wall Perl 5 / Debian perl consumers of the same programfile surface).
- Source uses only a trivial `print` of the probe string — dialect-honest
  (interpreter programfile probe, not a CPAN / XS / mod_perl claim).
- No tradenames beyond the filename culture — deliberately minimal.
- Fossils deliberately use `*.pl` and `*.pm`. Bare `.pl` is **refused** as a
  route tag (substring collision with PL/I `.pli` / `.pl1`). Prefer `perl` /
  `perl5` / `.pm`. Prolog already left `*.pl` alone for this reclaim.

Until `perl` / another Perl interpreter runs against this file, the dialect
label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python or shell. Understanding is a running
Perl interpreter. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-pl
# or: bash scripts/identify.sh evals/fixtures/lost-pl
```
