# blind-secrets-broker fixtures

Prove `emperor secrets list|declare|inject` never echoes plaintext,
`env show|sync` merges SOT plugin overlays with redacted show, and
HARD-GATE `--reject-secret-leak` / `--check-env-redacted` refuse dumps
that would expose values. Eval builds ephemeral roots; no vault CLI required.
