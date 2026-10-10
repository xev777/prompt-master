Credentials removed. Set as environment variables instead of embedding in prompts.
```
## Objective
Deploy the current build using the deploy key from the DEPLOY_API_KEY environment variable.
## Action Boundaries
Stop and ask before running the deploy command; show the exact command first.
```
🎯 Target: Claude Code, 💡 Secret replaced by an env var reference and the deploy gated behind confirmation.
⚠️ Assumptions: env var name DEPLOY_API_KEY, deploy target already configured
This prompt is for an agentic tool with real system access. Review the scope locks, forbidden actions, and stop conditions before pasting. Confirm file paths, directories, and permissions match the actual project.
