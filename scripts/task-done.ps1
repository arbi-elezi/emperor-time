<#
.SYNOPSIS
  Thin twin of task-done.sh — task-done via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/task_done.py'
& python3 $py @Rest
exit $LASTEXITCODE
