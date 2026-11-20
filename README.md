# Workspace Starter

An Obsidian starter workspace for building and improving your workflows with AI. Each workspace keeps its own change history and backup.

## Getting started

1. **Make a folder for your workspace.** Choose what it’s for and give it a name (e.g. `marketing-workspace`, `finance-workspace`, `sysadmin-workspace`). Use a dedicated empty folder for a new workspace.
2. **Open the folder in your AI app.** Create a new local project and select that folder. If your app opens folders directly, open the folder as your workspace.
3. **Paste the prompt below into a new chat.** Your assistant will check what’s needed, help you open the folder in Obsidian, and guide you through setting up a backup and planning your first improvement.

Workspace Starter is designed for macOS and Linux. To resume setup, open your existing workspace folder and paste the same prompt.

```text
Help me start or resume a Workspace Starter vault. Confirm that you can access this folder and run local commands with Git 2.28+ and Python 3.9+. Check for an existing workspace and confirm the destination with me before writing. Resume an existing workspace in place. If I’m moving to a new computer, use the existing backup repository I confirm.

For a new workspace, check out https://github.com/motionhungry/workspace-starter in a temporary folder. Use the release tag I specify or the checkout’s default HEAD. Run the helper at template/.agents/skills/setup/scripts/workspace.py with bootstrap --source <starter-checkout> --destination <confirmed-folder>, using the actual quoted paths. Keep my workspace backup separate from the starter repository.

Continue from my workspace folder. Read and follow AGENTS.md, then follow .agents/skills/setup/SKILL.md. Preserve existing work and ask me for any choices, sign-ins, or approvals that need my input.
```

## License

[MIT](LICENSE.txt)
