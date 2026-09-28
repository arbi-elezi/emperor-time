# Boot probe — lost-pptx / HELLO.pptx

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~20:24 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **Python 3.13.5** stdlib `zipfile` (already on box; module has no `__version__` attribute) |
| Binary / module | `/usr/bin/python3` + `zipfile.ZipFile.namelist` / `read` |
| Reported | `Python 3.13.5` / stdlib `zipfile` (`python3 --version`; `python3 -c 'import zipfile; print(zipfile.__file__)'`) |
| Install | already on box (CPython stdlib) — **zero new Apt Worthy Spend** this leaf; Debian `unzip` / `zip` / LibreOffice / powerpoint apt REJECTED vs zero-apt stdlib; still prefer over deferred TeXlive / C++ / graphviz multi-dep apt |

Probe used `python3` + stdlib `zipfile.ZipFile` on a minimal
`.pptx` (ZIP-based Office Open XML Presentation package) and printed the contents of member `PROBE.txt`.
Identify fossils use `*.pptx` (OOXML PowerPoint peer leaf after JSONL; PresentationML after DOCX/XLSX). Prefer `pptx` / `pypptx` / `ooxml-pptx` / `.pptx`.
Bare `pptx` / `pypptx` / `ooxml-pptx` are **allowed** as route tags (format / family / format-name).
Bare `.pptx` is **allowed** with extension-boundary matching (do not invent
`.pptxfoo` prefix hits). Bare `powerpoint` / `libreoffice` / `soffice` / `impress` refused this leaf (presentation-suite discourse / apt surface).
OOXML Presentation leaf after JSONL; treats PPTX as peer archive fossil not house twin language.
Do **not** claim a full PowerPoint / LibreOffice Impress / ECMA-376 authoring suite recovery from a CPython
stdlib `ZipFile.namelist`/`read` probe alone — this leaf pins stdlib
`zipfile` namelist+read on a `.pptx` with the probe token printed. Do **not** claim Debian
`unzip` / `zip` / LibreOffice as the verified toolchain this leaf (apt REJECTED).
Distinct from zip (`*.zip` / zipfile), wheel (`*.whl` / zipfile), JAR (`*.jar` / zipfile), WAR (`*.war` / zipfile), APK (`*.apk` / zipfile), DOCX (`*.docx` / zipfile), XLSX (`*.xlsx` / zipfile), TSV (`*.tsv` / csv+tab), JSONL (`*.jsonl` / json.loads-per-line), compressed-TAR (`*.tar.gz` / tarfile),
plain tar (`*.tar` / tarfile), plain gzip (`*.gz` / gzip), eml (`*.eml` / email.parser),
plist (`*.plist` / plistlib), JSON (`*.json` / json), and CSV (`*.csv` / csv).
Do **not** steal plain `*.zip` or `*.whl` or `*.jar` or `*.war` or `*.apk` or `*.docx` or `*.xlsx` ownership — those remain prior leaves.
Defer TeX/LaTeX / C++ / openjdk-as-owner / graphviz / CLIPS / embeddings this turn.

## Commands (VERIFIED)

```text
$ python3 --version
Python 3.13.5

$ python3 -c 'import zipfile; print(zipfile.__file__)'
/usr/lib/python3.13/zipfile/__init__.py

$ python3 -c "from zipfile import ZipFile; z=ZipFile('HELLO.pptx'); print(z.read('PROBE.txt').decode().strip())"
EMPEROR-TIME-PPTX-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| CPython 3.13.5 stdlib `zipfile.ZipFile.namelist`/`read` on this HELLO (deflated OOXML ZIP with PROBE.txt + [Content_Types].xml + ppt/presentation.xml + _rels/.rels) | VERIFIED |
| Full PowerPoint / LibreOffice Impress / ECMA-376 authoring suite are this dialect | CONJECTURE |
| Full Debian unzip/zip/LibreOffice suite recovery from this probe alone | UNVERIFIABLE |
