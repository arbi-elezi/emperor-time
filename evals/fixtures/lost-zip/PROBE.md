# Boot probe — lost-zip / HELLO.zip

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~14:54 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **Python 3.13.5** stdlib `zipfile` (already on box; module has no `__version__` attribute) |
| Binary / module | `/usr/bin/python3` + `zipfile.ZipFile.namelist` / `read` |
| Reported | `Python 3.13.5` / stdlib `zipfile` (`python3 --version`; `python3 -c 'import zipfile; print(zipfile.__file__)'`) |
| Install | already on box (CPython stdlib) — **zero new Apt Worthy Spend** this leaf; Debian `unzip` 6.0-29+deb13u1 apt simulated (Installed-Size ~387 kB; archive ~173 kB) — **REJECTED** vs zero-apt stdlib; Debian `zip` 3.0-15+deb13u1 (Installed-Size ~627 kB; archive ~235 kB) also REJECTED; still prefer over deferred TeXlive / C++ / openjdk / graphviz multi-dep apt |

Probe used `python3` + stdlib `zipfile.ZipFile` on a minimal
`.zip` archive and printed the contents of member `PROBE.txt`.
Identify fossils use `*.zip` (ZIP archive peer leaf after eml). Prefer `zip` / `pyzip` / `zipfile` / `.zip`.
Bare `zip` is **allowed** as a route tag (format/tool name; word-boundary).
Bare `pyzip` / `zipfile` are **allowed** as route tags (family / module).
Bare `.zip` is **allowed** with extension-boundary matching (do not invent
`.zipfoo` prefix hits). Archive-format leaf after eml;
treats zip as peer archive fossil not house twin language. Do **not**
claim a full unzip / zip suite / encryption / multi-volume ZIP recovery from a CPython
stdlib `ZipFile.namelist`/`read` probe alone — this leaf pins stdlib
`zipfile` namelist+read with the probe token printed. Do **not** claim Debian
`unzip` / `zip` as the verified toolchain this leaf (apt REJECTED).
Distinct from eml (`*.eml` / email.parser), plist (`*.plist` / plistlib),
JSON (`*.json` / json), CSV (`*.csv` / csv), and HTML (`*.html` / tidy).
Defer `*.jar` / `*.war` / `*.apk` / `*.whl` / `*.docx` / `*.xlsx` (zip-based containers) this turn.

## Commands (VERIFIED)

```text
$ python3 --version
Python 3.13.5

$ python3 -c 'import zipfile; print(zipfile.__file__)'
/usr/lib/python3.13/zipfile/__init__.py

$ python3 -c "from zipfile import ZipFile; z=ZipFile('HELLO.zip'); print(z.read(z.namelist()[0]).decode().strip())"
EMPEROR-TIME-ZIP-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| CPython 3.13.5 stdlib `zipfile.ZipFile.namelist`/`read` on this HELLO (deflated ZIP with PROBE.txt) | VERIFIED |
| Full unzip / zip suite / encryption / multi-volume / ZIP64 recovery are this dialect | CONJECTURE |
| Full Debian unzip/zip suite recovery from this probe alone | UNVERIFIABLE |
