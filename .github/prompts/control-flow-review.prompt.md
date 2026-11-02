---
description: "Control Flow Review: Branching logic hides missing branches, precedence mistakes and boundary errors."
---
Review the control flow of this function by enumeration, not by reading.

Rules it must implement: [RULES]
Function: [CODE]

1. List every atomic condition and the variables it reads.
2. Build a decision table of condition combinations (use equivalence classes and boundaries if there are more than four conditions; say what you grouped).
3. For each row trace the code and state the actual outcome. Do this before comparing to the rules.
4. Compare to the rules. Mark mismatches and rows with no defined intended outcome.
5. Look specifically for: missing else or default, unreachable branches, conditions that are always true or false, && / || precedence, negation errors, < versus <=, switch fall-through, enum values not handled.
6. For each defect give the smallest fix and the test row that fails before and passes after.
Cite the file and symbol for every claim you make about the code.

---
Generated from [prompts/code_review/control-flow-review.md](../../prompts/code_review/control-flow-review.md) by scripts/sync_adapters.py. Replace any [BRACKETED PLACEHOLDER] before sending. Validate the answer with the steps in the source file.
