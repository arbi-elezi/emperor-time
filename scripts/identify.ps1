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
if ($argsList.Count -eq 0) {
    & python3 $py
} else {
    & python3 $py @argsList
}
exit 0
