# Using PM Skills with Codex

This repo is a library of PM skill files designed for AI agents. Codex can read these files directly from your workspace and follow them as structured instructions.

## Quick Start
1. Clone or open this repo in your Codex workspace.
2. Pick a skill file from `skills/<skill-name>/SKILL.md`.
3. Ask Codex to use the skill by referencing the file path.

Example prompt:

```text
Using the skill at skills/prd-development/SKILL.md, create a PRD for a mobile onboarding redesign. Ask up to 3 clarifying questions first, then proceed.
```

## How to Apply Skills
- **Component skills**: Use when you need a specific artifact (user story, positioning statement, epic hypothesis). Ask Codex to produce the artifact using the skill's template and quality criteria.
- **Interactive skills**: Expect 3-5 questions, then numbered recommendations. Answer with a number (e.g., "2") or a combination ("1 & 3").
- **Workflow skills**: These run multi-phase processes. Ask Codex to outline the phases first, then execute one phase at a time.

## Working with Multiple Skills
You can chain skills explicitly:

```text
First use skills/problem-framing-canvas/SKILL.md to define the problem. Then apply skills/user-story/SKILL.md to write stories for the chosen solution.
```

## Tips
- Reference the skill file path explicitly to avoid ambiguity.
- If Codex goes off-format, remind it to follow the skill sections (Purpose, Key Concepts, Application, Examples, Common Pitfalls, References).
- Keep your context focused: supply goals, constraints, and target user details.

## Troubleshooting
- **Codex says it cannot find a file**: Confirm the repo is open and the path is correct.
- **Output is generic**: Provide more specific constraints and examples, or ask Codex to ask clarifying questions before drafting.
