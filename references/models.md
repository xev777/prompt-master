# Model Registry (dated snapshot)

Single source of truth for model IDs, versions, and parameter defaults used by Prompt Master. SKILL.md routes by **family and tier**; concrete identifiers live only here so they can be refreshed in one place.

## Freshness rule (apply before quoting anything below)

1. If a row's **Last verified** is empty or older than **60 days** from today:
   - With browsing/retrieval available → verify against the official source in the row, use the verified value, and tell the user it was checked today.
   - Without browsing → name the family/tier only and append `(verify current model ID in <source>)`. Never present the stored value as current.
2. A row marked **UNVERIFIED** was inherited from upstream and has never been checked by this fork. Treat it as rule 1 regardless of date.
3. Never invent an ID, context size, parameter, or default that is not in this file or in a source you checked during this session.
4. When you verify a value, the user can update this file: change the value, set **Last verified** to the date, and remove UNVERIFIED.

## Registry

| Provider | Tier / role | Identifier or setting | Status | Last verified | Official source |
|---|---|---|---|---|---|
| Anthropic | Highest-capability long-horizon | `claude-fable-5` | UNVERIFIED (upstream v1.8.0) | — | https://docs.claude.com/en/docs/about-claude/models |
| Anthropic | Flagship (agentic coding, enterprise) | `claude-opus-5` | UNVERIFIED (upstream v1.8.0) | — | same |
| Anthropic | Balanced (speed + intelligence) | `claude-sonnet-5` | UNVERIFIED (upstream v1.8.0) | — | same |
| Anthropic | Fast / economical | Claude Haiku 4.5 | UNVERIFIED (upstream v1.8.0) | — | same |
| OpenAI | Flagship | `gpt-5.6-sol` (alias `gpt-5.6`) | UNVERIFIED (upstream v1.8.0) | — | https://platform.openai.com/docs/models |
| OpenAI | Balanced | `gpt-5.6-terra` | UNVERIFIED (upstream v1.8.0) | — | same |
| OpenAI | Fast / high-volume | `gpt-5.6-luna` | UNVERIFIED (upstream v1.8.0) | — | same |
| OpenAI | ChatGPT/Codex product reasoning controls | "Sol Pro", "Max", "Ultra" (UI only, not API params) | UNVERIFIED (upstream v1.8.0) | — | https://help.openai.com |
| OpenAI | API pro reasoning | `reasoning.mode: "pro"` | UNVERIFIED (upstream v1.8.0) | — | https://platform.openai.com/docs |
| xAI | General / coding / agentic | `grok-4.6`; effort levels low/medium/high/xhigh; default high | UNVERIFIED (upstream v1.8.0) | — | https://docs.x.ai/docs/models |
| Google | Gemini (long context, multimodal) | check current Pro/Flash IDs | UNVERIFIED | — | https://ai.google.dev/gemini-api/docs/models |
| MiniMax | M3 / M2.7 (1M ctx on M2.7, temp 0–1) | as named | UNVERIFIED (upstream) | — | https://www.minimax.io/platform |
| Midjourney | Default version | `--v 7` (default since mid-2025; check for newer) | UNVERIFIED | — | https://docs.midjourney.com/docs/version |
| Black Forest Labs | Flux guidance | ~3.5 (dev), negative prompt unused in default pipelines | UNVERIFIED | — | https://github.com/black-forest-labs/flux |

## Maintenance

- Keep this file short; it may be loaded alongside another reference.
- When a family is renamed, update the rows here only. SKILL.md should not need edits.
