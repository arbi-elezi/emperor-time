# Jail pin — GNU flex SYNOPSIS / FILE arguments + FILES `-o` / `--outfile` (HELLO.L)

Contemporaneous manual pin for the lost-lex archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how lex
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-lex/HELLO.L` with
runnable dialect **VERIFIED** as GNU flex 2.6.4
under Linux x86_64
(`flex HELLO.L` → `lex.yy.c` → `gcc -o hello lex.yy.c -lfl` /
`flex -o hello.c HELLO.L && gcc -o hello hello.c -lfl` →
`EMPEROR-TIME-LEX-PROBE-OK`). Filename culture
(`.L` / 8.3 caps → lex input *naming*) remains **CONJECTURE** only.
Identify fossils use `*.l` and `*.lex`. Bare `lex` / `flex` are allowed as
route tags (tool binary names — not English collisions like
`scheme` / `basic`, and not a factory collision like refused bare
`make`). Bare `.l` is refused as a route tag (short-extension collision
with `.lisp`). This note supplies the Jail pin so excavate
can name the **verified** flex file-input shape
without inventing a full AT&T lex / POSIX lex / Flex++
suite claim for a compile-link print probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *flex(1)* — SYNOPSIS FILE arguments / FILES `-o` / `--outfile` |
| **Heading** | **SYNOPSIS** — `flex [OPTIONS] [FILE]...`; **FILES** `-o` / `--outfile=FILE` |
| **Dialect pinned** | **lex via GNU flex** with FILE input → `lex.yy.c` (or `-o`) surface — **not** full AT&T lex / POSIX lex / Flex++ suite claim |
| **URL** | https://manpages.debian.org/trixie/flex/flex.1.en.html (flex(1)); package `flex` 2.6.4-8.2+b4 on Debian trixie; Flex Project upstream; installed `flex --help` |
| **Anchors** | positional FILE… are lex inputs; default scanner output `lex.yy.c`; `-o` / `--outfile` name the C output |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Debian trixie flex(1) SYNOPSIS / FILES)

> **SYNOPSIS**
> `flex [OPTIONS] [FILE]...`

> **NAME**
> flex - the fast lexical analyser generator

> **FILES**
> `-o, --outfile=FILE` — specify output filename
> `-t, --stdout` — write scanner on stdout instead of lex.yy.c

(Source: Debian manpages for package `flex` 2.6.4-8.2+b4 on trixie,
https://manpages.debian.org/trixie/flex/flex.1.en.html sections
**SYNOPSIS**, **NAME**, and **FILES**, accessed 2026-09-28 Europe/Tirane.
Installed `flex --help` on GNU flex 2.6.4 matches:
`Usage: flex [OPTIONS] [FILE]...` and
`-o, --outfile=FILE  specify output filename`.
Probe uses `flex HELLO.L` so the generator reads the named lex input
and writes `lex.yy.c`, then `gcc -o hello lex.yy.c -lfl` links the
scanner; alternate VERIFIED form `flex -o hello.c HELLO.L`.
Debian ships `/usr/bin/lex` as a symlink to `flex`.)

### Why this heading (HELLO.L / excavate)

A minimal HELLO surface looks like a `%{ … %}` / `%%` lex input in a
`.L` / `.l` / `.lex` file whose generated C `main` prints the probe
string. That is exactly the pinned form:
**`flex FILE`** (optionally **`flex -o OUT FILE`**) reads lex rules
from the named input, observe compile-link print at run time. Pinning
SYNOPSIS FILE arguments + FILES `-o` / `--outfile` lets excavate treat
`lex` / `flex` / `gnu-flex` / `.lex` + flex file input as **era evidence**
(GNU flex / lex input file) without rewriting the fixture into a shell
one-liner, a Python port, or an interactive scanner session.

**Dialect precision:** this pin authorizes GNU flex reading of
the lex-input / compile-link shape only. It does
**not** claim the lost tree is AT&T lex, POSIX lex, or Flex++
on this host. Those are other manuals /
toolchains. HELLO's "gnu-flex-ish / lex-input subset" label remains
**CONJECTURE** until a dialect-specific vendor run is evidence — GNU flex
accepting the FILE input shape and the linked binary printing the probe
string is the VERIFIED claim for this leaf.
