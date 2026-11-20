---
name: setup
description: Set up Workspace Starter, resume incomplete setup, or open an existing vault on a new computer.
---

# Set up or resume the workspace

Work from the vault root. Reuse existing choices and ask only about unresolved ones.

Guide the operator through one choice at a time. Start with one sentence about what is ready, then ask one plain-language question. Give click-by-click instructions when the operator chooses an option that needs action. Keep commit IDs, remote names, branch names, and discovery details for troubleshooting or when the choice depends on them.

For a decision with two or three clear options, use the session’s built-in choice picker when available. Otherwise, present a short numbered list in chat. Put the recommendation first and include **Decide later** when deferral is supported. Wait for the operator’s answer before acting on that choice. Confirm the actual backup destination and policy separately before the first backup.

For backup, explain that a private online copy lets the operator recover the vault or use it on another computer. Offer to use an existing private repository, walk them through creating one, or continue with local work and set up backup later. For GitHub, after they choose to create one, guide them to **New repository**, choose **Private**, leave the initialization options unchecked, and ask them to share the repository link. Use the [backup instructions](references/settings-and-backup.md) to confirm the destination and settings. Present any technical settings that need approval as one recommended bundle and explain what it does.

1. **Inspect the vault.** Verify local file and command access, Git 2.28+, and Python 3.9+. Inspect `90 System Development/workflow-settings.json`, ignored `.agents/local.json` if present, and Git state if initialized. Investigate missing provenance before editing and preserve existing work. Use the [first-proposal procedure](references/first-proposal.md) to find any existing proposal.
2. **Verify Obsidian and backup.** If Obsidian access is unverified, tell the operator how to use **Open folder as vault** and what to look for. Use desktop controls only if the operator asks. When the vault is already open and the Obsidian CLI is enabled, a read-only check can confirm the vault and expected folders. Record an unconfirmed check as pending and continue. Follow [settings and Git backup](references/settings-and-backup.md) to establish or verify Git history, identity, and the approved backup. If backup is pending, preserve local work and continue once the vault is locally usable.
3. **Configure media, updates, and skill discovery.** Follow [media setup](references/media.md) when the destination is undecided or access needs checking. If the operator has yet to choose, offer to install a skill for checking starter updates on request. Record `starter.update_review` as `enabled` or `declined`. If enabled, use `python3 .agents/skills/setup/scripts/workspace.py enable-updates` to install it. Preserve its edits and review history. Follow [skill discovery](references/discovery.md) when configuring a new copy or checking discovery in a fresh session.
4. **Checkpoint and continue.** Checkpoint reviewed setup files under the approved Git policy and report any pending backup. Once the local vault is usable, use [Brainstorm](../brainstorm/SKILL.md) for the first proposal if it is absent. On resumption, report the existing proposal and handle pending checks. If backup was approved after the proposal was saved, validate and checkpoint the existing note. Retry an unpushed commit without restaging it.
