---
id: ADR-0001
type: decision
status: accepted
created: 2026-11-20
updated: 2026-11-20
---
# Keep conversation voice in each vault

## Context

Each operator should be able to tune the assistant's chat voice within a generated vault. Documents and messages will continue to use the voice and conventions appropriate to their author and audience.

## Choice and alternatives

Keep the voice guidance in `.agents/references/voice.md` and reference it from the generated `AGENTS.md`. A visible vault note would be editable inside Obsidian. The tooling directory keeps agent guidance together. Client-specific prompt configuration could load the guidance before the first message and would require separate setup for each client.

## Consequences and revisit condition

Each vault owns its copy and can tune it with a text editor or through the assistant. The agent may send an initial progress message before it reads the file. Revisit client-specific prompt configuration if that first message matters in practice or fresh sessions regularly skip the file.

## Approval and related records

The operator approved the vault-local file and startup instruction as the first trial and clarified that new vaults should inherit it from the starter. Implementation and validation are tracked in [[DEV-0003 - Add a conversation voice to new vaults]].
