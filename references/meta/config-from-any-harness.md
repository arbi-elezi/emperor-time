# Config from any harness

Host-agnostic adjustable rigor (schema v1).

## Paths

1. Built-in defaults (`default_effort_class=tiny`, `auto_detect_little=true`)
2. Project `.emperor/config.yaml`
3. User overlay `~/.config/emperor-time/config.yaml` (or `$EMPEROR_CONFIG` / `$XDG_CONFIG_HOME/emperor-time/config.yaml`) — **user wins**

## CLI (any host with `scripts/emperor`)

```
emperor config show
emperor config get rigor.default_effort_class
emperor config set features.archaeology_depth shallow
emperor config set wip.max 1
emperor config set critique.require_eight_count_at medium
emperor config edit   # $EDITOR or prints path if no TTY
```


## Smoke without stalling SessionStart / boot

`./scripts/emperor` (and `emperor config …` via that front) may **stall or boot** when `.emperor/host.env` is missing — the bash front runs `boot.sh` on first use. For config-only smoke / CI / eval fixtures prefer:

```
python3 scripts/lib/config.py show|get|set|edit
# or
bash scripts/config.sh get rigor.default_effort_class
```

Those hit the Python core directly and do not require a host survey. Create `.emperor/host.env` via `scripts/emperor boot` when you need the full front.

## Knobs (PR2)

| Key | Values | Notes |
|---|---|---|
| `rigor.default_effort_class` | tiny\|small\|medium\|large (+ aliases) | missing file → tiny |
| `rigor.auto_detect_little` | true\|false | false → stamp config default on emit |
| `features.archaeology_depth` | off\|shallow\|full | engage depth; not museum growth |
| `features.sandbox` | bool | cheap read for sandbox paths |
| `features.sot` | bool | cheap read for SOT paths |
| `wip.max` | int ≥ 1 | queue WIP ceiling (default 1) |
| `critique.scale_with_effort` | bool | tiny may SKIP museum |
| `critique.require_eight_count_at` | effort_class | floor for eight-count |

Iron gates stay hard. Freeze `*-hint-bind`. No k8s/Nen invention via config.
