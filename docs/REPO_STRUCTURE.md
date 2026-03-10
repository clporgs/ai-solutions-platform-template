# Repository Structure

## Mapping to SDLC

### Source control
- `prompts/`: Prompt library (versioned)
- `agentic-specs/`: Agent contracts and boundaries
- `backend/`: API/flows (Genkit skeleton)
- `apps/`: mobile/web clients

### Build & validation
- `.github/workflows/`: CI pipelines
- `tools/validate_prompts.py`: schema/contract checks
- `tests/`: golden prompt regression sets

### Deployment
- `deployment/openapi.yaml`: API contract
- `deployment/cloud-run/`: manifests (placeholder)
- `deployment/firebase/`: manifests (placeholder)
