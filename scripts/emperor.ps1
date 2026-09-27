<#
.SYNOPSIS
  Host dispatcher. Picks .ps1 on Windows, .sh elsewhere, with fallback.
  Silent-boots when .emperor/host.env is missing (twin of scripts/emperor).
.EXAMPLE
  .\emperor.ps1 done .emperor/tasks/demo
  .\emperor.ps1 queue next
  .\emperor.ps1 forge .emperor/tasks/demo
  .\emperor.ps1 finish
  .\emperor.ps1 activate
  .\emperor.ps1 identify .
  .\emperor.ps1 route "lost pascal tree"
  .\emperor.ps1 excavate .
  .\emperor.ps1 heal
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [ValidateSet('done','gate','eval','review-pack','dowse','install','worktree','queue','forge','finish','activate','boot','identify','route','heal','excavate')]
    [string]$Tool,
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$ToolArgs
)
$ErrorActionPreference = 'Stop'
$here = $PSScriptRoot
$ps1 = Join-Path $here "$Tool.ps1"
$sh  = Join-Path $here "$Tool.sh"
$isWin = ($env:OS -eq 'Windows_NT')
try { if ($IsWindows) { $isWin = $true } } catch {}
$bootPs1 = Join-Path $here 'boot.ps1'

# Host + survey live on disk. Client is never asked to identify the box.
if (-not (Test-Path '.emperor/host.env')) {
    if (Test-Path $bootPs1) {
        & $bootPs1 2>$null | Out-Null
    }
}

if ($Tool -eq 'boot') {
    if (Test-Path $bootPs1) {
        & $bootPs1 @ToolArgs
        if ($env:EMPEROR_BOOT_VERBOSE -eq '1' -and (Test-Path '.emperor/host.env')) {
            Get-Content '.emperor/host.env'
        }
        exit 0
    }
}

# identify with no path → silent (boot already wrote survey). Not a user ritual.
if ($Tool -eq 'identify' -and (-not $ToolArgs -or $ToolArgs.Count -eq 0)) {
    if (Test-Path $bootPs1) { & $bootPs1 2>$null | Out-Null }
    if ($env:EMPEROR_BOOT_VERBOSE -eq '1' -and (Test-Path '.emperor/survey.md')) {
        Get-Content '.emperor/survey.md'
    }
    exit 0
}

if ($isWin -and (Test-Path $ps1)) {
    & $ps1 @ToolArgs
    exit $LASTEXITCODE
}
if (-not $isWin -and (Test-Path $sh)) {
    & bash $sh @ToolArgs
    exit $LASTEXITCODE
}
if (Test-Path $ps1) { & $ps1 @ToolArgs; exit $LASTEXITCODE }
if ((Get-Command bash -ErrorAction SilentlyContinue) -and (Test-Path $sh)) {
    & bash $sh @ToolArgs; exit $LASTEXITCODE
}
Write-Error "emperor: no runtime for $Tool on this host"
exit 127
