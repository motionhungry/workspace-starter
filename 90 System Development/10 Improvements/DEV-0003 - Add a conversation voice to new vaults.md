---
id: DEV-0003
type: improvement
status: validating
created: 2026-11-20
updated: 2026-11-20
---
# Add a conversation voice to new vaults

## Problem and evidence

First-run feedback identified a need for operator-facing guidance that can be tuned in each vault. Saved notes and drafts need to reflect their own author, reader, purpose, and conventions.

## Outcome and boundaries

Give each new vault a default conversation voice that its operator can edit, with guidance on writing drafts and documents for their intended audience. Apply the same convention when the assistant enters the vault during setup or in a later chat.

## Proposed change

Ship `.agents/voice.md` in the template. Add an explicit read instruction to the vault's `AGENTS.md`. Have the bootstrap prompt direct the assistant to the generated operating instructions, and tell operators where to edit the voice in the vault README. The wording follows the precise references and single-source guidance in Matt Pocock's [Writing for Agents](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md).

## Acceptance criteria

- Bootstrap from a committed template gives each new vault an editable `.agents/voice.md` and a startup instruction that references it.
- The bootstrap prompt directs the assistant to the generated `AGENTS.md` before the setup skill, including when the chat started before the vault existed.
- A fresh session in a generated fixture reads the voice file without the request naming it, gives a direct update, and follows a supplied template for a draft shown in chat.

## Approval

The operator approved a trial of an editable voice file with a startup instruction and clarified on 2026-11-20 that it belongs in the starter template for all new vaults. See [[ADR-0001 - Keep conversation voice in each vault]].

## Validation

- All four integration tests passed on macOS with Git 2.50.1 and Python 3.14.2. Bootstrap copied the guide and its pointer from a committed template. A separate two-vault check confirmed independent customization and that bootstrap refused to overwrite an existing vault.
- The setup prompt directs the assistant to the generated `AGENTS.md` before the setup skill. In a fresh read-only Codex CLI 0.167.2 session in a generated fixture, the assistant read the voice guide without being prompted by name. It led its final reply with the result and open decision, then followed the draft template. Its first progress message preceded the guide read.
- Claude Code 2.1.246 timed out during the conversational check. Its discovery adapter passed the integration tests. Conversational checks in Claude Code and ChatGPT Work are pending.

## Next step

Review the starter change through a pull request. Observe the voice in normal use on the intended assistant surfaces and revisit the startup approach if initial replies need the guidance.
