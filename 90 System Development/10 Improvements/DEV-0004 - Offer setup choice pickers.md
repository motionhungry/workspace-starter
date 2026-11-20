---
id: DEV-0004
type: improvement
status: validating
created: 2026-11-20
updated: 2026-11-20
---
# Offer setup choice pickers

## Problem and evidence

The operator wants simple setup choices to be selectable when the assistant's client provides a picker. During a ChatGPT project trial, the initial reply led with successful preflight details and asked for the destination and setup route together without showing how to answer.

## Outcome and proposed change

Prefer the session's built-in choice picker for two or three clear options. Offer the same choices in a numbered list when a picker is unavailable. Keep backup destination and policy confirmation as a separate step.

The root README prompt applies the same picker guidance before the workspace exists. It names the selected folder, recommends starting fresh when the folder is empty, and offers restore or a folder change.

## Acceptance criteria

- Setup presents one question with the recommended option first and offers deferral when supported.
- Setup can collect the same answer using a picker or a numbered list.
- The selected backup route does not substitute for confirmation of the destination and policy.
- For an empty folder, the first choice names the folder and presents Start fresh (recommended), Restore from a backup, and Change folder in that order. The text fallback tells the operator how to reply.
- Selecting Start fresh confirms the named destination in one response. Restore requires separate confirmation of the backup URL before writing. Change folder starts a new check.
- Successful preflight and release details stay out of the first reply unless requested. A blocking check explains the action needed.

## Approval

The operator approved adding picker guidance to the starter setup skill. The operator then approved applying the agreed first-run choices to the pasted setup prompt for both ChatGPT and Claude.

## Validation

The integration suite passed on a generated workspace. The setup skill keeps both presentation paths and explicit backup confirmation.

After updating the README, all four integration tests and development record validation passed. The integration tests cover workspace operations. A read-only Codex CLI 0.167.2 trial surfaced the write-access blocker. A writable noninteractive Codex trial waited for a picker selection with the fixture still empty, but its text output did not show the choices. Claude Code 2.1.246 print mode listed all three options and gave reply instructions, along with extra preflight and release details. The prompt now limits the ready-folder reply and requires that the session can display choices and receive a selection before using a picker. A second Claude Code trial gave the expected numbered choices and omitted release details, but still led with a preflight summary. The prompt now explicitly limits preflight reporting to blockers. Its effect and live picker rendering still need confirmation.

## Next step

Observe the first-run choices in ChatGPT and Claude project sessions, including a picker where available and the numbered fallback. Check that selecting restore or change folder follows the expected route before any files are written.
