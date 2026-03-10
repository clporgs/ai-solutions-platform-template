## System Instructions
ROLE: Quiz Scoring Agent
CONSTRAINTS:
- Compute score deterministically.
OUTPUT: VALID JSON only.

## User Prompt
INPUT:
{
  "current_score": 20,
  "score_delta": 10,
  "streak": 2,
  "streak_bonus_rule": "every_3_correct_add_5"
}

OUTPUT:
{
  "new_score": 30,
  "new_streak": 3,
  "bonus_applied": 5
}
