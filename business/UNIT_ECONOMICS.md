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
| Realistic sale price, refurbished + loaded, eBay | **$85–$95** |
| Realistic net profit per unit at $30 acquisition, $88 sale | **≈ $26** |
| Realistic net profit per unit at $45 acquisition, $88 sale | **≈ $11** |
| All-in labour | **≈ 53 min/unit** at batch scale |
| Effective hourly, good case | **≈ $30/hr** |
| Effective hourly, typical case | **≈ $13–$20/hr** |
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
genuinely cheap — an aggregator's records show a 45-unit GovDeals lot in Montvale, NJ bid at $34
(<https://bidprowl.com/listing/lot-of-calculators-45-nj-govdeals-8869-90>, accessed 2026-08-12),
which is well under $1/unit. But read that lot's contents: *"TI-73: 3, TI-30SLR+: 10, TI-30Xa: 2,
TI-83: 4, TI-84 Plus (black): 25, TI-84 Plus Silver Edition: 1."* **Not one CE, and certainly not
a CE Python.** School surplus runs a decade behind retail. You will buy monochrome TI-84 Plus units
at pennies and you will not get the hardware this product needs. Treat surplus as a separate,
lower-value bare-resale line, not as the supply chain for the loaded SKU.

**Price anchors, for context** [RESEARCHED]:

- New TI-84 Plus CE Python at Walmart, 2026: listings from **$93.99** (promo, was $149.00) to
  **$149.95**; a plain CE promo at **$87.68** (was $139.00)
  (<https://www.walmart.com/ip/.../55586377>, accessed 2026-08-12).
- Amazon TI-84 Plus CE listing at **$117.50** (<https://www.amazon.com/dp/B01FY73EI8>, accessed
  2026-08-12).
- Walmart-marketplace third-party "Pre-Owned TI-84 Plus CE Python" **asking** prices: **$113.99–$129.99**.
  These are asking prices from marketplace resellers, not sold comps, and they are high.

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
- Promoted Listings: seller-set, typically **2–8%**. Practically mandatory in a competitive category
  if you want placement. Modelled at **2%**. [ESTIMATE]
- International fee 1.65% if applicable — not modelled; ship domestic only.
- **Store subscription:** the Basic Store saves 0.9% of the sale. On an $88 unit that's **$0.79**,
  so a ~$27.95/month Basic Store pays for itself at about **35 units/month**. Below that, no store.
  [Calculation mine; the 0.9% delta is RESEARCHED, the $27.95 price point is [ESTIMATE] — verify
  eBay's current tier pricing before subscribing.]

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
| Fees | $14.96 | $8.80 |
| **Net** | **$26.34** | **$32.50** |

**Cross-list everything, and prefer the Mercari sale when you get one** — it's about **$6/unit
better**, roughly 23% more profit for identical work. The catch is traffic: Mercari's buyer base for
a specific calculator model is much thinner than eBay's, and the "pre-loaded" story lands less well
with a browse-driven audience. Treat eBay as the demand engine and Mercari as the margin bonus.

### Facebook Marketplace [RESEARCHED, directionally]

Local, cash, in-person: **no platform fee, no shipping cost, no payment processing.** Shipping-enabled
Facebook sales carry a selling fee and payment processing. **Local sale is by a wide margin the
highest-margin channel per unit** — and the lowest-volume one.

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
| Box, bubble, label, tape | $1.20 | [ESTIMATE] |
| Printed quick-start / restore card | $0.25 | [ESTIMATE] |
| **Materials subtotal** | **$5.80** | |
| **Shipping** — USPS Ground Advantage, ~1 lb, blended zones, eBay label | **$6.50** | [RESEARCHED]: commercial Ground Advantage ~$7.61 (near zones) to ~$10.67 (far), retail $9.55–$12.90, effective 2026-07-12; eBay label pricing runs meaningfully below commercial, ~$4.50–$6.10 for 1 lb per one reseller guide. $6.50 is a conservative blend. (<https://idshipthat.app/how-much-to-ship/1-lb-package/>, <https://atoship.com/blog/usps-ground-advantage-ebay-resellers-guide>, accessed 2026-08-12) |
| **Returns / loss reserve** | **5% of sale price** | [ESTIMATE]. Covers INAD returns, return shipping you eat, the occasional unsellable unit, and lost-in-transit. Used electronics on eBay is a higher-return category than average, and the Money Back Guarantee means you carry the risk regardless of your stated policy. |
| **One-time setup** | ~$140 | Cables, powered hub, light/backdrop, scale, initial consumables. [ESTIMATE] Amortises to nothing past ~6 units. |

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
community programs, and *"a student can load a polynomial solver, a Riemann sum visualizer, or a
unit converter in about two minutes with a USB cable"*
(<https://storycircuit.us/blog/ti-84-plus-ce-comparison/>, accessed 2026-08-12). A refurb guide's
framing is that condition, accessories, and battery health drive used-calculator price; bundled
software is listed as something that *"can justify"* a higher price, with no figure attached
(<https://production.matthewmarks.com/refurbished-ti-84-graphing-calculator/>, accessed 2026-08-12).

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

### The arithmetic your buyer can do

A buyer can purchase a bare used CE Python and the **$35** complete digital toolkit
(`bundles/PRICING.md`) and end up with **more programs** than any physical SKU carries. So the
absolute ceiling on the premium is $35, and the realistic value is well below it, because what
you're actually selling on top of the bare unit is:

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

### How to actually find out

Stop guessing and run the test. **List matched pairs:** same grade, same photos, same week — one
bare, one loaded, priced $10–$15 apart. Ten pairs gives you a real answer. If loaded units sell no
faster and no dearer, you've learned the most valuable thing in this document, and you should stop
loading and sell bare units instead.

---

## 7. Per-unit P&L

**Assumptions:** eBay, free shipping to buyer (price includes shipping), no store subscription,
2% promoted, 5% returns reserve, $5.80 materials, $6.50 shipping.

Net = `P × (1 − 0.1655 − 0.05) − $0.40 − $6.50 − $5.80 − acquisition` = `0.7845 × P − 12.70 − acq`

### At $45 acquisition (buying units one at a time)

| Sale price | Fees | Reserve | **Net** | Margin | $/hr @0.88h |
|---:|---:|---:|---:|---:|---:|
| $75 | $12.81 | $3.75 | **$1.14** | 1.5% | $1.29 |
| $85 | $14.47 | $4.25 | **$8.98** | 10.6% | $10.21 |
| **$88** | $14.96 | $4.40 | **$11.34** | 12.9% | **$12.88** |
| $95 | $16.12 | $4.75 | **$16.83** | 17.7% | $19.12 |
| $105 | $17.78 | $5.25 | **$24.67** | 23.5% | $28.04 |

### At $30 acquisition (buying well — lots, local, June)

| Sale price | Fees | Reserve | **Net** | Margin | $/hr @0.88h |
|---:|---:|---:|---:|---:|---:|
| $75 | $12.81 | $3.75 | **$16.14** | 21.5% | $18.34 |
| $78 (bare) | $13.31 | $3.90 | **$18.49** | 23.7% | $21.01 |
| $85 | $14.47 | $4.25 | **$23.98** | 28.2% | $27.25 |
| **$88 (loaded)** | $14.96 | $4.40 | **$26.34** | 29.9% | **$29.93** |
| $95 | $16.12 | $4.75 | **$31.83** | 33.5% | $36.17 |
| $105 | $17.78 | $5.25 | **$39.67** | 37.8% | $45.08 |

### Facebook Marketplace, local pickup, $30 acquisition, $3.00 materials (no shipping box or cable-in-box)

| Sale price | **Net** |
|---:|---:|
| $60 | **$27.00** |
| $70 | **$37.00** |
| $75 | **$42.00** |

**Local sale at $70 nets more than an eBay sale at $95.** That is the most important single row in
this document and it is easy to miss. Fees and shipping are ~$21 of an $88 eBay sale; locally they
are zero.

### Break-even sale price

`P_breakeven = (acquisition + $12.70) / 0.7845`

| Acquisition | Break-even sale price |
|---:|---:|
| $20 | $41.68 |
| $30 | $54.43 |
| $45 | $73.55 |
| $55 | $86.30 |

**At $55 acquisition you need $86 just to break even on an eBay sale.** That is inside the realistic
range for a single-unit eBay purchase, which is why single-unit eBay sourcing is not a business —
it's a way to be busy.

### Maximum you can pay

Inverted, for the bench: `max acquisition = 0.7845 × target price − $12.70 − target profit`

| Target sale | Target profit $25 | Target profit $15 |
|---:|---:|---:|
| $85 | pay ≤ **$29** | pay ≤ **$39** |
| $88 | pay ≤ **$31** | pay ≤ **$41** |
| $95 | pay ≤ **$37** | pay ≤ **$47** |

**Print this. Do not exceed it at an auction.**

---

## 8. Sensitivity — the three variables that matter

Net profit at a fixed $88 sale price, by acquisition cost and labour time:

| Acquisition | Net/unit | $/hr @0.6h | $/hr @0.88h | $/hr @1.2h |
|---:|---:|---:|---:|---:|
| $20 | $36.34 | $60.56 | $41.29 | $30.28 |
| $25 | $31.34 | $52.23 | $35.61 | $26.11 |
| **$30** | **$26.34** | $43.89 | **$29.93** | $21.95 |
| $35 | $21.34 | $35.56 | $24.25 | $17.78 |
| $40 | $16.34 | $27.23 | $18.56 | $13.61 |
| **$45** | **$11.34** | $18.89 | **$12.88** | $9.45 |
| $50 | $6.34 | $10.56 | $7.20 | $5.28 |

**Ranked by how much they move the answer:**

1. **Acquisition cost — dominant.** Every $5 you shave is $5 straight to net, and net is only ~$26.
   A $5 saving is a **19%** improvement in per-unit profit. Nothing else in this business has that
   leverage. Buying in June instead of August is worth more than everything in `PREP_SOP.md`
   combined.
2. **Labour minutes — second.** Going from 53 to 36 min/unit takes you from $30/hr to $44/hr with no
   change to price or cost at all. Batching is the lever: six units at a time, OS-flash and charge
   in parallel, one photo session.
3. **The software premium — third, and the least controllable.** $10 of premium is $7.84 of net,
   ~30% of the total. Real, but you don't control whether the market pays it, and the honest base
   case may be closer to $5.

**Not on the list, and worth noting:** shipping cost and platform fees. They're large (~$21 of an
$88 sale) but you can't negotiate them. The only lever there is channel choice — which is why the
local-pickup row in §7 matters so much.

---

## 9. Scale

At $30 acquisition, $88 sale, $26.34 net, 0.88 h/unit:

| Units/month | Gross | Net | Hours | Effective $/hr |
|---:|---:|---:|---:|---:|
| 10 | $880 | **$263** | 8.8 | $29.93 |
| 20 | $1,760 | **$527** | 17.6 | $29.93 |
| 30 | $2,640 | **$790** | 26.4 | $29.93 |
| 50 | $4,400 | **$1,317** | 44.0 | $29.93 |
| 80 | $7,040 | **$2,107** | 70.4 | $29.93 |

**This scales linearly, and that is the problem.** There is essentially no operating leverage: unit
50 costs the same labour as unit 5. Batching improves the constant a bit and then stops. The only
step-changes available are:

- **A Basic Store past ~35 units/month** (§3), worth ~$0.79/unit.
- **Bulk acquisition**, which is the real one — if you can find a channel that reliably delivers CE
  Pythons at $20–25, per-unit net goes to $31–36 and the business becomes worth the trouble.
- **Hiring**, which at $29.93/hr gross-of-your-own-labour does not work. You cannot pay someone
  $18/hr to do 53 minutes of work that generates $26 of profit and have anything left.

**The realistic ceiling** is what one person can source and prep seasonally: **[ESTIMATE] roughly
30–60 units across a July–September season**, which is **$800–$1,600** of profit for 26–53 hours.
Real money, but a side project, not a business.

---

## 10. The comparison that matters

| | Loaded calculator | Digital $35 complete toolkit |
|---|---:|---:|
| Revenue | $88.00 | $35.00 |
| Platform fee | $14.96 | $3.50 (Gumroad 10%) |
| COGS | $35.80 | $0.00 |
| Shipping | $6.50 | $0.00 |
| Returns reserve | $4.40 | ~$0.35 |
| **Net** | **$26.34** | **$31.15** |
| **Labour per sale** | **~53 min** | **~0 min** |

**One digital sale nets more than one refurbished, loaded, packed, and shipped calculator, at
essentially zero marginal labour.** The hardware line has to justify itself against that, and on
pure per-transaction economics it cannot.

It can justify itself two other ways, both real:

1. **Different buyers.** Someone who needs a calculator is not currently a digital-bundle customer.
   The hardware line reaches a market the digital line can't.
2. **Customer acquisition.** Every calculator you ship puts your programs, your card, and your
   restore link in a student's hands. A discount code for the digital toolkit in the box converts
   some fraction of hardware buyers into ~$31-net digital buyers later. **[ESTIMATE]** Even a 10%
   conversion adds ~$3 of expected value per unit shipped — which is a third of the entire software
   premium, earned for the cost of printing a card.

---

## 10.5 Platform risk: the CE Python was discontinued in April 2026

This is not priced into anything above, and it should shape how much inventory you're willing to
hold. **[RESEARCHED — see [`SOURCING.md`](SOURCING.md) §0 for sources.]**

TI discontinued the TI-84 Plus CE Python on **2026-04-27** and launched the **TI-84 Evo** on
**2026-04-28**. The Evo has Python, but it uses USB-C instead of Mini-B, does not use TI Connect CE
(it connects via a web tool), and its compatibility with CE `.8xv` Python AppVars is
**[UNVERIFIED]**.

Effect on the model:

| Horizon | Acquisition cost | Sale price | Net effect |
|---|---|---|---|
| **2026 season (now)** | Flat to slightly up — new stock is draining, so the "just buy new on sale" alternative is weakening | Firm | **Best season this business will have.** Sell into it. |
| **2027** | **Down** — schools and students migrate to the Evo and dump CE Pythons | Down, probably faster than acquisition | Margins compress. Volume may rise. |
| **2028+** | Down sharply; surplus channels finally fill with CE Pythons | Down sharply | Bare-resale commodity business. The software line probably doesn't survive it unless the programs are ported. |

**Two decisions follow:**

1. **Do not stockpile.** Buy for the season you're selling into. Inventory in this category now has a
   declining half-life, and the June-buy/August-sell cycle in [`SOURCING.md`](SOURCING.md) §4 is
   short enough to be safe.
2. **Find out whether the programs run on the Evo, soon.** If they do, the product has a future and
   the whole thesis extends. If they don't, the hardware line has roughly a two-season runway and
   the digital line needs a port. One Evo, bought as R&D, answers this — and it is the highest-value
   $160 you can spend on this business.

---

## 11. Tax and admin

- **1099-K threshold, tax year 2026: more than $20,000 in gross payments AND more than 200
  transactions.** Both conditions must be met. The One Big Beautiful Bill Act (signed 2025-07-04)
  permanently restored this; the $600 threshold never took effect.
  (<https://jupid.com/blog/ebay-1099-k-seller-tax-guide-2026>,
  <https://www.webgility.com/blog/ebay-tax-reporting>, accessed 2026-08-12.) [RESEARCHED]
  Some states (e.g. Massachusetts, Virginia) have lower thresholds.
- **You will not hit that threshold at this volume** — 60 units at $88 is ~$5,300. **Profit is
  taxable from the first dollar regardless of whether a form is issued.** Keep per-unit acquisition
  receipts; the inventory app's cost field is your cost-basis record and it is the difference
  between paying tax on profit and paying tax on gross.
- **Sales tax:** eBay, Mercari, and Facebook (shipping-enabled) collect and remit as marketplace
  facilitators. Local cash sales are your own responsibility per your state's rules.
- Track everything in the inventory app: acquisition cost, channel, refurb spend, sale price, fees,
  shipping. The margin split the app already reports — hardware margin (baseline − acquisition) vs.
  software premium (sale − baseline) — is exactly the right instrumentation for the §6 experiment.
  **Set `baselinePrice` to your honest bare-unit comp for that grade, and let the app tell you
  whether the premium is real.** After 20 units you'll have a better answer than any research I can
  do.

---

## 12. Verdict

**The software premium does not justify the labour on its own. The refurb business, done with
disciplined buying, marginally does — and the software is a worthwhile topping on it.**

Concretely:

- **At $45 acquisition and $88 sale, you make $11 a unit for 53 minutes. Don't do that.** That is
  below minimum wage in most states once you count sourcing time.
- **At $30 acquisition and $88 sale, you make $26 a unit, about $30/hr.** That is a real but modest
  side income, and it is contingent on buying well, not on the software.
- **The software adds ~$8 of that $26 — if the market pays the $10 premium at all, which is
  unproven.** The marginal hourly on loading is good (~$43/hr) precisely because the marginal
  labour is small; the absolute dollars are not.
- **The highest-leverage moves, in order:** (1) buy in June, sell in August; (2) buy in lots and
  locally, never one-at-a-time on eBay; (3) sell locally where you can, because $70 local beats $95
  shipped; (4) batch six units at a time; (5) put a digital discount code in every box.
- **If you want to make more money per hour, sell more digital bundles.** One $35 download nets more
  than one shipped calculator and takes no time at all. Treat the hardware line as a seasonal way to
  convert capital and spare hours into cash, and as a distribution channel for the digital product —
  not as the main event.
- **And know the clock is running.** The CE Python was discontinued in April 2026 (§10.5). This is
  probably the best season this line will ever have.

The recommendation in [`README.md`](README.md) follows from this section.
