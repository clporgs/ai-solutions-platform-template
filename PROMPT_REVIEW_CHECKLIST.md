# Prompt Review Checklist (Architecture + Governance)

## A. Business Alignment
- [ ] Use-case is defined and mapped to a business capability
- [ ] Success criteria is measurable and documented

## B. Prompt Design Quality
- [ ] System Instructions and User Prompt are strictly separated
- [ ] Persona/role is explicit
- [ ] Constraints include "do not speculate" and missing-data behavior

## C. Output Contract
- [ ] Output format is explicitly defined (JSON/Table/Fixed headings)
- [ ] Schema includes required/optional keys and null-handling rules

## D. Risk Controls
- [ ] Grounding rules: use only provided context where applicable
- [ ] Evidence fields (quotes/citations) present for compliance scenarios

## E. Model & Cost Controls
- [ ] Model choice justified (Flash/Flash-Lite/Pro)
- [ ] 429 handling defined (retry/backoff)

## F. Security
- [ ] Data sensitivity classification defined
- [ ] API keys are server-side only (never in clients)

## G. Testing & Lifecycle
- [ ] Golden test set exists and is referenced
- [ ] Versions and change log updated

## Decision
- [ ] Approved
- [ ] Approved with conditions
- [ ] Rejected

Reviewer: __________ Date: __________
