# lost-yaml fixture

Synthetic lost YAML document tree for Emperor Time archaeology drills.

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
and `evals/fixtures/lost-xml/`.

YAML document leaf (kislyuk/yq YAML→JSON→jq filter + raw string) after jq/XML.
Debian `yq` 3.4.3-2 apt-installed this leaf (with python3-yaml and siblings) —
Worthy Spend (~267 kB archive; Installed-Size sum ~1063 kB; jq already present) after XML; still prefer over deferred
TeXlive / C++ / openjdk / graphviz multi-dep apt. Fossils `*.yaml` / `*.yml`.
Treats YAML as peer fossil not house twin language (same honesty as jq / XML leaves).

## Artifacts

| File | Role |
|------|------|
| `HELLO.yaml` | Minimal YAML mapping; `yq -r .probe HELLO.yaml` prints `EMPEROR-TIME-YQ-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until yq run)

Era labels (plain YAML 1.1 vs Kubernetes / Ansible / CloudFormation)
stay CONJECTURE until a processor run + manual pin lands. This fixture's
probe is the lander. mikefarah/yq (Go) is not the verified toolchain.
