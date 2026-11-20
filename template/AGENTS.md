# Workspace operating instructions

Read `.agents/references/voice.md` when you start working in this vault for guidance on speaking with the operator.

Work in this vault. Verify local file and command access before acting. Say what you inspected and flag any access or validation gaps.

At session entry, inspect Git state and existing work. Preserve manual edits, untracked files, and existing configuration. Work with one active writer across copies. Establish where a change belongs and read its existing instructions before editing.

The operator owns purpose, scope, and approval. Ask before saving an assistant-proposed improvement. Agreement to save an improvement grants permission to record it. Get separate approval to implement the agreed scope. Reconfirm material changes during implementation. Finish with the validation evidence, open issues, and the next action in the owning record.

Use `00 Inbox/` for uncategorized captures. Use [System Development](90%20System%20Development/README.md) to evolve the workspace. Apply the [folder naming convention](README.md#folder-order) to new workflow folders at every level. Preserve existing paths unless the operator approves a migration. Follow its templates and validate required frontmatter. Define a project's schema and lifecycle before introducing a project workflow. Keep work-specific media in the selected external store and link to it from notes.

Read the approved Git policy and portable choices in `90 System Development/workflow-settings.json`. Keep per-computer settings in `.agents/local.json`. Review explicit paths and make local commits at setup completion, proposal save, and meaningful stopping points. Push only after the operator approves the backup destination and policy. Confirm the pushed commit against the remote. If backup fails, retain the local commit and report pending backup. See the [Git checkpoint instructions](.agents/skills/setup/references/settings-and-backup.md).

Keep temporary test output outside the vault and retain meaningful evidence in the owning record. See the [tooling layout](.agents/README.md).
