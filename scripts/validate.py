#!/usr/bin/env python3
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "medical-photo-reader"


def require(path: Path) -> None:
    if not path.exists():
        raise SystemExit(f"Missing required file: {path.relative_to(ROOT)}")


def main() -> None:
    require(ROOT / "README.md")
    require(ROOT / "LICENSE")
    require(SKILL / "SKILL.md")
    require(SKILL / "agents" / "openai.yaml")
    require(SKILL / "references" / "repo-stack.md")
    require(SKILL / "references" / "input-quality.md")
    require(SKILL / "references" / "vision-model-workflow.md")
    require(SKILL / "references" / "dicom-workflow.md")
    require(SKILL / "references" / "model-workflow.md")

    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise SystemExit("SKILL.md must start with YAML frontmatter")
    match = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not match:
        raise SystemExit("SKILL.md frontmatter is malformed")
    frontmatter = match.group(1)
    if "name: medical-photo-reader" not in frontmatter:
        raise SystemExit("SKILL.md frontmatter must include name: medical-photo-reader")
    if "description:" not in frontmatter:
        raise SystemExit("SKILL.md frontmatter must include description")

    print("Repository validation passed.")


if __name__ == "__main__":
    main()
