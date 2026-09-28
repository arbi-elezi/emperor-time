# lost-xml fixture

Synthetic lost XML document tree for Emperor Time archaeology drills.

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
`evals/fixtures/lost-jq/`, and `evals/fixtures/lost-xsl/`.

XML document leaf (`xmllint` well-formed parse + XPath string) after XSLT.
Debian `libxml2-utils` 2.12.7 apt-installed this leaf —
Worthy Spend (101 kB archive; Installed-Size 181 kB; libxml2 already present) after XSLT; still prefer over deferred
TeXlive / C++ / openjdk / graphviz multi-dep apt. Fossils `*.xml`
(XSLT leaf still owns `*.xsl` / `*.xslt` only; bare `*.xml` was rejected there
as too broad for stylesheets, and is intentional here as the XML peer fossil).
Treats XML as peer fossil not house twin language (same honesty as XSLT / jq leaves).

## Artifacts

| File | Role |
|------|------|
| `HELLO.xml` | Minimal well-formed XML; `xmllint --xpath 'string(/probe)' HELLO.xml` prints `EMPEROR-TIME-XML-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until xmllint run)

Era labels (plain XML 1.0 vs XSD / RelaxNG / HTML / DocBook)
stay CONJECTURE until a processor run + manual pin lands. This fixture's
probe is the lander. xmlstarlet / Saxon is not the verified toolchain.
