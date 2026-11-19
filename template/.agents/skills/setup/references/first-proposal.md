# First workspace proposal

From the vault root, run `python3 .agents/skills/system-development/scripts/records.py first`. Reuse the returned proposal, even if it is archived. Exit 1 means it is absent. Resolve exit 2 before creating one.

When Brainstorm has produced an approved proposal, fill the [improvement template](../../system-development/assets/improvement.md) in a temporary draft outside the workspace. Use `DEV-0001`, `open` status, the actual local dates, and the user's authorization to save. From the vault root, run:

```sh
python3 .agents/skills/system-development/scripts/records.py save-first --draft "<draft-path>"
```

The helper validates the draft and saves it without replacing an existing proposal. Read the saved note and return its workspace-relative path. Checkpoint it under the approved backup policy. If backup is pending, preserve the proposal and report its actual backup status.
