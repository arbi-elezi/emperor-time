@echo off
REM Peer of emperor.ps1 — same tools, user chooses cmd vs PowerShell.
REM UTF-8 code page. Does not implement gates; forwards to the .ps1 twins.
setlocal EnableExtensions
chcp 65001 >nul
set "HERE=%~dp0"
set "EMPEROR_ENCODING=UTF-8"
if "%~1"=="" (
  echo usage: emperor.cmd ^<done^|gate^|eval^|review-pack^|dowse^|install^|worktree^|host^> [args]
  exit /b 2
)
if /I "%~1"=="host" (
  echo os=windows shell=cmd wsl=0 encoding=UTF-8
  exit /b 0
)
where pwsh >nul 2>&1 && (
  pwsh -NoProfile -ExecutionPolicy Bypass -File "%HERE%emperor.ps1" %*
  exit /b %ERRORLEVEL%
)
where powershell >nul 2>&1 && (
  powershell -NoProfile -ExecutionPolicy Bypass -File "%HERE%emperor.ps1" %*
  exit /b %ERRORLEVEL%
)
echo emperor.cmd: no PowerShell on PATH — install pwsh or Windows PowerShell
exit /b 127
