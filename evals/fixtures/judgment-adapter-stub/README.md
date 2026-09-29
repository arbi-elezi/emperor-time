# judgment-adapter-stub fixtures (PR3 / v0.4.171)

Optional judgment adapter — provider **off** by default; soft `None` when
unavailable; **never** required for core factory; **never** on tiny happy-path.

- `provider-off/` — `judgment.provider: off` → `judge(...) is None`
- `no-key-soft/` — provider `openai_compat` without `EMPEROR_JUDGMENT_API_KEY` → None
- `refuse-require/` — `--require` still soft-refuses when off/unavailable (None)
- `tiny-clear-skip/` — clear tiny ask → rigor_judge signals `skipped_tiny_clear`; no provider call

Env (when enabled): `EMPEROR_JUDGMENT_API_KEY`, `EMPEROR_JUDGMENT_BASE_URL`.
JEV: no concrete model slug shipped (`model: null`).
