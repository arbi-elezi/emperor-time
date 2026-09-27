#!/usr/bin/env python3
"""Host detect + host.env report line (Python core).

Closes bash↔ps1 twin drift on the silent-boot report: host.sh defaulted
encoding to C.UTF-8 and probed cmd/powershell/pwsh for WSL interop;
host.ps1 defaulted encoding to UTF-8 and only probed cmd.exe. One core
owns os/shell/wsl/win_interop/encoding/mnt/win_root and the report line.

Shell twins (host.sh / host.ps1) still provide sourceable EMPEROR_* vars
and path helpers for the emperor dispatcher; emperor_host_report /
Write-EmperorHostReport delegate here.

Thin consumers: boot.py (silent boot), host.sh/ps1 report helpers.
CLI: host.py [--report] [--as-json]
"""
from __future__ import annotations

import argparse
import json
import os
import platform
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class HostInfo:
    os: str
    shell: str
    wsl: int
    win_interop: int
    encoding: str
    mnt: str
    win_root: str

    def report_line(self) -> str:
        return (
            f"os={self.os} shell={self.shell} wsl={self.wsl} "
            f"win_interop={self.win_interop} encoding={self.encoding} "
            f"mnt={self.mnt} win_root={self.win_root}"
        )


def _which(name: str) -> bool:
    from shutil import which

    return which(name) is not None


def _detect_encoding() -> str:
    explicit = os.environ.get("EMPEROR_ENCODING", "").strip()
    if explicit:
        return explicit
    for key in ("LC_ALL", "LANG"):
        val = os.environ.get(key, "").strip()
        if val:
            if val in ("C", "POSIX"):
                return "C.UTF-8"
            return val
    # Windows hosts rarely set LANG; Unix silent-boot historically used C.UTF-8.
    if os.name == "nt" or platform.system().lower() == "windows":
        return "UTF-8"
    return "C.UTF-8"


def _detect_shell() -> str:
    explicit = os.environ.get("EMPEROR_SHELL", "").strip()
    if explicit:
        return explicit
    # Parent process name (Linux /proc; best-effort elsewhere).
    try:
        ppid = os.getppid()
        comm_path = Path(f"/proc/{ppid}/comm")
        if comm_path.is_file():
            comm = comm_path.read_text(encoding="utf-8", errors="replace").strip().lower()
            if comm in ("bash", "zsh", "sh", "dash", "pwsh", "powershell", "powershell.exe", "pwsh.exe"):
                return comm.replace(".exe", "")
            if "powershell" in comm:
                return "powershell"
            if comm == "pwsh":
                return "pwsh"
    except OSError:
        pass
    shell_env = os.environ.get("SHELL", "")
    base = Path(shell_env).name.lower() if shell_env else ""
    if base in ("bash", "zsh", "sh", "dash", "fish"):
        return base
    if os.name == "nt" or platform.system().lower() == "windows":
        # PSEdition is not visible here; prefer pwsh when on PATH.
        if _which("pwsh") or _which("pwsh.exe"):
            return "pwsh"
        return "powershell"
    return "sh"


def _linux_wsl() -> bool:
    if os.environ.get("WSL_DISTRO_NAME") or os.environ.get("WSL_INTEROP"):
        return True
    try:
        ver = Path("/proc/version").read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    low = ver.lower()
    return "microsoft" in low or "wsl" in low


def detect() -> HostInfo:
    system = platform.system()
    uname = system.lower() if system else "unknown"

    os_name = "unknown"
    wsl = 0
    win_interop = 0
    mnt = ""
    win_root = ""

    if os.environ.get("OS") == "Windows_NT" or uname == "windows":
        os_name = "windows"
    elif uname == "darwin":
        os_name = "macos"
    elif uname == "linux":
        if _linux_wsl():
            os_name = "wsl"
            wsl = 1
        else:
            os_name = "linux"
    elif uname.startswith("mingw") or uname.startswith("msys"):
        os_name = "gitbash"
    elif uname.startswith("cygwin"):
        os_name = "cygwin"
    else:
        os_name = uname or "unknown"

    # WSL can also appear when OS=Windows_NT is unset but interop env is set.
    if wsl == 0 and (os.environ.get("WSL_DISTRO_NAME") or os.environ.get("WSL_INTEROP")):
        os_name = "wsl"
        wsl = 1

    if wsl == 1:
        if Path("/mnt/c").is_dir():
            mnt = "/mnt"
            win_root = "/mnt/c"
        elif Path("/mnt/wslg").is_dir():
            mnt = "/mnt"
        # Match host.sh: any of cmd / powershell / pwsh counts as interop.
        if (
            _which("cmd.exe")
            or _which("powershell.exe")
            or _which("pwsh.exe")
            or _which("pwsh")
        ):
            win_interop = 1

    return HostInfo(
        os=os_name,
        shell=_detect_shell(),
        wsl=wsl,
        win_interop=win_interop,
        encoding=_detect_encoding(),
        mnt=mnt,
        win_root=win_root,
    )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Emperor Time host detect (report line for .emperor/host.env)."
    )
    ap.add_argument(
        "--report",
        action="store_true",
        help="print host.env report line (default when no flag)",
    )
    ap.add_argument(
        "--as-json",
        action="store_true",
        help="print HostInfo as JSON object",
    )
    args = ap.parse_args(argv)
    info = detect()
    if args.as_json:
        print(json.dumps(asdict(info), sort_keys=True))
        return 0
    # default = report line (also when --report)
    print(info.report_line())
    return 0


if __name__ == "__main__":
    sys.exit(main())
