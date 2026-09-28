# Jail pin — Python json.loads per line for HELLO.jsonl

Contemporaneous manual pin for the lost-jsonl archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how JSON Lines
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-jsonl/HELLO.jsonl` with
runnable dialect **VERIFIED** as CPython 3.13.5 stdlib `json` 2.0.9
under Linux x86_64
(`python3` + per-line `json.loads` on HELLO.jsonl →
`EMPEROR-TIME-JSONL-PROBE-OK`). Filename culture
(JSON Lines / NDJSON / JSON5 / JSONC / BSON) remains
**CONJECTURE** only for naming collisions. Identify fossils use `*.jsonl`.
Bare `jsonl` / `pyjsonl` / `ndjson` are **allowed** as route tags (format / family / format-name).
Bare `json` remains **refused** (substring collision with jsonl / json5 / jsonc; JSON leaf).
Bare `.jsonl` is **allowed** as a route tag with
extension-boundary matching. Prefer `jsonl` /
`pyjsonl` / `ndjson` / `.jsonl`.
Bare `jq` / `jsonlint` / `pandas` / `ijson` are **refused** this leaf (document-suite discourse / apt surface / jq owns `*.jq`).
Do **not** steal plain `*.json` ownership from the json leaf;
a `.jsonl` is a distinct line-delimited JSON fossil (JSON is not a framed protocol).
Toolchain is CPython stdlib `json` already on box (**zero new apt**).
Debian `jsonlint` apt was considered and **REJECTED**
as the verified leaf owner vs stdlib (same Worthy Spend honesty as lost-json). This note supplies
the Jail pin so excavate can name the **verified** stdlib
`json.loads`-per-line shape on a JSONL without inventing a full
jq / jsonschema / RFC 8259 suite claim for a
single-key probe. Distinct from the JSON archaeology leaf (`*.json` /
json.load), TSV (`*.tsv` / csv+tab), CSV (`*.csv` / csv),
and jq (`*.jq` filters).
Chain Jail leaf only — excavate fossil pin, not a vendored foreign JSONL skill.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Python 3 Library Reference — `json` — JSON encoder and decoder* |
| **Heading** | **`json.loads`** (per line) — Identical to `load()`, but instead of a file-like object, deserialize *s* (a `str`, `bytes` or `bytearray` instance containing a JSON document) to a Python object; applied once per non-empty line for JSON Lines / NDJSON |
| **Dialect pinned** | **CPython stdlib `json` 2.0.9 `loads`** per line with object key lookup → print `obj['probe']` — **not** full jq / jsonschema / RFC 8259 / streaming suite claim |
| **URL** | https://docs.python.org/3/library/json.html (Python docs — `json` module); CPython 3.13.5 on box; `json.__version__` → `2.0.9`; CLI also documents `--json-lines` (parse every input line as separate JSON object) |
| **Anchors** | `.jsonl` document path; `open(...)` line iteration; `json.loads(line)`; object key `probe` |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Python docs — `json.loads` / CLI `--json-lines`)

> Identical to `load()`, but instead of a file-like object, deserialize
> *s* (a `str`, `bytes` or `bytearray` instance containing a JSON
> document) to a Python object using this conversion table.
>
> `--json-lines` — Parse every input line as separate JSON object.

(Source: Python 3 Library Reference, section
**Basic Usage — `json.loads`** and **Command-line interface — `--json-lines`**,
https://docs.python.org/3/library/json.html
accessed 2026-09-28 Europe/Tirane.
Installed `python3 --version` reports Python 3.13.5.
`json.__version__` reports `2.0.9`.
Probe uses per-line
`json.loads(line)` on HELLO.jsonl
so stdlib json deserializes each line as its own JSON document and prints the `probe` key.
Format: JSON Lines / NDJSON — one JSON value per line. The docs also note JSON is not a framed protocol for repeated `dump()` into one file, which is why line-delimited JSONL is a distinct fossil from a single `*.json` document.)

### Why this heading (HELLO.jsonl / excavate)

A minimal HELLO surface looks like one JSON object per line with a
`probe` key on the first object. That is exactly the pinned form:
**stdlib `json.loads` per line on `.jsonl`**, observe key value at run time.

### Honesty

- VERIFIED: CPython 3.13.5 stdlib `json.loads` per line on this HELLO (one object per line).
- CONJECTURE: any claim that NDJSON / JSON5 / JSONC / BSON / full RFC 8259 streaming are this dialect.
- UNVERIFIABLE: Debian jsonlint / jq / pandas / ijson / full multi-dialect JSONL recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, jq/jsonlint/pandas/ijson as leaf owner (apt size / jq owns `*.jq`); graphviz this turn (multi-dep); Debian `jsonlint` apt (unnecessary vs stdlib); bare `json` as verified JSONL tag (substring collision; JSON leaf); stealing plain `*.json` ownership from the json leaf; vendoring foreign JSONL skills as this Jail pin.
