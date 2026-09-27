<#
.SYNOPSIS
  Trigger→skill router MVP (no embeddings). Peer of route.sh.
  Thin twin: delegates to scripts/lib/route.py.
.EXAMPLE
  .\route.ps1 "lost pascal tree"
  "queue next" | .\route.ps1
#>
[CmdletBinding()]
param(
    [Parameter(Position = 0, ValueFromRemainingArguments = $true)]
    [string[]]$Utterance,
    [Parameter(ValueFromPipeline = $true)]
    [string]$PipelineInput
)
$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$Triggers = if ($env:EMPEROR_TRIGGERS) { $env:EMPEROR_TRIGGERS } else { Join-Path $Root 'evals/triggers.json' }
$Py = Join-Path $Root 'scripts/lib/route.py'

$text = if ($Utterance -and $Utterance.Count -gt 0) {
    ($Utterance -join ' ').Trim()
} elseif ($PipelineInput) {
    $PipelineInput.Trim()
} else {
    $stdin = @($input)
    if ($stdin) { ($stdin -join ' ').Trim() } else { '' }
}
if (-not $text) {
    Write-Error 'usage: route.ps1 <utterance>   or pipe stdin'
    exit 2
}
if (-not (Test-Path $Triggers)) {
    Write-Error "route: missing $Triggers"
    exit 2
}
if (-not (Test-Path $Py)) {
    Write-Error "route: missing $Py"
    exit 2
}

$env:EMPEROR_ROUTE_UTTERANCE = $text
$env:EMPEROR_ROUTE_TRIGGERS = $Triggers
$pyCmd = $null
foreach ($c in @('python3', 'py', 'python')) {
    if (Get-Command $c -ErrorAction SilentlyContinue) { $pyCmd = $c; break }
}
if (-not $pyCmd) {
    Write-Error 'route.ps1: python3/python required for JSON route matching'
    exit 127
}
& $pyCmd $Py
exit $LASTEXITCODE
