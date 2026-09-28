# Jail pin — GNU M4 Invoking m4 / Command line files (HELLO.M4)

Contemporaneous manual pin for the lost-m4 archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how m4
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-m4/HELLO.M4` with
runnable dialect **VERIFIED** as GNU M4 1.4.19
under Linux x86_64
(`m4 HELLO.M4` →
`EMPEROR-TIME-M4-PROBE-OK`). Filename culture
(`.M4` / 8.3 caps → m4 *naming*) remains **CONJECTURE** only.
Identify fossils use `*.m4` only. Bare `m4` is allowed as a
route tag (tool binary name — not an English collision like
`scheme` / `basic`, and not a two-letter collision like refused bare
`gs`). This note supplies the Jail pin so excavate
can name the **verified** m4 FILE-argument shape
without inventing a full POSIX m4 / traditional AT&T m4 / Autoconf
suite claim for a `define`/`dnl` probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *GNU M4 macro processor* — Invoking m4 / Command line files |
| **Heading** | **2.6 Specifying input files on the command line** — remaining args are input file names |
| **Dialect pinned** | **m4 via GNU m4** with `define`/`dnl` surface — **not** full POSIX m4 / traditional AT&T m4 / Autoconf suite claim |
| **URL** | https://www.gnu.org/software/m4/manual/html_node/Command-line-files.html (Command line files — FILE args); package `m4` 1.4.19-8 on Debian trixie; Invoking m4 TOC confirmed at https://www.gnu.org/software/m4/manual/html_node/Invoking-m4.html |
| **Anchors** | remaining command-line arguments are taken to be input file names; conventional for input files to end in `.m4` |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from GNU M4 Command line files / installed `m4 --help`)

> The remaining arguments on the command line are taken to be input file
> names. If no names are present, standard input is read. A file
> name of `-` is taken to mean standard input. It is
> conventional, but not required, for input files to end in `.m4`.

(Source: GNU M4 1.4.20 manual §2.6 Specifying input files on the command
line at
https://www.gnu.org/software/m4/manual/html_node/Command-line-files.html ,
accessed 2026-09-28 Europe/Tirane. Invoking m4 chapter TOC lists
Command line files under Invoking m4. Installed `m4 --help` on GNU M4
1.4.19 matches: `Usage: m4 [OPTION]... [FILE]...` /
`Process macros in FILEs`. Probe uses
`m4 HELLO.M4` so the processor loads the named input file and expands
macros non-interactively.
`define(\`HELLO',\`…')dnl` + bare `HELLO` expands to the probe string.)

### Why this heading (HELLO.M4 / excavate)

A minimal HELLO surface looks like:

```m4
define(`HELLO',`EMPEROR-TIME-M4-PROBE-OK')dnl
HELLO
```

in a `.M4` / `.m4` file. That is exactly the pinned form:
**`m4 FILE`** reads and expands the named input file,
observe define/expansion at run time. Pinning Invoking m4 / Command
line files lets excavate treat `m4` / `gm4` / `.m4` + `define`/`dnl` as
**era evidence** (GNU m4 / m4 macro
file) without rewriting the fixture into a shell one-liner,
a Python port, or an Autoconf configure.ac.

**Dialect precision:** this pin authorizes GNU m4 reading of
the `define`/`dnl` / FILE-argument shape only. It does
**not** claim the lost tree is POSIX m4, traditional AT&T m4, or the
Autoconf suite on this host. Those are other manuals /
toolchains. HELLO's "gm4-ish / define subset" label remains
**CONJECTURE** until a dialect-specific vendor run is evidence — GNU m4
accepting the `define`/`dnl` shape and printing the probe string is the
VERIFIED claim for this leaf.
