# Jail pin — GNU ed Invoking ed / `-s` / `--script` (HELLO.ED)

Contemporaneous manual pin for the lost-ed archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how ed
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-ed/HELLO.ED` with
runnable dialect **VERIFIED** as GNU ed 1.21.1
under Linux x86_64
(`ed -s < HELLO.ED` →
`EMPEROR-TIME-ED-PROBE-OK`). Filename culture
(`.ED` / 8.3 caps → ed script *naming*) remains **CONJECTURE** only.
Identify fossils use `*.ed` only. Bare `ed` is allowed as a
route tag (tool binary name — not an English collision like
`scheme` / `basic`, and not a two-letter collision like refused bare
`gs`). This note supplies the Jail pin so excavate
can name the **verified** ed script-mode stdin shape
without inventing a full POSIX ed / BSD ed / Plan 9 ed
suite claim for an `a`/`,p`/`Q` probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *GNU ed* — Invoking ed / Options `-s` / `--script` |
| **Heading** | **Invoking ed** — `-s`, `--script` — suppress byte counts; useful when standard input is from a script |
| **Dialect pinned** | **ed via GNU ed** with `a`/`,p`/`Q` surface — **not** full POSIX ed / BSD ed / Plan 9 ed suite claim |
| **URL** | https://www.gnu.org/software/ed/manual/ed_manual.html (Invoking ed); package `ed` 1.21.1-1 on Debian trixie; source texinfo `doc/ed.texi` from `ed-1.21.1.tar.lz` (GNU ftp mirror); man page https://manpages.debian.org/trixie/ed/ed.1.en.html |
| **Anchors** | `-s` / `--script` suppress byte counts; may be useful if ed's standard input is from a script; commands read from stdin |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from GNU ed Invoking ed / installed `ed --help`)

> `-s`, `--script`
> Suppress the printing of byte counts by `e`, `E`, `r`, and
> `w` commands, and the `!` prompt after a `!` command.
> Suppress also the messages "Newline inserted" and "Newline appended". This
> option does not suppress diagnostic messages written to standard error (see
> `-q` above). `-s` may be useful if `ed`'s standard
> input is from a script.

(Source: GNU ed 1.21.1 texinfo `doc/ed.texi` node **Invoking ed**,
item `-s` / `--script`, from upstream tarball `ed-1.21.1.tar.lz`
(https://ftp.gnu.org/gnu/ed/ / mirror), accessed 2026-09-28
Europe/Tirane. HTML manual at
https://www.gnu.org/software/ed/manual/ed_manual.html .
Installed `ed --help` on GNU ed 1.21.1 matches:
`-s, --script  suppress byte counts and '!' prompt`.
Probe uses `ed -s < HELLO.ED` so the editor reads commands from the
script on stdin non-interactively without byte-count noise.
`a` / text / `.` / `,p` / `Q` appends one line, prints the buffer, and quits.)

### Why this heading (HELLO.ED / excavate)

A minimal HELLO surface looks like:

```ed
a
EMPEROR-TIME-ED-PROBE-OK
.
,p
Q
```

in a `.ED` / `.ed` file. That is exactly the pinned form:
**`ed -s < FILE`** reads editing commands from the named script on
stdin, observe append/print at run time. Pinning Invoking ed /
`-s` / `--script` lets excavate treat `ed` / `gnu-ed` / `.ed` +
`a`/`,p`/`Q` as **era evidence** (GNU ed / ed script
file) without rewriting the fixture into a shell one-liner,
a Python port, or an interactive tty session.

**Dialect precision:** this pin authorizes GNU ed reading of
the `a`/`,p`/`Q` / script-mode stdin shape only. It does
**not** claim the lost tree is POSIX ed, BSD ed, or Plan 9 ed
on this host. Those are other manuals /
toolchains. HELLO's "gnu-ed-ish / append-print subset" label remains
**CONJECTURE** until a dialect-specific vendor run is evidence — GNU ed
accepting the `a`/`,p`/`Q` shape and printing the probe string is the
VERIFIED claim for this leaf.
