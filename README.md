# Workspace Starter

An Obsidian starter workspace for building and improving your workflows with AI. Each workspace starts with its own local Git history and can add a private backup.

## Getting started

1. **Make a folder for your workspace.** Choose what it’s for and give it a name (e.g. `marketing-workspace`, `finance-workspace`, `sysadmin-workspace`). Use a dedicated empty folder for a new workspace.
2. **Open the folder in your AI app.** Create a new local project and select that folder. If your app opens folders directly, open the folder as your workspace.
3. **Paste the prompt below into a new chat.** Your assistant will check what’s needed, help you open the folder in Obsidian, and guide you through optional backup and planning your first improvement.

Workspace Starter is designed for macOS and Linux. To resume setup, open your existing workspace folder and paste the same prompt.

```text
Help me start or resume a Workspace Starter vault. Check that you can access this folder and run local commands with Git 2.28+ and Python 3.9+. Check for an existing workspace and confirm the destination with me before writing. Resume an existing workspace in place. If I’m moving to a new computer, use the existing backup repository I confirm.

When the selected folder is empty and ready, ask “How would you like to set up ‘<folder name>’?” Use the actual folder name. Offer one choice question with these options in order:

1. Start fresh (recommended)
2. Restore from a backup
3. Change folder

Use the built-in choice picker only if it can show the options to me and receive my selection in this session. Otherwise show the numbered choices and say “Reply 1, 2, or 3.” Accept the option names or an equivalent plain-language reply. Start fresh confirms the named folder for a new workspace. Restore from a backup confirms the named folder and prompts for the backup repository URL if I haven’t already provided it. Confirm the URL with me before writing. If I choose Change folder, ask which folder to use and check it before offering the applicable setup choices. Keep the ready-folder reply to the question, choices, and how to answer. Report preflight checks only if a check blocks setup. Explain the next step after I choose. If a check prevents setup, explain what I need to do in plain language.

For a new workspace, check out https://github.com/motionhungry/workspace-starter in a temporary folder. Use the release tag I specify or the checkout’s default HEAD. Run the helper at template/.agents/skills/setup/scripts/workspace.py with bootstrap --source <starter-checkout> --destination <confirmed-folder>, using the actual quoted paths. Bootstrap initializes the vault on `main` and saves the starter files as the first local commit. If Git needs an author identity, ask for my preferred commit name and email and retry with `--author-name` and `--author-email`. These choices apply to this vault. Keep my workspace backup separate from the starter repository.

Continue from my workspace folder. Read and follow AGENTS.md, then follow .agents/skills/setup/SKILL.md. Preserve existing work and ask me for any choices, sign-ins, or approvals that need my input.
```

## License

[MIT](LICENSE.txt)
