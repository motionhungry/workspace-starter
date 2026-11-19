---
name: system-development
description: Capture, resume, implement, validate or review improvements to skills, instructions, note structures and workflows in the current workspace. Use after brainstorming when saving an agreed improvement proposal.
---

# System Development

Read root `AGENTS.md` and `90 System Development/AGENTS.md` in the active workspace. This skill also serves maintainer work. Follow the active repository's Git policy and keep its development records with that repository.

## Capture and resume

Search active improvements for a matching issue, and check relevant archive entries when the issue has recurred. Update or reopen the matching record with new evidence. Follow the workspace's capture permission policy for assistant-discovered ideas. An explicit request to capture an idea authorizes saving it. Capture the known problem and next step. Leave unresolved design or acceptance criteria for later discussion.

For the first proposal during setup, run `python3 .agents/skills/system-development/scripts/records.py first` from the workspace root. An existing path means setup can resume using that record, including if it was archived. Exit 1 means the reserved record is absent. Resolve an error with exit 2 before saving. Once the user approves saving, fill [the improvement template](assets/improvement.md) with `IMP-0001`, open status, both actual local dates, the approved proposal and its save authorization. Use a temporary draft outside the workspace and run `python3 .agents/skills/system-development/scripts/records.py save-first --draft <draft-path>`. The command validates and creates the reserved note without replacing any existing record. Read the saved note, give the operator its workspace-relative path, and follow the workspace policy for a proposal-save checkpoint. When backup is pending, preserve the note and report its actual backup status.

On resumption, read the selected improvement, linked decisions, and relevant instructions. Reconcile any interrupted work, including local changes and unpushed checkpoints, before editing. Record whether work continues, awaits validation, or should return to open with a next step.

## Develop

1. Investigate the problem within the requested scope. Use [brainstorm](../brainstorm/SKILL.md) if a material design choice is unresolved. Keep the proposal, observable acceptance criteria, scoped authorization, results, and next step in the owning improvement. Ask for implementation approval when the existing authorization covers capturing, planning, or investigation.
2. Recommend a custom subagent when an independently delegable, repeatable task has a clear input and output and would benefit from a distinct perspective, tool access or reasoning depth. For the first follow-on agent-creator improvement, brainstorm the job, inputs, outputs, tools and depth. Explicitly choose or inherit both the model and reasoning effort for each applicable assistant. Check that the combination works and test one independent reviewer on a representative task before defining a shared format.
3. Implement the approved change. If it defines a reusable local skill, use [skill-creator](../skill-creator/SKILL.md). Use a decision record for a lasting choice with consequential alternatives or a changed convention. Link it and retain the approval evidence. Put the operating rule in the applicable instructions or skill.
4. Stop at each useful checkpoint. Validate the changed paths and run representative checks against the agreed criteria before committing. Use a disposable test workspace for mock records. Record the observed results and follow the active workspace's Git policy. In a generated vault with an approved backup policy, use `python3 .agents/skills/setup/scripts/workspace.py checkpoint --message "<description>" -- <explicit paths>` as directed by setup. For the maintainer repository, use its branch and PR workflow.
5. Leave an improvement in `validating` while real-use evidence is pending. Close it as resolved when the criteria are satisfied, or record the applicable disposition. Return unsuccessful attempts to open with concise findings and a next step. For substantive sessions, use a linked journal to retain useful findings that would otherwise be lost.

## Review

For an explicit system review, inspect current improvements, pending validation, governing decisions and relevant recent journals. Highlight recurring problems, conflicting rules and blocked work using observed evidence. Let the user select what to develop. Preserve the existing state where the review yields no change.
