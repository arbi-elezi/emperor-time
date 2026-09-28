# Jail pin — xsltproc SYNOPSIS (stylesheet + XML-FILE) for HELLO.xsl

Contemporaneous manual pin for the lost-xsl archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how XSLT
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-xsl/HELLO.xsl` with
runnable dialect **VERIFIED** as xsltproc (libxslt 1.1)
under Linux x86_64
(`xsltproc HELLO.xsl HELLO.xml` →
`EMPEROR-TIME-XSLT-PROBE-OK`). Filename culture
(`.xslt` / XSLT 2.0+ / Saxon) remains
**CONJECTURE** only for naming collisions. Identify fossils use `*.xsl` /
`*.xslt` only (not bare `*.xml`).
Bare `xslt` is **allowed** as a route tag (language / tool family name).
Bare `xsltproc` / `libxslt` are **allowed** as route tags (tool / library).
Bare `.xsl` / `.xslt` are **allowed** as route tags with
extension-boundary matching (`.xsl` does not alone prefix-hit `.xslt` —
both listed). Prefer `xsltproc` /
`libxslt` / `xslt` / `.xsl` / `.xslt`.
Toolchain is Debian package `xsltproc` 1.1.35-1.2+deb13u3 providing
`/usr/bin/xsltproc`. This note supplies
the Jail pin so excavate can name the **verified** xsltproc
stylesheet+xml evaluation shape without inventing a full Saxon /
Xalan / MSXML / XSLT 2.0+ suite claim for a
text-output probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *xsltproc(1) — Name / Synopsis / Description* |
| **Heading** | **Synopsis** — `xsltproc` [`OPTIONS`] [`STYLESHEET`] { `XML-FILE`... \| - } applies stylesheet to XML documents |
| **Dialect pinned** | **xsltproc / libxslt 1.1 XSLT 1.0** with text-output stylesheet → `xsltproc FILE.xsl FILE.xml` — **not** full Saxon / Xalan / XSLT 2.0+ suite claim |
| **URL** | https://gnome.pages.gitlab.gnome.org/libxslt/xsltproc.html (xsltproc man page — Name / Synopsis / Description); Debian package `xsltproc` 1.1.35-1.2+deb13u3; installed `xsltproc -V` |
| **Anchors** | `.xsl` / `.xslt` stylesheet path as first file argument; companion XML document; default output to stdout |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from xsltproc man page — Name / Synopsis / Description)

> xsltproc — command line XSLT processor
>
> `xsltproc` [[options…]] [`STYLESHEET`] { `XML-FILE`... | - }
>
> xsltproc is a command line tool for applying XSLT stylesheets to XML
> documents. It is part of libxslt(3), the XSLT C library for GNOME.
>
> xsltproc is invoked from the command line with the name of the
> stylesheet to be used followed by the name of the file or files to
> which the stylesheet is to be applied. It will use the standard input
> if a filename provided is - .
>
> By default, output is to `stdout`.

(Source: xsltproc man page / GNOME libxslt documentation, sections
**Name**, **Synopsis**, **Description**,
https://gnome.pages.gitlab.gnome.org/libxslt/xsltproc.html
accessed 2026-09-28 Europe/Tirane.
Installed `xsltproc -V` reports libxslt 10135 and matches the
CLI stylesheet+xml surface. Probe uses
`xsltproc HELLO.xsl HELLO.xml` so xsltproc
loads and runs the named stylesheet against the companion XML
non-interactively and prints the probe
string. Language: XSLT — see also libxslt(3).)

### Why this heading (HELLO.xsl / excavate)

A minimal HELLO surface looks like an XSLT 1.0 stylesheet with
`xsl:output method="text"` emitting a probe string, plus a tiny
companion XML root. That is exactly the pinned form:
**`xsltproc FILE.xsl FILE.xml`**, observe string print at run time.

### Honesty

- VERIFIED: Debian `xsltproc` 1.1.35 on this HELLO.
- CONJECTURE: any claim that `.xslt` / Saxon / XSLT 2.0+ are this dialect.
- UNVERIFIABLE: Saxon / Xalan / MSXML / XSLT 2.0+ recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, openjdk/Java (apt size); bare `*.xml` fossil; yq this turn (larger dep surface vs xsltproc one-package).
