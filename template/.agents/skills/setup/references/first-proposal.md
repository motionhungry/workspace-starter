# First workspace proposal

From the vault root, run `python3 .agents/skills/system-development/scripts/records.py first`. Reuse the returned proposal, even if it is archived. Exit 1 means it is absent. Resolve exit 2 before creating one.

If the proposal is absent, start with one open question: “What do you want to use this workspace for?” Invite the operator to describe what they do today, what they want to make easier, or what a useful outcome would look like. Reuse any purpose they have already shared and clarify only gaps that matter. Wait until you understand the purpose before asking about a first capability.

Pass the purpose and relevant examples or constraints to [System Development](../../system-development/SKILL.md) to shape and capture the first improvement. Use the conversation and the approved proposal to carry that context forward.

When the operator approves the first proposal and authorizes saving it, fill the [improvement template](../../system-development/assets/improvement.md) in a temporary draft outside the workspace. Use `DEV-0001`, `open` status, the actual local dates, and the user's authorization to save. From the vault root, run:

```sh
python3 .agents/skills/system-development/scripts/records.py save-first --draft "<draft-path>"
```

The helper validates the draft and saves it without replacing an existing proposal. Read the saved note and return its workspace-relative path. Checkpoint it under the approved backup policy. If backup is pending, preserve the proposal and report its actual backup status.
