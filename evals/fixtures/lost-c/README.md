# lost-c fixture

Synthetic lost C tree for Emperor Time archaeology drills.

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
`evals/fixtures/lost-ruby/`, `evals/fixtures/lost-go/`, and
`evals/fixtures/lost-rust/`.

Systems / compile-and-run leaf (GNU C / gcc toolchain) after Rust.
Already installed on the box (gcc 14.2.0) — Worthy Spend vs
deferred TeXlive.

## Artifacts

| File | Role |
|------|------|
| `HELLO.c` | C source (lowercase `.c` required; uppercase `.C` is C++ per GCC); `gcc HELLO.c -o HELLO` then `./HELLO` prints `EMPEROR-TIME-C-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a C toolchain runs)

Era labels (K&R vs ANSI C89 vs C99/C11/C17) stay CONJECTURE until a
compiler run + manual pin lands. This fixture's probe is the lander.
