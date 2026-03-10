# Agentic AI Specifications — Overview

This folder defines agentic patterns for deterministic, production-safe behavior.

## Standard agents
- **Orchestrator**: routes requests, maintains session/game lifecycle
- **Rule Engine**: deterministic enforcement of rules and constraints
- **Validation Agent**: checks user inputs and state transitions
- **Scoring Agent**: computes points/outcomes deterministically

All agents MUST:
- produce deterministic, machine-readable outputs
- avoid inventing state; operate only on provided state
