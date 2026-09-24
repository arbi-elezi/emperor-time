<#
.SYNOPSIS
  Mechanical gates G0–G5. Twin of gate.sh.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory=$true,Position=0)][ValidateSet('g0','g1','g2','g3','g4','g5')][string]$Gate,
    [Parameter(Mandatory=$true,Position=1)][string]$TaskDir
)
$ErrorActionPreference = 'Stop'
function Fail($m) { Write-Error "GATE $Gate FAIL: $m"; exit 1 }
function Ok($m) { Write-Host "GATE $Gate PASS: $m" }
function Has($pat, $file) {
    if (-not (Test-Path $file)) { return $false }
    return [bool](Select-String -Path $file -Pattern $pat -Quiet -ErrorAction SilentlyContinue)
}
if (-not (Test-Path $TaskDir -PathType Container)) { Fail "missing task dir $TaskDir" }
$ledger = Join-Path $TaskDir 'ledger.md'
$order  = Join-Path $TaskDir 'work-order.md'
$claims = Join-Path $TaskDir 'claims.md'
$critique = Join-Path $TaskDir 'critique.md'
$stamp = Join-Path $TaskDir '.gates'
New-Item -ItemType Directory -Force -Path $stamp | Out-Null
function NeedLedger { if (-not (Test-Path $ledger)) { Fail "missing $ledger" } }
function RequirePrior($p) { if (-not (Test-Path (Join-Path $stamp $p))) { Fail "prior gate $p never passed mechanically" } }
function Mark { Set-Content -Path (Join-Path $stamp $Gate) -Value (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ') }

switch ($Gate) {
    'g0' {
        NeedLedger
        if (-not (Has 'G0' $ledger)) { Fail 'ledger has no G0 section' }
        if (-not (Has 'quoted|Origin|Task:' $ledger)) { Fail 'ledger missing origin/task line' }
        Mark; Ok $ledger
    }
    'g1' {
        RequirePrior 'g0'; NeedLedger
        if (-not (Has 'Acceptance criteria' $ledger)) { Fail 'no acceptance criteria' }
        if (-not (Has 'Out of scope' $ledger)) { Fail 'no out-of-scope' }
        Mark; Ok 'requirements present'
    }
    'g2' {
        RequirePrior 'g1'; NeedLedger
        $trivial = (Has 'Size:.*trivial' $ledger) -or ((Test-Path $order) -and (Has 'Size:.*trivial' $order))
        if ($trivial) {
            if (-not (Has 'G2' $ledger)) { Fail 'trivial task still needs a G2 line' }
            Mark; Ok 'trivial G2'; exit 0
        }
        if (-not (Test-Path $order)) { Fail 'non-trivial task missing work-order.md' }
        if (-not (Has 'Expected:' $order)) { Fail 'work-order has no Expected: lines' }
        if (-not (Has 'Acceptance criteria' $order)) { Fail 'work-order missing acceptance criteria' }
        Mark; Ok $order
    }
    'g3' {
        RequirePrior 'g2'; NeedLedger
        if (-not (Has 'G3' $ledger)) { Fail 'no G3 section' }
        if (Get-Command git -ErrorAction SilentlyContinue) {
            git diff --stat | Out-File (Join-Path $TaskDir 'diffstat.txt')
        }
        Mark; Ok 'build section present'
    }
    'g4' {
        RequirePrior 'g3'; NeedLedger
        if (-not ((Test-Path $critique) -or (Has 'Self-critique' $ledger))) { Fail 'no critique artifact' }
        if (Test-Path $claims) {
            $verified = Select-String -Path $claims -Pattern '\|.*\|\s*VERIFIED\s*\|' -ErrorAction SilentlyContinue
            foreach ($row in $verified) {
                if ($row.Line -notmatch '"|`') { Fail 'VERIFIED row without quoted evidence' }
            }
        }
        if (-not (Has 'Verdict' $ledger)) { Fail 'ledger missing Verdict line' }
        Mark; Ok 'verify artifacts present'
    }
    'g5' {
        RequirePrior 'g4'; NeedLedger
        if (-not (Has 'PASS' $ledger)) { Fail 'no PASS / PASS-WITH-CONDITIONS on ledger' }
        if (-not (Has 'Breach Register' $ledger)) { Fail 'breach register missing (must exist even if empty)' }
        Mark; Ok 'deliverable artifacts present'
    }
}
