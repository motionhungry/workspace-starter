---
id: DEV-0007
type: improvement
status: validating
created: 2026-11-20
updated: 2026-11-20
---
# Recommend next steps after starter reviews

## Problem and outcome

An update review identified useful adaptations but left both decisions pending without giving the operator a clear next action. The review should recommend a next step based on the release and the current workspace.

## Acceptance criteria

- Lead with the most useful workspace-specific adaptation and its benefit. Briefly summarize other changes that can wait.
- Ask whether to save the recommendation as an improvement proposal. Agreement creates or updates the matching proposal. Share it and ask separately before implementing.
- End with “No action needed” when a completed review finds no adaptation worth pursuing. Explain what is needed when the review is blocked.
- Enabling reviews in a generated vault installs the updated guidance and preserves existing local edits on a repeat enable.

## Approval

On November 20, 2026, the operator agreed to the wording and approval flow and explicitly authorized implementing the skill change.

## Validation and next step

All five integration tests passed on macOS 26.7 with Apple Git 2.50.1 and Python 3.14.2. The generated fixture verified discovery, installation of the exact updated guidance, and preservation of a local skill edit. Check the conversation and approval flow in a live review. Other platforms were not exercised.
