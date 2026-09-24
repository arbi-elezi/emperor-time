$Root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$fail = 0
function Need([string]$f) {
  if (-not (Test-Path (Join-Path $Root $f))) {
    Write-Host "EVAL FAIL: missing $f"
    $script:fail = 1
  }
}
Write-Host '== presence =='
@(
  'SKILL.md',
  'chains/dowsing-chain/SKILL.md','chains/chain-jail/SKILL.md',
  'chains/judgment-chain/SKILL.md','chains/steal-chain/SKILL.md','chains/holy-chain/SKILL.md',
  'scripts/emperor','scripts/emperor.ps1','scripts/emperor.cmd'
) | ForEach-Object { Need $_ }

Write-Host '== twins (every mechanical script) =='
@('done','gate','eval','review-pack','dowse','install','worktree') | ForEach-Object {
  Need "scripts/$_.sh"
  Need "scripts/$_.ps1"
}

Write-Host '== vows + five chains =='
$skill = Get-Content (Join-Path $Root 'SKILL.md') -Raw
if ($skill -notmatch 'Vow of Evidence') { Write-Host 'EVAL FAIL: vows missing'; $fail = 1 }
@('Dowsing Chain','Chain Jail','Judgment Chain','Steal Chain','Holy Chain') | ForEach-Object {
  if ($skill -notmatch [regex]::Escape($_)) { Write-Host "EVAL FAIL: $_ unnamed in SKILL.md"; $fail = 1 }
}

if ($fail -ne 0) { Write-Host 'EVALS FAILED'; exit 1 }
Write-Host 'EVALS PASSED'
