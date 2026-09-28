# Jail pin — GNU Bison SYNOPSIS / FILE arguments + Output Files `-o` / `--output` (HELLO.Y)

Contemporaneous manual pin for the lost-yacc archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how yacc
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-yacc/HELLO.Y` with
runnable dialect **VERIFIED** as GNU Bison 3.8.2
under Linux x86_64
(`bison -o hello.c HELLO.Y` → `gcc -o hello hello.c` /
`bison -y HELLO.Y` → `y.tab.c` → `gcc -o hello y.tab.c` →
`EMPEROR-TIME-YACC-PROBE-OK`). Filename culture
(`.Y` / 8.3 caps → yacc grammar *naming*) remains **CONJECTURE** only.
Identify fossils use `*.y`. Bare `yacc` / `bison` are allowed as
route tags (tool binary names — not English collisions like
`scheme` / `basic`, and not a factory collision like refused bare
`make`). This note supplies the Jail pin so excavate
can name the **verified** bison file-input shape
without inventing a full POSIX Yacc / Berkeley Yacc / Bison++
suite claim for a compile-link print probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *bison(1)* — SYNOPSIS FILE arguments / Output Files `-o` / `--output` |
| **Heading** | **SYNOPSIS** — `bison [OPTION]... FILE`; **Output Files** `-o` / `--output=FILE` |
| **Dialect pinned** | **yacc via GNU Bison** with FILE input → parser C (or `-o` / `-y`) surface — **not** full POSIX Yacc / Berkeley Yacc / Bison++ suite claim |
| **URL** | https://manpages.debian.org/trixie/bison/bison.1.en.html (bison(1)); package `bison` 2:3.8.2+dfsg-1+b2 on Debian trixie; GNU Bison upstream; installed `bison --help` |
| **Anchors** | positional FILE is the yacc grammar; default parser output uses input prefix (`.tab.c`); `-o` / `--output` name the C output; `-y` forces `y.tab.c` |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Debian trixie bison(1) SYNOPSIS / Output Files)

> **SYNOPSIS**
> `bison [OPTION]... FILE`

> **NAME**
> bison - GNU Project parser generator (yacc replacement)

> **DESCRIPTION**
> Bison is a parser generator in the style of yacc(1).
> It should be upwardly compatible with input files designed for yacc.
> Input files should follow the yacc convention of ending in `.y`.

> **Output Files**
> `-o, --output=FILE` — leave output to FILE
> `-b, --file-prefix=PREFIX` — specify a PREFIX for output files

(Source: Debian manpages for package `bison` 2:3.8.2+dfsg-1+b2 on trixie,
https://manpages.debian.org/trixie/bison/bison.1.en.html sections
**SYNOPSIS**, **NAME**, **DESCRIPTION**, and **Output Files**, accessed
2026-09-28 Europe/Tirane.
Installed `bison --help` on GNU Bison 3.8.2 matches:
`Usage: bison [OPTION]... FILE` and
`-o, --output=FILE             leave output to FILE`.
Probe uses `bison -o hello.c HELLO.Y` so the generator reads the named
yacc grammar and writes the named C output, then `gcc -o hello hello.c`
links the parser; alternate VERIFIED form `bison -y HELLO.Y` → `y.tab.c`.
Debian ships `/usr/bin/yacc` via update-alternatives to `bison.yacc`.)

### Why this heading (HELLO.Y / excavate)

A minimal HELLO surface looks like a `%{ … %}` / `%%` yacc grammar in a
`.Y` / `.y` file whose generated C `main` prints the probe
string. That is exactly the pinned form:
**`bison FILE`** (typically **`bison -o OUT FILE`** or **`bison -y FILE`**)
reads yacc rules from the named input, observe compile-link print at run
time. Pinning SYNOPSIS FILE arguments + Output Files `-o` / `--output`
lets excavate treat `yacc` / `bison` / `gnu-bison` / `.y` + bison file
input as **era evidence** (GNU Bison / yacc grammar file) without
rewriting the fixture into a shell one-liner, a Python port, or an
interactive parser session.

**Dialect precision:** this pin authorizes GNU Bison reading of
the yacc-grammar / compile-link shape only. It does
**not** claim the lost tree is POSIX Yacc, Berkeley Yacc, or Bison++
on this host. Those are other manuals /
toolchains. HELLO's "gnu-bison-ish / yacc-grammar subset" label remains
**CONJECTURE** until a dialect-specific vendor run is evidence — GNU Bison
accepting the FILE input shape and the linked binary printing the probe
string is the VERIFIED claim for this leaf.
