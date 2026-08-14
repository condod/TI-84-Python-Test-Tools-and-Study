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
