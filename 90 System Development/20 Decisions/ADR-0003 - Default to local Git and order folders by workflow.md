---
id: ADR-0003
type: decision
status: accepted
created: 2026-11-20
updated: 2026-11-20
---
# Default to local Git and order folders by workflow

## Context

Pilot feedback called for dependable local history and predictable folder order at each level.

## Choice and alternatives

Create a baseline commit when the operator starts fresh and commit reviewed work as it progresses. Deferring the first commit until setup review would combine the original scaffold with setup changes. Keep remote backup optional.

Retain the two starter areas and derive additional folders from the workspace purpose. A fixed set of workflow folders would make vaults more uniform but assumes a shared workflow. Use two-digit prefixes in steps of ten within each parent so folder sorting follows the workflow.

## Consequences and revisit condition

Bootstrap needs a Git author identity. Operators can provide a repository-local identity when one is missing. Existing folder paths and history are preserved. Revisit the defaults if pilots identify a common missing area or workflows outgrow the numbering scheme.

## Approval and related records

The operator approved both choices and implementation on November 20, 2026. See [[DEV-0006 - Start with local Git and ordered folders]].
