# Jail pin — Python csv module DictReader for HELLO.csv

Contemporaneous manual pin for the lost-csv archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how CSV
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-csv/HELLO.csv` with
runnable dialect **VERIFIED** as CPython 3.13.5 stdlib `csv` 1.0
under Linux x86_64
(`python3` + `csv.DictReader` on HELLO.csv →
`EMPEROR-TIME-CSV-PROBE-OK`). Filename culture
(Excel / RFC 4180 / TSV / semicolon locales) remains
**CONJECTURE** only for naming collisions. Identify fossils use `*.csv`.
Bare `csv` is **allowed** as a route tag (format name; word-boundary).
Bare `pycsv` / `csv1.0` are **allowed** as route tags (family / version).
Bare `.csv` is **allowed** as a route tag with
extension-boundary matching. Prefer `csv` /
`pycsv` / `csv1.0` / `.csv`.
Toolchain is CPython stdlib `csv` already on box (**zero new apt**).
Debian `csvkit` 2.0.1-3 apt was simulated and **REJECTED** (~10.6 MB
archives / ~53 MB Installed-Size / 29 new packages). This note supplies
the Jail pin so excavate can name the **verified** stdlib `csv`
DictReader column lookup shape without inventing a full
csvkit / pandas / RFC 4180 suite claim for a
single-column probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Python 3 Library Reference — `csv` — CSV File Reading and Writing* |
| **Heading** | **`csv.DictReader`** — maps each row to a `dict` whose keys come from the optional `fieldnames` parameter, or from the first row of the file when omitted |
| **Dialect pinned** | **CPython stdlib `csv` 1.0 DictReader** with header-row fieldnames → print `row['probe']` — **not** full csvkit / pandas / RFC 4180 suite claim |
| **URL** | https://docs.python.org/3/library/csv.html (Python docs — `csv` module); CPython 3.13.5 on box; `csv.__version__` → `1.0` |
| **Anchors** | `.csv` document path; `open(..., newline='')`; `csv.DictReader`; column key `probe` |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Python docs — `csv.DictReader`)

> Create an object that operates like a regular reader but maps the
> information in each row to a `dict` whose keys are given by the
> optional fieldnames parameter.
>
> The fieldnames parameter is a sequence. If fieldnames is omitted, the
> values in the first row of file f will be used as the fieldnames and
> will be omitted from the results.

(Source: Python 3 Library Reference, section
**`csv.DictReader`**,
https://docs.python.org/3/library/csv.html
accessed 2026-09-28 Europe/Tirane.
Installed `python3 --version` reports Python 3.13.5 and
`csv.__version__` reports `1.0`. Probe uses
`csv.DictReader(open('HELLO.csv', newline=''))` so stdlib csv
loads the named CSV document, takes the header row as fieldnames, and
prints the `probe` column value. Format: CSV — see also module overview
and `newline=''` footnote.)

### Why this heading (HELLO.csv / excavate)

A minimal HELLO surface looks like a one-column CSV with header
`probe` and a single data row. That is exactly the pinned form:
**stdlib `csv.DictReader` + `row['probe']`**, observe probe token at run time.

### Honesty

- VERIFIED: CPython 3.13.5 stdlib `csv` 1.0 DictReader on this HELLO.
- CONJECTURE: any claim that Excel / RFC 4180 / TSV / semicolon locales are this dialect.
- UNVERIFIABLE: csvkit / pandas / full RFC 4180 recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, openjdk/Java (apt size); graphviz this turn (multi-dep); Debian `csvkit` apt (~10.6 MB / 29 pkgs); bare `csvkit` / `csvcut` / `pandas` as verified toolchain; `*.tsv` fossil this leaf (defer; peer tool ownership unclear).
