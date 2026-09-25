<#
.SYNOPSIS
  Host dispatcher. Picks .ps1 on Windows, .sh elsewhere, with fallback.
.EXAMPLE
  .\emperor.ps1 done .emperor/tasks/demo
  .\emperor.ps1 queue next
  .\emperor.ps1 forge .emperor/tasks/demo
  .\emperor.ps1 identify .
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [ValidateSet('done','gate','eval','review-pack','dowse','install','worktree','queue','forge','identify')]
    [string]$Tool,
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$ToolArgs
)
$ErrorActionPreference = 'Stop'
$here = $PSScriptRoot
$ps1 = Join-Path $here "$Tool.ps1"
$sh  = Join-Path $here "$Tool.sh"
$isWin = ($env:OS -eq 'Windows_NT') -or $IsWindows

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
