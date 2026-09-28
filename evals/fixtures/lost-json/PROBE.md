# Boot probe — lost-json / HELLO.json

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~13:26 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **Python 3.13.5** stdlib `json` (already on box; module `__version__` reports `2.0.9`) |
| Binary / module | `/usr/bin/python3` + `json.load` |
| Reported | `Python 3.13.5` / `json` 2.0.9 (`python3 --version`; `python3 -c 'import json; print(json.__version__)'`) |
| Install | already on box (CPython stdlib) — **zero new Apt Worthy Spend** this leaf; Debian `jsonlint` 1.11.0-2 apt simulated at ~15 kB archives / ~71 kB Installed-Size — **REJECTED** vs zero-apt stdlib (tiny but unnecessary); still prefer over deferred TeXlive / C++ / openjdk / graphviz multi-dep apt |

Probe used `python3` + stdlib `json.load` on a minimal
JSON object with a `probe` key.
Identify fossils use `*.json` (JSON document peer leaf after CSV). Prefer `pyjson` / `json2.0` / `.json`.
Bare `json` is **refused** as a route tag (substring collision with `jsonl` / `json5` / `jsonc`; 4-char tokens use substring match).
Bare `pyjson` / `json2.0` are **allowed** as route tags (family / version).
Bare `.json` is **allowed** with extension-boundary matching (do not invent
`.jsonfoo` / `.jsonl` / `.json5` / `.jsonc` prefix hits). JSON document leaf after CSV;
treats JSON as peer fossil not house twin language. Do **not**
claim a full jq / jsonschema / RFC 8259 suite recovery from a CPython
stdlib `json.load` probe alone — this leaf pins stdlib `json.load`
key lookup with the probe token printed. Do **not** claim Debian
`jsonlint` or `jq` as the verified JSON-*document* toolchain this leaf
(`jq` already owns `*.jq` filter programs; JS carefully extension-bounds
so `.js` does not steal `.json`).

## Commands (VERIFIED)

```text
$ python3 --version
Python 3.13.5

$ python3 -c 'import json; print(json.__version__)'
2.0.9

$ python3 -c "import json; print(json.load(open('HELLO.json'))['probe'])"
EMPEROR-TIME-JSON-PROBE-OK
```
