# Model Registry (dated snapshot)

Single source of truth for model IDs, versions, and parameter defaults used by Prompt Master. SKILL.md routes by **family and tier**; concrete identifiers live only here so they can be refreshed in one place.

## Freshness rule (apply before quoting anything below)

1. If a row's **Last verified** is empty or older than **60 days** from today:
   - With browsing/retrieval available → verify against the official source in the row, use the verified value, and tell the user it was checked today.
   - Without browsing → name the family/tier only and append `(verify current model ID in <source>)`. Never present the stored value as current.
2. A row marked **UNVERIFIED** has never been checked against its source. Treat it as rule 1 regardless of date.
3. Never invent an ID, context size, parameter, or default that is not in this file or in a source you checked during this session.
4. When you verify a value, the user can update this file: change the value, set **Last verified**, and remove UNVERIFIED.

## Registry

| Provider | Tier / role | Identifier or setting | Status | Last verified | Official source |
|---|---|---|---|---|---|
| Anthropic | Top tier: hardest reasoning, long-horizon agents | `claude-fable-5-1` (Claude Fable 5.1). Thinking adaptive, always on; default effort `high` | Verified | 2026-10-10 | https://platform.claude.com/docs/en/models/overview |
| Anthropic | Recommended starting point: agentic coding, knowledge work | `claude-opus-5-5` (Claude Opus 5.5). Thinking adaptive, always on; default effort `medium` | Verified | 2026-10-10 | same |
| Anthropic | Balanced speed + intelligence | `claude-sonnet-5-5` (Claude Sonnet 5.5). Adaptive thinking; default effort `high` | Verified | 2026-10-10 | same |
| Anthropic | Fast / high-volume (classification, extraction, routing) | `claude-haiku-5-5` (Claude Haiku 5.5). Adaptive thinking; default effort `medium` | Verified | 2026-10-10 | same |
| OpenAI | Most capable | `gpt-6-astra` (GPT-6 Astra). Effort: low/medium/high/xhigh/max | Verified | 2026-10-10 | https://developers.openai.com/api/docs/models |
| OpenAI | Near-flagship, lower cost | `gpt-6.1-sol` (GPT-6.1 Sol). Effort: low/medium/high/xhigh/max | Verified | 2026-10-10 | same |
| OpenAI | Efficient / high-volume | `gpt-6-luna` (GPT-6 Luna). Effort: none/low/medium/high/xhigh/max | Verified | 2026-10-10 | same |
| OpenAI | o-series (o3, o4-mini) | Not listed on the current models page — treat as legacy; prefer the GPT-6 family | Verified (absence) | 2026-10-10 | same |
| OpenAI | ChatGPT/Codex product controls; API "pro" reasoning mode | Not documented on the models page; do not quote names | UNVERIFIED | — | https://help.openai.com |
| xAI | Flagship (chat, coding, agentic) | `grok-4.7`. `reasoning_effort`: low/medium/high/xhigh, default `high`; reasoning cannot be disabled. Aliases: `<name>` stable, `<name>-latest`, `<name>-<date>` | Verified | 2026-10-10 | https://docs.x.ai/docs/models · https://docs.x.ai/docs/guides/reasoning |
| xAI | Image / video | `grok-imagine-image-2.0`, `grok-imagine-video-1.5` | Verified | 2026-10-10 | https://docs.x.ai/docs/models |
| Google | Latest Pro | `gemini-3.1-pro-preview` (preview) | Verified | 2026-10-10 | https://ai.google.dev/gemini-api/docs/models |
| Google | Latest Flash (stable) | `gemini-3.8-flash` | Verified | 2026-10-10 | same |
| MiniMax | M3 / M2.7 (1M ctx on M2.7, temperature 0–1) | as named | UNVERIFIED | — | https://www.minimax.io/platform |
| Midjourney | Default version | V8.2 is the default (`--v 8.2`); also 8.1, 7, 6.1, 6. V8.0 retired. `--no` supported on V6+ | Verified | 2026-10-10 | https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version |
| Black Forest Labs | FLUX.2 negative prompts | Not supported — rewrite exclusions as positive descriptions ("sharp focus" instead of "not blurry") | Verified | 2026-10-10 | https://help.bfl.ai/articles/4358307410-does-flux-2-support-negative-prompting |
| Black Forest Labs | FLUX.1 dev guidance | ~3.5 typical | UNVERIFIED | — | https://github.com/black-forest-labs/flux |

## Maintenance

- Keep this file short; it may be loaded alongside another reference.
- When a family is renamed, update the rows here only. SKILL.md should not need edits.
- Upstream v1.8.0 listed `claude-opus-5`, `claude-fable-5`, `claude-sonnet-5`, Haiku 4.5, `gpt-5.6-sol/terra/luna`, and `grok-4.6`. None matched the official pages on 2026-10-10.
