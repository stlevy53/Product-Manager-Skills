#!/usr/bin/env python3
"""Validate skill metadata for Claude custom skills compatibility.

Checks:
- Valid YAML frontmatter
- name present and <= 64 chars
- description present and <= 200 chars
- folder name matches frontmatter name
"""

from __future__ import annotations

import glob
import os
import sys
from dataclasses import dataclass

try:
    import yaml
except ImportError:  # pragma: no cover
    print("PyYAML is required. Install with: python3 -m pip install pyyaml", file=sys.stderr)
    raise


@dataclass
class Issue:
    path: str
    code: str
    detail: str


def load_frontmatter(text: str) -> dict | None:
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    return yaml.safe_load(parts[1]) or {}


def check_skill(path: str) -> list[Issue]:
    with open(path, "r", encoding="utf-8") as handle:
        text = handle.read()

    issues: list[Issue] = []
    data = load_frontmatter(text)
    if data is None:
        issues.append(Issue(path, "frontmatter_missing", "Missing or malformed frontmatter"))
        return issues

    name = (data.get("name") or "").strip()
    description = (data.get("description") or "").strip()

    if not name:
        issues.append(Issue(path, "name_missing", "Frontmatter name is required"))
    elif len(name) > 64:
        issues.append(Issue(path, "name_too_long", f"{len(name)} chars"))

    if not description:
        issues.append(Issue(path, "description_missing", "Frontmatter description is required"))
    elif len(description) > 200:
        issues.append(Issue(path, "description_too_long", f"{len(description)} chars"))

    folder = os.path.basename(os.path.dirname(path))
    if name and folder != name:
        issues.append(Issue(path, "folder_name_mismatch", f"folder={folder} name={name}"))

    return issues


def main() -> int:
    skill_files = sorted(glob.glob("skills/*/SKILL.md"))
    if not skill_files:
        print("No skills found.")
        return 1

    all_issues: list[Issue] = []
    for path in skill_files:
        all_issues.extend(check_skill(path))

    if not all_issues:
        print("All skills pass metadata checks.")
        return 0

    print("Metadata issues detected:\n")
    for issue in all_issues:
        print(f"- {issue.code}: {issue.path} ({issue.detail})")

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
