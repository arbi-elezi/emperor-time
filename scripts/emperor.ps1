<#
.SYNOPSIS
  Host dispatcher. Picks .ps1 on Windows, .sh elsewhere, with fallback.
  Silent-boots when .emperor/host.env is missing (twin of scripts/emperor).
.EXAMPLE
  .\emperor.ps1 done .emperor/tasks/demo
  .\emperor.ps1 queue next
  .\emperor.ps1 forge .emperor/tasks/demo
  .\emperor.ps1 finish
  .\emperor.ps1 activate
  .\emperor.ps1 identify .
  .\emperor.ps1 route "lost pascal tree"
  .\emperor.ps1 excavate .
  .\emperor.ps1 heal
  .\emperor.ps1 grill
  .\emperor.ps1 tdd
  .\emperor.ps1 work-order
  .\emperor.ps1 claim-audit
  .\emperor.ps1 judgment-audit
  .\emperor.ps1 quarantine
  .\emperor.ps1 steal-quarantine
  .\emperor.ps1 critique
  .\emperor.ps1 self-critique
  .\emperor.ps1 verdict
  .\emperor.ps1 breach
  .\emperor.ps1 iso
  .\emperor.ps1 review
  .\emperor.ps1 author
  .\emperor.ps1 evidence
  .\emperor.ps1 receive
  .\emperor.ps1 execute
  .\emperor.ps1 subagent
  .\emperor.ps1 parallel
  .\emperor.ps1 session-discovery
  .\emperor.ps1 diagnose
  .\emperor.ps1 trace
  .\emperor.ps1 defense
  .\emperor.ps1 wait
  .\emperor.ps1 polluter
  .\emperor.ps1 pressure
  .\emperor.ps1 good-tests
  .\emperor.ps1 skill-test
  .\emperor.ps1 persuasion
  .\emperor.ps1 sdo
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [ValidateSet('done','gate','eval','review-pack','dowse','install','worktree','queue','forge','finish','activate','boot','identify','route','heal','grill','tdd','iso','review','author','evidence','receive','execute','subagent','parallel','excavate','session-discovery','diagnose','trace','defense','wait','polluter','pressure','good-tests','skill-test','persuasion','sdo','task-brief','task-start','task-done','sdd-workspace','sdd-review-pack','work-order','claim-audit','judgment-audit','quarantine','steal-quarantine','consent','steal-consent','critique','self-critique','verdict','breach','brief','context','thoughttrail','super-context','sandbox','sot','runtime','env','secrets','steal-flow','sign-in-handoff','steal-dispatch','swarm-emulate','pin-and-consent','jail-pin','ask-spec','harness-plan','tool-force','proportionality','anti-loop','config')]
    [string]$Tool,
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$ToolArgs
)
$ErrorActionPreference = 'Stop'
$here = $PSScriptRoot
# wait: first-class alias → condition-wait HARD-GATE card
if ($Tool -eq 'wait') { $Tool = 'condition-wait' }
# polluter: first-class alias → find-polluter HARD-GATE card
if ($Tool -eq 'polluter') { $Tool = 'find-polluter' }
if ($Tool -eq 'brief') { $Tool = 'task-brief' }
if ($Tool -eq 'judgment-audit') { $Tool = 'claim-audit' }
if ($Tool -eq 'steal-quarantine') { $Tool = 'quarantine' }
if ($Tool -eq 'steal-consent') { $Tool = 'consent' }
if ($Tool -eq 'heal-and-verify') { $Tool = 'heal-verify' }
if ($Tool -eq 'reproduce-and-bisect') { $Tool = 'reproduce' }
if ($Tool -eq 'holy-triage') { $Tool = 'triage' }
if ($Tool -eq 'process-healing') { $Tool = 'process-heal' }
if ($Tool -eq 'sign-in-handoff') { $Tool = 'steal-flow' }
if ($Tool -eq 'steal-dispatch') { $Tool = 'steal-flow' }
if ($Tool -eq 'swarm-emulate') { $Tool = 'steal-flow' }
if ($Tool -eq 'jail-pin') { $Tool = 'pin-and-consent' }
if ($Tool -eq 'tool-force') { $Tool = 'harness-plan' }
if ($Tool -eq 'anti-loop') { $Tool = 'proportionality' }
if ($Tool -eq 'self-critique') { $Tool = 'critique' }
if ($Tool -eq 'breach') { $Tool = 'verdict' }
$ps1 = Join-Path $here "$Tool.ps1"
$sh  = Join-Path $here "$Tool.sh"
$isWin = ($env:OS -eq 'Windows_NT')
try { if ($IsWindows) { $isWin = $true } } catch {}
$bootPs1 = Join-Path $here 'boot.ps1'

# Host + survey live on disk. Client is never asked to identify the box.
if (-not (Test-Path '.emperor/host.env')) {
    if (Test-Path $bootPs1) {
        & $bootPs1 2>$null | Out-Null
    }
}

if ($Tool -eq 'boot') {
    if (Test-Path $bootPs1) {
        & $bootPs1 @ToolArgs
        if ($env:EMPEROR_BOOT_VERBOSE -eq '1' -and (Test-Path '.emperor/host.env')) {
            Get-Content '.emperor/host.env'
        }
        exit 0
    }
}

# identify with no path → silent (boot already wrote survey). Not a user ritual.
if ($Tool -eq 'identify' -and (-not $ToolArgs -or $ToolArgs.Count -eq 0)) {
    if (Test-Path $bootPs1) { & $bootPs1 2>$null | Out-Null }
    if ($env:EMPEROR_BOOT_VERBOSE -eq '1' -and (Test-Path '.emperor/survey.md')) {
        Get-Content '.emperor/survey.md'
    }
    exit 0
}

if ($isWin -and (Test-Path $ps1)) {
    & $ps1 @ToolArgs
    exit $LASTEXITCODE
}
if (-not $isWin -and (Test-Path $sh)) {
    & bash $sh @ToolArgs
    exit $LASTEXITCODE
}
if (Test-Path $ps1) { & $ps1 @ToolArgs; exit $LASTEXITCODE }
if ((Get-Command bash -ErrorAction SilentlyContinue) -and (Test-Path $sh)) {
    & bash $sh @ToolArgs; exit $LASTEXITCODE
}
Write-Error "emperor: no runtime for $Tool on this host"
exit 127
