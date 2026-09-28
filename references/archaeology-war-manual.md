# Jail pin — Python zipfile.ZipFile.namelist/read for HELLO.war (WAR format)

Contemporaneous manual pin for the lost-war archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how WARs
work" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-war/HELLO.war` with
runnable dialect **VERIFIED** as CPython 3.13.5 stdlib `zipfile`
under Linux x86_64
(`python3` + `ZipFile.namelist`/`read` on HELLO.war → member
`PROBE.txt` yields `EMPEROR-TIME-WAR-PROBE-OK`). Filename culture
(JVM / openjdk / javac / jar-tool / Tomcat / servlet / EAR/APK/OOXML)
remains **CONJECTURE** only for naming collisions. Identify fossils use `*.war`.
Bare `war` / `pywar` / `web-archive` are **allowed** as route tags (format / family / format-name).
Bare `.war` is **allowed** as a route tag with
extension-boundary matching. Prefer `war` /
`pywar` / `web-archive` / `.war`.
Bare `java` / `openjdk` / `javac` / `tomcat` / `servlet` are **refused** this leaf (JDK / servlet-container discourse / apt surface).
Do **not** steal plain `*.zip` or `*.whl` or `*.jar` ownership from the zip / wheel / jar leaves;
a `.war` is a distinct zip-based container fossil (JAR + WEB-INF layout).
Toolchain is CPython stdlib `zipfile` already on box (**zero new apt**).
Debian `unzip` / `zip` / `openjdk-*` / `tomcat*` apt were considered and **REJECTED**
as the verified leaf owner vs stdlib (same as lost-zip / lost-whl / lost-jar). This note supplies
the Jail pin so excavate can name the **verified** stdlib `zipfile`
namelist/read shape on a WAR without inventing a full
JVM / openjdk / javac / jar-tool / Tomcat / servlet suite claim for a
single-member probe. Distinct from the zip archaeology leaf (`*.zip` /
zipfile), wheel (`*.whl` / zipfile), JAR (`*.jar` / zipfile), compressed-TAR (`*.tar.gz` / tarfile), plain tar (`*.tar` /
tarfile), plain gzip (`*.gz` / gzip), eml (`*.eml` / email.parser),
plist (`*.plist` / plistlib), JSON (`*.json` / json),
and CSV (`*.csv` / csv).

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Python 3 Library Reference — `zipfile`: Work with ZIP archives* + *Java EE / Jakarta Servlet — Web Application Archive (WAR)* |
| **Heading** | **`ZipFile.namelist` / `ZipFile.read` on `.war`** — List WAR archive members by name; return the bytes of a named member (WAR is ZIP-format with `.war` extension + WEB-INF/ + optional META-INF/MANIFEST.MF) |
| **Dialect pinned** | **CPython stdlib `zipfile.ZipFile.namelist`/`read`** on a `.war` with member `PROBE.txt` → print token — **not** full JVM / openjdk / javac / jar-tool / Tomcat / servlet suite claim |
| **URL** | https://docs.python.org/3/library/zipfile.html (Python docs — `zipfile`); https://docs.oracle.com/javaee/7/tutorial/packaging001.htm (Oracle Java EE 7 Tutorial — Packaging Applications / WAR); CPython 3.13.5 on box |
| **Anchors** | `.war` archive path; `ZipFile(path)`; `namelist()`; `read(name)`; WAR = ZIP-format + `.war` (+ WEB-INF + META-INF) |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Python docs — `zipfile.ZipFile.namelist` / `read` + Oracle Java EE WAR packaging)

> ZipFile.namelist() — Return a list of archive members by name.
>
> ZipFile.read(name, pwd=None) — Return the bytes of the file name in the archive. name is the name of the file in the archive, or a ZipInfo object.
>
> A WAR file is a standard JAR with a .war extension. WAR files are used to package web applications so that a single file can be uploaded to a container.

(Source: Python 3 Library Reference, section
**zipfile — Work with ZIP archives — ZipFile objects**,
https://docs.python.org/3/library/zipfile.html
accessed 2026-09-28 Europe/Tirane;
Oracle Java EE 7 Tutorial — Packaging Applications,
https://docs.oracle.com/javaee/7/tutorial/packaging001.htm
accessed 2026-09-28 Europe/Tirane.
Module intro: "The ZIP file format is a common archive and compression standard. This module provides tools to create, read, write, append, and list a ZIP file."
WAR intro: "A WAR file is a standard JAR with a .war extension. WAR files are used to package web applications so that a single file can be uploaded to a container."
Installed `python3 --version` reports Python 3.13.5.
Probe uses
`ZipFile('HELLO.war').read('PROBE.txt').decode().strip()`
so stdlib zipfile loads the named `.war` and prints the member token.
Format: PKZIP / Info-ZIP compatible deflated WAR archive with META-INF/MANIFEST.MF + WEB-INF/web.xml.)

### Why this heading (HELLO.war / excavate)

A minimal HELLO surface looks like a one-package deflated WAR with
`PROBE.txt` holding a probe token plus `META-INF/MANIFEST.MF` and `WEB-INF/web.xml`. That is exactly the pinned form:
**stdlib `ZipFile.namelist`/`read` on `.war`**, observe member bytes at run time.

### Honesty

- VERIFIED: CPython 3.13.5 stdlib `zipfile.ZipFile.namelist`/`read` on this HELLO (deflated WAR ZIP with PROBE.txt + META-INF + WEB-INF).
- CONJECTURE: any claim that JVM / openjdk / javac / full jar-tool / Tomcat / servlet-container / EAR/APK/OOXML are this dialect.
- UNVERIFIABLE: Debian unzip / zip / openjdk / tomcat / full multi-dialect archive recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, openjdk/Java/Tomcat as leaf owner (apt size); graphviz this turn (multi-dep); Debian `unzip` / `zip` apt (unnecessary vs stdlib); bare `unzip` / `zip` / `openjdk` / `tomcat` apt as verified toolchain; `*.apk` / `*.docx` / `*.xlsx` / `*.tsv` / `*.jsonl` fossils this leaf (defer); stealing plain `*.zip` or `*.whl` or `*.jar` ownership from the zip / wheel / jar leaves.
