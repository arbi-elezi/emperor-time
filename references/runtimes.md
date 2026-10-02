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
- Thin twins call Python cores; many `.ps1` files still hardcode `python3`
  (S12 resolver). Asset regen via `assets/render-pixel-art.ps1` needs
  System.Drawing (PS 5.1+).
- WSL force today: `EMPEROR_FORCE_WIN` (below). **Core-prefer-`.ps1` /
  `EMPEROR_FORCE_PS1` behavior docs are Bet T / S13** — not claimed shipped here.

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
