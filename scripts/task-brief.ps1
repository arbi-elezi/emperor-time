<#
.SYNOPSIS
  Thin twin of task-brief.sh — task-brief via Python core.
#>
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = Join-Path $root 'scripts/lib/task_brief.py'
& python3 $py @Rest
exit $LASTEXITCODE
