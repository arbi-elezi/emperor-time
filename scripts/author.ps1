<#
.SYNOPSIS
  Thin twin of author.sh — authoring iron-law / skill RGR checklist via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/author.py'
& python3 $py @Rest
exit $LASTEXITCODE
