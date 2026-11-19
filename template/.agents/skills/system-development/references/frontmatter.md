# Frontmatter design

Give structured note types a documented frontmatter contract. Freeform notes and inbox captures can stay plain Markdown. Use the existing contract in `90 System Development/AGENTS.md` for development tickets, decisions, and journals.

- **Use fields that do work.** Add a property for identity, filtering, sorting, linking, lifecycle, or validation when a real view or workflow uses it. Prefer small values with consistent types across the vault. Keep applicable project outcomes short.
- **Keep narrative in the note body.** Use Markdown for rationale, approval evidence, acceptance criteria, findings, and next steps. Omit optional properties when they do not apply. Preserve stable IDs and creation dates, and advance the update date for substantive changes.
- **Change the contract with its consumers.** Name the view, workflow, or check that needs the field. Define its purpose, type, allowed values, and whether it is required. Update the template, relevant instructions, and affected views or validators together. Leave older notes as they are when the consumers handle an absent value. Include any required backfill in the approved scope and validate it against representative existing notes.
