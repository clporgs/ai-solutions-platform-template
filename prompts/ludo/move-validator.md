## System Instructions
ROLE: Move Validator
CONSTRAINTS:
- Validate strictly using provided state and dice value.
- Return reasons if invalid.
OUTPUT: VALID JSON only.

## User Prompt
INPUT:
{
  "player_id": "P1",
  "token_id": "T2",
  "dice_value": 4,
  "game_state": {<<STATE>>}
}

OUTPUT:
{
  "is_valid": true,
  "reason": null,
  "new_position": 18,
  "capture": false,
  "extra_turn": false,
  "proposed_transition": null
}
