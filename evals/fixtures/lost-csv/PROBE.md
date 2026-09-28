# Boot probe — lost-csv / HELLO.csv

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~13:14 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **Python 3.13.5** stdlib `csv` (already on box; module `__version__` reports `1.0`) |
| Binary / module | `/usr/bin/python3` + `csv.DictReader` |
| Reported | `Python 3.13.5` / `csv` 1.0 (`python3 --version`; `python3 -c 'import csv; print(csv.__version__)'`) |
| Install | already on box (CPython stdlib) — **zero new Apt Worthy Spend** this leaf; Debian `csvkit` 2.0.1-3 apt simulated at ~10.6 MB archives / ~53 MB Installed-Size across 29 new packages (agate/sqlalchemy/lxml/babel…) — **REJECTED** vs tidy-class Worthy Spend; still prefer over deferred TeXlive / C++ / openjdk / graphviz multi-dep apt |

Probe used `python3` + stdlib `csv.DictReader` on a minimal
CSV header/`probe` column with a single data row.
Identify fossils use `*.csv` (CSV tabular peer leaf after HTML document chain). Prefer `csv` / `pycsv` / `csv1.0` / `.csv`.
Bare `csv` is **allowed** as a route tag (language / format name; word-boundary for 3-char token).
Bare `pycsv` / `csv1.0` are **allowed** as route tags (family / version).
Bare `.csv` is **allowed** with extension-boundary matching (do not invent
`.csvfoo` prefix hits). CSV tabular leaf after HTML;
treats CSV as peer fossil not house twin language. Do **not**
claim a full csvkit / pandas / RFC 4180 suite recovery from a CPython
stdlib `DictReader` probe alone — this leaf pins stdlib `csv` DictReader
column lookup with the probe token printed. Do **not** claim Debian
`csvkit` / `csvcut` as the verified toolchain this leaf (apt REJECTED).

## Commands (VERIFIED)

```text
$ python3 --version
Python 3.13.5

$ python3 -c 'import csv; print(csv.__version__)'
1.0

$ python3 -c "import csv; print(next(csv.DictReader(open('HELLO.csv', newline='')))['probe'])"
EMPEROR-TIME-CSV-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| Host runs stdlib `csv.DictReader` on HELLO.csv → probe string | VERIFIED |
| Filename culture (Excel / RFC 4180 / TSV / semicolon locales) maps to this dialect | CONJECTURE (probe uses plain comma + header row) |
| Full csvkit / pandas / RFC 4180 feature recovery | UNVERIFIABLE from CPython stdlib csv 1.0 DictReader probe alone |
| bare `csvkit` / `csvcut` / `pandas` as verified CSV toolchain this leaf | REJECTED (csvkit apt ~10.6 MB / 29 pkgs; not installed; different CLI) |
