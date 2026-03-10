# AI Solutions Platform (Google AI Studio + Gemini) — Template Repository

This repository is a **startup GitHub template** for building **AI-enabled applications** with:
- **Governed prompts** (system/user separation, deterministic output contracts)
- **Agentic specifications** (orchestrator, rules, validation, scoring)
- **Backend patterns** (Genkit/Cloud Run/Firebase) and **mobile apps**

## What you get
- Governance: Prompt review checklist, RACI, prompt asset register template
- Agentic specs: state machine, decision boundaries, failure modes
- Prompt library: reusable templates + sample app prompts (Quiz + Ludo)
- CI: prompt/schema validation pipeline
- API: OpenAPI contract stub for backend endpoints

## Repo layout
See [`docs/REPO_STRUCTURE.md`](docs/REPO_STRUCTURE.md).

## Branching & release workflow
This template follows a **develop → main** flow:
- `develop`: lower environments (DEV). Feature branches merge to develop via PR.
- `main`: stage/prod. No direct commits. Cherry-pick from develop after validation.

> Source: internal workflow note captured in <Email>GitHub Repository Workflow Guidelines</Email>. citeturn10search153

## Quick start (local)
1. Copy `.env.example` to `.env` and set `GEMINI_API_KEY`.
2. Use the prompts in `prompts/` to prototype in Google AI Studio.
3. Implement backend flows using `backend/` skeleton and keep keys server-side.

## Template usage (GitHub)
1. Create a new repository from this template.
2. In GitHub: **Settings → Template repository → Enable**.
3. Rename namespaces (`quiz-game`, `ludo`) and update owners in `CODEOWNERS`.
