# Using PM Skills with Codex

Codex can apply these skills directly from your repo files. There are two practical paths:
- Local workspace (Codex in your coding environment)
- Codex on ChatGPT (`chatgpt.com/codex`) with GitHub connected

---

## Option 1: Local Workspace (Fastest)

1. Open this repo in your Codex workspace.
2. Pick a skill file at `skills/<skill-name>/SKILL.md`.
3. Prompt Codex with the explicit file path.

Example:

```text
Using the skill at skills/prd-development/SKILL.md, create a PRD for a mobile onboarding redesign. Ask up to 3 clarifying questions first, then proceed.
```

### How to Apply Skill Types

- **Component skills**: ask for a specific artifact (for example, user story, positioning statement, epic hypothesis).
- **Interactive skills**: expect 3-5 adaptive questions, then numbered recommendations.
- **Workflow skills**: ask Codex to outline phases, then execute one phase at a time.

### Chain Multiple Skills

```text
First use skills/problem-framing-canvas/SKILL.md to define the problem. Then apply skills/user-story/SKILL.md to write stories for the chosen solution.
```

---

## Option 2: Codex on ChatGPT (GitHub-Connected)

Codex on ChatGPT works against connected repos. No ZIP upload flow is required.
Availability can vary by plan and rollout region.

1. Open [Codex](https://chatgpt.com/codex).
2. Connect GitHub when prompted (or via ChatGPT settings).
3. Select this repo and branch.
4. Prompt Codex to use a specific skill path, for example:

```text
Use skills/finance-based-pricing-advisor/SKILL.md to evaluate whether we should test a 10% price increase. Show assumptions and risks.
```

### Practical Prompt Pattern

Use this structure to keep outputs consistent:

```text
Using skills/<skill-name>/SKILL.md:
1) Ask up to 3 clarifying questions.
2) Follow the skill sections exactly.
3) Show output in markdown.
4) End with risks, assumptions, and next steps.
```

---

## Troubleshooting

- **Codex cannot find the file**: confirm repo/branch selection and exact case-sensitive path.
- **Output is generic**: provide real constraints (stage, KPI target, customer segment, timeline).
- **Format drift**: explicitly instruct Codex to follow `Purpose, Key Concepts, Application, Examples, Common Pitfalls, References`.

---

## Official References

- [Codex in ChatGPT](https://openai.com/index/introducing-codex/)
- [Getting started with Codex](https://help.openai.com/en/articles/11096431-getting-started-with-codex)
- [Apps in ChatGPT (GitHub connection)](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt/)
