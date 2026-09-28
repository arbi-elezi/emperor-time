# Blind credentials

Unified way to obtain/inject secrets into workspace/stacks
WITHOUT the LLM seeing values (vault / 1Password / env-file
broker). Agent only sees names + status, never plaintext.

CLI: `emperor secrets list|inject` — inject must not print values.
