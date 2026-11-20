---
name: brainstorm
description: Brainstorm or stress-test a plan, decision, or idea through rounds of questions and recommendations. Use during workspace setup to clarify the purpose and first useful capability, or during system development to resolve design choices.
---

# Brainstorm

Interview the user until you reach a shared understanding. Map the decisions as a **design tree** where each decision opens the questions that depend on it. Start from the user's intended outcome and use only the local context needed to resolve the choices at hand.

Work in rounds. Ask the whole **frontier**, the decisions whose prerequisites are settled. Number each question and give your recommended answer with a brief reason. Use this format:

> ❓ **Q1 — Decision title**
>
> Ask the question.
>
> ➡️ Give your recommendation and why.

Wait for the user's response. Accept a free-form reply across multiple questions and use any examples or corrections to update the tree. Follow up on unresolved decisions in the next round. Hold questions whose answers depend on an unsettled decision. Look up facts available from files, tools, or documentation. When useful and available, use read-only subagents so independent questions can proceed while research is pending. The user makes the decisions.

Probe assumptions, tradeoffs, and failure cases that could change the decision. Follow up on vague or conflicting answers. Stop when the user has resolved the material choices or explicitly deferred them. Use the relevant handoff to summarize and confirm the agreed direction before taking action.

- **During setup** — Return the agreed purpose, first capability, boundaries, acceptance criteria, and next step to [System Development](../system-development/SKILL.md) for the first proposal preview and save confirmation.
- **During an existing improvement** — Reuse its record and relevant decisions. Once the user confirms the summary, return the agreed scope, acceptance criteria, and any explicitly deferred questions to the owning improvement.
- **For a new workspace improvement** — Once the user confirms the summary, offer a handoff to system development. If the request is only to capture an idea, use its capture path directly without interviewing the user.

For other topics, summarize and confirm the agreed direction and finish the brainstorm.
