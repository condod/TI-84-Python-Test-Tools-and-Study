# Business — Operating Playbook for the Pre-Loaded Calculator Line

Everything needed to run the physical side of this project: buying used TI-84 Plus CE Python units,
preparing them, loading them with the programs in this repo, and selling them.

Research date: **2026-08-12.** Every figure is marked **[RESEARCHED]** (citable source given inline)
or **[ESTIMATE]** (my own modelling). Nothing here is legal, tax, or financial advice.

---

## Executive summary — is this worth doing?

**Qualified yes, but not for the reason you'd hope. Do it as a seasonal buy-low/sell-high refurb
operation with the software as a topping — not as a software business with a calculator attached.**

The numbers, from [`UNIT_ECONOMICS.md`](UNIT_ECONOMICS.md): a used TI-84 Plus CE Python realistically
costs **$30–$45** to acquire and sells refurbished-and-loaded for **$85–$95** on eBay. After fees
(~16.5% + $0.40), shipping (~$6.50), materials (~$5.80), and a 5% returns reserve, that nets **≈$26
per unit at $30 acquisition** and **≈$11 at $45** — against about **53 minutes** of all-in labour, so
roughly **$30/hr in the good case and $13/hr in the typical one.** The honest software premium — what
a buyer will actually pay *because* the programs are on it — is **$5–$12, and might be $0.** I found
no evidence of an established market paying a premium for pre-loaded calculators, and a buyer can
always buy a bare unit plus the $35 digital toolkit and get more programs for less. Be skeptical of
anyone (including yourself) who models this higher.

**So the software premium does not justify the labour on its own.** What does the work is buying
well: the June-to-August price spread on used calculators is worth more per unit than the premium
is, and it costs no labour at all. Acquisition cost is the dominant variable by a wide margin — a $5
change in what you pay moves per-unit profit ~19%, which nothing else in the model comes close to.

Three things sharpen the verdict:

1. **Local sales beat shipped sales, badly.** A $70 Facebook Marketplace pickup nets more than a $95
   eBay sale, because fees and shipping are ~$21 of that eBay sale and $0 locally. If you can sell
   locally, do.
2. **One $35 digital download nets more than one refurbished, packed, shipped calculator** — $31 vs
   $26 — at essentially zero marginal labour. The hardware line cannot win that comparison on
   per-transaction economics. Its real justification is that it reaches buyers the digital line
   can't, and that every box you ship puts your programs and a discount code in a student's hands.
3. **The clock is running.** TI discontinued the TI-84 Plus CE Python on 2026-04-27 and launched the
   TI-84 Evo the next day. Whether these programs run on the Evo is unverified. **[RESEARCHED — see
   [`SOURCING.md`](SOURCING.md) §0.]** The 2026 back-to-school season is probably the best this line
   will ever have; from 2027 supply rises, prices fall, and margins compress.

**Recommended shape of the business:**

- Run it **seasonally**: buy hard from late May through June, prep in July, list from late July
  through mid-September. Don't hold inventory across years.
- Buy **locally and in lots**, never one unit at a time on eBay — at $45+ acquisition the model
  barely clears break-even.
- Keep the loaded SKU, because the **marginal** return on loading (~$43/hr on ~11 extra minutes) is
  better than the average return on the unit — but **run the A/B test** in
  [`UNIT_ECONOMICS.md`](UNIT_ECONOMICS.md) §6 (ten matched pairs, bare vs loaded) and let the data
  decide, rather than assuming the premium exists.
- **Put marginal effort into the digital line.** It's higher margin, infinitely scalable, has no
  shipping, no returns, no battery swaps, and no discontinued-hardware risk.
- **Buy one TI-84 Evo as R&D.** Whether the `.8xv` format and these programs work on it determines
  whether any of this has a future past 2027.

If the goal is maximum money per hour, the honest answer is: **sell digital bundles, and treat
calculators as a seasonal side activity that pays for itself and feeds the digital funnel.**

---

## The documents

| Document | What's in it |
|---|---|
| **[`SOURCING.md`](SOURCING.md)** | Where to buy units and what to pay. Channel-by-channel pricing (eBay, Facebook, OfferUp/Mercari, thrift/pawn, bulk lots, government surplus), the retail price anchors, seasonality, how to tell a CE Python from a plain CE **before** you buy, defect screening, stolen/school-property red flags, and a concrete walk-away price table. |
| **[`UNIT_ECONOMICS.md`](UNIT_ECONOMICS.md)** | The money model. Acquisition, refurb, platform fees, shipping, labour, and a per-unit P&L at several price points and two acquisition costs. A skeptical treatment of the software premium, break-even, maximum-bid maths, sensitivity analysis on the three variables that matter, scaling, the discontinuation risk, and tax/1099-K. |
| **[`PREP_SOP.md`](PREP_SOP.md)** | Step-by-step procedure from acquired unit to sellable unit, mapped to the app's five checklist steps. Includes the critical ordering constraint, bench setup, per-step time estimates, battery replacement, cleaning and cosmetic grading, what goes in the box, and a printable bench card. |
| **[`LOADOUT_STRATEGY.md`](LOADOUT_STRATEGY.md)** | Which programs go on a physical unit, given the 50 KB ceiling. Seven measured loadouts with exact footprints and headroom, per-program sizes, how many SKUs to actually stock, the buyer's-choice option, the archive tier, and how physical SKUs interact with the $14/$35 digital bundles. |
| **[`LISTING_AND_SUPPORT.md`](LISTING_AND_SUPPORT.md)** | Marketplace titles and description templates, a 12-shot photo list, keyword do/don't, the quick-start card, the Press-to-Test warning and restore-link recommendation, returns policy, platform-by-platform notes, and the legal operating rules (first sale, your own software, and the absolute prohibition on redistributing TI's OS or apps). |

---

## The four things you must not get wrong

1. **Only the CE Python runs Python.** A plain TI-84 Plus CE cannot be upgraded — the Python
   interpreter needs an ARM coprocessor the plain CE doesn't have. Verify the variant from the
   faceplate, the `84CEPY/…` part number, or an on-device `About` screenshot **before every
   purchase**. OS version proves nothing. [`SOURCING.md`](SOURCING.md) §1.1

2. **Load the programs LAST.** A full memory reset, entering Press-to-Test, and sending an OS bundle
   all destroy Python AppVars — and the memory reset also removes the Python App itself. The order is
   **wipe → clear exam mode → OS+Apps bundle → programs → verify**, and after the exam-mode step you
   never touch Press-to-Test again on that unit. [`PREP_SOP.md`](PREP_SOP.md) §0

3. **Warn every buyer about Press-to-Test, in the listing, not just the box.** Exam mode deletes the
   programs permanently. A buyer who was warned treats it as expected behaviour; one who wasn't opens
   an "item not as described" case. Ship a free restore link with every unit.
   [`LISTING_AND_SUPPORT.md`](LISTING_AND_SUPPORT.md) §5

4. **Never redistribute TI's software.** You may flash TI's OS onto a calculator you own and are
   servicing. You may not put TI's OS, apps, or manuals on a USB stick, a website, or a download
   link — TI's licence says *"You may not sell, rent or lease copies of the Licensed Materials."*
   The only software that leaves your bench is your own. [`LISTING_AND_SUPPORT.md`](LISTING_AND_SUPPORT.md) §5.1

---

## Exam claims

Everything said about exams in these documents follows
[`../COMPLIANCE_RESEARCH.md`](../COMPLIANCE_RESEARCH.md) and
[`../MARKETING_CLAIMS_GUIDE.md`](../MARKETING_CLAIMS_GUIDE.md) exactly. In short: College Board's AP®
policy is genuinely permissive and does not require clearing calculator memory, and the TI-84 Plus CE
Python is on its approved-calculator list — say that, quoted and sourced. NCEES prohibits the TI-84
outright on the FE/PE, so warn buyers proactively and never market there. SAT®/PSAT and ACT® require
programs to be removed, so never market to those either. Use no exam-brand terms in titles, tags, or
keywords, use no third-party logos, and carry the non-affiliation footer on every surface that names
a mark. If a phrasing isn't on the claims guide's "safe to say" list, don't ship it.

---

AP®, Advanced Placement®, SAT®, and CLEP® are trademarks registered by the College Board, which is
not affiliated with, and does not endorse, this product. PSAT/NMSQT® is a registered trademark of the
College Board and the National Merit Scholarship Corporation, which are not affiliated with, and do
not endorse, this product. ACT® is a registered trademark of ACT Education Corp., which is not
affiliated with, and does not endorse, this product. IB® and International Baccalaureate® are
registered trademarks of the International Baccalaureate Organization, which is not affiliated with,
and does not endorse, this product. NCEES® is a registered trademark of the National Council of
Examiners for Engineering and Surveying, which is not affiliated with, and does not endorse, this
product. TI-84 Plus CE Python™, TI-84 Evo™, TI Connect™ CE, and Texas Instruments® are trademarks of
Texas Instruments Incorporated, which is not affiliated with, and does not endorse, this product. All
trademarks are the property of their respective owners. Exam policies are subject to change; verify
current policy with the relevant exam authority.
