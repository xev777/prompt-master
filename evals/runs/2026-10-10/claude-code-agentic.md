```
## Objective
Add JWT authentication to the existing Express API so protected routes reject requests without a valid token.

## Context
Express API in src/. No auth layer exists yet.

## Target State
- src/middleware/auth.js verifies a Bearer JWT and attaches the user to req.
- POST /auth/login issues a signed token; protected routes use the middleware.
- Tests cover valid, expired, missing, and malformed tokens.

## Scope
- Work only in: src/ and tests/
- Do not touch: .env, package-lock.json, deployment or CI config

## Constraints
- Read the signing secret from the JWT_SECRET environment variable.
- Only make changes directly requested.

## Acceptance Criteria
- [ ] Protected route returns 401 without a token
- [ ] Valid token returns 200
- [ ] npm test passes

## Action Boundaries
- Proceed with reversible, in-scope inspection, edits, and test runs.
- Stop and ask before adding any dependency (e.g., jsonwebtoken), deleting files, or changing the database schema.

## Progress Evidence
Ground every completion claim in a test run or changed file.
```
🎯 Target: Claude Code, 💡 Front-loaded outcome, file scope, and stop points so the agent cannot over-scope.
⚠️ Assumptions: login route path /auth/login, tests in tests/, npm test as the test command, JWT_SECRET env var
This prompt is for an agentic tool with real system access. Review the scope locks, forbidden actions, and stop conditions before pasting. Confirm file paths, directories, and permissions match the actual project.
