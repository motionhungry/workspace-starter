---
name: system-development
description: Capture, resume, implement, validate or review improvements to skills, instructions, note structures and workflows in the current workspace. Use after brainstorming when saving an agreed improvement proposal.
---

# System Development

Use the record conventions in `90 System Development/AGENTS.md` and the active repository's Git policy. Start with the requested mode. Capture and targeted work stay scoped to the ticket.

## Capture and resume

Search current tickets and relevant archive entries for a match. Update a matching ticket with new evidence. If a closed issue recurs, reopen it and record why. Link a new ticket when the problem is materially different.

An explicit request to capture authorizes saving. Follow the workspace's capture policy for assistant-discovered ideas. Record the source, known problem, evidence, known outcome, and next step. Label inferences and leave open design questions for later. Give the user the saved ID and path.

On resumption, read the ticket, linked decisions, and relevant previous attempts. Reconcile interrupted work, local changes, and unpushed checkpoints before editing. Mark only work being actively undertaken as `in-progress`.

## Develop

1. Use the ticket as the working spec. Keep the proposed change, observable acceptance criteria, approval scope, results, and next step there. For larger changes, keep the shared design in a parent ticket and link child deliverables. Use [Brainstorm](../brainstorm/SKILL.md) for unresolved material choices. Obtain approval for implementation before acting on a capture or investigation request.
2. Recommend a custom subagent when a repeatable, independently delegable job has a clear input and output and benefits from a distinct perspective, tool access, or reasoning depth. Use [Skill Creator](../skill-creator/SKILL.md) for reusable local skills. Consult the [frontmatter guidance](references/frontmatter.md) when defining a note type or changing its fields.
3. For a lasting choice with consequential alternatives or a changed convention, link a decision record with the tradeoffs, consequences, approval, and when to revisit it. Put the current rule in the applicable instructions or skill.
4. Validate the approved change against its criteria. Use a disposable workspace for test records and use read-only checks against actual records when useful. Keep concise evidence in the ticket and checkpoint under the active repository's Git policy.
5. Wrap up each ticket worked on. Leave it `validating` while real-use evidence is pending, close it as resolved when the criteria are satisfied, or record the applicable disposition. Return unsuccessful attempts to `open` with what was learned and a next step. Use a linked journal for substantive findings worth keeping.

## Review

For an explicit system review, give a fresh read-only subagent the scope, relevant records, and questions. Ask it to inspect the evidence independently across current tickets, pending validation, decisions, and recent relevant journals. For a requested deeper audit, include the underlying skills and instructions in scope. Have it cite evidence, distinguish findings from hypotheses, and rank priorities by impact, recurrence, blocked work, and effort.

The reviewer reports to the primary assistant. Verify the material findings yourself and request a targeted follow-up if the evidence is unclear. Present the verified findings and choices that need the user's judgment. The user selects what to develop. Keep the review read-only until the user approves recording or acting on a finding. If delegation is unavailable, report that independent review is pending and offer a fresh-session review.
