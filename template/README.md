# Your workspace

Open this folder as a vault in Obsidian. Put uncategorized notes in `00 Inbox/` and use [System Development](90%20System%20Development/README.md) to propose and develop new capabilities.

To resume setup or open this workspace on another computer, use the [Workspace Starter prompt](https://github.com/motionhungry/workspace-starter#getting-started). If the folder is already open in your assistant, ask it to resume workspace setup.

Edit `.agents/references/voice.md` to change how your assistant speaks with you in this vault. You can edit it in a text editor or ask your assistant to update it.

## Folder order

Keep `00 Inbox/` for uncategorized notes and `90 System Development/` for workspace improvements. Add other workflow folders when the workspace purpose calls for them.

Give new workflow folders a two-digit prefix followed by a space and a descriptive name. Assign prefixes in steps of ten in the order people use the folders. Start the sequence again inside each parent. For example, a workspace that publishes articles could use `10 Publishing/10 Drafts/`, `10 Publishing/20 Review/`, and `10 Publishing/30 Published/`. Preserve existing folder paths unless a migration is agreed.

## Claude Code recovery

From the workspace root, check `/memory` in a fresh session for `AGENTS.md`, and look for the workspace skills in the command menu. Older or differently configured versions may need a local `CLAUDE.md`. After checking that the path is unused, run `ln -s AGENTS.md CLAUDE.md` in the workspace root and reopen Claude Code. Preserve an existing file and review it with the operator before changing it. If a link cannot load, read `AGENTS.md` and the skill by path.

[Claude Code project instructions](https://code.claude.com/docs/en/memory#agentsmd) · [Claude Code skills](https://code.claude.com/docs/en/skills#choose-where-skills-load)
