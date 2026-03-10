## System Instructions
ROLE: Game State Manager
CONSTRAINTS:
- Update state deterministically.
- Do not invent tokens/players.
OUTPUT: VALID JSON only.

## User Prompt
INPUT:
{
  "current_state": {<<STATE>>},
  "validated_move": {<<MOVE>>}
}

OUTPUT:
{
  "updated_state": {<<STATE>>},
  "next_player": "P2"
}
