# Runtimes (user choice, same law)

Four fronts. They dispatch the same tools. None is the one true shell.

| Front | Who runs it |
|---|---|
| `scripts/emperor` | bash (Linux, macOS bash, Git Bash) |
| `scripts/emperor.zsh` | zsh (macOS default, oh-my-zsh) |
| `scripts/emperor.ps1` | PowerShell 7 / `pwsh` (**preferred**); Windows PowerShell 5.1 (**structure / HOLD** equal-smooth) |
| `scripts/emperor.cmd` | cmd.exe — peer of `.ps1`, UTF-8 `chcp 65001` |

Interactive helpers: `emperor-time.bash` and `emperor-time.plugin.zsh` are
convenience functions. They must call the dispatcher, not assume zsh syntax
in the `.sh` tools. Mechanical scripts stay bash or PowerShell; they are not
zsh scripts.

## Platforms honesty (claim bar — S11)

- Same law on four fronts; **preferred stranger path** is PowerShell Core /
  `pwsh` exercising the `.ps1` twins (Windows, macOS, Linux).
- Windows PowerShell **5.1** remains a structure path — **HOLD** equal-smooth
  until a dated native-Windows receipt. Do not read “four fronts” as equal-UX.
- Thin `.ps1` twins resolve Python via `Resolve-EmperorPython`
  (`scripts/lib/resolve-emperor-python.ps1`): `EMPEROR_PYTHON` → `python3` →
  `py -3` → `python`. Asset regen via `assets/render-pixel-art.ps1` needs
  System.Drawing (PS 5.1+).
- WSL force today: `EMPEROR_FORCE_WIN` (below). **Core-prefer-`.ps1` /
  `EMPEROR_FORCE_PS1`:** live under Bet T / S13 — see ## pwsh Core on Linux / macOS.

## Encoding

- Unix: honor `LANG`/`LC_ALL` if set; else `C.UTF-8`.
- cmd: `chcp 65001`.
- PowerShell: UTF-8 console encoding in `lib/host.ps1`.

## WSL

Detect: `WSL_DISTRO_NAME` / `WSL_INTEROP` / `/proc/version` contains Microsoft.

- Linux tools stay Linux (`.sh` via bash).
- Windows tools via interop: `powershell.exe` / `pwsh.exe` / `cmd.exe`.
- Paths: `wslpath -w` / `wslpath -u`. Drives under `/mnt/<letter>` when present.
- Force a Windows twin from WSL: `EMPEROR_FORCE_WIN=1 scripts/emperor done ...`
- From Windows into the distro: `wsl.exe -e bash scripts/emperor ...`

`scripts/emperor host` / `emperor.ps1 host` / `emperor.cmd host` prints the
detected os/shell/wsl/interop/encoding line.

## pwsh Core on Linux / macOS

`scripts/emperor.ps1` under PowerShell **Core** (`pwsh`) prefers `$Tool.ps1`
even when the OS is not Windows. Same prefer when `EMPEROR_FORCE_PS1=1`
(explicit proof / override).

Fallback order inside `emperor.ps1`:
1. Prefer `.ps1` when Windows, or `$PSEdition -eq 'Core'`, or `EMPEROR_FORCE_PS1=1`
2. Else bash `$Tool.sh` if bash + twin exist
3. Else `.ps1` if present
4. Else error 127

Symmetric to WSL `EMPEROR_FORCE_WIN=1`. Bash front `scripts/emperor` unchanged.
Windows PowerShell 5.1 (`Desktop`) still takes `.ps1` via host detect.

ValidateSet on `emperor.ps1` matches bash / `emperor.cmd` tool count (84),
including heal-verify / reproduce / triage / process-heal (+ aliases).

Structure / twin-exercise bridge only — not equal-UX. Native Windows smoothness
stays HOLD until a dated receipt (Platforms honesty / Bet S).
