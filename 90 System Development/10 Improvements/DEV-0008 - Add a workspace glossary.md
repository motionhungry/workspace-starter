---
id: DEV-0008
type: improvement
status: validating
created: 2026-11-20
updated: 2026-11-20
---
# Add a workspace glossary

## Problem and evidence

The starter calls `DEV-` notes tickets, proposals, and working specs at different points in their lifecycle. An operator and agent need a shared name for the record type, and generated vaults need a place to record their own terms when the meaning matters in future work.

## Outcome and boundaries

Ship one root glossary entry for *workspace improvement*, the `DEV-####` record type. Keep System Development as the folder name and use *improvement proposal* for the initial proposal. Record fields, statuses, and the reserved setup ID stay in the record conventions. The glossary can grow through explicit requests and approved suggestions during normal work.

## Proposed change

Add `template/GLOSSARY.md` and link it from the vault and System Development instructions. Base the format on the concise entries and ongoing terminology work in [Matt Pocock's glossary](https://github.com/mattpocock/skills/blob/main/GLOSSARY.md) and [domain modeling skill](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md).

## Acceptance criteria

- A generated vault has one root glossary entry. The vault and System Development instructions link to it.
- The entry defines the `DEV-####` record type across its lifecycle. System Development still owns record mechanics, including the role of `DEV-0001` in setup.
- The agent adds terms at the operator's request or with approval when a definition would prevent a specific future misunderstanding. It revises existing entries when meanings change and looks up definitions that are already documented.

## Approval

On 2026-11-20, the operator confirmed the one-entry glossary and explicitly approved saving the proposal and implementing it.

## Validation

All five integration tests and maintainer record validation passed on macOS 26.7 with Apple Git 2.50.1 and Python 3.14.2. A fresh fixture built with the setup command contained one glossary entry and both instruction links resolved to it. The fixture retained the approval and update guidance, left the reserved first proposal available for setup, and had a clean Git checkout.

## Next step

In a live assistant session in a new vault, ask what a `DEV-` record is, then check whether the assistant offers to save a useful local term and waits for approval. Live assistant behavior and other platforms are pending.
