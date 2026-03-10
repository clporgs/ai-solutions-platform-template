import os, sys, json

REQUIRED_FILES = [
  'prompts/quiz-game/system.md',
  'prompts/quiz-game/question-generator.md',
  'prompts/ludo/system.md',
  'agentic-specs/agent-state-machine.md',
  'agentic-specs/agent-decision-boundaries.md',
  'agentic-specs/agent-failure-modes.md'
]

missing = [p for p in REQUIRED_FILES if not os.path.exists(p)]
if missing:
    print('Missing required files:')
    for m in missing:
        print(' -', m)
    sys.exit(1)

# Lightweight rules: ensure key keywords for determinism are present
checks = {
  'prompts/quiz-game/system.md': ['OUTPUT', 'JSON'],
  'prompts/ludo/system.md': ['OUTPUT', 'JSON'],
  'agentic-specs/agent-decision-boundaries.md': ['Decision Boundaries', 'Required output contract'],
}

failed = False
for path, must_have in checks.items():
    text = open(path, 'r', encoding='utf-8').read()
    for kw in must_have:
        if kw not in text:
            print(f'Validation failed: {path} missing "{kw}"')
            failed = True

if failed:
    sys.exit(2)

print('Prompt validation passed.')
