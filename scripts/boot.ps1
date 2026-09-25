param()
$ErrorActionPreference = 'SilentlyContinue'
$here = $PSScriptRoot
if (-not (Test-Path '.emperor')) { New-Item -ItemType Directory -Path '.emperor' | Out-Null }
$os = if ($env:OS -eq 'Windows_NT') { 'windows' } else { 'posix' }
$shell = 'powershell'
Set-Content -Path '.emperor/host.env' -Value "os=$os shell=$shell wsl=0 encoding=UTF-8"
if (Test-Path (Join-Path $here 'identify.ps1')) {
  & (Join-Path $here 'identify.ps1') . | Out-File -FilePath '.emperor/survey.md' -Encoding utf8
}
if ((Test-Path (Join-Path $here 'eval.ps1')) -and (Test-Path 'SKILL.md')) {
  & (Join-Path $here 'eval.ps1') 2>&1 | Out-File -FilePath '.emperor/eval.log' -Encoding utf8
}
if ($env:EMPEROR_BOOT_VERBOSE -eq '1') { Get-Content '.emperor/host.env' }
exit 0
