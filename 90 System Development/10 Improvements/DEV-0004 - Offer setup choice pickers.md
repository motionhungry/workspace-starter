---
id: DEV-0004
type: improvement
status: validating
created: 2026-11-20
updated: 2026-11-20
---
# Offer setup choice pickers

## Problem and evidence

The operator wants simple setup choices to be selectable when the assistant's client provides a picker.

## Outcome and proposed change

Prefer the session's built-in choice picker for two or three clear options. Offer the same choices in a numbered list when a picker is unavailable. Keep backup destination and policy confirmation as a separate step.

## Acceptance criteria

- Setup presents one question with the recommended option first and offers deferral when supported.
- Setup can collect the same answer using a picker or a numbered list.
- The selected backup route does not substitute for confirmation of the destination and policy.

## Approval

The operator approved adding picker guidance to the starter setup skill.

## Validation

The integration suite passed on a generated workspace. The setup skill keeps both presentation paths and explicit backup confirmation.

## Next step

Observe an interactive setup choice in a picker-capable session and the equivalent numbered-list turn in a session without a picker.
