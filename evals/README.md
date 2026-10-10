# Evals

Regression checks for the skill's hard rules and output format (not a quality score).

1. For each case in `cases.json`, start a fresh conversation with the skill installed and send `input`.
2. Save the full reply to `outputs/<id>.md`.
3. Run `python check.py outputs/` — prints PASS / FAIL / SKIP per case; exit code 1 if any fail.

The `emphatic-overuse` case may produce false positives on legitimate safety constraints; review by hand.
Add a case whenever a bug is found in the skill's output.
