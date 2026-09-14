#!/usr/bin/env python3

import hashlib
import json
import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IDENTITY = ROOT / "repository.json"


def repository_slug() -> str | None:
    slug = os.environ.get("GITHUB_REPOSITORY") or os.environ.get("REPOSITORY_SLUG")
    if slug:
        return slug.removesuffix(".git").strip("/")

    result = subprocess.run(
        ["git", "config", "--get", "remote.origin.url"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    remote = result.stdout.strip()
    match = re.search(r"github\.com(?::|/)([^/]+/[^/]+?)(?:\.git)?$", remote)
    return match.group(1) if match else None


def check_readme_identity(path: Path, published: bool) -> list[str]:
    """Check only this project's brand and publication state."""
    text = path.read_text(encoding="utf-8")
    errors = []
    if "<h1>laiism.skill</h1>" not in text:
        errors.append(f"{path.name}: expected the laiism.skill project display name")
    if published:
        if "status-local_draft" in text:
            errors.append(f"{path.name}: published repository still marked as local")
    elif "status-local_draft" not in text or "repository.json" not in text:
        errors.append(f"{path.name}: unpublished repository must identify its local state")
    if not published and "img.shields.io/github/" in text:
        errors.append(f"{path.name}: remote badge before publication")
    return errors


def tracked_text() -> list[tuple[str, str]]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    files = []
    for raw in result.stdout.split(b"\0"):
        if not raw:
            continue
        rel = raw.decode()
        path = ROOT / rel
        if path.is_symlink() or not path.is_file():
            continue
        try:
            files.append((rel, path.read_bytes().decode("utf-8")))
        except UnicodeDecodeError:
            pass
    return files


def evidence_valid(value) -> bool:
    if not isinstance(value, dict):
        return False
    linked = (
        isinstance(value.get("url"), str)
        and value["url"].startswith("https://")
        and isinstance(value.get("locator"), str)
        and bool(value["locator"].strip())
    )
    recorded = (
        isinstance(value.get("date"), str)
        and re.fullmatch(r"\d{4}-\d{2}-\d{2}", value["date"]) is not None
        and isinstance(value.get("statement"), str)
        and bool(value["statement"].strip())
    )
    return bool(linked or recorded)


def content_digest(item) -> str:
    payload = json.dumps(
        {key: item.get(key) for key in ("id", "title", "content")},
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def check_positions(data) -> list[str]:
    errors = []
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        return ["positions: unsupported schema"]
    positions = data.get("positions")
    if not isinstance(positions, list) or not positions:
        return ["positions: expected a nonempty list"]
    ids = set()
    for index, item in enumerate(positions):
        prefix = f"positions[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix}: expected an object")
            continue
        for field in ("id", "title", "content"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                errors.append(f"{prefix}: missing {field}")
        item_id = item.get("id")
        if not isinstance(item_id, str) or not re.fullmatch(r"[a-z]+(?:-[a-z]+)*", item_id):
            errors.append(f"{prefix}: invalid ID")
        elif item_id in ids:
            errors.append(f"{prefix}: duplicate ID {item_id}")
        else:
            ids.add(item_id)
        source = item.get("source")
        if not evidence_valid(source):
            errors.append(f"{prefix}: missing source evidence")
        elif source.get("kind") not in ("model-summary", "user-statement", "proposal"):
            errors.append(f"{prefix}: invalid source kind")
        if item.get("personal_status") not in ("confirmed", "unconfirmed"):
            errors.append(f"{prefix}: invalid personal status")
        if item.get("doctrine_status") not in ("ratified", "unratified"):
            errors.append(f"{prefix}: invalid doctrine status")
        if item.get("personal_status") == "confirmed" and not evidence_valid(
            item.get("confirmation")
        ):
            errors.append(f"{prefix}: confirmed position lacks confirmation evidence")
        if item.get("doctrine_status") == "ratified":
            evidence = item.get("ratification")
            if item.get("personal_status") != "confirmed":
                errors.append(f"{prefix}: doctrine requires a confirmed position")
            if not evidence_valid(evidence):
                errors.append(f"{prefix}: doctrine lacks separate ratification evidence")
            elif evidence.get("approved_by") != "lailai" or evidence.get("scope") != "doctrine":
                errors.append(
                    f"{prefix}: ratification must identify the approver and doctrine scope"
                )
            elif evidence == item.get("confirmation"):
                errors.append(f"{prefix}: personal confirmation cannot double as ratification")
            elif evidence.get("content_sha256") != content_digest(item):
                errors.append(f"{prefix}: ratification does not match the current content")
    return errors


def check_text(rel: str, content: str) -> list[str]:
    errors = []
    if any(
        match.group() != match.group().lower()
        for match in re.finditer(r"laiism(?:[.-]skill)?", rel + "\n" + content, re.IGNORECASE)
    ):
        errors.append(f"{rel}: brand must remain lowercase")
    if rel == "SKILL.md" and not re.search(r"^# laiism\.skill$", content, re.MULTILINE):
        errors.append(f"{rel}: expected the laiism.skill project title")
    if "\r" in content or not content.endswith("\n"):
        errors.append(f"{rel}: use LF and a final newline")
    if rel.endswith(".md"):
        for target in re.findall(r"\]\(([^\s)]+)\)", content):
            if re.match(r"[a-z]+:|#", target):
                continue
            path = target.split("#", 1)[0]
            if not (ROOT / rel).parent.joinpath(path).exists():
                errors.append(f"{rel}: broken local link: {target}")
    return errors


def main() -> int:
    errors = []
    required_files = (
        "README.md",
        "README.zh-Hans.md",
        "scripts/check_repository.py",
        "repository.json",
        "positions.json",
        "SKILL.md",
        "LICENSE-docs",
    )
    for rel in required_files:
        if not (ROOT / rel).exists():
            errors.append(f"missing required file: {rel}")

    if errors:
        print("\n".join(f"ERROR {error}" for error in errors))
        return 1
    try:
        identity = json.loads(IDENTITY.read_text(encoding="utf-8"))
        data = json.loads((ROOT / "positions.json").read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        print(f"ERROR invalid project data: {exc}")
        return 1
    if not isinstance(identity, dict):
        print("ERROR repository metadata must be an object")
        return 1
    slug = identity.get("slug")
    if slug != "lailai0916/laiism-skill" or identity.get("display_name") != "laiism.skill":
        errors.append("repository: unexpected project identity")
    published = identity.get("published")
    if type(published) is not bool:
        errors.append("repository: publication state must be boolean")
    detected_slug = repository_slug()
    if detected_slug is not None and detected_slug != slug:
        errors.append("repository: runtime or remote identity disagrees with metadata")
    if published and not detected_slug:
        errors.append(
            "repository: published state requires a real configured origin or CI identity"
        )
    errors.extend(check_readme_identity(ROOT / "README.md", published))
    errors.extend(check_readme_identity(ROOT / "README.zh-Hans.md", published))
    errors.extend(check_positions(data))

    for rel, text in tracked_text():
        errors.extend(check_text(rel, text))

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1

    print(f"Position and project-specific checks passed for {slug} (published={published}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
