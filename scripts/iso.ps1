<#
.SYNOPSIS
  Thin twin of iso.sh — worktree isolation checklist via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/worktree_iso.py'
& python3 $py @Rest
exit $LASTEXITCODE
