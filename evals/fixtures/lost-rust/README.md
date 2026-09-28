# lost-rust fixture

Synthetic lost Rust tree for Emperor Time archaeology drills.

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
`evals/fixtures/lost-ruby/`, and `evals/fixtures/lost-go/`.

Systems / compile-and-run leaf (Rust rustc toolchain) after Go.
Already installed on the box (rustc 1.85.1) — Worthy Spend vs
deferred TeXlive.

## Artifacts

| File | Role |
|------|------|
| `HELLO.rs` | Rust source (lowercase `.rs` required on case-sensitive hosts); `rustc HELLO.rs` then `./HELLO` prints `EMPEROR-TIME-RUST-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a Rust toolchain runs)

**Named era+dialect from evidence alone:**

- Extension `.rs` (lowercase required by rustc on case-sensitive hosts) → Rust source file culture
  (rustc / other Rust consumers of the same `fn main` + `println!` surface).
- Source uses only fn main + println! — dialect-honest (println!
  probe, not a full Cargo / edition / async / unsafe claim).
- No tradenames beyond the filename culture — deliberately minimal.
- Fossils deliberately use `*.rs` only. Prefer `rust` /
  `rustc` / `rust1.85` / `.rs`. Bare `rust` allowed (language / tool name; word-boundary).

Until `rustc` / another Rust toolchain runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python or shell. Understanding is a running Rust
system. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-rust
# or: bash scripts/identify.sh evals/fixtures/lost-rust
```
