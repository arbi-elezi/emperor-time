# Jail pin — yq Synopsis (jq filter + YAML file) for HELLO.yaml

Contemporaneous manual pin for the lost-yaml archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how YAML
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-yaml/HELLO.yaml` with
runnable dialect **VERIFIED** as kislyuk/yq 3.4.3
under Linux x86_64
(`yq -r .probe HELLO.yaml` →
`EMPEROR-TIME-YQ-PROBE-OK`). Filename culture
(Kubernetes / Ansible / CloudFormation) remains
**CONJECTURE** only for naming collisions. Identify fossils use `*.yaml` /
`*.yml`.
Bare `yaml` is **allowed** as a route tag (language name).
Bare `yq` / `kislyuk-yq` / `yq3.4` are **allowed** as route tags (tool / family / version).
Bare `.yaml` / `.yml` are **allowed** as route tags with
extension-boundary matching. Prefer `yq` /
`kislyuk-yq` / `yq3.4` / `yaml` / `.yaml` / `.yml`.
Toolchain is Debian package `yq` 3.4.3-2 providing
`/usr/bin/yq` (kislyuk/yq Python jq-wrapper; depends on `jq`). This note supplies
the Jail pin so excavate can name the **verified** kislyuk/yq
YAML→JSON→jq filter evaluation shape without inventing a full mikefarah/yq (Go) /
YAML 1.2 / JSON Schema suite claim for a
string-output probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *yq documentation — Synopsis* |
| **Heading** | **Synopsis** — `yq` takes YAML input, converts it to JSON, and pipes it to jq; input filename(s) as arguments; jq options such as `-r` are forwarded |
| **Dialect pinned** | **kislyuk/yq 3.4 CLI** with YAML mapping + jq filter → `yq -r .probe FILE.yaml` — **not** full mikefarah/yq (Go) / YAML 1.2 suite claim |
| **URL** | https://kislyuk.github.io/yq/ (yq documentation — Synopsis); Debian package `yq` 3.4.3-2; installed `yq --version` |
| **Anchors** | `.yaml` / `.yml` document path as file argument; jq filter `.probe`; `-r` raw-output forwarded to jq |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from yq documentation — Synopsis)

> `yq` takes YAML input, converts it to JSON, and pipes it to jq:
>
> ```
> cat input.yml | yq .foo.bar
> ```
>
> Like in `jq`, you can also specify input filename(s) as arguments:
>
> ```
> yq .foo.bar input.yml
> ```
>
> By default, no conversion of `jq` output is done. Use the `--yaml-output`/`-y`
> option to convert it back into YAML.
>
> All other command line arguments are forwarded to `jq`.

(Source: yq documentation, section
**Synopsis**,
https://kislyuk.github.io/yq/
accessed 2026-09-28 Europe/Tirane.
Installed `yq --version` reports yq 3.4.3 and matches the
CLI filter+file surface. Probe uses
`yq -r .probe HELLO.yaml` so yq
loads the named YAML document, converts to JSON, runs the jq filter with
raw string output, and prints the probe
string. Language: YAML — see also the jq Manual.)

### Why this heading (HELLO.yaml / excavate)

A minimal HELLO surface looks like a YAML mapping with a single string
under `probe`. That is exactly the pinned form:
**`yq -r .probe FILE.yaml`**, observe string print at run time.

### Honesty

- VERIFIED: Debian `yq` (kislyuk 3.4.3-2) on this HELLO.
- CONJECTURE: any claim that Kubernetes / Ansible / CloudFormation YAML are this dialect.
- UNVERIFIABLE: mikefarah/yq (Go) / YAML 1.2 / JSON Schema recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, openjdk/Java (apt size); graphviz this turn (multi-dep); tidy/HTML this turn (separate peer); bare `mikefarah-yq` / `go-yq` as verified toolchain.
