#!/usr/bin/env python3
"""Validate development records and save the workspace's first proposal."""

import argparse
from datetime import date
import json
import os
from pathlib import Path
import re
import sys
from tempfile import NamedTemporaryFile


DEVELOPMENT = Path("90 System Development")
RECORD_TYPES = {
    "improvement": ("DEV", "10 Improvements", {"open", "in-progress", "validating", "closed"}),
    "decision": ("ADR", "20 Decisions", {"proposed", "accepted", "superseded", "rejected"}),
    "journal": ("JRN", "30 Journal", set()),
}
ARCHIVE = "99 Archive"
FIRST_ID = f"{RECORD_TYPES['improvement'][0]}-0001"
FIRST_PATH = DEVELOPMENT / RECORD_TYPES["improvement"][1] / f"{FIRST_ID}.md"
CLOSURE_REASONS = {"resolved", "declined", "duplicate", "no-longer-relevant"}
REQUIRED_SECTIONS = (
    "Problem and evidence",
    "Outcome and boundaries",
    "Proposed change",
    "Acceptance criteria",
    "Approval",
    "Next step",
)


class RecordError(ValueError):
    pass


def parse_record(markdown):
    lines = markdown.splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        raise RecordError("Expected YAML frontmatter enclosed by ---.")
    end = lines.index("---", 1)
    fields = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        key, separator, raw_value = line.partition(": ")
        if not separator or not re.fullmatch(r"[a-z][a-z0-9_]*", key):
            raise RecordError(f"Invalid property line: {line!r}")
        if key in fields:
            raise RecordError(f"Duplicate property: {key}")
        value = raw_value.strip()
        if value.startswith('"'):
            try:
                value = json.loads(value)
            except ValueError as error:
                raise RecordError(f"{key} needs a valid double-quoted string.") from error
        elif not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", value):
            raise RecordError(f"{key} needs a plain scalar or a double-quoted string.")
        fields[key] = value
    return fields, "\n".join(lines[end + 1:])


def validate_fields(fields, relative_path):
    record_type = fields.get("type")
    if record_type not in RECORD_TYPES:
        raise RecordError("type must be improvement, decision, or journal.")
    prefix, folder, statuses = RECORD_TYPES[record_type]
    record_id = fields.get("id", "")
    if not re.fullmatch(rf"{prefix}-(?:[0-9]{{4}}|[1-9][0-9]{{4,}})", record_id) or record_id.endswith("-0000"):
        raise RecordError(f"id must begin with {prefix}- and have a positive number padded to four digits.")
    if relative_path.parent not in (DEVELOPMENT / folder, DEVELOPMENT / ARCHIVE):
        raise RecordError(f"Expected a note directly inside {folder}/ or {ARCHIVE}/.")
    if record_id == FIRST_ID:
        if relative_path.name != FIRST_PATH.name:
            raise RecordError(f"The first proposal must keep the basename {FIRST_PATH.name}.")
    elif not re.fullmatch(rf"{re.escape(record_id)} - \S.*\.md", relative_path.name):
        raise RecordError(f"Expected the filename {record_id} - <short title>.md.")

    dates = []
    for key in ("created", "updated"):
        value = fields.get(key, "")
        try:
            if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
                raise ValueError
            dates.append(date.fromisoformat(value))
        except ValueError as error:
            raise RecordError(f"{key} needs a valid local date in YYYY-MM-DD format.") from error
    if dates[1] < dates[0]:
        raise RecordError("updated must be on or after created.")

    allowed = {"id", "type", "created", "updated"}
    if statuses:
        allowed.add("status")
        if fields.get("status") not in statuses:
            raise RecordError(f"Invalid status. Use {', '.join(sorted(statuses))}.")
    if record_type == "improvement":
        allowed.add("parent")
        if "parent" in fields and not re.fullmatch(
            rf"\[\[{prefix}-[0-9]{{4,}}(?: - [^\[\]\r\n]+)?\]\]", fields["parent"]
        ):
            raise RecordError("parent must be a quoted wikilink to an improvement.")
        if fields["status"] == "closed":
            allowed.add("closure_reason")
            if fields.get("closure_reason") not in CLOSURE_REASONS:
                raise RecordError(f"Invalid closure_reason. Use {', '.join(sorted(CLOSURE_REASONS))}.")
    unknown = fields.keys() - allowed
    if unknown:
        raise RecordError(f"Unexpected properties for this record: {', '.join(sorted(unknown))}.")


def record_paths(workspace, folders):
    for folder in folders:
        directory = workspace / DEVELOPMENT / folder
        yield from sorted(path.relative_to(workspace) for path in directory.rglob("*.md"))


def validate_record(workspace, path):
    note = workspace / path
    try:
        if path.is_absolute() or note.resolve() != note:
            raise RecordError("Development record paths must be inside the workspace and use real files.")
        fields, _ = parse_record(note.read_text(encoding="utf-8"))
        validate_fields(fields, path)
    except (OSError, UnicodeError, RecordError) as error:
        raise RecordError(f"{path}: {error}") from error
    return fields


def first_record(workspace):
    folders = [RECORD_TYPES["improvement"][1], ARCHIVE]
    found = []
    for path in record_paths(workspace, folders):
        fields = validate_record(workspace, path)
        if fields["id"] == FIRST_ID:
            found.append(path)
    if len(found) > 1:
        raise RecordError(f"Found multiple first proposals: {', '.join(str(path) for path in found)}")
    return next(iter(found), None)


def validate_first_body(body):
    body = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL).strip()
    if not re.match(r"# \S.+", body) or body.splitlines()[0] == "# Improvement title":
        raise RecordError("Give the first proposal a descriptive title.")
    parts = re.split(r"^## (.+?) *$", body, flags=re.MULTILINE)
    sections = dict(zip(parts[1::2], parts[2::2]))
    missing = [section for section in REQUIRED_SECTIONS if not sections.get(section, "").strip()]
    if missing:
        raise RecordError(f"Fill in the first proposal sections: {', '.join(missing)}.")


def save_first(workspace, draft):
    existing = first_record(workspace)
    if existing:
        raise RecordError(f"The first proposal already exists at {existing}.")
    markdown = draft.read_text(encoding="utf-8")
    fields, body = parse_record(markdown)
    validate_fields(fields, FIRST_PATH)
    if fields["status"] != "open":
        raise RecordError("Save the first proposal with open status.")
    validate_first_body(body)

    destination = workspace / FIRST_PATH
    if destination.resolve() != destination:
        raise RecordError("The first proposal requires a real file path inside the workspace.")
    # Publish only after the complete draft has been written. The link fails if the path exists.
    with NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=destination.parent, prefix=".first-proposal-"
    ) as temporary:
        temporary.write(markdown)
        temporary.flush()
        os.link(temporary.name, destination)
    print(FIRST_PATH)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, default=Path.cwd())
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("first", help="Print the saved first proposal's path, or exit 1 if absent.")
    save = commands.add_parser("save-first", help="Validate and save an approved first proposal.")
    save.add_argument("--draft", type=Path, required=True)
    validate = commands.add_parser("validate", help="Validate development record frontmatter.")
    validate.add_argument("paths", type=Path, nargs="*")
    args = parser.parse_args()

    try:
        workspace = args.workspace.resolve(strict=True)
        if not (workspace / DEVELOPMENT).is_dir():
            raise RecordError(f"Open the workspace root containing {DEVELOPMENT}/.")
        if args.command == "first":
            path = first_record(workspace)
            if path is None:
                return 1
            print(path)
        elif args.command == "save-first":
            save_first(workspace, args.draft)
        else:
            folders = [folder for _, folder, _ in RECORD_TYPES.values()] + [ARCHIVE]
            paths = args.paths or list(record_paths(workspace, folders))
            ids = {}
            for path in paths:
                fields = validate_record(workspace, path)
                record_id = fields["id"]
                if record_id in ids and ids[record_id] != path:
                    raise RecordError(f"Duplicate id {record_id}: {ids[record_id]} and {path}")
                ids[record_id] = path
            print(f"Validated {len(paths)} development record(s).")
    except (OSError, UnicodeError, RecordError) as error:
        print(f"Record error: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
