# Boot probe — lost-yaml / HELLO.yaml

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~12:23 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **yq** 3.4.3-2 (Debian trixie; kislyuk/yq Python jq-wrapper) |
| Binary | `/usr/bin/yq` |
| Reported | `yq 3.4.3` (`yq --version`) |
| Install | apt this leaf (~267 kB archive across yq + python3-yaml + python3-tomlkit + python3-xmltodict + python3-argcomplete; Installed-Size sum ~1063 kB; jq already on box; Worthy Spend after XML; still prefer over TeXlive / C++ / openjdk / graphviz multi-dep apt) |

Probe used `yq -r .probe HELLO.yaml` on a minimal
YAML mapping with a single string under `probe` (kislyuk/yq forwards
`-r` to jq for raw string output).
Identify fossils use `*.yaml` / `*.yml` (YAML peer leaf after jq/XML).
Prefer `yq` / `kislyuk-yq` / `yq3.4` / `yaml` / `.yaml` / `.yml`.
Bare `yaml` is **allowed** as a route tag (language name; word-boundary).
Bare `yq` is **allowed** as a route tag (tool binary name).
Bare `kislyuk-yq` / `yq3.4` are **allowed** as route tags (family / version).
Bare `.yaml` / `.yml` are **allowed** with extension-boundary matching (do not invent
`.yamlfoo` / `.ymlfoo` prefix hits). YAML document leaf after jq/XML;
treats YAML as peer fossil not house twin language. Do **not**
claim a full mikefarah/yq (Go) / YAML 1.2 suite / JSON Schema recovery from a Debian
kislyuk `yq` raw-string probe alone — this leaf pins kislyuk/yq YAML→JSON→jq
filter evaluation with raw string output.

## Commands (VERIFIED)

```text
$ which yq
/usr/bin/yq

$ yq --version
yq 3.4.3

$ yq -r .probe HELLO.yaml
EMPEROR-TIME-YQ-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| Host runs `yq -r .probe HELLO.yaml` → probe string | VERIFIED |
| Filename culture (Kubernetes / Ansible / CloudFormation YAML) maps to this dialect | CONJECTURE (probe uses plain mapping + string key) |
| Full mikefarah/yq (Go) / YAML 1.2 / JSON Schema feature recovery | UNVERIFIABLE from Debian kislyuk yq 3.4.3 CLI probe alone |
| bare `mikefarah-yq` / `go-yq` as verified YAML toolchain | REJECTED (not used this leaf; different CLI) |
