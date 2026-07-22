# Adapter — Generic (any open-weight model or unknown harness)

`EMPEROR_TIME.core.md` is the whole doctrine distilled to a single system
prompt (~2.5k tokens), with a ~300-token **Vow card** at the top as the
minimal form for small worker models.

## Use it with…

- **LM Studio / Jan / any chat UI:** paste the file (or just the Vow card) as
  the system prompt.
- **llama.cpp:** `llama-cli -m model.gguf --system-prompt-file EMPEROR_TIME.core.md -p "<task>"`
  (flag names vary by build — `--help` first, per the tripwire rule).
- **vLLM / OpenAI-compatible servers:** send it as the `system` message.
- **Ollama:** bake it in — see `adapters/ollama/`.
- **Any agent CLI you're enlisting as a worker:** prepend the Vow card to the
  worker prompt so even skill-less workers operate under the vows.

## Sizing guidance

| Model class | Load |
|---|---|
| Frontier / large (orchestrator-capable) | Full skill tree if the harness supports skills; else full core |
| ~14B–70B open-weight | Full core as system prompt; worker or critic roles |
| < 14B | Vow card only; tightly-scoped worker prompts; orchestrator judges everything |

Distillation order and the compatibility trial (what to disable when a harness
can't read files / execute / reach the web): `references/portability.md`.
The last thing standing is always the claim discipline — an agent with nothing
but "label what you didn't verify" is still safer than a bare model.
