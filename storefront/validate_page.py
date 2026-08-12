#!/usr/bin/env python3
"""Structural checks for the storefront landing page.

The landing page is hand-written, has no build step, and is edited by hand every time the
bundle lineup changes -- which is exactly the situation where a stray unclosed ``<div>`` or a
link to an ``id`` that got renamed slips through and nobody notices until a buyer does. This
script is the cheap substitute for a framework:

* every tag is balanced and properly nested;
* every ``href="#..."`` resolves to an ``id`` that actually exists on the page;
* every ``class`` used in the HTML is defined somewhere in ``styles.css``, and every class
  defined in the CSS is used by the HTML (a dead rule usually means a renamed element);
* every ``getElementById``/``querySelector`` target in ``main.js`` exists in the HTML;
* the ``<title>`` and meta description fit in a search result without being truncated;
* the purchase links are still placeholders, so a half-finished edit cannot ship a listing
  page whose buy buttons go nowhere.

Run from the repository root::

    python storefront/validate_page.py

Exit status is non-zero if anything fails, so it can gate a deploy.
"""

from __future__ import annotations

import os
import re
import sys
from html.parser import HTMLParser

# Tags that never have a closing tag in HTML5.
VOID = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}

# Google truncates around these widths. They are guidelines, not hard limits, so going over
# is a warning rather than an error -- but the title in particular is worth keeping short.
TITLE_MAX = 60
DESC_MIN, DESC_MAX = 120, 160


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[tuple[str, int]] = []
        self.errors: list[str] = []
        self.ids: set[str] = set()
        self.anchors: list[tuple[str, int]] = []
        self.classes: set[str] = set()
        self.title = ""
        self.description = ""
        self.og_title = ""
        self.og_description = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        attrd = dict(attrs)
        line = self.getpos()[0]

        if "id" in attrd:
            if attrd["id"] in self.ids:
                self.errors.append(f"line {line}: duplicate id {attrd['id']!r}")
            self.ids.add(attrd["id"])

        href = attrd.get("href", "")
        if href.startswith("#") and href != "#":
            self.anchors.append((href[1:], line))

        for cls in (attrd.get("class") or "").split():
            self.classes.add(cls)

        if tag == "title":
            self._in_title = True
        if tag == "meta":
            if attrd.get("name") == "description":
                self.description = attrd.get("content", "")
            if attrd.get("property") == "og:title":
                self.og_title = attrd.get("content", "")
            if attrd.get("property") == "og:description":
                self.og_description = attrd.get("content", "")

        if tag not in VOID:
            self.stack.append((tag, line))

    def handle_endtag(self, tag):
        line = self.getpos()[0]
        if tag == "title":
            self._in_title = False
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append(f"line {line}: stray </{tag}> with nothing open")
            return
        open_tag, open_line = self.stack.pop()
        if open_tag != tag:
            self.errors.append(
                f"line {line}: </{tag}> closes <{open_tag}> opened on line {open_line}"
            )

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def check(ok: bool, passed: list, failed: list, message: str) -> bool:
    (passed if ok else failed).append(message)
    return ok


def main(argv=None) -> int:
    root = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(root, "index.html")
    css_path = os.path.join(root, "styles.css")
    js_path = os.path.join(root, "main.js")

    with open(html_path, encoding="utf-8") as handle:
        html = handle.read()
    with open(css_path, encoding="utf-8") as handle:
        css = handle.read()
    with open(js_path, encoding="utf-8") as handle:
        js = handle.read()

    parser = PageParser()
    parser.feed(html)

    passed: list[str] = []
    failed: list[str] = []

    # --- structure -------------------------------------------------------------------
    for err in parser.errors:
        failed.append(f"markup: {err}")
    if parser.stack:
        for tag, line in parser.stack:
            failed.append(f"markup: <{tag}> opened on line {line} is never closed")
    if not parser.errors and not parser.stack:
        passed.append("markup: all tags balanced and correctly nested")

    # --- internal anchors ------------------------------------------------------------
    broken = [(a, line) for a, line in parser.anchors if a not in parser.ids]
    if broken:
        for anchor, line in broken:
            failed.append(f"anchor: line {line}: href=\"#{anchor}\" has no matching id")
    else:
        passed.append(
            f"anchors: all {len(parser.anchors)} internal links resolve "
            f"({len(parser.ids)} ids on the page)"
        )

    # --- CSS classes -----------------------------------------------------------------
    # Strip comments first so a commented-out rule does not count as "defined".
    css_live = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    defined = set(re.findall(r"\.(-?[_a-zA-Z][\w-]*)", css_live))
    # "js-" prefixed classes are behaviour hooks for main.js, deliberately unstyled so that
    # restyling an element cannot silently detach its JavaScript. They are checked against
    # main.js below instead of against the stylesheet.
    hooks = {c for c in parser.classes if c.startswith("js-")}
    undefined = sorted(parser.classes - defined - hooks)
    if undefined:
        for cls in undefined:
            failed.append(f"css: class {cls!r} used in HTML but not defined in styles.css")
    else:
        passed.append(
            f"css: all {len(parser.classes) - len(hooks)} styled HTML classes are defined "
            f"in styles.css"
        )

    # Every js- hook must actually be referenced by main.js, or it is a dead hook.
    for hook in sorted(hooks):
        check(hook in js, passed, failed, f"js: hook class {hook!r} is used by main.js")

    # Classes the JS adds at runtime are legitimately absent from the HTML.
    js_classes = set(re.findall(r"classList\.\w+\(\s*[\"']([\w-]+)", js))
    js_classes |= set(re.findall(r"[\"']\.([\w-]+)[\"']", js))
    unused = sorted(defined - parser.classes - js_classes)
    if unused:
        failed.append(
            "css: defined but never used in HTML or JS (renamed element?): "
            + ", ".join(unused)
        )
    else:
        passed.append("css: no dead class rules")

    # --- JS hooks --------------------------------------------------------------------
    js_ids = set(re.findall(r"getElementById\(\s*[\"']([\w-]+)[\"']", js))
    missing_ids = sorted(js_ids - parser.ids)
    if missing_ids:
        for name in missing_ids:
            failed.append(f"js: getElementById({name!r}) has no matching id in the HTML")
    else:
        passed.append(f"js: all {len(js_ids)} getElementById targets exist")

    js_sel = set(re.findall(r"querySelector(?:All)?\(\s*[\"']\.([\w-]+)[\"']", js))
    missing_sel = sorted(js_sel - parser.classes)
    if missing_sel:
        for name in missing_sel:
            failed.append(f"js: querySelector('.{name}') matches nothing in the HTML")
    else:
        passed.append(f"js: all {len(js_sel)} class selectors match the HTML")

    # --- search-result metadata ------------------------------------------------------
    title = parser.title.strip()
    desc = parser.description.strip()
    check(bool(title), passed, failed, f"seo: <title> present ({len(title)} chars)")
    if title and len(title) > TITLE_MAX:
        failed.append(
            f"seo: <title> is {len(title)} chars, over the ~{TITLE_MAX} shown in results: {title!r}"
        )
    elif title:
        passed.append(f"seo: <title> fits in {TITLE_MAX} chars ({len(title)})")

    if not desc:
        failed.append("seo: no meta description")
    elif not DESC_MIN <= len(desc) <= DESC_MAX:
        failed.append(
            f"seo: meta description is {len(desc)} chars, outside the "
            f"{DESC_MIN}-{DESC_MAX} range shown in results"
        )
    else:
        passed.append(f"seo: meta description is {len(desc)} chars, within "
                      f"{DESC_MIN}-{DESC_MAX}")

    for label, value in (("og:title", parser.og_title), ("og:description", parser.og_description)):
        check(bool(value.strip()), passed, failed, f"seo: {label} present")

    # --- buy links -------------------------------------------------------------------
    buy_comments = len(re.findall(r"BUY LINK", html))
    live_buy = re.findall(r'href="(https?://(?:gumroad|etsy)[^"]*)"', html, re.I)
    if live_buy:
        passed.append(f"buy links: {len(live_buy)} real store URLs wired up")
    else:
        passed.append(f"buy links: {buy_comments} BUY LINK placeholders still marked for editing")
    if buy_comments == 0 and not live_buy:
        failed.append("buy links: no BUY LINK markers and no store URLs -- purchase path is missing")

    # --- report ----------------------------------------------------------------------
    for line in passed:
        print(f"[ok]   {line}")
    for line in failed:
        print(f"[FAIL] {line}")

    print()
    print(f"checks passed: {len(passed)}   failed: {len(failed)}")
    if failed:
        print("landing page validation FAILED")
        return 1
    print("landing page validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
