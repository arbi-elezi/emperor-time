# Boot probe — lost-rust / HELLO.rs

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~09:47 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **rustc** 1.85.1+dfsg1-1+deb13u1 |
| Binary | `/usr/bin/rustc` |
| Reported | `rustc 1.85.1 (4eb161250 2025-03-15)` (built from a source tarball) |
| Install | already present on box (no apt this leaf) |

Probe used compile-then-run
(`rustc HELLO.rs` → `./HELLO`)
on a minimal `fn main` / `println!` program. Identify fossils
use `*.rs` only. Rust on case-sensitive hosts requires a lowercase `.rs` extension (uppercase `.RS` is not treated as a Rust source file by default). Prefer `rust` / `rustc` / `rust1.85` / `.rs`. Bare `rust`
is **allowed** as a route tag (language name; word-boundary). Bare `.rs` is
**allowed** (no known substring collision with peer excavate fossils).
Do not claim a full Cargo workspace / edition / async / unsafe suite
recovery from a `println!` probe alone — this leaf pins Rust
compile-and-run via `rustc` + binary execution.

## Commands (VERIFIED)

```text
$ dpkg -l rustc | awk '/^ii/ {print $2, $3}'
rustc 1.85.1+dfsg1-1+deb13u1

$ rustc --version
rustc 1.85.1 (4eb161250 2025-03-15) (built from a source tarball)

$ which rustc
/usr/bin/rustc

$ rustc HELLO.rs
$ ./HELLO
EMPEROR-TIME-RUST-PROBE-OK
# (from evals/fixtures/lost-rust; also works: rustc evals/fixtures/lost-rust/HELLO.rs -o /tmp/hello && /tmp/hello from repo root)
# exit 0
```

Note: rustc Usage is
`rustc [OPTIONS] INPUT`.
Documented VERIFIED form is **`rustc HELLO.rs`** then run the produced
binary (`./HELLO` on *NIX). Long help:
Usage: rustc [OPTIONS] INPUT. The rustc book Basic usage shows
`rustc hello.rs` then `./hello`. `println!` is the standard-library
macro for string output.

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is Rust fossil named `HELLO.rs` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-rust` prints `1 *.rs` |
| Runs under rustc 1.85.1 compile-then-run | VERIFIED | `rustc HELLO.rs` + `./HELLO` exit 0 |
| Prints known string | VERIFIED | stdout contains `EMPEROR-TIME-RUST-PROBE-OK` |
| Dialect is a specific Cargo / edition / async claim | CONJECTURE | No Cargo.toml / edition flag / async jury beyond `println!` under rustc 1.85.1 |
| Would run under period Rust 1.0 / mrustc | UNVERIFIABLE here | No period Rust ROM in this session |
| Full Cargo workspace / edition / async / unsafe suite | UNVERIFIABLE here | single println! probe only |

## Not done (honest gaps)

- No Jail-hunt of the full Rust language reference beyond
  rustc Basic usage (`rustc FILE`) + `println!` (deferred; pin is
  **`rustc FILE` then run binary** — see `references/archaeology-rust-manual.md`).
- Bare `rust` allowed (language name); also `rustc` /
  `rust1.85` / `.rs`. Bare `.rs` allowed (no peer collision).
- No `Cargo.toml` / workspace fossil this leaf (Cargo out of
  scope for the println! probe).
