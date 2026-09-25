param([string]$Root = '.')
Write-Output "== identify $Root =="
Get-ChildItem -Path $Root -Recurse -File -ErrorAction SilentlyContinue |
  Where-Object { $_.FullName -notmatch '\\.git\\|\\.emperor\\' } |
  ForEach-Object { if ($_.Extension) { $_.Extension.ToLower() } } |
  Group-Object | Sort-Object Count -Descending | Select-Object -First 40 |
  ForEach-Object { Write-Output ("{0} {1}" -f $_.Count, $_.Name) }
