# Pricing Tiers — TI-84 Plus CE Python Toolkit

Suggested USD pricing for the free starter pack, the seven subject bundles, and the
complete 52-program toolkit, grounded in current competitor and general digital-download
pricing research (see "Market Research" below) and in the platform fee maths worked out in
[`../storefront/SETUP_CHECKLIST.md`](../storefront/SETUP_CHECKLIST.md).

## Suggested Prices

| Item | Contents | Suggested Price | Per program |
|---|---|---|---|
| **Free Starter Pack** | 5 programs, one from each of five subjects | **$0** (lead magnet) | — |
| Individual program (à la carte) | 1 `.py` + `.8xv` + mini install note | **$3–$4** | $3–4 |
| **Calculus & Differential Equations** | 6 programs | **$12** | $2.00 |
| **Statistics, Probability & Discrete Math** | 5 programs | **$12** | $2.40 |
| **Biology & Lab Science** | 6 programs | **$12** | $2.00 |
| **Finance & Business Math** | 5 programs | **$12** | $2.40 |
| **Chemistry & Exam Tools** | 7 programs | **$15** | $2.14 |
| **Algebra, Precalculus & Trigonometry** | 11 programs | **$19** | $1.73 |
| **Physics & Engineering** | 13 programs | **$19** | $1.46 |
| **Complete Toolkit** | **All 52 programs** + full master reference guide | **$49** | $0.94 |

### The "buying separately" maths

The seven subject bundles bought individually come to
**$12 + $12 + $12 + $12 + $15 + $19 + $19 = $101**.

The Complete Toolkit at **$49** is therefore a **51% discount** against the sum of the
subject bundles — you save **$52**. Against the à-la-carte anchor (52 programs at $4 each
= $208) it is a 76% discount.

Note that the seven bundles list 53 slots but the library is 52 distinct programs:
`chi_square_genetics.py` sells into both the statistics and the biology bundle. The
Complete Toolkit ships it once.

### Why the discount is 51% and not more

This is the number that had to change. The previous lineup was four subject bundles at
$14 ($56 total) against a $35 toolkit — a 37% discount. Simply keeping $35 while growing
to seven bundles would have implied a **65%** discount against $101, which causes two
concrete problems:

1. **It cannibalises the subject bundles.** If everything costs barely more than two
   subject bundles, nobody buys one subject bundle — and the single-subject buyer is the
   most common buyer, because most students are taking one course that needs this.
2. **It reads as fake anchoring.** A struck-through "$101" next to $35 invites the
   suspicion that the $101 was never a real price. Discounts in this market are credible
   up to roughly half off; past that they signal that the component prices are invented.

At $49 the upgrade ladder works the way it should:

| What the buyer needs | Cheapest bundle route | Complete Toolkit | Rational choice |
|---|---|---|---|
| 1 subject | $12–$19 | $49 | The single bundle |
| 2 subjects | $24–$38 | $49 | Still the bundles |
| 3 subjects | $36–$53 | $49 | Roughly break-even; toolkit wins on breadth |
| 4+ subjects | $48+ | $49 | The toolkit, clearly |

So one- and two-subject buyers are never pushed away from a purchase they were ready to
make, and the toolkit becomes the obvious choice exactly where average order value should
rise. That inflection at three subjects is the design goal, and it is what sets the $49.

### Why prices vary by bundle size

Bundles are not all the same size any more, so a single flat price would either overcharge
for the 5-program statistics bundle or undercharge for the 13-program physics bundle. The
three tiers track size while keeping the per-program price falling as bundles get larger
($2.40 → $1.46 → $0.94), which is the pattern buyers already expect from bundle pricing
and which makes the Complete Toolkit's value self-evident without any struck-through
theatrics.

The tiers stay inside the researched $9–$25 "bundle" band on both platforms, and every
paid item clears the ~$9 floor below which fixed per-transaction fees eat an unreasonable
share of the sale.

## Platform pricing: Etsy vs Gumroad

**Do not reflexively price lower on Etsy.** Earlier guidance here suggested listing 10–20%
below the Gumroad price to absorb Etsy's fees. The fee maths in
[`../storefront/SETUP_CHECKLIST.md`](../storefront/SETUP_CHECKLIST.md) §0 shows that
premise is wrong: **Etsy nets more per unit than Gumroad direct at every price in this
range.**

Using the formulas in that document — Gumroad direct = `price − 0.129 × price − $0.80`,
Etsy = `price − 0.095 × price − $0.45` (listing fee incurred per sale via renewal,
excluding Offsite Ads):

| Price | Gumroad direct nets | Gumroad fee share | Etsy nets | Etsy fee share |
|---|---|---|---|---|
| $12 | $9.65 | 19.6% | **$10.41** | 13.3% |
| $15 | $12.27 | 18.2% | **$13.13** | 12.5% |
| $19 | $15.75 | 17.1% | **$16.75** | 11.9% |
| $49 | $41.88 | 14.5% | **$43.90** | 10.4% |

So the recommendation is to **list at the same price on both platforms**, and treat any
Etsy discount as an audience decision rather than a fee-recovery necessity. If you do want
to test lower Etsy pricing for that marketplace's more impulse-driven traffic, prefer
running Etsy's own time-boxed sales events over a permanently lower price — a sale keeps
the anchor intact and is reversible.

Two standing cautions from the same document:

- **Gumroad Discover can charge 30%.** A $12 bundle sold through Discover nets about
  $7.90. Leave Discover off until the pricing supports it.
- **Etsy Offsite Ads adds up to 15%** on top of the ~13% base stack, which is punishing at
  these price points. Revisit only once a listing is established.

## Rationale

- **Free starter pack → paid funnel.** The free bundle mirrors the funnel pattern used by
  mcstutoring.com ("Free TI-84 Starter Bundle: five essential programs... completely
  free") and is standard practice for digital-download sellers: it costs nothing to
  distribute, builds trust and reviews, demonstrates program quality, and is the natural
  on-ramp to a paid bundle. It is now **5 programs** rather than 3, matching the
  competitor's free tier, and each one is drawn from a different subject so it is useful
  whatever the student is enrolled in. Every program in it also ships inside a paid
  bundle, which is stated openly in its README — buyers are never asked to pay twice for
  the same file.
- **Subject bundles sit in the impulse/considered-purchase sweet spot.** At $12–$19 they
  are inside the "bundle / template" range ($9–$25 on Gumroad, $5–$20 on Etsy) that
  general digital-download pricing research shows converts without an established audience
  or review history. They remain well under mcstutoring.com's exam-specific solver bundles
  ($40–$75 each), which is appropriate: those are marketed as full curriculum-branded
  "solvers," while these are general-purpose calculation tools sold with an explicitly
  non-exam-legality disclaimer. A lower price reflects the narrower, more literal scope
  and sets accurate buyer expectations.
- **Complete Toolkit priced below the sum of its parts, on purpose.** This is the same
  bundle-discount logic the competitor uses (their AP Physics Ultimate Bundle is marketed
  as a "$205 value" for $100 — a 51% discount, the same ratio landed on here; their
  Chemistry Complete Bundle as "$150 value" for $50). Pricing at $49 against $101 gives
  students taking several STEM courses a clear reason to trade up without making the
  individual bundles look pointless.
- **Individual program price ($3–$4)** exists mainly as an anchor that makes the bundles
  look obviously better value (11 programs for $19 vs. $33–$44 à la carte). Most sellers
  in this space report the bulk of revenue comes from bundles rather than singles, and the
  competitor's own "Bundle Value Breakdown" tables use the same technique. Note that $3–4
  is below the ~$9 fee floor, so à-la-carte sales are barely worth fulfilling on their own
  — which is precisely why they work better as an anchor than as a product line.

## Market Research

**Competitor (mcstutoring.com) — exam-specific TI-84 CE program bundles, current pricing:**

| Bundle | Programs | Price |
|---|---|---|
| AP & General Chemistry Complete Bundle (2 semester solvers + 8 support programs) | ~10 | $50 |
| AP & General Chemistry Solver — single semester | 1 | $40 |
| AP Physics 1 Mechanics Solver Bundle (Units 1–8 + bonus programs) | ~7 | $75 |
| Electricity & Magnetism Physics Bundle | 2 | $50 |
| AP Physics Ultimate Bundle (Mechanics + E&M + support programs) | 10 | $100 |
| AP Science Mega Bundle (Physics + Chemistry combined) | 14 | $130 |
| AP STEM Mega Bundle (everything) | ~20+ | $160 |
| Free Starter Bundle | 5 | $0 |

Their model: heavily curriculum-branded ("Units 1–8," "AP-Exam-Legal" marketing), higher
price points per bundle ($40–$160), value-anchored against a much higher struck-through
"if bought separately" price, and a free 5-program starter bundle as the lead magnet.

Worth noting for positioning: their 20+ program "everything" bundle is $160 against our
52-program toolkit at $49. We are not trying to match their price; we are a broader,
cheaper, honestly-described library rather than a narrower curriculum-branded one. Their
"AP-Exam-Legal" framing is exactly the claim
[`../MARKETING_CLAIMS_GUIDE.md`](../MARKETING_CLAIMS_GUIDE.md) documents as inaccurate and
that this project does not make.

**General digital-download / study-tool pricing (Etsy & Gumroad, 2026):**

- Etsy: short guides/tools $3–$15; bundles of multiple items $15–$25; buyers expect
  impulse-buy pricing.
- Gumroad: short guides/tools $5–$19; bundles $15–$40; premium/specialised tools $29–$97.
- Consensus guidance across both platforms: avoid pricing under ~$9 per listing once past
  the free tier, since fixed per-transaction fees eat a large share of very low-priced
  sales; bundle related items to justify a $15–$25 price point.

**Conclusion:** subject bundles at $12/$15/$19 and a complete toolkit at $49 sit inside the
observed ranges for both the direct competitor (scaled down to reflect narrower,
non-curriculum-specific scope and an honest non-"legal-claim" disclaimer) and for general
digital study-tool pricing norms — while keeping the toolkit's discount at a credible 51%
rather than an implausible 65%.
