# Media setup

Reuse the existing choice or recommend a folder on a Google Shared Drive so media has a shared online copy. Offer an external local folder and the option to decide later. Verify access on each computer.

- **Google Shared Drive (recommended)** — Use the available Drive connection to verify the account, folder metadata, membership in the selected Shared Drive, and access to list its contents. Store `kind: google-shared-drive`, the drive ID, folder ID, and folder URL in the [portable settings](settings-and-backup.md). Record verified access or the blocker in ignored local settings. Missing credentials, inaccessible folders, and personal My Drive folders leave media pending.
- **Local folder** — Confirm a folder outside the vault. Store `"media": {"kind": "local"}` in workflow settings. From the vault root, run `python3 .agents/skills/setup/scripts/workspace.py local-media --folder "<confirmed local folder>"` to verify listing access and record the result and path in ignored local settings. Omit `--folder` to recheck an existing path.

Continue text work while media access is pending.
