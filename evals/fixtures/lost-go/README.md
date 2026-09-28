# lost-go fixture

Synthetic lost Go tree for Emperor Time archaeology drills.

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
and `evals/fixtures/lost-ruby/`.

Systems / compile-and-run leaf (Go toolchain) after Ruby scripting.
Already installed on the box (golang-go / go1.24.4) — Worthy Spend vs
deferred TeXlive.

## Artifacts

| File | Role |
|------|------|
| `HELLO.go` | Go source (lowercase `.go` required on case-sensitive hosts); `go run HELLO.go` prints `EMPEROR-TIME-GO-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a Go toolchain runs)

**Named era+dialect from evidence alone:**

- Extension `.go` (lowercase required by gc on case-sensitive hosts) → Go source file culture
  (gc / other Go consumers of the same `package main` surface).
- Source uses only package main + fmt.Println — dialect-honest (Println
  probe, not a full modules / workspace / cgo claim).
- No tradenames beyond the filename culture — deliberately minimal.
- Fossils deliberately use `*.go` only. Prefer `golang` /
  `go1.24` / `.go`. Bare `go` refused (common English).

Until `go` / another Go toolchain runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python or shell. Understanding is a running Go
system. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-go
# or: bash scripts/identify.sh evals/fixtures/lost-go
```
