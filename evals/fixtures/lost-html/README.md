# lost-html fixture

Synthetic lost HTML document tree for Emperor Time archaeology drills.

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
`evals/fixtures/lost-expect/`, `evals/fixtures/lost-lua/`,
`evals/fixtures/lost-ruby/`, `evals/fixtures/lost-go/`,
`evals/fixtures/lost-rust/`, `evals/fixtures/lost-c/`,
`evals/fixtures/lost-js/`, `evals/fixtures/lost-py/`,
`evals/fixtures/lost-ts/`, `evals/fixtures/lost-sh/`,
`evals/fixtures/lost-php/`, `evals/fixtures/lost-sql/`,
`evals/fixtures/lost-jq/`, `evals/fixtures/lost-xsl/`,
`evals/fixtures/lost-xml/`, `evals/fixtures/lost-yaml/`,
and `evals/fixtures/lost-toml/`.

HTML document leaf (HTML Tidy 5.8 quiet body-only XHTML emit) after XML/TOML.
Debian `tidy` 2:5.8.0-2 + `libtidy58` apt-installed this leaf —
**Apt Worthy Spend ~252 kB** archives (~1198 kB disk); still prefer over deferred
TeXlive / C++ / openjdk / graphviz multi-dep apt. Fossils `*.html` / `*.htm`.
Treats HTML as peer fossil not house twin language (same honesty as XML / YAML leaves).

## Artifacts

| File | Role |
|------|------|
| `HELLO.html` | Minimal HTML5; `tidy -q -utf8 --show-body-only yes -asxml HELLO.html` emits body containing `EMPEROR-TIME-TIDY-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until tidy run)

Era labels (HTML5 vs XHTML vs HTML4)
stay CONJECTURE until a processor run + manual pin lands. This fixture's
probe is the lander. prettier / jsoup / html5lib are not the verified toolchain.
