param([string]$Root = '.')
$ErrorActionPreference = 'Continue'
Write-Output "== identify $Root =="
Write-Output '-- extensions --'
Get-ChildItem -Path $Root -Recurse -File -ErrorAction SilentlyContinue |
  Where-Object { $_.FullName -notmatch '\\.git\\|\\.emperor\\|node_modules' } |
  ForEach-Object { if ($_.Extension) { $_.Extension.TrimStart('.').ToLowerInvariant() } } |
  Group-Object | Sort-Object Count -Descending | Select-Object -First 40 |
  ForEach-Object { Write-Output ('{0,6} {1}' -f $_.Count, $_.Name) }
Write-Output '-- named fossils --'
$pats = @('.pas','.pp','.dpr','.lpr','.asm','.s','.inc','.cbl','.cob','.for','.f','.f90','.vhd','.vhdl','.rel','.hex','.bin','.rom','.mak')
Get-ChildItem -Path $Root -Recurse -File -ErrorAction SilentlyContinue |
  Where-Object {
    $ext = $_.Extension.ToLowerInvariant()
    ($pats -contains $ext) -or ($_.Name -match '^(Makefile|makefile)$')
  } |
  Group-Object { $_.Extension.ToLowerInvariant() } |
  ForEach-Object { Write-Output ('{0} *{1}' -f $_.Count, $_.Name) }
Write-Output 'identify: done (read-only)'
exit 0
