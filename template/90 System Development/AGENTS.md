# System Development Records

Read these conventions when working on system development. Follow the workspace root's operating instructions and Git policy. The system-development skill owns the workflow.

## Record locations

- Keep one note per improvement in `10 Improvements/`, decision in `20 Decisions/`, or substantive session in `30 Journal/`.
- Use independent numeric sequences for development tickets (`DEV-`), decisions (`ADR-`), and journals (`JRN-`). Use `<ID> - <short title>.md`. Setup reserves `DEV-0001.md` for the first workspace proposal. Check active and archived records before choosing the next number. Keep stable IDs and filenames, and retain archived records so their IDs remain issued. Coordinate across copies before allocating an ID.
- Name each DEV ticket with a short summary of the work, such as `DEV-0002 - Verify backup after setup.md`. Use that summary as the note heading. For the reserved first proposal, put the summary in the heading.
- Name each ADR for the choice it records, such as `ADR-0001 - Keep media outside the vault.md`. Track the decision's lifecycle in `status` and keep the filename stable as the status changes.
- Link records with basename wikilinks, including an alias if helpful. Keep the archive flat and retain basenames on moves. Keep current accepted decisions active while they govern work. Closed improvements and superseded or rejected decisions can move to `99 Archive/` after recording their disposition and verifying their links. Reopening restores the active location, sets `status: open`, removes `closure_reason`, and records the reason. Preserve identity and creation date during moves and updates.
- Store concise evidence in the owning improvement. Put any durable supporting brief in this visible development area and link it to its owner. Put disposable test output outside the workspace.

## Frontmatter

Start with the templates in `.agents/skills/system-development/assets/`. All records begin with `---`, one flat property per line, and a closing `---`. Use plain scalar values for the core fields. Double-quote wikilinks such as `parent: "[[DEV-0002 - Example]]"`.

| Record | Required properties | Additional properties |
| --- | --- | --- |
| All | `id`, `type`, `created`, `updated` | Use actual local dates in `YYYY-MM-DD` format. Preserve `created` and update `updated` on substantive changes. |
| Improvement | `type: improvement`, `status` of `open`, `in-progress`, `validating`, or `closed` | `closure_reason` is required on closure and takes `resolved`, `declined`, `duplicate`, or `no-longer-relevant`. Omit it while active. Optional `parent` links to a parent improvement. |
| Decision | `type: decision`, `status` of `proposed`, `accepted`, `superseded`, or `rejected` | Retain context, alternatives, consequences, actual approval evidence, and links in the body. |
| Journal | `type: journal` | Record substantive session findings and a next step. Link the owning improvement when applicable. |

Read-only lookup leaves dates and status alone. Metadata represents record state. Record the actual authorization and its scope in the body when work is approved.

Run `python3 .agents/skills/system-development/scripts/records.py validate` from the workspace root to validate the contract and check for duplicate IDs across active and archived records. Pass root-relative note paths after `validate` to check selected records. The validator accepts a flat subset of YAML with plain letters, numbers, hyphens and underscores, or double-quoted strings. Keep lists and explanatory text in the note body.

When an approved improvement introduces project notes, define their frontmatter before creating the first project. Include at least record type, outcome, lifecycle state, creation date and last substantive update date. Define the template, allowed values, validity checks and treatment of existing notes for any new record type or field. Skill metadata has its own contract.
