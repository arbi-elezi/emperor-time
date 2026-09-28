# lost-xsl fixture

Synthetic lost XSLT stylesheet tree for Emperor Time archaeology drills.

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
and `evals/fixtures/lost-jq/`.

XML/XSLT transform leaf (`xsltproc` stylesheet + XML) after jq.
Debian `xsltproc` 1.1.35 apt-installed this leaf —
Worthy Spend (115 kB archive; Installed-Size 151 kB; libxslt1.1 already present) after jq; still prefer over deferred
TeXlive / C++ / openjdk apt. Fossils `*.xsl` / `*.xslt` only (not bare `*.xml`).
Treats XSLT as peer fossil not house twin language (same honesty as jq / SQL leaves).

## Artifacts

| File | Role |
|------|------|
| `HELLO.xsl` | XSLT 1.0 stylesheet (lowercase `.xsl`); `xsltproc HELLO.xsl HELLO.xml` prints `EMPEROR-TIME-XSLT-PROBE-OK` |
| `HELLO.xml` | Minimal companion XML input (not an identify fossil) |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until xsltproc run)

Era labels (XSLT 1.0 / libxslt vs Saxon / Xalan / XSLT 2.0+)
stay CONJECTURE until a processor run + manual pin lands. This fixture's
probe is the lander. Saxon / Xalan is not the verified toolchain.
