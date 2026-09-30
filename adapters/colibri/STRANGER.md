# Stranger recipe: Colibrì + Emperor Time (≤1 page)

**Claim:** Colibrì as inference host, integrate-if-you-want.
**Who this is:** Emperor Time runs in your editor (client side); Colibrì is only
the local model server that editor talks to. Wiring the two together is your
call, not a requirement.
Harness ownership and native equal-UX are out of scope.
Target: JustVugg/colibri only (AMS name collision is out of scope / stale).

## Steps

1. **Install / check.** Build or install `coli`. Run `coli doctor` and
   `coli plan`. Have a converted model directory the engine supports.
2. **Serve (localhost):**

   ```bash
   COLI_MODEL=/path/to/model ./coli serve \
     --host 127.0.0.1 --port 8000 --model-id local-colibri
   ```

   Client base URL: `http://127.0.0.1:8000/v1`. Dummy key only if the client
   insists. Set `COLI_API_KEY` before any non-local bind.
3. **Point the harness** (OpenCode, Cursor, or generic OpenAI-compat client) at
   that base URL and model id. Load ET on the **client** side
   (`AGENTS.md` / OpenCode skill / generic core). Do not expect Colibrì to load
   ET itself. See `README.md` and `config.snippet.yaml`.
4. **Boot and activate** in the project (both commands must go green):

   ```bash
   bash scripts/boot.sh
   python3 scripts/lib/activate.py --cwd . -u "<tiny ask>"
   ```

5. **Tiny ask**, smallest change, then `python3 scripts/lib/done.py
   .emperor/tasks/<id>`.

## Fail closed

| If this happens | Label |
|---|---|
| `coli` missing or model/disk/RAM insufficient | **Colibrì engine live = BLOCKED** (+ reason) |
| ET boot / activate / done green without `coli` | **structure PASS** only |
| llama.cpp / toy HTTP works | **compat-shape** only (not Colibrì engine) |
| Iron gate refuses forge / secrets without consent | **PASS** (iron working) |

Full pack: `README.md`. Smoke rules: `QA-SMOKE.md`.
