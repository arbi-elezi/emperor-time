# Jail pin — Python zipfile.ZipFile.namelist/read for HELLO.docx (OOXML Word)

Contemporaneous manual pin for the lost-docx archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how DOCX
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-docx/HELLO.docx` with
runnable dialect **VERIFIED** as CPython 3.13.5 stdlib `zipfile`
under Linux x86_64
(`python3` + `ZipFile.namelist`/`read` on HELLO.docx → member
`PROBE.txt` yields `EMPEROR-TIME-DOCX-PROBE-OK`). Filename culture
(Word / LibreOffice / pandoc / ECMA-376 authoring / xlsx)
remains **CONJECTURE** only for naming collisions. Identify fossils use `*.docx`.
Bare `docx` / `pydocx` / `ooxml-word` are **allowed** as route tags (format / family / format-name).
Bare `.docx` is **allowed** as a route tag with
extension-boundary matching. Prefer `docx` /
`pydocx` / `ooxml-word` / `.docx`.
Bare `word` / `libreoffice` / `soffice` / `pandoc` are **refused** this leaf (document-suite discourse / apt surface).
Do **not** steal plain `*.zip` or `*.whl` or `*.jar` or `*.war` or `*.apk` ownership from the zip / wheel / jar / war / apk leaves;
a `.docx` is a distinct zip-based container fossil (Office Open XML Word + word/document.xml layout).
Toolchain is CPython stdlib `zipfile` already on box (**zero new apt**).
Debian `unzip` / `zip` / LibreOffice / pandoc apt were considered and **REJECTED**
as the verified leaf owner vs stdlib (same as lost-zip / lost-whl / lost-jar / lost-war / lost-apk). This note supplies
the Jail pin so excavate can name the **verified** stdlib `zipfile`
namelist/read shape on a DOCX without inventing a full
Word / LibreOffice / pandoc / ECMA-376 authoring suite claim for a
single-member probe. Distinct from the zip archaeology leaf (`*.zip` /
zipfile), wheel (`*.whl` / zipfile), JAR (`*.jar` / zipfile), WAR (`*.war` / zipfile), APK (`*.apk` / zipfile), compressed-TAR (`*.tar.gz` / tarfile), plain tar (`*.tar` /
tarfile), plain gzip (`*.gz` / gzip), eml (`*.eml` / email.parser),
plist (`*.plist` / plistlib), JSON (`*.json` / json),
and CSV (`*.csv` / csv).
Chain Jail leaf only — excavate fossil pin, not a vendored anthropics document skill.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Python 3 Library Reference — `zipfile`: Work with ZIP archives* + *ECMA-376 / Office Open XML — WordprocessingML package* |
| **Heading** | **`ZipFile.namelist` / `ZipFile.read` on `.docx`** — List OOXML Word package members by name; return the bytes of a named member (DOCX is ZIP-format OPC package with `.docx` extension + [Content_Types].xml + word/document.xml + _rels/) |
| **Dialect pinned** | **CPython stdlib `zipfile.ZipFile.namelist`/`read`** on a `.docx` with member `PROBE.txt` → print token — **not** full Word / LibreOffice / pandoc / ECMA-376 authoring suite claim |
| **URL** | https://docs.python.org/3/library/zipfile.html (Python docs — `zipfile`); https://www.ecma-international.org/publications-and-standards/standards/ecma-376/ (ECMA-376 Office Open XML File Formats); CPython 3.13.5 on box |
| **Anchors** | `.docx` archive path; `ZipFile(path)`; `namelist()`; `read(name)`; DOCX = ZIP/OPC + `.docx` (+ [Content_Types].xml + word/document.xml + _rels) |
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
`ZipFile('HELLO.docx').read('PROBE.txt').decode().strip()`
so stdlib zipfile loads the named `.docx` and prints the member token.
Format: PKZIP / Info-ZIP compatible deflated OOXML Word package with [Content_Types].xml + word/document.xml + _rels/.rels.)

### Why this heading (HELLO.docx / excavate)

A minimal HELLO surface looks like a one-package deflated OOXML Word ZIP with
`PROBE.txt` holding a probe token plus `[Content_Types].xml`, `word/document.xml`, and `_rels/.rels`. That is exactly the pinned form:
**stdlib `ZipFile.namelist`/`read` on `.docx`**, observe member bytes at run time.

### Honesty

- VERIFIED: CPython 3.13.5 stdlib `zipfile.ZipFile.namelist`/`read` on this HELLO (deflated OOXML ZIP with PROBE.txt + [Content_Types].xml + word/document.xml + _rels/.rels).
- CONJECTURE: any claim that Word / LibreOffice / pandoc / full ECMA-376 authoring / xlsx are this dialect.
- UNVERIFIABLE: Debian unzip / zip / LibreOffice / pandoc / full multi-dialect archive recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, LibreOffice/pandoc as leaf owner (apt size); graphviz this turn (multi-dep); Debian `unzip` / `zip` apt (unnecessary vs stdlib); bare `unzip` / `zip` / LibreOffice / pandoc apt as verified toolchain; `*.xlsx` / `*.tsv` / `*.jsonl` fossils this leaf (defer); stealing plain `*.zip` or `*.whl` or `*.jar` or `*.war` or `*.apk` ownership from the zip / wheel / jar / war / apk leaves; vendoring anthropics document skills as this Jail pin.
