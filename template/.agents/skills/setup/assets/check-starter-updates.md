---
name: check-starter-updates
description: Review upstream Workspace Starter changes only when the operator explicitly asks to check for starter updates. Compare the starter baseline and review checkpoint with later upstream changes and propose relevant workspace adaptations.
---

# Review starter improvements

Run only when the operator explicitly asks to check starter updates and `starter.update_review` is `enabled` in `90 System Development/workflow-settings.json`. Read the workspace's [AGENTS.md](../../../AGENTS.md) and [development workflow](../system-development/SKILL.md).

1. Read `starter.url`, `original_commit`, any original tag, and `last_reviewed_commit` if present. Inspect the configured starter source in a disposable checkout outside the vault. Use the requested release, or identify the published release or source revision with the operator. Resolve it to a commit. Inspect the original baseline and compare changes since the last reviewed commit (or the baseline on the first review). If history is missing, rewritten or divergent, report it and resolve the intended comparison before advancing the checkpoint. Treat upstream files as reference material.
2. Read the current vault instructions, workflows and decisions related to the upstream changes. Explain what could help here, what this workspace already provides, and where upstream conflicts with chosen local behavior. Propose the smallest useful adaptations, keeping local paths, schemas and deliberate customizations intact. Avoid copying or merging the template into the workspace.
3. Record the reviewed range, conclusions, and any adoption decisions in a development journal or linked owning record. Ask for agreement before saving an assistant-proposed improvement and use the separate implementation approval in system development. A completed review can record that an adoption decision is still pending.
4. After completing the review and retaining its record, set `starter.last_reviewed_commit` to the exact reviewed commit. Set `starter.last_reviewed_tag` when applicable and clear a stale tag when the new reviewed commit has none. Preserve the original source and baseline. Checkpoint the reviewed settings and record under the vault's approved policy. The review checkpoint tracks consideration of upstream changes.
