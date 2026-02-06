---
name: workshop-facilitation
description: Facilitate workshop sessions in a multi-turn, one-step flow with numbered recommendations each turn. Use alongside workshop skills to guide choices and keep advice context-aware.
type: interactive
---

## Purpose
Provide a consistent facilitation pattern for workshop-style skills: one step at a time, with numbered recommendations that adapt to prior answers.

## Key Concepts
- **One-step-at-a-time:** Ask a single targeted question per turn.
- **Enumerated recommendations:** Provide 3-4 numbered options with a recommended choice first, so users can reply "Choice 1" or "1 & 3."
- **Context-aware progression:** Each turn builds on previous answers and avoids re-asking resolved questions.
- **Fast path:** If the user requests a single-shot output, skip the multi-turn flow and deliver a condensed result.

## Application
1. Confirm goal and scope in one question if missing.
2. Ask one targeted question that advances the workshop.
3. Offer 3-4 numbered, context-aware recommendations.
4. Accept a numbered choice or a custom alternative.
5. Update context and repeat until outputs are complete.
6. Summarize decisions and deliver final artifacts.

## Examples
**Question:** "What scope should we map?"
1. **End-to-end journey** (Recommended)
2. **Single workflow**
3. **Specific pain point**
4. **Existing backlog slice**

**User:** "1"

**Next question:** "Which persona should anchor the map?"
1. **Primary persona** (Recommended)
2. **High-churn segment**
3. **Newly discovered persona**

## Common Pitfalls
- Asking multiple questions in the same turn.
- Offering generic options that ignore user context.
- Ignoring the user's chosen option or custom direction.

## References
- Apply alongside workshop skills in `skills/*-workshop/SKILL.md` when a facilitated, multi-turn flow is desired.
