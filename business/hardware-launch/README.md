# Hardware Launch Kit — Start Here

**A six-week sequence to go from zero to a decided answer on whether the pre-loaded calculator line
is a business.**

Created 2026-08-12. **Rewritten 2026-08-13** for the owner's decision to buy all **24 units up front**
rather than run a 6-unit pilot first. **Revised again the same day (second pass)** for two further
decisions: the A/B test is **demoted to a harm screen**, and **the gate unit is bought locally, in
person, today.** Companion to the strategy docs in [`../`](../) — this folder is the tactical layer.

> ## 🔴 What to do today, Aug 13, before anything else
>
> **Go buy one TI-84 Plus CE Python locally, in person, and run the hardware gate on it tonight.**
>
> Not online. Today. One unit. [`SOURCING_SHORTLIST.md`](SOURCING_SHORTLIST.md) **§7** is the playbook
> — channels, what to pay, what to bring, and the **point-of-sale variant test** that lets you prove
> the unit is a genuine *Python* model **before you hand over money.**
>
> **Why this is now day 0 rather than "days 1–3, locally if possible."** The `.8xv` AppVars in this
> repository **have never been executed on a physical calculator.** The gate
> ([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §3.5) is what finds that out — and under the previous
> schedule it ran on the *first shipment to arrive*, which meant it would have reported back on
> **$875–$1,115 of units that were already bought and largely non-returnable.** A gate that fires after
> the money is gone is a post-mortem, not a gate.
>
> **One local unit converts the repo's oldest open question into an answer within a day, for the price
> of one calculator, before the other 23 are ordered.** That is the entire rationale, and it is right.
>
> **The cost of the change: the online order window gets tighter, not looser.** Orders now go out
> Aug 14–20 instead of Aug 13–24, and **Aug 19–20 is a hard deadline** — see
> [the deadline section](#the-buy-deadline-is-aug-1920-not-aug-24) below. You are trading two days of
> ordering slack for the ability to not waste $875. **Take that trade.**

---

## The one thing this kit is for

**The software premium is unproven, and — as of 2026-08-13 — this kit no longer claims it will prove
it.** [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §6 estimates it at **$5–$12 and explicitly allows
that it may be $0.** Loading programs costs ~11 minutes per unit. If buyers don't pay for it, the
correct business is *refurbish and resell bare calculators*.

**But 12 pairs cannot measure a $5–$12 premium, and the arithmetic showing that is not close.** At 12
pairs the smallest effect detectable at 80% power is **$10.66**, while the largest per-unit difference
the design can physically produce — every unit in both arms selling at full ask — is **$10.37**.
**The detection floor sits above the design's own ceiling.** Measuring the premium properly needs
**~48 pairs** ([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §6.4), which this season cannot supply.

**So the owner has changed what the test is for, and the new job is one the design is genuinely good
at:**

> ### The question is no longer *"how much is the software worth?"*
> ### It is *"is loading the software actively hurting sales?"*

That reframing is not a retreat. It is what makes the rest of the plan coherent:

- **Loading costs ~11 marginal minutes per unit**, so the rational default is **keep loading** — no
  evidence required. **The burden of proof is on stopping.**
- **Harm is not capped the way benefit is.** A loaded unit that fails to sell while its matched bare
  partner sells costs that pair **−$61.49**, roughly **six times** the +$10.37 ceiling on the upside.
  A design that cannot reach 80% power against any attainable *benefit* does reach it against harm of
  about **−$10** (§6.3a).
- **So the test is a smoke alarm, not a scale.** It will not tell you the premium is $7. It will tell
  you if the loaded arm is on fire.

**Everything in this folder exists to answer that narrower question with 24 calculators and about ten
weeks — and, first, to find out whether the software runs on real hardware at all.**

---

## The documents

| Read | For |
|---|---|
| **[`SOURCING_SHORTLIST.md`](SOURCING_SHORTLIST.md)** | How to find and price CE Python units, how to prove the variant before paying, and the walk-away prices. **§7 is today's playbook — same-day local buying.** §1.5 and §6 are the two highest-value sections in this folder |
| **[`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md)** | The 12-matched-pair **harm screen**: design, endpoints, the decision rule written in advance, **the blocking hardware gate in §3.5**, and an honest account of what n=12 can and cannot detect. **§0 is one page and it is the one to read** |
| **[`AB_TEST_LOG.csv`](AB_TEST_LOG.csv)** | **The tracking sheet.** Pre-filled: 24 rows, 12 pairs, arm assignments already randomised and committed. **66 columns** as of 2026-08-13 |
| **[`TRACKING_SHEET_NOTES.md`](TRACKING_SHEET_NOTES.md)** | How to fill the sheet, and how to compute the verdict by hand in a spreadsheet. **§4.5's worked example is the best five minutes in this folder** |
| **[`HW_VALIDATION.md`](HW_VALIDATION.md)** | Where the §3.5 hardware gate result gets recorded. **Currently empty — filling it in is tonight's job.** §3.0 carries the hand-derived expected value for `TRIG`, the one program with no `qa/` fixture |
| **[`LISTING_TEMPLATES.md`](LISTING_TEMPLATES.md)** | Paste-ready eBay and Mercari copy for both arms, photo shot list, and the compliance boundaries |
| **[`PREP_BENCH.md`](PREP_BENCH.md)** | What to buy to process units, what to skip, total startup cost, and the throughput it supports |

**Today, read [`SOURCING_SHORTLIST.md`](SOURCING_SHORTLIST.md) §7 and §6.2, then go buy one unit.**
Read [`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §0 and §3.5 before you run the gate tonight. The rest
can wait until the gate result is known — **there is no point studying the experiment design until you
know whether the treatment exists.**

⚠️ **Two known gaps, stated up front.** [`SOURCING_SHORTLIST.md`](SOURCING_SHORTLIST.md) §0 explains
that **live eBay comps could not be retrieved** (eBay returns 403 to automated fetches on every
surface, and the sold-comp aggregators are bot-gated). Its price bands are **derived from the existing
repo baselines, not observed 2026-08 transactions** — §2 of that document is a 15-minute manual
routine that fixes this, and **you should run it before your first purchase** — which, as of the day-0
decision, is today. That matters more now than it did under the pilot plan: you are about to commit the
whole budget in **seven days**.
[`PREP_BENCH.md`](PREP_BENCH.md) §0 flags that most individual equipment prices are estimates. Neither
gap blocks starting.

---

## ⚠️ Read this before the sequence: what buying 24 at once costs you

The kit previously recommended **6 units first** (2 pilot pairs + spares) precisely so that the things
below could be discovered cheaply. **The decision to buy 24 up front is being executed as instructed,
and it is defensible** — the season really is short, and the units really are inventory you were going
to buy anyway. But four risks changed shape, and pretending otherwise would make this document useless.

| Risk | What the pilot did about it | What now stands in its place |
|---|---|---|
| **The `.8xv` programs have never run on hardware** | Found out on unit 1 for ~$38 of exposure | ✅ **Solved, as of the day-0 decision.** [`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §3.5 runs on **one locally-bought unit today, before the other 23 are ordered.** This is now *better* than the pilot: the pilot risked ~$38 and answered in a week; this risks one unit and answers tonight |
| **First-timer mistakes in prep, photos, packing, shipping** | 4 throwaway units, listed outside the experiment | **Still a genuine loss, but smaller than it was.** The gate unit arrives a week before everything else, so it *is* a shakedown unit for wipe / OS+Apps / load / photograph — you just can't throw it away afterwards. Prep it slowly, weigh the parcel, build the listing as an unpublished draft |
| **Paying too much, in a window with no comp data** | 6 units of exposure while you learned the market | **$720–$960 committed in a week on price bands the kit itself labels underived.** Run the §2 comp routine **first, today** — and note that the day-0 unit is bought *before* the comps exist, which is accepted deliberately: see §7.4 of the shortlist on why a gate unit is worth a small premium |
| **Buying 24 and yielding fewer pairs than expected** | Would have been discovered at 6 | **Unchanged and unavoidable.** §3.1 of the protocol computes it: 24 units yields **9–11 pairs**, not 12 |

**And the statistical point that the extra units do not fix — which is now the *premise* of the design
rather than a caveat.** The protocol's §6 was recomputed at n=12 with exact noncentral-*t* and the
conclusion held: **12 pairs cannot detect the $5–$12 premium this business plan is built on.** Going
from 10 pairs to 12 moved the minimum detectable effect from $11.94 to $10.66 — **$1.28.** Buying 24
units instead of 20 did not buy a measurement; it bought inventory sooner and removed the pilot.

**That fact is why the test was demoted to a harm screen** (see the section above). The response to
"this design cannot measure what we wanted" was not to pretend otherwise, and not to abandon the test
— it was to **use it for the thing it is well-powered for.** You should not read a 24-unit test as more
conclusive than a 20-unit one, and after Oct 21 you should not read it as a measurement at all.

---

## Week 1 (Aug 13–20) — the gate first, then the money

**Goal: prove the software runs on real silicon *before* $875 leaves the account.**

**The sequence changed on 2026-08-13.** It used to be *buy for twelve days, gate whatever arrives
first.* It is now **gate first, buy second.** Everything below is in the order it happens.

### 🔴 Day 0 — TODAY, Aug 13, in this order

```
STEP 1 - 30 minutes at the desk, before you leave the house
[ ] Read SOURCING_SHORTLIST.md section 7 (same-day local playbook) and
    section 6.2. Put 6.2 on your phone - you will use it at a counter
[ ] Read AB_TEST_PROTOCOL.md 3.5 so you know what the gate is before you buy
    the unit that has to pass it
[ ] Run the 15-minute manual comp routine (SOURCING_SHORTLIST.md section 2).
    Terapeak first - free with your seller account, and it is eBay's own data.
    Write the medians into section 3 of that file
    ** This now happens BEFORE the first purchase, not before the third. **
[ ] Buy the five-item minimum from PREP_BENCH.md section 1 (~$38)
[ ] Install TI Connect CE and download the OS *AND APPS* bundle (.b84)
       ** Do this BEFORE the unit is in your hands. It is a large download and
          it is the thing that will make you lose the evening otherwise. **

STEP 2 - GO BUY ONE UNIT, IN PERSON  (SOURCING_SHORTLIST.md section 7)
[ ] Bring: cash, a phone, the section 6.2 checklist, and a USB mini-B cable
[ ] Work the channels in 7.2 order - the ones that can produce a unit TODAY
[ ] RUN THE POINT-OF-SALE VARIANT TEST BEFORE PAYING (section 7.3):
       faceplate must read PYTHON, and print(1+1) must return 2 in the Shell
[ ] Walk away on any of the section 7.5 conditions. There will be another unit
[ ] Log it: acquisition_channel, acquisition_cost, hw_gate_unit = TRUE

STEP 3 - RUN THE GATE TONIGHT  (AB_TEST_PROTOCOL.md 3.5)
[ ] All ten P6 programs: launches, accepts input, correct known answer,
    exits cleanly
[ ] Send QUAD BOTH ways (.8xv and .py). The comparison localises any fault
[ ] TRIG: use the DERIVED expected value in HW_VALIDATION.md 3.0 - SAS with
    5, 8, 60 gives c = 7 exactly. TRIG is the only P6 program with no qa/
    fixture, so its answer is stated there and nowhere else
[ ] Photograph TRIG and SIMPSON on-screen
[ ] Record every result in HW_VALIDATION.md
[ ] Write hw_gate_status / hw_gate_date / payload_format into AB_TEST_LOG.csv
```

> **Tape to the wall:** an All-Memory reset **deletes the Python App itself.** A wiped unit boots,
> looks entirely normal, and has no Python until you send the **OS *and Apps*** bundle. And **never**
> enter Press-to-Test after loading — it deletes the AppVars. Neither of these is a gate failure;
> [`HW_VALIDATION.md`](HW_VALIDATION.md) §2 lists both so you don't misdiagnose one as a converter bug.

> **If you cannot get a unit today.** Keep trying **Aug 14, 15 and 16** — §7.2 lists which channels can
> plausibly deliver same-day versus in a few days. **Aug 16 is the point of no return:** past it, the
> gate cannot both run and leave room for a program substitution before the **Aug 23 loadout freeze**,
> and you fall back to gating the first online arrival — which is the old, worse plan. **In that case
> place the online orders on Aug 14–15 anyway.** Missing the order deadline costs you Drop 1; missing
> the local unit costs you a week of certainty. **The deadline wins.**

### Day 1–7 (Aug 14–20) — NOW buy the other 23

**Only after the gate result is written down.**

```
[ ] Target 23 more units at <= $32 each, $40 absolute ceiling
[ ] ** Aug 19-20 IS A HARD ORDER DEADLINE. ** See the next section
[ ] Ask EVERY online seller the section 1.5 question (below). It is worth more
    than every price table in this folder - and note it is strictly WEAKER than
    the test you ran yourself at the counter on day 0
[ ] Log every purchase into AB_TEST_LOG.csv Pass 1 the day you buy
[ ] As units arrive: SOP steps 1-3 (wipe, exam clear, OS+Apps) and step 5
    (clean and grade). These are NOT blocked by the gate - only loading is
[ ] Sell or part out anything that fails intake. A cracked-screen CE Python is
    worth $30-$40 to the repair community (SOURCING_SHORTLIST.md 3.3)
```

**The gate is blocking. Until it reads PASS, exactly one unit has programs on it — and ideally, no
online order has been placed.**

### What happens to the schedule if the gate fails

| Gate result | The loaded arm | The schedule | The money |
|---|---|---|---|
| **PASS** | Proceeds on `.8xv` | Unchanged. Order Aug 14–20 | ~$875 committed as planned |
| **`FAIL_8XV_ONLY`** — `.py` runs, `.8xv` doesn't | **Proceeds on `.py`.** Set `payload_format = PY` on all 12 loaded rows | **No impact.** [`../PREP_SOP.md`](../PREP_SOP.md) §5 already calls `.py` the default and validated path | Unchanged. **Order as planned** |
| **`FAIL_BOTH`** — neither format runs | **Blocked.** All 24 units ship **bare**, `excluded = TRUE`, `exclusion_reason = HW_GATE_FAILED` on every row | **The A/B test is cancelled, not delayed.** There is nothing to compare. Drop 1 and Drop 2 become ordinary bare-inventory listings and the Sunday-evening timing stops mattering | **Still order the units** — bare resale was always the fallback business and the economics of it don't depend on the software. **But order at the bare-comp price, not with a premium in mind** |
| **Fixable by substituting one program out of P6** | Proceeds, after a re-run | **Only legitimate before the Aug 23 loadout freeze.** This is why day 0 matters: gating on Aug 13 leaves ten days for a fix; gating on the first arrival left about three | Unchanged |

**On `FAIL_BOTH`, three things happen immediately:**

1. **No Δ̂ is ever computed.** [`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §7.1 step 0 and §3.5.4: the
   experiment **did not run.** It did not return a null. Do not write it up as one, and do not let
   "we tested it and there was no premium" become the story — that sentence would be false.
2. **Buy the Evo R&D unit immediately** — this overrides the week-of-Sep-14 timing below. At that point
   the `.py`-as-portable-payload question stops being next season's research and becomes this season's
   blocker, and [`../EVO_TRANSITION.md`](../EVO_TRANSITION.md) is the document with the answer.
3. **The gate failure is worth more than the A/B test was.** It is a fact about the product rather than
   an estimate about the market, and it is the single most valuable result this launch can produce.
   Record it in full in [`HW_VALIDATION.md`](HW_VALIDATION.md) §3.1, traceback verbatim.

> **Ask every online seller the §1.5 question:** *"Please open the Python app, type `print(1+1)`, press
> Run, and send me a photo."* A faked unit — a plain CE with an edited certificate — shows Python in the
> app list and opens the editor, and fails **only** when code runs, with the exact string **"Run and
> Shell are not available right now."**
>
> **In person you do not have to ask. You press the keys yourself** — see
> [`SOURCING_SHORTLIST.md`](SOURCING_SHORTLIST.md) §7.3. A seller's photo can be of a different unit;
> your own keystrokes cannot.

> **Ask every seller the §1.5 question:** *"Please open the Python app, type `print(1+1)`, press Run,
> and send me a photo."* A faked unit — a plain CE with an edited certificate — shows Python in the
> app list and opens the editor, and fails **only** when code runs, with the exact string **"Run and
> Shell are not available right now."** This one message is worth more than every price table in this
> folder.

---

## The buy deadline is Aug 19–20, not Aug 24

**This is the scheduling problem the 24-unit decision creates, and it needs stating plainly.**

Drop 1 is **Sun Aug 30**. To list 6 matched pairs that evening, all 12 of those units must be
**graded** — because pairs cannot be formed until every candidate has a grade
([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §2.4 stage 2) — and then prepped. Working backwards:

```
Aug 30  Drop 1 lists                        <- fixed
Aug 26-29  prep 12 units (6.7 bench hours)   <- comfortable
Aug 26  HARD CUTOFF: all Drop 1 units in hand, graded, paired
Aug 19-20  LATEST ONLINE ORDER DATE          <- 3-7 day shipping
```

> ### Aug 24 is when the window *closes*. It is not a date you can order on.
>
> **This distinction has caused confusion and it is worth being blunt about.** A unit ordered **Aug 24**
> arrives, at 3–7 days' shipping, somewhere between **Aug 27 and Aug 31.** It then needs to be
> triaged, wiped, flashed, cleaned, **graded**, matched into a pair, bound to an arm, prepped
> (~38 min loaded), photographed and listed — **for a drop that happens Aug 30 at 7 PM.** That does not
> fit, and the failure is not recoverable on the night.
>
> **So: Aug 19–20 is the last usable online order date for Drop 1 inventory.** Aug 21–24 orders arrive
> Aug 24–31 and realistically make **Drop 2 only** (Sep 6 needs them in hand by ~Sep 2, which is
> comfortable). **After Aug 24 there is no point ordering at all** for this test.
>
> **The day-0 change makes this tighter, and that is the accepted cost.** Ordering now starts Aug 14
> instead of Aug 13, so the online window is **Aug 14–20: seven days, not twelve.** In exchange, you
> find out whether the software works before you spend the money. **The trade is correct, but it means
> Aug 19–20 has no slack left in it — do not treat it as a soft target.**

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
[ ] Aug 19-20 was the last order date that can make Drop 1. After this,
    purchases are Drop 2 stock
[ ] Re-run the comp routine - prices move weekly in August
[ ] Gate should have PASSED on Aug 13. If day 0 slipped and it has not run
    yet, you have ONE DAY left to substitute a program before the loadout
    freezes on Aug 23 - and that is the risk moving the gate to day 0 was
    meant to eliminate
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
[ ] Promoted Listings OFF on all 24 listings (no longer a logged column - it is
    a protocol constant, so check it rather than record it)
[ ] listed_at recorded to the hour for every unit - there is NO recovery path
[ ] Both listing URLs logged and screenshotted
```

**Then stop touching them.** No price changes, no relists, no promoted-listing boosts on one arm.
Every mid-test adjustment destroys the comparison.

**Weekly from here, every Sunday:** **`sold` status first** — it is the primary endpoint — then views
and watchers (**day 7 only** now), offers, and questions-about-programs into
[`AB_TEST_LOG.csv`](AB_TEST_LOG.csv), and commit it. Traffic stats age out of Seller Hub — a missed
week is gone for good.

---

## The decision checkpoint — Oct 21

Run **45 days from drop 2**, then analyse ([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §5).
**Interim look Oct 6 is descriptive only** — the sole permitted early stop is the safety stop in
§5.3 (loaded arm ≤1 of 12 sold while bare ≥7 of 12 by day 30).

**The rule, written in advance so you cannot rationalise afterwards.** The arithmetic is in
[`TRACKING_SHEET_NOTES.md`](TRACKING_SHEET_NOTES.md) §4. **Apply it in this order** — the order changed
on 2026-08-13 to match which endpoint is primary:

**Step 0 — the prerequisite.** If the §3.5 hardware gate did not pass, **there is no verdict and no
Δ̂.** Do not compute one. An experiment whose treatment never worked has no result to report.

**Step 1 — the primary endpoint. The sell-through gap.** If **loaded sell-through is ≥3 units below
bare** (e.g. bare 10/12, loaded 7/12 — or ≥30 percentage points if you delivered fewer than 12 pairs),
the verdict is **stop loading at $12, regardless of Δ̂**, and step 2 does not happen. A tolerable mean
while inventory sits is hiding a carrying cost the endpoint doesn't price — and unsold stock in October
is worth less than unsold stock in August. **This is the step with the statistical power** (§6.3a).

**Step 2 — the secondary screen. The Δ̂ bands**, on **net revenue per unit *listed***, counting unsold
units as $0. **Report Δ̂ with its 95% confidence interval, always:**

| Δ̂ (loaded − bare) | Decision |
|---|---|
| **≥ +$6.00** | **Keep loading.** Make P6 the default SKU; list at bare + $12 |
| **+$2.00 to +$6.00** | **Inconclusive — lean keep.** Keep loading, drop the differential to +$8. Do **not** fund another 12 pairs to resolve this band — §6.4 prices that at ~48 pairs |
| **−$2.00 to +$2.00** | **Inconclusive — null.** Keep loading for differentiation (it's 11 minutes) but **price at the bare comp.** Stop modelling a premium |
| **≤ −$2.00** | **Stop loading for price.** Sell bare; push the digital bundles and put a discount card in the box |

> **Three of the four rows say "keep loading," and that is not a defect — it is the design.** Loading
> costs 11 minutes, so continuing needs no evidence; **the burden of proof is on stopping.** What the
> rows change is **how much you may price around it**, from "+$12 differential" down to "bare comp."
> **Read the table as a pricing instruction, not as a conclusion about the premium.**
>
> **And Δ̂ is never a measured premium.** [`TRACKING_SHEET_NOTES.md`](TRACKING_SHEET_NOTES.md) §4.5
> works a case where the verdict is **KEEP LOADING** off **Δ̂ = +$7.67** with a confidence interval of
> **−$37 to +$52** — an interval that contains the STOP threshold and is wider than the entire range
> the design can produce. **The verdict is still correct. The measurement does not exist.** If you read
> one thing before Oct 21, read that example.

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
four** — and **77.8%** against $10.37. It only becomes reliable at **$15+ (97.5%)**, which is *above*
the $5–$12 range [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §6 actually expects.

**And there is a harder version of that, which the recomputation at n=12 made visible.** The design's
**maximum possible** Δ̂ — every unit in both arms selling at full ask — is **+$10.37**
([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §4.2). The **minimum effect detectable at 80% power** at
the base-case variance is **+$10.66.** The detection threshold is *above the ceiling*: **at realistic
variance this test cannot reach 80% power against any outcome it is capable of producing.** Power at
the +$6 decision threshold itself is **35.3%**.

So a positive result means **absence of evidence about magnitude**, and a null result means **absence of
evidence, not evidence of absence.**

### What the test *can* do — and this is now the headline **[COMPUTED 2026-08-13]**

**Harm is not capped the way benefit is**, and that asymmetry is where the design's power lives:

| | Bounded by | Attainable extreme |
|---|---|---:|
| **Benefit** | The $12 differential minus fees, and it cannot widen — a new CE is in stock at **$94.99** | **+$10.37** |
| **Harm** | Nothing. An unsold loaded unit scores $0 against its partner's $61.49 | **−$61.49** per pair |

**So the pre-registered stop rule, read as the screening rule it always was:**

| If loading truly costs you… | …the rule says STOP with probability |
|---|---:|
| Nothing (loading is neutral or good) | **5.8%** ← the false-stop rate |
| −$1.96 — *the −$2 threshold* | **52.9%** |
| **−$10.08** | **80.0%** ← **the honest harm detection floor** |
| −$19.93 | **94.6%** |
| −$27.12 | **98.2%** |

**Read plainly: this is a competent smoke alarm and a useless scale.** It reaches 80% sensitivity
against harm of about **−$10** at a **5.8%** false-stop rate, and 80% power against **no attainable
benefit whatsoever.** At the realistic 9–11 pair yield it loses only ~5 points of sensitivity — count
based rules degrade slowly — so **do not let a 10-pair yield talk you out of applying the rule.**

**Three honest caveats on those figures**, all in [`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §6.3a:

1. **They are upper bounds.** The model has no haggling variance, no returns, no listing-quality
   drift. Read 80% as *80% under a model kinder than reality*.
2. **A quiet result is weak evidence.** At the −$2 threshold the rule misses **47%** of the time. The
   write-up says **"no harm detected,"** never *"no harm."*
3. **The *t*-test on Δ̂ is not the harm detector** — it has **5.4%** power at the −$2 threshold, because
   the event that creates harm (a loaded unit not selling) is the same event that inflates the variance
   hiding it. **The count is what carries the power.** That finding is why the count was promoted to
   the primary endpoint.

**The other thing n=12 is genuinely good for:** validating the whole pipeline, and producing a real
**σ_d** to replace an assumption. §6.3a suggests the true σ_d is **$21–$40**, not the $12 base case —
if that holds, it is the most valuable number the test produces.

**The trap to avoid:** deciding after 3 pairs because the early ones look good. **Pre-commit to all
pairs and the full 45 days.** Watcher and view counts are leading indicators only — never a decision
basis. **And never run a sign test on the dollar differences** as a harm check: §6.8 shows it reports a
significant *win* about a third of the time when loading is genuinely losing you money.

---

## Money and timing

### What it costs, and when the cash leaves

| | Amount | When |
|---|---:|---|
| Bench, five-item minimum ([`PREP_BENCH.md`](PREP_BENCH.md) §1) | **~$38** | Aug 13 |
| **The gate unit — 1 unit, bought locally** | **$30 – $45** | **Aug 13. This is the only money at risk before the gate result exists** |
| Bench, rest of essential §2.1 | **~$117** | as units arrive |
| **The other 23 units at $30–$40** | **$690 – $920** | **Aug 14–20 — released only after the gate result** |
| Consumables: 24 mini-B cables, ~8 spare slide cases, ~5 batteries at $8, mailers + stiffeners, printed cards | **~$133** | Aug 20 – Sep 5 |
| **All-in** | **$1,008 – $1,253** | |

That lands on the **~$1,000–$1,250** all-in estimate this kit has carried from the start.

**The shape is what the day-0 decision changed, and it is the best feature of the new plan.** Under the
pilot plan ~$380 went out in week 1 and the rest only after you'd shipped something. Under the
24-up-front plan **$875–$1,115 left in twelve days before a single unit had sold, with the gate
reporting somewhere in the middle of that.** Now:

```
Aug 13   ~$38 bench + ~$30-45 for ONE unit   <- total exposure before the gate answers
Aug 13   GATE RUNS
Aug 14-20  $690-$920 for the other 23        <- released against a KNOWN gate result
```

**Roughly $75 is at risk on the open hardware question instead of roughly $900.** The total is
unchanged and the season is unchanged; only the order changed. **That is a free improvement, and it is
the strongest argument for the decision.**

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
runway **before Aug 19–20** rather than after. **If the answer is uncomfortable, buy 16–18 units instead
of 24** — that yields 7–8 pairs against 9–11, which costs about $1.20 of minimum detectable effect
(§6.2's n=9 column versus n=12) and almost nothing in decision quality, because §6.3 shows the test is
underpowered on the benefit side at either size and §6.3a shows the harm screen loses only ~5 points of
sensitivity. **The sample size is the cheapest thing to give up here — cheaper than it looked before
the harm-power table existed.**

### The Evo R&D unit — re-timed to the week of Sep 14

[`../EVO_TRANSITION.md`](../EVO_TRANSITION.md) §7 wants **one Evo, ~$160, as R&D** — not as
inventory — because a single purchase converts most of that document's UNVERIFIED items to VERIFIED.
The reconciliation pass timed it "after the pilot pairs ship." **There are no pilot pairs any more, so
that phrase no longer maps to anything.**

**New timing: the week of Sep 14**, and the reasoning is cash, not priority:

- **Not in the Aug 13–20 window.** $160 there competes directly with test inventory — it is 4–5
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

> **The day-0 gate makes that override much more useful, which is a side benefit worth naming.** Under
> the old schedule a `FAIL_BOTH` would have surfaced around Aug 20 with the money already spent and the
> drops nine days away. **Now it surfaces on Aug 13, before the online orders, with the whole $160
> unspent and the Evo research able to start in the same week.** A contingency that fires early is a
> plan; one that fires late is an explanation.

⚠️ **You are starting late in the season.** It is August; peak sell-side runs to mid-September, and
the ideal *buy* window (late May–June, 20–35% below average) has passed for this year. Expect to pay
toward the top of the $25–$40 band — **including today's gate unit, which you are buying without comps
and in a hurry.** **The paired comparison is unaffected** — that is what pairing is for — but absolute
sell-through will look worse than a true August cohort.
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
11. **Never load unit #2 before the §3.5 gate passes — and don't place the online orders before it
    either.** Added 2026-08-13, strengthened the same day. This is the rule that replaces the pilot,
    and it is the cheapest insurance in the plan.
12. **Never edit the `arm` column** in [`AB_TEST_LOG.csv`](AB_TEST_LOG.csv). It is pre-committed and
    hashed; editing it voids the randomisation audit trail. **Demoting the test to a screen does not
    relax this** — a screen you allocated after seeing the units is not a screen.
13. **Never pay for a unit you have not variant-tested yourself when you are standing in front of
    it.** Added 2026-08-13. Online you have to accept a seller's photo; in person you do not, and
    accepting one anyway throws away the only real advantage local buying has
    ([`SOURCING_SHORTLIST.md`](SOURCING_SHORTLIST.md) §7.3).
14. **Never call Δ̂ a measured premium.** Added 2026-08-13. Report it with its confidence interval and
    the word *descriptive*, every time. [`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §7.4 item 11
    requires the disclaimer in the write-up verbatim.

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
