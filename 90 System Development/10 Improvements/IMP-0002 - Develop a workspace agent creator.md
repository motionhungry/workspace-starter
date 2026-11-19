---
id: IMP-0002
type: improvement
status: open
created: 2026-11-19
updated: 2026-11-19
---
# Develop a workspace agent creator

## Problem and evidence

Some workspace tasks have a repeatable, independently delegable job and benefit from an assistant with a distinct perspective, tool set, or reasoning depth. The v1 development workflow can identify these tasks during improvement design.

## Outcome and boundaries

Help an operator design and test a custom agent for one clear workspace job. Start with an independent reviewer. Learn from the Claude and ChatGPT configurations before specifying any shared agent format.

## Proposed change

Brainstorm the reviewer's job, inputs, outputs, tool access, and expected depth. For each applicable assistant, explicitly choose or inherit both the model and reasoning effort. Test those choices together on the same representative review task.

## Acceptance criteria

- The reviewer receives clear inputs and returns the agreed output without editing the principal work.
- The chosen or inherited model and reasoning effort are documented and verified together on each applicable surface.
- Findings from the representative review inform whether a shared format would help.

## Approval

The approved v1 design identifies this as the first follow-on improvement. Implementation scope remains to be agreed after brainstorming.

## Next step

After v1 validation, select a real review task and agree the reviewer's expected output with the operator.
