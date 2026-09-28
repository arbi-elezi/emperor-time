# hetero-critique-isolation fixtures

Prove review-pack isolation HARD-GATE (`review_pack.py --reject-unisolated` /
`--reject-author-diary` / `--check-isolation`).

| Fixture | Expect |
|---|---|
| `pack-ok/` | PASS — allowed files only |
| `pack-author-diary/` | FAIL — self-critique.md in pack |
| `pack-unisolated/` | FAIL — out.txt / notes.md in pack |
| `pack-diary-content/` | FAIL — author-diary markers in criteria.md |
| `task-ok/` | PASS — clean review-pack/ |
| `task-author-diary/` | FAIL — diary file in pack |
| `task-unisolated/` | FAIL — forbidden files in pack |
| `task-missing-pack/` | FAIL — hetero claimed, pack absent |
| `task-vacuous/` | PASS vacuous — no pack / no hetero signal |
