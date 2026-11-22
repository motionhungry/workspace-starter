---
id: ADR-0004
type: decision
status: accepted
created: 2026-11-22
updated: 2026-11-22
---
# Keep workspace handoffs in the calling workflow

## Context

Brainstorm supports both standalone decisions and interviews that inform workspace proposals. Setup and System Development already know the context and where the decisions belong.

## Choice and alternatives

Brainstorm owns the interview and its summary. The workflow that starts the interview supplies the context and decides how to present, confirm, and record the outcome. Keeping the workspace handoffs in Brainstorm would make it easy to offer a proposal from a standalone interview, but it would tie a reusable interview to the starter’s record conventions and repeat rules in both skills.

## Consequences and revisit condition

Workspace proposal rules have one owner. A standalone interview can finish in chat. The user can ask System Development to pick up the outcome as a proposal. Revisit the handoff if live use shows that operators routinely lose the transition from discussion to a saved improvement.

## Approval and related records

The operator requested implementation of this division on 2026-11-22. See [[DEV-0009 - Make Brainstorm reusable on its own]].
