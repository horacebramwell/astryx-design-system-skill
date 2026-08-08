#!/usr/bin/env python3
"""Validate the standalone Astryx Agent Skill package."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
EXPECTED_NAME = "astryx-design-system"
REQUIRED = [
    SKILL,
    ROOT / "README.md",
    ROOT / "references" / "cli-workflow.md",
    ROOT / "references" / "setup-styling.md",
    ROOT / "references" / "layout-themes.md",
    ROOT / "references" / "migration-browser.md",
    ROOT / "references" / "integrations-api.md",
    ROOT / "references" / "research-sources.md",
    ROOT / "checklists" / "implementation-checklist.md",
    ROOT / "checklists" / "review-checklist.md",
]

errors: list[str] = []

for path in REQUIRED:
    if not path.is_file():
        errors.append(f"missing required file: {path.relative_to(ROOT)}")

if SKILL.is_file():
    text = SKILL.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) >= 500:
        errors.append(f"SKILL.md must be under 500 lines; found {len(lines)}")

    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
    else:
        end = text.find("\n---\n", 4)
        if end == -1:
            errors.append("SKILL.md frontmatter is not closed")
        else:
            frontmatter = text[4:end]
            name_match = re.search(r"^name:\s*(.+)$", frontmatter, re.MULTILINE)
            description_match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
            if not name_match:
                errors.append("frontmatter missing name")
            elif name_match.group(1).strip() != EXPECTED_NAME:
                errors.append(
                    f"frontmatter name must be {EXPECTED_NAME!r}; found {name_match.group(1).strip()!r}"
                )
            if not description_match or not description_match.group(1).strip():
                errors.append("frontmatter missing non-empty description")

    referenced = set(
        re.findall(r"`((?:references|checklists)/[^`]+\.md)`", text)
    )
    for rel in sorted(referenced):
        if not (ROOT / rel).is_file():
            errors.append(f"broken relative reference from SKILL.md: {rel}")

if ROOT.name != EXPECTED_NAME:
    errors.append(
        f"skill directory should be named {EXPECTED_NAME!r}; found {ROOT.name!r}"
    )

if errors:
    print("FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("PASS")
print(f"- skill: {EXPECTED_NAME}")
print(f"- SKILL.md lines: {len(SKILL.read_text(encoding='utf-8').splitlines())}")
print(f"- required files: {len(REQUIRED)}")
