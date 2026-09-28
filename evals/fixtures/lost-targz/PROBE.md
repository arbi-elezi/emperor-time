# Boot probe — lost-targz / HELLO.tar.gz

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~16:12 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **Python 3.13.5** stdlib `tarfile` (+ `gzip` / `bz2` / `lzma` compression backends; already on box; module has no `__version__` attribute) |
| Binary / module | `/usr/bin/python3` + `tarfile.open` modes `r:gz` / `r:bz2` / `r:xz` / `getmembers` / `extractfile` |
| Reported | `Python 3.13.5` / stdlib `tarfile` (`python3 --version`; `python3 -c 'import tarfile; print(tarfile.__file__)'`) |
| Install | already on box (CPython stdlib) — **zero new Apt Worthy Spend** this leaf; Debian `tar` / `gzip` / `bzip2` / `xz-utils` already on box — **REJECTED** as verified toolchain vs zero-apt stdlib; still prefer over deferred TeXlive / C++ / openjdk / graphviz multi-dep apt |

Probe used `python3` + stdlib `tarfile.open` on minimal
compressed TAR archives and printed the contents of member `PROBE.txt`.
Identify fossils use `*.tar.gz` / `*.tgz` / `*.tar.bz2` / `*.tar.xz`
(compressed TAR peer leaf after plain gzip). Prefer `targz` / `tarball` / `pytargz` / `.tar.gz` / `.tgz` / `.tar.bz2` / `.tar.xz`.
Bare `targz` / `tarball` / `pytargz` are **allowed** as route tags (family / format / module-family).
Bare `.tar.gz` / `.tgz` / `.tar.bz2` / `.tar.xz` are **allowed** with extension-boundary matching
(do not invent `.tar.gzfoo` / `.tgzfoo` prefix hits). Compressed-TAR leaf after plain `*.gz`;
treats compressed TAR as peer archive fossil not house twin language. Do **not**
claim a full GNU tar / pax / sparse / multi-volume compressed suite recovery from a CPython
stdlib `tarfile` compressed-mode probe alone — this leaf pins stdlib
`tarfile` list+read under `r:gz`/`r:bz2`/`r:xz` with the probe token printed. Do **not** claim Debian
`tar` / `gzip` / `bzip2` / `xz-utils` as the verified toolchain this leaf (apt/system binary REJECTED as leaf owner).
Distinct from plain tar (`*.tar` / tarfile uncompressed), plain gzip (`*.gz` / gzip), zip (`*.zip` / zipfile),
eml (`*.eml` / email.parser), plist (`*.plist` / plistlib), JSON (`*.json` / json), and CSV (`*.csv` / csv).
Do **not** steal plain `*.gz` or plain `*.tar` ownership — those remain prior leaves.
Defer `*.jar` / `*.war` / `*.apk` / `*.whl` / `*.docx` / `*.xlsx` this turn.

## Commands (VERIFIED)

```text
$ python3 --version
Python 3.13.5

$ python3 -c 'import tarfile; print(tarfile.__file__)'
/usr/lib/python3.13/tarfile.py

$ python3 -c "import tarfile; t=tarfile.open('HELLO.tar.gz','r:gz'); m=t.getmembers()[0]; print(t.extractfile(m).read().decode().strip())"
EMPEROR-TIME-TARGZ-PROBE-OK

$ python3 -c "import tarfile; t=tarfile.open('HELLO.tgz','r:gz'); m=t.getmembers()[0]; print(t.extractfile(m).read().decode().strip())"
EMPEROR-TIME-TARGZ-PROBE-OK

$ python3 -c "import tarfile; t=tarfile.open('HELLO.tar.bz2','r:bz2'); m=t.getmembers()[0]; print(t.extractfile(m).read().decode().strip())"
EMPEROR-TIME-TARGZ-PROBE-OK

$ python3 -c "import tarfile; t=tarfile.open('HELLO.tar.xz','r:xz'); m=t.getmembers()[0]; print(t.extractfile(m).read().decode().strip())"
EMPEROR-TIME-TARGZ-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| CPython 3.13.5 stdlib `tarfile.open`/`getmembers`/`extractfile` on this HELLO family (`r:gz` / `r:bz2` / `r:xz` compressed TAR with PROBE.txt) | VERIFIED |
| Full GNU tar / pax / sparse / multi-volume / exotic compressor recovery are this dialect | CONJECTURE |
| Full Debian tar/gzip/bzip2/xz suite recovery from this probe alone | UNVERIFIABLE |
