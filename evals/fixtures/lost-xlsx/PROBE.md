# Boot probe — lost-xlsx / HELLO.xlsx

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~19:08 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **Python 3.13.5** stdlib `zipfile` (already on box; module has no `__version__` attribute) |
| Binary / module | `/usr/bin/python3` + `zipfile.ZipFile.namelist` / `read` |
| Reported | `Python 3.13.5` / stdlib `zipfile` (`python3 --version`; `python3 -c 'import zipfile; print(zipfile.__file__)'`) |
| Install | already on box (CPython stdlib) — **zero new Apt Worthy Spend** this leaf; Debian `unzip` / `zip` / LibreOffice / openpyxl / xlsxwriter apt REJECTED vs zero-apt stdlib; still prefer over deferred TeXlive / C++ / graphviz multi-dep apt |

Probe used `python3` + stdlib `zipfile.ZipFile` on a minimal
`.xlsx` (ZIP-based Office Open XML Spreadsheet package) and printed the contents of member `PROBE.txt`.
Identify fossils use `*.xlsx` (OOXML Excel peer leaf after DOCX). Prefer `xlsx` / `pyxlsx` / `ooxml-excel` / `.xlsx`.
Bare `xlsx` / `pyxlsx` / `ooxml-excel` are **allowed** as route tags (format / family / format-name).
Bare `.xlsx` is **allowed** with extension-boundary matching (do not invent
`.xlsxfoo` prefix hits). Bare `excel` / `libreoffice` / `soffice` / `openpyxl` / `xlsxwriter` refused this leaf (spreadsheet-suite discourse / apt surface).
OOXML Spreadsheet leaf after DOCX; treats XLSX as peer archive fossil not house twin language.
Do **not** claim a full Excel / LibreOffice / openpyxl / xlsxwriter / ECMA-376 authoring suite recovery from a CPython
stdlib `ZipFile.namelist`/`read` probe alone — this leaf pins stdlib
`zipfile` namelist+read on a `.xlsx` with the probe token printed. Do **not** claim Debian
`unzip` / `zip` / LibreOffice / openpyxl / xlsxwriter as the verified toolchain this leaf (apt REJECTED).
Distinct from zip (`*.zip` / zipfile), wheel (`*.whl` / zipfile), JAR (`*.jar` / zipfile), WAR (`*.war` / zipfile), APK (`*.apk` / zipfile), DOCX (`*.docx` / zipfile), compressed-TAR (`*.tar.gz` / tarfile),
plain tar (`*.tar` / tarfile), plain gzip (`*.gz` / gzip), eml (`*.eml` / email.parser),
plist (`*.plist` / plistlib), JSON (`*.json` / json), and CSV (`*.csv` / csv).
Do **not** steal plain `*.zip` or `*.whl` or `*.jar` or `*.war` or `*.apk` or `*.docx` ownership — those remain the zip / wheel / jar / war / apk / docx leaves.
Defer `*.tsv` / `*.jsonl` this turn.

## Commands (VERIFIED)

```text
$ python3 --version
Python 3.13.5

$ python3 -c 'import zipfile; print(zipfile.__file__)'
/usr/lib/python3.13/zipfile/__init__.py

$ python3 -c "from zipfile import ZipFile; z=ZipFile('HELLO.xlsx'); print(z.read('PROBE.txt').decode().strip())"
EMPEROR-TIME-XLSX-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| CPython 3.13.5 stdlib `zipfile.ZipFile.namelist`/`read` on this HELLO (deflated OOXML ZIP with PROBE.txt + [Content_Types].xml + xl/workbook.xml + _rels/.rels) | VERIFIED |
| Full Excel / LibreOffice / openpyxl / xlsxwriter / ECMA-376 authoring suite are this dialect | CONJECTURE |
| Full Debian unzip/zip/LibreOffice/openpyxl/xlsxwriter suite recovery from this probe alone | UNVERIFIABLE |
