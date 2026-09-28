# Boot probe — lost-toml / HELLO.toml

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~12:43 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **yq** 3.4.3-2 (Debian trixie; kislyuk/yq ships `tomlq`) |
| Binary | `/usr/bin/tomlq` |
| Reported | `tomlq 3.4.3` (`tomlq --version`) |
| Install | already on box from YAML leaf (yq apt); **zero new Apt Worthy Spend** this leaf (tomlq peer of yq; still prefer over TeXlive / C++ / openjdk / tidy / graphviz multi-dep apt) |

Probe used `tomlq -r .probe HELLO.toml` on a minimal
TOML key/value with a single string under `probe` (kislyuk/tomlq forwards
`-r` to jq for raw string output).
Identify fossils use `*.toml` (TOML peer leaf after YAML).
Prefer `tomlq` / `kislyuk-tomlq` / `tomlq3.4` / `toml` / `.toml`.
Bare `toml` is **allowed** as a route tag (language name; word-boundary).
Bare `tomlq` is **allowed** as a route tag (tool binary name).
Bare `kislyuk-tomlq` / `tomlq3.4` are **allowed** as route tags (family / version).
Bare `.toml` is **allowed** with extension-boundary matching (do not invent
`.tomlfoo` prefix hits). TOML document leaf after YAML;
treats TOML as peer fossil not house twin language. Do **not**
claim a full Taplo / BurntSushi toml crate / TOML 1.0 suite recovery from a Debian
kislyuk `tomlq` raw-string probe alone — this leaf pins kislyuk/tomlq TOML→JSON→jq
filter evaluation with raw string output.

## Commands (VERIFIED)

```text
$ which tomlq
/usr/bin/tomlq

$ tomlq --version
tomlq 3.4.3

$ tomlq -r .probe HELLO.toml
EMPEROR-TIME-TOMLQ-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| Host runs `tomlq -r .probe HELLO.toml` → probe string | VERIFIED |
| Filename culture (Cargo / pyproject / Hugo TOML) maps to this dialect | CONJECTURE (probe uses plain key = string) |
| Full Taplo / BurntSushi toml / TOML 1.0 feature recovery | UNVERIFIABLE from Debian kislyuk tomlq 3.4.3 CLI probe alone |
| bare `taplo` / `toml-cli` as verified TOML toolchain | REJECTED (not used this leaf; different CLI) |
