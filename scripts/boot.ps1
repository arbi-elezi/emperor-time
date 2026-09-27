# Silent session defaults. User never types this.
# Twin of boot.sh — writes .emperor/host.env, survey.md, optional eval.log.
param()
$ErrorActionPreference = 'SilentlyContinue'
$here = $PSScriptRoot
# Dot-source host twin (parity with boot.sh → lib/host.sh).
. (Join-Path $here 'lib/host.ps1')
if (-not (Test-Path '.emperor')) { New-Item -ItemType Directory -Path '.emperor' | Out-Null }
Write-EmperorHostReport | Set-Content -Path '.emperor/host.env' -Encoding utf8
if (Test-Path (Join-Path $here 'identify.ps1')) {
  & (Join-Path $here 'identify.ps1') . | Out-File -FilePath '.emperor/survey.md' -Encoding utf8
}
if ((Test-Path (Join-Path $here 'eval.ps1')) -and (Test-Path 'SKILL.md')) {
  & (Join-Path $here 'eval.ps1') 2>&1 | Out-File -FilePath '.emperor/eval.log' -Encoding utf8
}
if ($env:EMPEROR_BOOT_VERBOSE -eq '1') { Get-Content '.emperor/host.env' }
exit 0
