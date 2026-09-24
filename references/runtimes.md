# Runtimes (user choice, same law)

Four fronts. They dispatch the same tools. None is the one true shell.

| Front | Who runs it |
|---|---|
| `scripts/emperor` | bash (Linux, macOS bash, Git Bash) |
| `scripts/emperor.zsh` | zsh (macOS default, oh-my-zsh) |
| `scripts/emperor.ps1` | PowerShell 7 / Windows PowerShell 5.1 |
| `scripts/emperor.cmd` | cmd.exe — peer of `.ps1`, UTF-8 `chcp 65001` |

Interactive helpers: `emperor-time.bash` and `emperor-time.plugin.zsh` are
convenience functions. They must call the dispatcher, not assume zsh syntax
in the `.sh` tools. Mechanical scripts stay bash or PowerShell; they are not
zsh scripts.

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
