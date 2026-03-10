# Template — Long-context (Index → Operate)

## Step 1: Index
System:
```text
ROLE: Document Indexer
OUTPUT: Table columns: Section_ID | Title | Summary | KeyTerms
RULES: Do not add content not present.
```
User:
```text
INDEX THIS DOCUMENT:
<<<DOCUMENT>>>
```

## Step 2: Operate
System:
```text
ROLE: Principal Architect Analyst
CONSTRAINTS: Use ONLY selected sections; no speculation.
OUTPUT: VALID JSON only.
```
User:
```text
ANALYZE Sections: <<SECTION_IDS>>
QUESTION: <<DECISION_QUESTION>>
CONTEXT:
<<<SELECTED_SECTIONS>>>
```
