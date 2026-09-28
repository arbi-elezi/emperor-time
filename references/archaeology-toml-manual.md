# Jail pin — yq documentation TOML support (tomlq) for HELLO.toml

Contemporaneous manual pin for the lost-toml archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how TOML
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-toml/HELLO.toml` with
runnable dialect **VERIFIED** as kislyuk/tomlq 3.4.3
under Linux x86_64
(`tomlq -r .probe HELLO.toml` →
`EMPEROR-TIME-TOMLQ-PROBE-OK`). Filename culture
(Cargo / pyproject / Hugo) remains
**CONJECTURE** only for naming collisions. Identify fossils use `*.toml`.
Bare `toml` is **allowed** as a route tag (language name).
Bare `tomlq` / `kislyuk-tomlq` / `tomlq3.4` are **allowed** as route tags (tool / family / version).
Bare `.toml` is **allowed** as a route tag with
extension-boundary matching. Prefer `tomlq` /
`kislyuk-tomlq` / `tomlq3.4` / `toml` / `.toml`.
Toolchain is Debian package `yq` 3.4.3-2 providing
`/usr/bin/tomlq` (kislyuk/yq TOML jq-wrapper sibling; already installed with YAML leaf). This note supplies
the Jail pin so excavate can name the **verified** kislyuk/tomlq
TOML→JSON→jq filter evaluation shape without inventing a full Taplo /
BurntSushi toml / TOML 1.0 suite claim for a
string-output probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *yq documentation — TOML support* |
| **Heading** | **TOML support** — `tomlq` uses tomlkit to transcode TOML to JSON, then pipes it to jq; input filename(s) as arguments; jq options such as `-r` are forwarded |
| **Dialect pinned** | **kislyuk/tomlq 3.4 CLI** with TOML mapping + jq filter → `tomlq -r .probe FILE.toml` — **not** full Taplo / BurntSushi toml suite claim |
| **URL** | https://kislyuk.github.io/yq/ (yq documentation — TOML support); Debian package `yq` 3.4.3-2; installed `tomlq --version` |
| **Anchors** | `.toml` document path as file argument; jq filter `.probe`; `-r` raw-output forwarded to jq |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from yq documentation — TOML support)

> `yq` supports TOML as well. The `yq` package installs an executable, `tomlq`,
> which uses the tomlkit library to transcode TOML to JSON, then pipes it to `jq`.
> Roundtrip transcoding is available with the `tomlq --toml-output`/`tomlq -t`
> option. Use `tomlq --toml-roundtrip`/`tomlq -T` to preserve TOML comments,
> whitespace, and formatting metadata while editing.

(Source: yq documentation, section
**TOML support**,
https://kislyuk.github.io/yq/
accessed 2026-09-28 Europe/Tirane.
Installed `tomlq --version` reports tomlq 3.4.3 and matches the
CLI filter+file surface. Probe uses
`tomlq -r .probe HELLO.toml` so tomlq
loads the named TOML document, converts to JSON, runs the jq filter with
raw string output, and prints the probe
string. Language: TOML — see also the jq Manual / YAML yq leaf.)

### Why this heading (HELLO.toml / excavate)

A minimal HELLO surface looks like a TOML key/value with a single string
under `probe`. That is exactly the pinned form:
**`tomlq -r .probe FILE.toml`**, observe string print at run time.

### Honesty

- VERIFIED: Debian `tomlq` (kislyuk yq 3.4.3-2 sibling) on this HELLO.
- CONJECTURE: any claim that Cargo / pyproject / Hugo TOML are this dialect.
- UNVERIFIABLE: Taplo / BurntSushi toml / TOML 1.0 recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, openjdk/Java (apt size); tidy/HTML this turn (separate peer); graphviz this turn (multi-dep); bare `taplo` / `toml-cli` as verified toolchain.
