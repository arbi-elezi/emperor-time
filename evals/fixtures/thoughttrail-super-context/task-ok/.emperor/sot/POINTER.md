# SOT — source of truth (fetch-only mirrors)

Emperor Time inverted workspace (virtual context = host-max):
- Workspace ≠ one repo. A task may bind multiple repos that
  work together; each bound repo is a *plugin* under
  `.emperor/sot/plugins/<repo>/` (fetch-only).
- Primary SOT = copy of `origin/main` kept current for
  context + regression reference. Do **not** mutate SOT.
- Regression runs from *copies* under `.emperor/artifacts/`,
  never by checking out over the SOT.
- Live checkout of main is not the only workspace; ET owns
  the workspace model.

CLI: `emperor sot sync|add-plugin` (v1 stub).

```yaml
remote: origin
ref: main
mirror_path:  # e.g. .emperor/sot/main-mirror (optional)
fetch_only: true
plugins: []  # filled by sot add-plugin
```
