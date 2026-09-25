[CmdletBinding()]
param([Parameter(Mandatory = $true, Position = 0)][string]$TaskDir)
$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
if (-not (Test-Path $TaskDir -PathType Container)) { Write-Error 'usage: forge.ps1 <task-dir>'; exit 2 }
$consent = $env:EMPEROR_CONSENT_PR
$ledger = Join-Path $TaskDir 'ledger.md'
if (Test-Path $ledger) {
    if (Select-String -Path $ledger -Pattern 'consent.*pr|open a pr|yes.*pr' -Quiet) { $consent = '1' }
}
if ($consent -ne '1') {
    Write-Error 'FORGE REFUSED: no EMPEROR_CONSENT_PR=1 and no quoted PR consent in ledger.md'
    exit 3
}
& (Join-Path $PSScriptRoot 'done.ps1') $TaskDir
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$title = 'emperor-time change'
$body = Join-Path $TaskDir 'PR.md'
@(
    '## G1'
    if (Test-Path $ledger) { Get-Content $ledger }
    ''
    '## DONE probes'
    if (Test-Path (Join-Path $TaskDir 'DONE.md')) { Get-Content (Join-Path $TaskDir 'DONE.md') }
) | Set-Content $body
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Host "FORGE DRY: gh not installed. Client runs: gh pr create --title '$title' --body-file $body"
    exit 0
}
gh pr create --title $title --body-file $body
