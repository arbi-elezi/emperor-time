# Jail pin — Python zipfile.ZipFile.namelist/read for HELLO.jar (JAR format)

Contemporaneous manual pin for the lost-jar archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how JARs
work" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-jar/HELLO.jar` with
runnable dialect **VERIFIED** as CPython 3.13.5 stdlib `zipfile`
under Linux x86_64
(`python3` + `ZipFile.namelist`/`read` on HELLO.jar → member
`PROBE.txt` yields `EMPEROR-TIME-JAR-PROBE-OK`). Filename culture
(JVM / openjdk / javac / jar-tool / WAR/EAR/APK/OOXML)
remains **CONJECTURE** only for naming collisions. Identify fossils use `*.jar`.
Bare `jar` / `pyjar` / `java-archive` are **allowed** as route tags (format / family / format-name).
Bare `.jar` is **allowed** as a route tag with
extension-boundary matching. Prefer `jar` /
`pyjar` / `java-archive` / `.jar`.
Bare `java` / `openjdk` / `javac` are **refused** this leaf (JDK discourse / apt surface).
Do **not** steal plain `*.zip` or `*.whl` ownership from the zip / wheel leaves;
a `.jar` is a distinct zip-based container fossil.
Toolchain is CPython stdlib `zipfile` already on box (**zero new apt**).
Debian `unzip` / `zip` / `openjdk-*` apt were considered and **REJECTED**
as the verified leaf owner vs stdlib (same as lost-zip / lost-whl). This note supplies
the Jail pin so excavate can name the **verified** stdlib `zipfile`
namelist/read shape on a JAR without inventing a full
JVM / openjdk / javac / jar-tool suite claim for a
single-member probe. Distinct from the zip archaeology leaf (`*.zip` /
zipfile), wheel (`*.whl` / zipfile), compressed-TAR (`*.tar.gz` / tarfile), plain tar (`*.tar` /
tarfile), plain gzip (`*.gz` / gzip), eml (`*.eml` / email.parser),
plist (`*.plist` / plistlib), JSON (`*.json` / json),
and CSV (`*.csv` / csv).

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Python 3 Library Reference — `zipfile`: Work with ZIP archives* + *JAR File Specification (Oracle)* |
| **Heading** | **`ZipFile.namelist` / `ZipFile.read` on `.jar`** — List JAR archive members by name; return the bytes of a named member (JAR is ZIP-format with `.jar` extension + optional META-INF/MANIFEST.MF) |
| **Dialect pinned** | **CPython stdlib `zipfile.ZipFile.namelist`/`read`** on a `.jar` with member `PROBE.txt` → print token — **not** full JVM / openjdk / javac / jar-tool suite claim |
| **URL** | https://docs.python.org/3/library/zipfile.html (Python docs — `zipfile`); https://docs.oracle.com/javase/8/docs/technotes/guides/jar/jar.html (Oracle — JAR File Specification); CPython 3.13.5 on box |
| **Anchors** | `.jar` archive path; `ZipFile(path)`; `namelist()`; `read(name)`; JAR = ZIP-format + `.jar` (+ META-INF) |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Python docs — `zipfile.ZipFile.namelist` / `read` + Oracle JAR)

> ZipFile.namelist() — Return a list of archive members by name.
>
> ZipFile.read(name, pwd=None) — Return the bytes of the file name in the archive. name is the name of the file in the archive, or a ZipInfo object.
>
> JAR file is a file format based on the popular ZIP file format and is used for aggregating many files into one. A JAR file is essentially a zip file that contains an optional META-INF directory.

(Source: Python 3 Library Reference, section
**zipfile — Work with ZIP archives — ZipFile objects**,
https://docs.python.org/3/library/zipfile.html
accessed 2026-09-28 Europe/Tirane;
Oracle JAR File Specification,
https://docs.oracle.com/javase/8/docs/technotes/guides/jar/jar.html
accessed 2026-09-28 Europe/Tirane.
Module intro: "The ZIP file format is a common archive and compression standard. This module provides tools to create, read, write, append, and list a ZIP file."
JAR intro: "JAR file is a file format based on the popular ZIP file format and is used for aggregating many files into one."
Installed `python3 --version` reports Python 3.13.5.
Probe uses
`ZipFile('HELLO.jar').read('PROBE.txt').decode().strip()`
so stdlib zipfile loads the named `.jar` and prints the member token.
Format: PKZIP / Info-ZIP compatible deflated JAR archive with META-INF/MANIFEST.MF.)

### Why this heading (HELLO.jar / excavate)

A minimal HELLO surface looks like a one-package deflated JAR with
`PROBE.txt` holding a probe token plus `META-INF/MANIFEST.MF`. That is exactly the pinned form:
**stdlib `ZipFile.namelist`/`read` on `.jar`**, observe member bytes at run time.

### Honesty

- VERIFIED: CPython 3.13.5 stdlib `zipfile.ZipFile.namelist`/`read` on this HELLO (deflated JAR ZIP with PROBE.txt + META-INF).
- CONJECTURE: any claim that JVM / openjdk / javac / full jar-tool / WAR/EAR/APK/OOXML are this dialect.
- UNVERIFIABLE: Debian unzip / zip / openjdk / full multi-dialect archive recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, openjdk/Java as leaf owner (apt size); graphviz this turn (multi-dep); Debian `unzip` / `zip` apt (unnecessary vs stdlib); bare `unzip` / `zip` / `openjdk` apt as verified toolchain; `*.war` / `*.apk` / `*.docx` / `*.xlsx` / `*.tsv` / `*.jsonl` fossils this leaf (defer); stealing plain `*.zip` or `*.whl` ownership from the zip / wheel leaves.
