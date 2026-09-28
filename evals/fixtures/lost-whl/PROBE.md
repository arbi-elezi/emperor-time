# Boot probe — lost-whl / HELLO.whl

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~16:40 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **Python 3.13.5** stdlib `zipfile` (already on box; module has no `__version__` attribute) |
| Binary / module | `/usr/bin/python3` + `zipfile.ZipFile.namelist` / `read` |
| Reported | `Python 3.13.5` / stdlib `zipfile` (`python3 --version`; `python3 -c 'import zipfile; print(zipfile.__file__)'`) |
| Install | already on box (CPython stdlib) — **zero new Apt Worthy Spend** this leaf; Debian `unzip` / `zip` apt REJECTED vs zero-apt stdlib (same as lost-zip); still prefer over deferred TeXlive / C++ / openjdk / graphviz multi-dep apt |

Probe used `python3` + stdlib `zipfile.ZipFile` on a minimal
`.whl` (ZIP-based wheel) archive and printed the contents of member `PROBE.txt`.
Identify fossils use `*.whl` (Python wheel peer leaf after compressed-TAR). Prefer `whl` / `pywhl` / `wheel` / `.whl`.
Bare `whl` / `pywhl` / `wheel` are **allowed** as route tags (format / family / format-name).
Bare `.whl` is **allowed** with extension-boundary matching (do not invent
`.whlfoo` prefix hits). Zip-based wheel leaf after compressed-TAR;
treats wheel as peer archive fossil not house twin language. Do **not**
claim a full pip / wheel / bdist_wheel / installer suite recovery from a CPython
stdlib `ZipFile.namelist`/`read` probe alone — this leaf pins stdlib
`zipfile` namelist+read on a `.whl` with the probe token printed. Do **not** claim Debian
`unzip` / `zip` as the verified toolchain this leaf (apt REJECTED).
Distinct from zip (`*.zip` / zipfile), compressed-TAR (`*.tar.gz` / tarfile),
plain tar (`*.tar` / tarfile), plain gzip (`*.gz` / gzip), eml (`*.eml` / email.parser),
plist (`*.plist` / plistlib), JSON (`*.json` / json), and CSV (`*.csv` / csv).
Do **not** steal plain `*.zip` ownership — that remains the zip leaf.
Defer `*.jar` / `*.war` / `*.apk` / `*.docx` / `*.xlsx` this turn.

## Commands (VERIFIED)

```text
$ python3 --version
Python 3.13.5

$ python3 -c 'import zipfile; print(zipfile.__file__)'
/usr/lib/python3.13/zipfile/__init__.py

$ python3 -c "from zipfile import ZipFile; z=ZipFile('HELLO.whl'); print(z.read('PROBE.txt').decode().strip())"
EMPEROR-TIME-WHL-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| CPython 3.13.5 stdlib `zipfile.ZipFile.namelist`/`read` on this HELLO (deflated wheel ZIP with PROBE.txt + dist-info) | VERIFIED |
| Full pip / wheel / bdist_wheel / RECORD verification / installer suite are this dialect | CONJECTURE |
| Full Debian unzip/zip suite recovery from this probe alone | UNVERIFIABLE |
