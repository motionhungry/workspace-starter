---
name: setup
description: Set up Workspace Starter, resume incomplete setup, or open an existing vault on a new computer.
---

# Set up or resume the workspace

Work from the vault root. Reuse existing choices and ask only about unresolved ones.

1. **Inspect the vault.** Verify local file and command access, Git 2.28+, and Python 3.9+. Inspect `90 System Development/workflow-settings.json`, ignored `.agents/local.json` if present, and Git state if initialized. Investigate missing provenance before editing and preserve existing work. Use the [first-proposal procedure](references/first-proposal.md) to find any existing proposal.
2. **Verify Obsidian and backup.** If Obsidian access is unverified on this computer, reopen the folder as a vault and check that it shows the inbox and System Development. Ask the operator to confirm if the app is unavailable to you. Record the result in local settings. Follow [settings and Git backup](references/settings-and-backup.md) to establish or verify Git history, identity, and the approved backup. If backup is pending, preserve local work and continue once the vault is locally usable.
3. **Configure media, updates, and skill discovery.** Follow [media setup](references/media.md) when the destination is undecided or access needs checking. If the operator has yet to choose, offer to install a skill for checking starter updates on request. Record `starter.update_review` as `enabled` or `declined`. If enabled, use `python3 .agents/skills/setup/scripts/workspace.py enable-updates` to install it. Preserve its edits and review history. Follow [skill discovery](references/discovery.md) when configuring a new copy or checking discovery in a fresh session.
4. **Checkpoint and continue.** Checkpoint reviewed setup files under the approved Git policy and report any pending backup. Once the local vault is usable, use [Brainstorm](../brainstorm/SKILL.md) for the first proposal if it is absent. On resumption, report the existing proposal and handle pending checks. If backup was approved after the proposal was saved, validate and checkpoint the existing note. Retry an unpushed commit without restaging it.
