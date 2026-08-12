# Deploying the Landing Page (Free, via GitHub Pages)

The landing page is three static files — `index.html`, `styles.css`, `main.js` — with no
build step, no framework and no server-side code. Any static host will serve it. GitHub
Pages is free and the files already live in this repo, so that is the fastest route.

---

## Before you publish: three edits

Do these first, or you will ship a page with dead buttons.

1. **Paste in your real product URLs.** Open `index.html` and search for `BUY LINK`.
   There are 16 of those comments marking 14 purchase links (12 currently `href="#"`,
   plus 2 that point at the on-page `#free` section). Replace each placeholder `href="#"`
   with the matching Gumroad or Etsy product URL.
2. **Wire up the free-pack signup.** In the `#free` section, either point the `<form>`
   `action` at your email provider's endpoint, or delete the form and replace it with a
   button linking to your Gumroad $0 product. See `SETUP_CHECKLIST.md`.
3. **Fix the canonical URL.** Update `<link rel="canonical">` and `og:url` in the `<head>`
   to the real address you settle on below.

Once the real links are in, you can delete the two guard blocks at the bottom of
`main.js` (the buy-link `alert()` and the inert-form handler). They exist only so an
unconfigured page fails loudly instead of silently.

---

## Option A — publish from `main`, page lives at `/storefront/`

Simplest, zero file moves. Best if you also want the repo README visible.

1. Go to <https://github.com/condod/TI-84-Python-Test-Tools-and-Study>.
2. **Settings** → **Pages** (left sidebar, under "Code and automation").
3. Under **Build and deployment**:
   - **Source:** `Deploy from a branch`
   - **Branch:** `main`, folder `/ (root)` → **Save**
4. Wait 1–3 minutes for the first build. The Pages panel shows a green
   "Your site is live at …" banner when it's done. You can watch the build under the
   **Actions** tab (`pages build and deployment`).

**Resulting URLs**

| What | URL |
|---|---|
| Site root (renders `README.md`) | `https://condod.github.io/TI-84-Python-Test-Tools-and-Study/` |
| **The landing page** | `https://condod.github.io/TI-84-Python-Test-Tools-and-Study/storefront/` |

The pattern is `https://<username>.github.io/<repository-name>/<path>/`. The trailing
slash matters — `/storefront/` serves `storefront/index.html` automatically.

That URL is long and ugly for a bio link. Use Option B or a custom domain if you plan to
put it in a TikTok bio.

### A note on Jekyll

Pages runs Jekyll by default, which is what turns `README.md` into the site root page.
Jekyll **ignores files and folders whose names start with `_` or `.`**. Nothing in
`storefront/` starts with either character, so the landing page is unaffected. If you
ever add an `_assets/` folder, add an empty `.nojekyll` file at the repo root to switch
Jekyll off — but note that doing so also stops `README.md` being rendered as the site
root, so the root URL would 404.

---

## Option B — dedicated `gh-pages` branch, page at the repo root URL

Gives you the shorter `https://condod.github.io/TI-84-Python-Test-Tools-and-Study/`
with no `/storefront/` suffix. Slightly more work, and you must remember to re-push the
branch whenever you edit the page.

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

## Option C — a separate repo for the shortest possible URL

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

**If it 404s:** confirm the branch and folder in Settings → Pages, confirm the file is
actually named `index.html` (lowercase), and check the Actions tab for a failed build.
First deploys occasionally take up to 10 minutes.

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

> If you're publishing with Option A, the `CNAME` file lands at the repo root, not in
> `storefront/`. That is correct — leave it there.

### 3. Wait, then force HTTPS

DNS propagation takes anywhere from a few minutes to 24 hours. Once GitHub reports the
domain as verified, tick **Enforce HTTPS** (it stays greyed out until the Let's Encrypt
certificate is issued, typically under an hour).

### 4. Update the page

Change the canonical URL and `og:url` in `index.html` to the new domain, and update the
link you've been sharing.

### Custom domain + Option A caveat

With a custom domain on Option A, the landing page is at `https://example.com/storefront/`,
not the bare domain. To serve it at the bare domain, either switch to Option B, or add a
one-line redirect at the repo root as `index.html`:

```html
<meta http-equiv="refresh" content="0; url=/storefront/">
```

That replaces the README-rendered root page, which is a fine trade for a sales site.

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
