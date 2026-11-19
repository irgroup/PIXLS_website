#!/usr/bin/env python3
"""
Static site builder for the PIXLS project website.
Reads structured Markdown & YAML files from content/ and renders index.html
via templates/base.html.

Usage:
    python3 scripts/build.py
"""

from __future__ import annotations

import html
import re
from pathlib import Path

import jinja2
import markdown
import yaml
from markupsafe import Markup

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"
TEMPLATES_DIR = ROOT / "templates"
OUTPUT_FILE = ROOT / "index.html"


def add_external_link_attrs(rendered_html: str) -> str:
    """Add target='_blank' rel='noopener noreferrer' to external http(s) links."""
    return re.sub(
        r'<a\s+href="(https?://[^"]+)"',
        r'<a href="\1" target="_blank" rel="noopener noreferrer"',
        rendered_html,
    )


def md_block(text: str) -> Markup:
    """Render block-level Markdown to HTML."""
    rendered = markdown.markdown(text.strip(), extensions=["extra"])
    return Markup(add_external_link_attrs(rendered))


def md_inline(text: str) -> Markup:
    """Render inline Markdown to HTML (strips outer <p>...</p>)."""
    rendered = markdown.markdown(text.strip(), extensions=["extra"])
    rendered = re.sub(r"^<p>(.*)</p>$", r"\1", rendered, flags=re.DOTALL)
    return Markup(add_external_link_attrs(rendered))


def highlight_code(code: str, lang: str = "python") -> Markup:
    """Lightweight syntax highlighter matching the dark code theme."""
    lines = code.rstrip().splitlines()
    out: list[str] = []
    for raw_line in lines:
        escaped = html.escape(raw_line)
        if escaped.lstrip().startswith("#"):
            out.append(f'<span style="color: #8b949e;">{escaped}</span>')
            continue

        if lang == "python":
            escaped = re.sub(
                r'(&quot;[^&]*?&quot;|"[^"]*?")',
                r'<span style="color: #a5d6ff;">\1</span>',
                escaped,
            )
            escaped = re.sub(
                r"\b(from|import|def|return|as|with|for|in)\b",
                r'<span style="color: #ff7b72;">\1</span>',
                escaped,
            )
            escaped = re.sub(
                r"\b(True|False|None)\b",
                r'<span style="color: #79c0ff;">\1</span>',
                escaped,
            )
        elif lang == "bash":
            escaped = re.sub(
                r"(https?://\S+|\./\S+)",
                r'<span style="color: #a5d6ff;">\1</span>',
                escaped,
            )
            escaped = re.sub(
                r"^(\s*)(cd)\b",
                r'\1<span style="color: #79c0ff;">\2</span>',
                escaped,
            )
        out.append(escaped)
    return Markup("\n".join(out))


def parse_frontmatter_md(path: Path) -> tuple[dict, str]:
    """Parse a Markdown file with YAML frontmatter (--- ... ---)."""
    raw = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", raw, flags=re.DOTALL)
    if not match:
        raise ValueError(f"Missing YAML frontmatter in {path}")
    meta = yaml.safe_load(match.group(1)) or {}
    body = match.group(2).strip()
    return meta, body


def load_yaml(name: str) -> dict:
    return yaml.safe_load((CONTENT_DIR / name).read_text(encoding="utf-8")) or {}


def load_blog_posts() -> list[dict]:
    posts: list[dict] = []
    blog_dir = CONTENT_DIR / "blog"
    for md_file in sorted(blog_dir.glob("*.md")):
        meta, body = parse_frontmatter_md(md_file)
        meta["body_html"] = md_block(body)
        posts.append(meta)
    # Sort newest first by YYYY-MM date string
    posts.sort(key=lambda p: str(p.get("date", "")), reverse=True)
    return posts


def build() -> None:
    site = load_yaml("site.yaml")
    hero = load_yaml("hero.yaml")
    pillars = load_yaml("pillars.yaml")
    tools = load_yaml("tools.yaml")
    publications = load_yaml("publications.yaml")
    team = load_yaml("team.yaml")
    funding = load_yaml("funding.yaml")

    # Sort publications chronologically (newest first)
    publications["publications"].sort(
        key=lambda p: str(p.get("date", "")), reverse=True
    )

    about_meta, about_body = parse_frontmatter_md(CONTENT_DIR / "about.md")
    about_meta["challenge_html"] = md_block(about_body)

    blog_posts = load_blog_posts()

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=jinja2.select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["md_inline"] = md_inline
    env.filters["md_block"] = md_block
    env.filters["highlight_code"] = highlight_code

    template = env.get_template("base.html")
    rendered = template.render(
        site=site,
        hero=hero,
        about=about_meta,
        pillars=pillars,
        tools=tools,
        publications=publications,
        blog_posts=blog_posts,
        team=team,
        funding=funding,
    )

    OUTPUT_FILE.write_text(rendered, encoding="utf-8")
    print(f"Built {OUTPUT_FILE.relative_to(ROOT)} ({len(rendered):,} bytes) from {CONTENT_DIR.relative_to(ROOT)}/")


if __name__ == "__main__":
    build()
