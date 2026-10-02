# Thin twin of boot.sh — silent session boot via Python core.
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'SilentlyContinue'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
if (-not $env:EMPEROR_SHELL) {
    if ($PSVersionTable.PSEdition -eq 'Core') { $env:EMPEROR_SHELL = 'pwsh' }
    else { $env:EMPEROR_SHELL = 'powershell' }
}
$py = Join-Path $root 'scripts/lib/boot.py'
. (Join-Path $PSScriptRoot 'lib/resolve-emperor-python.ps1')
Invoke-EmperorPython $py @Rest
exit $LASTEXITCODE
