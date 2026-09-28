# Jail pin — Python zipfile.ZipFile.namelist/read for HELLO.pptx (OOXML Presentation)

Contemporaneous manual pin for the lost-pptx archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how PPTX
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-pptx/HELLO.pptx` with
runnable dialect **VERIFIED** as CPython 3.13.5 stdlib `zipfile`
under Linux x86_64
(`python3` + `ZipFile.namelist`/`read` on HELLO.pptx → member
`PROBE.txt` yields `EMPEROR-TIME-PPTX-PROBE-OK`). Filename culture
(PowerPoint / LibreOffice Impress / ECMA-376 authoring / docx / xlsx)
remains **CONJECTURE** only for naming collisions. Identify fossils use `*.pptx`.
Bare `pptx` / `pypptx` / `ooxml-pptx` are **allowed** as route tags (format / family / format-name).
Bare `.pptx` is **allowed** as a route tag with
extension-boundary matching. Prefer `pptx` /
`pypptx` / `ooxml-pptx` / `.pptx`.
Bare `powerpoint` / `libreoffice` / `soffice` / `impress` are **refused** this leaf (presentation-suite discourse / apt surface).
Do **not** steal plain `*.zip` or `*.whl` or `*.jar` or `*.war` or `*.apk` or `*.docx` or `*.xlsx` ownership from prior leaves;
a `.pptx` is a distinct zip-based container fossil (Office Open XML Presentation + ppt/presentation.xml layout).
Toolchain is CPython stdlib `zipfile` already on box (**zero new apt**).
Debian `unzip` / `zip` / LibreOffice apt were considered and **REJECTED**
as the verified leaf owner vs stdlib (same as lost-zip / lost-whl / lost-jar / lost-war / lost-apk / lost-docx / lost-xlsx). This note supplies
the Jail pin so excavate can name the **verified** stdlib `zipfile`
namelist/read shape on a PPTX without inventing a full
PowerPoint / LibreOffice Impress / ECMA-376 authoring suite claim for a
single-member probe. Distinct from the zip archaeology leaf (`*.zip` /
zipfile), wheel (`*.whl` / zipfile), JAR (`*.jar` / zipfile), WAR (`*.war` / zipfile), APK (`*.apk` / zipfile), DOCX (`*.docx` / zipfile), XLSX (`*.xlsx` / zipfile), TSV (`*.tsv` / csv+tab), JSONL (`*.jsonl` / json.loads-per-line), compressed-TAR (`*.tar.gz` / tarfile), plain tar (`*.tar` /
tarfile), plain gzip (`*.gz` / gzip), eml (`*.eml` / email.parser),
plist (`*.plist` / plistlib), JSON (`*.json` / json),
and CSV (`*.csv` / csv).
Chain Jail leaf only — excavate fossil pin, not a vendored anthropics document skill.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Python 3 Library Reference — `zipfile`: Work with ZIP archives* + *ECMA-376 / Office Open XML — PresentationML package* |
| **Heading** | **`ZipFile.namelist` / `ZipFile.read` on `.pptx`** — List OOXML Presentation package members by name; return the bytes of a named member (PPTX is ZIP-format OPC package with `.pptx` extension + [Content_Types].xml + ppt/presentation.xml + _rels/) |
| **Dialect pinned** | **CPython stdlib `zipfile.ZipFile.namelist`/`read`** on a `.pptx` with member `PROBE.txt` → print token — **not** full PowerPoint / LibreOffice Impress / ECMA-376 authoring suite claim |
| **URL** | https://docs.python.org/3/library/zipfile.html (Python docs — `zipfile`); https://www.ecma-international.org/publications-and-standards/standards/ecma-376/ (ECMA-376 Office Open XML File Formats); CPython 3.13.5 on box |
| **Anchors** | `.pptx` archive path; `ZipFile(path)`; `namelist()`; `read(name)`; PPTX = ZIP/OPC + `.pptx` (+ [Content_Types].xml + ppt/presentation.xml + _rels) |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Python docs — `zipfile.ZipFile.namelist` / `read` + ECMA-376 OOXML)

> ZipFile.namelist() — Return a list of archive members by name.
>
> ZipFile.read(name, pwd=None) — Return the bytes of the file name in the archive. name is the name of the file in the archive, or a ZipInfo object.
>
> This Standard defines Office Open XML file formats, or documents representing a collection of character, paragraph and table formatting properties, spreadsheet data, and presentation slide data, contained in packages conforming to the Open Packaging Conventions.

(Source: Python 3 Library Reference, section
**zipfile — Work with ZIP archives — ZipFile objects**,
https://docs.python.org/3/library/zipfile.html
accessed 2026-09-28 Europe/Tirane;
ECMA-376 Office Open XML File Formats,
https://www.ecma-international.org/publications-and-standards/standards/ecma-376/
accessed 2026-09-28 Europe/Tirane.
Module intro: "The ZIP file format is a common archive and compression standard. This module provides tools to create, read, write, append, and list a ZIP file."
OOXML intro: packages conforming to the Open Packaging Conventions hold WordprocessingML / SpreadsheetML / PresentationML parts.
Installed `python3 --version` reports Python 3.13.5.
Probe uses
`ZipFile('HELLO.pptx').read('PROBE.txt').decode().strip()`
so stdlib zipfile loads the named `.pptx` and prints the member token.
Format: PKZIP / Info-ZIP compatible deflated OOXML Presentation package with [Content_Types].xml + ppt/presentation.xml + _rels/.rels.)

### Why this heading (HELLO.pptx / excavate)

A minimal HELLO surface looks like a one-package deflated OOXML Presentation ZIP with
`PROBE.txt` holding a probe token plus `[Content_Types].xml`, `ppt/presentation.xml`, and `_rels/.rels`. That is exactly the pinned form:
**stdlib `ZipFile.namelist`/`read` on `.pptx`**, observe member bytes at run time.

### Honesty

- VERIFIED: CPython 3.13.5 stdlib `zipfile.ZipFile.namelist`/`read` on this HELLO (deflated OOXML ZIP with PROBE.txt + [Content_Types].xml + ppt/presentation.xml + _rels/.rels).
- CONJECTURE: any claim that PowerPoint / LibreOffice Impress / full ECMA-376 authoring / docx / xlsx are this dialect.
- UNVERIFIABLE: Debian unzip / zip / LibreOffice / full multi-dialect archive recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, LibreOffice/powerpoint as leaf owner (apt size); graphviz this turn (multi-dep); Debian `unzip` / `zip` apt (unnecessary vs stdlib); bare `unzip` / `zip` / LibreOffice / powerpoint apt as verified toolchain; stealing plain `*.zip` or `*.whl` or `*.jar` or `*.war` or `*.apk` or `*.docx` or `*.xlsx` ownership from prior leaves; vendoring anthropics document skills as this Jail pin.
