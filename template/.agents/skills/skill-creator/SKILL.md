---
name: skill-creator
description: Design, create or update a reusable skill for the current workspace when the user wants a repeatable local capability. Use with the system-development workflow and its approval boundaries.
---

# Workspace Skill Creator

1. Read the development record conventions, the owning improvement and related skills. Update the matching skill when one already owns the capability. If the request is still an idea, use [brainstorm](../brainstorm/SKILL.md) and [system development](../system-development/SKILL.md) to agree on the trigger, inputs, required output, side effects, permissions and acceptance criteria.
2. After implementation is authorized, create or update `.agents/skills/<skill-name>/SKILL.md` in this workspace. Use a lowercase hyphenated name matching the folder, no more than 64 characters. Begin with YAML frontmatter containing `name` and a `description` that states what the skill does and when it should activate. Describe the workflow in the body. Put needed scripts, references and assets inside its skill directory. Add only files the workflow uses. Maintain one editable definition.
3. Check the Claude discovery adapter. With `.claude/skills` linked to the canonical skill directory, additions are available through that link. For a configured per-skill adapter, run `python3 .agents/skills/setup/scripts/workspace.py discovery --per-skill` from the workspace root. Inspect conflicts and preserve existing discovery entries. In a maintainer checkout, apply its local discovery procedure with the same canonical skill source.
4. Check metadata, trigger and near-miss requests, permissions, output, and any applicable record validation. Verify discovery and representative use in a fresh session of the intended assistant whenever available. Record actual environments, evidence and remaining checks in the owning improvement. Follow the workspace's checkpoint policy after validation.

For ordinary skills, use the shared folder in the current workspace. If the requested capability is a custom subagent, route it through the scoped agent-creator improvement in system development.
