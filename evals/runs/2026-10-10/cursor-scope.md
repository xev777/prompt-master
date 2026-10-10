```
File: src/pages/Login.tsx
Function: handleLogin

Current Behavior:
Crashes with a null reference when the login response or user object is null.

Desired Change:
Guard against null and show the existing error message instead of crashing.

Scope:
Only modify handleLogin. Do not touch other components, API clients, or types.

Done When:
Submitting with a null response shows the error message and the app does not crash; existing tests pass.
```
🎯 Target: Cursor, 💡 Anchored to one file and function with a binary Done When.
⚠️ Assumptions: null comes from the login response, an error message component already exists
This prompt is for an agentic tool with real system access. Review the scope locks, forbidden actions, and stop conditions before pasting. Confirm file paths, directories, and permissions match the actual project.
