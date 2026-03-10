# Hello World – AI Solution Toolkit

This tutorial is the **starting point** for every developer using the **AI Solution Toolkit Template**.

## Objective
Create your first **governed AI prompt**, experience **prompt validation failure**, fix it, and successfully merge a PR.

This is the AI equivalent of `print("Hello World")`.

---

## Step 1: Choose a Simple Use Case
We will build a **Greeting Generator**.

**Input:** Name  
**Output:** Friendly greeting in JSON

---

## Step 2: Prototype in Google AI Studio

### System Instructions
```
ROLE: Greeting Generator
CONSTRAINTS:
- No emojis
- No speculation
OUTPUT:
- VALID JSON only
```

### User Prompt
```
TASK: Generate a greeting
NAME: Alex
```

Expected output:
```json
{ "greeting": "Hello Alex! Welcome to AI development." }
```

---

## Step 3: Add Prompt to Repo
Create folder:
```
prompts/hello-world/
```

Add `system.md` and `greeting-generator.md`.

---

## Step 4: Create Feature Branch
```
git checkout -b feature/hello-world
```

---

## Step 5: Fail Prompt Validation (On Purpose)
Remove JSON constraint from system prompt.
Commit and push.

CI will fail ✅

---

## Step 6: Fix Prompt
Restore JSON constraint.
Push again.

CI will pass ✅

---

## Step 7: Raise PR and Merge
Prompt is now:
- Deterministic
- Governed
- Production-ready

🎉 You have completed your AI Hello World.

---

## What You Learned
- Prompt ≠ free text
- Governance adds safety
- CI protects AI quality

Proceed to next tutorial when ready.
