---
id: DEV-0005
type: improvement
status: validating
created: 2026-11-20
updated: 2026-11-20
---
# Start setup with workspace purpose

## Problem and evidence

In actual setup use, the operator reported that the flow had improved and asked for a Google Shared Drive recommendation, a purpose question before choosing the first task, and guidance on how to participate in Brainstorm as an interview.

## Outcome and boundaries

Recommend Google Shared Drive for external media so it has a shared online copy. Keep vault history and restore on the existing Git path. Use the operator's purpose to guide the first System Development improvement. Link the setup pilot follow-up to [[DEV-0004 - Offer setup choice pickers]].

## Acceptance criteria

- Setup recommends Google Shared Drive first when media is undecided, offers local storage or deferral, and preserves existing selections.
- Setup asks what the workspace is for before discussing the first capability, reuses purpose already given, and passes it to System Development.
- Before the first Brainstorm round, invite the operator to talk through ideas in their own words, share examples and corrections, and answer multiple questions together.
- System Development previews one proposal with the workspace purpose, seeks approval to save, and preserves separate approval for implementation. A resumed workspace with a first proposal reuses it.

## Approval

The operator requested the three setup changes on 2026-11-20 based on actual use. The Shared Drive recommendation applies to the existing media choice.

## Validation

All four integration tests and development record validation passed. A separate generated fixture check confirmed the media choice order, purpose question and skill handoff paths, free-form interview guidance, and separate implementation approval. The integration suite also checked recovering a saved first proposal and retrying Git backup.

The updated conversation, live skill discovery, and Google Shared Drive access still need observation in the pilot.

## Next step

Exercise the updated conversation in a live pilot, including Shared Drive access and an interrupted first interview.
