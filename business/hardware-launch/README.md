# Hardware Launch Kit — Start Here

**A six-week sequence to go from zero to a decided answer on whether the pre-loaded calculator line
is a business.**

Created 2026-08-12. **Rewritten 2026-08-13** for the owner's decision to buy all **24 units up front**
in a buy window that closes **Aug 24**, rather than run a 6-unit pilot first. Companion to the
strategy docs in [`../`](../) — this folder is the tactical layer.

---

## The one thing this kit is for

**The software premium is unproven.** [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §6 estimates it
at **$5–$12 and explicitly allows that it may be $0.** Loading programs costs ~11 minutes per unit.
If buyers don't pay for it, the correct business is *refurbish and resell bare calculators*, and every
minute spent loading software is a minute wasted.

**Everything in this folder exists to answer that question with 24 calculators and about ten weeks,
before you commit real money to the assumption.**

---

## The documents

| Read | For |
|---|---|
| **[`SOURCING_SHORTLIST.md`](SOURCING_SHORTLIST.md)** | How to find and price CE Python units, how to prove the variant before paying, and the walk-away prices. **§1.5 and §6 are the two highest-value sections in this folder.** |
| **[`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md)** | The 12-matched-pair experiment: design, metrics, the decision rule written in advance, **the blocking hardware gate in §3.5**, and an honest account of what n=12 cannot detect |
| **[`AB_TEST_LOG.csv`](AB_TEST_LOG.csv)** | **The tracking sheet.** Pre-filled: 24 rows, 12 pairs, arm assignments already randomised and committed |
| **[`TRACKING_SHEET_NOTES.md`](TRACKING_SHEET_NOTES.md)** | How to fill the sheet, and how to compute the verdict by hand in a spreadsheet |
| **[`HW_VALIDATION.md`](HW_VALIDATION.md)** | Where the §3.5 hardware gate result gets recorded. **Currently empty — filling it in is task one** |
| **[`LISTING_TEMPLATES.md`](LISTING_TEMPLATES.md)** | Paste-ready eBay and Mercari copy for both arms, photo shot list, and the compliance boundaries |
| **[`PREP_BENCH.md`](PREP_BENCH.md)** | What to buy to process units, what to skip, total startup cost, and the throughput it supports |

**Read the first two in that order before spending anything.**

⚠️ **Two known gaps, stated up front.** [`SOURCING_SHORTLIST.md`](SOURCING_SHORTLIST.md) §0 explains
that **live eBay comps could not be retrieved** (eBay returns 403 to automated fetches on every
surface, and the sold-comp aggregators are bot-gated). Its price bands are **derived from the existing
repo baselines, not observed 2026-08 transactions** — §2 of that document is a 15-minute manual
routine that fixes this, and **you should run it before spending more than ~$200.** That matters more
now than it did under the pilot plan: you are about to commit the whole budget in twelve days.
[`PREP_BENCH.md`](PREP_BENCH.md) §0 flags that most individual equipment prices are estimates. Neither
gap blocks starting.

---

## ⚠️ Read this before the sequence: what buying 24 at once costs you

The kit previously recommended **6 units first** (2 pilot pairs + spares) precisely so that the things
below could be discovered cheaply. **The decision to buy 24 up front is being executed as instructed,
and it is defensible** — the buy window really does close Aug 24, the season really is short, and the
units really are inventory you were going to buy anyway. But four risks changed shape, and pretending
otherwise would make this document useless.

| Risk | What the pilot did about it | What now stands in its place |
|---|---|---|
| **The `.8xv` programs have never run on hardware** | Found out on unit 1 for ~$38 of exposure | **[`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §3.5 — the blocking gate.** Only one unit gets loaded until all ten P6 programs run correctly. **This is not optional and it is the single most important item in this document** |
| **First-timer mistakes in prep, photos, packing, shipping** | 4 throwaway units, listed outside the experiment | **Nothing, honestly.** The first pair you prep is inside the experiment. Mitigation is in the sequence below: prep one pair slowly, weigh the parcel, build the listing as an unpublished draft, fix what's wrong. It recovers most of the value but not all |
| **Paying too much, in a window with no comp data** | 6 units of exposure while you learned the market | **$720–$960 committed in twelve days on price bands the kit itself labels underived.** Run the §2 comp routine **first**, today, before the third purchase |
| **Buying 24 and yielding fewer pairs than expected** | Would have been discovered at 6 | **Unchanged and unavoidable.** §3.1 of the protocol computes it: 24 units yields **9–11 pairs**, not 12 |

**And the statistical point that the extra units do not fix.** The protocol's §6 was recomputed at
n=12 and the conclusion held: **12 pairs still cannot detect the $5–$12 premium this whole business
plan is built on.** Going from 10 pairs to 12 moved the minimum detectable effect from $11.94 to
$10.66 — **$1.28.** Buying 24 units instead of 20 did not buy a measurement; it bought inventory
sooner and removed the pilot. Both of those may be the right call. Neither is a statistical
improvement, and **you should not read a 24-unit test as more conclusive than a 20-unit one.**

---

## Week 1 (Aug 13–19) — comps, bench, and the gate unit

**Goal: get one unit in hand fast and prove the software runs on it.**

### Day 1 (today, Aug 13) — before you buy anything

```
[ ] Read SOURCING_SHORTLIST.md sections 1, 2 and 6. Tape section 6.2 to the monitor
[ ] Run the 15-minute manual comp routine (SOURCING_SHORTLIST.md section 2).
    Use eBay Terapeak first - it is free with your seller account and it is
    eBay's own data. Write the medians into section 3 of that file.
    ** DO THIS BEFORE THE THIRD PURCHASE. You are committing $720-$960 in
       twelve days against price bands the kit labels as underived. **
[ ] Buy the five-item minimum from PREP_BENCH.md section 1 (~$38)
[ ] Install TI Connect CE and download the OS *AND APPS* bundle (.b84)
[ ] Set up Facebook Marketplace saved searches and post the WANTED ad
    (SOURCING_SHORTLIST.md section 5)
```

### Days 1–3 — get ONE unit in hand, locally if at all possible

```
[ ] Buy the GATE UNIT first, and buy it LOCAL if you can - Facebook
    Marketplace, OfferUp, thrift. A local pickup lands in 1-2 days;
    an eBay order lands in 3-7.
[ ] Everything else can be online. This one should not be.
```

> **Why the gate unit's arrival date is the tightest constraint in the whole plan.** The **loadout
> freezes Aug 23** ([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §5.1). If the gate finds one broken
> program, substituting it out of P6 is legitimate — **but only before Aug 23.** So the gate needs to
> run by about **Aug 20** to leave room for a fix and a re-run. Working back through 3–7 days of
> shipping, **an online order placed later than ~Aug 15 is too late to be the gate unit.** Buy locally
> this week.

### Days 3–5 — RUN THE GATE

```
[ ] AB_TEST_PROTOCOL.md section 3.5, in full. All ten P6 programs.
[ ] Each program: launches, accepts input, correct known answer, exits cleanly
[ ] Send QUAD BOTH ways (.8xv and .py). The comparison localises any fault
[ ] Photograph TRIG and SIMPSON on-screen (TRIG has no qa/ coverage at all)
[ ] Record every result in HW_VALIDATION.md
[ ] Write hw_gate_status / hw_gate_date / payload_format into AB_TEST_LOG.csv
```

> **Tape to the wall:** an All-Memory reset **deletes the Python App itself.** A wiped unit boots,
> looks entirely normal, and has no Python until you send the **OS *and Apps*** bundle. And **never**
> enter Press-to-Test after loading — it deletes the AppVars.

**The gate is blocking. Until it reads PASS, exactly one unit has programs on it.**

- **If only `.8xv` fails** → fall back to `.py` on all 12 loaded units, re-run the gate, carry on. No
  schedule impact. [`../PREP_SOP.md`](../PREP_SOP.md) §5 already calls `.py` the default and the
  validated path.
- **If both formats fail** → **the loaded arm is blocked.** Sell all 24 units bare, record
  `exclusion_reason = HW_GATE_FAILED`, and **do not report it as an A/B result.** The experiment did
  not run. Your capital is fine — bare resale was always the fallback business.

### Days 3–7 — buy the rest, and start prepping what arrives

```
[ ] Target 24 units total at <= $32 each, $40 absolute ceiling
[ ] Ask EVERY seller the section 1.5 question (below). It is worth more than
    every price table in this folder
[ ] Log every purchase into AB_TEST_LOG.csv Pass 1 the day you buy
[ ] As units arrive: SOP steps 1-3 (wipe, exam clear, OS+Apps) and step 5
    (clean and grade). These are NOT blocked by the gate - only loading is
[ ] Sell or part out anything that fails intake. A cracked-screen CE Python is
    worth $30-$40 to the repair community (SOURCING_SHORTLIST.md 3.3)
```

> **Ask every seller the §1.5 question:** *"Please open the Python app, type `print(1+1)`, press Run,
> and send me a photo."* A faked unit — a plain CE with an edited certificate — shows Python in the
> app list and opens the editor, and fails **only** when code runs, with the exact string **"Run and
> Shell are not available right now."** This one message is worth more than every price table in this
> folder.

---

## The buy deadline is not Aug 24 — it is ~Aug 19 for half the batch

**This is the scheduling problem the 24-unit decision creates, and it needs stating plainly.**

Drop 1 is **Sun Aug 30**. To list 6 matched pairs that evening, all 12 of those units must be
**graded** — because pairs cannot be formed until every candidate has a grade
([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §2.4 stage 2) — and then prepped. Working backwards:

```
Aug 30  Drop 1 lists                        <- fixed
Aug 26-29  prep 12 units (6.7 bench hours)   <- comfortable
Aug 26  HARD CUTOFF: all Drop 1 units in hand, graded, paired
Aug 19-20  latest online order date          <- 3-7 day shipping
```

**So the effective purchase deadline for Drop 1 inventory is around Aug 19–20, not Aug 24.** Units
bought Aug 21–24 will arrive Aug 24–31 and realistically make **Drop 2 only** (Sep 6 needs them in
hand by ~Sep 2, which is comfortable).

**The rule, so this doesn't turn into an improvisation at 6 PM on Aug 30:**

```
[ ] Aug 26 is a HARD CUTOFF for Drop 1 pairing. No exceptions.
[ ] A unit that misses it moves to Drop 2. Move the WHOLE PAIR, never one unit
    (AB_TEST_PROTOCOL.md 2.5) - moving one unit destroys the pairing AND the
    arm assignment
[ ] A unit that misses Sep 2 is out of the experiment entirely: arm =
    NOT_IN_TEST. List it, sell it, just don't analyse it
[ ] Do NOT delay a drop to wait for a unit. Both drop dates are Sunday
    7-9 PM ET and both arms of a pair must list in the same hour
```

**Battery-swap units need two extra calendar days, not ten extra minutes.** The swap is 10 min of
bench time, but [`../PREP_SOP.md`](../PREP_SOP.md) §7 then sends the unit back through the §2.6
overnight hold test, and §6b wants another overnight battery hold before shipping. At ~20% incidence
that is about **5 of 24 units.** Worse, §2.1's matching rule is *"replace both or split the pair"* —
so one battery unit drags its partner along. **Flag battery units at intake and put them at the front
of the prep queue.**

---

## Week 2 (Aug 20–29) — freeze, pair, prep

### Aug 20–22 — finish buying, keep prepping

```
[ ] Last orders that can make Drop 1. After this, purchases are Drop 2 stock
[ ] Re-run the comp routine - prices move weekly in August
[ ] Gate must be PASS by now. If it is not, you have one day left to
    substitute a program before the loadout freezes
```

### Aug 23 — FREEZE

```
[ ] Template, photos, prices, thresholds and the LOADOUT locked
[ ] Loadout re-measured: total P6 bytes <= 34,816 (AB_TEST_PROTOCOL.md 3.4)
[ ] Nothing changes after today
```

> **The arm sequence was already frozen on Aug 13** — it is committed in
> [`AB_TEST_LOG.csv`](AB_TEST_LOG.csv) with seed `20260813` and SHA-256 `a6fc5cea…`
> ([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §2.4). **There is nothing to generate and nothing to
> decide.** Do not regenerate it.

### Aug 24–26 — grade, pair, bind

```
[ ] Fill grade, colour, case, battery, screen notes, serial for EVERY unit
    ** BEFORE you look at the arm column. This is the whole safeguard. **
[ ] Form pairs on the AB_TEST_PROTOCOL.md 2.1 rules only
[ ] Number pairs by ascending LOWEST SERIAL. Unit A = lower serial in each pair
[ ] READ the arms off the section 2.4 table. You are doing a lookup, not a choice
[ ] PAIR-INTEGRITY CHECK on every pair before prep: grade, case, battery,
    photo count all equal within the pair (section 11 checklist)
```

### Aug 26–29 — prep the 12 units for Drop 1

```
[ ] Prep in batches of 6, ~38 min/unit loaded, ~29 bare (PREP_BENCH.md 7)
[ ] Read PREP_SOP.md end to end. The order is NOT negotiable:
       wipe -> clear exam mode -> OS+Apps bundle -> load programs -> verify
[ ] Record 1:About OS version on every unit BEFORE flashing
    (5.5-or-older units may be worth more untouched - PREP_BENCH.md 4.4)
[ ] Verify every program on every loaded unit against the known-answer card
    (LISTING_TEMPLATES.md 7.2). The gate proved the PAYLOAD; this proves
    THIS UNIT
[ ] Build the photo station and tape the tripod position
```

> **Do the first pair slowly, and treat it as the pilot you no longer have.** Weigh the parcel. Build
> both listings as **unpublished drafts.** Time yourself. Fix everything that's awkward *before* you
> touch the other 22 units. A draft listing costs nothing and recovers most of what the pilot did.

### Does 24 units actually fit before the freeze? **[COMPUTED]**

**The bench hours fit comfortably. The arrival dates are what's tight.** At
[`../PREP_SOP.md`](../PREP_SOP.md) §10's batch-of-six timings:

| | Per unit | × units | Total |
|---|---:|---:|---:|
| **Loaded** (full 38-min SOP) | 38 min | 12 | 7.6 h |
| **Bare** (no load step, no program verification; hardware verification still required) | ~29 min | 12 | 5.8 h |
| **All 24 units** | | | **~13.4 h** |
| **Per drop** (6 loaded + 6 bare) | | 12 | **~6.7 h** |

Against the windows: **Aug 26–29 is four days for 6.7 hours** (~1.7 h/day), and **Aug 31–Sep 5 is six
days for another 6.7** (~1.1 h/day). Both fit for one person without heroics.

**Three caveats on that conclusion, in order of how likely they are to bite:**

1. **Prep cannot start before units arrive**, and that is the real constraint — see the deadline
   section above. 13.4 hours of bench time spread over three weeks is easy; 13.4 hours compressed
   into the four days after a late delivery is not.
2. **The 38-minute figure is `[ESTIMATE]`, and the SOP says so.** It also says program verification
   (8 min) is **the bottleneck and does not parallelise** — that alone is 1.6 h across 12 loaded
   units. [`../PREP_SOP.md`](../PREP_SOP.md) §10 asks you to replace these with stopwatch numbers
   after ten units. **Do that, and recheck this table**, because if it is really 50 min/unit the total
   is 17.6 h and the four-day window gets uncomfortable.
3. **The 29-minute bare figure is derived, not published.** It is 38 minus the 4-minute load step and
   ~5 of the 8-minute verify step. **[DERIVED]** — hardware verification, cleaning, grading, photos,
   listing and packing are identical on both arms, which is the point: *bare does not mean
   unprepared* ([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §3.2).

---

## Week 3 (Aug 30 – Sep 6) — the two drops

```
[ ] Drop 1 - Sun Aug 30, 7-9 PM ET: pairs P01-P06, 12 listings
[ ] Aug 31 - Sep 5: prep the 12 units for Drop 2 (~6.7 h)
[ ] Drop 2 - Sun Sep 6, 7-9 PM ET: pairs P07-P12, 12 listings
[ ] Fixed price + Best Offer, 30-day GTC, identical format both arms
[ ] Bare $78 / loaded $90. Auto-accept >= 92% of ask, auto-decline < 80%,
    set IDENTICALLY on both arms (AB_TEST_PROTOCOL.md 2.3)
[ ] Promoted Listings OFF on all 24 listings
[ ] listed_at recorded to the hour for every unit - there is NO recovery path
[ ] Both listing URLs logged and screenshotted
```

**Then stop touching them.** No price changes, no relists, no promoted-listing boosts on one arm.
Every mid-test adjustment destroys the comparison.

**Weekly from here, every Sunday:** views, watchers, offers, questions-about-programs into
[`AB_TEST_LOG.csv`](AB_TEST_LOG.csv), and commit it. Traffic stats age out of Seller Hub — a missed
week is gone for good.

---

## The decision checkpoint — Oct 21

Run **45 days from drop 2**, then analyse ([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §5).
**Interim look Oct 6 is descriptive only** — the sole permitted early stop is the safety stop in
§5.3 (loaded arm ≤1 of 12 sold while bare ≥7 of 12 by day 30).

**The rule, written in advance so you cannot rationalise afterwards** — measured on **net revenue per
unit *listed***, which counts unsold units as $0 and is the only metric that can't be gamed. The
arithmetic is in [`TRACKING_SHEET_NOTES.md`](TRACKING_SHEET_NOTES.md) §4:

| Δ̂ (loaded − bare) | Decision |
|---|---|
| **≥ +$6.00** | **Keep loading.** Make P6 the default SKU; list at bare + $12 |
| **+$2.00 to +$6.00** | **Inconclusive — lean keep.** Keep loading, drop the differential to +$8. Do **not** fund another 12 pairs to resolve this band — §6.4 prices that at ~48 pairs |
| **−$2.00 to +$2.00** | **Inconclusive — null.** Keep loading for differentiation (it's 11 minutes) but **price at the bare comp.** Stop modelling a premium |
| **≤ −$2.00** | **Stop loading for price.** Sell bare; push the digital bundles and put a discount card in the box |

**Overriding condition, checked first:** if **loaded sell-through is ≥3 units below bare** (e.g. bare
10/12, loaded 7/12 — or ≥30 percentage points if you delivered fewer than 12 pairs), the verdict is
**stop loading at $12 regardless of Δ̂.** A tolerable mean while inventory sits is hiding a carrying
cost the endpoint doesn't price — and unsold stock in October is worth less than unsold stock in
August.

**Prerequisite, checked before either:** if the §3.5 hardware gate did not pass, **there is no
verdict.** Do not compute Δ̂ from an experiment whose treatment never worked.

**Why $6 and $2:** loading adds ~11 min/unit. $6.00 works out to **$32.7/hr**, which matches the
~$31.80/hr the rest of the refurb work earns; $2.00 is **$10.9/hr**, below any sensible floor. **Note
that neither threshold depends on the sample size** — they come from the marginal labour rate, which
is why going to 12 pairs did not change them ([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §7.3
re-derives this at n=12 and keeps the rule as pre-registered).

**Note the default:** because loading is only 11 minutes, the rational stance is **keep loading unless
the test shows harm.** The burden of proof is on stopping.

### Read this before you interpret the result

**n=12 cannot detect the effect you most want to measure.** At the base-case variance, 12 pairs has
roughly **26% power** against a true $5 premium — **a real $5 premium is missed three times out of
four** — and about **75%** against $10. It only becomes reliable at **$15+ (~98%)**, which is *above*
the $5–$12 range [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §6 actually expects.

**And there is a harder version of that, which the recomputation at n=12 made visible.** The design's
**maximum possible** Δ̂ — every unit in both arms selling at full ask — is **+$10.37**
([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §4.1). The **minimum effect detectable at 80% power** at
the base-case variance is **+$10.66.** The detection threshold is *above the ceiling*: **at realistic
variance this test cannot reach 80% power against any outcome it is capable of producing.** Power at
the +$6 decision threshold itself is **35%**.

So a "no difference" result means **absence of evidence, not evidence of absence.**
**[`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §6 covers this honestly — read it before you draw a
conclusion, not after.**

**What n=12 *is* good for:** catching a catastrophe (loaded units performing *worse*), validating the
whole pipeline, and producing a real **σ_d** to replace an assumption. **Treat it as a screening test,
not a measurement.** The sell-through endpoint is the better-powered one, and it is the one that
matters most: 10 of 12 pairs in the same direction gives *p* = 0.039.

**The trap to avoid:** deciding after 3 pairs because the early ones look good. **Pre-commit to all
pairs and the full 45 days.** Watcher and view counts are leading indicators only — never a decision
basis.

---

## Money and timing

### What it costs, and when the cash leaves

| | Amount | When |
|---|---:|---|
| Bench, five-item minimum ([`PREP_BENCH.md`](PREP_BENCH.md) §1) | **~$38** | Aug 13 |
| Bench, rest of essential §2.1 | **~$117** | as units arrive |
| **24 units at $30–$40** | **$720 – $960** | **Aug 13–24 — the whole commitment in twelve days** |
| Consumables: 24 mini-B cables, ~8 spare slide cases, ~5 batteries at $8, mailers + stiffeners, printed cards | **~$133** | Aug 20 – Sep 5 |
| **All-in** | **$1,008 – $1,248** | |

That lands on the **~$1,000–$1,240** all-in estimate this kit has carried from the start. The
difference from the old plan is not the total — it is the **shape**: under the pilot plan ~$380 went
out in week 1 and the remaining ~$600 only after you'd shipped something. **Now $875–$1,115 leaves in
the first twelve days, before a single unit has sold.**

### When money comes back — later than you think

| | |
|---|---|
| First listings live | **Aug 30** |
| First sales | Days, if the price is right |
| **First usable cash** | **~Sep 14–21.** eBay holds payouts for new sellers — commonly up to 21 days on early sales — and you have no selling history on this account |
| Expected gross recovery at 85% sell-through | **~$1,400 – $1,500** |
| Expected return if the premium is real | ~$28/unit net at $30 acquisition |
| Expected return if it's $0 | ~$28/unit net on **bare** units, minus 11 wasted min/unit |

**So plan for roughly a month with the full $1,000–$1,250 committed and nothing coming back.** That is
the genuine cash consequence of buying 24 up front, and it is worth checking against your actual
runway before Aug 24 rather than after. **If the answer is uncomfortable, buy 16–18 units instead of
24** — that yields 7–8 pairs against 9–11, which costs about $1.20 of minimum detectable effect
(§6.2's n=9 column versus n=12) and almost nothing in decision quality, because §6.3 shows the test is
underpowered at either size. **The sample size is the cheapest thing to give up here.**

### The Evo R&D unit — re-timed to the week of Sep 14

[`../EVO_TRANSITION.md`](../EVO_TRANSITION.md) §7 wants **one Evo, ~$160, as R&D** — not as
inventory — because a single purchase converts most of that document's UNVERIFIED items to VERIFIED.
The reconciliation pass timed it "after the pilot pairs ship." **There are no pilot pairs any more, so
that phrase no longer maps to anything.**

**New timing: the week of Sep 14**, and the reasoning is cash, not priority:

- **Not in the Aug 13–24 window.** $160 there competes directly with test inventory — it is 4–5
  calculators, or roughly two pairs. Two pairs is a bigger loss to the experiment than a two-week
  delay is to the Evo research.
- **Not before Drop 2 (Sep 6).** Not for money, for attention. Prep and two drops inside three weeks
  with no pilot is already the tightest part of this plan.
- **The week of Sep 14 is when the first payouts clear**, which makes it fundable from revenue rather
  than from the launch budget. It is also comfortably before the Oct 21 decision, so the Evo findings
  are available for whatever the verdict implies about next season.

**One condition that overrides all of the above:** if the §3.5 gate **fails on both payload formats**,
buy the Evo immediately. At that point the `.py`-as-portable-payload question stops being next
season's research and becomes this season's blocker, and [`../EVO_TRANSITION.md`](../EVO_TRANSITION.md)
is the document with the answer.

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
11. **Never load unit #2 before the §3.5 gate passes.** Added 2026-08-13. This is the one rule that
    replaces the pilot, and it is the cheapest insurance in the plan.
12. **Never edit the `arm` column** in [`AB_TEST_LOG.csv`](AB_TEST_LOG.csv). It is pre-committed and
    hashed; editing it voids the randomisation audit trail.

---

## App support — ⛔ deferred, not being built

The inventory app tracks per-unit variant, OS, serial, bundles, costs, prices and the 5-step prep
checklist, but **cannot run this experiment.** It has no experiment-arm field, no pair ID, no listing
timestamp for days-to-sale, and no realised-premium report by arm.

**The owner decided on 2026-08-13 that tracking is a spreadsheet.**
[`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §10 remains as the written specification of what the app
would need — **all 20 items of it are unbuilt and unscheduled.** Do not read it as shipped
functionality and do not wait for it.

**Track the test in [`AB_TEST_LOG.csv`](AB_TEST_LOG.csv)**, which is committed and pre-filled, using
[`TRACKING_SHEET_NOTES.md`](TRACKING_SHEET_NOTES.md) for the fill order and the by-hand arithmetic. At
24 rows a spreadsheet is not a compromise — it is the right tool, and it is the only one that will
exist before the season ends.

---

AP®, SAT®, and ACT® are trademarks registered by their respective owners, none of which are affiliated
with, or endorse, this product. TI-84 Plus CE Python™ and Texas Instruments® are trademarks of Texas
Instruments Incorporated, which is not affiliated with, and does not endorse, this product. Nothing in
this document is legal advice.
