# Thin alias: same survey as identify. First-class excavate tool name.
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Continue'
$identify = Join-Path $PSScriptRoot 'identify.ps1'
if (-not $Rest -or $Rest.Count -eq 0) {
    & $identify
} else {
    & $identify @Rest
}
exit 0
