---
name: setup
description: Set up Workspace Starter, resume interrupted setup, or open an existing Workspace Starter vault on a new computer. Verify local tools and Obsidian, configure the approved Git backup, handle media and update preferences, and help save the first improvement proposal.
---

# Set up or resume the workspace

Read the workspace's [AGENTS.md](../../../AGENTS.md) and [settings and Git instructions](references/settings-and-backup.md). Work from the vault root. Use existing state first, then ask only for unresolved choices. Use the operator's local date when saving records.

## 1. Inspect this copy

1. Verify that this assistant can read workspace files and run commands here. Check Git 2.28+ and Python 3.9+. Confirm the folder and read `90 System Development/workflow-settings.json`, ignored `.agents/local.json` if present, and `git status --short --branch` when a repository exists. If provenance is missing, investigate before editing. Preserve current work, and use one active writer across copies.
2. Check whether the first proposal already exists with `python3 .agents/skills/system-development/scripts/records.py first`. A path means there is already a first improvement. Exit 1 means absent and exit 2 calls for resolving invalid or ambiguous records. Use the existing record on resumption, including after it has been archived.
3. For a fresh template, initialize Git in the vault only after confirming the chosen branch and checking `git rev-parse --show-toplevel` does not identify another repository. For a new computer, use the existing clone and history. For either path check the repository-local `user.name` and `user.email`. Confirm values with the operator before adding or changing them through `git config --local`.
4. In Obsidian, select **Open folder as vault** and choose the workspace root. Use the app when available or ask the operator to confirm it opens and shows the inbox and System Development. Reopen it to verify setup, and record the observation for this computer. Treat an installed application or an `.obsidian` directory as evidence of presence only.
5. Run `python3 .agents/skills/setup/scripts/workspace.py discovery` for Claude Code discovery. Restart or use a fresh session to check that it loads `AGENTS.md` and lists the workspace skills. If the whole-directory link does not work, use `discovery --per-skill` to switch the managed link to individual links, then retest. Preserve existing Claude files, links and folders. Use the vault README for the `CLAUDE.md` recovery. In ChatGPT, check for repo-local discovery in a fresh session. If missing, read skills by path. Record the actual surface, version when available, and what was verified.

## 2. Establish backup

Confirm the independent destination, branch, and checkpoint policy as described in [settings and Git](references/settings-and-backup.md). Set the approved remote and check authentication. If the remote already contains workspace history and this is a fresh copy, inspect before proceeding. An existing workspace should be cloned and resumed from its history. Use a normal push and verify the remote commit.

If credentials or the backup choice are pending, record the blocker and continue the first proposal once the vault is locally usable. After backup is approved, the checkpoint can save local work even when push access is temporarily unavailable. Backup is complete once the remote contains the checkpoint.

## 3. Confirm media and update review

- Reuse the existing media choice. If undecided, ask the operator to choose an existing local folder outside the vault or a folder on a Google Shared Drive. After confirming local media, record the portable choice and run `python3 .agents/skills/setup/scripts/workspace.py local-media --folder "<confirmed local folder>"`. This verifies listing access and saves the path and result in ignored local settings. Omit `--folder` to recheck an existing local path. Confirm a path independently on each computer.
- For Google Shared Drive, verify the selected account and destination using the available Drive connection. Inspect the folder's metadata, confirm it belongs to the selected Shared Drive and verify that its contents can be listed. Store the drive ID, folder ID, and folder URL in workflow settings. On another computer, verify access with that session's connection. Record actual access or the blocker in local settings. Treat missing credentials, lack of directory access, or a personal My Drive folder as pending media. Continue independent text work.
- Offer the operator a skill they can invoke explicitly to review future starter improvements. Save `starter.update_review` as `enabled` or `declined` when chosen. If enabled, run `python3 .agents/skills/setup/scripts/workspace.py enable-updates`. Preserve existing settings, skill edits, and review history. When declined during first setup, leave the skill absent. Never run update review automatically. Keep an unanswered choice pending.

Once the setup files are ready, validate the local vault and review the explicit portable files for the setup checkpoint. Checkpoint using the approved policy when available. Report failed pushes as pending backup.

## 4. Brainstorm and save the first proposal

If a first record does not already exist and the local vault is usable, follow [brainstorm](../brainstorm/SKILL.md) in first-proposal mode. Work through the system's purpose, desired outcome, boundaries and first useful capability. Preview the full proposal, ask for one confirmation to approve the content and save it, and follow the development record template. Provide the saved path and checkpoint it if the backup policy is approved. Ask for separate approval before implementation.

On a rerun, report existing proposal and setup evidence, then address any pending checks. If the proposal was saved before the backup policy was approved, review and validate that existing note and checkpoint it when the policy is approved. If the commit is already saved, retry backup without restaging the work.
