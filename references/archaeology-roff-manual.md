# Jail pin — GNU groff SYNOPSIS / file operands + Options `-T` / output-device (HELLO.ROFF)

Contemporaneous manual pin for the lost-roff archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how roff
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-roff/HELLO.ROFF` with
runnable dialect **VERIFIED** as GNU groff 1.23.0
under Linux x86_64
(`groff -Tascii HELLO.ROFF` →
`EMPEROR-TIME-ROFF-PROBE-OK`). Filename culture
(`.ROFF` / 8.3 caps → roff document *naming*) remains **CONJECTURE** only.
Identify fossils use `*.roff`. Bare `roff` / `nroff` / `groff` are allowed as
route tags (tool binary names — not English collisions like
`scheme` / `basic`, and not a factory collision like refused bare
`make`). This note supplies the Jail pin so excavate
can name the **verified** groff file-input + `-Tascii` shape
without inventing a full AT&T troff / Heirloom Doctools /
ms/me/mm/man macro suite claim for a terminal print probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *groff(1)* — SYNOPSIS file operands / Options `-T` / output-device |
| **Heading** | **SYNOPSIS** — `groff [OPTION]... [file ...]`; **Options** `-T output-device` |
| **Dialect pinned** | **roff via GNU groff** with file input → ASCII device surface — **not** full AT&T troff / Heirloom / ms/me/mm/man suite claim |
| **URL** | https://manpages.debian.org/trixie/groff-base/groff.1.en.html (groff(1)); package `groff` / `groff-base` 1.23.0-9 on Debian trixie; GNU groff upstream; installed `groff --help` |
| **Anchors** | positional `file ...` is roff input; `-T output-device` selects the output driver (`ascii` for terminal); default when omitted still formats files |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Debian trixie groff(1) SYNOPSIS / Description / Options)

> **SYNOPSIS**
> `groff [-abcCeEgGijklNpRsStUVXzZ] … [-T output-device] … [file …]`

> **NAME**
> groff - front end to the GNU roff document formatting system

> **DESCRIPTION**
> groff is the primary front end to the GNU roff document formatting
> system. GNU roff is a typesetting system that reads plain text input
> files that include formatting commands to produce output in PostScript,
> PDF, HTML, DVI, or other formats, or for display to a terminal.
> If no file operands are specified, or if file is “-”, groff reads
> the standard input stream.

(Source: Debian manpages for package `groff-base` 1.23.0-9 on trixie,
https://manpages.debian.org/trixie/groff-base/groff.1.en.html sections
**SYNOPSIS**, **NAME**, and **DESCRIPTION**, accessed
2026-09-28 Europe/Tirane.
Installed `groff --help` on GNU groff 1.23.0 matches:
`usage: groff [OPTION]... [file ...]` and
`-T output-device` among the option letters.
Probe uses `groff -Tascii HELLO.ROFF` so the formatter reads the named
roff input and writes ASCII terminal output containing the probe string.
Debian ships `/usr/bin/nroff` as the GNU nroff wrapper around groff.)

### Why this heading (HELLO.ROFF / excavate)

A minimal HELLO surface looks like roff requests (`.nf` / `.fi`) wrapping
a probe line in a `.ROFF` / `.roff` file. That is exactly the pinned form:
**`groff [file ...]`** (typically **`groff -Tascii FILE`**)
reads roff input from the named file, observe print at format time.
Pinning SYNOPSIS file operands + Options `-T` / output-device
lets excavate treat `roff` / `nroff` / `groff` / `gnu-groff` / `.roff` + groff
file input as **era evidence** (GNU groff / roff document file) without
rewriting the fixture into a Markdown one-liner, a Python port, or an
interactive typesetter session.

**Dialect precision:** this pin authorizes GNU groff reading of
the roff-document / `-Tascii` print shape only. It does
**not** claim the lost tree is AT&T troff, Heirloom Doctools, or a
specific ms/me/mm/man macro package on this host. Those are other manuals /
toolchains. HELLO's "gnu-groff-ish / roff-request subset" label remains
**CONJECTURE** until a dialect-specific vendor run is evidence — GNU groff
accepting the FILE input shape and printing the probe
string is the VERIFIED claim for this leaf.
