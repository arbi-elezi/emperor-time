# Jail pin — xmllint SYNOPSIS (XML-FILE + XPath) for HELLO.xml

Contemporaneous manual pin for the lost-xml archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how XML
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-xml/HELLO.xml` with
runnable dialect **VERIFIED** as xmllint (libxml2 2.9)
under Linux x86_64
(`xmllint --xpath 'string(/probe)' HELLO.xml` →
`EMPEROR-TIME-XML-PROBE-OK`). Filename culture
(XSD / RelaxNG / HTML / DocBook) remains
**CONJECTURE** only for naming collisions. Identify fossils use `*.xml`
(XML peer after XSLT; XSLT still owns `*.xsl` / `*.xslt` only).
Bare `xml` is **allowed** as a route tag (three-letter language abbreviation).
Bare `xmllint` / `libxml2` are **allowed** as route tags (tool / library).
Bare `.xml` is **allowed** as a route tag with
extension-boundary matching. Prefer `xmllint` /
`libxml2` / `xml` / `.xml`.
Toolchain is Debian package `libxml2-utils` 2.12.7+dfsg+really2.9.14-2.1+deb13u3 providing
`/usr/bin/xmllint`. This note supplies
the Jail pin so excavate can name the **verified** xmllint
well-formed parse + XPath string evaluation shape without inventing a full
XSD / RelaxNG / Schematron / HTML suite claim for a
string-output probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *xmllint(1) — Name / Synopsis / Description* |
| **Heading** | **Synopsis** — `xmllint` [`OPTIONS`] { `XML-FILE(S)`... \| - } parses XML documents; `--xpath` runs an XPath expression |
| **Dialect pinned** | **xmllint / libxml2 2.9 XML 1.0** with XPath string → `xmllint --xpath 'string(/probe)' FILE.xml` — **not** full XSD / RelaxNG / Schematron / HTML suite claim |
| **URL** | https://gnome.pages.gitlab.gnome.org/libxml2/xmllint.html (xmllint man page — Name / Synopsis / Description); Debian package `libxml2-utils` 2.12.7+dfsg+really2.9.14-2.1+deb13u3; installed `xmllint --version` |
| **Anchors** | `.xml` document path as file argument; `--xpath` expression; default result print to stdout |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from xmllint man page — Name / Synopsis / Description)

> xmllint — command line XML tool
>
> `xmllint` [[options…]] { `XML-FILE(S)`... | - }
>
> The xmllint program parses one or more XML files, specified on the
> command line as `XML-FILE` (or the standard input if the filename
> provided is - ). It prints various types of output, depending upon
> the options selected. It is useful for detecting errors both in XML
> code and in the XML parser itself.
>
> xmllint is part of the libxml2 library.
>
> `--xpath "XPath_expression"` — Run an XPath expression given as
> argument and print the result.

(Source: xmllint man page / GNOME libxml2 documentation, sections
**Name**, **Synopsis**, **Description**, **DEBUG OPTIONS** (`--xpath`),
https://gnome.pages.gitlab.gnome.org/libxml2/xmllint.html
accessed 2026-09-28 Europe/Tirane.
Installed `xmllint --version` reports libxml 20914 and matches the
CLI parse+xpath surface. Probe uses
`xmllint --xpath 'string(/probe)' HELLO.xml` so xmllint
loads and evaluates the named document
non-interactively and prints the probe
string. Language: XML — see also libxml(3).)

### Why this heading (HELLO.xml / excavate)

A minimal HELLO surface looks like a well-formed XML document with a
single text node under `/probe`. That is exactly the pinned form:
**`xmllint --xpath 'string(/probe)' FILE.xml`**, observe string print at run time.

### Honesty

- VERIFIED: Debian `xmllint` (libxml2-utils 2.12.7) on this HELLO.
- CONJECTURE: any claim that XSD / RelaxNG / HTML / DocBook are this dialect.
- UNVERIFIABLE: XSD / RelaxNG / Schematron / HTML recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, openjdk/Java (apt size); graphviz this turn (multi-dep vs xmllint one-package); xmlstarlet this turn (larger than xmllint); bare `xmlstarlet` / `saxon` as verified toolchain.
