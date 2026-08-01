#!/usr/bin/env python3
"""Check or install orchestrate-dev into Codex and Claude Code skill folders."""

from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


SKILL_NAME = "orchestrate-dev"
IGNORED_PARTS = {"__pycache__", ".git"}


def manifest(root: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if not path.is_file() or any(part in IGNORED_PARTS for part in relative.parts):
            continue
        if path.suffix == ".pyc":
            continue
        result[relative.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def validate_source(source: Path) -> None:
    skill_md = source / "SKILL.md"
    if source.name != SKILL_NAME or not skill_md.is_file():
        raise ValueError(f"source must be a {SKILL_NAME} skill directory")
    content = skill_md.read_text(encoding="utf-8")
    if "name: orchestrate-dev" not in content:
        raise ValueError("SKILL.md does not declare name: orchestrate-dev")


def target_paths() -> list[Path]:
    user_root = Path.home()
    return [
        user_root / ".codex" / "skills" / SKILL_NAME,
        user_root / ".claude" / "skills" / SKILL_NAME,
    ]


def status(source: Path, target: Path) -> str:
    if not target.exists():
        return "missing"
    return "synced" if manifest(source) == manifest(target) else "drifted"


def install(source: Path, target: Path) -> Path | None:
    target.parent.mkdir(parents=True, exist_ok=True)
    stage = target.parent / f".{SKILL_NAME}.staging-{os.getpid()}"
    if stage.exists():
        raise RuntimeError(f"staging path already exists: {stage}")
    shutil.copytree(source, stage, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".git"))
    if manifest(source) != manifest(stage):
        shutil.rmtree(stage)
        raise RuntimeError(f"staged copy verification failed for {target}")

    backup: Path | None = None
    try:
        if target.exists():
            timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
            backup_root = target.parent.parent / "skill-backups"
            backup_root.mkdir(parents=True, exist_ok=True)
            backup = backup_root / f"{SKILL_NAME}-{timestamp}-{os.getpid()}"
            target.rename(backup)
        stage.rename(target)
    except Exception:
        if stage.exists():
            shutil.rmtree(stage)
        if backup is not None and backup.exists() and not target.exists():
            backup.rename(target)
        raise
    return backup


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--check", action="store_true", help="Check installation drift (default)")
    action.add_argument("--install", action="store_true", help="Install source to both hosts")
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    source = args.source.resolve()
    try:
        validate_source(source)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    targets = target_paths()
    if not args.install:
        all_synced = True
        for target in targets:
            current = status(source, target)
            print(f"{target}: {current}")
            all_synced &= current == "synced"
        return 0 if all_synced else 1

    for target in targets:
        try:
            backup = install(source, target)
        except (OSError, RuntimeError) as exc:
            print(f"ERROR installing {target}: {exc}", file=sys.stderr)
            return 2
        print(f"installed: {target}")
        if backup is not None:
            print(f"backup: {backup}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
