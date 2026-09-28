# Managed env overlays (no secrets in git)

Per-artifact / per-plugin overlays merged by `emperor env sync`.
Values that are secrets MUST come from the secrets broker, not here.
