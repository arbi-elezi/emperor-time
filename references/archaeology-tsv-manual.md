# Jail pin — Python csv.DictReader with tab delimiter for HELLO.tsv

Contemporaneous manual pin for the lost-tsv archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how TSV
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-tsv/HELLO.tsv` with
runnable dialect **VERIFIED** as CPython 3.13.5 stdlib `csv` 1.0
under Linux x86_64
(`python3` + `csv.DictReader(..., delimiter='\t')` on HELLO.tsv →
`EMPEROR-TIME-TSV-PROBE-OK`). Filename culture
(Excel TSV / RFC 4180 / CSV / semicolon locales) remains
**CONJECTURE** only for naming collisions. Identify fossils use `*.tsv`.
Bare `tsv` / `pytsv` / `tab-separated` are **allowed** as route tags (format / family / format-name).
Bare `.tsv` is **allowed** as a route tag with
extension-boundary matching. Prefer `tsv` /
`pytsv` / `tab-separated` / `.tsv`.
Bare `csvkit` / `miller` / `pandas` / `tsv-utils` are **refused** this leaf (tabular-suite discourse / apt surface).
Do **not** steal plain `*.csv` ownership from the csv leaf;
a `.tsv` is a distinct tab-delimited tabular fossil.
Toolchain is CPython stdlib `csv` already on box (**zero new apt**).
Debian `csvkit` / `miller` / `tsv-utils` apt were considered and **REJECTED**
as the verified leaf owner vs stdlib (same Worthy Spend honesty as lost-csv). This note supplies
the Jail pin so excavate can name the **verified** stdlib `csv`
DictReader+tab shape on a TSV without inventing a full
csvkit / miller / pandas suite claim for a
single-column probe. Distinct from the CSV archaeology leaf (`*.csv` /
csv), JSON (`*.json` / json), XLSX (`*.xlsx` / zipfile),
and HTML (`*.html` / tidy).
Chain Jail leaf only — excavate fossil pin, not a vendored foreign tabular skill.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Python 3 Library Reference — `csv` — CSV File Reading and Writing* |
| **Heading** | **`csv.DictReader` with `delimiter='\t'`** — maps each tab-separated row to a `dict` whose keys come from the optional `fieldnames` parameter, or from the first row of the file when omitted |
| **Dialect pinned** | **CPython stdlib `csv` 1.0 DictReader** with `delimiter='\t'` and header-row fieldnames → print `row['probe']` — **not** full csvkit / miller / pandas suite claim |
| **URL** | https://docs.python.org/3/library/csv.html (Python docs — `csv` module); CPython 3.13.5 on box; `csv.__version__` → `1.0` |
| **Anchors** | `.tsv` document path; `open(..., newline='')`; `csv.DictReader(..., delimiter='\t')`; column key `probe` |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Python docs — `csv.DictReader` / dialect `delimiter`)

> Create an object that operates like a regular reader but maps the
> information in each row to a `dict` whose keys are given by the
> optional fieldnames parameter.
>
> The fieldnames parameter is a sequence. If fieldnames is omitted, the
> values in the first row of file f will be used as the fieldnames and
> will be omitted from the results.
>
> Dialect.delimiter — A one-character string used to separate fields. It defaults to `','`.

(Source: Python 3 Library Reference, section
**csv — CSV File Reading and Writing — DictReader objects / Dialects and Formatting Parameters**,
https://docs.python.org/3/library/csv.html
accessed 2026-09-28 Europe/Tirane.
Installed `python3 --version` reports Python 3.13.5.
`csv.__version__` reports `1.0`.
Probe uses
`next(csv.DictReader(open('HELLO.tsv', newline=''), delimiter='\t'))['probe']`
so stdlib csv loads the named `.tsv` with tab delimiter and prints the column token.
Format: tab-separated header row + one data row.)

### Why this heading (HELLO.tsv / excavate)

A minimal HELLO surface looks like a one-table tab-separated text file with
a `probe` header and a single data cell holding a probe token. That is exactly the pinned form:
**stdlib `csv.DictReader` with `delimiter='\t'` on `.tsv`**, observe column value at run time.

### Honesty

- VERIFIED: CPython 3.13.5 stdlib `csv.DictReader` with `delimiter='\t'` on this HELLO (tab + header row).
- CONJECTURE: any claim that Excel TSV / RFC 4180 / CSV / semicolon locales / full csvkit are this dialect.
- UNVERIFIABLE: Debian csvkit / miller / tsv-utils / pandas / full multi-dialect tabular recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, csvkit/miller/pandas as leaf owner (apt size); graphviz this turn (multi-dep); Debian `csvkit` / `miller` / `tsv-utils` apt (unnecessary vs stdlib); bare `csvkit` / `miller` / `pandas` as verified toolchain; `*.jsonl` fossils this leaf (defer); stealing plain `*.csv` ownership from the csv leaf; vendoring foreign tabular skills as this Jail pin.
