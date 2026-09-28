# Boot probe — lost-plist / HELLO.plist

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~14:04 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **Python 3.13.5** stdlib `plistlib` (already on box; module has no `__version__` attribute) |
| Binary / module | `/usr/bin/python3` + `plistlib.load` |
| Reported | `Python 3.13.5` / stdlib `plistlib` (`python3 --version`; `python3 -c 'import plistlib; print(plistlib.__file__)'`) |
| Install | already on box (CPython stdlib) — **zero new Apt Worthy Spend** this leaf; Debian `libplist-utils` 2.6.0-2+b1 apt simulated with `libplist-2.0-4` (~68 kB archives / ~184 kB Installed-Size across 2 new packages) — **REJECTED** vs zero-apt stdlib (tiny but unnecessary); still prefer over deferred TeXlive / C++ / openjdk / graphviz multi-dep apt |

Probe used `python3` + stdlib `plistlib.load` on a minimal
XML property list with top-level dict key `probe`.
Identify fossils use `*.plist` (Apple property-list peer leaf after INI). Prefer `plist` / `pyplist` / `plistlib` / `.plist`.
Bare `plist` is **allowed** as a route tag (format name; substring match for 5-char token).
Bare `pyplist` / `plistlib` are **allowed** as route tags (family / module).
Bare `.plist` is **allowed** with extension-boundary matching (do not invent
`.plistfoo` / `.plistx` prefix hits). Property-list config leaf after INI;
treats plist as peer fossil not house twin language. Do **not**
claim a full plutil / libplist / NeXTSTEP binary-plist suite recovery from a CPython
stdlib `plistlib.load` probe alone — this leaf pins stdlib `plistlib`
XML load with the probe token printed. Do **not** claim Debian
`libplist-utils` / `plutil` as the verified toolchain this leaf (apt REJECTED).
Distinct from XML (`*.xml` / xmllint) and from JSON (`*.json` / stdlib json).

## Commands (VERIFIED)

```text
$ python3 --version
Python 3.13.5

$ python3 -c 'import plistlib; print(plistlib.__file__)'
/usr/lib/python3.13/plistlib.py

$ python3 -c "import plistlib; print(plistlib.load(open('HELLO.plist','rb'))['probe'])"
EMPEROR-TIME-PLIST-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| CPython 3.13.5 stdlib `plistlib` `load` on this HELLO (XML FMT) | VERIFIED |
| NeXTSTEP / OpenStep binary plist / plutil round-trip are this dialect | CONJECTURE |
| Full libplist / macOS plutil suite recovery from this probe alone | UNVERIFIABLE |
