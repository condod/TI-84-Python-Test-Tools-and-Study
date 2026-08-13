# Hardware Launch Kit — Start Here

**A two-week sequence to go from zero to a decided answer on whether the pre-loaded calculator line
is a business.**

Created 2026-08-12. Companion to the strategy docs in [`../`](../) — this folder is the tactical
layer.

---

## The one thing this kit is for

**The software premium is unproven.** [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §6 estimates it
at **$5–$12 and explicitly allows that it may be $0.** Loading programs costs ~11 minutes per unit.
If buyers don't pay for it, the correct business is *refurbish and resell bare calculators*, and every
minute spent loading software is a minute wasted.

**Everything in this folder exists to answer that question with 20 calculators and about three weeks,
before you commit real money to the assumption.**

---

## The documents

| Read | For |
|---|---|
| **[`SOURCING_SHORTLIST.md`](SOURCING_SHORTLIST.md)** | How to find and price CE Python units, how to prove the variant before paying, and the walk-away prices. **§1.5 and §6 are the two highest-value sections in this folder.** |
| **[`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md)** | The 10-matched-pair experiment: design, metrics, the decision rule written in advance, and an honest account of what n=10 cannot detect |
| **[`LISTING_TEMPLATES.md`](LISTING_TEMPLATES.md)** | Paste-ready eBay and Mercari copy for both arms, photo shot list, and the compliance boundaries |
| **[`PREP_BENCH.md`](PREP_BENCH.md)** | What to buy to process units, what to skip, total startup cost, and the throughput it supports |

**Read in that order.** Each depends on the previous one's numbers.

⚠️ **Two known gaps, stated up front.** [`SOURCING_SHORTLIST.md`](SOURCING_SHORTLIST.md) §0 explains
that **live eBay comps could not be retrieved** (eBay returns 403 to automated fetches on every
surface, and the sold-comp aggregators are bot-gated). Its price bands are **derived from the existing
repo baselines, not observed 2026-08 transactions** — §2 of that document is a 15-minute manual
routine that fixes this, and **you should run it before spending more than ~$200.**
[`PREP_BENCH.md`](PREP_BENCH.md) §0 flags that most individual equipment prices are estimates. Neither
gap blocks starting.

---

## Week 1 — buy 6, prep 4, ship 2 pairs

**Goal: prove you can do this at all. Not the experiment.**

### Days 1–2 — set up, then buy

```
[ ] Read SOURCING_SHORTLIST.md sections 1, 2 and 6. Tape section 6.2 to the monitor
[ ] Run the 15-minute manual comp routine (SOURCING_SHORTLIST.md section 2).
    Use eBay Terapeak first - it is free with your seller account and it is
    eBay's own data. Write the medians into section 3 of that file
[ ] Buy the five-item minimum from PREP_BENCH.md section 1 (~$38)
[ ] Install TI Connect CE and download the OS *AND APPS* bundle (.b84)
[ ] Set up Facebook Marketplace saved searches and post the WANTED ad
    (SOURCING_SHORTLIST.md section 5)
[ ] Start hunting. Target 6 units at <= $32 each, $40 absolute ceiling
```

> **Ask every seller the §1.5 question:** *"Please open the Python app, type `print(1+1)`, press Run,
> and send me a photo."* A faked unit — a plain CE with an edited certificate — shows Python in the
> app list and opens the editor, and fails **only** when code runs, with the exact string **"Run and
> Shell are not available right now."** This one message is worth more than every price table in this
> folder.

**Why 6 and not 24:** the full test puts **$720–$960 of inventory at risk**
([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §3.1). You have not yet shipped one of these, and the
repo's `.8xv` program files have **never been tested on physical hardware**
([`../PREP_SOP.md`](../PREP_SOP.md) §5). Find that out on unit 1.

### Days 3–5 — prep the pilot pairs

```
[ ] Buy the rest of PREP_BENCH.md section 2.1 as units arrive (~$155 total)
[ ] Read PREP_SOP.md end to end. The order is NOT negotiable:
       wipe -> clear exam mode -> OS+Apps bundle -> load programs -> verify
[ ] Record 1:About OS version on every unit BEFORE flashing
    (5.5-or-older units may be worth more untouched - PREP_BENCH.md 4.4)
[ ] Prep 4 units as 2 pilot pairs: 2 loaded, 2 bare
[ ] Mark all 4 arm = PILOT in the app. They are EXCLUDED from the analysis
[ ] Verify every program on every loaded unit with the known-answer card
    (LISTING_TEMPLATES.md section 7.2)
[ ] Build the photo station and tape the tripod position
```

> **Tape to the wall:** an All-Memory reset **deletes the Python App itself.** A wiped unit boots,
> looks entirely normal, and has no Python until you send the **OS *and Apps*** bundle. And **never**
> enter Press-to-Test after loading — it deletes the AppVars.

### Days 6–7 — list and ship the pilots

```
[ ] Verify each loadout's total bytes <= 34,816 (AB_TEST_PROTOCOL.md 3.4)
[ ] Build the 4 listings from LISTING_TEMPLATES.md. Bare at $78, loaded at $90
[ ] 12 photos each, identical counts and framing across arms
[ ] Weigh every parcel. Target 9-12 oz. Buy labels THROUGH the platform
[ ] Ship, and note what went wrong. Something will
```

**Week 1 gate — do not proceed until all four are true:**

```
[ ] A unit went through all 5 SOP steps without a surprise
[ ] The .8xv programs actually run on real hardware
[ ] A parcel came in at or under 12 oz
[ ] You can build a listing in under 5 minutes from the template
```

**If the `.8xv` files don't run on hardware, stop.** That is a product bug, not a test result, and no
amount of A/B testing fixes it.

---

## Week 2 — commit the batch and launch the test

### Days 8–10 — buy 18 more

```
[ ] Commit ~$500-$600 for 18 more units at <= $32 each
[ ] Re-run the comp routine - prices move weekly in August
[ ] Sell or part out anything that fails intake. A cracked-screen CE Python is
    worth $30-$40 to the repair community (SOURCING_SHORTLIST.md 3.3)
[ ] Generate the pair/arm randomisation sequence BEFORE prepping anything
    (AB_TEST_PROTOCOL.md 2.4)
```

### Day 11 (Aug 23) — FREEZE

```
[ ] Template, photos, prices, thresholds and the randomisation sequence LOCKED
[ ] Nothing changes after today. Write the decision rule down and date it
```

### Days 11–14 — prep 20 for the two drops

```
[ ] Prep in batches of 6, ~38 min/unit (PREP_BENCH.md section 7)
[ ] Match into 10 pairs on: variant, condition grade, cosmetics, accessories,
    battery status (AB_TEST_PROTOCOL.md 2.1)
[ ] Assign arms from the pre-generated sequence. Never by feel
[ ] Log every unit in the app with arm, pair ID, list date, list price
```

Then list in **two drops**, both pairs of every pair going live together
([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §2.5, §5.1):

```
[ ] Drop 1 - Sun Aug 30, 7-9 PM ET: pairs 1-5, 10 listings
[ ] Drop 2 - Sun Sep 6, 7-9 PM ET: pairs 6-10, 10 listings
[ ] Fixed price + Best Offer, 30-day GTC, identical format both arms
```

**Then stop touching them.** No price changes, no relists, no promoted-listing boosts on one arm.
Every mid-test adjustment destroys the comparison.

---

## The decision checkpoint — Oct 21

Run **45 days from drop 2**, then analyse ([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §5).
**Interim look Oct 6 is descriptive only** — the sole permitted early stop is the safety stop in
§5.3 (loaded arm ≤1 of 10 sold while bare ≥6 of 10 by day 30).

**The rule, written in advance so you cannot rationalise afterwards** — measured on **net revenue per
unit *listed***, which counts unsold units as $0 and is the only metric that can't be gamed:

| Δ̂ (loaded − bare) | Decision |
|---|---|
| **≥ +$6.00** | **Keep loading.** Make P6 the default SKU; list at bare + $12 |
| **+$2.00 to +$6.00** | **Inconclusive — lean keep.** Keep loading, drop the differential to +$8, run 10 more pairs |
| **−$2.00 to +$2.00** | **Inconclusive — null.** Keep loading for differentiation (it's 11 minutes) but **price at the bare comp.** Stop modelling a premium |
| **≤ −$2.00** | **Stop loading for price.** Sell bare; push the digital bundles and put a discount card in the box |

**Overriding condition, checked first:** if **loaded sell-through is ≥3 units below bare** (e.g. bare
9/10, loaded 6/10), the verdict is **stop loading at $12 regardless of Δ̂.** A tolerable mean while
inventory sits is hiding a carrying cost the endpoint doesn't price — and unsold stock in October is
worth less than unsold stock in August.

**Why $6 and $2:** loading adds ~11 min/unit. $6.00 works out to **$32.7/hr**, which matches the
~$31.80/hr the rest of the refurb work earns; $2.00 is **$10.9/hr**, below any sensible floor. The
band between them is precisely the range this test cannot resolve, which is why it resolves to "run
more pairs" rather than to a decision.

**Note the default:** because loading is only 11 minutes, the rational stance is **keep loading unless
the test shows harm.** The burden of proof is on stopping.

### Read this before you interpret the result

**n=10 cannot detect the effect you most want to measure.** At the base-case variance, 10 pairs has
roughly **18% power** against a true $5 premium — **a real $5 premium is missed four times out of
five** — and about **62%** against $10. It only becomes reliable at **$15+ (~93%)**, which is *above*
the $5–$12 range [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §6 actually expects. In other words,
**the entire base-case range sits at or below this test's detection threshold**, and confirming a $5
premium would take ~47 pairs.

So a "no difference" result means **absence of evidence, not evidence of absence.**
**[`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §6 covers this honestly — read it before you draw a
conclusion, not after.**

**What n=10 *is* good for:** catching a catastrophe (loaded units performing *worse*), validating the
whole pipeline, and producing a real number to replace an assumption. **Treat it as a screening test,
not a measurement.**

**The trap to avoid:** deciding after 3 pairs because the early ones look good. **Pre-commit to all 10
pairs and the full 45 days.** Watcher and view counts are leading indicators only — never a decision
basis.

---

## Money and timing

| | |
|---|---|
| **To first unit** | **~$38** bench + one calculator |
| **Week 1 (6 units + essential bench)** | **~$380** |
| **Full 24-unit launch** | **~$1,000–$1,240** all-in |
| **Expected return if the premium is real** | ~$28/unit net at $30 acquisition |
| **Expected return if it's $0** | ~$28/unit net on **bare** units, minus 11 wasted min/unit |

⚠️ **You are starting late in the season.** It is August; peak sell-side runs to mid-September, and
the ideal *buy* window (late May–June, 20–35% below average) has passed for this year. Expect to pay
toward the top of the $25–$40 band. **The paired comparison is unaffected** — that is what pairing is
for — but absolute sell-through will look worse than a true August cohort.
**Set a calendar reminder for 2027-05-25.** Buying in June instead of August is worth more than every
efficiency gain in [`../PREP_SOP.md`](../PREP_SOP.md) combined.

---

## Hard rules

Violate these and you lose more than the test is worth.

1. **Never claim FE/PE eligibility.** The TI-84 is **banned outright** by NCEES. This is the one claim
   with genuine liability.
2. **Never market to SAT/PSAT/ACT.** Those exams require programs be removed — you'd be selling a
   product that must be undone to be used.
3. **No "AP-approved" or "AP-legal."** AP permits the calculator; it does not approve your software.
4. **No exam-brand terms in titles, tags, or item specifics** — only inside the explicit *warning*
   block in the loaded description ([`LISTING_TEMPLATES.md`](LISTING_TEMPLATES.md) §5).
5. **Include the Press-to-Test warning on every loaded listing.** Entering exam mode deletes the
   programs. A buyer who loses them will blame you.
6. **Include the trademark/non-affiliation disclaimer** on every listing.
7. **Never buy or sell school-marked units** — EZ-Spot yellow backs, engraving, asset tags.
8. **Never ship a swollen battery**, and never bin a lithium cell.
9. **Never sell a cracked-screen unit as working.** There is no repair path; it is parts only.
10. **Never change a listing mid-test.**

---

## App support — not yet built

The inventory app tracks per-unit variant, OS, serial, bundles, costs, prices and the 5-step prep
checklist, but **cannot currently run this experiment.** It needs an experiment-arm field, a pair ID,
listing/sale date capture for days-to-sale, and a realized-premium report.

**The spec is in [`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §10.** It is a written specification
only — deliberately not implemented, per the scope constraint on this folder.

**Until it exists, log the test in a spreadsheet** using the CSV schema in
[`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §8. **Do not wait on app work to start the test** — the
season is short and a spreadsheet is sufficient for 20 rows.

---

AP®, SAT®, and ACT® are trademarks registered by their respective owners, none of which are affiliated
with, or endorse, this product. TI-84 Plus CE Python™ and Texas Instruments® are trademarks of Texas
Instruments Incorporated, which is not affiliated with, and does not endorse, this product. Nothing in
this document is legal advice.
