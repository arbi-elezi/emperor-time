# Boot probe — lost-tsv / HELLO.tsv

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~19:35 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **Python 3.13.5** stdlib `csv` (already on box; module `__version__` reports `1.0`) |
| Binary / module | `/usr/bin/python3` + `csv.DictReader(..., delimiter='\t')` |
| Reported | `Python 3.13.5` / `csv` 1.0 (`python3 --version`; `python3 -c 'import csv; print(csv.__version__)'`) |
| Install | already on box (CPython stdlib) — **zero new Apt Worthy Spend** this leaf; Debian `csvkit` / `miller` / `tsv-utils` apt REJECTED vs zero-apt stdlib; still prefer over deferred TeXlive / C++ / graphviz multi-dep apt |

Probe used `python3` + stdlib `csv.DictReader` with `delimiter='\t'` on a minimal
TSV header/`probe` column with a single data row.
Identify fossils use `*.tsv` (TSV tabular peer leaf after XLSX archive chain / CSV peer). Prefer `tsv` / `pytsv` / `tab-separated` / `.tsv`.
Bare `tsv` / `pytsv` / `tab-separated` are **allowed** as route tags (format / family / format-name).
Bare `.tsv` is **allowed** with extension-boundary matching (do not invent
`.tsvfoo` prefix hits). Bare `csvkit` / `miller` / `pandas` refused this leaf (tabular-suite discourse / apt surface).
TSV tabular leaf after XLSX; treats TSV as peer fossil not house twin language.
Do **not** claim a full csvkit / miller / pandas / RFC 4180 suite recovery from a CPython
stdlib `DictReader`+tab-delimiter probe alone — this leaf pins stdlib
`csv` DictReader with `delimiter='\t'` and the probe token printed. Do **not** claim Debian
`csvkit` / `miller` / `tsv-utils` as the verified toolchain this leaf (apt REJECTED).
Distinct from CSV (`*.csv` / csv), JSON (`*.json` / json), XLSX (`*.xlsx` / zipfile),
and HTML (`*.html` / tidy).
Do **not** steal plain `*.csv` ownership — that remains the csv leaf.
Defer `*.jsonl` this turn.

## Commands (VERIFIED)

```text
$ python3 --version
Python 3.13.5

$ python3 -c 'import csv; print(csv.__version__)'
1.0

$ python3 -c "import csv; print(next(csv.DictReader(open('HELLO.tsv', newline=''), delimiter='\t'))['probe'])"
EMPEROR-TIME-TSV-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| Host runs stdlib `csv.DictReader` with `delimiter='\t'` on HELLO.tsv → probe string | VERIFIED |
| Filename culture (Excel TSV / RFC 4180 / semicolon locales / CSV) maps to this dialect | CONJECTURE (probe uses plain tab + header row) |
| Full csvkit / miller / pandas / RFC 4180 feature recovery | UNVERIFIABLE from CPython stdlib csv 1.0 DictReader+tab probe alone |
| bare `csvkit` / `miller` / `pandas` / `tsv-utils` as verified TSV toolchain this leaf | REJECTED (apt / different CLI; not installed) |
