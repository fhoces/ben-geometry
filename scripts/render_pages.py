"""Render a course .md (concepts.md, learning-plan.md) to the styled .html GitHub Pages serves.

Usage (from the repo root):  python3 scripts/render_pages.py module-01/concepts.md [more.md ...]

Pages serves .md raw, so each .md has a committed .html twin; re-run this after
every edit to a .md. Needs python-markdown (`extra`, `sane_lists`, `toc`).
"""
import re
import sys
from pathlib import Path

import markdown

HEAD = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
STYLE = '<style>\n  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;\n         max-width: 760px; margin: 2.2rem auto; padding: 0 1.2rem; color: #1a1a1a; line-height: 1.6;\n         overflow-wrap: break-word; }\n  h1, h2, h3 { line-height: 1.25; }\n  h1 { margin-bottom: .3rem; }\n  h2 { margin-top: 2rem; }\n  a { color: #1769aa; text-decoration: none; }\n  a:hover { text-decoration: underline; }\n  blockquote { margin: 1.2rem 0; padding: .6rem 1rem; border-left: 4px solid #1769aa;\n               background: #f6f8fa; color: #333; }\n  code { background: #f0f0f0; padding: .1em .3em; border-radius: 3px;\n         font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: .9em; }\n  pre { background: #f6f8fa; padding: .9rem 1rem; border-radius: 6px; overflow-x: auto; line-height: 1.4;\n        max-width: 100%; }\n  table { display: block; overflow-x: auto; }\n  pre code { background: none; padding: 0; font-size: .82em; }\n  table { border-collapse: collapse; width: 100%; margin: 1.2rem 0; }\n  th, td { text-align: left; padding: .5rem .6rem; border-bottom: 1px solid #e2e2e2; vertical-align: top; }\n  hr { border: none; border-top: 1px solid #e2e2e2; margin: 1.6rem 0; }\n  img { max-width: 100%; }\n  footer { margin-top: 2.5rem; padding-top: 1rem; border-top: 1px solid #e2e2e2; color: #888; font-size: .85rem; }\n</style>\n</head>\n'
FOOTER = ('<footer>Part of <a href="https://github.com/fhoces">fhoces</a>\'s '
          'math-tutoring collection.</footer>\n</body>\n</html>')
RESOURCES = "https://github.com/fhoces/math-tutoring/blob/main/resources.md"


def fix_links(src):
    src = re.sub(r"\]\((\.\./)+resources\.md", "](" + RESOURCES, src)
    src = re.sub(r"\]\(([^)\s]*?)README\.md", r"](\1index.html", src)
    return re.sub(r"\]\(([^)\s:]+?)\.md(#[^)]*)?\)", r"](\1.html\2)", src)


def render(md_path):
    md_path = Path(md_path)
    src = md_path.read_text()
    title = re.search(r"^# (.+)$", src, re.M).group(1).strip()
    body = markdown.markdown(fix_links(src), extensions=["extra", "sane_lists", "toc"])
    out = HEAD + "<title>" + title + "</title>\n" + STYLE + "<body>\n" + body + "\n" + FOOTER
    md_path.with_suffix(".html").write_text(out)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        render(p)
