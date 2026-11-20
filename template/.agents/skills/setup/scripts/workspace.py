"""Bootstrap a vault, manage local discovery, and checkpoint reviewed files."""

import argparse
import io
import json
import os
from pathlib import Path
import re
import subprocess
import tarfile
import tempfile
from urllib.parse import unquote, urlsplit


SETTINGS = Path("90 System Development/workflow-settings.json")
LOCAL = Path(".agents/local.json")
SKILLS = Path(".agents/skills")
CLAUDE_SKILLS = Path(".claude/skills")
UPDATE_SKILL = "check-starter-updates"


class WorkspaceError(Exception):
    pass


def git(root, *args, check=True):
    result = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
    if check and result.returncode:
        operation = args[2] if args[0] == "-c" else args[0]
        if operation == "--literal-pathspecs":
            operation = args[1]
        raise WorkspaceError(f"git {operation} failed. Check Git configuration and access.")
    return result


def git_root(folder):
    result = git(folder, "rev-parse", "--show-toplevel", check=False)
    return Path(result.stdout.strip()).resolve() if result.returncode == 0 else None


def repo_key(url, root):
    """Compare common HTTPS, SSH, and local forms of the same repository."""
    if url.startswith("-") or not url or any(ord(char) < 32 for char in url):
        raise WorkspaceError("Use a Git repository URL or path.")
    parsed = urlsplit(url)
    if "://" in url:
        if parsed.query or parsed.fragment or parsed.password is not None:
            raise WorkspaceError("Use a credential-free repository URL.")
        if parsed.scheme == "file" and parsed.hostname in (None, "localhost"):
            return ("file", str(Path(unquote(parsed.path)).resolve()))
        if parsed.scheme not in ("https", "ssh") or not parsed.hostname:
            raise WorkspaceError("Use an HTTPS, SSH, or local Git repository URL.")
        if parsed.scheme == "https" and parsed.username is not None:
            raise WorkspaceError("Use HTTPS credentials from Git's credential helper.")
        host = parsed.hostname.lower()
        path = unquote(parsed.path)
    else:
        scp = re.fullmatch(r"(?:[^/@:]+@)?([^/:]+):(.+)", url)
        if scp is None:
            return ("file", str((root / url).resolve()))
        host, path = scp.groups()
        host = host.lower()
    if host == "ssh.github.com":
        host = "github.com"
    path = path.strip("/").removesuffix(".git")
    return (host, path.lower() if host == "github.com" else path)


def bootstrap(source, destination, author_name, author_email):
    if (author_name is not None or author_email is not None) and not (
        author_name and author_name.strip() and author_email and author_email.strip()
    ):
        raise WorkspaceError("Provide both a Git author name and email.")
    source = source.resolve()
    destination = destination.expanduser().absolute()
    if destination.is_symlink():
        raise WorkspaceError("Choose a destination folder directly, without a symlink.")
    destination = destination.resolve()
    if not destination.parent.is_dir():
        raise WorkspaceError("Create the intended parent directory first.")
    if destination.exists() and (not destination.is_dir() or any(destination.iterdir())):
        raise WorkspaceError("Destination has existing files. Inspect it and resume setup in place.")
    if git_root(destination.parent) is not None:
        raise WorkspaceError("Choose a parent outside existing Git repositories.")
    if git_root(source) != source:
        raise WorkspaceError("Select the starter checkout root as the source.")
    commit = git(source, "rev-parse", "HEAD").stdout.strip()
    url = git(source, "remote", "get-url", "origin").stdout.strip()
    repo_key(url, source)
    tag = git(source, "describe", "--exact-match", "--tags", commit, check=False)
    starter = {"url": url, "original_commit": commit}
    if tag.returncode == 0:
        starter["original_tag"] = tag.stdout.strip()
    archive = subprocess.run(
        ["git", "archive", "--format=tar", f"{commit}:template"],
        cwd=source, capture_output=True,
    )
    if archive.returncode:
        raise WorkspaceError("The selected source commit has no distributable template.")
    with tempfile.TemporaryDirectory(prefix=".workspace-starter-", dir=destination.parent) as staging:
        vault = Path(staging) / "vault"
        vault.mkdir()
        baseline_paths = []
        with tarfile.open(fileobj=io.BytesIO(archive.stdout), mode="r:") as payload:
            for entry in payload:
                path = vault / entry.name
                if not path.resolve().is_relative_to(vault) or not (entry.isdir() or entry.isfile()):
                    raise WorkspaceError("The template contains an unsupported archive entry.")
                if entry.isdir():
                    path.mkdir(parents=True, exist_ok=True)
                else:
                    baseline_paths.append(entry.name)
                    path.parent.mkdir(parents=True, exist_ok=True)
                    with path.open("xb") as output:
                        output.write(payload.extractfile(entry).read())
        with (vault / SETTINGS).open("x", encoding="utf-8") as output:
            json.dump({"schema_version": 1, "starter": starter}, output, indent=2)
            output.write("\n")
        git(vault, "init", "-b", "main")
        if author_name is not None:
            git(vault, "config", "--local", "user.name", author_name)
            git(vault, "config", "--local", "user.email", author_email)
        for identity in ("GIT_AUTHOR_IDENT", "GIT_COMMITTER_IDENT"):
            if git(vault, "-c", "user.useConfigOnly=true", "var", identity, check=False).returncode:
                raise WorkspaceError(
                    "Git needs an author name and email. Retry bootstrap with "
                    "--author-name and --author-email to set them for this vault."
                )
        git(vault, "--literal-pathspecs", "add", "-f", "--", *baseline_paths, str(SETTINGS))
        git(vault, "-c", "user.useConfigOnly=true", "commit", "-m", "Create workspace from starter")
        vault.rename(destination)
    print(f"Created workspace at {destination}")


def settings(root):
    path = root / SETTINGS
    if path.is_symlink() or not path.resolve().is_relative_to(root):
        raise WorkspaceError("Keep workflow settings inside the workspace.")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        source = data["starter"]
        if data["schema_version"] != 1 or not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", source["original_commit"]):
            raise ValueError
        repo_key(source["url"], root)
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        raise WorkspaceError("Missing or invalid workflow settings. Inspect setup before continuing.") from None
    return data


def discovery(root, per_skill):
    settings(root)
    claude = root / ".claude"
    if claude.is_symlink():
        raise WorkspaceError("Existing .claude symlink preserved. Inspect its discovery configuration.")
    claude.mkdir(exist_ok=True)
    adapter = root / CLAUDE_SKILLS
    relative_target = "../.agents/skills"
    source = root / SKILLS
    if source.resolve() != source or not source.is_dir():
        raise WorkspaceError("Keep the editable skill directory inside the workspace.")
    if adapter.is_symlink():
        if os.readlink(adapter) != relative_target:
            raise WorkspaceError("Existing Claude skill link preserved. Review its target.")
        if not per_skill:
            return
        adapter.unlink()
    if not adapter.exists() and not per_skill:
        adapter.symlink_to(relative_target, target_is_directory=True)
        return
    if not adapter.exists():
        adapter.mkdir()
    if not adapter.is_dir():
        raise WorkspaceError("Existing Claude skills entry preserved. Review its type.")
    conflicts = []
    for skill in sorted(source.iterdir()):
        if skill.is_symlink() or not (skill / "SKILL.md").is_file():
            continue
        link = adapter / skill.name
        if link.is_symlink() or link.exists():
            if not link.is_symlink() or link.resolve() != skill:
                conflicts.append(skill.name)
        else:
            link.symlink_to(f"../../.agents/skills/{skill.name}", target_is_directory=True)
    if conflicts:
        raise WorkspaceError("Existing Claude entries preserved. Review conflicts: " + ", ".join(conflicts))


def enable_updates(root):
    data = settings(root)
    if data["starter"].get("update_review") != "enabled":
        raise WorkspaceError("Record the operator's opt-in before enabling starter update review.")
    skill = root / SKILLS / UPDATE_SKILL
    if skill.resolve() != skill:
        raise WorkspaceError("Existing update skill symlink preserved. Inspect it before continuing.")
    skill.mkdir(exist_ok=True)
    definition = skill / "SKILL.md"
    if definition.is_symlink() or (definition.exists() and not definition.is_file()):
        raise WorkspaceError("Existing update skill entry preserved. Inspect it before continuing.")
    if not definition.exists():
        source = root / SKILLS / "setup/assets" / f"{UPDATE_SKILL}.md"
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=skill) as output:
            output.write(source.read_text(encoding="utf-8"))
            output.flush()
            os.link(output.name, definition)
    discovery(root, per_skill=False)


def verify_local_media(root, folder):
    data = settings(root)
    if data.get("media", {}).get("kind") != "local":
        raise WorkspaceError("Record the operator's local media choice first.")
    local_path = root / LOCAL
    if local_path.resolve() != local_path:
        raise WorkspaceError("Keep local settings in a regular file inside the workspace.")
    local = json.loads(local_path.read_text(encoding="utf-8")) if local_path.exists() else {}
    if not isinstance(local, dict):
        raise WorkspaceError("Local settings must be a JSON object.")
    if folder is None:
        if not isinstance(local.get("media_path"), str) or not local["media_path"]:
            raise WorkspaceError("Confirm a local media folder for this computer.")
        folder = Path(local["media_path"])
    folder = folder.expanduser().resolve()
    if folder.is_relative_to(root) or root.is_relative_to(folder):
        raise WorkspaceError("Choose a separate media folder outside the workspace.")
    local["media_path"] = str(folder)
    local.pop("media_pending_reason", None)
    try:
        with os.scandir(folder) as listing:
            next(listing, None)
        local["media_access"] = "verified"
    except OSError:
        local["media_access"] = "pending"
        local["media_pending_reason"] = "The selected folder could not be listed."
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=local_path.parent, delete=False,
    ) as output:
        candidate = Path(output.name)
        try:
            json.dump(local, output, indent=2)
            output.write("\n")
            output.close()
            candidate.replace(local_path)
        finally:
            candidate.unlink(missing_ok=True)
    if local["media_access"] == "pending":
        raise WorkspaceError(local["media_pending_reason"])
    print("Verified access to the selected local media folder.")


def backup_target(root, data):
    backup = data.get("backup")
    if not isinstance(backup, dict) or backup.get("policy") != "commit-and-push":
        raise WorkspaceError("Confirm the backup destination and checkpoint policy first.")
    remote = backup.get("remote")
    branch = backup.get("branch")
    url = backup.get("url")
    if not isinstance(remote, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", remote):
        raise WorkspaceError("Invalid approved backup remote name.")
    if not isinstance(branch, str) or branch.startswith("-") or not branch:
        raise WorkspaceError("Invalid approved backup branch.")
    git(root, "check-ref-format", f"refs/heads/{branch}")
    if not isinstance(url, str):
        raise WorkspaceError("Record the approved backup URL.")
    approved = repo_key(url, root)
    if approved == repo_key(data["starter"]["url"], root):
        raise WorkspaceError("The backup destination must be independent of the starter source.")
    for options in ([], ["--push"]):
        urls = git(root, "remote", "get-url", *options, "--all", remote).stdout.splitlines()
        if urls != [url]:
            raise WorkspaceError("The configured Git URLs differ from the single approved backup URL.")
    ref = f"refs/heads/{branch}"
    current = git(root, "symbolic-ref", "HEAD").stdout.strip()
    if current != ref:
        raise WorkspaceError("Switch to the approved backup branch before checkpointing.")
    source_commit = data["starter"]["original_commit"]
    ancestry = git(root, "merge-base", "--is-ancestor", source_commit, "HEAD", check=False)
    if ancestry.returncode == 0:
        raise WorkspaceError("The workspace contains the starter's Git history. Use an independent workspace.")
    return remote, ref


def validate_paths(root, paths):
    for path in paths:
        relative = Path(path)
        if (relative.is_absolute() or ".." in relative.parts or not relative.parts
                or relative.parts[0] == ".git"):
            raise WorkspaceError("List individual workspace-relative files.")
        item = root / relative
        if not item.parent.resolve().is_relative_to(root) or item.is_dir():
            raise WorkspaceError("List individual files inside the workspace.")
        if git(root, "check-ignore", "--no-index", "--", path, check=False).returncode == 0:
            raise WorkspaceError(f"An explicit path is ignored: {path}")


def checkpoint(root, message, paths):
    data = settings(root)
    if git_root(root) != root:
        raise WorkspaceError("Run from the generated workspace's own Git root.")
    operations = ("MERGE_HEAD", "CHERRY_PICK_HEAD", "REVERT_HEAD", "rebase-merge", "rebase-apply", "sequencer")
    git_paths = git(root, "rev-parse", *(arg for name in operations for arg in ("--git-path", name)))
    if any((root / path).exists() for path in git_paths.stdout.splitlines()):
        raise WorkspaceError("A Git operation is in progress. Resolve it before checkpointing.")
    if paths:
        if not message or not message.strip():
            raise WorkspaceError("Provide a commit message with the reviewed paths.")
        validate_paths(root, paths)
        staged = git(
            root, "diff", "--cached", "--name-only", "--no-renames", "--ignore-submodules=none", "-z",
        ).stdout.rstrip("\0").split("\0")
        if set(staged) - {str(Path(path)) for path in paths} - {""}:
            raise WorkspaceError("Unrelated staged work is present. Preserve it and resolve the index first.")
        git(root, "--literal-pathspecs", "add", "-A", "--", *paths)
        if git(root, "diff", "--cached", "--quiet", check=False).returncode == 1:
            git(root, "commit", "-m", message)
    elif message is not None:
        raise WorkspaceError("List reviewed files with the commit message, or omit both to retry backup.")
    head = git(root, "rev-parse", "HEAD").stdout.strip()
    if "backup" not in data:
        print(f"Saved local checkpoint {head}")
        return
    try:
        remote, ref = backup_target(root, data)
        git(root, "-c", "push.followTags=false", "push", "--recurse-submodules=no", "--", remote, f"{head}:{ref}")
        observed = git(root, "ls-remote", "--exit-code", "--refs", "--", remote, ref).stdout.strip()
        if observed != f"{head}\t{ref}":
            raise WorkspaceError("Remote verification returned a different commit.")
    except WorkspaceError as error:
        raise WorkspaceError(f"Backup pending for local commit {head}. {error}") from None
    print(f"Verified backup of {head} on {remote}/{data['backup']['branch']}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    create = commands.add_parser("bootstrap")
    create.add_argument("--source", type=Path, required=True)
    create.add_argument("--destination", type=Path, required=True)
    create.add_argument("--author-name")
    create.add_argument("--author-email")
    adapter = commands.add_parser("discovery")
    adapter.add_argument("--per-skill", action="store_true")
    commands.add_parser("enable-updates")
    media = commands.add_parser("local-media")
    media.add_argument("--folder", type=Path)
    save = commands.add_parser("checkpoint")
    save.add_argument("--message")
    save.add_argument("paths", nargs="*")
    args = parser.parse_args()
    root = Path.cwd()
    try:
        if args.command == "bootstrap":
            bootstrap(args.source, args.destination, args.author_name, args.author_email)
        elif args.command == "discovery":
            discovery(root, args.per_skill)
        elif args.command == "enable-updates":
            enable_updates(root)
        elif args.command == "local-media":
            verify_local_media(root, args.folder)
        else:
            checkpoint(root, args.message, args.paths)
    except (WorkspaceError, OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
