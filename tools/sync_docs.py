#!/usr/bin/env python3
"""Regenerate ``docs/`` from ``storefront/`` for GitHub Pages.

GitHub Pages, when publishing from a branch, will only serve the repository root or
``/docs``. The landing page lives in ``storefront/`` alongside its own tooling and
notes, which should not be published, so ``docs/`` is a generated copy containing
only the three files a browser needs.

Two directories holding the same page is exactly the kind of thing that silently
drifts, so this script is the only sanctioned way to update ``docs/``: run it after
every ``storefront/`` edit, and run ``--check`` if you want to find out whether the
published copy is stale without changing anything.

Usage::

    python tools/sync_docs.py            # regenerate docs/
    python tools/sync_docs.py --check     # exit 1 if docs/ is out of date

Exit status is non-zero when ``--check`` finds drift, so it can gate a deploy.
"""

from __future__ import annotations

import argparse
import os
import sys

# Only the files a browser actually requests. Everything else in storefront/ --
# DEPLOY.md, validate_page.py, the planning notes -- deliberately stays unpublished.
PUBLISHED = ["index.html", "styles.css", "main.js", "catalog.js"]

# Not generated from storefront/, but legitimately present: GitHub itself writes a
# CNAME file into the publishing directory when a custom domain is configured, and
# deleting it takes the custom domain down.
PRESERVED = {"CNAME"}

BANNER = (
    "GENERATED FILE - DO NOT EDIT. Copied from storefront/{name} by "
    "tools/sync_docs.py. Edit storefront/{name} and re-run the script; edits made "
    "here are overwritten."
)

DOCS_README = """\
# docs/ is generated - do not edit these files

This directory is the GitHub Pages publishing root (Settings -> Pages -> Deploy from
a branch -> `main` / `/docs`). Pages can only publish from the repository root or
`/docs`, and the landing page's source lives in [`storefront/`](../storefront/)
together with tooling that should not be published -- so this is a generated copy of
just the files a browser needs.

| File | Source |
|---|---|
| `index.html` | [`../storefront/index.html`](../storefront/index.html) |
| `styles.css` | [`../storefront/styles.css`](../storefront/styles.css) |
| `main.js` | [`../storefront/main.js`](../storefront/main.js) |
| `catalog.js` | [`../storefront/catalog.js`](../storefront/catalog.js) |

**Edit the files in `storefront/`, never the ones here.** Then regenerate:

```bash
python tools/sync_docs.py          # rewrite docs/ from storefront/
python tools/sync_docs.py --check  # exit 1 if docs/ is stale
```

`.nojekyll` disables Jekyll processing, so the files are served exactly as written.

See [`../storefront/DEPLOY.md`](../storefront/DEPLOY.md) for the full deployment
notes.
"""


def rendered(name: str, source: str) -> str:
    """Return the published text for one file, with a generated-file banner."""
    banner = BANNER.format(name=name)
    if name.endswith(".html"):
        # After the doctype, so the very first line of the document stays valid.
        marker = "<!DOCTYPE html>"
        comment = f"<!-- {banner} -->"
        if source.startswith(marker):
            return source.replace(marker, f"{marker}\n{comment}", 1)
        return f"{comment}\n{source}"
    return f"/* {banner} */\n{source}"


def build(repo: str) -> dict:
    """Render every published file. Returns ``{relative path: text}``."""
    out = {"README.md": DOCS_README, ".nojekyll": ""}
    for name in PUBLISHED:
        path = os.path.join(repo, "storefront", name)
        if not os.path.exists(path):
            raise SystemExit(f"missing source file {path}")
        with open(path, encoding="utf-8") as handle:
            out[name] = rendered(name, handle.read())
    return out


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate docs/ (the GitHub Pages root) from storefront/."
    )
    parser.add_argument(
        "--repo",
        default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        help="repository root (defaults to this script's parent directory)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="report whether docs/ matches storefront/ without writing anything",
    )
    args = parser.parse_args(argv)

    docs = os.path.join(args.repo, "docs")
    wanted = build(args.repo)

    if args.check:
        stale = []
        for name, text in sorted(wanted.items()):
            path = os.path.join(docs, name)
            if not os.path.exists(path):
                stale.append(f"{name}: missing from docs/")
                continue
            # Text mode, so a CRLF checkout on Windows is not reported as drift.
            with open(path, encoding="utf-8") as handle:
                if handle.read() != text:
                    stale.append(f"{name}: differs from storefront/")
        extra = []
        if os.path.isdir(docs):
            extra = sorted(set(os.listdir(docs)) - set(wanted) - PRESERVED)
        for name in extra:
            stale.append(f"{name}: in docs/ but not generated by this script")
        for line in stale:
            print(f"[STALE] {line}")
        if stale:
            print("\ndocs/ is out of date -- run: python tools/sync_docs.py")
            return 1
        print(f"docs/ is up to date ({len(wanted)} files)")
        return 0

    os.makedirs(docs, exist_ok=True)
    for name, text in sorted(wanted.items()):
        path = os.path.join(docs, name)
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
        print(f"wrote docs/{name}  ({len(text)} bytes)")
    print(f"\ndocs/ regenerated from storefront/ ({len(wanted)} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
