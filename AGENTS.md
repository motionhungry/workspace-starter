# Workspace Starter maintainer instructions

The distributable vault is in `template/`. Keep maintainer records, tests, release procedures, and pilot evidence outside it. Never commit client material, private paths, credentials, or raw session transcripts.

Use the [system-development skill](template/.agents/skills/system-development/SKILL.md) and its record conventions for maintainer work. Store records under the root `90 System Development/`. Apply the policy in this file to the maintainer repository. Files under `template/` describe the generated workspace.

Develop on a branch. At a useful stopping point, review explicit paths and validate the change against its acceptance criteria before committing. Use a pull request for integration into main and a Git tag for the exact release commit. Record observed compatibility and outstanding checks in the owning improvement. Tag and publish only after the release decision.

Keep `template/.agents/` limited to operating instructions and active skill machinery. Preserve user edits and record any schema or workflow changes in the owning improvement.
