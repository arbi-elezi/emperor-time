# Jail pin — Python zipfile.ZipFile.namelist/read for HELLO.whl (wheel format)

Contemporaneous manual pin for the lost-whl archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how wheels
work" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-whl/HELLO.whl` with
runnable dialect **VERIFIED** as CPython 3.13.5 stdlib `zipfile`
under Linux x86_64
(`python3` + `ZipFile.namelist`/`read` on HELLO.whl → member
`PROBE.txt` yields `EMPEROR-TIME-WHL-PROBE-OK`). Filename culture
(pip / bdist_wheel / RECORD verify / installer / JAR/WAR/APK/OOXML)
remains **CONJECTURE** only for naming collisions. Identify fossils use `*.whl`.
Bare `whl` / `pywhl` / `wheel` are **allowed** as route tags (format / family / format-name).
Bare `.whl` is **allowed** as a route tag with
extension-boundary matching. Prefer `whl` /
`pywhl` / `wheel` / `.whl`.
Do **not** steal plain `*.zip` ownership from the zip leaf;
a `.whl` is a distinct zip-based container fossil.
Toolchain is CPython stdlib `zipfile` already on box (**zero new apt**).
Debian `unzip` / `zip` apt were considered and **REJECTED**
as the verified leaf owner vs stdlib (same as lost-zip). This note supplies
the Jail pin so excavate can name the **verified** stdlib `zipfile`
namelist/read shape on a wheel without inventing a full
pip / wheel / bdist_wheel / installer suite claim for a
single-member probe. Distinct from the zip archaeology leaf (`*.zip` /
zipfile), compressed-TAR (`*.tar.gz` / tarfile), plain tar (`*.tar` /
tarfile), plain gzip (`*.gz` / gzip), eml (`*.eml` / email.parser),
plist (`*.plist` / plistlib), JSON (`*.json` / json),
and CSV (`*.csv` / csv).

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Python 3 Library Reference — `zipfile`: Work with ZIP archives* + *PyPA Binary distribution format (wheel)* |
| **Heading** | **`ZipFile.namelist` / `ZipFile.read` on `.whl`** — List wheel archive members by name; return the bytes of a named member (wheel is ZIP-format with `.whl` extension) |
| **Dialect pinned** | **CPython stdlib `zipfile.ZipFile.namelist`/`read`** on a `.whl` with member `PROBE.txt` → print token — **not** full pip / wheel / bdist_wheel / installer suite claim |
| **URL** | https://docs.python.org/3/library/zipfile.html (Python docs — `zipfile`); https://packaging.python.org/en/latest/specifications/binary-distribution-format/ (PyPA — Binary distribution format); CPython 3.13.5 on box |
| **Anchors** | `.whl` archive path; `ZipFile(path)`; `namelist()`; `read(name)`; wheel = ZIP-format + `.whl` |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Python docs — `zipfile.ZipFile.namelist` / `read` + PyPA wheel)

> ZipFile.namelist() — Return a list of archive members by name.
>
> ZipFile.read(name, pwd=None) — Return the bytes of the file name in the archive. name is the name of the file in the archive, or a ZipInfo object.
>
> A wheel is a ZIP-format archive with a specially formatted file name and the `.whl` extension.

(Source: Python 3 Library Reference, section
**zipfile — Work with ZIP archives — ZipFile objects**,
https://docs.python.org/3/library/zipfile.html
accessed 2026-09-28 Europe/Tirane;
PyPA Binary distribution format,
https://packaging.python.org/en/latest/specifications/binary-distribution-format/
accessed 2026-09-28 Europe/Tirane.
Module intro: "The ZIP file format is a common archive and compression standard. This module provides tools to create, read, write, append, and list a ZIP file."
Wheel intro: "A wheel is a ZIP-format archive with a specially formatted file name and the `.whl` extension."
Installed `python3 --version` reports Python 3.13.5.
Probe uses
`ZipFile('HELLO.whl').read('PROBE.txt').decode().strip()`
so stdlib zipfile loads the named `.whl` and prints the member token.
Format: PKZIP / Info-ZIP compatible deflated wheel archive with `.dist-info`.)

### Why this heading (HELLO.whl / excavate)

A minimal HELLO surface looks like a one-package deflated wheel with
`PROBE.txt` holding a probe token plus `hello-0.0.0.dist-info/`. That is exactly the pinned form:
**stdlib `ZipFile.namelist`/`read` on `.whl`**, observe member bytes at run time.

### Honesty

- VERIFIED: CPython 3.13.5 stdlib `zipfile.ZipFile.namelist`/`read` on this HELLO (deflated wheel ZIP with PROBE.txt + dist-info).
- CONJECTURE: any claim that pip / bdist_wheel / full RECORD verify / installer / JAR/WAR/APK/OOXML are this dialect.
- UNVERIFIABLE: Debian unzip / zip / full multi-dialect archive recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, openjdk/Java (apt size); graphviz this turn (multi-dep); Debian `unzip` / `zip` apt (unnecessary vs stdlib); bare `unzip` / `zip` apt as verified toolchain; `*.jar` / `*.war` / `*.apk` / `*.docx` / `*.xlsx` / `*.tsv` / `*.jsonl` fossils this leaf (defer); stealing plain `*.zip` ownership from the zip leaf.
