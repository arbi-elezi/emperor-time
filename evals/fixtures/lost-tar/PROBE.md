# Boot probe — lost-tar / HELLO.tar

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~15:23 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **Python 3.13.5** stdlib `tarfile` (already on box; module has no `__version__` attribute) |
| Binary / module | `/usr/bin/python3` + `tarfile.open` / `getmembers` / `extractfile` |
| Reported | `Python 3.13.5` / stdlib `tarfile` (`python3 --version`; `python3 -c 'import tarfile; print(tarfile.__file__)'`) |
| Install | already on box (CPython stdlib) — **zero new Apt Worthy Spend** this leaf; Debian `tar` 1.35+dfsg-3.1 already on box (Installed-Size ~3085 kB) — **REJECTED** as verified toolchain vs zero-apt stdlib; still prefer over deferred TeXlive / C++ / openjdk / graphviz multi-dep apt |

Probe used `python3` + stdlib `tarfile.open` on a minimal
`.tar` archive and printed the contents of member `PROBE.txt`.
Identify fossils use `*.tar` (ustar/POSIX TAR archive peer leaf after zip). Prefer `tar` / `pytar` / `tarfile` / `.tar`.
Bare `tar` is **allowed** as a route tag (format/tool name; word-boundary so `target` does not hit).
Bare `pytar` / `tarfile` are **allowed** as route tags (family / module).
Bare `.tar` is **allowed** with extension-boundary matching (do not invent
`.tarfoo` prefix hits; do not alone own `.tar.gz` / `.tgz` this leaf). Archive-format leaf after zip;
treats tar as peer archive fossil not house twin language. Do **not**
claim a full GNU tar / pax / sparse / multi-volume TAR recovery from a CPython
stdlib `tarfile` getmembers/extractfile probe alone — this leaf pins stdlib
`tarfile` list+read with the probe token printed. Do **not** claim Debian
`tar` as the verified toolchain this leaf (apt/system binary REJECTED as leaf owner).
Distinct from zip (`*.zip` / zipfile), eml (`*.eml` / email.parser), plist (`*.plist` / plistlib),
JSON (`*.json` / json), and CSV (`*.csv` / csv).
Defer `*.tar.gz` / `*.tgz` / `*.tar.bz2` / `*.tar.xz` (compressed TAR variants) and
`*.jar` / `*.war` / `*.apk` / `*.whl` / `*.docx` / `*.xlsx` this turn.

## Commands (VERIFIED)

```text
$ python3 --version
Python 3.13.5

$ python3 -c 'import tarfile; print(tarfile.__file__)'
/usr/lib/python3.13/tarfile.py

$ python3 -c "import tarfile; t=tarfile.open('HELLO.tar'); m=t.getmembers()[0]; print(t.extractfile(m).read().decode().strip())"
EMPEROR-TIME-TAR-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| CPython 3.13.5 stdlib `tarfile.open`/`getmembers`/`extractfile` on this HELLO (ustar TAR with PROBE.txt) | VERIFIED |
| Full GNU tar / pax / sparse / multi-volume / compressed `.tar.gz` recovery are this dialect | CONJECTURE |
| Full Debian tar suite recovery from this probe alone | UNVERIFIABLE |
