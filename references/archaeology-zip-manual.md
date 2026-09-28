# Jail pin — Python zipfile.ZipFile.namelist/read for HELLO.zip

Contemporaneous manual pin for the lost-zip archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how zip
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-zip/HELLO.zip` with
runnable dialect **VERIFIED** as CPython 3.13.5 stdlib `zipfile`
under Linux x86_64
(`python3` + `ZipFile.namelist`/`read` on HELLO.zip → member
`PROBE.txt` yields `EMPEROR-TIME-ZIP-PROBE-OK`). Filename culture
(JAR / WAR / APK / wheel / Office Open XML)
remains **CONJECTURE** only for naming collisions. Identify fossils use `*.zip`.
Bare `zip` / `pyzip` / `zipfile` are **allowed** as route tags (format / family / module).
Bare `.zip` is **allowed** as a route tag with
extension-boundary matching. Prefer `zip` /
`pyzip` / `zipfile` / `.zip`.
Toolchain is CPython stdlib `zipfile` already on box (**zero new apt**).
Debian `unzip` 6.0-29+deb13u1 apt was simulated (~387 kB Installed-Size) and **REJECTED**;
Debian `zip` 3.0-15+deb13u1 (~627 kB Installed-Size) also **REJECTED**. This note supplies
the Jail pin so excavate can name the **verified** stdlib `zipfile`
namelist/read shape without inventing a full
unzip / zip / encryption / multi-volume suite claim for a
single-member probe. Distinct from the eml archaeology leaf (`*.eml` /
email.parser), plist (`*.plist` / plistlib), JSON (`*.json` / json),
CSV (`*.csv` / csv), and HTML (`*.html` / tidy).

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Python 3 Library Reference — `zipfile`: Work with ZIP archives* |
| **Heading** | **`ZipFile.namelist` / `ZipFile.read`** — List archive members by name; return the bytes of a named member |
| **Dialect pinned** | **CPython stdlib `zipfile.ZipFile.namelist`/`read`** with member `PROBE.txt` → print token — **not** full unzip / zip / encryption / multi-volume suite claim |
| **URL** | https://docs.python.org/3/library/zipfile.html (Python docs — `zipfile`); CPython 3.13.5 on box |
| **Anchors** | `.zip` archive path; `ZipFile(path)`; `namelist()`; `read(name)` |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Python docs — `zipfile.ZipFile.namelist` / `read`)

> ZipFile.namelist() — Return a list of archive members by name.
>
> ZipFile.read(name, pwd=None) — Return the bytes of the file name in the archive. name is the name of the file in the archive, or a ZipInfo object.

(Source: Python 3 Library Reference, section
**zipfile — Work with ZIP archives — ZipFile objects**,
https://docs.python.org/3/library/zipfile.html
accessed 2026-09-28 Europe/Tirane.
Module intro: "The ZIP file format is a common archive and compression standard. This module provides tools to create, read, write, append, and list a ZIP file."
Installed `python3 --version` reports Python 3.13.5.
Probe uses
`ZipFile('HELLO.zip').read(ZipFile('HELLO.zip').namelist()[0]).decode().strip()`
so stdlib zipfile loads the named `.zip` and prints the member token.
Format: PKZIP / Info-ZIP compatible deflated archive.)

### Why this heading (HELLO.zip / excavate)

A minimal HELLO surface looks like a one-member deflated ZIP with
`PROBE.txt` holding a probe token. That is exactly the pinned form:
**stdlib `ZipFile.namelist`/`read`**, observe member bytes at run time.

### Honesty

- VERIFIED: CPython 3.13.5 stdlib `zipfile.ZipFile.namelist`/`read` on this HELLO (deflated ZIP with PROBE.txt).
- CONJECTURE: any claim that Info-ZIP / PKZIP / encrypted / multi-volume / JAR/WAR/APK/wheel/OOXML are this dialect.
- UNVERIFIABLE: Debian unzip / zip / full multi-dialect archive recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, openjdk/Java (apt size); graphviz this turn (multi-dep); Debian `unzip` / `zip` apt (unnecessary vs stdlib); bare `unzip` / `zip` apt as verified toolchain; `*.jar` / `*.war` / `*.apk` / `*.whl` / `*.docx` / `*.xlsx` / `*.tsv` / `*.jsonl` fossils this leaf (defer).
