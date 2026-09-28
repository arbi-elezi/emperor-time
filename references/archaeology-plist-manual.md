# Jail pin — Python plistlib.load for HELLO.plist

Contemporaneous manual pin for the lost-plist archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how plist
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-plist/HELLO.plist` with
runnable dialect **VERIFIED** as CPython 3.13.5 stdlib `plistlib`
under Linux x86_64
(`python3` + `plistlib.load` on HELLO.plist →
`EMPEROR-TIME-PLIST-PROBE-OK`). Filename culture
(NeXTSTEP binary plist / OpenStep / macOS `plutil`)
remains **CONJECTURE** only for naming collisions. Identify fossils use `*.plist`.
Bare `plist` / `pyplist` / `plistlib` are **allowed** as route tags (format / family / module).
Bare `.plist` is **allowed** as a route tag with
extension-boundary matching. Prefer `plist` /
`pyplist` / `plistlib` / `.plist`.
Toolchain is CPython stdlib `plistlib` already on box (**zero new apt**).
Debian `libplist-utils` 2.6.0-2+b1 apt was simulated with `libplist-2.0-4` and **REJECTED** (~68 kB
archives / ~184 kB Installed-Size; unnecessary vs stdlib). This note supplies
the Jail pin so excavate can name the **verified** stdlib `plistlib`
XML load shape without inventing a full
plutil / libplist / NeXTSTEP binary-plist suite claim for a
single-key probe. Distinct from the XML archaeology leaf (`*.xml` /
xmllint) and from JSON (`*.json` / stdlib json).

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Python 3 Library Reference — `plistlib` — Generate and parse Apple `.plist` files* |
| **Heading** | **`plistlib.load`** — Read a `.plist` file from a binary file object; return the unpacked root object |
| **Dialect pinned** | **CPython stdlib `plistlib` `load`** with XML FMT top-level dict key `probe` → print value — **not** full plutil / libplist / NeXTSTEP binary-plist suite claim |
| **URL** | https://docs.python.org/3/library/plistlib.html (Python docs — `plistlib` module); CPython 3.13.5 on box |
| **Anchors** | `.plist` document path; `plistlib.load(fp)`; XML property list; top-level dict key `probe` |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Python docs — `plistlib.load`)

> Read a .plist file. fp should be a readable and binary file object.
> Return the unpacked root object (which usually is a dictionary).

(Source: Python 3 Library Reference, section
**plistlib — Generate and parse Apple `.plist` files — `load`**,
https://docs.python.org/3/library/plistlib.html
accessed 2026-09-28 Europe/Tirane.
Installed `python3 --version` reports Python 3.13.5.
Probe uses
`plistlib.load(open('HELLO.plist','rb'))['probe']` so stdlib
plistlib loads the named XML property-list document and prints the key value.
Format: Apple XML property list — see also module overview and
FMT_XML / FMT_BINARY.)

### Why this heading (HELLO.plist / excavate)

A minimal HELLO surface looks like a one-key XML property list with
top-level dict key `probe` holding a string value. That is exactly the pinned form:
**stdlib `plistlib.load`**, observe probe token at run time.

### Honesty

- VERIFIED: CPython 3.13.5 stdlib `plistlib` `load` on this HELLO (XML FMT).
- CONJECTURE: any claim that NeXTSTEP binary plist / OpenStep / macOS plutil are this dialect.
- UNVERIFIABLE: libplist / full multi-dialect plist recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, openjdk/Java (apt size); graphviz this turn (multi-dep); Debian `libplist-utils` apt (unnecessary vs stdlib); bare `plutil` / `libplist` as verified toolchain; `*.cfg` / `*.conf` / `*.tsv` / `*.jsonl` fossils this leaf (defer).
