```
Classify each support ticket into exactly one category: Billing, Technical, Account, Shipping, Other.
Return JSON: {"id": "...", "category": "...", "confidence": "high|low"}.
Use "Other" when no category clearly fits, and mark confidence low when two categories fit.
<examples>
<example><input>Charged twice this month</input><output>{"id":"1","category":"Billing","confidence":"high"}</output></example>
<example><input>App crashes and I can't log in</input><output>{"id":"2","category":"Technical","confidence":"low"}</output></example>
</examples>
<tickets>[paste]</tickets>
```
🎯 Target: Claude (Haiku 5.5 suits high-volume classification), 💡 Few-shot with an ambiguous case locks format and the tie rule.
⚠️ Assumptions: the 5 category names, JSON output, two-level confidence
