# Boot probe — lost-py / HELLO.py

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~10:31 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **python3** 3.13.5-1 |
| Binary | `/usr/bin/python3` |
| Reported | `Python 3.13.5` |
| Install | already present on box (no apt this leaf) |

Probe used script-file evaluation
(`python3 HELLO.py`)
on a minimal `print` program. Identify fossils
use `*.py` only. Prefer `python3` / `python3.13` / `cpython` / `.py`.
Bare `python` is **refused** as a route tag (ET meta / house-tooling
discourse collision; substring would steal non-excavate utterances).
Bare `py` is **allowed** as a route tag (two-letter abbreviation;
word-boundary match). Bare `.py` is **allowed** with extension-boundary
matching (does not prefix-hit `.pyc` / `.pyo` / `.pyw` / `.pyx` / `.pyi`).
Classic scripting / runtime leaf after JavaScript; language-agnostic.md
already named Python as a peer; toolchain already on box (Worthy Spend
vs TeXlive / C++ apt). Do not claim a full stdlib / packaging / typing
graph recovery from a `print` probe alone — this leaf pins Python
script-file evaluation via `python3` + stdout.

## Commands (VERIFIED)

```text
$ dpkg -l python3 | awk '/^ii/ {print $2, $3}'
python3 3.13.5-1

$ python3 --version
Python 3.13.5

$ which python3
/usr/bin/python3

$ python3 HELLO.py
EMPEROR-TIME-PY-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| Host runs Python 3.13 and executes `HELLO.py` via `python3 HELLO.py` | VERIFIED |
| Filename culture (`.pyw` / `.pyx` / `.pyi` / packaging layout) maps to this dialect | CONJECTURE (probe uses plain `.py` script) |
| Full stdlib / packaging / typing / free-threaded GIL recovery | UNVERIFIABLE from print probe alone |
