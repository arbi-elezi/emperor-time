# Jail pin — HTML Tidy documentation Running Tidy / CLI for HELLO.html

Contemporaneous manual pin for the lost-html archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how HTML
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-html/HELLO.html` with
runnable dialect **VERIFIED** as HTML Tidy 5.8.0
under Linux x86_64
(`tidy -q -utf8 --show-body-only yes -asxml HELLO.html` →
body containing `EMPEROR-TIME-TIDY-PROBE-OK`). Filename culture
(XHTML / HTML4 / polyglot / AMP) remains
**CONJECTURE** only for naming collisions. Identify fossils use `*.html` / `*.htm`.
Bare `html` is **allowed** as a route tag (language name).
Bare `tidy` / `html-tidy` / `tidy5.8` are **allowed** as route tags (tool / family / version).
Bare `.html` / `.htm` are **allowed** as route tags with
extension-boundary matching. Prefer `tidy` /
`html-tidy` / `tidy5.8` / `html` / `.html` / `.htm`.
Toolchain is Debian packages `tidy` 2:5.8.0-2 + `libtidy58` 2:5.8.0-2 providing
`/usr/bin/tidy`. This note supplies
the Jail pin so excavate can name the **verified** HTML Tidy
HTML parse + quiet body-only XHTML emit shape without inventing a full
HTML5 / WHATWG / CSS / browser suite claim for a
pretty-print probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *HTML Tidy documentation — Running Tidy in a Terminal (Console)* |
| **Heading** | **Running Tidy in a Terminal (Console)** — `tidy [[options] filename]` reads HTML, writes cleaned markup to stdout; `-q` quiet; `-asxml` / `-asxhtml` convert HTML to well formed XHTML; `--show-body-only yes` emits body content |
| **Dialect pinned** | **HTML Tidy 5.8 CLI** with HTML→XHTML quiet body-only emit → `tidy -q -utf8 --show-body-only yes -asxml FILE.html` — **not** full HTML5 / WHATWG / CSS / browser suite claim |
| **URL** | https://www.html-tidy.org/documentation/ (HTML Tidy documentation — Running Tidy in a Terminal); Debian packages `tidy` / `libtidy58` 2:5.8.0-2; installed `tidy --version` |
| **Anchors** | `.html` / `.htm` document path as file argument; `-q` quiet; `-asxml` XHTML emit; `--show-body-only yes` body-only |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from HTML Tidy documentation — Running Tidy in a Terminal)

> This is the syntax for invoking Tidy from the command line:
>
> `tidy [[options] filename]`
>
> Tidy defaults to reading from standard input, so if you run Tidy without
> specifying the `filename` argument, it will just sit there waiting for
> input to read.
>
> Tidy defaults to writing to standard output. So you can pipe output from
> Tidy to other programs, as well as pipe output from other programs to Tidy.

(Source: HTML Tidy documentation, section
**Running Tidy in a Terminal (Console)**,
https://www.html-tidy.org/documentation/
accessed 2026-09-28 Europe/Tirane.
Installed `tidy --version` reports HTML Tidy for Linux version 5.8.0 and matches the
CLI clean+pretty-print surface. Probe uses
`tidy -q -utf8 --show-body-only yes -asxml HELLO.html` so tidy
loads the named HTML document, emits quiet body-only XHTML, and preserves the probe
token in stdout. Language: HTML — see also tidy `-help` Processing directives
`-asxml` / `-asxhtml` / `-quiet`.)

### Why this heading (HELLO.html / excavate)

A minimal HELLO surface looks like an HTML5 document with a
single text node under `<p id="probe">`. That is exactly the pinned form:
**`tidy -q -utf8 --show-body-only yes -asxml FILE.html`**, observe body emit with probe token at run time.

### Honesty

- VERIFIED: Debian `tidy` (5.8.0-2) on this HELLO.
- CONJECTURE: any claim that XHTML / HTML4 / polyglot / AMP are this dialect.
- UNVERIFIABLE: HTML5 / WHATWG / CSS / browser recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, openjdk/Java (apt size); graphviz this turn (multi-dep); csvkit/CSV this turn (separate peer); bare `html5` / `prettier` / `jsoup` as verified toolchain.
