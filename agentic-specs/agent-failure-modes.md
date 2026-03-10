# Agent Failure Modes

## 1. Quota / Rate limiting (429)
- Symptom: RESOURCE_EXHAUSTED / 429
- Control: exponential backoff + user-visible retry guidance

## 2. Schema violations
- Symptom: non-JSON output where JSON required
- Control: strict system instruction + server-side JSON validation

## 3. Hallucinated state
- Symptom: agent outputs positions/scores not derivable from state
- Control: validation agent rejects; orchestrator logs and replays with stricter constraints

## 4. Non-deterministic randomness
- Symptom: dice rolls not reproducible when required
- Control: require explicit RNG seed; otherwise use server RNG, not LLM

## 5. Toxic/unsafe content (quiz)
- Symptom: inappropriate question content
- Control: allowlist categories; blocklist; moderation pass; fallback bank

## 6. Partial failure
- Symptom: one agent fails but session must continue
- Control: orchestrator degrades gracefully (skip round / default scoring)
