# Deploying the Landing Page (Free, via GitHub Pages)

The landing page is three static files — `index.html`, `styles.css`, `main.js` — with no
build step, no framework and no server-side code. Any static host will serve it. GitHub
Pages is free and the files already live in this repo, so that is the fastest route.

---

## Before you publish: three edits

Do these first, or you will ship a page with dead buttons.

1. **Paste in your real product URLs.** Open `index.html` and search for `BUY LINK`.
   There are 22 of those comments marking 20 purchase links (18 currently `href="#"`,
   plus 2 that point at the on-page `#free` section). Replace each placeholder `href="#"`
   with the matching Gumroad or Etsy product URL.
2. **Wire up the free-pack signup.** In the `#free` section, either point the `<form>`
   `action` at your email provider's endpoint, or delete the form and replace it with a
   button linking to your Gumroad $0 product. See `SETUP_CHECKLIST.md`.
3. **Fix the canonical URL.** `<link rel="canonical">` and `og:url` in the `<head>` already
   point at the live Pages URL below. Change them only if you move to a custom domain —
   and re-run `tools/sync_docs.py` afterwards.

Once the real links are in, you can delete the two guard blocks at the bottom of
`main.js` (the buy-link `alert()` and the inert-form handler). They exist only so an
unconfigured page fails loudly instead of silently.

---

## This is how the page is published today: `main` + `/docs`

**Live URL: <https://condod.github.io/TI-84-Python-Test-Tools-and-Study/>**

Branch-based Pages will only serve the repository root or `/docs` — there is no way to
point it at `storefront/` and get the page on the bare project URL. So `docs/` is a
**generated copy** of the three files a browser needs (`index.html`, `styles.css`,
`main.js`), plus a `.nojekyll` marker and a README explaining that it is generated.

This needs no GitHub Actions workflow file, which matters if your token lacks the
`workflow` scope — a branch source is configured through the API or the Settings UI.

### ⚠️ Re-run the sync script after every `storefront/` edit

`docs/` does not update itself. If you edit `storefront/index.html` and don't re-run the
script, the live site keeps serving the old page and nothing warns you:

```bash
python tools/sync_docs.py          # regenerate docs/ from storefront/
python tools/sync_docs.py --check  # exit 1 if docs/ is stale (use before pushing)
```

Then commit both directories together. Never hand-edit anything in `docs/` — the next
sync overwrites it, and each generated file carries a "DO NOT EDIT" banner saying so.

A sensible pre-push sequence:

```bash
python storefront/validate_page.py     # structural checks on the page
python tools/sync_docs.py              # publish the current storefront/ into docs/
python tools/sync_docs.py --check      # belt and braces
```

### Configuring Pages (already done, kept here for re-creation)

With the GitHub CLI:

```bash
# First time:
gh api -X POST repos/condod/TI-84-Python-Test-Tools-and-Study/pages \
  -f 'source[branch]=main' -f 'source[path]=/docs'

# Change an existing configuration:
gh api -X PUT repos/condod/TI-84-Python-Test-Tools-and-Study/pages \
  -f 'source[branch]=main' -f 'source[path]=/docs'

# Confirm:
gh api repos/condod/TI-84-Python-Test-Tools-and-Study/pages
```

Or by hand, if the API refuses for permission reasons:

1. Go to <https://github.com/condod/TI-84-Python-Test-Tools-and-Study>.
2. **Settings** (top tab) → **Pages** (left sidebar, under "Code and automation").
3. Under **Build and deployment** → **Source**, choose **Deploy from a branch**.
4. In **Branch**, pick `main`, set the folder dropdown to `/docs`, then **Save**.
5. Wait 1–3 minutes. The Pages panel shows a green "Your site is live at …" banner.
   The build itself appears under the **Actions** tab as `pages build and deployment`.

### Why not just publish the repo root?

You can — see the alternative below — but then the landing page sits at
`/storefront/` and the bare project URL renders `README.md` instead. The `/docs`
arrangement puts the sales page on the shortest URL this repo can have, which is what
you want in a bio link, and keeps `storefront/`'s notes and `validate_page.py`
unpublished.

---

## Alternative — publish the repo root, page lives at `/storefront/`

Zero file copies, and the repo README stays visible as the site root.

1. **Settings** → **Pages** → **Source:** `Deploy from a branch`, **Branch:** `main`,
   folder `/ (root)` → **Save**.

**Resulting URLs**

| What | URL |
|---|---|
| Site root (renders `README.md`) | `https://condod.github.io/TI-84-Python-Test-Tools-and-Study/` |
| **The landing page** | `https://condod.github.io/TI-84-Python-Test-Tools-and-Study/storefront/` |

The pattern is `https://<username>.github.io/<repository-name>/<path>/`. The trailing
slash matters — `/storefront/` serves `storefront/index.html` automatically. If you
switch to this, update the canonical URL and `og:url` in `index.html` to match.

### A note on Jekyll

Pages runs Jekyll by default, which is what turns `README.md` into the site root page.
Jekyll **ignores files and folders whose names start with `_` or `.`**. Nothing in
`storefront/` starts with either character, so the landing page is unaffected. The
generated `docs/` directory sidesteps the question entirely by including an empty
`.nojekyll` file, so its contents are served exactly as written.

---

## Alternative — dedicated `gh-pages` branch, page at the repo root URL

Also gives `https://condod.github.io/TI-84-Python-Test-Tools-and-Study/` with no
`/storefront/` suffix, i.e. the same URL as the `/docs` arrangement above, but with a
second branch to keep in step instead of a generated directory. There is no reason to
switch to this unless you want the repo root to stay a README page on `main`.

```bash
# from a clone of the repo, on main
git checkout --orphan gh-pages
git rm -rf .                        # clear the index; the working tree keeps your files
cp storefront/index.html storefront/styles.css storefront/main.js .
git add index.html styles.css main.js
git commit -m "Publish landing page to gh-pages"
git push -u origin gh-pages
git checkout main
```

Then set **Settings → Pages → Source: Deploy from a branch → Branch: `gh-pages` / `(root)`**.

Result: `https://condod.github.io/TI-84-Python-Test-Tools-and-Study/`

---

## Alternative — a separate repo for the shortest possible URL

Create a repo named exactly `condod.github.io`, put the three files at its root, and
enable Pages on `main`. The site is then served from
`https://condod.github.io/` — no path at all. Only do this if you don't want that
address for anything else; you get one per account.

---

## Verifying it worked

1. Open the URL in a private/incognito window (Pages caches aggressively).
2. Check that the CSS loaded — if you see unstyled black-on-white text, the relative path
   to `styles.css` broke, which usually means you visited the URL without a trailing slash.
3. Click a buy button. If you still get the "Checkout link not configured yet" alert,
   you missed a `href="#"`.
4. Resize the window below ~760px to confirm the mobile menu button appears.
5. Run the URL through Google's Rich Results / mobile-friendly test, or just load it on
   your phone.

From a terminal, the two-second version — status codes and content types for the page and
both assets:

```bash
BASE=https://condod.github.io/TI-84-Python-Test-Tools-and-Study
for f in "" styles.css main.js; do curl -s -o /dev/null \
  -w "%{http_code} %{content_type} $BASE/$f\n" "$BASE/$f"; done
```

Expect `200 text/html`, `200 text/css` and `200 text/javascript`. A 404 on the assets but
not the page means a path problem; a 200 on everything but stale content means you forgot
`python tools/sync_docs.py`.

**If it 404s:** confirm the branch and folder in Settings → Pages (should be `main` and
`/docs`), confirm `docs/index.html` exists and is committed, and check the Actions tab for
a failed `pages build and deployment`. First deploys occasionally take up to 10 minutes.

**If it serves an old version of the page:** `docs/` is stale. Run
`python tools/sync_docs.py --check`, regenerate, commit and push.

---

## Adding a custom domain later

Worth doing before you print the URL anywhere. A `.com` runs roughly $10–15/year at
Namecheap, Porkbun or Cloudflare Registrar. Something like `ti84python.com` or
`calcpytools.com`.

### 1. Point DNS at GitHub

**For an apex domain** (`example.com`) — create four `A` records, all with host `@`:

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

GitHub also publishes AAAA (IPv6) records; add them too if your registrar supports it.
Verify the current addresses at
<https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site>
before relying on them — they have changed historically.

**For a subdomain** (`www.example.com` or `tools.example.com`) — one `CNAME` record:

```
Host: www        Value: condod.github.io
```

A `CNAME` is the more robust choice. If you use the apex, also add the `www` CNAME and
let GitHub redirect between them.

### 2. Tell GitHub about it

**Settings → Pages → Custom domain** → type the domain → **Save**. GitHub commits a
`CNAME` file to the branch you're publishing from. Don't delete it.

> Publishing from `main` + `/docs`, GitHub commits the `CNAME` file into `docs/`. That is
> correct — leave it there. `tools/sync_docs.py` already knows to leave `docs/CNAME`
> alone, so a sync will not delete your custom domain.

### 3. Wait, then force HTTPS

DNS propagation takes anywhere from a few minutes to 24 hours. Once GitHub reports the
domain as verified, tick **Enforce HTTPS** (it stays greyed out until the Let's Encrypt
certificate is issued, typically under an hour).

### 4. Update the page

Change the canonical URL and `og:url` in `index.html` to the new domain, and update the
link you've been sharing.

### Custom domain on the current setup

Nothing extra to do. Publishing from `/docs` already puts the landing page at the
publishing root, so a custom domain serves it at the bare domain — `https://example.com/`,
no `/storefront/` suffix. Just remember step 4 above, and re-run `tools/sync_docs.py`
after changing the canonical URL.

If you ever switch to publishing the repository root instead, the page moves to
`https://example.com/storefront/` and you would need a one-line redirect at the root as
`index.html`:

```html
<meta http-equiv="refresh" content="0; url=/storefront/">
```

---

## Alternatives to GitHub Pages

All free at this traffic level, all take the same three static files:

| Host | Why you'd pick it |
|---|---|
| **Cloudflare Pages** | Fastest global CDN, free custom domain + SSL, connects to the same GitHub repo. Best pick if you outgrow Pages. |
| **Netlify** | Drag-and-drop the `storefront/` folder onto the dashboard and it's live in seconds. Easiest possible deploy, and it has built-in form handling that would take the free-pack email signup with no email provider. |
| **Vercel** | Same idea; strongest if you later turn this into a real app. |

Netlify Forms is worth a look specifically for point 2 in the pre-publish checklist: add
`netlify` as an attribute on the `<form>` and submissions land in your Netlify dashboard
with no third-party email service at all.
