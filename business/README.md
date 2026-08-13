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
(~16.5% + $0.40), shipping (~$5.50), materials (~$5.15), and a 5% returns reserve, that nets **≈$28
per unit at $30 acquisition** and **≈$13 at $45** — against about **53 minutes** of all-in labour, so
roughly **$32/hr in the good case and $15/hr in the typical one.** The honest software premium — what
a buyer will actually pay *because* the programs are on it — is **$5–$12, and might be $0.** I found
no evidence of an established market paying a premium for pre-loaded calculators, and a buyer can
always buy a bare unit plus the $49 digital toolkit and get **all 52 programs instead of 8–10.** Be
skeptical of anyone (including yourself) who models this higher.

**So the software premium does not justify the labour on its own.** What does the work is buying
well: the June-to-August price spread on used calculators is worth more per unit than the premium
is, and it costs no labour at all. Acquisition cost is the dominant variable by a wide margin — a $5
change in what you pay moves per-unit profit ~18%, which nothing else in the model comes close to.

Four things sharpen the verdict:

1. **Local sales beat shipped sales, badly.** A $70 Facebook Marketplace pickup nets more than a $95
   eBay sale, because fees and shipping are ~$20 of that eBay sale and $0 locally. If you can sell
   locally, do.
2. **One $49 digital download nets far more than one refurbished, packed, shipped calculator** —
   **$44 vs $28** — at essentially zero marginal labour. **This gap widened materially:** the complete
   toolkit was repriced from $35 to $49 as the library grew to 52 programs, taking the digital net from
   $31 to $44, so what used to be a $3 edge is now a **$16** one. The hardware line cannot win that
   comparison on per-transaction economics and no longer comes close. Its real justification is that it
   reaches buyers the digital line can't, and that every box you ship puts your programs and a discount
   code in a student's hands — worth ~$4.36/unit at a 10% conversion, over half the net value of the
   whole software premium.
3. **The supply pool is closed, but the clock runs longer than it first looked.** TI discontinued the
   TI-84 Plus CE Python on 2026-04-27 and launched the TI-84 Evo the next day — and separately appears
   to have **removed Python from newly manufactured plain CE units** as of early 2026. So every
   Python-capable TI-84 CE that will ever exist was built in a 57-month window that has closed.
   **[RESEARCHED — see [`SOURCING.md`](SOURCING.md) §0.]** The 2026 back-to-school season is probably
   the best this line will ever have, and from 2027 supply rises, prices fall, and margins compress.
   But this is **not a two-season business**: five production years at TI-84 scale is a very large
   installed base, student hardware lives 4–6 years and then gets handed down, and school refresh runs
   on multi-year capital cycles, so the CE Python base stays viable **into roughly 2029–2030**. The
   transition also *feeds* the used-resale channel this business buys from rather than starving it.
   **[RESEARCHED — see [`EVO_TRANSITION.md`](EVO_TRANSITION.md) Q4.]**
4. **The library is not stranded on the CE, which was the one genuinely existential question.** It is
   now largely answered, and answered favourably. The `.8xv` AppVars **definitely do not** transfer to
   an Evo (Python AppVars there are `.8xv2`), but the **`.py` sources are expected to** — TI Connect
   Evo auto-converts them on send — and an audit of all 52 programs found they import only `math`,
   `random`, and `time`, with the two TI-proprietary imports guarded by `try/except ImportError` and
   working text fallbacks. **An "Evo edition" is a packaging change plus one hardware verification
   pass, not a port.** Every Evo ships with Python (there is no separate Python edition any more) and
   C/assembly are locked out, so Python is the *only* third-party content channel on the new platform
   and the Evo Python archives are nearly empty. **[RESEARCHED — see
   [`EVO_TRANSITION.md`](EVO_TRANSITION.md) Q1, Q2, Q5.]** Do not make a public Evo compatibility
   claim until we have tested one.

**Recommended shape of the business:**

- Run it **seasonally**: buy hard from late May through June, prep in July, list from late July
  through mid-September. Don't hold inventory across years.
- Buy **locally and in lots**, never one unit at a time on eBay — at $45+ acquisition the model
  barely clears break-even.
- Keep the loaded SKU, because the **marginal** return on loading (~$43/hr on ~11 extra minutes) is
  better than the average return on the unit — but **run the A/B test** in
  [`hardware-launch/AB_TEST_PROTOCOL.md`](hardware-launch/AB_TEST_PROTOCOL.md) (**twelve** matched
  pairs, bare vs loaded, tracked in
  [`hardware-launch/AB_TEST_LOG.csv`](hardware-launch/AB_TEST_LOG.csv)) and let the data decide,
  rather than assuming the premium exists. **Read §6 of the protocol before you interpret the
  result** — twelve pairs cannot resolve the $5–$12 premium the model expects, and the protocol says
  so plainly.
- **Before you load the second unit, run the hardware gate**
  ([`hardware-launch/AB_TEST_PROTOCOL.md`](hardware-launch/AB_TEST_PROTOCOL.md) §3.5). The `.8xv`
  AppVars have never been executed on a physical calculator. That gate is blocking, and it is the
  cheapest insurance in the whole plan.
- **Put marginal effort into the digital line.** It's higher margin, infinitely scalable, has no
  shipping, no returns, no battery swaps, and — because the `.py` sources are platform-portable — the
  least discontinued-hardware risk of anything here.
- **Buy one TI-84 Evo as R&D — as an option purchase, not a threat assessment.** The question is no
  longer "does the product survive." It's "how cheaply can we open a second market where every unit is
  Python-capable and nobody is publishing yet." One unit at ~$160 converts nearly every remaining
  unknown in [`EVO_TRANSITION.md`](EVO_TRANSITION.md) to verified. **Do not stock Evo units for
  resale** until that test pass is done.

If the goal is maximum money per hour, the honest answer is: **sell digital bundles, and treat
calculators as a seasonal side activity that pays for itself and feeds the digital funnel.**

---

## The documents

| Document | What's in it |
|---|---|
| **[`SOURCING.md`](SOURCING.md)** | Where to buy units and what to pay. Channel-by-channel pricing (eBay, Facebook, OfferUp/Mercari, thrift/pawn, bulk lots, government surplus), the retail price anchors, seasonality, how to tell a CE Python from a plain CE **before** you buy, defect screening, stolen/school-property red flags, and a concrete walk-away price table. |
| **[`UNIT_ECONOMICS.md`](UNIT_ECONOMICS.md)** | The money model. Acquisition, refurb, platform fees, shipping, labour, and a per-unit P&L at several price points and two acquisition costs. A skeptical treatment of the software premium, break-even, maximum-bid maths, sensitivity analysis on the three variables that matter, scaling, the discontinuation risk, and tax/1099-K. |
| **[`PREP_SOP.md`](PREP_SOP.md)** | Step-by-step procedure from acquired unit to sellable unit, mapped to the app's five checklist steps. Includes the critical ordering constraint, bench setup, per-step time estimates, battery replacement, cleaning and cosmetic grading, what goes in the box, and a printable bench card. |
| **[`LOADOUT_STRATEGY.md`](LOADOUT_STRATEGY.md)** | Which programs go on a physical unit, given the 50 KB ceiling. Seven measured loadouts with exact footprints and headroom, per-program sizes, how many SKUs to actually stock, the buyer's-choice option, the archive tier, and how physical SKUs interact with the $12–$19 / $49 digital bundles. |
| **[`LISTING_AND_SUPPORT.md`](LISTING_AND_SUPPORT.md)** | Marketplace titles and description templates, a 12-shot photo list, keyword do/don't, the quick-start card, the Press-to-Test warning and restore-link recommendation, how to tell the three live TI-84 variants apart, the "I have an Evo" support macro, returns policy, platform-by-platform notes, and the legal operating rules (first sale, your own software, and the absolute prohibition on redistributing TI's OS or apps). |
| **[`EVO_TRANSITION.md`](EVO_TRANSITION.md)** | What the April 2026 TI-84 Evo launch and the CE Python discontinuation actually mean. The Evo's Python environment and module set, the `.8xv` → `.8xv2` file-format break, the `connectevo.ti.com` WebUSB transfer tool that replaces TI Connect CE, how long the CE Python installed base stays viable, the first-mover case on the Evo, an import audit of all 52 programs, and the hardware test checklist to run on the first Evo. **Read this before making any compatibility claim about either platform.** |
| **[`hardware-launch/`](hardware-launch/README.md)** | **The tactical layer — start here if you are actually buying units.** A dated, six-week sequence for the 24-unit launch: what to buy and by when, the blocking hardware validation gate, the 12-pair A/B protocol with its pre-committed randomisation and decision rule, paste-ready listing copy, the prep bench, and the committed tracking spreadsheet. Everything above is strategy; this folder is the calendar. |

---

## The four things you must not get wrong

1. **Among CE units, only the CE Python runs Python.** A plain TI-84 Plus CE cannot be upgraded — the
   Python interpreter needs an ARM coprocessor the plain CE doesn't have. Verify the variant from the
   faceplate, the `84CEPY/…` part number, or an on-device `About` screenshot **before every
   purchase**. OS version proves nothing. [`SOURCING.md`](SOURCING.md) §1.1
   **The Evo inverts this** — every TI-84 Evo has Python built in and there is no separate Python
   edition — which is exactly why the model name is no longer a reliable compatibility unit. Sell
   against "does it have the Python app," not against a model number
   ([`LISTING_AND_SUPPORT.md`](LISTING_AND_SUPPORT.md) §1).

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

## Before you commit real money, verify these five things yourself

Every figure in these documents is labelled `[RESEARCHED]`, `[ESTIMATE]`, or `[UNVERIFIED]`. Five of
them are load-bearing enough that you should confirm them personally rather than trust this research,
and each takes minutes:

1. **Your actual eBay final-value-fee rate.** Third-party sources gave 12.35%, 12.7%, 13.25%, and
   13.6% for overlapping descriptions of the same category. Pull one real payout statement and back
   out the rate. The model uses 13.6%.
2. **Whether eBay US has a flat 5% used/refurbished rate.** eBay's July 2026 fee restructure
   introduced one in Europe; sources flatly contradict each other on whether it reached the US. If it
   did, per-unit profit rises by roughly **$8** and the whole verdict above gets more favourable.
3. **Real eBay sold comps.** Run a 90-day sold-listings or Terapeak search for "TI-84 Plus CE Python"
   and build an actual price distribution. This replaces the single best estimate in
   [`UNIT_ECONOMICS.md`](UNIT_ECONOMICS.md) §2 with fact, and it takes fifteen minutes.
4. **Bulk battery pricing at 50–100 units.** The model uses $8; genuine TI cells were found at
   **$6.95–$9.99**, and overseas bulk is plausibly $4–$6. It's your second-largest variable cost.
5. **Whether these programs actually run on a TI-84 Evo.** The desk research says they very probably
   do, unchanged — but that is inference plus one expert's general statement, and **"we tested all 52
   on an Evo" is a different and far more defensible claim than "they should work."** One unit, bought
   once, converts it. Start with `help('modules')` in the Evo Python shell, then send one `.py` via
   `connectevo.ti.com`, then try sending all 52 at once — that last one is the real unknown for a
   pre-loaded-hardware business. Full checklist in [`EVO_TRANSITION.md`](EVO_TRANSITION.md),
   "Strategy" §4.

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
product. TI-84 Plus CE Python™, TI-84 Evo™, TI Connect™ CE, TI Connect™ Evo, and Texas Instruments®
are trademarks of Texas Instruments Incorporated, which is not affiliated with, and does not endorse,
this product. All
trademarks are the property of their respective owners. Exam policies are subject to change; verify
current policy with the relevant exam authority.
