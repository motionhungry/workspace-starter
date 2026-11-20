# Workspace tooling

- `references/` holds durable agent guidance shared across the vault. Link each reference from the instructions or workflow that needs it and say when to read it.
- `skills/` is the editable source for workspace skills. A skill can own necessary scripts, references, and assets in its directory.
- `local.json` stores ignored per-computer setup observations and paths.

Keep guidance used by one skill in that skill’s `references/`. Keep source material that people use in the visible area that owns it. Record the rationale, approval, and validation in the owning improvement.

Claude discovery links live under the ignored `.claude/` directory. Put human-readable development work and evidence in the visible system-development area. Use disposable external temporary directories for test output. Add tooling only when an agreed workflow needs it.
