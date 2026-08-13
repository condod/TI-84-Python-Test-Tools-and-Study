# Unit Economics — Pre-Loaded TI-84 Plus CE Python

The money model. Read §7 first if you only read one section.

**Labelling convention:** **[RESEARCHED]** = a figure I found with a citable source, given inline.
**[ESTIMATE]** = my own modelling assumption, not a researched figure. Every number in the P&L is
one or the other and is marked.

---

## 1. Headline answer

| | |
|---|---|
| Realistic acquisition cost, CE Python, blended | **$30–$45** (must be ≤$30 for the model to work) |
| Realistic sale price, refurbished + loaded, eBay | **$85–$95** (hard ceiling: the $95 Walmart back-to-school promo) |
| Realistic net profit per unit at $30 acquisition, $88 sale | **≈ $28** |
| Realistic net profit per unit at $45 acquisition, $88 sale | **≈ $13** |
| All-in labour | **≈ 53 min/unit** at batch scale |
| Effective hourly, good case | **≈ $32/hr** |
| Effective hourly, typical case | **≈ $15–$21/hr** |
| **Honest software premium the market will bear** | **$5–$12. Possibly $0.** |

**The verdict, plainly: the software premium is thin, and it is not what makes this business work
or fail. Acquisition cost is.** A $15 swing in what you pay for the calculator moves per-unit
profit more than doubling the software premium does. Everything else in this document is detail
around that sentence.

---

## 2. Acquisition cost

Full channel detail is in [`SOURCING.md`](SOURCING.md). The economics summary:

| Channel | Realistic per-unit cost, CE Python | Reliability | Notes |
|---|---|---|---|
| eBay, single unit, "untested/as-is" | **$40–$55** [ESTIMATE] | High | Almost no margin left. Use only to fill an order. |
| eBay, multi-unit lots | **$35–$50** [ESTIMATE] | Medium | Lots are usually mixed-model; the Python share is the problem. |
| Facebook Marketplace, negotiated | **$30–$50** [ESTIMATE] | Medium | Best realistic channel for volume at a workable price. |
| OfferUp / Mercari | **$40–$55** [ESTIMATE] | Medium | |
| June end-of-year dumping, any local channel | **$25–$40** [ESTIMATE] | Seasonal | The single best acquisition window. |
| Thrift / pawn | **$15–$40** [ESTIMATE] | Very low | Real, but you cannot plan around it. |
| Government/school surplus lots (GovDeals, PublicSurplus) | **$1–$25/unit** [RESEARCHED — but see caveat] | Low for *this* product | |

**The surplus caveat matters and is easy to get wrong.** Government surplus calculator lots are
genuinely cheap — a 45-unit GovDeals lot in Montvale, NJ closed at **$200 after 37 bids**, about
**$5.00/unit** including the 12.5% buyer's premium
(<https://bidprowl.com/listing/lot-of-calculators-45-nj-govdeals-8869-90>, accessed 2026-08-12). But
read that lot's contents: *"TI-73: 3, TI-30SLR+: 10, TI-30Xa: 2, TI-83: 4, TI-84 Plus (black): 25,
TI-84 Plus Silver Edition: 1."* **Not one CE, and certainly not a CE Python.** School surplus runs a
decade behind retail. The one large *CE* surplus result found — Bryan ISD, 250 units — went for
**$4,750 + 10% ≈ $20.90/unit**, and they were **EZ-Spot school-property editions**, which carry the
provenance and cosmetic problems described in [`SOURCING.md`](SOURCING.md). Treat surplus as a
separate, lower-value bare-resale line, not as the supply chain for the loaded SKU.

**Price anchors, for context** [RESEARCHED]:

- New TI-84 Plus CE Python at Walmart, 2026: listings from **$93.99** (promo, was $149.00) to
  **$149.95**; a plain CE promo at **$87.68** (was $139.00)
  (<https://www.walmart.com/ip/.../55586377>, accessed 2026-08-12). **Re-checked 2026-08-13:** the
  Python-labelled Walmart SKUs now run **$129.98–$149.95**, and the plain-CE promo is still
  **$87.68**. The cheapest new in-stock CE anywhere in the sweep is **$94.99 at Target** — see the
  resolved note below.
- Amazon TI-84 Plus CE listing at **$117.50** (<https://www.amazon.com/dp/B01FY73EI8>, accessed
  2026-08-12).
- Walmart-marketplace third-party "Pre-Owned TI-84 Plus CE Python" **asking** prices: **$113.99–$129.99**.
  These are asking prices from marketplace resellers, not sold comps, and they are high.
- **Amazon Renewed / Certified Refurbished CE: $105–$130**, professionally refurbished with a return
  guarantee. This is the trust-adjusted ceiling on your own pricing — you cannot beat Amazon on buyer
  confidence, so you must beat it on price.

**The single most useful sell-side data point found** [RESEARCHED]: an eBay US multi-quantity listing
of good-condition tested CEs — *"TESTED AND WORKING. 30 DAY WARRANTY. GOOD USED CONDITION"* — priced at
**$79.00 with 354 units sold** and 23 still available, last revised 2025-12-28
(<https://www.ebay.com.au/itm/395431720336>, an AU mirror of the US listing, accessed 2026-08-12).
That is real, repeated sell-through at $79 on a **plain CE with no software**, from a seller offering
a warranty. It is the most credible single anchor in this document, and it brackets the model: a
loaded CE **Python** should clear above it, but not far above it.

**And a hard ceiling to respect:** Walmart's back-to-school promotional pricing puts **new** CE and CE
Python units around **$95**. When that promo is live — which is exactly your peak selling season — a
used unit asking $95 is competing with a new one in a box. Price under it, always.

> ### ✅ Resolved 2026-08-13 — the $95 ceiling is confirmed by a live listing, not a lapsed promo
>
> **This entry previously said the ceiling was "promo-dependent" and might be gone. It is not.** The
> apparent contradiction — $93.99 here versus a $129.98–$134.00 sweep of the same retailers on the
> same day in [`hardware-launch/SOURCING_SHORTLIST.md`](hardware-launch/SOURCING_SHORTLIST.md) §3.2 —
> **was real but was not a disagreement about price. Both figures were correct and were measuring
> different SKUs.**
>
> **The $130+ figures were all Python-*labelled* listings. The sub-$95 figures are plain-CE-*labelled*
> listings — which, per their own buyers, frequently ship as Python units.**
>
> **A new TI-84 Plus CE, in a box, in stock at Target for `$94.99`** (reg $110.59), accessed
> 2026-08-13 [RESEARCHED —
> <https://www.target.com/p/texas-instruments-84-plus-ce-graphing-calculator-black/-/A-82545755>]. The
> listing is not labelled Python and Target's support rep says it isn't — but **four separate
> customers on that page report receiving the Python variant**, one stating plainly that it *"is being
> sold online & instores as Ti-84CE (but it's a python model)."* That is consistent with
> [`SOURCING.md`](SOURCING.md)'s finding that TI's retail channel no longer separates the variants
> cleanly. Full sweep, including the retailers that were bot-gated or out of stock, in
> `SOURCING_SHORTLIST.md` **§3.2a**.
>
> **So `$95` stays, and the reason is now evidence rather than caution.** The old justification was
> *"a promo that lapsed once can return overnight."* The new one is *"there is a live, in-stock,
> $94.99 new-in-box listing that has repeatedly shipped Python units."* **When that is what a buyer
> sees, a used unit asking $95 is competing with a new one — exactly as this section always said.**
>
> **And note what this rules out.** If new really were ~$130, there would be unclaimed headroom above
> the $95 ceiling and the sell-side model would be leaving money on the table. **There isn't.** At the
> A/B test's $90 loaded ask you are already within $5 of new-in-box. No unit-economics figure in this
> document changes, because none of them were relying on the extra room — but the **$18 differential**
> floated for a follow-up test in
> [`hardware-launch/AB_TEST_PROTOCOL.md`](hardware-launch/AB_TEST_PROTOCOL.md) §1.3 would put a
> *used* unit at $96, **above a new one.** Do not run that without re-checking this price first.

**Modelled acquisition cost: $30 (good case) / $45 (typical if you buy one at a time).** [ESTIMATE]

> **The CE Python constraint is the whole sourcing problem.** Only the Python variant runs Python —
> TI: *"Only the Python version of the TI-84 Plus CE graphing calculator has Python programming
> capability."* A plain CE cannot be upgraded; it lacks the ARM coprocessor. So roughly the cheapest
> two-thirds of the used TI-84 market is off the table for the loaded SKU. This is the structural
> reason acquisition cost is high and hard to push down.

---

## 3. Platform fees

### eBay [RESEARCHED]

- Final value fee, most US categories, 2026: **13.6%** of the total sale amount (item + shipping +
  tax), **12.7%** with a Basic Store or higher, plus a per-order fee of **$0.40** (orders over $10)
  or **$0.30** ($10 or less). Payment processing is consolidated into the FVF; there is no separate
  processing charge under managed payments.
  (<https://www.underpriced.app/blog/ebay-seller-fees-2026>,
  <https://www.listing-forge.com/blog/ebay-final-value-fee>, both accessed 2026-08-12.)
  Note the base rate rose from 13.25% to 13.6% for 2026.
- **The FVF applies to sales tax eBay collects as marketplace facilitator.** At a ~7% blended tax
  rate that's an extra ≈**0.95%** of the item price, quietly. [ESTIMATE — the 7% blend is mine.]
- **Promoted Listings — and a 2026 change that makes them worse.** Ad rate is seller-set; eBay's
  *suggested* rates run 8–15% and are optimised for eBay's revenue, while practitioner consensus for
  electronics is **2–4%**. As of January 2026, attribution changed to **any click by any buyer within
  30 days**, whether or not that click caused the sale. One analysis reports attribution rates
  jumping from 30–40% to 80–90% overnight with no lift in volume
  (<https://www.flipsail.io/blog/ebay-promoted-listings-2026>, accessed 2026-08-12). **In practice a
  3% ad rate is now close to a flat 3% tax on nearly all your sales, not a fee on incremental ones.**
  Start at **2%** — which is what's modelled — or skip it entirely and watch what happens to
  impressions.
- International fee 1.65% if applicable — not modelled; ship domestic only.
- **Seller-performance surcharges are real and dangerous at low volume:** Below Standard adds **+6%**
  (rising to +7% after four consecutive months from 2026-07-01), and a Very High INAD rate adds
  **+5%** (rising to +6%). See §6 of [`LISTING_AND_SUPPORT.md`](LISTING_AND_SUPPORT.md) — with a small
  denominator, one or two disputes can trip these.
- **Store subscription:** the Basic Store saves 0.9% of the sale, at **$21.95/mo** billed annually or
  **$27.95** month-to-month. On an $88 unit the saving is **$0.79**, so the store pays for itself at
  about **28–35 units/month**; several independent analyses put the Basic break-even at roughly
  **$2,440/month gross**, which agrees. **The Starter Store ($4.95–$7.95) carries no final-value-fee
  discount at all** — it's a branding product, not a savings one. Stay on a free account with 250
  free listings until you're consistently past ~$2,500/month.
  (<https://www.listing-forge.com/blog/ebay-store-subscription>,
  <https://ecomli.com/blog/ebay-store-subscription-guide>, accessed 2026-08-12.)
- **One thing worth checking yourself before you price anything.** eBay ran a fee restructure around
  2026-07-01 that, in the European marketplaces, introduced a **flat 5% fee on used, refurbished, and
  reconditioned goods.** Sources disagree on whether it reached eBay US — one claims it did and then
  reports the US rate as unchanged at 13.6%, another states plainly that US sellers *"haven't seen
  this exact change hit"* yet (<https://beancount.io/blog/2026/07/28/ebay-seller-fee-overhaul-flat-rate-refurbished-guide>,
  accessed 2026-08-12). **[UNVERIFIED — and it matters more than anything else on this page.]** If a
  5% used-goods rate is live on eBay US, per-unit profit on an $88 sale rises by roughly **$8** and
  the whole channel calculus changes. Pull one real payout statement and back out your actual rate.

**Modelled eBay take: 13.6% + 2% promoted + 0.95% tax drag = 16.55% + $0.40.**

### Mercari [RESEARCHED]

**A flat 10% selling fee** on item price plus buyer-paid shipping. **No listing fee, no per-order
fee, and no seller payment-processing fee** — the old 2.9% + $0.50 processing charge was removed for
listings created or updated after the January fee restructure. Buyers separately pay a ~3.6% Buyer
Protection fee, which does not come out of your payout but does affect what a buyer is willing to
offer. If you offer free shipping, the 10% applies to the item price only, but you pay the label.
(<https://sellerfeecalc.com/mercari-fees>, <https://ecomcalctools.com/blog/mercari-fees/>,
<https://crosslist.com/blog/mercari-seller-fees>, accessed 2026-08-12.)

**This is materially cheaper than eBay** — 10% versus an effective ~16.55% + $0.40. On an $88 free-
shipping sale at $30 acquisition:

| | eBay | Mercari |
|---|---:|---:|
| Platform fees | $14.96 | $8.80 |
| Shipping label | $5.50 | $6.73 |
| **Net** | **$27.99** | **$32.92** |

**Cross-list everything, and prefer the Mercari sale when you get one** — it's about **$5/unit
better**, roughly 18% more profit for identical work. The catch is traffic: Mercari's buyer base for
a specific calculator model is much thinner than eBay's, and the "pre-loaded" story lands less well
with a browse-driven audience. Treat eBay as the demand engine and Mercari as the margin bonus.

### Facebook Marketplace [RESEARCHED]

**Local pickup, cash or Venmo/Zelle: $0.00.** No listing fee, no transaction fee, no subscription.
**Shipped through Marketplace checkout: 10% of the total** (item + shipping + tax), $0.80 minimum —
the rate **doubled from 5% in April 2024**, so any guide still citing 5% is stale. One source adds a
further 2.9% processing on top for ~13% all-in while others describe the 10% as inclusive; treat
shipped FB as **10–13%** and check your payout preview. Also note Facebook **discontinued prepaid
shipping labels for most sellers in February 2025**, so a shipped FB sale means buying your own label.
(<https://www.underpriced.app/blog/facebook-marketplace-fees-2026> — re-verified against Meta's help
text 2026-07-29; <https://www.listing-forge.com/blog/facebook-marketplace-fees>, accessed 2026-08-12.)

**Local sale is by a wide margin the highest-margin channel per unit** — and the lowest-volume one.
The arithmetic is striking: at $30 acquisition, **a $70 local cash sale nets ~$37 against ~$28 for an
$88 eBay sale.** You can price 20% under the shipped market, sell faster, skip the returns risk
entirely because the buyer inspects before paying, and still make more money. If you have access to a
college town, a high-school parent network, or a campus Facebook group, work it hard in August and
January.

### Etsy / Gumroad

Not for hardware. See [`LISTING_AND_SUPPORT.md`](LISTING_AND_SUPPORT.md) §7 and
`COMPLIANCE_RESEARCH.md` §8.4.

---

## 4. Cost stack per unit

| Line | Cost | Basis |
|---|---:|---|
| **Acquisition** | $30.00 / $45.00 | §2 [ESTIMATE] |
| Replacement battery, TI **3.7L1200SPB**, at ~20% incidence × ~$8 | $1.60 | [ESTIMATE]; part number [RESEARCHED] |
| New generic USB A-to-**Mini-B** cable (bulk) | $1.50 | [ESTIMATE]; connector type [RESEARCHED] |
| Replacement slide case, ~15% incidence × ~$6 | $0.90 | [ESTIMATE] |
| Cleaning consumables (IPA, cloths, swabs) | $0.35 | [ESTIMATE] |
| #1 (7.25×12) bubble mailer + cardboard stiffener + tape + label | $0.55 | [RESEARCHED]: kraft bubble mailers run $0.12–$0.36/unit by case size (e.g. Lavex #0 250/case at $33.99 = $0.14/unit, <https://www.webstaurantstore.com/lavex-packaging-self-sealing-kraft-bubble-mailer-0-6-x-10-case/442KBM0S.html>). Stiffener from scrap cardboard, tape ~$0.03, thermal label ~$0.02. |
| Printed quick-start / restore card | $0.25 | [ESTIMATE] |
| **Materials subtotal** | **$5.15** | |
| **Shipping** — USPS Ground Advantage, **12 oz in a bubble mailer**, eBay Labels, contiguous US | **$5.50** | See the sub-pound note below. |
| **Returns / loss reserve** | **5% of sale price** | [ESTIMATE]. Covers INAD returns, return shipping you eat, the occasional unsellable unit, and lost-in-transit. Used electronics on eBay is a higher-return category than average, and the Money Back Guarantee means you carry the risk regardless of your stated policy. |
| **One-time setup** | ~$140 | Cables, powered hub, light/backdrop, scale, initial consumables. [ESTIMATE] Amortises to nothing past ~6 units. |

### Stay under one pound — this is worth ~$1.50/unit

A bare TI-84 Plus CE is **7.59 × 3.42 × 0.8 in and 0.44 lb**. In a bubble mailer with a cable and a
stiffener it packs at **9–12 oz**; in a 9×5×3 box it's 12–15 oz and risks crossing 1 lb. **Use the
mailer.**

The reason this matters in 2026: effective **2026-07-12**, USPS **eliminated the 4/8/12 oz tiers for
published *commercial* Ground Advantage**, pricing all sub-pound commercial packages at the 15.999 oz
rate — roughly an 11.8% increase. Retail prices were unchanged. (USPS Notice 123,
<https://pe.usps.com/text/dmm300/Notice123.htm>; USPS Final Rule,
<https://pe.usps.com/resources/Misc/Final%20Rule%20-%20July%202026%20Domestic%20Competitive%20Products.pdf>;
analysis at <https://transimpact.com/blog/usps-rate-to-increase-ground-advantage-commercial-rates-by-11.8>.)

**But eBay negotiated an exemption that works in your favour.** Per an eBay moderator post of
2026-07-08, reported by EcommerceBytes and ValueAddedResource: the flat-per-zone treatment applies to
rural ZIPs, Alaska, Hawaii, Puerto Rico and military addresses, and *"for the continental United
States, the tiered-weight structure remains in place."*
(<https://www.ecommercebytes.com/2026/07/07/usps-july-rate-changes-impact-sites-like-ebay-differently/>,
<https://www.valueaddedresource.net/ebay-usps-ground-advantage-oz-based-rates/>, accessed 2026-08-12.)
**So eBay Labels still gives you the cheap 8 oz and 12 oz tiers for most of your volume** —
**[ESTIMATE] $4.50–$7.00 by zone, $5.50 blended.** Note Pirate Ship reportedly did *not* apply the
rural exception, so it may beat eBay on some destinations and lose on others.

Mercari is simpler: **flat national rates, no zones** — 8 oz $5.66, **12 oz $6.73**, 1 lb $7.48
(Best Rate, effective 2026-01-20, <https://www.mercari.com/us/help_center/article/632/>). That's
worse than eBay on near zones and better on far ones. Mercari **rounds up to the tier ceiling**, so a
9 oz package pays the 12 oz price — weigh precisely.

**UPS Ground is never the right answer here** — roughly $11–$15 for a 1 lb parcel.

**Not in the cost stack, deliberately:** TI Connect CE (free), the OS bundle (free from TI, and
must not be redistributed — see [`LISTING_AND_SUPPORT.md`](LISTING_AND_SUPPORT.md) §5.1), and the
software itself (already written; marginal cost of copying it is zero).

---

## 5. Labour

From [`PREP_SOP.md`](PREP_SOP.md) §10: **~38 min/unit of bench work at a batch of six.** [ESTIMATE]

Add the work the SOP doesn't cover:

| Activity | Min/unit |
|---|---:|
| Bench prep (SOP §10, batch of 6) | 38 |
| Sourcing: browsing, bidding, negotiating, pickup, unpacking | 10 |
| Post-sale: messages, tracking, records, the occasional support reply | 5 |
| **All-in** | **≈ 53 min = 0.88 h** |

All [ESTIMATE]. Sourcing time is the one most people underestimate — at these price points you are
scanning a lot of listings per unit actually bought.

---

## 6. The software premium — the crux, treated skeptically

This is the question the whole business rests on: **how much more will a buyer pay for the same
calculator because it has your programs on it?**

### What the evidence actually says

**Very little, and none of it encouraging.** I searched for existing "pre-loaded with programs"
calculator listings across marketplaces and found no established market segment with observable
premium pricing. What I did find, repeatedly, is the counter-argument, stated plainly by
third-party guides: TI publishes free program libraries, ticalc.org hosts tens of thousands of
community programs, and a student can load a solver or a unit converter in a couple of minutes with a
USB cable. A refurb guide's framing is that condition, accessories, and battery health drive
used-calculator price; bundled software is listed as something that *"can justify"* a higher price,
with no figure attached
(<https://production.matthewmarks.com/refurbished-ti-84-graphing-calculator/>, accessed 2026-08-12).

> **A source removed from this paragraph, and why.** The "two minutes with a USB cable" phrasing was
> previously quoted from `storycircuit.us/blog/ti-84-plus-ce-comparison/`. **That source has been
> retired across `business/`** — the same article claims Python can be added to a base TI-84 Plus CE
> via a *"$30 add-on module,"* which is false; that adapter is a **TI-83 Premium CE** accessory
> ([`SOURCING.md`](SOURCING.md) §2 has the citations). An article that is wrong about whether the
> base CE can run Python is not a source this document should lean on for anything.
>
> **The argument is unaffected**, which is why the sentence stays: that loading programs yourself is
> easy and free is common knowledge, is directly observable in TI's and ticalc.org's own libraries,
> and is corroborated below by mcstutoring's own buyer instructions, which tell purchasers to
> *"transfer files using TI Connect CE"* themselves.

**The most telling evidence is what the closest competitor doesn't do.** mcstutoring.com — the
established TI-84 program seller this repo already benchmarks against in `bundles/PRICING.md`, run by
someone with *"25+ years of tutoring experience and 30 years of TI-BASIC programming"* — sells
programs at **$20–$60 each** and bundles up to **$160**, and sells them **exclusively as digital
downloads**. Their own instructions tell buyers to *"transfer files using TI Connect CE"* and list
the USB mini cable as something the buyer supplies.
(<https://mcstutoring.com/collections/formula-programs>,
<https://mcstutoring.com/pages/ti-84-plus-ce-calculator-programs-complete-reference-guide>, accessed
2026-08-12.) **They do not sell pre-loaded hardware at any price.** Someone who has spent decades in
this exact niche, and who prices software far more aggressively than this repo does, has evidently
concluded that shipping calculators isn't worth it. That should carry weight.

Etsy's TI-84 hardware listings are likewise bare used calculators — "tested," "with cover," no
software angle (<https://www.etsy.com/market/ti84_calculator>, accessed 2026-08-12).

**[UNVERIFIED]** I was not able to pull live eBay sold-comp data for "preloaded" calculator
listings specifically. The absence of a visible segment is itself weak evidence — if there were an
easy $30 premium here, this category is competitive enough that someone would already be farming it.

**A second, independent research pass reached the same conclusion, and added three arguments worth
recording.** Targeted searches for "loaded with programs," "programs installed," "preloaded formulas"
and similar returned no marketplace listing selling a used TI-84 at a documented premium, no sold-price
differential from any source, and no seller review or reseller guide describing preloading as a
working margin tactic. The additional structural arguments:

1. **Teachers clear memory.** Many instructors reset calculator memory before exams, which vaporises
   the preload on day one. The value you charged for can disappear before the first test.
2. **Modifications read as a liability to the median buyer.** One resale guide puts it directly:
   *"Modifications are often viewed as a liability, meaning original, unmodified units consistently
   maintain the highest resale ceiling"*
   (<https://www.aurascience.blog/values-texas-instruments-ti83-calculator>, accessed 2026-08-12).
3. **It raises your not-as-described exposure rather than lowering it.** A buyer who expected 30
   programs and found 12, or whose teacher wiped them, has a ready-made INAD claim — and §6 of
   [`LISTING_AND_SUPPORT.md`](LISTING_AND_SUPPORT.md) explains why that is disproportionately
   expensive at low volume.

**What the market does pay for is the software on its own.** mcstutoring.com's $20–$60 programs and
$160 bundle sell to people who *already own a calculator*. That is the demonstrated business; loaded
hardware is not.

### The arithmetic your buyer can do

A buyer can purchase a bare used CE Python and the **$49** complete digital toolkit
(`bundles/PRICING.md`) and end up with **all 52 programs** instead of the 8–10 a physical SKU carries.
That puts a nominal ceiling of $49 on the premium — but **do not read the toolkit's repricing from $35
to $49 as licence to charge more.** The ceiling was never the binding constraint; the market evidence
above is, and it still says **$5–$12**. What you're actually selling on top of the bare unit is:

- it's already installed (saves ~20 minutes and a TI Connect CE install),
- every program was launched and checked **on that specific unit**,
- the OS is current,
- there's a printed card and a restore link.

That is a **convenience and assurance** premium, not a software premium. Convenience premiums on
used marketplaces are real but small.

### The number

| Scenario | Premium | My confidence |
|---|---:|---|
| **Skeptical / base case** | **$5–$12** | This is what I'd plan against |
| Optimistic, requires proof | $20–$25 | Possible with excellent photos and a strong niche listing; unproven |
| Zero case | $0 | Genuinely plausible. Many buyers filter on price and condition alone and never read the description. |

**Modelled premium: $10.** Bare unit $78, loaded unit $88.

### The one genuinely good thing about it

The premium is thin in absolute terms but the **marginal labour is also thin** — loading takes about
5 minutes and the extra program verification about 6 more, so ~11 minutes on top of a unit you were
refurbishing anyway.

| Premium | Extra net after fees | Marginal $/hr on 11 min |
|---:|---:|---:|
| $0 | $0.00 | $0 |
| $5 | $3.92 | **$21** |
| $10 | $7.84 | **$43** |
| $15 | $11.77 | **$64** |
| $20 | $15.69 | **$86** |

So: **even at a modest $10 premium, the marginal return on loading the programs (~$43/hr) is
better than the average return on the whole unit (~$30/hr).** If you're already refurbishing the
calculator, loading it is worth doing. What the premium does **not** do is turn a marginal refurb
business into a good one. It is a topping, not the meal.

### How to actually find out — ⚠️ **corrected 2026-08-13: you cannot, not at this scale**

**The design in this section is right and the claim about it was wrong.** It used to end: *"Ten pairs
gives you a real answer."* **Ten pairs does not, and neither does twelve.** The matched-pair design was
built, pre-registered and costed in
[`hardware-launch/AB_TEST_PROTOCOL.md`](hardware-launch/AB_TEST_PROTOCOL.md), and computing its power
properly is what overturned the claim:

| | |
|---|---:|
| Minimum detectable effect at **10 pairs** | **$11.94** |
| Minimum detectable effect at **12 pairs** | **$10.66** |
| **Maximum per-unit difference the design can physically produce** — every unit in both arms selling at full ask | **$10.37** |
| Pairs needed to detect the **$5–$12** premium above at 80% power | **~48** |

**The detection floor sits above the design's own ceiling.** And the arms cannot be spread further
apart to fix it: a new CE is in stock at **$94.99** today and its own buyers report being shipped Python
units (§2 above), so a *used* loaded unit asking much over $90 is competing with new-in-box.

**Three things follow, and none of them is "don't run the test":**

1. **The $5–$12 range in this section stays [ESTIMATE], and its "$0 is genuinely plausible" row stays
   too.** Nothing available this season can promote it to a measurement. Plan against it; do not expect
   to confirm it.
2. **The test has been re-purposed rather than cancelled.** It is now a **harm screen**: its job is to
   catch the loaded arm doing *worse*, and it is genuinely well-powered for that — roughly **80%
   sensitivity against harm of about −$10** at a 5.8% false-stop rate, because **harm is not capped the
   way benefit is.** An unsold loaded unit costs its pair −$61.49 against a +$10.37 upside ceiling.
   §6.3a of the protocol has the derivation.
3. **The decision rule survives untouched, and this section is why.** Its thresholds — **keep loading at
   ≥ +$6, stop at ≤ −$2** — come from **the marginal labour table immediately above**: 11 minutes at $6
   is $32.7/hr, matching the ~$31.80/hr the rest of the refurb work earns; $2 is $10.9/hr, below any
   sensible floor. **Not one term in that derivation involves the sample size or what the test can
   detect.** A rule grounded in opportunity cost does not need rebuilding when the instrument measuring
   it turns out to be blunt.

**So the honest version of this section's advice:** run the matched pairs — same grade, same photos,
same week, one bare, one loaded, **$12 apart** — and read the result as *"is loading hurting me?"*, never
as *"the premium is $X."* **Because loading costs only ~11 marginal minutes, the rational default is to
keep loading unless the data shows harm.** The burden of proof is on stopping, and that is the entire
design.

---

## 7. Per-unit P&L

**Assumptions:** eBay, free shipping to buyer (price includes shipping), no store subscription,
2% promoted, 5% returns reserve, $5.15 materials, $5.50 shipping (12 oz bubble mailer, eBay Labels).

Net = `P × (1 − 0.1655 − 0.05) − $0.40 − $5.50 − $5.15 − acquisition` = `0.7845 × P − 11.05 − acq`

### At $45 acquisition (buying units one at a time)

| Sale price | Fees | Reserve | **Net** | Margin | $/hr @0.88h |
|---:|---:|---:|---:|---:|---:|
| $75 | $12.81 | $3.75 | **$2.79** | 3.7% | $3.17 |
| $85 | $14.47 | $4.25 | **$10.63** | 12.5% | $12.08 |
| **$88** | $14.96 | $4.40 | **$12.99** | 14.8% | **$14.76** |
| $95 | $16.12 | $4.75 | **$18.48** | 19.4% | $21.00 |
| $105 | $17.78 | $5.25 | **$26.32** | 25.1% | $29.91 |

### At $30 acquisition (buying well — lots, local, June)

| Sale price | Fees | Reserve | **Net** | Margin | $/hr @0.88h |
|---:|---:|---:|---:|---:|---:|
| $75 | $12.81 | $3.75 | **$17.79** | 23.7% | $20.21 |
| $78 (bare) | $13.31 | $3.90 | **$20.14** | 25.8% | $22.89 |
| $85 | $14.47 | $4.25 | **$25.63** | 30.2% | $29.13 |
| **$88 (loaded)** | $14.96 | $4.40 | **$27.99** | 31.8% | **$31.80** |
| $95 | $16.12 | $4.75 | **$33.48** | 35.2% | $38.04 |
| $105 | $17.78 | $5.25 | **$41.32** | 39.4% | $46.96 |

### Facebook Marketplace, local pickup, $30 acquisition, $3.00 materials (no mailer or cable-in-box)

| Sale price | **Net** |
|---:|---:|
| $60 | **$27.00** |
| $70 | **$37.00** |
| $75 | **$42.00** |

**Local sale at $70 nets more than an eBay sale at $95.** That is the most important single row in
this document and it is easy to miss. Fees and shipping are ~$21 of an $88 eBay sale; locally they
are zero.

### Break-even sale price

`P_breakeven = (acquisition + $11.05) / 0.7845`

| Acquisition | Break-even sale price |
|---:|---:|
| $20 | $39.58 |
| $30 | $52.33 |
| $45 | $71.45 |
| $55 | $84.19 |

**At $55 acquisition you need $84 just to break even on an eBay sale.** That is inside the realistic
range for a single-unit eBay purchase, which is why single-unit eBay sourcing is not a business —
it's a way to be busy.

### Maximum you can pay

Inverted, for the bench: `max acquisition = 0.7845 × target price − $11.05 − target profit`

| Target sale | Target profit $25 | Target profit $15 |
|---:|---:|---:|
| $85 | pay ≤ **$30** | pay ≤ **$40** |
| $88 | pay ≤ **$32** | pay ≤ **$42** |
| $95 | pay ≤ **$38** | pay ≤ **$48** |

**Print this. Do not exceed it at an auction.**

---

## 8. Sensitivity — the three variables that matter

Net profit at a fixed $88 sale price, by acquisition cost and labour time:

| Acquisition | Net/unit | $/hr @0.6h | $/hr @0.88h | $/hr @1.2h |
|---:|---:|---:|---:|---:|
| $20 | $37.99 | $63.31 | $43.17 | $31.65 |
| $25 | $32.99 | $54.98 | $37.48 | $27.49 |
| **$30** | **$27.99** | $46.64 | **$31.80** | $23.32 |
| $35 | $22.99 | $38.31 | $26.12 | $19.15 |
| $40 | $17.99 | $29.98 | $20.44 | $14.99 |
| **$45** | **$12.99** | $21.64 | **$14.76** | $10.82 |
| $50 | $7.99 | $13.31 | $9.07 | $6.65 |

**Ranked by how much they move the answer:**

1. **Acquisition cost — dominant.** Every $5 you shave is $5 straight to net, and net is only ~$28.
   A $5 saving is an **18%** improvement in per-unit profit. Nothing else in this business has that
   leverage. Buying in June instead of August is worth more than everything in `PREP_SOP.md`
   combined.
2. **Labour minutes — second.** Going from 53 to 36 min/unit takes you from $32/hr to $47/hr with no
   change to price or cost at all. Batching is the lever: six units at a time, OS-flash and charge
   in parallel, one photo session.
3. **The software premium — third, and the least controllable.** $10 of premium is $7.84 of net,
   ~28% of the total. Real, but you don't control whether the market pays it, and the honest base
   case may be closer to $5.

**Not on the list, and worth noting:** shipping cost and platform fees. They're large (~$20 of an
$88 sale) but you can't negotiate them. The only lever there is channel choice — which is why the
local-pickup row in §7 matters so much.

---

## 9. Scale

At $30 acquisition, $88 sale, $27.99 net, 0.88 h/unit:

| Units/month | Gross | Net | Hours | Effective $/hr |
|---:|---:|---:|---:|---:|
| 10 | $880 | **$280** | 8.8 | $31.80 |
| 20 | $1,760 | **$560** | 17.6 | $31.80 |
| 30 | $2,640 | **$840** | 26.4 | $31.80 |
| 50 | $4,400 | **$1,399** | 44.0 | $31.80 |
| 80 | $7,040 | **$2,239** | 70.4 | $31.80 |

**This scales linearly, and that is the problem.** There is essentially no operating leverage: unit
50 costs the same labour as unit 5. Batching improves the constant a bit and then stops. The only
step-changes available are:

- **A Basic Store past ~28–35 units/month** (§3), worth ~$0.79/unit.
- **Bulk acquisition**, which is the real one — if you can find a channel that reliably delivers CE
  Pythons at $20–25, per-unit net goes to $33–38 and the business becomes worth the trouble.
- **Hiring**, which at $31.80/hr gross-of-your-own-labour does not work. You cannot pay someone
  $18/hr to do 53 minutes of work that generates $28 of profit and have anything left.

**The realistic ceiling** is what one person can source and prep seasonally: **[ESTIMATE] roughly
30–60 units across a July–September season**, which is **$840–$1,680** of profit for 26–53 hours.
Real money, but a side project, not a business.

---

## 10. The comparison that matters

| | Loaded calculator | Digital $49 complete toolkit |
|---|---:|---:|
| Revenue | $88.00 | $49.00 |
| Platform fee | $14.96 | $4.90 (Gumroad 10%) |
| COGS | $35.15 | $0.00 |
| Shipping | $5.50 | $0.00 |
| Returns reserve | $4.40 | ~$0.49 |
| **Net** | **$27.99** | **$43.61** |
| **Labour per sale** | **~53 min** | **~0 min** |

**One digital sale nets more than one refurbished, loaded, packed, and shipped calculator, at
essentially zero marginal labour.** The hardware line has to justify itself against that, and on
pure per-transaction economics it cannot.

**And this gap widened sharply.** The complete toolkit was repriced from $35 to **$49** as the library
grew to 52 programs (`bundles/PRICING.md`), which takes the digital net from $31.15 to **$43.61**. One
digital sale now nets **~1.6× a shipped calculator** rather than roughly matching it — a $15.62 gap
where it used to be $3.16. **Nothing about the hardware line got worse; the alternative got much
better.** Every hour you have to allocate should feel that.

It can justify itself two other ways, both real:

1. **Different buyers.** Someone who needs a calculator is not currently a digital-bundle customer.
   The hardware line reaches a market the digital line can't.
2. **Customer acquisition.** Every calculator you ship puts your programs, your card, and your
   restore link in a student's hands. A discount code for the digital toolkit in the box converts
   some fraction of hardware buyers into ~$44-net digital buyers later. **[ESTIMATE]** Even a 10%
   conversion adds **~$4.36** of expected value per unit shipped — **more than half the net value of
   the entire software premium** ($7.84 at the modelled $10), earned for the cost of printing a card.
   At the new $49 toolkit price this is the strongest argument the hardware line has.

---

## 10.5 Platform risk: the CE Python was discontinued in April 2026

This is not priced into anything above, and it should shape how much inventory you're willing to
hold. **[RESEARCHED — see [`SOURCING.md`](SOURCING.md) §0 and
[`EVO_TRANSITION.md`](EVO_TRANSITION.md) for sources.]**

TI discontinued the TI-84 Plus CE Python on **2026-04-27** and launched the **TI-84 Evo** on
**2026-04-28**. The Evo uses USB-C instead of Mini-B and does not use TI Connect CE — it connects
through a web app at `connectevo.ti.com`.

**The compatibility question this section used to hang on is now largely resolved, and resolved in
the product's favour.** Two findings, both [RESEARCHED]:

- **The CE `.8xv` AppVars do not work on an Evo.** Python AppVars there are **`.8xv2`** (TI KB 29430),
  and TI-Toolkit describe the Evo container as "entirely new & non-backwards compatible."
- **The `.py` sources are expected to transfer fine**, because TI Connect Evo auto-converts `.py` on
  send. Eddie Shore, who owns both calculators: *"Python programs can be transferred easily between
  the 84 Python and 84 Evo."* And a static audit of all 52 programs found imports of only `math`,
  `random`, and `time`, with the two TI-proprietary imports guarded by `try/except ImportError` and
  working text fallbacks.

So the phrase that mattered here — "unless the programs are ported" — is the wrong frame. **An "Evo
edition" is hours of packaging plus one hardware verification pass, not a rewrite.** The residual
unknown is narrow: our own test pass on real hardware. Until that exists, make no public Evo
compatibility claim.

Revised effect on the model:

| Horizon | Acquisition cost | Sale price | Net effect |
|---|---|---|---|
| **2026 season (now)** | Flat to slightly up — new stock is draining, so the "just buy new on sale" alternative is weakening | Firm | **Best season this line will have.** Sell into it. |
| **2027–2028** | **Down** — schools and students migrate to the Evo and dump CE Pythons | Down, probably faster than acquisition | Margins compress per unit, **but transaction volume rises**: the transition feeds the used channel this business buys from. Net effect on total profit is ambiguous, not clearly negative. |
| **2029–2030** | Down further; surplus channels finally fill with CE Pythons | Down further | Thinning, harvest-mode. Increasingly a bare-resale commodity business at the hardware end. |
| **Beyond ~2030** | — | — | CE installed base is genuinely shrinking by now. **The software line survives this if it wants to**, because the `.py` sources are platform-portable and the Evo's entire installed base is Python-capable. |

Note what did **not** change: **no figure in §§1–10 above was hedged for Evo risk**, so nothing in the
P&L, break-even, or maximum-bid tables moves. What changes is the *holding-period* judgement and the
verdict language, not the arithmetic.

**One number that does move, in the right direction:** the useful life of the compatibility target.
TI's Evo-T product sheet marks "Continued OS support" as an Evo feature and leaves it blank for the
CE-T Python Edition, so **[INFERRED]** 5.8.5 is likely the terminal CE release. A frozen platform
means the thing your programs must work against stops moving — which slightly *reduces* long-run
support cost per unit sold, at the price of "we update it to the latest OS" ceasing to be an evolving
differentiator.

**Three decisions follow:**

1. **Do not stockpile — but for inventory-turn reasons, not existential ones.** Buy for the season
   you're selling into. The June-buy/August-sell cycle in [`SOURCING.md`](SOURCING.md) §4 is short
   enough to be safe, and capital tied up in calculators earns nothing while prices drift down.
2. **Buy one Evo as R&D, and treat it as an option purchase rather than a threat assessment.** The
   question is no longer "does the product survive." It is "how cheaply can we open a second market
   where every unit is Python-capable, the archives are nearly empty, and C/assembly are locked out so
   Python is the only third-party content channel." That is a **$160 call option on a first-mover
   position**, and it is still the highest-value $160 available to this business.
3. **Lead with the `.py` sources, not the `.8xv` AppVars, everywhere they are described.** The `.py`
   files are the durable, forward-compatible asset and the honest basis for any future Evo claim; the
   `.8xv` files are a CE-specific convenience layer. This costs nothing and it is what keeps the
   digital line's addressable market from being pinned to discontinued hardware.

---

## 11. Tax and admin

- **1099-K threshold, tax year 2026: more than $20,000 in gross payments AND more than 200
  transactions.** Both conditions must be met. The One Big Beautiful Bill Act (signed 2025-07-04)
  permanently restored this (§70432, applying retroactively "as if included in" ARPA); the announced
  $5,000 / $2,500 / $600 phase-in never took effect. Confirmed against the IRS directly: *"third
  party settlement organizations are not required to file Forms 1099-K unless the gross amount of
  reportable payment transactions to a payee exceeds $20,000 and the number of transactions exceeds
  200"* (<https://www.irs.gov/newsroom/form-1099-k-faqs-general-information>, updated 2025-10-23;
  <https://www.irs.gov/instructions/i1099k>, accessed 2026-08-12). [RESEARCHED — primary source]
  Four traps: platforms may issue a form anyway; several states (Maryland, Massachusetts, Vermont,
  Virginia) use $600 or $1,000; **direct card processing through Stripe or a PayPal merchant account
  is a merchant acquirer, not a TPSO, and has no de minimis threshold at all**; and the threshold is
  per-platform, not aggregated.
- **You will not hit that threshold at this volume** — 60 units at $88 is ~$5,300. **Profit is
  taxable from the first dollar regardless of whether a form is issued.** Keep per-unit acquisition
  receipts; the inventory app's cost field is your cost-basis record and it is the difference
  between paying tax on profit and paying tax on gross.
- **Sales tax: essentially a non-issue for you.** All 45 states with a general sales tax, plus DC,
  now have marketplace facilitator laws (Missouri was last, 2023-01-01), so eBay, Mercari, Etsy and
  Facebook collect and remit automatically on facilitated sales
  (<https://nexusbystate.com/guides/marketplace-facilitator-laws>, verified 2026-08-06). Direct and
  local cash sales are your own responsibility under your home state's rules. **Get a home-state
  seller's permit anyway** — it doubles as your resale certificate, letting you buy inventory,
  batteries, and packaging tax-free. Note one fee interaction: eBay charges its final value fee on
  the sales tax it collects, costing you roughly 1.4% of the tax amount.
- Track everything in the inventory app: acquisition cost, channel, refurb spend, sale price, fees,
  shipping. The margin split the app already reports — hardware margin (baseline − acquisition) vs.
  software premium (sale − baseline) — is the right instrumentation for the §6 question **in the long
  run**. **Set `baselinePrice` to your honest bare-unit comp for that grade.**

  > **⚠️ Corrected 2026-08-13. This bullet used to end: *"let the app tell you whether the premium is
  > real. After 20 units you'll have a better answer than any research I can do."* The second sentence
  > is false, and the arithmetic that shows it is now written down.**
  >
  > [`hardware-launch/AB_TEST_PROTOCOL.md`](hardware-launch/AB_TEST_PROTOCOL.md) §6 computes it
  > exactly: **20 units is 10 matched pairs, whose minimum detectable effect is $11.94** — and even the
  > *randomised, matched-pair* version at 12 pairs only reaches **$10.66**, which **exceeds the $10.37
  > maximum difference the design can physically produce.** Measuring a $5–$12 premium at 80% power
  > needs roughly **48 pairs** (§6.4). **An un-randomised running tally in an app is strictly weaker
  > than that**, because it has no control arm at all — every difference in grade, season, photo quality
  > and buyer confounds the comparison.
  >
  > **So the honest instruction is: track it, and do not expect it to answer the question.** The A/B
  > test has been **demoted to a harm screen** for exactly this reason (§0 of that protocol), and the
  > premium range in §6 below stays **[ESTIMATE]** — including its explicit allowance that it may be
  > **$0** — because nothing available this season can move it. **What the app's tally is genuinely good
  > for is spotting a *collapse*, which is the same thing the A/B test is now for.**

---

## 12. Verdict

**The software premium does not justify the labour on its own. The refurb business, done with
disciplined buying, marginally does — and the software is a worthwhile topping on it.**

Concretely:

- **At $45 acquisition and $88 sale, you make $13 a unit for 53 minutes. Don't do that.** That is
  below minimum wage in most states once you count sourcing time.
- **At $30 acquisition and $88 sale, you make $28 a unit, about $32/hr.** That is a real but modest
  side income, and it is contingent on buying well, not on the software.
- **The software adds ~$8 of that $28 — if the market pays the $10 premium at all, which is
  unproven.** The marginal hourly on loading is good (~$43/hr) precisely because the marginal
  labour is small; the absolute dollars are not.
- **The highest-leverage moves, in order:** (1) buy in June, sell in August; (2) buy in lots and
  locally, never one-at-a-time on eBay; (3) sell locally where you can, because $70 local beats $95
  shipped; (4) batch six units at a time; (5) put a digital discount code in every box.
- **If you want to make more money per hour, sell more digital bundles.** One $49 download nets
  **~$44 against ~$28** for a shipped calculator, and takes no time at all — a gap that widened when
  the toolkit was repriced from $35 to $49. Treat the hardware line as a seasonal way to
  convert capital and spare hours into cash, and as a distribution channel for the digital product —
  not as the main event.
- **And know the clock is running — but it is a longer clock than it first looked.** The CE Python was
  discontinued in April 2026 (§10.5), and 2026 is probably the best *season* this line will ever have.
  It is not a two-season business, though: the installed base runs to roughly 2030, the transition
  actually pushes more used units through the channel you buy from, and the `.py` sources are portable
  to the Evo without a rewrite. Sell hard into this August; don't write the line off for 2028.

The recommendation in [`README.md`](README.md) follows from this section.
