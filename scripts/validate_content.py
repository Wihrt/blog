#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "jsonschema>=4.23",
#     "python-frontmatter>=1.1",
#     "pyyaml>=6.0",
# ]
# ///
"""Validate every blog post against the publishing contract.

Posts reach this repository through automated pull requests. Hugo will happily
build a post with a missing description, a tag nobody uses, or a body that got
truncated mid-generation, so the build alone is not a sufficient gate. This
script is that gate: it fails loudly, names the file and the field, and says
what to do about it.

Run it with `mise run validate`.
"""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import frontmatter
import yaml
from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = REPO_ROOT / "content" / "posts"
SCHEMA_PATH = REPO_ROOT / "schemas" / "post.schema.json"
TAGS_PATH = REPO_ROOT / "data" / "tags.yaml"

MIN_BODY_WORDS = 200
MAX_FUTURE = timedelta(hours=24)

RAW_HTML = re.compile(r"<(?!!--)\s*/?\s*[a-zA-Z][a-zA-Z0-9-]*(?:\s[^>]*)?>")
INSECURE_URL = re.compile(r"\bhttp://(?!localhost|127\.0\.0\.1)", re.IGNORECASE)
REMOTE_IMAGE = re.compile(r"!\[[^\]]*\]\(\s*(https?://[^)\s]+)")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(\s*([^)\s]+)")
FENCE = re.compile(r"^(```|~~~)")


class Problem(Exception):
    """Not used for control flow; findings are accumulated instead."""


def load_schema() -> Draft202012Validator:
    with SCHEMA_PATH.open(encoding="utf-8") as handle:
        return Draft202012Validator(json.load(handle))


def load_allowed_tags() -> set[str]:
    with TAGS_PATH.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    tags = data.get("tags") or []
    if not tags:
        sys.exit(f"{TAGS_PATH.relative_to(REPO_ROOT)}: no tags defined")
    return set(tags)


def strip_code_fences(body: str) -> str:
    """Drop fenced code blocks so examples inside posts are not linted as prose."""
    out, inside = [], False
    for line in body.splitlines():
        if FENCE.match(line.strip()):
            inside = not inside
            continue
        if not inside:
            out.append(line)
    return "\n".join(out)


def as_datetime(value: object) -> datetime | None:
    """Accept what a YAML parser may produce for a timestamp field."""
    if isinstance(value, datetime):
        return value
    if isinstance(value, str):
        try:
            return datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            return None
    return None


def check_dates(meta: dict, report) -> None:
    now = datetime.now(timezone.utc)
    published = as_datetime(meta.get("date"))
    if published is None:
        report("date", "not a valid RFC 3339 timestamp")
        return
    if published.tzinfo is None:
        report("date", "missing a UTC offset (use e.g. 2026-08-21T09:00:00+02:00)")
        return
    if published > now + MAX_FUTURE:
        report("date", f"is more than 24h in the future ({published.isoformat()})")

    modified = meta.get("lastmod")
    if modified is not None:
        parsed = as_datetime(modified)
        if parsed is None or parsed.tzinfo is None:
            report("lastmod", "not a valid RFC 3339 timestamp with an offset")
        elif parsed < published:
            report("lastmod", "is earlier than date")


def check_body(body: str, report) -> None:
    prose = strip_code_fences(body)

    words = len(prose.split())
    if words < MIN_BODY_WORDS:
        report(
            "body",
            f"has {words} words, below the {MIN_BODY_WORDS} word minimum "
            "(a truncated generation usually looks like this)",
        )

    if RAW_HTML.search(prose):
        report(
            "body",
            "contains raw HTML, which Hugo is configured to drop "
            "(markup.goldmark.renderer.unsafe = false)",
        )

    for match in INSECURE_URL.finditer(prose):
        snippet = prose[match.start() : match.start() + 60].splitlines()[0]
        report("body", f"links over plain http: {snippet}")

    for match in REMOTE_IMAGE.finditer(prose):
        report(
            "body",
            f"embeds a remote image ({match.group(1)}); "
            "commit it to the page bundle instead",
        )

    for match in MARKDOWN_LINK.finditer(prose):
        target = match.group(1)
        if target.startswith(("http://", "https://", "#", "mailto:", "/")):
            continue
        report("body", f"uses a relative link ({target}); use a site-absolute path")


def check_tags(meta: dict, allowed: set[str], report) -> None:
    for tag in meta.get("tags") or []:
        if tag not in allowed:
            report(
                "tags",
                f"'{tag}' is not in data/tags.yaml "
                "(add it there in a separate, human-reviewed change)",
            )


def main() -> int:
    if not POSTS_DIR.is_dir():
        sys.exit(f"{POSTS_DIR.relative_to(REPO_ROOT)} does not exist")

    validator = load_schema()
    allowed_tags = load_allowed_tags()

    posts = sorted(POSTS_DIR.rglob("*.md"))
    if not posts:
        sys.exit("no posts found under content/posts/")

    failures = 0
    slugs: dict[str, list[str]] = defaultdict(list)

    for path in posts:
        rel = path.relative_to(REPO_ROOT)
        findings: list[str] = []

        def report(field: str, message: str, _f: list[str] = findings) -> None:
            _f.append(f"{field}: {message}")

        try:
            post = frontmatter.load(path)
        except Exception as exc:  # noqa: BLE001 - surfaced verbatim to the author
            print(f"FAIL {rel}\n  front matter is not parseable: {exc}")
            failures += 1
            continue

        meta = dict(post.metadata)

        # jsonschema cannot compare a PyYAML datetime against a string type, so
        # timestamps are normalised here and range-checked separately.
        normalised = {
            k: (v.isoformat() if isinstance(v, datetime) else v) for k, v in meta.items()
        }
        for error in sorted(validator.iter_errors(normalised), key=str):
            location = ".".join(str(p) for p in error.absolute_path) or "(root)"
            report(location, error.message)

        check_dates(meta, report)
        check_tags(meta, allowed_tags, report)
        check_body(post.content, report)

        slug = meta.get("slug")
        if isinstance(slug, str):
            slugs[slug].append(str(rel))
            if path.stem != slug and path.stem != "index":
                report(
                    "slug",
                    f"'{slug}' does not match the filename '{path.stem}' "
                    "(keep them identical so the file is findable from a URL)",
                )

        if findings:
            failures += 1
            print(f"FAIL {rel}")
            for finding in findings:
                print(f"  {finding}")

    for slug, files in sorted(slugs.items()):
        if len(files) > 1:
            failures += 1
            print(f"FAIL duplicate slug '{slug}' in: {', '.join(files)}")

    checked = len(posts)
    if failures:
        print(f"\n{failures} problem(s) across {checked} post(s).")
        return 1

    print(f"{checked} post(s) validated against schemas/post.schema.json.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
