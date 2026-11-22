---
id: DEV-0009
type: improvement
status: validating
created: 2026-11-22
updated: 2026-11-22
---
# Make Brainstorm reusable on its own

## Problem and evidence

The revised Brainstorm interview can serve general planning, but its closing instructions still name setup and development records. Those workflows already call Brainstorm and can supply the context, confirmation, and recording steps they need. The interview also assumes subagents are available and asks for every branch to be visited, even when the user has deferred a decision.

## Outcome and boundaries

Keep the revised question rounds and recommendations. Make Brainstorm portable and keep workspace proposals and records in System Development. Keep the existing Setup and Skill Creator entry points. See [[ADR-0004 - Keep workspace handoffs in the calling workflow]].

## Proposed change

Define a generic interview close, allow direct fact-finding, and let calling workflows supply the context and present the confirmation. Put the rules for first proposals, existing improvements, and new proposals in System Development. Route explicit capture requests directly to capture.

## Acceptance criteria

- A standalone interview can use the skill by itself, look up facts without subagents, and close in chat with confirmed decisions and explicitly deferred questions.
- Setup passes the workspace purpose to System Development. The first proposal preview confirms the brainstorm and authorizes saving in one step. Implementation requires separate approval.
- System Development starts an existing improvement interview with the ticket and relevant decisions and records its confirmed scope, acceptance criteria, and deferred questions there.
- An explicit capture request goes straight to capture. A user who wants to save the outcome of a standalone brainstorm can start a new proposal from the agreed summary.

## Approval

On 2026-11-22 the operator requested implementation of the reviewed changes through System Development.

## Validation

All five integration tests passed on macOS 26.7 with Git 2.50.1 and Python 3.14.2. A generated vault contained the revised skills, resolved the Setup and Skill Creator links, and resolved both Claude discovery adapters to the canonical skills. Maintainer record validation passed.

In read-only Codex CLI 0.167.2 trials, a skill-only workspace looked up a local fact directly, retained deferred questions, and asked for confirmation in chat. A generated vault used the workspace purpose to open the first Brainstorm round. A separate setup trial previewed one proposal with a combined confirmation and separate implementation approval. A new-proposal trial reused a standalone brainstorm and requested permission to save. The generated vault stayed clean.

Reviewed the explicit capture path and existing-improvement handoff against the acceptance criteria. Live writes through those paths, a complete interactive setup session, and Claude Code invocation remain unverified.

## Next step

Observe the remaining handoffs in the next workspace pilot and record the results.
