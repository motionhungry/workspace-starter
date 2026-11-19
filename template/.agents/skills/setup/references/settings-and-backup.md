# Settings and Git backup

## Portable choices

`90 System Development/workflow-settings.json` is tracked. Bootstrap creates `schema_version: 1` and the `starter` object with `url`, `original_commit`, and `original_tag` if the exact source commit has a tag. Preserve that baseline. When chosen, add `starter.update_review` (`enabled` or `declined`). The update-review skill records `starter.last_reviewed_commit` after a completed review and `starter.last_reviewed_tag` when applicable.

Add top-level objects when the operator confirms their choices. Keep unrelated keys intact.

```json
{
  "backup": {
    "url": "https://github.com/OWNER/WORKSPACE.git",
    "remote": "origin",
    "branch": "main",
    "policy": "commit-and-push"
  },
  "media": {
    "kind": "google-shared-drive",
    "drive_id": "DRIVE_ID",
    "folder_id": "FOLDER_ID",
    "folder_url": "https://drive.google.com/drive/folders/FOLDER_ID"
  }
}
```

For machine-local media, store just `"media": {"kind": "local"}` in the shared document. In ignored `.agents/local.json`, keep `media_path` for local media, `media_access` (`verified` or `pending`), and `obsidian_access` (`verified` or `pending`). For pending checks, optionally add short `media_pending_reason` and `obsidian_pending_reason` fields. Record fresh-session observations under `discovery` keyed by assistant and surface. Update per-computer evidence after verification. Keep credentials in the system credential manager or available connector.

## First backup

Confirm the workspace repository URL, remote name (usually `origin`), branch, and whether the operator wants `commit-and-push` checkpoints. Confirm that the remotely hosted repository is intended for the content that will be saved, including its visibility. Prefer a private, empty repository for a new personal workspace. The operator can create one or explicitly authorize creation. Keep the starter remote and workspace backup distinct, including HTTPS and SSH forms of the same repository.

Use `git init -b <branch>` for a new vault and configure repository-local identity. Add the approved remote with `git remote add <remote> <url>` only if absent. Inspect an existing matching remote and use it. If it differs from the approved choice, stop and reconcile it with the operator before modifying it or pushing. Inspect both fetch and push URLs. Use the repository's normal SSH or HTTPS authentication, and use `git ls-remote <remote>` to check connectivity. An empty result with exit 0 is expected from an empty remote. For a new computer, use the workspace's existing history and verify that the effective URLs match the approved settings.

## Review and checkpoint

Run `git status --short --branch`. Inspect the content and diffs, including new files. Verify scope, validation results, paths, and private data. Pass explicit, vault-relative files after `--`. For the initial setup checkpoint include reviewed vault scaffold, skills, templates, settings and any other approved portable setup files. Keep unrelated staged changes out of the checkpoint.

```sh
python3 .agents/skills/setup/scripts/workspace.py checkpoint --message 'Save workspace setup' -- AGENTS.md README.md '90 System Development/workflow-settings.json' # include remaining reviewed paths
```

At proposal save and useful stopping points, repeat with the files for that change. The helper makes a scoped commit and pushes the current commit to the approved branch using a normal push, then independently checks the advertised branch commit. With the policy confirmed, if authentication or the push fails after a commit, keep that commit and report backup pending. At the next checkpoint retry with no arguments after `checkpoint` when the commit is already saved. If the remote has diverged, inspect and resolve it with the operator before retrying. Preserve both histories and avoid force pushes.
