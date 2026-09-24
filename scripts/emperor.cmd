@echo off
REM Windows cmd shim → PowerShell dispatcher
setlocal
set HERE=%~dp0
where pwsh >nul 2>&1 && (
  pwsh -NoProfile -File "%HERE%emperor.ps1" %*
  exit /b %ERRORLEVEL%
)
where powershell >nul 2>&1 && (
  powershell -NoProfile -File "%HERE%emperor.ps1" %*
  exit /b %ERRORLEVEL%
)
echo emperor.cmd: no PowerShell on PATH
exit /b 127
