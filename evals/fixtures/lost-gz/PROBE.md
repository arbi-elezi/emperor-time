# Boot probe — lost-gz / HELLO.gz

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~15:46 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **Python 3.13.5** stdlib `gzip` (already on box; module has no `__version__` attribute) |
| Binary / module | `/usr/bin/python3` + `gzip.open` / read |
| Reported | `Python 3.13.5` / stdlib `gzip` (`python3 --version`; `python3 -c 'import gzip; print(gzip.__file__)'`) |
| Install | already on box (CPython stdlib) — **zero new Apt Worthy Spend** this leaf; Debian `gzip` 1.13-1+deb13u1 already on box (Installed-Size ~256 kB) — **REJECTED** as verified toolchain vs zero-apt stdlib; still prefer over deferred TeXlive / C++ / openjdk / graphviz multi-dep apt |

Probe used `python3` + stdlib `gzip.open` on a minimal
`.gz` (RFC 1952 gzip) member and printed the decompressed payload.
Identify fossils use `*.gz` (plain gzip compressed single-member peer leaf after tar). Prefer `gzip` / `pygzip` / `gzipfile` / `.gz`.
Bare `gzip` is **allowed** as a route tag (format/tool name; word-boundary so `gunzip` does not hit as bare `gzip`).
Bare `pygzip` / `gzipfile` are **allowed** as route tags (family / module).
Bare `.gz` is **allowed** with extension-boundary matching (do not invent
`.gzfoo` prefix hits). A `.gz` suffix match may fire excavate on
`file.tar.gz` as a gzip-compressed utterance without claiming compressed-TAR
ownership this leaf — do **not** add `*.tar.gz` / `*.tgz` fossils. Compression-format leaf after tar;
treats gzip as peer compressed fossil not house twin language. Do **not**
claim a full GNU gzip / multi-member / concatenated gzip recovery from a CPython
stdlib `gzip` open/read probe alone — this leaf pins stdlib
`gzip.open` read with the probe token printed. Do **not** claim Debian
`gzip` as the verified toolchain this leaf (apt/system binary REJECTED as leaf owner).
Distinct from tar (`*.tar` / tarfile), zip (`*.zip` / zipfile), eml (`*.eml` / email.parser), plist (`*.plist` / plistlib),
JSON (`*.json` / json), and CSV (`*.csv` / csv).
Defer `*.tar.gz` / `*.tgz` / `*.tar.bz2` / `*.tar.xz` (compressed TAR variants) and
`*.jar` / `*.war` / `*.apk` / `*.whl` / `*.docx` / `*.xlsx` this turn.

## Commands (VERIFIED)

```text
$ python3 --version
Python 3.13.5

$ python3 -c 'import gzip; print(gzip.__file__)'
/usr/lib/python3.13/gzip.py

$ python3 -c "import gzip; print(gzip.open('HELLO.gz','rb').read().decode().strip())"
EMPEROR-TIME-GZIP-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| CPython 3.13.5 stdlib `gzip.open`/read on this HELLO (RFC 1952 gzip single-member) | VERIFIED |
| Full GNU gzip / multi-member / concatenated / compressed `.tar.gz` recovery are this dialect | CONJECTURE |
| Full Debian gzip suite recovery from this probe alone | UNVERIFIABLE |
