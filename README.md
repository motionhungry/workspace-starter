# Workspace Starter

An Obsidian vault for building and improving your workflows with an assistant. Each generated workspace has its own Git history and backup.

## Start or resume a workspace

Use macOS or Linux with Git 2.28+, Python 3.9+, Obsidian, and an assistant session that can read and write local files and run local commands. Open your assistant in the intended parent folder or in an existing workspace. Paste the same prompt for Claude or ChatGPT.

> Help me start or resume a Workspace Starter vault. First verify that you can run Git and Python 3 locally and read the intended folder. Inspect the current directory and its Git state for an existing workspace. Confirm the destination with me before writing. If this is an existing workspace, use it in place. On a new computer, clone my existing workspace from the backup repository I confirm.
>
> For a new workspace only, use a trusted checkout of https://github.com/motionhungry/workspace-starter in a temporary directory. Check out the release tag I specify, or use the checkout's default HEAD. Run `python3 <starter-checkout>/template/.agents/skills/setup/scripts/workspace.py bootstrap --source <starter-checkout> --destination <confirmed-folder>` with the actual quoted paths. This copies the committed template and records its provenance. Use my workspace's own repository for backup.
>
> In the workspace, read `AGENTS.md` and `.agents/skills/setup/SKILL.md` by path. Follow the setup skill for prerequisite checks, Obsidian, Git, optional media and update review, and the first improvement proposal. Inspect what already exists and preserve my work. Ask me for missing choices and actions that require my account or approval.

For ChatGPT, use a local session and verify file and command access. Codex documents repository-local skill discovery. If a ChatGPT Work session can access the files and run commands but does not discover skills, use their explicit paths. [ChatGPT Work](https://learn.chatgpt.com/docs/get-started-with-work) · [Codex skill discovery](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)

Development and release checks live in the [v1 improvement record](90%20System%20Development/10%20Improvements/IMP-0001.md). See [MIT](LICENSE.txt) for the license.
