# Thin alias: same survey as identify. First-class excavate tool name.
param([string]$Root = '.')
$ErrorActionPreference = 'Stop'
& (Join-Path $PSScriptRoot 'identify.ps1') -Root $Root
exit $LASTEXITCODE
