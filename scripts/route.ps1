<#
.SYNOPSIS
  Trigger→skill router MVP (no embeddings). Peer of route.sh.
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

$env:EMPEROR_ROUTE_UTTERANCE = $text
$env:EMPEROR_ROUTE_TRIGGERS = $Triggers
$py = @'
import json, os, re, sys
utterance = os.environ["EMPEROR_ROUTE_UTTERANCE"]
path = os.environ["EMPEROR_ROUTE_TRIGGERS"]
text = utterance.casefold()
with open(path, encoding="utf-8") as f:
    data = json.load(f)
routes = data.get("routes") or []

def matches(pattern: str) -> bool:
    p = pattern.casefold().strip()
    if not p:
        return False
    compact = re.sub(r"[^a-z0-9]+", "", p)
    if len(compact) <= 3 or p.startswith("."):
        if p.startswith("."):
            return p in text
        return re.search(r"(?<![a-z0-9])" + re.escape(p) + r"(?![a-z0-9])", text) is not None
    return p in text

for route in routes:
    pats = list(route.get("patterns") or [])
    tags = list(route.get("tags") or [])
    hit = None
    for p in pats:
        if matches(p):
            hit = p
            break
    if hit is None:
        for t in tags:
            if matches(t):
                hit = t
                break
    if hit is None:
        continue
    target = route.get("target") or ""
    reason = route.get("reason") or route.get("id") or "match"
    if not target:
        continue
    print(f"{target} — {reason}")
    sys.exit(0)
print("route: no match", file=sys.stderr)
sys.exit(1)
'@
# Prefer python3, then py, then python
$pyCmd = $null
foreach ($c in @('python3', 'py', 'python')) {
    if (Get-Command $c -ErrorAction SilentlyContinue) { $pyCmd = $c; break }
}
if (-not $pyCmd) {
    Write-Error 'route.ps1: python3/python required for JSON route matching'
    exit 127
}
$py | & $pyCmd -
exit $LASTEXITCODE
