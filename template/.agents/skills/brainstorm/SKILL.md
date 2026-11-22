---
name: brainstorm
description: Probe the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'brainstorm' trigger phrases.
---

Interview the user relentlessly until you reach a shared understanding. Map the decisions as a **design tree** where each decision opens the questions that hang off it. Start from the user's intended outcome and use only the local context needed to resolve the choices at hand.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

Format a round like so:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>

---

❓ **Q2** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

Each round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Accept free-form answers, examples, and corrections. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round, not this one.

Finding _facts_ is your job. Delegate independent lookups to read-only subagents when available and useful. Otherwise, check the relevant files, tools, or documentation directly. While research is pending, hold the questions that depend on it and ask the rest of the frontier. State what remains unknown if you cannot verify a fact. The _decisions_ are the user's.

When the material decisions are settled or explicitly deferred, summarize the agreed direction and deferred questions. For a standalone interview, show the summary in chat and ask the user to confirm it. If another workflow started the interview, return the summary for that workflow to present and confirm with the user. Wait for confirmation before acting on the decisions.
