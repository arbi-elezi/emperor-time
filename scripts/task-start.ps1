<#
.SYNOPSIS
  Thin twin of task-start.sh — task-start via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/task_start.py'
& python3 $py @Rest
exit $LASTEXITCODE
