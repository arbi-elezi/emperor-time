# Jail pin — Python json module load for HELLO.json

Contemporaneous manual pin for the lost-json archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how JSON
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-json/HELLO.json` with
runnable dialect **VERIFIED** as CPython 3.13.5 stdlib `json` 2.0.9
under Linux x86_64
(`python3` + `json.load` on HELLO.json →
`EMPEROR-TIME-JSON-PROBE-OK`). Filename culture
(JSON Lines / JSON5 / JSONC / NDJSON)
remains **CONJECTURE** only for naming collisions. Identify fossils use `*.json`.
Bare `json` is **refused** as a route tag (substring collision with `jsonl` / `json5` / `jsonc`).
Bare `pyjson` / `json2.0` are **allowed** as route tags (family / version).
Bare `.json` is **allowed** as a route tag with
extension-boundary matching. Prefer `pyjson` /
`json2.0` / `.json`.
Toolchain is CPython stdlib `json` already on box (**zero new apt**).
Debian `jsonlint` 1.11.0-2 apt was simulated and **REJECTED** (~15 kB
archives / ~71 kB Installed-Size; unnecessary vs stdlib). This note supplies
the Jail pin so excavate can name the **verified** stdlib `json.load`
key lookup shape without inventing a full
jq / jsonschema / RFC 8259 suite claim for a
single-key probe. Distinct from the jq archaeology leaf (`*.jq` filter
programs) and from JavaScript (`.js` already extension-bounds so it does
not steal `.json`).

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Python 3 Library Reference — `json` — JSON encoder and decoder* |
| **Heading** | **`json.load`** — Deserialize `fp` (a `.read()`-supporting text or binary file containing a JSON document) to a Python object using the JSON-to-Python conversion table |
| **Dialect pinned** | **CPython stdlib `json` 2.0.9 `load`** with object key lookup → print `doc['probe']` — **not** full jq / jsonschema / RFC 8259 suite claim |
| **URL** | https://docs.python.org/3/library/json.html (Python docs — `json` module); CPython 3.13.5 on box; `json.__version__` → `2.0.9` |
| **Anchors** | `.json` document path; `json.load(fp)`; object key `probe` |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Python docs — `json.load`)

> Deserialize *fp* to a Python object using the JSON-to-Python
> conversion table.
>
> *fp* is a `.read()`-supporting text file or binary file containing
> the JSON document to be deserialized.

(Source: Python 3 Library Reference, section
**Basic Usage — `json.load`**,
https://docs.python.org/3/library/json.html
accessed 2026-09-28 Europe/Tirane.
Installed `python3 --version` reports Python 3.13.5 and
`json.__version__` reports `2.0.9`. Probe uses
`json.load(open('HELLO.json'))` so stdlib json
loads the named JSON document and prints the `probe` key value.
Format: JSON — see also module overview and RFC 7159 / ECMA-404 notes.)

### Why this heading (HELLO.json / excavate)

A minimal HELLO surface looks like a one-key JSON object with key
`probe` and a string value. That is exactly the pinned form:
**stdlib `json.load` + `doc['probe']`**, observe probe token at run time.

### Honesty

- VERIFIED: CPython 3.13.5 stdlib `json` 2.0.9 `load` on this HELLO.
- CONJECTURE: any claim that JSON Lines / JSON5 / JSONC / NDJSON / BSON are this dialect.
- UNVERIFIABLE: jq / jsonschema / full RFC 8259 recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, openjdk/Java (apt size); graphviz this turn (multi-dep); Debian `jsonlint` apt (unnecessary vs stdlib); bare `json` route tag (substring collision with jsonl/json5/jsonc); bare `jq` / `jsonlint` / `jsonschema` as verified *document* toolchain (jq already owns `*.jq`); `*.jsonl` / `*.json5` / `*.jsonc` / `*.tsv` fossils this leaf (defer).
