---
id: ADR-0002
type: decision
status: accepted
created: 2026-11-20
updated: 2026-11-20
---
# Recommend Shared Drive for workspace media

## Context

The setup pilot requested that Google Shared Drive be recommended so the workspace has online copies there. Setup has separate choices for external media and Git-backed vault history.

## Choice and alternatives

Recommend a folder on a Google Shared Drive for external media. Keep the external local folder available for operators who need local storage. Operators can defer the media choice. Retain the Git workflow for vault history and restore.

## Consequences and revisit condition

Shared Drive media is available online to authorized members. Each computer still needs verified access. Revisit the recommendation if Shared Drive access consistently blocks the pilot or the operator needs the vault itself copied to Drive.

## Approval and related records

The operator requested the Shared Drive recommendation in pilot feedback on 2026-11-20. The media scope follows the current setup choice. See [[DEV-0005 - Start setup with workspace purpose]].
