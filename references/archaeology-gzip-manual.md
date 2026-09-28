# Jail pin — Python gzip.open/read for HELLO.gz

Contemporaneous manual pin for the lost-gz archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how gzip
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-gz/HELLO.gz` with
runnable dialect **VERIFIED** as CPython 3.13.5 stdlib `gzip`
under Linux x86_64
(`python3` + `gzip.open`/read on HELLO.gz → payload
yields `EMPEROR-TIME-GZIP-PROBE-OK`). Filename culture
(`.tar.gz` / `.tgz` / multi-member / concatenated gzip)
remains **CONJECTURE** only for naming collisions. Identify fossils use `*.gz`.
Bare `gzip` / `pygzip` / `gzipfile` are **allowed** as route tags (format / family / module).
Bare `.gz` is **allowed** as a route tag with
extension-boundary matching. Prefer `gzip` /
`pygzip` / `gzipfile` / `.gz`.
A `.gz` suffix match may fire excavate on `file.tar.gz` as a gzip-compressed
utterance without claiming compressed-TAR ownership; do **not** add `*.tar.gz`
fossils this leaf.
Toolchain is CPython stdlib `gzip` already on box (**zero new apt**).
Debian `gzip` 1.13-1+deb13u1 (Installed-Size ~256 kB; already on box) was considered and **REJECTED**
as the verified leaf owner vs stdlib. This note supplies
the Jail pin so excavate can name the **verified** stdlib `gzip`
open/read shape without inventing a full
GNU gzip / multi-member / concatenated suite claim for a
single-member probe. Distinct from the tar archaeology leaf (`*.tar` /
tarfile), zip (`*.zip` / zipfile), eml (`*.eml` / email.parser), plist (`*.plist` / plistlib), JSON (`*.json` / json),
and CSV (`*.csv` / csv).

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Python 3 Library Reference — `gzip`: Support for gzip files* |
| **Heading** | **`gzip.open`** — Open a gzip-compressed file in binary or text mode |
| **Dialect pinned** | **CPython stdlib `gzip.open`/read** with payload → print token — **not** full GNU gzip / multi-member / concatenated / compressed-TAR suite claim |
| **URL** | https://docs.python.org/3/library/gzip.html (Python docs — `gzip`); CPython 3.13.5 on box |
| **Anchors** | `.gz` path; `gzip.open(path, 'rb')`; `.read()` |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Python docs — `gzip.open`)

> gzip.open(filename, mode='rb', compresslevel=9, encoding=None, errors=None, newline=None) — Open a gzip-compressed file in binary or text mode.
>
> The filename argument can be an actual filename (a str or bytes object), or an existing file object to read from or write to.
>
> The mode argument can be "r", "rb", "w", "wb", "x", "xb", "a" or "ab" for binary mode, or "rt", "wt", "xt" or "at" for text mode. The default mode is "rb", and the default compresslevel is 9.

(Source: Python 3 Library Reference, section
**gzip — Support for gzip files**,
https://docs.python.org/3/library/gzip.html
accessed 2026-09-28 Europe/Tirane.
Module intro: "This module provides a simple interface to compress and decompress files just like the GNU programs gzip and gunzip would."
Installed `python3 --version` reports Python 3.13.5.
Probe uses
`gzip.open('HELLO.gz', 'rb').read().decode().strip()`
so stdlib gzip loads the named `.gz` and prints the payload token.
Format: RFC 1952 gzip single-member compressed file.)

### Why this heading (HELLO.gz / excavate)

A minimal HELLO surface looks like a one-member gzip file with
a plaintext probe token. That is exactly the pinned form:
**stdlib `gzip.open`/read**, observe decompressed bytes at run time.

### Honesty

- VERIFIED: CPython 3.13.5 stdlib `gzip.open`/read on this HELLO (RFC 1952 gzip single-member).
- CONJECTURE: any claim that GNU gzip / multi-member / concatenated / compressed `.tar.gz` are this dialect.
- UNVERIFIABLE: Debian gzip / full multi-dialect archive recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, openjdk/Java (apt size); graphviz this turn (multi-dep); Debian `gzip` as verified leaf owner (stdlib owns); bare `gzip` apt/system as verified toolchain; `*.tar.gz` / `*.tgz` / `*.tar.bz2` / `*.tar.xz` / `*.jar` / `*.war` / `*.apk` / `*.whl` / `*.docx` / `*.xlsx` / `*.tsv` / `*.jsonl` fossils this leaf (defer).
