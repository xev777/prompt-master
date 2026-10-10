```
<context>
You will receive one contract in <contract> tags.
</context>
<task>
Summarize the contract for a non-lawyer: parties, term, payment obligations, termination rights, liability caps, and unusual clauses.
</task>
<output_format>
Headed sections in that order, max 300 words. Quote clause numbers for each point. If a section is absent, say "Not found".
</output_format>
Base the summary only on the contract text.
<contract>[paste]</contract>
```
🎯 Target: Claude Opus 5.5 (`claude-opus-5-5`, verified in models.md 2026-10-10; use Fable 5.1 for very long or complex contracts), 💡 XML separation and clause citations keep the summary grounded.
⚠️ Assumptions: non-lawyer audience, 300-word cap, single contract per call
