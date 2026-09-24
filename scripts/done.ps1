<#
.SYNOPSIS
  Agent-defined DONE. Exit 0 only if every probe:/expect: pair matches.
#>
[CmdletBinding()]
param([Parameter(Mandatory=$true,Position=0)][string]$TaskDir)
$ErrorActionPreference = 'Continue'
if (-not (Test-Path $TaskDir -PathType Container)) { Write-Error "usage: done.ps1 <task-dir>"; exit 2 }
$done = Join-Path $TaskDir 'DONE.md'
if (-not (Test-Path $done)) { Write-Error "DONE FAIL: no $done (agent must define DONE)"; exit 1 }
$text = Get-Content -Raw $done
if ($text -notmatch '(?m)^probe:') { Write-Error "DONE FAIL: no probes in DONE.md"; exit 1 }

function Invoke-Probe([string]$Cmd) {
    if (Get-Command bash -ErrorAction SilentlyContinue) {
        return (& bash -lc $Cmd 2>&1 | Out-String)
    }
    return (Invoke-Expression $Cmd 2>&1 | Out-String)
}

$fail = 0; $cmd = $null; $expect = ''
function Flush {
    param()
    if ([string]::IsNullOrWhiteSpace($script:cmd)) { return }
    $out = Invoke-Probe $script:cmd
    if ($script:expect -and ($out -notlike "*$($script:expect)*")) {
        Write-Host "DONE FAIL: $($script:cmd)"
        Write-Host "  expected substring: $($script:expect)"
        Write-Host "  got tail: $(($out -split "`n" | Select-Object -Last 8) -join "`n")"
        $script:fail = 1
    } else {
        Write-Host "DONE PASS: $($script:cmd)"
    }
}
Get-Content $done | ForEach-Object {
    if ($_ -match '^probe:\s*(.*)$') { Flush; $script:cmd = $Matches[1]; $script:expect = '' }
    elseif ($_ -match '^expect:\s*(.*)$') { $script:expect = $Matches[1] }
}
Flush
if ($fail -ne 0) { exit 1 }
Write-Host 'DONE OK'
exit 0
