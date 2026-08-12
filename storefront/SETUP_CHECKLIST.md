# Storefront Setup Checklist

Everything needed to go from "files in a repo" to "products people can buy," on Gumroad
and Etsy. Work top to bottom; the shared prep section feeds both platforms.

**Fee figures were checked in August 2026 against the platforms' own published pages and
are cited inline. Verify before you rely on them — both platforms change fees.**

---

## 0. Read this first: the fee maths changes the plan

A widely repeated claim is that Gumroad takes "a flat 10%." That has not been true for
some time. Per [Gumroad's own fee page](https://gumroad.com/help/article/66-gumroads-fees.html):

- **Direct sales** (your own link, your profile, an embedded button): **10% + $0.50**,
  and credit-card processing of **2.9% + $0.30** is charged on top.
- **Gumroad Discover sales** (a buyer found you by browsing Gumroad's marketplace):
  **a flat 30%**, processing included.

Etsy's stack, per [Etsy's Fees & Payments Policy](https://www.etsy.com/legal/fees/):
**$0.20 listing fee** (charged on publish, on renewal, and again each time an item sells),
**6.5% transaction fee**, and **3% + $0.25** payment processing for US sellers.

At our price points that inverts the usual "Gumroad is cheaper" assumption, because both
platforms charge fixed per-transaction fees that bite hardest on cheap products:

| Sale | Gumroad direct | Gumroad Discover | Etsy (US) |
|---|---|---|---|
| $14 subject bundle | keeps **$11.39** (18.6% fees) | keeps $9.80 (30%) | keeps **$12.22** (12.7%) |
| $12 Etsy-priced bundle | — | — | keeps **$10.41** (13.3%) |
| $35 complete toolkit | keeps **$29.68** (15.2%) | keeps $24.50 (30%) | keeps **$31.23** (10.8%) |
| $30 Etsy-priced toolkit | — | — | keeps **$26.70** (11%) |

*(Gumroad direct = price − 0.129 × price − $0.80. Etsy = price − 0.095 × price − $0.45,
assuming the listing fee is incurred per sale via renewal and excluding Offsite Ads.)*

**Three practical consequences:**

1. **Etsy nets more per unit than Gumroad at every price in our range**, despite Etsy's
   reputation as the pricier marketplace. The $12/$30 Etsy pricing in `bundles/PRICING.md`
   still nets slightly less than $14/$35 on Gumroad direct — but Etsy brings its own
   traffic, which Gumroad direct does not.
2. **Don't count on Gumroad Discover.** 30% on a $14 sale leaves $9.80. Discover is a
   discovery channel you pay dearly for; treat any Discover sale as a bonus, and drive
   your own traffic to direct links.
3. **Never price a paid product below about $9 on either platform.** At $5 on Etsy the
   fixed fees alone are ~18.6% of the sale. This is exactly why the à-la-carte $3–4
   single-program tier in `PRICING.md` should stay a price anchor on the landing page
   rather than an actual listing.

---

## 1. Shared prep (do once, before touching either platform)

### 1.1 Assemble the deliverable files

The ZIPs already exist in `bundles/`. Confirm sizes are sane — they are tiny, which means
no platform limit is anywhere close to being a problem:

| File | Size |
|---|---|
| `free_starter_bundle.zip` | 5.3 KB |
| `calculus_bundle.zip` | 8.9 KB |
| `algebra_linear_stats_bundle.zip` | 8.8 KB |
| `physics_engineering_bundle.zip` | 8.8 KB |
| `chemistry_and_exam_tools_bundle.zip` | 10.9 KB |
| `complete_toolkit_bundle.zip` | 37.3 KB |

Etsy allows 5 files per listing at 20 MB each; Gumroad's limits are far higher. Every
bundle fits in a single file slot with room to spare.

- [ ] Open each ZIP and confirm the install README and the exam-policy disclaimer are inside.
- [ ] Confirm filenames are lowercase, no spaces. (Etsy caps filenames at 70 characters
      and allows only letters, numbers, periods, underscores and hyphens.)
- [ ] Decide now whether you're also shipping `.8xv`/calculator-native versions — if the
      conversion work in `tools/` lands, re-zip and re-upload before launch rather than
      after, so early buyers don't get a stale file.

### 1.2 Make the listing images

This is the single highest-leverage thing on this page. On Etsy in particular, the
thumbnail decides whether anyone reads your title. You need, per product:

- [ ] **Main image (1:1, at least 2000 px on the short side, under 1 MB, JPG).** A photo of
      an actual TI-84 Plus CE with a program running on screen beats any mockup. Take it
      yourself with a phone on a plain desk in daylight. If you cannot photograph the
      device, do a clean graphic: bundle name, "6 programs," a screenshot of the program
      output, and the TI-84 CE silhouette.
- [ ] **Image 2 — the contents list.** All six filenames with a one-line description each.
      Buyers zoom in on this.
- [ ] **Image 3 — a real screen capture** of one program's output. Authenticity sells here.
- [ ] **Image 4 — the install path**, three panels: unzip → TI Connect CE → run on device.
- [ ] **Image 5 — the compatibility card.** "Works: TI-84 Plus CE Python Edition. Does not
      work: TI-83, TI-84 Plus (monochrome), TI-Nspire, Casio." This one prevents refunds
      and one-star reviews more than it prevents sales.
- [ ] **A short video/GIF** if you have one — Etsy allows a 5–15 s video and it measurably
      lifts conversion. Point a phone at the calculator and run a program.

Reuse the same image set across both platforms.

### 1.3 Write the copy once

`bundles/LISTING_COPY.md` already has ready-to-paste titles, descriptions and
"what's included" blocks for all six products. Keyword-optimised titles and tag sets are
in `SEO_KEYWORDS.md`. Use those rather than writing fresh copy per platform.

- [ ] Every listing states the compatibility line (CE Python Edition only).
- [ ] Every listing states the format line (plain-text `.py` in a ZIP).
- [ ] Every listing carries the exam-policy disclaimer. **Do not** write "AP-exam-legal,"
      "exam approved," "allowed on the AP exam," or anything equivalent, anywhere.

> **Run everything past [`MARKETING_CLAIMS_GUIDE.md`](../MARKETING_CLAIMS_GUIDE.md) before you
> publish.** It is the repo's sourced "safe to say / do not say" reference, and its §8
> pre-publish checklist is the authoritative version of the claim rules summarised here. Two
> items from it materially affect this checklist: the ready-to-paste storefront disclaimer in
> its §5.1, and the trademark rule that **exam-brand terms must not appear in tags, keywords
> or meta tags** — which is why `SEO_KEYWORDS.md` strips them out of the tag sets that
> `bundles/LISTING_COPY.md` currently suggests.

- [ ] Include the Press-to-Test backup warning in every listing and every ZIP README. A student
      who enters exam mode and loses the programs they just paid for is your most likely refund
      request, and it is entirely preventable with one sentence.

---

## 2. Gumroad

Best for: the free lead magnet, email capture, follow-up automation, and being the
destination you send your own traffic to. Worst for: passive discovery.

### 2.1 Account

- [ ] Sign up at <https://gumroad.com>. Free, no monthly fee.
- [ ] Pick a username — it becomes your URL, `https://USERNAME.gumroad.com`. Choose
      something you'd say out loud in a video: `ti84python`, `calcpytools`.
- [ ] Complete payout settings: bank details or PayPal, plus the tax/identity information
      Gumroad requires before it will release money. **Do this on day one** — payouts are
      held until it's complete, and the verification can take days.
- [ ] Set your profile bio and avatar. One line: what you sell, for which calculator.

### 2.2 The free starter bundle (build this product first)

This is the top of the funnel and the reason to be on Gumroad at all.

- [ ] **New product** → type **Digital product**.
- [ ] Name: `Free TI-84 Plus CE Python Starter Pack — 3 Programs`
- [ ] Pricing: set the amount to **$0** and enable **"Allow customers to pay what they
      want."** Setting a $0 minimum with an optional suggested price of $3–5 means the
      pack is genuinely free, you still capture the email, and a meaningful minority of
      people will pay anyway.
- [ ] Upload `free_starter_bundle.zip`.
- [ ] Description: use the Free Starter Bundle copy from `LISTING_COPY.md`. End with a
      line pointing at the paid bundles.
- [ ] **Content tab:** add a short rich-text section above the download with the three
      install steps, so buyers see instructions without unzipping anything.
- [ ] Turn OFF "Require customers to enter a shipping address."
- [ ] Under **Checkout**, keep the email field required — that's the whole point.
- [ ] Publish and buy your own copy in an incognito window to confirm the download works.

### 2.3 The five paid products

Repeat for each of the four subject bundles ($14) and the complete toolkit ($35):

- [ ] New digital product, title from `LISTING_COPY.md`, price set, ZIP uploaded.
- [ ] Set a memorable custom permalink: `/l/ti84-calculus`, `/l/ti84-physics`,
      `/l/ti84-algebra-stats`, `/l/ti84-chemistry`, `/l/ti84-complete`. These are the URLs
      you paste into `index.html`.
- [ ] Add the cover images from step 1.2.
- [ ] Add a **thumbnail** (600×600) — it's a separate field from the cover and Gumroad
      uses it in emails and Discover.
- [ ] In **Content**, put the install guide as rich text above the file, same as the free
      product.
- [ ] Add tags — see `SEO_KEYWORDS.md`. Gumroad's tag field is free-text; tags feed
      Discover categorisation.
- [ ] **Decide on Discover.** Toggling a product into Discover exposes it to Gumroad's
      marketplace but means Gumroad *may* charge 30% on those sales. Recommendation: leave
      the complete toolkit in Discover (30% of $35 still nets $24.50 from a buyer you'd
      never have reached) and keep the $14 bundles out, where 30% hurts proportionally more.
- [ ] Set up **cross-sells / upsells**: on each $14 bundle checkout, offer the $35 complete
      toolkit as an upgrade. Gumroad supports this natively and it is the easiest average-
      order-value win available.
- [ ] Create a **version/variant** if you end up shipping both `.py` and `.8xv` formats —
      one product, two files, rather than two listings.

### 2.4 Email follow-up (Gumroad Workflows)

Gumroad Workflows send automated emails to buyers of a given product. This is how the
free pack turns into revenue.

- [ ] **Workflow 1 — free-pack nurture.** Trigger: purchase of the free starter pack.
      Three emails; the drafts are written for you in `DEMO_SCRIPTS.md`.
      - Email 1, immediately: the download + install help.
      - Email 2, day 3: a genuinely useful tip, plus a soft mention of the paid bundles.
      - Email 3, day 7: a time-limited discount code on the complete toolkit.
- [ ] **Workflow 2 — post-purchase.** Trigger: purchase of any paid bundle. One email at
      day 2 asking how the install went and inviting a reply with bugs or requests.
      Replies are your product roadmap and your review source.
- [ ] Create a discount code for the workflow: **Discounts** → new code, e.g. `STARTER25`
      for 25% off, capped in redemptions and expiring in 7 days.
- [ ] Under **Settings → Emails**, confirm the "receipt" email is branded and not blank.

### 2.5 Gumroad policy notes for this product category

- Gumroad explicitly welcomes software and educational digital products; calculator
  programs are unremarkable there.
- What could actually get you in trouble is marketing, not the files: framing the product
  as a way to beat an exam. Keep the honest study-aid positioning and the disclaimer.
- Gumroad handles VAT/sales tax collection where required, but you're responsible for
  your own income tax reporting. Export the sales CSV each quarter.
- Refunds: Gumroad returns its own 10% + $0.50 on a refunded sale but the payment
  processor's cut is not returned. Budget for that rather than being surprised by it.

---

## 3. Etsy

Best for: passive discovery — real buyers searching "ti 84 programs" with a credit card
already on file. Worst for: margins on cheap items, and the audience skews more
price-sensitive and less technical.

### 3.1 Shop setup

- [ ] Create a seller account at <https://www.etsy.com/sell>. Etsy requires identity and
      bank verification; allow a couple of days.
- [ ] Shop name: keyword-adjacent and pronounceable, e.g. `CalcPyTools`, `TI84PythonLab`.
      You get one free rename later, so don't agonise.
- [ ] Set the shop to **digital items only** — no shipping profiles needed.
- [ ] **Shop policies** (Settings → Policies). Write these before your first sale:
      - Digital delivery: instant download, no physical shipment.
      - **Returns:** state plainly that digital downloads are non-refundable once
        downloaded. Etsy's own policy treats downloaded digital items as an accepted
        exception to returns; being explicit prevents disputes.
      - Support: promise a 24–48 h reply to messages, and mean it.
- [ ] **Shop announcement:** one line naming the calculator explicitly. Half of Etsy
      digital-download shoppers are not technical and need to be told what this is.
- [ ] **About section:** who you are and why the programs exist. Genuine and specific
      beats polished. No invented credentials.

### 3.2 Create the listings

Do **five paid listings** (4 subject bundles + complete toolkit). Consider a sixth $0
listing for the free pack only if you want the traffic — see 3.4.

For each:

- [ ] **Listing type:** Digital → **Instant download**. Upload the ZIP (one file slot used).
- [ ] **Title:** 140-character limit. Front-load the terms buyers actually type. Use the
      titles in `SEO_KEYWORDS.md` rather than the prettier ones on the landing page —
      Etsy titles are search inputs, not headlines.
- [ ] **Category:** Etsy has no perfect fit. The usual choices are
      *Craft Supplies & Tools → Digital → Templates*, or *Paper & Party Supplies →
      Paper → Educational*. Pick the one whose existing listings look most like study
      materials and stay consistent across your shop.
- [ ] **Tags: exactly 13, and use all 13.** Each is capped at 20 characters, multi-word
      phrases allowed and preferred. Sets are pre-written in `SEO_KEYWORDS.md`. Empty tag
      slots are the most common Etsy SEO mistake.
- [ ] **Attributes/materials:** fill anything offered; they're free extra indexed text.
- [ ] **Description:** first two lines are what shows above the fold and what Google
      indexes — put the calculator model and the program count there. Then the
      "what's included" list, install steps, compatibility, exam disclaimer.
- [ ] **Price:** the $12 / $30 Etsy pricing from `PRICING.md` is a reasonable read of the
      audience, but note from the fee table above that Etsy nets more per unit than
      Gumroad even at $14/$35. Consider launching at $14/$35 to match the landing page —
      consistent pricing across channels avoids awkward questions — and discounting via
      Etsy sales events instead of a permanently lower price.
- [ ] **Renewal:** manual vs. automatic. Automatic renews at $0.20 every four months; with
      a handful of listings that is trivial and you should leave it on.
- [ ] **Offsite Ads:** under $10k in annual sales you can opt out. Opt out at launch — the
      15% fee on top of the ~13% base stack is brutal at $14. Revisit once a listing is
      proven. (Above $10k/year in Etsy sales, participation becomes mandatory at 12%.)

### 3.3 Fees to actually expect

- $0.20 per listing when you publish, again every four months, and again each time an
  item sells.
- 6.5% transaction fee on the displayed price.
- 3% + $0.25 payment processing (US bank account; rates vary by country).
- Etsy collects and remits VAT on digital sales to buyers in certain countries; it shows
  separately in your payment account and isn't yours to keep.
- Budget roughly **11–13%** of revenue at our price points, 15%+ if you leave Offsite Ads on.

### 3.4 The free bundle on Etsy — probably don't

Etsy has no $0 price point; the minimum listing price is $0.20. Options:

- **Recommended:** don't list the free pack on Etsy. Keep the free funnel on Gumroad and
  the landing page. Instead, put a line in each Etsy listing description and in your shop
  announcement pointing to the landing page for a free sample. Etsy does not love outbound
  links in listings, so keep it low-key and don't put a URL in the title.
- **Alternative:** list a $1–2 "sampler." It filters for intent and earns you reviews
  cheaply, but the fixed fees eat about half of it and it forfeits the email capture,
  which is the actual point of a lead magnet.

Etsy deliberately makes buyer emails hard to use for marketing — you cannot export a
mailing list. This is the structural reason Gumroad owns the free tier and Etsy owns
discovery.

### 3.5 Etsy policy considerations for study tools

- Etsy permits digital study materials. What is prohibited is content that deceives or
  facilitates fraud — Etsy's Prohibited Items Policy names things like falsified
  qualifications and fraudulent test results.
- **The risk here is entirely about how you describe it.** A listing that says "get the
  answers on your AP exam" invites a takedown and possible suspension. A listing that
  says "practice and homework tools for the TI-84 Plus CE, check your exam's calculator
  policy" is an ordinary educational digital product. Keep the disclaimer visible in the
  listing body, not just in the ZIP.
- Sell only your own original code. Do not include anything copied from a textbook,
  another seller's programs, or a course's materials.
- Note that Etsy's Prohibited Items Policy was updated with an effective date of
  **11 August 2026** — re-read the current version at <https://www.etsy.com/legal/prohibited/>
  before you publish, since the version cited here may have just been superseded.
- Do not use "TI-84," "Texas Instruments" or "TI Connect" in your *shop name* — using
  another company's trademark as your brand invites an IP complaint. Using them
  descriptively in listing titles and tags ("programs for TI-84 Plus CE") is normal
  nominative use and is what every seller in this niche does. Keep a "not affiliated with
  Texas Instruments" line in the description, as the landing page footer does.

---

## 4. Connect the pieces

- [ ] Paste all five paid product URLs into `index.html` (search `BUY LINK`).
- [ ] Point the free-pack form or button at the Gumroad free product.
- [ ] Deploy the landing page (see `DEPLOY.md`) and put its URL in the Gumroad profile,
      the Etsy shop announcement, and every social bio.
- [ ] Add the landing page URL to the repo's GitHub "About" sidebar.
- [ ] Set up basic analytics so you know which channel works: Gumroad shows views and
      conversion per product natively; Etsy Stats shows search terms that led to visits —
      that second one is free keyword research, check it weekly and feed it back into
      `SEO_KEYWORDS.md`.
- [ ] Buy one of your own paid products end to end on each platform. Check the receipt,
      the download, the file contents, and the follow-up email actually arrive.

---

## 5. First-week sanity checks

- [ ] Does a stranger, reading only the listing thumbnail and title, understand which
      calculator this needs? (Ask someone. This is the number-one refund cause.)
- [ ] Does the exam disclaimer appear in the listing, in the ZIP's README, and on the
      landing page?
- [ ] Is there a working reply-to email address on every automated message?
- [ ] Have you handled the first support question within 24 hours? Early responsiveness is
      what produces the first reviews, and reviews are what make Etsy's algorithm show you
      to anyone.
