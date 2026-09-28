# Boot probe — lost-jsonl / HELLO.jsonl

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~20:03 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **Python 3.13.5** stdlib `json` (already on box; module `__version__` reports `2.0.9`) |
| Binary / module | `/usr/bin/python3` + per-line `json.loads` |
| Reported | `Python 3.13.5` / `json` 2.0.9 (`python3 --version`; `python3 -c 'import json; print(json.__version__)'`) |
| Install | already on box (CPython stdlib) — **zero new Apt Worthy Spend** this leaf; Debian `jsonlint` apt REJECTED vs zero-apt stdlib; still prefer over deferred TeXlive / C++ / graphviz multi-dep apt |

Probe used `python3` + stdlib `json.loads` on each non-empty line of a minimal
JSON Lines (NDJSON) file with a `probe` key on the first object line.
Identify fossils use `*.jsonl` (JSON Lines peer leaf after TSV). Prefer `jsonl` / `pyjsonl` / `ndjson` / `.jsonl`.
Bare `jsonl` / `pyjsonl` / `ndjson` are **allowed** as route tags (format / family / format-name).
Bare `json` remains **refused** (substring collision with jsonl / json5 / jsonc; owned refusal from the JSON leaf).
Bare `.jsonl` is **allowed** with extension-boundary matching (do not invent
`.jsonlfoo` prefix hits). Bare `jq` / `jsonlint` / `pandas` / `ijson` refused this leaf (document-suite discourse / apt surface / jq already owns `*.jq`).
JSON Lines leaf after TSV; treats JSONL as peer fossil not house twin language.
Do **not** claim a full jq / jsonschema / RFC 8259 / NDJSON suite recovery from a CPython
stdlib per-line `json.loads` probe alone — this leaf pins stdlib
`json.loads` on each line and the probe token printed. Do **not** claim Debian
`jsonlint` or `jq` as the verified JSONL-*document* toolchain this leaf.
Distinct from JSON (`*.json` / json.load), TSV (`*.tsv` / csv+tab), CSV (`*.csv` / csv),
and jq (`*.jq` filters).
Do **not** steal plain `*.json` ownership — that remains the json leaf.
Defer TeX/LaTeX / C++ / openjdk-as-owner / graphviz / CLIPS / embeddings this turn.

## Commands (VERIFIED)

```text
$ python3 --version
Python 3.13.5

$ python3 -c 'import json; print(json.__version__)'
2.0.9

$ python3 -c "import json; print(next(json.loads(l)['probe'] for l in open('HELLO.jsonl') if l.strip() and 'probe' in json.loads(l)))"
EMPEROR-TIME-JSONL-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| Host runs stdlib per-line `json.loads` on HELLO.jsonl → probe string | VERIFIED |
| Filename culture (JSON Lines / NDJSON / JSON5 / JSONC / BSON) maps to this dialect | CONJECTURE (probe uses plain one-object-per-line UTF-8) |
| Full jq / jsonschema / RFC 8259 / streaming ijson feature recovery | UNVERIFIABLE from CPython stdlib json 2.0.9 per-line loads probe alone |
| bare `jq` / `jsonlint` / `pandas` / `ijson` as verified JSONL toolchain this leaf | REJECTED (apt / different CLI; jq owns `*.jq`) |
