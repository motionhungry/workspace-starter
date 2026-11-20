"""Exercise portable setup and backup with disposable Git repositories."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest


REPO = Path(__file__).resolve().parents[1]
WORKSPACE = Path(".agents/skills/setup/scripts/workspace.py")
RECORDS = Path(".agents/skills/system-development/scripts/records.py")
SETTINGS = Path("90 System Development/workflow-settings.json")
FIRST = Path("90 System Development/10 Improvements/DEV-0001.md")
ADAPTER = Path(".claude/skills")
UPDATE_SKILL = Path(".agents/skills/check-starter-updates/SKILL.md")


class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        temp = TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name).resolve()
        self.source = self.root / "starter"
        self.source.mkdir()
        self.vault = self.root / "A new vault"
        self.backup = self.root / "backup.git"
        self.git(self.source, "init", "-b", "main")
        self.identity(self.source)
        shutil.copytree(
            REPO / "template", self.source / "template",
            ignore=shutil.ignore_patterns("__pycache__"),
        )
        self.git(self.source, "add", "template")
        self.git(self.source, "commit", "-m", "Fixture template")
        self.git(self.source, "tag", "v1.0.0")
        self.git(self.source, "remote", "add", "origin", "https://github.com/example/workspace-starter.git")

    def run_command(self, root, *args, code=0):
        env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
        env.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull, GIT_TERMINAL_PROMPT="0")
        result = subprocess.run(args, cwd=root, env=env, capture_output=True, text=True)
        self.assertEqual(result.returncode, code, result.stdout + result.stderr)
        return result.stdout.strip() if code == 0 else result.stderr.strip()

    def git(self, root, *args):
        return self.run_command(root, "git", *args)

    def identity(self, root):
        self.git(root, "config", "--local", "user.name", "Test Operator")
        self.git(root, "config", "--local", "user.email", "operator@example.invalid")

    def bootstrap(self, destination=None, code=0):
        target = destination if destination is not None else self.vault
        return self.run_command(
            self.root, sys.executable, str(self.source / "template" / WORKSPACE),
            "bootstrap", "--source", str(self.source), "--destination", str(target), code=code,
        )

    def setup_tool(self, *args, code=0):
        return self.run_command(self.vault, sys.executable, str(WORKSPACE), *args, code=code)

    def records_tool(self, *args, code=0, root=None):
        return self.run_command(root or self.vault, sys.executable, str(RECORDS), *args, code=code)

    def change_settings(self, configure):
        path = self.vault / SETTINGS
        data = json.loads(path.read_text())
        configure(data)
        path.write_text(json.dumps(data, indent=2) + "\n")

    def configure_backup(self, url):
        self.git(self.vault, "remote", "add", "origin", url)
        self.change_settings(lambda data: data.update(backup={
            "remote": "origin", "branch": "main", "policy": "commit-and-push", "url": url,
        }))

    def first_checkpoint(self):
        self.git(self.vault, "init", "-b", "main")
        self.identity(self.vault)
        self.configure_backup(str(self.backup))
        paths = sorted(
            str(path.relative_to(self.vault)) for path in self.vault.rglob("*")
            if path.is_file() and ".git" not in path.relative_to(self.vault).parts
        )
        return self.setup_tool("checkpoint", "--message", "Save setup", "--", *paths, code=1)

    def test_clean_setup_resumption_and_backup_retry(self):
        self.vault.mkdir()
        self.bootstrap()
        source_commit = self.git(self.source, "rev-parse", "HEAD")
        settings = json.loads((self.vault / SETTINGS).read_text())
        self.assertEqual(settings["starter"], {
            "url": "https://github.com/example/workspace-starter.git",
            "original_commit": source_commit,
            "original_tag": "v1.0.0",
        })
        self.assertFalse((self.vault / ".git").exists())
        self.assertTrue((self.vault / "00 Inbox").is_dir())
        self.assertFalse((self.vault / "CLAUDE.md").exists())
        voice = Path(".agents/references/voice.md")
        self.assertEqual((self.source / "template" / voice).read_bytes(), (self.vault / voice).read_bytes())
        self.assertIn(voice.as_posix(), (self.vault / "AGENTS.md").read_text())
        self.records_tool("first", code=1)
        self.assertIn("existing files", self.bootstrap(code=1))
        self.assertIn("Backup pending", self.first_checkpoint())
        initial = self.git(self.vault, "rev-parse", "HEAD")
        self.assertNotEqual(source_commit, initial)
        self.assertEqual("1", self.git(self.vault, "rev-list", "--count", "HEAD"))
        self.git(self.root, "init", "--bare", "-b", "main", str(self.backup))
        self.assertIn(initial, self.setup_tool("checkpoint"))
        self.assertEqual(initial, self.git(self.backup, "rev-parse", "main"))

        draft = self.root / "Approved draft.md"
        draft.write_text(
            "---\nid: DEV-0001\ntype: improvement\nstatus: open\n"
            "created: 2026-11-19\nupdated: 2026-11-19\n---\n"
            "# Collect board meeting decisions\n"
            "## Problem and evidence\n Follow-ups are scattered.\n"
            "## Outcome and boundaries\n Use one note for decisions and owners.\n"
            "## Proposed change\n Agree a note template.\n"
            "## Acceptance criteria\n Capture one decision and its owner.\n"
            "## Approval\n Test operator approved saving the proposal.\n"
            "## Next step\n Review an anonymized sample.\n"
        )
        self.assertEqual(str(FIRST), self.records_tool("save-first", "--draft", str(draft)))
        self.records_tool("save-first", "--draft", str(draft), code=2)
        self.records_tool("validate")

        manual = self.vault / "00 Inbox" / "Manual work.md"
        manual.write_text("Keep this unrelated note.\n")
        self.git(self.vault, "add", "--", str(manual.relative_to(self.vault)))
        arguments = ("checkpoint", "--message", "Save first proposal", "--", str(FIRST))
        self.assertIn("Unrelated staged work", self.setup_tool(*arguments, code=1))
        self.git(self.vault, "reset", "HEAD", "--", str(manual.relative_to(self.vault)))
        self.setup_tool(*arguments)
        self.assertEqual("Keep this unrelated note.\n", manual.read_text())
        self.assertIn("?? ", self.git(self.vault, "status", "--short"))
        clone = self.root / "Fresh copy"
        self.git(self.root, "clone", str(self.backup), str(clone))
        self.assertEqual(str(FIRST), self.records_tool("first", root=clone))
        self.assertEqual(draft.read_text(), (clone / FIRST).read_text())
        self.assertFalse((clone / manual.relative_to(self.vault)).exists())

        self.git(self.vault, "mv", "README.md", "Moved.md")
        error = self.setup_tool("checkpoint", "--message", "Incomplete rename", "--", "Moved.md", code=1)
        self.assertIn("Unrelated staged work", error)

    def test_decline_then_enable_updates_and_preserve_adapters(self):
        self.bootstrap()
        self.change_settings(lambda data: data["starter"].update(update_review="declined"))
        self.setup_tool("enable-updates", code=1)
        self.assertFalse((self.vault / UPDATE_SKILL).exists())
        self.setup_tool("discovery")
        self.assertEqual("../.agents/skills", os.readlink(self.vault / ADAPTER))
        self.setup_tool("discovery", "--per-skill")
        existing = self.vault / ADAPTER / "local-user-skill"
        existing.mkdir()
        self.change_settings(lambda data: data["starter"].update(update_review="enabled"))
        self.setup_tool("enable-updates")
        link = self.vault / ADAPTER / UPDATE_SKILL.parent.name
        self.assertEqual(self.vault / UPDATE_SKILL.parent, link.resolve())
        definition = self.vault / UPDATE_SKILL
        self.assertIn("only when the operator explicitly asks", definition.read_text())
        definition.write_text(definition.read_text() + "\nLocal instruction.\n")
        self.setup_tool("enable-updates")
        self.assertTrue(existing.is_dir())
        self.assertTrue(definition.read_text().endswith("Local instruction.\n"))

    def test_media_is_local_and_missing_folder_stays_pending(self):
        self.bootstrap()
        self.git(self.vault, "init", "-b", "main")
        media = self.root / "Media folder"
        self.change_settings(lambda data: data.update(media={"kind": "local"}))
        self.setup_tool("local-media", "--folder", str(media), code=1)
        local = self.vault / ".agents/local.json"
        self.assertEqual("pending", json.loads(local.read_text())["media_access"])
        media.mkdir()
        self.setup_tool("local-media")
        self.assertEqual({"media_path": str(media.resolve()), "media_access": "verified"}, json.loads(local.read_text()))
        self.assertNotIn(str(media), (self.vault / SETTINGS).read_text())
        self.assertEqual(".agents/local.json", self.git(self.vault, "check-ignore", ".agents/local.json"))

    def test_source_remote_and_nested_destination_are_rejected(self):
        self.assertIn("outside existing Git repositories", self.bootstrap(self.source / "nested", code=1))
        self.bootstrap()
        self.git(self.vault, "init", "-b", "main")
        self.identity(self.vault)
        for url in ("git@github.com:Example/Workspace-Starter.git", "ssh://git@ssh.github.com:443/example/workspace-starter.git"):
            with self.subTest(url=url):
                self.configure_backup(url)
                error = self.setup_tool("checkpoint", "--message", "Wrong remote", "--", "AGENTS.md", code=1)
                self.assertIn("independent of the starter source", error)
                self.git(self.vault, "remote", "remove", "origin")
        self.assertEqual("", self.git(self.vault, "diff", "--cached", "--name-only"))


if __name__ == "__main__":
    unittest.main()
