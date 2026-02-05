# Using PM Skills with Claude

This repo contains skill files designed for AI agents. Claude can read these files directly from your workspace and follow them as structured instructions.

## Quick Start
1. Open this repo in your Claude workspace.
2. Choose a skill file (e.g., `skills/user-story/SKILL.md`).
3. Ask Claude to use that skill and specify the output you want.

Example prompt:

```text
Using the skill at skills/prd-development/SKILL.md, draft a PRD for a mobile onboarding redesign. Ask up to 3 clarifying questions first, then proceed.
```

## Claude Code (CLI)
- Open a terminal in this repo.
- Reference the skill path in your prompt so Claude can load it.

Example:

```bash
claude "Using skills/roadmap-planning/SKILL.md, create a Q3 roadmap outline. Ask 2 clarifying questions first."
```

Tips:
- Use absolute or repo-relative paths.
- If the output drifts, restate the required sections (Purpose, Key Concepts, Application, Examples, Common Pitfalls, References).

## Claude Cowork
- Import this repo as a knowledge source in Cowork.
- Reference the exact skill file path in your task prompt.

Example:

```text
Use skills/positioning-statement/SKILL.md to draft a positioning statement for a mid-market analytics SaaS. Ask for missing inputs before drafting.
```

Tips:
- For interactive skills, answer with numbers ("2" or "1 & 3") to move through options quickly.
- For workflow skills, ask Claude to outline phases first, then run one phase at a time.

## Troubleshooting
- **File not found**: Confirm the repo is connected and the path is correct.
- **Generic output**: Provide constraints (audience, goals, timeline) and ask for clarifying questions before drafting.
