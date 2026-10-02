<#
.SYNOPSIS
  Thin twin of identify.sh — language-agnostic artifact survey via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [string]$Root = '',
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Continue'
$repo = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $repo 'scripts/lib/identify.py'
$argsList = @()
if ($Root) { $argsList += $Root }
if ($Rest) { $argsList += $Rest }
. (Join-Path $PSScriptRoot 'lib/resolve-emperor-python.ps1')
if ($argsList.Count -eq 0) {
    Invoke-EmperorPython $py
} else {
    Invoke-EmperorPython $py @argsList
}
exit 0
