# Jail pin — Python configparser ConfigParser.read/get for HELLO.ini

Contemporaneous manual pin for the lost-ini archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how INI
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-ini/HELLO.ini` with
runnable dialect **VERIFIED** as CPython 3.13.5 stdlib `configparser`
under Linux x86_64
(`python3` + `ConfigParser.read` / `get` on HELLO.ini →
`EMPEROR-TIME-INI-PROBE-OK`). Filename culture
(Windows Registry extended INI / configobj / `.cfg` / `.conf`)
remains **CONJECTURE** only for naming collisions. Identify fossils use `*.ini`.
Bare `ini` / `pyini` / `configparser` are **allowed** as route tags (format / family / module).
Bare `.ini` is **allowed** as a route tag with
extension-boundary matching. Prefer `ini` /
`pyini` / `configparser` / `.ini`.
Toolchain is CPython stdlib `configparser` already on box (**zero new apt**).
Debian `crudini` 0.9.6-1 apt was simulated with `python3-iniparse` and **REJECTED** (~43 kB
archives / ~185 kB Installed-Size; unnecessary vs stdlib). This note supplies
the Jail pin so excavate can name the **verified** stdlib `ConfigParser`
section/option lookup shape without inventing a full
crudini / configobj / Windows Registry INI suite claim for a
single-option probe. Distinct from the TOML archaeology leaf (`*.toml` /
tomlq) and from JSON (`*.json` / stdlib json).

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Python 3 Library Reference — `configparser` — Configuration file parser* |
| **Heading** | **`ConfigParser.read`** / **`ConfigParser.get`** — Attempt to read and parse filenames; get an option value for the named section |
| **Dialect pinned** | **CPython stdlib `configparser` `ConfigParser.read`/`get`** with section `probe` option `token` → print value — **not** full crudini / configobj / Windows Registry INI suite claim |
| **URL** | https://docs.python.org/3/library/configparser.html (Python docs — `configparser` module); CPython 3.13.5 on box |
| **Anchors** | `.ini` document path; `ConfigParser.read(filenames)`; `ConfigParser.get(section, option)`; section `probe` / option `token` |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Python docs — `ConfigParser.read` / `get`)

> Attempt to read and parse an iterable of filenames, returning a list
> of filenames which were successfully parsed.
>
> Get an option value for the named section.

(Source: Python 3 Library Reference, sections
**ConfigParser Objects — `read`** and **`get`**,
https://docs.python.org/3/library/configparser.html
accessed 2026-09-28 Europe/Tirane.
Installed `python3 --version` reports Python 3.13.5.
Probe uses
`ConfigParser().read('HELLO.ini')` then `get('probe','token')` so stdlib
configparser loads the named INI document and prints the option value.
Format: INI-style configuration — see also module overview and
Supported INI File Structure.)

### Why this heading (HELLO.ini / excavate)

A minimal HELLO surface looks like a one-section INI file with section
`probe` and option `token` holding a string value. That is exactly the pinned form:
**stdlib `ConfigParser.read` + `get(section, option)`**, observe probe token at run time.

### Honesty

- VERIFIED: CPython 3.13.5 stdlib `configparser` `ConfigParser.read`/`get` on this HELLO.
- CONJECTURE: any claim that Windows Registry extended INI / configobj / `.cfg` / `.conf` are this dialect.
- UNVERIFIABLE: crudini / full multi-dialect INI recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, openjdk/Java (apt size); graphviz this turn (multi-dep); Debian `crudini` apt (unnecessary vs stdlib); bare `crudini` / `configobj` as verified toolchain; `*.cfg` / `*.conf` / `*.tsv` / `*.jsonl` fossils this leaf (defer).
