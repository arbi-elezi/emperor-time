# Jail pin — rustc Basic usage (`rustc FILE`) for HELLO.rs

Contemporaneous manual pin for the lost-rust archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how Rust
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-rust/HELLO.rs` with
runnable dialect **VERIFIED** as Rust 1.85.1
under Linux x86_64
(`rustc HELLO.rs` → `./HELLO` →
`EMPEROR-TIME-RUST-PROBE-OK`). Filename culture
(`.RS` / 8.3 caps → Rust source *naming*) remains **CONJECTURE** only.
Identify fossils use `*.rs` only. Bare `rust` is **allowed** as a
route tag (language name; word-boundary). Bare `.rs` is **allowed** as a route tag (no known peer
excavate substring collision). Prefer `rust` / `rustc` / `rust1.85` / `.rs`.
Debian package `rustc` (1.85.1+dfsg1-1+deb13u1) provides `/usr/bin/rustc`.
This note supplies the Jail pin so excavate
can name the **verified** Rust compile-and-run shape
without inventing a full Cargo workspace / edition / async / unsafe
suite claim for a `println!` probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *The rustc book* — What is rustc? / Basic usage |
| **Heading** | **Basic usage** — `rustc hello.rs` then `./hello` (*NIX); crate root only; `fn main` + `println!` |
| **Dialect pinned** | **Rust via rustc 1.85** with `fn main` + `println!` compile-then-run surface — **not** full Cargo / edition / async / unsafe suite claim |
| **URL** | https://doc.rust-lang.org/rustc/what-is-rustc.html (The rustc book — What is rustc? / Basic usage); package `rustc` 1.85.1+dfsg1-1+deb13u1 on Debian trixie; installed `rustc --version` |
| **Anchors** | `rustc` compiles named crate root; `.rs` source file; `println!` for string output; binary run after compile; Cargo optional (not required for this probe) |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from The rustc book — What is rustc? / Basic usage)

> **Basic usage**
>
> Let's say you've got a little hello world program in a file `hello.rs`:
>
> ```rust
> fn main() {
>     println!("Hello, world!");
> }
> ```
>
> To turn this source code into an executable, you can use `rustc`:
>
> ```bash
> $ rustc hello.rs
> $ ./hello # on a *NIX
> $ .\hello.exe # on Windows
> ```

(Source: The rustc book, What is rustc?, section **Basic usage**,
https://doc.rust-lang.org/rustc/what-is-rustc.html
accessed 2026-09-28 Europe/Tirane.
Installed `rustc --version` reports 1.85.1 and matches the
compile-then-run surface. Probe uses `rustc HELLO.rs` then `./HELLO`
so rustc compiles the crate root and the binary prints the probe string.
Language: Rust — see https://www.rust-lang.org/.)

### Why this heading (HELLO.rs / excavate)

A minimal HELLO surface looks like:

```rust
fn main() {
    println!("EMPEROR-TIME-RUST-PROBE-OK");
}
```

in a `.RS` / `.rs` file. That is exactly the pinned form:
**`rustc FILE`** then run the produced binary, observe string print at run time.
Pinning rustc Basic usage lets excavate treat `rust` /
`rustc` / `rust1.85` / `.rs` + `println!` as **era evidence** (Rust / Rust source
file) without rewriting the fixture into a shell one-liner, a Python
port, or an interactive `cargo` REPL. Identify surveys `*.rs` fossils on
disk. `.rs` extension and `rust` / `rustc` / `rust1.85` tags cover excavate intent.
