# lost-ruby fixture

Synthetic lost Ruby tree for Emperor Time archaeology drills.

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
`evals/fixtures/lost-pl/`, `evals/fixtures/lost-bc/`,
`evals/fixtures/lost-expect/`, and `evals/fixtures/lost-lua/`.

Classic scripting leaf (MRI Ruby) after Lua.

## Artifacts

| File | Role |
|------|------|
| `HELLO.RB` | DOS-era 8.3 caps filename; `ruby HELLO.RB` prints `EMPEROR-TIME-RUBY-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a Ruby system runs)

**Named era+dialect from evidence alone:**

- Extension `.RB` / `.rb` + 8.3 uppercase name → Ruby script file culture
  (MRI / other Ruby consumers of the same `puts` surface).
- Source uses only puts — dialect-honest (puts probe,
  not a full Rails / Bundler / RubyGems claim).
- No tradenames beyond the filename culture — deliberately minimal.
- Fossils deliberately use `*.rb` only. Prefer `ruby` /
  `ruby3.3` / `.rb`.

Until `ruby` / another Ruby interpreter runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python or shell. Understanding is a running Ruby
system. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-ruby
# or: bash scripts/identify.sh evals/fixtures/lost-ruby
```
