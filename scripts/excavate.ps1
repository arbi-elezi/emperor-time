<#
.SYNOPSIS
  Thin alias of excavate.sh — same survey as identify via Python core.
  Calls identify.py directly (no twin hop).
.EXAMPLE
  .\excavate.ps1 .
  .\excavate.ps1 path/to/lost-tree
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
