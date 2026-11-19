# Your workspace

Open this folder as a vault in Obsidian. Put uncategorized notes in `00 Inbox/` and use [System Development](90%20System%20Development/README.md) to propose and develop new capabilities.

To resume setup or open this workspace on another computer, use the [Workspace Starter prompt](https://github.com/motionhungry/workspace-starter#getting-started). If the folder is already open in your assistant, ask it to resume workspace setup.

## Claude Code recovery

From the workspace root, check `/memory` in a fresh session for `AGENTS.md`, and look for the workspace skills in the command menu. Older or differently configured versions may need a local `CLAUDE.md`. After checking that the path is unused, run `ln -s AGENTS.md CLAUDE.md` in the workspace root and reopen Claude Code. Preserve an existing file and review it with the operator before changing it. If a link cannot load, read `AGENTS.md` and the skill by path.

[Claude Code project instructions](https://code.claude.com/docs/en/memory#agentsmd) · [Claude Code skills](https://code.claude.com/docs/en/skills#choose-where-skills-load)
