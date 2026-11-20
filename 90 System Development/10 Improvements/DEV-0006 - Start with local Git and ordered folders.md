---
id: DEV-0006
type: improvement
status: validating
created: 2026-11-20
updated: 2026-11-20
---
# Start with local Git and ordered folders

## Problem and evidence

The operator reported from actual workspace setup that local history should begin immediately and folder names should show the order of work. The checkpoint helper required approved backup settings before committing, and the numbered template folders lacked a general convention for additions.

## Outcome and boundaries

Fresh vaults start with their own Git history. Existing paths and history are preserved. Backup remains optional. New workflow folders reflect the workspace purpose and follow a convention at every level.

## Proposed change

Initialize and commit the generated scaffold during bootstrap. Make checkpointing work locally and push only when approved. Document folder ordering in the vault instructions and setup handoff. See [[ADR-0003 - Default to local Git and order folders by workflow]].

## Acceptance criteria

- A fresh vault has one independent baseline commit and no remote. Bootstrap uses the configured identity or asks for an identity to use in the new vault.
- Scoped setup and proposal commits succeed without a remote. Approved backup can later transfer the local history and recover the proposal.
- The generated vault documents the convention and shows two-digit workflow order at both levels. Existing paths stay intact.

## Approval

On November 20, 2026, the operator agreed to the recommended details and explicitly approved saving and implementing them.

## Validation

Five integration tests passed on macOS 26.7 with Git 2.50.1 and Python 3.14.2. Generated fixtures covered configured and explicitly supplied identities, missing identity with an untouched destination, an independent baseline and scoped setup and proposal commits with no remote, later backup and recovery after a failed push, and rejection of starter URLs. The fixture checked the folder guidance and preserved numbered template paths. Development records and whitespace checks passed.

## Next step

Confirm the identity prompt and purpose-driven folder planning in a live assistant setup. Linux and hosted backup were not exercised for this change.
