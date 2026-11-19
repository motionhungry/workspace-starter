# Skill discovery

On a new workspace copy, run `python3 .agents/skills/setup/scripts/workspace.py discovery` from the vault root to set up Claude Code's local discovery link. Preserve existing Claude files, links, and folders.

Verify discovery the next time the operator naturally opens a fresh session from the vault. Check that project instructions and the expected skills are available. Record the assistant, surface, version if available, and observed result under `discovery` in ignored `.agents/local.json`. Keep an unobserved check pending and continue setup.

If Claude Code cannot discover skills through the whole-directory link, try `discovery --per-skill` and recheck on the next fresh session. Use the vault README for `CLAUDE.md` recovery when project instructions fail to load. If a skill is unavailable in the current session, use its `SKILL.md` by path.
