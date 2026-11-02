"""Validate the public skill catalog without installing or running any skill."""
from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


def assert_plain_tree(directory: Path) -> int:
    count = 0
    for item in directory.iterdir():
        if item.name == "__pycache__":
            continue
        if item.is_symlink() or getattr(item, "is_junction", lambda: False)():
            raise ValueError(f"Public skill contains a link: {item.relative_to(ROOT)}")
        if item.is_dir():
            count += assert_plain_tree(item)
        else:
            count += 1
    return count


def check_markdown_links(file: Path) -> int:
    count = 0
    for raw in re.findall(r"\]\(([^)]+)\)", file.read_text(encoding="utf-8")):
        target = raw.strip().strip("<>")
        if not target or target.startswith("#") or urlsplit(target).scheme:
            continue
        relative = unquote(urlsplit(target).path)
        if relative and not (file.parent / relative).exists():
            raise ValueError(f"Missing reference in {file.relative_to(ROOT)}: {target}")
        count += 1
    return count


def main() -> None:
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    names: set[str] = set()
    counts = {}
    links = 0
    for entry in catalog["skills"]:
        name = entry["name"]
        if name in names or entry["path"] != f"skills/{name}":
            raise ValueError(f"Duplicate or invalid catalog entry: {name}")
        names.add(name)
        directory = ROOT / entry["path"]
        skill = directory / "SKILL.md"
        text = skill.read_text(encoding="utf-8")
        if not text.startswith("---") or not re.search(rf"(?m)^name:\s*{re.escape(name)}\s*$", text):
            raise ValueError(f"Invalid skill entry point: {name}")
        counts[name] = assert_plain_tree(directory)
        for markdown in directory.rglob("*.md"):
            links += check_markdown_links(markdown)
        if not entry.get("license"):
            raise ValueError(f"Missing license declaration: {name}")
    directories = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
    if directories != names:
        raise ValueError("Skill directories and catalog differ")
    for file in [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md")), ROOT / "third-party/NOTICE.md"]:
        links += check_markdown_links(file)
    tracked = subprocess.run(["git", "ls-files", "--cached", "-z"], cwd=ROOT, check=True, capture_output=True).stdout.decode("utf-8").split("\0")
    for name in filter(None, tracked):
        if name.startswith((".local/", "local-only/", ".agents/")) or "/__pycache__/" in name:
            raise ValueError(f"Local-only path in Git: {name}")
        data = subprocess.run(["git", "show", f":{name}"], cwd=ROOT, check=True, capture_output=True).stdout
        if re.search(rb"gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", data):
            raise ValueError(f"Credential pattern in staged content: {name}")
        normalized = data.replace(b"\\", b"/").lower()
        for private_root in (Path.home(), ROOT.parent):
            if str(private_root).replace("\\", "/").encode("utf-8").lower() in normalized:
                raise ValueError(f"Personal machine path in staged content: {name}")
    print(json.dumps({"skills":len(names), "files":counts, "local_links":links, "staged_files":len(list(filter(None, tracked))), "errors":[]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
