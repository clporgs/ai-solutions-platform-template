# Agent State Machine

Defines canonical lifecycle states and transitions for agentic apps.

## 1. Common State Model
Represent state as JSON:
```json
{
  "session_id": "...",
  "app": "quiz|ludo",
  "state": "INIT|LOBBY|IN_PROGRESS|PAUSED|FINISHED|ERROR",
  "turn": {"player_id": "P1", "number": 1},
  "context": {"difficulty": "medium"},
  "payload": {},
  "errors": []
}
```

## 2. Allowed Transitions
- INIT → LOBBY
- LOBBY → IN_PROGRESS
- IN_PROGRESS → PAUSED | FINISHED | ERROR
- PAUSED → IN_PROGRESS | FINISHED
- ERROR → FINISHED (graceful shutdown)

## 3. Transition Rules
- Only **Orchestrator** may transition global `state`.
- Rule/Validation/Scoring agents may only return `proposed_transition`.

## 4. Determinism
- Transition decisions must be computed from input state + action.
- No time-based randomness unless explicitly provided (e.g., RNG seed).
