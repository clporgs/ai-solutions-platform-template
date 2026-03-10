# Agent Decision Boundaries

## Principle
Agents have strict responsibility boundaries to prevent logic drift.

## Orchestrator (A)
**Can:** select which agent runs next; persist session; decide state transitions.
**Cannot:** invent facts, scores, or validate rules without the rule/validation agent.

## Rule Engine (B)
**Can:** enforce formal rules; validate moves; emit deterministic results.
**Cannot:** generate creative content; alter global session state.

## Content Generator (C)
**Can:** generate questions/content within constraints.
**Cannot:** change scores/state; override validation; fabricate current affairs facts.

## Validation Agent (D)
**Can:** validate user answers/moves against rules and state.
**Cannot:** generate content; decide winners.

## Scoring Agent (E)
**Can:** compute score deltas and win conditions.
**Cannot:** create or alter rules.

## Required output contract
Every agent output MUST include:
```json
{ "agent": "...", "decision": "...", "confidence": "high|med|low", "evidence": [], "proposed_transition": null }
```
