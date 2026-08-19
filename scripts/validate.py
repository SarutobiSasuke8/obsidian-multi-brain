#!/usr/bin/env python3
"""Validate the public multi-brain contract without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "examples" / "pattern-d-agent-bridge"

REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "docs/patterns.md",
    "docs/agent-context-satellites.md",
    "docs/security.md",
    "templates/satellite-entry-point.md",
    "examples/pattern-d-agent-bridge/README.md",
    "examples/pattern-d-agent-bridge/satellite-entry-point.md",
    "examples/pattern-d-agent-bridge/central/Public/Product Overview.md",
    "examples/pattern-d-agent-bridge/satellite/Context/public-safe/product-overview.md",
    "examples/pattern-d-agent-bridge/satellite/Workspace/research/brief.md",
    "examples/pattern-d-agent-bridge/satellite/CRM/Proposals/contact-update.md",
    ".github/workflows/validate.yml",
)

FRONTMATTER_SPECS = {
    "templates/satellite-entry-point.md": {
        "title",
        "type",
        "brand",
        "satellite-root",
        "pattern",
        "authority-model",
        "mutability",
        "created",
    },
    "examples/pattern-d-agent-bridge/satellite-entry-point.md": {
        "title",
        "type",
        "brand",
        "satellite-root",
        "pattern",
        "authority-model",
        "mutability",
        "created",
    },
    "examples/pattern-d-agent-bridge/satellite/Context/public-safe/product-overview.md": {
        "type",
        "tier",
        "master",
        "sync",
        "last_synced",
        "mutability",
    },
    "examples/pattern-d-agent-bridge/satellite/Workspace/research/brief.md": {
        "type",
        "workspace_scope",
        "authority",
        "created",
        "mutability",
    },
    "examples/pattern-d-agent-bridge/satellite/CRM/Proposals/contact-update.md": {
        "type",
        "status",
        "source_agent",
        "canonical_target",
        "created",
        "mutability",
    },
}

EXACT_VALUES = {
    "templates/satellite-entry-point.md": {
        "title": "[Brand Name] Satellite Vault Sync",
        "type": "satellite-entry-point",
        "brand": "[Brand Name]",
        "satellite-root": "[absolute path to the satellite vault or repo]",
        "pattern": "[A / B / C / D]",
        "authority-model": "[single-owner / mixed-authority]",
        "mutability": "living",
        "created": "YYYY-MM-DD",
    },
    "examples/pattern-d-agent-bridge/satellite-entry-point.md": {
        "type": "satellite-entry-point",
        "pattern": "D",
        "authority-model": "mixed-authority",
        "mutability": "living",
    },
    "examples/pattern-d-agent-bridge/satellite/Context/public-safe/product-overview.md": {
        "type": "agent-context",
        "tier": "public-safe",
        "sync": "push",
        "mutability": "mirror",
    },
    "examples/pattern-d-agent-bridge/satellite/Workspace/research/brief.md": {
        "type": "agent-workspace",
        "workspace_scope": "research",
        "mutability": "living",
    },
    "examples/pattern-d-agent-bridge/satellite/CRM/Proposals/contact-update.md": {
        "type": "crm-proposal",
        "status": "proposed",
        "mutability": "append-only",
    },
}

CONTRACT_TERMS = {
    "README.md": (
        "Why this exists / strategic value",
        "Context/public-safe/",
        "Workspace/",
        "CRM/Proposals/",
        "python scripts/validate.py",
    ),
    "AGENTS.md": ("Context/public-safe/", "Workspace/<mount>/", "CRM/Proposals/"),
    "docs/patterns.md": (
        "Mixed-authority agent bridge",
        "Context/public-safe/",
        "Workspace/",
        "CRM/Proposals/",
    ),
    "templates/satellite-entry-point.md": (
        "Authority zones (Pattern D only)",
        "Context/public-safe/",
        "Workspace/[mount]/",
        "CRM/Proposals/",
    ),
}

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
DATE_VALUE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
UNSAFE_FIXTURE_PLACEHOLDERS = (
    "YYYY-MM-DD",
    "[Brand Name]",
    "[absolute path",
    "[path to",
    "[Add rows",
    "[agent ids",
    "[mount]",
)
CREDENTIAL_SHAPE = re.compile(
    r"(?i)(?:gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16}|"
    r"(?:api[_-]?key|access[_-]?token|password|client[_-]?secret)\s*[:=]\s*[\"']?[A-Za-z0-9_./+-]{12,})"
)


def strip_scalar(value: str) -> str:
    """Return the useful value from the small scalar-only YAML subset we use."""
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value.split(" #", 1)[0].strip()


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str | None]:
    """Parse top-level scalar frontmatter and return (fields, error)."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, "missing opening frontmatter delimiter"

    try:
        closing = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        return {}, "missing closing frontmatter delimiter"

    fields: dict[str, str] = {}
    for line_number, line in enumerate(lines[1:closing], start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line[:1].isspace() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        if not re.fullmatch(r"[A-Za-z0-9_-]+", key):
            return {}, f"invalid frontmatter key on line {line_number}: {key!r}"
        fields[key] = strip_scalar(value)
    return fields, None


def contains_private_path(text: str) -> bool:
    """Detect concrete home-directory paths while allowing documented placeholders."""
    patterns = (
        r"(?i)\b[A-Z]:[\\/]Users[\\/](?!\[|<|\{|\$)[^\\/\s]+",
        r"(?i)(?<![A-Za-z0-9_])/Users/(?!\[|<|\{|\$)[^/\s]+",
        r"(?i)(?<![A-Za-z0-9_])/home/(?!\[|<|\{|\$)[^/\s]+",
        r"(?i)file://(?:/[A-Z]:)?/(?:Users|home)/",
    )
    return any(re.search(pattern, text) for pattern in patterns)


def validate_required_files() -> list[str]:
    return [f"missing required file: {name}" for name in REQUIRED_FILES if not (ROOT / name).is_file()]


def validate_frontmatter() -> list[str]:
    errors: list[str] = []
    parsed: dict[str, dict[str, str]] = {}

    for relative, required in FRONTMATTER_SPECS.items():
        path = ROOT / relative
        if not path.is_file():
            continue
        fields, error = parse_frontmatter(path)
        if error:
            errors.append(f"{relative}: {error}")
            continue
        parsed[relative] = fields
        missing = sorted(field for field in required if not fields.get(field))
        if missing:
            errors.append(f"{relative}: missing frontmatter fields: {', '.join(missing)}")

        for field in ("created", "last_synced"):
            value = fields.get(field)
            if value and value != "YYYY-MM-DD" and not DATE_VALUE.fullmatch(value):
                errors.append(f"{relative}: {field} must be YYYY-MM-DD, got {value!r}")

    for relative, expected in EXACT_VALUES.items():
        fields = parsed.get(relative, {})
        for field, value in expected.items():
            if fields.get(field) != value:
                errors.append(f"{relative}: expected {field}: {value!r}, got {fields.get(field)!r}")

    context_relative = "examples/pattern-d-agent-bridge/satellite/Context/public-safe/product-overview.md"
    context = parsed.get(context_relative, {})
    master = context.get("master")
    if master and not (FIXTURE / "central" / Path(master)).is_file():
        errors.append(f"{context_relative}: master does not exist in fixture central vault: {master}")

    workspace_relative = "examples/pattern-d-agent-bridge/satellite/Workspace/research/brief.md"
    workspace = parsed.get(workspace_relative, {})
    workspace_scope = workspace.get("workspace_scope")
    if workspace_scope and workspace_scope != "research":
        errors.append(f"{workspace_relative}: scope must match Workspace/research/")

    return errors


def link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    elif " \"" in target:
        target = target.split(" \"", 1)[0]
    return unquote(target.split("#", 1)[0].split("?", 1)[0])


def validate_links() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            target = link_target(match.group(1))
            if not target or target.startswith(("http://", "https://", "mailto:", "obsidian://", "#")):
                continue
            resolved = (path.parent / Path(target)).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                relative = path.relative_to(ROOT).as_posix()
                errors.append(f"{relative}: local link escapes repository: {match.group(1)}")
                continue
            if not resolved.exists():
                relative = path.relative_to(ROOT).as_posix()
                errors.append(f"{relative}: broken local link: {match.group(1)}")
    return errors


def validate_placeholder_safety() -> list[str]:
    errors: list[str] = []
    public_suffixes = {".md", ".canvas", ".json", ".yml", ".yaml"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in public_suffixes:
            continue
        text = path.read_text(encoding="utf-8")
        if contains_private_path(text):
            errors.append(f"{path.relative_to(ROOT).as_posix()}: contains a concrete private machine path")

    for path in FIXTURE.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for marker in UNSAFE_FIXTURE_PLACEHOLDERS:
            if marker in text:
                errors.append(f"{path.relative_to(ROOT).as_posix()}: unresolved fixture placeholder: {marker}")
        if CREDENTIAL_SHAPE.search(text):
            errors.append(f"{path.relative_to(ROOT).as_posix()}: contains credential-shaped content")
    return errors


def validate_contract_terms() -> list[str]:
    errors: list[str] = []
    for relative, terms in CONTRACT_TERMS.items():
        path = ROOT / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for term in terms:
            if term not in text:
                errors.append(f"{relative}: missing Pattern D contract term: {term}")
    return errors


def validate_canvases() -> list[str]:
    errors: list[str] = []
    for relative in ("Multi-Brain Management System.canvas", "canvas/multi-brain-management-system.canvas"):
        path = ROOT / relative
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{relative}: invalid canvas JSON: {exc}")
            continue
        combined = "\n".join(str(node.get("text", "")) for node in data.get("nodes", []))
        for term in ("Mixed-authority agent bridge", "Context/public-safe/", "Workspace/<mount>/", "CRM/Proposals/"):
            if term not in combined:
                errors.append(f"{relative}: missing Pattern D canvas term: {term}")
    return errors


def run_checks() -> list[str]:
    errors: list[str] = []
    for check in (
        validate_required_files,
        validate_frontmatter,
        validate_links,
        validate_placeholder_safety,
        validate_contract_terms,
        validate_canvases,
    ):
        errors.extend(check())
    return errors


def main() -> int:
    errors = run_checks()
    if errors:
        print(f"validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"validation passed: {len(REQUIRED_FILES)} required files and Pattern D fixture checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
