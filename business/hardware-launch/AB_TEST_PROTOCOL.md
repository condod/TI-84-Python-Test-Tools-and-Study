# A/B Test Protocol — Is The Software Premium Real?

**Pre-registered design for a 12-matched-pair test of loaded vs. bare TI-84 Plus CE Python units.**

Written 2026-08-12. **Revised 2026-08-13** for the owner's decision to buy all 24 units up front
rather than run a 6-unit pilot first. This document is the pre-registration. **The decision rule and
the randomisation sequence are now filled in and committed** — see §2.4 and §7 — and they do not
change after listings go live. Changing a decision rule after seeing data is the single easiest way
to fool yourself, and it is the failure mode this whole document exists to prevent.

> ### What the 2026-08-13 revision changed, and what it deliberately did not
>
> **Changed.** The design is now **12 pairs / 24 units** bought in one window instead of 10 pairs
> behind a 6-unit pilot. Randomisation is **pre-committed for all 12 pairs at once** with a recorded
> seed and hash (§2.4) — it can no longer be generated as units trickle in. Drops are **6 pairs
> each** (§2.5). §6 is recomputed from scratch at n=12. A **blocking hardware validation gate**
> (§3.5) replaces the protection the pilot used to provide. §8 now points at a **committed
> spreadsheet**, and §10's app spec is marked **deferred**.
>
> **Not changed, on purpose.** The **decision thresholds are still +$6 / +$2 / −$2 with the
> ≥3-unit sell-through override.** §7.3 is a new section that re-derives them at n=12 and explains
> why moving them would be wrong. Going from 10 pairs to 12 does not buy enough resolution to
> justify touching a pre-registered rule, and the thresholds were never derived from *n* in the
> first place — they come from the marginal labour rate.
>
> **The headline honesty finding is unchanged and, if anything, sharper:** see §6.3. **12 pairs
> still cannot detect the $5–$12 premium that [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §6
> expects.** Buying 24 units up front does not fix that, because it was never a sample-size problem
> you could solve at this scale.

**Labelling convention, matching the rest of `business/`:** **[RESEARCHED]** = a figure with a
citable source. **[ESTIMATE]** = my modelling assumption. Statistical results below are computed,
not cited, and are marked **[COMPUTED]** with the inputs shown so you can check them.

**Companion docs:** [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §6 poses this question and
explicitly asks for this test. [`../PREP_SOP.md`](../PREP_SOP.md) governs the prep.
[`LISTING_TEMPLATES.md`](LISTING_TEMPLATES.md) contains the exact copy for both arms.
[`SOURCING_SHORTLIST.md`](SOURCING_SHORTLIST.md) tells you what to pay.

**Where the data goes:** [`AB_TEST_LOG.csv`](AB_TEST_LOG.csv) is the committed, pre-filled tracking
sheet, and [`TRACKING_SHEET_NOTES.md`](TRACKING_SHEET_NOTES.md) explains how to fill it and how to
compute the verdict by hand. [`HW_VALIDATION.md`](HW_VALIDATION.md) records the §3.5 hardware gate.
**The spreadsheet is the primary and only supported path** — §10's app integration is deferred.

---

## 0. The one-page version

| | |
|---|---|
| **Question** | Does a used CE Python loaded with my Python study programs realise more net revenue than an identical bare one? |
| **Design** | **12 matched pairs. 24 units.** Within each pair, one unit is loaded, one is bare, from an arm sequence **committed for all 12 pairs before any unit was in hand** (§2.4). |
| **Realistic yield** | **24 units bought is 9–11 pairs delivered, not 12** — the dud rate and unpairable survivors eat 2–3 pairs. §3.1. Plan the analysis for **10**. |
| **Price differential** | Bare listed at **$78**, loaded at **$90**. A **$12** gross differential. |
| **Platform** | eBay, fixed price with Best Offer, 30-day GTC. Both arms identical format. |
| **Blocking gate** | **§3.5. No loaded unit past the first gets programs until every P6 program has run correctly on real hardware.** This is the only thing standing where the pilot used to stand. |
| **Primary endpoint** | Realised **net revenue per unit listed** = `sale price − platform fees − shipping label`, counted as **$0 if unsold at day 45**. |
| **Decision statistic** | `mean(loaded) − mean(bare)`, paired within pair. |
| **Decide at** | Day 45 after the last pair is listed. Not before. **2026-10-21.** |
| **Keep loading if** | ≥ **+$6.00**/unit |
| **Stop loading if** | ≤ **+$2.00**/unit |
| **Otherwise** | Inconclusive → keep loading, stop planning around a premium |
| **Where it's logged** | [`AB_TEST_LOG.csv`](AB_TEST_LOG.csv), committed and pre-filled. **A spreadsheet is the primary and only supported path** — the app work in §10 is deferred and is not being built. |
| **Honest power** | At n=12 this test **cannot** distinguish a $0 premium from a $10 one. It *can* detect a ≥$15 premium (~98%) and it *can* detect the loaded arm actively underperforming. Going from 10 pairs to 12 moved the minimum detectable effect from **$11.94 to $10.66** — a $1.28 improvement, not a change of category. See §6. |

**The most important sentence in this document:** because loading a unit costs only ~11 extra
minutes ([`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §6), the rational default is **keep loading
unless the test shows harm.** The burden of proof belongs on *stopping*, not on continuing. Design
the test to catch a disaster, not to precisely measure a small win you can't afford to measure.

---

## 1. Hypothesis, and what would actually change the business

### 1.1 The hypotheses, stated formally

Let *Δ* be the true mean difference in realised net revenue per unit listed, loaded minus bare, at a
$12 list-price differential.

- **H₀:** *Δ* = 0. The market pays nothing for pre-loaded programs; the loaded arm's higher price is
  fully offset by worse sell-through or more discounting.
- **H₁:** *Δ* > 0. The market pays something.
- **H₋ (the outcome that matters most):** *Δ* < 0. Pricing $12 higher costs you more in lost and
  delayed sales than the premium earns. **This is the result that changes behaviour immediately.**

### 1.2 The prior, from the existing research

[`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §6 is deliberately pessimistic and its reasoning is
sound. Its base case is a **$5–$12 gross premium, possibly $0**, and it lists three structural
arguments against: teachers clear memory, modifications read as a liability to the median used-goods
buyer, and a preload raises not-as-described exposure. It also notes that the closest competitor
(mcstutoring.com) sells programs at $20–$60 as downloads and **does not sell loaded hardware at any
price** — a decades-experienced operator in this exact niche has evidently concluded it isn't worth
it.

**So go in expecting a small or zero effect.** If the test comes back at +$25 you should suspect a
confound before you believe it.

### 1.3 What each result changes

| Result | Business decision | What changes in practice |
|---|---|---|
| *Δ* ≥ **+$6** | **Keep loading. Make it the default SKU.** | Every prepped CE Python gets P6 loaded before listing. Continue to a 20–30 pair cumulative estimate to tighten the number. Consider testing a *higher* differential ($18) on the next batch. |
| *Δ* between **+$2 and +$6** | **Inconclusive. Keep loading.** | Loading is cheap and the point estimate is positive; continue, but stop treating the premium as a planning input. Price at bare + $8 rather than bare + $12. **Do not fund another 12 pairs to chase this band** — §6.4 shows resolving it needs ~48 pairs, which is not a purchase you should make. |
| *Δ* between **−$2 and +$2** | **Inconclusive-null. Keep loading only as a differentiator, not a price lever.** | Load units because it makes the listing distinctive and it costs 11 minutes — but **price them at the bare comp.** Stop building the premium into `baselinePrice`/`listPrice` planning. Redirect effort to acquisition cost, which §8 of the economics doc says dominates anyway. |
| *Δ* ≤ **−$2** | **Stop loading for price. Sell bare.** | The preload is costing you money. Sell bare units at the bare comp, and push the software as the $12–$49 digital product it already is. Put a discount card in the box instead of programs on the device. |
| **Loaded sell-through ≥ 3 units worse** than bare, at any *Δ* | **Stop loading at $12 regardless of the mean.** | Slow inventory in a seasonal business is a real cost the mean doesn't capture. Retest at a $6 differential or not at all. **Threshold re-checked at n=12 in §7.3 and kept at 3.** |

### 1.4 What this test does *not* answer

Be clear about the boundaries so you don't over-read it:

- It tests **one differential ($12) on one platform (eBay) in one season (late 2026)**. It does not
  produce a demand curve.
- It does not test the **digital** product. That business is separately established and better
  (§10 of the economics doc: one $49 toolkit download nets more than one shipped calculator).
- It does not test **Mercari or local**, where both the fee structure and the buyer are different.
  [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §3 shows Mercari nets ~$5/unit more; a premium
  might land differently with a browse-driven audience. Note it as future work.
- It does not test **loadout choice** (P1 vs P2 vs P6). Twelve pairs cannot resolve two questions —
  §6 shows they can barely resolve one. **Hold loadout constant at P6** — see §3.4.
- It does not, by itself, prove the programs **work on hardware**. That is a product question, not a
  market question, and it is answered before the experiment starts by the gate in **§3.5**. Do not
  let a hardware failure be reported as an A/B result.

---

## 2. Matching — the design decisions that actually determine whether this works

At n=12 your entire ability to learn anything comes from **variance reduction**, not sample size.
§6 shows that halving the within-pair standard deviation is worth more than doubling the number of
pairs — and that the jump from 10 pairs to 12 bought only **$1.28** of detectable effect. Every rule
in this section exists to shrink the noise, and at this sample size they are the experiment.

### 2.1 Match on these, hard

| Factor | Rule | Why |
|---|---|---|
| **Variant** | Both units in a pair must be confirmed **CE Python** (faceplate wordmark *and* About screen). | A plain CE in the bare arm makes the comparison meaningless and is an INAD claim waiting to happen. |
| **Cosmetic grade** | Both units the **same grade** from [`../PREP_SOP.md`](../PREP_SOP.md) §8, and **grade A, B, or C only**. Never pair an A with a B. | Condition is the dominant price driver on used electronics. An unmatched grade will swamp a $12 effect. Grade D is excluded by SOP §8 anyway ("do not load software onto a D"). |
| **Accessories** | Both units either **have slide case + cable**, or **neither does**. Cable is always a new generic one (SOP §9), so in practice: match on **case present / case absent**. | A missing case is a real $6 value hit and buyers notice. |
| **Colour** | Same colour within a pair where possible; if not, record both colours and note it. | Weak effect, cheap to control. Do not reject an otherwise-good pair over colour. |
| **Screen condition** | Both flawless, or both with an equivalent minor flaw that is photographed on both. | The #1 buyer worry. Do not pair a flawless screen against a faintly scuffed one. |
| **Battery** | Both original-and-holding, or both replaced. If one needs a new cell, **replace both** or split the pair. | "New battery installed" is one of the few claims that genuinely moves price (SOP §7). It cannot appear on only one arm. |
| **OS version** | Both flashed to the same current bundle (5.8.5 or later, per SOP §4b). | Standardised by the SOP already. Record it. |
| **Listing format** | Both **fixed price + Best Offer, 30-day GTC**, free shipping, same handling time, same return policy (30-day, buyer pays return shipping). | See §2.3. |
| **Photos** | **Same shot list, same count, same background, same lighting, same order** — [`../LISTING_AND_SUPPORT.md`](../LISTING_AND_SUPPORT.md) §2. | Photo quality is a huge, easily-avoided confound. |
| **Day and time listed** | Both units of a pair go live **in the same drop**, within the same hour, on a **Sunday between 7:00 and 9:00 PM Eastern**. | Removes day-of-week and time-of-day demand effects entirely, and removes any drift in your own seller reputation between the two arms. |
| **Promoted Listings** | **Off, or the same rate on both.** Recommend **off** for the whole test. | 2026 attribution changes made Promoted Listings close to a flat tax on all sales (economics §3). It adds cost and variance without adding information. |

### 2.2 The only differences allowed

The treatment is "loaded, plus the disclosures that loading requires." That bundle is what you would
actually ship, so it is the correct causal contrast. Exactly five things differ:

1. The **programs on the device** (P6 loadout, 10 programs).
2. The **"what's loaded on it" manifest** block in the description, and the two extra photos that go
   with it (Python File Manager; a program running).
3. The **Press-to-Test data-loss warning** and the exam program-removal lines.
4. The **restore link / unit code** on the printed card.
5. The **price**: $78 vs $90.

Everything else — every word, every other photo, every item specific, every policy — is byte-for-byte
identical. Write the bare description first, then produce the loaded description by *adding* blocks,
never by rewriting.

> **Photo-count caveat, and how to neutralise it.** The loaded arm gets 2 more photos, and eBay
> rewards photo count slightly. Neutralise it: give the **bare** arm two extra shots of equal
> informational weight — a second angle of the clean home screen and a `2nd MEM` free-memory shot —
> so both arms have the **same number of photos**. Record the count per listing in the log.

### 2.3 Why fixed price + Best Offer, and not auction

Auction is tempting because the hammer price *is* revealed willingness to pay, with no anchoring
from you. Reject it anyway:

- **Auction variance is much larger.** A $90 item can close anywhere from $45 to $95 depending on
  who happens to be awake. §6 shows the minimum detectable effect scales linearly with that
  standard deviation. High variance at n=12 means you learn nothing.
- **Auctions on eBay systematically under-realise** for a specific-model item with steady demand;
  you would be measuring auction dynamics, not the premium.
- **A fixed differential is a cleaner test of the actual question.** You want to know "if I ask $12
  more, does it still sell?" — which is the decision you face every time you list. Fixed price
  answers exactly that.
- **Best Offer preserves price discovery** without the variance. Buyers who won't pay $90 will offer
  $82, and you learn the shape of the demand.

**Best Offer discipline — pre-commit to this, in writing, now:** accept any offer **≥ 92% of ask**
automatically (set eBay's auto-accept threshold, so you cannot be inconsistent). Auto-decline below
**80%**. Counter everything in between **once**, at the midpoint, then accept or let it lapse. Set
these thresholds identically on both arms.

- Bare arm: ask $78, auto-accept ≥ **$71.76**, auto-decline < **$62.40**
- Loaded arm: ask $90, auto-accept ≥ **$82.80**, auto-decline < **$72.00**

**Using eBay's automatic thresholds rather than your own judgement is not a convenience — it is the
control.** Human offer-handling is exactly where unconscious bias enters ("I'll hold out on the
loaded one, it's worth more"), and it would invalidate the test.

### 2.4 Randomisation — pre-committed for all 12 pairs **[COMPUTED]**

Buying all 24 units at once changes this section's problem. Previously arms could be drawn as units
trickled in; now every pair exists at once, so the assignment must be **fixed before any unit is
graded** or there is no defence against post-hoc allocation. The audit trail this protocol cares
about is the claim *"randomisation was not chosen after I saw the units."* Below is how that claim is
made checkable by a third party rather than merely asserted.

#### Stage 1 — the sequence, committed before the units exist

**Already done. Do not regenerate it.** The sequence below was generated on **2026-08-13**, before
any unit was in hand, and is committed in
[`AB_TEST_LOG.csv`](AB_TEST_LOG.csv) in the `arm` column.

| Parameter | Value |
|---|---|
| Method | `python random.Random(seed)`, `shuffle` on a **balanced** slot list |
| Seed | **`20260813`** |
| Balance | Exactly **6** pairs have unit A loaded and **6** have unit B loaded, so the arms are guaranteed 12/12 rather than 12/12 *on average* |
| Sequence SHA-256 | **`a6fc5ceaa00ba1516adc936b09c10e1b7fbcfaa5e0917fa36d2ada1c5b11dc50`** |

| Pair | Unit A | Unit B | Publish first | Drop |
|---|---|---|---|---:|
| `P01` | **LOADED** | BARE | BARE | 1 |
| `P02` | BARE | **LOADED** | LOADED | 1 |
| `P03` | BARE | **LOADED** | LOADED | 1 |
| `P04` | **LOADED** | BARE | LOADED | 1 |
| `P05` | BARE | **LOADED** | BARE | 1 |
| `P06` | BARE | **LOADED** | BARE | 1 |
| `P07` | **LOADED** | BARE | LOADED | 2 |
| `P08` | **LOADED** | BARE | LOADED | 2 |
| `P09` | BARE | **LOADED** | LOADED | 2 |
| `P10` | BARE | **LOADED** | BARE | 2 |
| `P11` | **LOADED** | BARE | LOADED | 2 |
| `P12` | **LOADED** | BARE | BARE | 2 |

**Why balanced rather than 12 free coin flips.** Independent flips would sometimes hand you an 8–4
split, which wastes pairs you paid for: the paired *t*-test's power depends on the number of
*complete* pairs, and an unbalanced draw does not reduce that, but it does make the arms unequal if
any pair later drops out asymmetrically. Balance costs nothing — assignment *within* each pair is
still random, which is the only place bias could enter — and it removes a way to get unlucky.
`publish_first` is a second, independent draw from the same seeded stream.

#### Stage 2 — binding physical units to the sequence, after grading

The sequence commits `(pair, slot) → arm`. It does **not** and cannot commit which physical
calculator is `P03`'s unit A, because you have to grade a unit before you know what it can be paired
with. So the binding step needs its own rules, applied mechanically:

1. **Grade and record every unit first**, with the arm column ignored — cosmetic grade, colour, case,
   battery, screen notes, serial. Fill those columns in the CSV before you look at the `arm` column.
2. **Form pairs by the §2.1 matching rules only.** Grade is the hard constraint; then screen
   condition, then case, then battery, then colour. Never consider which arm a pair will be.
3. **Assign pair IDs in ascending order of the pair's lower serial number.** The pair containing the
   lowest serial in the batch becomes `P01`, the next `P02`, and so on. Arbitrary, but objective and
   decided in advance.
4. **Within each pair, unit A is the lower serial number.** Unchanged from the original protocol.
5. **Read the arm off the table above.** You are executing a lookup, not making a choice.

Steps 3 and 4 are the load-bearing ones. Every tiebreak is a serial number — a fact about the unit
that you cannot influence and that has no plausible relationship to how well it will sell.

#### Why this preserves the audit trail

Four independent things have to line up, and all four are checkable after the fact:

1. **The seed and method are published**, so anyone can re-run them and confirm the sequence.
2. **The SHA-256 fixes the sequence**, so a later edit to the `arm` column is detectable — recompute
   the hash over the `pair,unitA_arm,unitB_arm,publish_first,drop` block and compare.
3. **`git log` on [`AB_TEST_LOG.csv`](AB_TEST_LOG.csv) is a timestamp you do not control.** The
   commit that introduced the pre-filled arm column predates every acquisition date, listing
   timestamp, and sale in the file. That is the actual proof, and it is stronger than the dated
   printout the original protocol asked for, because you cannot backdate a pushed commit.
4. **`arm_assigned_at` is `2026-08-13` on all 24 rows** and must predate every `listed_at`. If it
   doesn't, something went wrong and the affected pair is excluded and logged.

> **The one rule that makes all of this worth anything:** fill in grade, colour, case, battery,
> screen and serial **before** you read the arm column. The protection is not the randomisation — it
> is that you graded blind to the assignment. If you grade a unit while knowing it is destined for
> the loaded arm, you will grade it generously, and no seed or hash detects that.

**Why this matters more than it looks:** if you choose which unit to load after handling both, you
will load the nicer one. Not deliberately — you just will. Pre-committed randomisation on an
objective tiebreak removes the opportunity.

#### If you end up with fewer than 12 pairs

You probably will — §3.1 says 9–11 is the realistic yield. **Do not reshuffle.** Fill the pair IDs
from `P01` upward and simply leave the unused high-numbered rows empty, marking them
`excluded = TRUE` with `exclusion_reason = NEVER_LISTED_INSUFFICIENT_UNITS`. Dropping the tail of a
pre-committed sequence is unbiased; re-drawing a shorter sequence after seeing how many units
survived is not, because the number of survivors is correlated with their quality.

If you finish with an **odd** number of usable units, the leftover is not a half-pair — list it
outside the experiment with `arm = NOT_IN_TEST` and leave it out of the analysis entirely.

### 2.5 Blocking, and how to allocate pairs across drops

Twelve pairs at once from a new seller looks like a dropshipper and invites eBay's duplicate-listing
suppression. Split into **two drops of six pairs, one week apart**, both on Sunday evening. The drop
assignment is part of the committed sequence in §2.4: **`P01`–`P06` in drop 1, `P07`–`P12` in
drop 2.**

- Drop is a **blocking factor**. Record it. Analyse with drop as a paired block (it already is one,
  since both arms of a pair are always in the same drop).
- **Do not** change anything between drops — not the template, not the photos, not the price. If you
  must change something, drop 1 is excluded and you run drop 2 and drop 3 instead. Say so in the log.
- **Drop assignment interacts with the compressed buy window.** Pairs are numbered by serial, not by
  arrival date, so a late-arriving unit can land in a `P01`–`P06` pair it cannot physically make. If
  that happens, **swap the whole pair with a drop-2 pair** and log the swap with the reason. Swapping
  a *pair* preserves the arm assignment and the pairing; moving a single *unit* between pairs
  destroys both. See [`README.md`](README.md) for the arrival-date cutoff this implies.

### 2.6 The interference problem — read this, it biases the result

Two near-identical listings from the same seller, live at the same time, **compete with each other**.
A buyer who finds both will very often take the cheaper one. This is a genuine violation of the
independence assumption behind the statistics, and it **biases the estimate of Δ downward.**

Three honest responses:

1. **Accept the bias and note its direction.** A positive result under downward bias is *more*
   trustworthy, not less. A null result is ambiguous — it may be interference rather than absence of
   a premium.
2. **Reduce discoverability overlap** where it is free to do so: use the different titles in
   [`LISTING_TEMPLATES.md`](LISTING_TEMPLATES.md) (the bare arm leads with "Tested, Wiped, Updated
   OS"; the loaded arm with "Preloaded Study Programs"), so the two listings rank on partly
   different queries.
3. **Do not** try to hide the pair by listing them weeks apart. That trades a bias you can reason
   about for a seasonality confound you can't.

**Record this as a stated limitation in your write-up.** If the result is null, the correct
conclusion is "no premium detected, possibly attenuated by within-seller competition," not "there is
no premium."

---

## 3. Materials and setup

### 3.1 Units required

| | |
|---|---|
| Units purchased | **24**, all in the Aug 13–24 window |
| Nominal design | **12 pairs** — 24 units ÷ 2 |
| **Realistic delivered design** | **9–11 pairs.** See the yield table below. **Plan on 10.** |
| Target acquisition | **≤$32/unit** ([`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §7 max-pay table, $88 target / $25 target profit) |
| Capital at risk, 24 units at $30–$40 | **$720 – $960** |
| Expected gross recovery at 85% sell-through | **~$1,400 – $1,500** |

#### 24 units is not 12 pairs — the arithmetic **[COMPUTED]**

The instruction was to confirm whether 24 units is the right split for 12 pairs. **It is the right
split, but it is not the right expectation.** [`../SOURCING.md`](../SOURCING.md) §6 budgets a
**10–20% dud rate on untested purchases**, and this design additionally loses units that pass intake
but cannot be *matched* under §2.1's rules.

| Dud rate | Units passing intake | Pairs if every survivor matches | Pairs if 2 survivors are unpairable |
|---:|---:|---:|---:|
| 10% | 21.6 | **10** | 9 |
| 15% | 20.4 | **10** | 9 |
| 20% | 19.2 | **9** | 8 |

Two things follow, and the second one is the point:

1. **To land 12 real pairs you would need to buy about 28–30 units**, not 24. At 24 the modal
   outcome is 10 pairs.
2. **So the move from a 6-unit pilot to a 24-unit buy is not a sample-size increase — it is the
   removal of the pilot.** The old plan was 10 pairs from 24 units; the new plan is 10 pairs from 24
   units, bought sooner and without a shakedown phase. **The statistical position is unchanged.**
   What changed is that the pilot's protection is gone, which is why §3.5 exists and why it is
   blocking rather than advisory.

**A dud is not lost capital, but it is a lost pair.** [`../SOURCING.md`](../SOURCING.md) §6 now
documents a genuine part-out floor — a dud CE Python recovers **$30–$40** from the repair community,
roughly what you paid — so the money comes back. The *pair* does not, and pairs are the unit of
statistical currency here. Budget the dud rate against **the design**, not against the wallet.

**Do not buy extra units mid-window to backfill to 12 pairs.** A unit bought on Aug 22 to replace a
dud arrives too late to be graded, paired and prepped for either drop (see [`README.md`](README.md)),
and the temptation to squeeze it in is exactly how a matched pair becomes an unmatched one. Accept 10.

**The test is not a research expense — it is your inventory.** You were going to buy and sell these
units anyway. The only true cost of running the experiment is the price differential you may be
leaving on the table on the bare arm: 10–12 units × up to $12 = **≤$144**, and less than that after
fees. Frame it that way when it starts to feel expensive.

### 3.2 Prep

Run [`../PREP_SOP.md`](../PREP_SOP.md) unchanged on **both arms**, including all five checklist
steps, with one difference: on bare-arm units, step 4 (programs loaded) is skipped and recorded as
**deliberately skipped**, not as incomplete.

> **Recording a deliberate skip.** In [`AB_TEST_LOG.csv`](AB_TEST_LOG.csv) the bare rows are already
> pre-filled with `prep_programs_loaded = NA_BY_DESIGN`, which is the honest value and needs no
> workaround. **The spreadsheet is the system of record for this test** (§8).
>
> **If you also mirror units into the inventory app**, its schema models the prep checklist as five
> booleans with no "N/A" state, so a bare unit can never show as fully prepped. That fix is specified
> in §10 and is **deferred, not built.** In the meantime tick `programsLoaded` on bare units in the
> app and write `ARM=BARE, no programs loaded by design` in `Item.notes`. Ugly, but it keeps the app's
> "ready to list" logic working. Do **not** leave it unticked, or you will lose track of which units
> are actually ready. **This workaround affects the app only — never write it into the CSV**, where
> the correct value is `NA_BY_DESIGN`.

Everything else is identical: the wipe, the exam-mode clear, the OS+Apps bundle flash, the hardware
verification, the cleaning, the grading, the packaging. **Bare does not mean unprepared.** If the
bare arm ships dirty and un-flashed you are testing refurbishment, not software.

### 3.3 What ships in each box

| Item | Bare arm | Loaded arm |
|---|---|---|
| Calculator, fully charged | ✅ | ✅ |
| Slide case (if matched) | ✅ | ✅ |
| New USB A-to-Mini-B cable | ✅ | ✅ |
| Printed quick-start card | ✅ (hardware side only) | ✅ (full card: manifest + Press-to-Test warning + restore link) |
| Digital-bundle discount card | ✅ — **same card, same code, both arms** | ✅ |
| Bubble mailer + stiffener | ✅ | ✅ |

The discount card goes in **both** arms deliberately. It is a customer-acquisition device
([`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §10), it is not part of the treatment, and putting
it in only one arm would confound the test.

### 3.4 Loadout — hold it constant

**Every loaded unit gets P6 (STEM Sampler).** No exceptions, no buyer's-choice option during the
test, no P1/P2 substitutions. Twelve pairs cannot answer "is loading worth it" *and* "which loadout
sells best" at the same time.

Turn the buyer's-choice option ([`../LOADOUT_STRATEGY.md`](../LOADOUT_STRATEGY.md) §4) **off** for
the duration. It is a real conversion feature and you should ship it later — but it introduces
per-unit variation in what the buyer receives, and variation is the enemy here.

> ### ✅ Resolved 2026-08-13 — P6 re-derived, and now adopted upstream
>
> **This is no longer a contradiction.** [`../LOADOUT_STRATEGY.md`](../LOADOUT_STRATEGY.md) now
> specifies exactly the loadout below, and that document is the authority; this table is retained as
> the derivation.
>
> Two corrections to what this section previously claimed, for the record. First,
> `LOADOUT_STRATEGY.md` had **already** been re-measured against the 52-program / 249,322-byte library
> before this folder was written — the `QUADSOLV`/`DESCSTAT`-era filenames were gone from it, and its
> P6 read `QUAD · LINSOLV · STATS · UNITS · DERIV · SIMPSON · SUVAT · OHMS · GASLAW · TRIG` at
> **35,080 B**, which is the renamed old set. So the "cannot be loaded as written" framing was
> overstated: the files existed, the total was just at the wrong end of the headroom policy.
>
> Second, **the 35,080 B set was compliant on that document's published `Free` column** (16.5 KB,
> computed on-calc) and non-compliant only against the conservative **34,816 B file-byte gate** this
> protocol checks. That ambiguity has been resolved in `LOADOUT_STRATEGY.md` §1: the file-byte gate
> wins where the two readings disagree, which is what makes the substitution below correct rather
> than merely tidy.
>
> **P6 STEM Sampler, as adopted — 10 programs, 33,956 B / 33.2 KB · 66.3% of 50 KB · 16.8 KB free**
> (17.6 KB free on the on-calc convention). Re-measured from `8xv/` on 2026-08-13, unchanged.
>
> | Program | Bytes | Subject |
> |---|---:|---|
> | `QUAD` | 2,033 | Algebra |
> | `LINSOLV` | 2,638 | Linear systems |
> | `STATS` | 3,859 | Statistics |
> | `UNITS` | 4,422 | Cross-subject |
> | `DERIV` | 2,441 | Calculus |
> | `SIMPSON` | 2,645 | Calculus |
> | `SUVAT` | 3,523 | Physics |
> | `OHMS` | 3,375 | Circuits |
> | `PH` | 3,659 | Chemistry — **the one change from the previous P6** |
> | `TRIG` | 5,361 | Trigonometry |
> | **Total** | **33,956** | |
>
> One substantive change: **`PH` (3,659 B) takes the chemistry slot** instead of `GASLAW` (4,783 B).
> The `GASLAW` version totals 35,080 B, which leaves 15.7 KB free on the file-byte reading and
> **breaks the ≥16 KB headroom policy**. Swapping in the smaller chemistry program restores
> compliance with 1.1 KB to spare and costs nothing pedagogically — acid/base and pH is at least as
> commonly used in intro chemistry as the ideal gas law. `GASLAW` is the first swap-in if you ever
> want it back, at the cost of the headroom.
>
> **Re-measure before the batch** (`../LOADOUT_STRATEGY.md` §2 says to, and it was right):
>
> ```powershell
> Get-ChildItem -Recurse -File -Filter *.8xv | Select-Object Name, Length | Sort-Object Length
> ```
>
> If any size has drifted, recheck the total against 34,816 B (the ≥16 KB-free ceiling) before you
> load a single unit — and **use the same 10 files on all 12 loaded units.**

---

## 3.5 The hardware validation gate — BLOCKING

**Read this before you load anything. It is the single most important operational change in the
2026-08-13 revision, and it is the only part of the plan that can still stop the whole loaded arm.**

### 3.5.1 Why this section exists

The repo's `.8xv` AppVars **have never been executed on physical hardware.**
[`../PREP_SOP.md`](../PREP_SOP.md) §5 says so plainly, and the root `README.md` says so too. The
conversion in `tools/py_to_8xv.py` is byte-exact against TI's reference output, which proves the
*container* is right. **It does not prove the program runs.** A byte-perfect AppVar can still contain
a program that raises on import, hangs on input, or returns a wrong number, and none of the repo's
static checks or the desktop QA harness in `qa/` would catch that — they run CPython on a PC, not
MicroPython on a calculator.

The 6-unit pilot existed to find this out on unit 1 for ~$38 of exposure. **Buying 24 units up front
deletes that protection unless loading is sequenced.** Twelve loaded units prepped in a batch, all
carrying the same broken payload, is a twelve-unit recall — plus the returns, the negative feedback,
and the loss of the experiment. This gate restores the pilot's protective function at zero cost: it
does not delay the buy, it delays only *the second loaded unit*.

> **The gate is not part of the experiment. It is a precondition for it.** A failure here is a
> **product bug**, and it must never be written up as an A/B result. If the gate fails, the correct
> statement is "the test did not run," not "loading did not pay."

### 3.5.2 When the gate runs

**On the first unit that arrives and passes SOP §2 intake triage** — whichever unit that is,
regardless of which pair it will eventually join. It does not have to be a loaded-arm unit; the gate
is about the payload, not about the arm. Run it before any pairing is finalised.

That unit is the **gate unit**. Mark it in the CSV with `hw_gate_unit = TRUE`.

```
BLOCKING RULE, stated once, unambiguously:

    Exactly ONE unit gets programs loaded until the gate passes.

    Prep on all other units may proceed through SOP steps 1-3 and 5
    (wipe, exam-mode clear, OS+Apps bundle, clean and grade) freely.

    SOP step 4 (LOAD PROGRAMS) is FROZEN on every other unit
    until hw_gate_status = PASS is recorded.
```

This costs you nothing on the schedule. Loading is 4–5 min/unit and it is the *last* prep step
anyway; everything upstream of it parallelises and can run on all 24 units while the gate is
resolved on one. See [`README.md`](README.md) for how this sits in the calendar.

### 3.5.3 What "pass" means, per program

Run all **ten P6 programs** ([§3.4](#34-loadout--hold-it-constant)). For each one, all four of these
must hold:

| # | Criterion | How you know |
|---|---|---|
| 1 | **Appears and launches** | The program is listed in the Python App's **File Manager**, and running it from the Shell prints its banner without a traceback |
| 2 | **Accepts input** | It reads the keystrokes below without hanging, and its input validation rejects garbage rather than crashing |
| 3 | **Produces the correct known answer** | The output matches the *Expected* column below, digit for digit on the digits shown |
| 4 | **Exits cleanly** | Choosing the program's `0. Quit` returns you to the Shell prompt with no traceback and no frozen screen, and the unit is still responsive afterwards |

**The known-answer inputs are taken from `qa/cases.py`, not invented.** These are the same
expectations the desktop harness asserts, so a mismatch on-device is a real
platform difference rather than a disagreement between two sets of made-up numbers. The `qa/` case
label is cited so you can find the derivation comment above it.

| # | On-calc | Source | Keystrokes / input | Expected output | From |
|---|---|---|---|---|---|
| 1 | `QUAD` | `algebra_linear_stats/quadratic_solver.py` | `1`, `-3`, `2` | `x1 = 2.0`, `x2 = 1.0`, "Two distinct real roots" | `qa/cases.py` — *quadratic two real roots 2 and 1* |
| 2 | `LINSOLV` | `algebra_linear_stats/linear_system_solver.py` | `2` then `1,1,3` then `1,-1,1` | `x = 2.0`, `y = 1.0` | `qa/cases.py` — *2x2 system* |
| 3 | `STATS` | `algebra_linear_stats/descriptive_stats.py` | `2,4,4,4,5,5,7,9` | `Mean = 5.0`, `Median = 4.5`, `Population variance (n) = 4.0`, `Population std dev (n) = 2.0` | `qa/cases.py` — *descriptive stats classic data set* |
| 4 | `UNITS` | `chemistry_and_exam_tools/unit_converter.py` | `5` (temp), `1`, `2`, `100` | `212.0` | `qa/cases.py` — *temperature 100 C → 212 F* |
| 5 | `DERIV` | `calculus/derivative_numeric.py` | `x**3`, `2`, `0.001` | `12.000001` | `qa/cases.py` — *derivative x^3 at 2* |
| 6 | `SIMPSON` | `calculus/simpsons_rule.py` | `x**2`, `0`, `3`, `6` | `9.0` **exactly** | `qa/cases.py` — *Simpson x^2 on [0,3]* |
| 7 | `SUVAT` | `physics_engineering/kinematics_solver.py` | `2` (solve v), `0`, `9.81`, `2` | `19.62` | `qa/cases.py` — *kinematics solve v* |
| 8 | `OHMS` | `physics_engineering/ohms_law_circuits.py` | `1`, `1`, `2`, `5` | `10.0` | `qa/cases.py` — *ohms law V = I*R* |
| 9 | `PH` | `chemistry_and_exam_tools/acid_base_calculator.py` | `1`, `1`, `0.001` | `pH  = 3.0`, `pOH = 11.0`, "acidic" | `qa/cases.py` — *pH from [H+] = 0.001* |
| 10 | `TRIG` | `trigonometry/oblique_triangle_solver.py` | `2` (SAS), `3`, `4`, `90` | `Side c (opposite C) = 5.0` | **No `qa/` case exists** — from [`LISTING_TEMPLATES.md`](LISTING_TEMPLATES.md) §7.2 |

Three notes on that table, because the details matter:

- **`TRIG` is the one program with no automated coverage.** It is not in `qa/cases.py` or
  `qa/cases_new.py` — the trigonometry case there covers `UNITCIRC`
  (`unit_circle_reference.py`), a different program. `TRIG` is
  `oblique_triangle_solver.py`. Its known answer is the 3-4-5 right triangle from
  `LISTING_TEMPLATES.md` §7.2, entered through the **SAS** branch, and it is arithmetically
  unambiguous (c² = 9 + 16 − 2·3·4·cos 90° = 25). **Treat `TRIG` as the highest-risk program in P6**
  — largest file at 5,361 B and the only one with no desktop test.
- **Two entries deliberately differ from `LISTING_TEMPLATES.md` §7.2.** For `SIMPSON`, §7.2 uses
  ∫₀¹x² dx = 0.3333, but the `qa/` case uses ∫₀³x² dx = **9.0 exactly** — Simpson's rule is exact for
  quadratics, so an exact integer is a far better verification target than a repeating decimal you
  have to eyeball. For `PH`, §7.2 checks pH 4 only, while the `qa/` case also pins `pOH` and the
  acidic/basic classification. **Use the `qa/` values for the gate.** §7.2's card stays as-is for the
  photo-4 shot, which is a different job.
- **Test both payload formats on the gate unit.** This is the diagnostic that tells you *where* a
  failure lives, and [`../PREP_SOP.md`](../PREP_SOP.md) §5 already asks for it. Send `QUAD` **twice**
  — once as `8xv/algebra_linear_stats/QUAD.8xv`, and once as the raw
  `algebra_linear_stats/quadratic_solver.py`, letting TI Connect CE do its own conversion. Run both.
  Their behaviour separates the two failure modes in §3.5.4.

### 3.5.4 On failure — what is broken, and what you do

Read the two-format result first; it localises the fault immediately.

| `.8xv` | `.py` | Diagnosis | Action |
|---|---|---|---|
| ✅ | ✅ | Converter and source both fine | **Gate passes.** Record it, then proceed |
| ❌ | ✅ | **`tools/py_to_8xv.py` is wrong.** Byte-exact container, bad payload in practice | **Fall back to `.py` for all 12 loaded units.** The loaded arm proceeds. See below |
| ❌ | ❌ | **The program source is wrong**, or the program uses something MicroPython on the CE doesn't have | **The loaded arm is blocked.** See below |
| ✅ | ❌ | Very unlikely; suspect a TI Connect CE conversion quirk | Use `.8xv`, and log it — this is a genuinely novel finding |

#### If only `.8xv` fails — fall back, do not stop

This is the **expected** failure mode if there is one, and it is not serious.
[`../PREP_SOP.md`](../PREP_SOP.md) §5 already names `.py` the default and the validated path, and
[`../EVO_TRANSITION.md`](../EVO_TRANSITION.md) established `.py` as the portable format that survives
the Evo transition — the Evo's Python AppVar extension is `.8xv2` and will not accept `.8xv` at all.

1. Set `payload_format = PY` on **all 12** loaded rows. It must be identical across the arm — a mixed
   arm is a second uncontrolled variable inside the treatment.
2. Send `.py` sources via TI Connect CE, which converts on transfer.
3. Re-run the full ten-program gate on the `.py` payload. **It has to pass on the format you ship.**
4. The experiment proceeds on schedule. `.8xv` is a convenience layer, not the product.

#### If both formats fail — the loaded arm is blocked

**Stop. Do not load the other 11 units, and do not list a loaded arm.** This is the outcome the
pilot was designed to catch, and catching it on unit 1 is the gate working, not the gate failing.

1. **Diagnose per program.** A single failing program is very different from all ten failing. If nine
   pass and only `TRIG` fails, the fix is to **substitute `TRIG` out of P6** and re-run the gate — a
   change to the loadout *before the freeze* is legitimate. `GASLAW` (4,783 B) is the documented
   swap-in candidate (§3.4), and dropping `TRIG` (5,361 B) leaves ample headroom.
2. **If the failure is broad**, the loaded arm cannot ship. Then:
   - **Sell all 24 units bare.** The inventory is fine — bare units were always the fallback
     business, [`README.md`](README.md) has said so from the start, and you lose no capital.
   - **Record the outcome as `GATE_FAILED`, not as a Δ̂.** Set `excluded = TRUE` and
     `exclusion_reason = HW_GATE_FAILED` on every row. **The experiment did not run.** Writing this up
     as "the premium is zero" would be the single worst analytical error available in this document.
   - **The A/B question stays open.** Re-run it next season once the programs are fixed.
3. **Fix the product, then feed it back.** The result belongs in `bundles/FILE_FORMAT_NOTES.md` and
   the root `README.md`'s "not tested on physical hardware" caveat either way — that is outside this
   folder's scope, so log it here and hand it over.

> **Escape hatch, so a fixable bug does not kill a season:** the freeze date is **Aug 23** and drop 1
> is **Aug 30**. If the gate fails on a *single program* and you can substitute it before Aug 23, do
> that and re-run the gate. **After Aug 23, no loadout changes** — if the gate is still failing on
> Aug 23, the loaded arm does not ship and everything sells bare. That is a real deadline; put it in
> the calendar.

### 3.5.5 Where the result is recorded

Three places, all of them cheap:

1. **[`AB_TEST_LOG.csv`](AB_TEST_LOG.csv)**, on the gate unit's row: `hw_gate_unit = TRUE`,
   `hw_gate_status` ∈ `PASS` / `FAIL_8XV_ONLY` / `FAIL_BOTH` / `PASS_AFTER_SUBSTITUTION`,
   `hw_gate_date`, and the chosen `payload_format`. Then write the **same `payload_format` into all
   12 loaded rows**, because it is a property of the arm.
2. **A per-program record**, because "it passed" is not auditable and this is the one hardware fact
   the whole repo is missing. Ten lines is enough — append them to
   [`HW_VALIDATION.md`](HW_VALIDATION.md), which exists for exactly this and has the table ready:

   ```
   2026-08-__  gate unit serial ____  OS ____  TI Connect CE version ____
   PROGRAM   FORMAT  LAUNCH  INPUT  KNOWN-ANSWER  CLEAN EXIT  NOTES
   QUAD      8xv     pass    pass   2.0 / 1.0     pass
   QUAD      py      pass    pass   2.0 / 1.0     pass
   ...
   ```

3. **Photograph the `TRIG` and `SIMPSON` results on-screen.** They are the two with the weakest
   desktop coverage — `TRIG` has none — and a photo is proof rather than recollection. Costs 20
   seconds.

**Then tick the gate line in §11's pre-flight checklist.** Nothing downstream of it is valid until
that tick is real.

---

## 4. Metrics

### 4.1 Primary endpoint

> **Realised net revenue per unit listed**
> `net = sale_price − platform_fees − shipping_label_cost`
> **`net = 0` if the unit has not sold by day 45.** A returned unit is `net = 0` and the return
> costs are logged separately.

**Decision statistic:** `Δ̂ = mean(net_loaded) − mean(net_bare)`, computed on the within-pair
differences — 12 of them if all 12 pairs are delivered, and however many you actually have if not
(§3.1 expects 9–11).

Three deliberate choices worth defending:

1. **Actual fees, not modelled fees.** Pull `platform_fees` and `shipping_label_cost` from the real
   eBay payout statement per order, into the CSV columns of the same name. Do not use the 16.55%
   model from [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §3 — one of the open questions in that
   document is whether eBay US now applies a flat 5% used-goods rate, and this test is a free
   opportunity to settle it from a real statement.
2. **No 5% returns reserve.** That reserve is a planning device. Here, returns are observed events
   and are logged as such.
3. **Unsold counts as zero, not as missing.** This is the crux. If you analyse only sold units you
   are conditioning on the outcome, and a price differential that kills sell-through will look like
   a *win*. Counting unsold as $0 revenue folds price and sell-through into one honest number.

**Sanity check on the expected magnitude.** Using the model's own fee stack (13.6% + $0.40, no
promoted, $5.50 label):

| Arm | Ask | Fees | Label | Net | |
|---|---:|---:|---:|---:|---|
| Bare | $78 | $11.01 | $5.50 | **$61.49** | |
| Loaded | $90 | $12.64 | $5.50 | **$71.86** | |
| | | | | **+$10.37** | if every unit sells at ask in both arms |

So the **maximum** *Δ* this design can produce is about **+$10.4**, and only if the market pays the
full $12 with no sell-through penalty. Note what that means: **the decision threshold of +$6 is 58%
of the maximum possible result.** The test is asking "does the market pay at least 58% of the asked
premium?" — a reasonable question, but be aware the ceiling is low and the resolution (§6) is
coarse.

### 4.2 Secondary endpoints

| Metric | Definition | Why | Analysis |
|---|---|---|---|
| **Sell-through at 45 days** | Sold / listed, per arm | The metric with the most decision value at this n (§6.6). Slow inventory in a seasonal business is a real cost. | Discordant pairs, exact binomial (McNemar) |
| **Days-to-sale** | `sold_at − listed_at`, in days, sold units only | Leading indicator of demand at the asked price. Censored at 45 for unsold. | Wilcoxon signed-rank on pairs where both sold; report the censoring |
| **Realised price, conditional on sale** | `sale_price` for sold units | Shows how much of the $12 survived Best Offer haggling | Paired t / Wilcoxon on pairs where both sold. **Do not use as the primary endpoint** — it conditions on the outcome |
| **Sell-through at 30 days** | Sold / listed | Interim only. **Look at it, do not decide on it** (§5.3) | Descriptive |

### 4.3 Leading indicators — collect them, don't decide on them

| Metric | When | Source |
|---|---|---|
| Impressions, page views | Day 7 and day 21 | eBay Seller Hub → Listings → per-listing traffic |
| Watchers | Day 7, day 14, day 45 | Listing page |
| Offers received, and the amount of each | Continuous | Offer thread |
| Questions asked, and whether about the programs | Continuous | Message thread |

**Watchers are the classic trap.** They correlate strongly with *low price*, so the bare arm will
usually win on watchers, and that tells you almost nothing about the premium. Views and watchers
are useful for diagnosing *why* a result happened — "the loaded listing got the same views but a
third of the offers" is a real insight — but they are **not** endpoints, and a pre-registered
protocol does not let you promote them to endpoints after the fact.

Questions about the programs are the one qualitative signal genuinely worth reading. If nobody ever
asks about them, that is evidence the story isn't landing at all.

---

## 5. Timeline and run length

### 5.1 The schedule

Anchored to the seasonality in [`../SOURCING.md`](../SOURCING.md) §4 and
[`../LISTING_AND_SUPPORT.md`](../LISTING_AND_SUPPORT.md) §8: peak sell-side is **late July → mid
September**, and it is already 2026-08-12.

| Phase | Dates | What happens |
|---|---|---|
| **Buy** | Aug 13 – Aug 24 | Acquire 24 units per [`SOURCING_SHORTLIST.md`](SOURCING_SHORTLIST.md). Log every purchase. **Anything bought after ~Aug 20 online will not make drop 1** — see [`README.md`](README.md) for the arrival maths. |
| **Hardware gate** | On first unit's arrival | **§3.5. Blocking.** Ten programs, both payload formats, on one unit. No other unit gets programs until it passes. |
| **Intake + grade** | as units arrive | SOP §2 triage, grade, serial, photos-as-received. Fill the CSV's intake columns **before reading the arm column** (§2.4). |
| **Pair + bind** | by **Aug 26** | Apply §2.4 stage 2: match into pairs, number by serial, read arms off the committed table. |
| **Freeze** | **Aug 23** | Template, photos, prices, thresholds and loadout **locked**. The arm sequence was already locked on Aug 13. Nothing changes after this date. |
| **Prep** | Aug 20 – Sep 4 | Two batches of 12. SOP §10 timings — ~13.4 bench hours total for 24 units. Fits; see [`README.md`](README.md). |
| **Drop 1** | Sun **Aug 30**, 7–9 PM ET | Pairs `P01`–`P06`. 12 listings. |
| **Drop 2** | Sun **Sep 6**, 7–9 PM ET | Pairs `P07`–`P12`. 12 listings. |
| **Observation** | to **Oct 21** | 45 days after drop 2. Collect data weekly. Change nothing. |
| **Interim look** | Oct 6 | Descriptive only. **No decisions.** See §5.3. |
| **Decide** | **Oct 21** | Apply §7. Write it up. |

**There is no pilot phase any more.** The owner's decision to buy 24 up front removed it. Its two
functions have been reassigned explicitly, and neither is optional:

- **Validating that the software works** → **§3.5**, the blocking hardware gate. Stronger than the
  pilot was, because it is a defined pass/fail on ten programs rather than "prep four units and see."
- **Shaking down prep, photos, packing and shipping** → **the first pair you prep is the shakedown,
  and it is inside the experiment.** This is a genuine loss and it should be named: there is no
  longer a throwaway batch on which to make first-timer mistakes. Mitigation: prep the gate unit and
  its eventual partner **first and slowly**, weigh the parcel, build a full listing as a draft
  without publishing it, and fix what's wrong before touching the other 22. A draft listing costs
  nothing and recovers most of the pilot's value.

### 5.2 Why 45 days, and what it costs you

45 days is a compromise, and both sides of it are real:

- **Shorter (30 days) is cleaner seasonally** — it keeps the whole window inside the demand tail —
  **but** it censors more units as unsold, which inflates variance on the primary endpoint and makes
  a null result harder to interpret.
- **Longer (60–90 days) resolves more sales** but drags deep into the thin
  October–November window ([`../SOURCING.md`](../SOURCING.md) §4), where *both* arms sell slowly.

45 days keeps most of the window in usable demand while giving genuinely slow units a chance to
clear. **Pre-commit to it.**

> **Accept this limitation openly:** drop 2 + 45 days runs to Oct 21, which is past peak. Absolute
> sell-through in this test will look worse than a true August cohort would. **The paired contrast is
> still valid** — both arms of every pair face the identical demand curve, which is the entire point
> of pairing — but **do not quote the absolute sell-through number as your seasonal expectation.**

### 5.3 The interim look, and the rule about it

You will look at the data on Oct 6. Pretending otherwise is unrealistic. So define the rule now:

- **The Oct 6 look is descriptive only.** Record it. Do not act on it.
- **You may stop the test early for exactly one reason:** a **safety stop** — if by day 30 the
  loaded arm has sold **≤1 of 12** while the bare arm has sold **≥7 of 12**, stop, relist the
  remaining loaded units at the bare price, and record a *Δ* ≤ −$2 outcome. That is a large enough
  gap to be real, and continuing would cost you inventory turns in a declining season.

  > **Rescaled from n=10, holding the gap constant in proportion.** The original rule was ≤1 of 10
  > against ≥6 of 10 — a **50-percentage-point** gap. At 12 pairs, ≤1 vs ≥7 is 8% vs 58%, which is the
  > same 50 points, so the rule is exactly as hard to trigger as it was. **[COMPUTED]** If you end up
  > with 10 or 11 pairs instead of 12, use the proportional form — **loaded ≤10% while bare ≥60%** —
  > rather than re-deriving counts.
- **You may not** stop early because the result looks good, extend the test because it doesn't,
  change the price, change the thresholds, or drop a pair.

**Why the rule is strict:** repeatedly testing accumulating data ("optional stopping") drives the
false-positive rate far above 5% — with a few looks it can exceed 20%. With n=12 and a true effect
you can't resolve anyway, optional stopping would essentially guarantee you conclude whatever you
were hoping for. The one asymmetric exception above is deliberate: it only triggers on the outcome
where continuing costs real money, and it requires a gap far larger than noise.

---

## 6. Statistical power at n=12 — the honest treatment

**This is the section to read if you read only one.** It is also the section that will make you want
a bigger test, and you should let it.

**Recomputed from scratch on 2026-08-13 for n=12.** Not scaled from the old n=10 figures — the
critical values, the noncentral-*t* power integrals and the exact binomial tests were all
re-evaluated. Method and a note on why some old numbers moved are in §6.8.

### 6.1 The design

Twelve matched pairs is a **paired** design, analysed on the 12 within-pair differences
*d*ᵢ = net(loaded)ᵢ − net(bare)ᵢ. Pairing is the right choice: it removes between-unit variation
(condition, colour, accessories, listing week) from the error term, which is why the matching rules
in §2.1 are not optional bureaucracy — they *are* the power of the study.

**Read every number below as an upper bound.** §3.1 expects **9–11** delivered pairs from 24 units,
not 12. The n=9 and n=11 columns are shown throughout so you can find your real position.

### 6.2 What n=12 can detect **[COMPUTED]**

For a two-sided paired *t*-test at α = 0.05 with 80% power and n = 12 (df = 11):

```
required standardised effect  d_z = (t₀.₀₂₅,₁₁ + t₀.₂₀,₁₁) / √n
                                  = (2.2010 + 0.8755) / √12
                                  = 3.0765 / 3.4641
                                  = 0.8881
```

So the **minimum detectable effect is about 0.89 × the standard deviation of the pair differences**,
down from 0.99 at n=10. The same calculation across the plausible yield range:

| n (pairs) | df | t₀.₀₂₅ | t₀.₂₀ | **d_z at 80% power** | CI half-width multiplier |
|---:|---:|---:|---:|---:|---:|
| 9 | 8 | 2.3060 | 0.8889 | **1.0650** | 0.7687 × σ_d |
| 10 | 9 | 2.2622 | 0.8834 | **0.9947** | 0.7154 × σ_d |
| 11 | 10 | 2.2281 | 0.8791 | **0.9369** | 0.6718 × σ_d |
| **12** | **11** | **2.2010** | **0.8755** | **0.8881** | **0.6354 × σ_d** |

Everything then hinges on σ_d — which you do not know yet, and which this test will measure as a
by-product. In dollars, at 80% power:

| σ_d scenario | Plausible if… | MDE at n=9 | MDE at n=10 | **MDE at n=12** |
|---|---|---:|---:|---:|
| **$6** | Tight matching, fixed price, most units sell, little haggling | $6.39 | $5.97 | **$5.33** |
| **$12** | Realistic base case — some haggling, 1–2 unsold per arm | $12.78 | $11.94 | **$10.66** |
| **$20** | Loose matching, or 3+ unsold units per arm swinging pairs by $60+ | $21.30 | $19.89 | **$17.76** |

**[ESTIMATE]** — the σ_d values are my modelling, not measured. There is no published variance
figure for this. Report your observed σ_d in the write-up; it is the most valuable number the test
produces, because it tells you how many pairs a *real* measurement would need.

**What the extra two pairs bought you: $1.28.** At the base-case σ_d = $12 the minimum detectable
effect went from **$11.94 to $10.66.** That is the entire statistical return on adding 4 units to the
design. It is not nothing, but it does not change what the test can conclude, and it is worth knowing
before you interpret a result as though 24 units bought you a real measurement.

### 6.3 Power against the effect sizes we actually expect **[COMPUTED]**

Exact noncentral-*t*, α = 0.05 two-sided. Base case σ_d = $12:

| True Δ | d_z | n=9 | n=10 | n=11 | **n=12** | Plain reading |
|---:|---:|---:|---:|---:|---:|---|
| $2 | 0.17 | 7% | 8% | 8% | **8%** | Invisible |
| **$5** | 0.42 | 20% | 22% | 24% | **26%** | **A real $5 premium is missed 3 times out of 4** |
| $6 | 0.50 | 26% | 29% | 32% | **35%** | Below a coin flip *at your own decision threshold* |
| $8 | 0.67 | 42% | 47% | 51% | **56%** | Coin flip |
| **$10** | 0.83 | 59% | 65% | 70% | **75%** | Favourable, not reliable |
| $12 | 1.00 | 75% | 80% | 85% | **88%** | Detectable |
| $15 | 1.25 | 91% | 94% | 96% | **98%** | Comfortably detectable |
| $20 | 1.67 | 99% | 100% | 100% | **100%** | Obvious |

And under the other two variance scenarios at n=12:

| σ_d | Δ=$2 | Δ=$5 | Δ=$10 | Δ=$15 | Δ=$20 |
|---:|---:|---:|---:|---:|---:|
| $6 | 18% | **75%** | 100% | 100% | 100% |
| $20 | 6% | **12%** | 35% | 66% | 88% |

#### The answer to the question you were told to ask plainly

**No. Twelve pairs still cannot detect the $5–$12 premium
[`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §6 expects.** At the base-case variance the power
across that range runs from **26% at $5 to 88% at $12**, and the bottom two-thirds of the range —
$5 through $10 — sits at **26%–75%**, i.e. more likely to be missed than found for most of it. The
conclusion of the original n=10 analysis survives the extra pairs intact.

**And there is a sharper version of the problem that the larger sample makes visible.** §4.1 computes
this design's **maximum attainable** Δ: if every unit in both arms sells at full ask, the difference
in net revenue is **+$10.37**. Put that next to the base-case MDE:

```
    maximum effect the design can even produce   =  +$10.37
    minimum effect it can detect at 80% power    =  +$10.66   (sigma_d = $12, n = 12)
                                                    ---------
    the detection threshold EXCEEDS the ceiling by  $0.29
```

**At the base-case variance, this test cannot reach 80% power against any outcome it is physically
capable of producing.** Power at the $10.37 ceiling is **77.8%** at n=12 (68.2% at n=10) — close to
80%, but that is the power against the *best case where nothing goes wrong in either arm*, which is
not a case that happens. Power at the **+$6 decision threshold itself is 35.3%.**

That is not a reason to skip the test, and it is not a reason to buy more units — §6.4 shows what
"more" would have to mean. It is a reason to know in advance what a "not significant" result means:
**absence of evidence, not evidence of absence.** And it is the reason §7.3 concludes the decision
rule should be read as a **screening rule on the point estimate**, not as a significance test.

### 6.4 How many pairs a real measurement would take **[COMPUTED]**

Pairs needed for 80% power, two-sided α = 0.05:

| True Δ | σ_d = $6 | σ_d = $12 | σ_d = $20 |
|---:|---:|---:|---:|
| $5 | 14 | **48** | 128 |
| $10 | 6 | **14** | 34 |
| $15 | 4 | 8 | 16 |

**Read the σ_d = $12 column.** Confirming a $5 premium would take **48 pairs — 96 units** and most
of a season's capital. That is not a decision you should fund, and knowing so is genuinely
actionable: **stop trying to measure a $5 premium and go work on acquisition cost instead**, which
§8 of the economics doc says moves profit far more anyway.

**Note what the $10 row says about the buy you just made.** Detecting a $10 effect at 80% power needs
**14 pairs — 28 units.** You bought 24, which yields 9–11 pairs in practice (§3.1). **You are 3–5
pairs short of being adequately powered against even the top of the expected range**, and the gap is
6–12 units of acquisition. If there is one argument for buying a few more units, that is it — but it
is an argument for **28–30 units**, not for 24, and the buy window makes that a decision for next
season rather than this one.

**Now read across the rows.** Halving σ_d from $12 to $6 cuts the pairs needed for a $10 effect from
14 to 6 — **a bigger gain than doubling the sample.** This is the whole argument for §2's matching
discipline, the auto-accept thresholds, and the identical photo counts. **Variance reduction is the
cheapest statistical power available to you, and it is free.** Going from 10 pairs to 12 bought $1.28
of MDE; tightening matching enough to halve σ_d would buy $5.33.

### 6.5 The confidence interval is the number to report

Significance testing is the wrong frame for a business decision. Report the interval.

95% CI half-width = `t₀.₀₂₅,₁₁ × σ_d / √n = 2.2010 × σ_d / 3.4641 = 0.6354 × σ_d` **[COMPUTED]**

| σ_d | Half-width at n=12 | If you observe Δ̂ = **+$10**, the 95% CI is… | What you can honestly say |
|---:|---:|---|---|
| $6 | ±$3.81 | **[+$6.2, +$13.8]** | "Between $6 and $14. Above my $6 keep-loading threshold across the whole interval. **Act on it.**" |
| $12 | ±$7.62 | **[+$2.4, +$17.6]** | "Somewhere between negligible and excellent. Technically significant, **practically useless.**" |
| $20 | ±$12.71 | **[−$2.7, +$22.7]** | "I learned nothing." |

**Stare at the middle row.** A statistically significant *p* < 0.05 result at n=12 with realistic
variance still leaves you unable to tell $2 from $18. **A significant result is not the same as an
answer**, and this is exactly how a small A/B test fools a careful person: the *p*-value gives
permission to believe a point estimate the data cannot support. At n=10 that interval was
[+$1.4, +$18.6]; two more pairs narrowed it by about a dollar at each end.

### 6.6 Sell-through is the better-powered endpoint at this n **[COMPUTED]**

Because sell-through is binary, the paired analysis (McNemar / exact binomial on discordant pairs)
has clean small-sample properties. Exact two-sided *p*-values:

| Discordant pairs (D) | Splits and their exact *p* |
|---:|---|
| 6 | 6–0: **0.031** · 5–1: 0.219 |
| 7 | 7–0: **0.016** · 6–1: 0.125 |
| 8 | 8–0: **0.008** · 7–1: 0.070 · 6–2: 0.289 |
| 9 | 9–0: **0.004** · 8–1: **0.039** · 7–2: 0.180 |
| 10 | 10–0: **0.002** · 9–1: **0.021** · 8–2: 0.109 |
| 11 | 11–0: **0.001** · 10–1: **0.012** · 9–2: 0.065 |
| 12 | 12–0: **0.0002** · 11–1: **0.006** · 10–2: **0.039** · 9–3: 0.146 |

And on the simple "which arm sold more" sign test over all 12 pairs: **12–0 gives *p* = 0.0005,
11–1 gives *p* = 0.006, 10–2 gives *p* = 0.039, and 9–3 gives *p* = 0.146.**

**This is where the extra two pairs actually helped.** At n=10 you needed 9 of 10 in one direction
(*p* = 0.021) for significance and 8 of 10 was not enough (*p* = 0.11). At n=12 **10 of 12 clears it**
(*p* = 0.039) — so the binary endpoint gained a genuine tolerance for one discordant pair that the
continuous endpoint did not gain anything comparable to. Worth noting, because it is the one place
where 24 units bought a real improvement rather than a rounding difference.

So sell-through still needs **near-total consistency** to be significant — but that is exactly the
signature of the result that matters most. **If pricing $12 higher genuinely breaks sell-through, it
will break it in most pairs, and this test will see it.** That asymmetry is the strongest thing
about the design: it is well-powered against disaster and poorly powered against a small win. Given
that loading costs 11 minutes and the default is to keep doing it, **being well-powered against
disaster is the correct thing to be well-powered against.**

### 6.7 Method, and why two old numbers moved **[COMPUTED]**

Stated so the arithmetic can be checked rather than trusted:

- **Critical values** are exact Student-*t* quantiles, obtained by inverting the *t* CDF. They were
  validated against published tables before anything else was computed — t₀.₉₇₅,₉ = 2.2622,
  t₀.₉₇₅,₁₁ = 2.2010, t₀.₈₀,₉ = 0.8834 all reproduce to four decimal places.
- **Power** is the **exact noncentral-*t*** tail, `P(|T'(df, ncp)| > t₀.₀₂₅,df)` with
  `ncp = (Δ/σ_d)·√n`, evaluated by quadrature over the chi distribution. It is not a normal
  approximation.
- **Sign test and McNemar** *p*-values are exact binomial, summing all outcomes no more likely than
  the observed one.
- **Sell-through false-trigger rates** (§7.3) are computed by enumerating the number of discordant
  pairs and the split within them.

> **Two numbers in the previous version of this section were slightly low, and the correction goes
> against interest.** The old n=10 table reported ~18% power at Δ=$5 and ~62% at Δ=$10; the exact
> noncentral-*t* values are **22%** and **65%**. The old figures came from a normal approximation,
> which understates power at small df. The like-for-like comparison — exact against exact — is
> therefore **22% → 26%** at $5 and **65% → 75%** at $10 going from 10 pairs to 12. The old n=10 MDE
> of "≈$12" was right: it is $11.94.
>
> This is recorded rather than quietly fixed because the direction matters. **The test is very
> slightly better than the previous section claimed, and still not good enough to measure the effect
> we expect.** Correcting a number in the direction you'd like it to go, and finding the conclusion
> unchanged, is the outcome you want from a re-derivation.

### 6.8 Seven ways to fool yourself, and the countermeasure for each

| Trap | What it looks like | Countermeasure |
|---|---|---|
| **Optional stopping** | "The loaded ones are winning, I'll call it now" | §5.3. One pre-defined safety stop, otherwise decide on Oct 21 |
| **Dropping inconvenient pairs** | "That buyer was weird, doesn't count" | **Intent-to-treat.** Every listed pair is analysed as assigned, forever. A pair is excluded only if a unit was never listed at all, and the exclusion is logged with the reason and the date |
| **Post-hoc endpoint swapping** | Price shows nothing, so you report watchers | Endpoints are fixed in §4. Everything else is exploratory and must be labelled exploratory |
| **Conditioning on the sale** | Comparing only units that sold | Primary endpoint counts unsold as $0. Always report both |
| **Unequal effort** | Answering the loaded arm's messages faster; holding out on offers | Auto-accept/decline thresholds (§2.3); template replies; a 24-hour response standard on both arms |
| **Reputation drift** | Later listings sell better as feedback accumulates | Both arms of a pair always list in the same hour |
| **Reading noise as signal** | "Loaded sold in 4 days, bare took 19 — huge!" | n=1 is an anecdote. Report the CI (§6.5), not the best pair |

**The eighth, and the hardest: you want the premium to be real.** You wrote the programs. Every
unconscious thumb on the scale points the same way. That is precisely why the thresholds, the
randomisation sequence, and the offer-acceptance rules must all be written down *before* the first
unit is listed — so that on Oct 21 you are reading a rule, not making a decision.

---

## 7. The decision rule — pre-registered

**Fill in the blanks below on Oct 21 and follow the row you land in. Do not amend this table after
2026-08-23.**

### 7.1 Primary rule

Compute `Δ̂ = mean(net_loaded) − mean(net_bare)` over all delivered pairs, unsold = $0, and its 95%
CI. Step-by-step spreadsheet arithmetic is in
[`TRACKING_SHEET_NOTES.md`](TRACKING_SHEET_NOTES.md) §4.

| Condition | Verdict | Action |
|---|---|---|
| `Δ̂ ≥ +$6.00` | **KEEP LOADING** | P6 becomes the default on every prepped CE Python. List at bare + $12. |
| `+$2.00 ≤ Δ̂ < +$6.00` | **INCONCLUSIVE — LEAN KEEP** | Keep loading. Drop the differential to **+$8**. Stop treating the premium as a planning input. **Do not fund another 12 pairs to resolve this band** — §6.4 prices that at ~48 pairs. |
| `−$2.00 < Δ̂ < +$2.00` | **INCONCLUSIVE — NULL** | Keep loading (11 min, listing differentiation) but **price at the bare comp**. Set `baseline_price = list_price`. Stop modelling a premium. Redirect effort to acquisition cost. |
| `Δ̂ ≤ −$2.00` | **STOP LOADING FOR PRICE** | Sell bare at the bare comp. Push the digital bundles instead; put the discount card in every box. |

**Overriding condition, applied first:** if **loaded sell-through is ≥3 units below bare**
(e.g. bare 10/12, loaded 7/12), the verdict is **STOP LOADING AT $12** regardless of `Δ̂`. Retest at
a $6 differential or not at all. Rationale: a mean that looks acceptable while inventory sits is
hiding a carrying-cost problem the endpoint doesn't price, and this is a seasonal business where
unsold stock in October is worth less than unsold stock in August.

**Prerequisite, applied before either of the above:** if `hw_gate_status` is not `PASS` or
`PASS_AFTER_SUBSTITUTION` (§3.5), **there is no verdict.** The experiment did not run. Do not compute
`Δ̂`.

### 7.2 Why the thresholds are $6 and $2

Both are grounded in the marginal labour, not picked for roundness. Loading adds **~11 min/unit**
([`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §6) = 0.183 h.

| Δ̂ | Marginal $/hr on 11 min | Compare to | Verdict |
|---:|---:|---|---|
| $6.00 | **$32.7/hr** | The whole unit's average, **$31.80/hr** (economics §7) | Loading at least matches the rest of your work. Worth continuing |
| $2.00 | **$10.9/hr** | Below any sensible floor | Not worth the minutes |

So the rule reads plainly: **keep loading if it pays at least as well per hour as the refurb work
itself; stop if it pays less than $11/hr.** The inconclusive band between them is exactly the range
this test cannot resolve (§6.3), which is why it resolves to "keep loading, stop planning around it"
rather than to a confident decision.

### 7.3 Are $6 / $2 / 3-units still the right thresholds at n=12? **[COMPUTED]**

**Yes. Nothing here changes.** This section exists because the instruction was to re-examine the
thresholds at the new sample size rather than assume they carry over, and the re-examination is worth
recording — but the honest answer is that the rule stays exactly as pre-registered.

#### Why the two dollar thresholds are not functions of n at all

$6.00 and $2.00 come from **§7.2's marginal labour arithmetic**: 11 minutes per unit, $32.7/hr at $6,
$10.9/hr at $2, against a $31.80/hr blended rate for the refurb work. **Not one term in that
derivation involves the sample size.** They are statements about when loading is worth your time,
and your time is worth the same at 12 pairs as at 10. A threshold derived from opportunity cost
should not move because the measurement got marginally sharper.

The temptation is to move a threshold toward what the test can *detect* — to raise the keep-loading
bar to ~$10.66 so that clearing it would also be statistically significant. **Resist it, for two
reasons.** First, it would convert a business rule into a statistical one and make the decision
depend on σ_d, which you will not know until the test is over — you would be choosing a threshold
after seeing data, which is precisely the failure mode §6.8 and §5.3 exist to prevent. Second, it gets
the burden of proof backwards. The rational default is **keep loading unless the test shows harm**
(the most important sentence in §0), because loading costs 11 minutes. A rule that demands
statistical significance before *continuing* an already-cheap activity would stop a profitable
practice on the basis of a test that §6.3 shows is underpowered by construction.

**So read the primary rule as a screening rule on the point estimate, not as a significance test.**
That is what it always was; n=12 just makes it more obvious. The CI in §6.5 is what tells you how
much to believe the point estimate, and it is reported alongside the verdict either way (§7.4).

#### The sell-through override, which *is* a function of n — and still keeps its threshold

The ≥3-unit override is the one threshold where the sample size genuinely enters, because "3 units"
is a raw count and 3 of 12 is a smaller proportion than 3 of 10. So it was checked properly: how often
would a ≥3-unit gap appear **by chance alone**, when the arms are truly identical?

False-trigger rate under H₀, by enumeration over discordant pairs **[COMPUTED]**:

| Discordance rate | n=10, gap ≥3 | **n=12, gap ≥3** | n=12, gap ≥4 |
|---:|---:|---:|---:|
| 20% | 3.6% | **5.0%** | 1.2% |
| 30% | 7.2% | **9.1%** | 3.1% |
| 40% | 10.4% | **12.6%** | 5.4% |

Moving from 10 to 12 pairs raises the false-trigger rate from roughly 4–10% to roughly 5–13%. That is
a real loosening, and the obvious fix — raise the override to ≥4 units — would push it back down to
1–5%.

**Keep it at 3 anyway.** Three reasons, in order of weight:

1. **The override is deliberately asymmetric and deliberately trigger-happy.** It is not a hypothesis
   test; it is a **stop-loss**. §1.3 and §5.3 both frame it as protection against slow inventory in a
   declining season, where the cost of a false trigger is small (you relist at the bare price and
   sell bare units, which is the fallback business anyway) and the cost of a missed trigger is
   carrying loaded stock into November. **A 5–13% false-trigger rate on a stop-loss is acceptable;
   the same rate on a keep-loading claim would not be.**
2. **Raising it to 4 would make it nearly unreachable at the real yield.** §3.1 expects 9–11 pairs. A
   4-unit gap on 10 pairs is a 40-percentage-point difference in sell-through — by then you do not
   need a rule, you can see it.
3. **It is pre-registered.** Changing a threshold in the direction of "harder to stop" while holding
   an unproven belief that loading pays is exactly the thumb-on-the-scale §6.8's eighth trap warns
   about. If it were changed at all it should be changed to be *stricter*, and it does not need to be.

**One clarification added, since the delivered n is uncertain:** the override is **≥3 units on 12
pairs, or ≥30 percentage points of sell-through if you finish with fewer than 12 pairs.** At 10 pairs
that is the original 3 units; at 9 it is 3 units (33 points). This keeps the rule's strictness roughly
constant instead of letting it drift with the yield.

#### Summary of the re-examination

| Threshold | At n=10 | **At n=12** | Changed? |
|---|---|---|---|
| Keep loading | ≥ +$6.00 | **≥ +$6.00** | **No** — derived from labour cost, not from n |
| Stop loading | ≤ −$2.00 | **≤ −$2.00** | **No** — same reason |
| Inconclusive band | −$2 to +$6 | **−$2 to +$6** | **No** |
| Sell-through override | ≥3 of 10 | **≥3 of 12, or ≥30 pts** | **No** — threshold held; proportional form added for partial yields |
| Safety stop (§5.3) | ≤1/10 vs ≥6/10 | **≤1/12 vs ≥7/12** | **Rescaled only** — same 50-point gap |

### 7.4 What to report alongside the verdict

Non-negotiable, because a verdict without these is not auditable:

1. `Δ̂` and its **95% CI**.
2. The observed **σ_d** — the input every future power calculation needs.
3. **Sell-through, both arms**, at 30 and 45 days.
4. **Median days-to-sale**, both arms, with the censoring stated.
5. **Realised price conditional on sale**, both arms, and how much of the $12 survived Best Offer.
6. The **actual eBay fee rate** backed out of a real payout statement — settles the open
   [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §3 question about the 5% used-goods rate.
7. Every **exclusion**, with the reason and date.
8. **The delivered number of pairs**, and the dud/unpairable count behind it. §3.1 predicts 9–11 from
   24 units; the actual figure is a genuinely useful input to next season's buy.
9. **The hardware gate result** (§3.5) and which `payload_format` shipped.
10. **Stated limitations**, minimum: within-seller interference (§2.6), the post-peak tail (§5.2),
    single platform, single loadout, no pilot shakedown (§5.1), and n=12 power (§6) — including the
    fact from §6.3 that **the minimum detectable effect exceeds the design's maximum attainable
    effect** at the base-case variance.

---

## 8. Data-logging schema

### 8.1 The spreadsheet is the system of record

> ## ✅ Built and committed — use this, not the app
>
> **[`AB_TEST_LOG.csv`](AB_TEST_LOG.csv)** is in this folder, **pre-filled with all 24 rows**, the
> committed arm assignments from §2.4, and every constant that is known in advance. It is a
> **70-column** extension of the schema below.
>
> **[`TRACKING_SHEET_NOTES.md`](TRACKING_SHEET_NOTES.md)** is the companion: which columns to fill at
> which moment, and the exact spreadsheet formulas that compute `Δ̂`, σ_d, the 95% CI, sell-through
> and the §7.1 verdict **by hand, with no app and no R.**
>
> **The app path in §10 is deferred and is not being built.** Do not wait for it.

One row per **unit**, so a pair is two rows sharing a `pair_id`. The columns added beyond the original
schema are marked **NEW 08-13** in the table and exist for one of three reasons: the up-front
randomisation needs an audit trail (§2.4), the hardware gate needs somewhere to record its result
(§3.5), or a derived column needed a helper so the arithmetic is doable in a spreadsheet.

The `App field` column records where each value *would* live in the inventory app. It is now
**reference only** — the app cannot run this experiment and §10 is deferred.

```csv
pair_id,unit_slot,arm,drop,publish_first,arm_assigned_at,arm_seed,arm_seq_sha256,unit_id,app_sku,acquisition_date,acquisition_channel,acquisition_cost,extra_costs,variant,variant_confirmed_by,serial_last4,os_version_before,os_version_after,cosmetic_grade,colour,case_included,cable_included,battery_replaced,screen_notes,defects,loadout_sku,payload_format,program_count,payload_bytes,hw_gate_unit,hw_gate_status,hw_gate_date,bundles_loaded,prep_wiped,prep_os_updated,prep_p2t_cleared,prep_programs_loaded,prep_device_verified,prep_minutes,baseline_price,list_price,listing_platform,listing_format,listing_url,listed_at,photo_count,promoted_rate,views_d7,watchers_d7,views_d21,watchers_d21,offers_received,best_offer_amount,questions_about_programs,price_changes,sold_at,sale_price,platform_fees,shipping_label_cost,net_revenue,days_to_sale,sold,unsold_at_30d,unsold_at_45d,returned_at,return_reason,excluded,exclusion_reason,notes
```

#### The columns added on 2026-08-13, and why

| Column | Values | Why it was added |
|---|---|---|
| `unit_slot` | `A` \| `B` | **The arm is a property of (pair, slot), not of a unit.** §2.4 stage 1 commits the sequence by slot before any unit exists; stage 2 binds units to slots by serial number. Without this column the pre-commitment cannot be expressed |
| `publish_first` | `LOADED` \| `BARE` | Second randomisation from §2.4, previously described but never given a column |
| `arm_seed` | `20260813` | Lets anyone re-derive the sequence |
| `arm_seq_sha256` | 64 hex chars | Fixes the sequence against later editing. Recompute and compare |
| `app_sku` | e.g. `CALC-000017` | Separated from `unit_id` so the sheet has a stable identity of its own. `unit_id` (`X01`–`X24`) is committed **before** the units exist; `app_sku` is filled when a physical unit is bound to the row |
| `payload_format` | `8XV` \| `PY` | §3.5. Which format the gate cleared, and therefore what shipped. **Must be identical on all 12 loaded rows** |
| `hw_gate_unit` | bool | Marks the one unit the gate ran on |
| `hw_gate_status` | `PASS` \| `FAIL_8XV_ONLY` \| `FAIL_BOTH` \| `PASS_AFTER_SUBSTITUTION` | §3.5.4. **Gates the whole verdict** (§7.1) |
| `hw_gate_date` | ISO date | Must predate every `prep_programs_loaded` on the other units |
| `sold` | bool | Redundant with `sold_at` but makes the sell-through and McNemar arithmetic a one-column `COUNTIFS` instead of a date test. §6.6 and §7.3 both need it |

Two deliberate changes to existing columns:

- **`prep_programs_loaded` accepts `NA_BY_DESIGN`** on bare rows, instead of the app's
  tick-it-anyway workaround (§3.2). The spreadsheet has no "ready to list" logic to keep happy, so it
  can record the truth.
- **`pair_id` now runs `P01`–`P12`.** The `PILOT` value is gone — there is no pilot (§5.1). Units
  outside the experiment are `arm = NOT_IN_TEST`.

| Column | Type / values | App field | Notes |
|---|---|---|---|
| `pair_id` | `P01`–`P12` | — NEW — | The blocking variable. Without it there is no paired analysis. **Pre-filled** |
| `unit_id` | `X01`–`X24` | ✗ | The sheet's own permanent row identity, committed before the units existed. **Pre-filled** |
| `arm` | `BARE` \| `LOADED` \| `NOT_IN_TEST` | — NEW — | **The single most important field.** **Pre-filled from §2.4 — never edit it** |
| `arm_assigned_at` | ISO date | — NEW — | `2026-08-13` on all rows. Must predate every `listed_at`. Proves the randomisation wasn't post-hoc |
| `drop` | `1` \| `2` | — NEW — | Blocking factor. **Pre-filled**: `P01`–`P06` → 1, `P07`–`P12` → 2 |
| `variant` | `TI84_PLUS_CE_PYTHON` | `CalculatorUnit.variant` | ✅ exists |
| `variant_confirmed_by` | `FACEPLATE+ABOUT` \| `ABOUT` \| `FACEPLATE` \| `PYTHON_RAN` | — NEW — | Provenance of the variant claim. See `SOURCING_SHORTLIST.md` |
| `serial_last4` | 4 chars | `CalculatorUnit.serialNumber` | ✅ exists. **Also the pair-numbering and A/B tiebreak** (§2.4 stage 2) — record it accurately, the assignment depends on it |
| `os_version_before` / `_after` | e.g. `5.8.4` / `5.8.5` | `CalculatorUnit.osVersion` (after only) | ⚠️ only one field exists; "before" matters for the OS-5.5 exception in SOP §4b |
| `cosmetic_grade` | `A` \| `B` \| `C` \| `D` | ✗ | **Mandatory, and pairs cannot be formed without it.** `Item.condition` is `USED_GOOD`/`USED_FAIR` — **too coarse to match on**. Grade from [`../PREP_SOP.md`](../PREP_SOP.md) §8; `D` never enters the loaded arm. Fill this **before** reading the `arm` column (§2.4) |
| `colour` | free text | ✗ | Matching factor |
| `case_included` / `cable_included` | bool | ✗ | Matching factors. Directly affect price |
| `battery_replaced` | bool | ✗ (`Item.extraCosts` only implies it) | A claim that moves price; must be matched |
| `screen_notes`, `defects` | free text | `Item.notes` | ⚠️ unstructured today |
| `loadout_sku` | `P6` \| `P1` \| `P2` \| `NONE` | ✗ | `CalculatorUnit.bundles[]` is the **digital** bundle enum, not the physical loadout |
| `program_count`, `payload_bytes` | int | ✗ | `10`, `33956` for P6 (§3.4). `0`, `0` for bare |
| `bundles_loaded` | enum list | `CalculatorUnit.bundles[]` | ✅ exists, but see §9.1 — **the enum is stale** |
| `acquisition_date` | ISO date | `Item.purchaseDate` | ✅ |
| `acquisition_channel` | `EBAY_AUCTION` \| `EBAY_BIN` \| `FB_LOCAL` \| `MERCARI` \| `OFFERUP` \| `THRIFT` \| `LOT` | `Item.purchaseSource` | ✅ free text — normalise the values yourself |
| `acquisition_cost` | money | `Item.purchasePrice` | ✅ |
| `extra_costs` | money | `Item.extraCosts` | ✅ battery, case, cable |
| `baseline_price` | money | `CalculatorUnit.baselinePrice` | ✅ **Set to $78 on BOTH arms.** It is your honest bare comp for the grade — not the arm's list price |
| `list_price` | money | `CalculatorUnit.listPrice` | ✅ $78 bare / $90 loaded |
| `listing_platform` | `EBAY` | ✗ at listing time | `Sale.platformId` only exists once sold — **so an unsold unit has no platform**, which breaks sell-through by platform |
| `listing_format` | `FIXED_BO` \| `FIXED` \| `AUCTION` | ✗ | Held constant here, but needed for future tests |
| `listing_url` | URL | ✗ | Your audit trail. Screenshot the listing too |
| `listed_at` | ISO datetime | ✗ | **Mandatory. Days-to-sale, sell-through at 30/45 days, and the day-45 decision date are all uncomputable without it**, and it cannot be reconstructed in October. Log it the hour you publish. The app has no listing timestamp at all |
| `photo_count` | int | `Item.photos[]` length | ✅ derivable. Must match within pair (§2.2) |
| `promoted_rate` | % | ✗ | `0` for this test |
| `views_d7`, `watchers_d7`, `views_d21`, `watchers_d21` | int | ✗ | Manual from Seller Hub. Leading indicators only (§4.3) |
| `offers_received` | int | ✗ | |
| `best_offer_amount` | money | ✗ | The accepted offer, if any |
| `questions_about_programs` | int | ✗ | The one qualitative signal worth counting |
| `price_changes` | int | ✗ | Should be `0`. Non-zero = protocol deviation, log it |
| `sold_at` | ISO date | `Sale.soldDate` | ✅ |
| `sale_price` | money | `Sale.soldPrice` | ✅ |
| `platform_fees` | money | `Sale.platformFees` | ✅ **from the real payout statement** |
| `shipping_label_cost` | money | `Sale.shippingCost` | ✅ |
| `net_revenue` | money | derived | `sale_price − platform_fees − shipping_label_cost`; **0 if unsold** |
| `days_to_sale` | int | ✗ derived | `sold_at − listed_at`. Needs `listed_at` |
| `unsold_at_30d`, `unsold_at_45d` | bool | ✗ derived | Needs `listed_at` |
| `returned_at` | ISO date | `Sale.returnedAt` | ✅ |
| `return_reason` | `P2T_DATA_LOSS` \| `HARDWARE` \| `REMORSE` \| `INAD_OTHER` | ✗ | The three scenarios in `../LISTING_AND_SUPPORT.md` §6. `P2T_DATA_LOSS` is the one that would be caused by the treatment |
| `prep_*` (5 cols) | bool | the 5 `CalculatorUnit` booleans | ✅ — but see §3.2 on the missing N/A state |
| `prep_minutes` | int | ✗ | Validates the SOP §10 38-min estimate. Worth collecting once |
| `excluded`, `exclusion_reason` | bool, text | ✗ | Intent-to-treat audit trail |
| `notes` | free text | `Item.notes` | ✅ |

### 8.2 Analysis, straight from the CSV

**The supported path is the spreadsheet.** [`TRACKING_SHEET_NOTES.md`](TRACKING_SHEET_NOTES.md) §4
gives every formula you need in Excel/Sheets syntax, including the *t*-interval and the verdict
lookup. Use that.

The R below is kept as a cross-check for the same numbers, not as a requirement. If the two disagree,
the spreadsheet is what you filled in and R is what you typed twice — find the difference before you
decide anything.

```r
# R, or the pandas equivalent
d <- read.csv("ab_test_log.csv")
d <- subset(d, arm %in% c("BARE","LOADED") & excluded == FALSE)

w <- reshape(d[, c("pair_id","arm","net_revenue")],
             idvar = "pair_id", timevar = "arm", direction = "wide")
diff <- w$net_revenue.LOADED - w$net_revenue.BARE

mean(diff)          # Delta-hat  -> compare to the section 7.1 table
sd(diff)            # sigma_d    -> report this; every future power calc needs it
t.test(diff)        # 95% CI     -> this is the number to report, not the p-value
wilcox.test(diff)   # rank-based sanity check, robust to one wild pair

# Sell-through, paired
table(w$sold.LOADED, w$sold.BARE)   # discordant cells -> exact binomial
binom.test(sum(w$sold.LOADED & !w$sold.BARE),
           sum(xor(w$sold.LOADED, w$sold.BARE)))
```

**Report `t.test(diff)$conf.int` and `sd(diff)` in the write-up whatever the *p*-value says.**

### 8.3 Collection discipline

- **Weekly, every Sunday**, at the same time: views, watchers, offers, questions. Traffic stats
  ageing out of Seller Hub is the most likely way you lose data.
- **Screenshot both listings on day 1** of each drop. Proof they were identical apart from the
  treatment.
- **Log the day it happens.** Reconstructing dates in October from memory is how a clean test
  becomes a story. `listed_at` is the one field with no recovery path at all.
- **Commit the CSV to git after every session.** It costs one command and it converts the file into a
  dated, tamper-evident record — which is what §2.4 leans on for the randomisation audit trail. A
  spreadsheet sitting unversioned on the desktop has none of that property.

---

## 9. Contradictions with existing docs

**Resolved 2026-08-13.** These were originally flagged rather than edited, per the scope constraint on
this folder. They have since been worked through in the owning documents; the status of each is
recorded below so nobody re-opens a settled question.

### 9.1 The digital bundle lineup — ✅ already current, this entry was wrong

| Source | Says | Status |
|---|---|---|
| `bundles/PRICING.md` | **52 programs**; 7 subject bundles at **$12/$15/$19**; Complete Toolkit **$49**; free starter **5 programs** | ✅ Current |
| `../UNIT_ECONOMICS.md` §6, §10 | **$49** complete digital toolkit; explicitly warns against reading the $35→$49 repricing as licence to charge more | ✅ Current — **this row previously said "$35, stale." It was not.** |
| `../LOADOUT_STRATEGY.md` §7 | **$12–$19** per subject bundle / **$49** complete toolkit; free **5-program** starter | ✅ Current — **same correction** |
| App `ProgramBundle` enum | 6 values: `FREE_STARTER, CALCULUS, ALGEBRA_LINEAR_STATS, PHYSICS_ENGINEERING, CHEMISTRY_EXAM_TOOLS, COMPLETE_TOOLKIT` | ❌ Still missing `BIOLOGY`, `FINANCE`, `STATISTICS_PROBABILITY`; two names drifted. **The only genuine gap here** — spec at §10.2 #14 |

**What happened:** this folder was drafted against a snapshot of `business/` taken before the pass
that reconciled those two documents to the 52-program library. Both had already been updated. The
lesson is worth keeping — **re-read the owning document before recording a contradiction against it**.

**The substantive point still stands and is unchanged.** The arithmetic ceiling on the premium is
$49, not $35, but the binding constraint was never the ceiling — it was observed willingness to pay,
which no evidence supports at any level. **The $12 test differential stands.**

### 9.2 `LOADOUT_STRATEGY.md` P6 — ✅ resolved, P6 changed

Covered in §3.4. The re-derived 10-program / **33,956 B** P6 (`PH` in the chemistry slot instead of
`GASLAW`) has been adopted in `../LOADOUT_STRATEGY.md`, which is now the authority for it. That
document also resolves the underlying ambiguity that produced the disagreement: the ≥16 KB headroom
policy is enforced against **file bytes** (≤34,816 B), not the on-calc figure, wherever the two
readings disagree.

Note the original framing here was overstated — the filenames in that document were *already* current;
only the byte total was at the wrong end of the policy.

### 9.3 `UNIT_ECONOMICS.md` §6 asks for "$10–$15 apart"; this test uses $12

Not a contradiction — $12 is the midpoint of the range that document specifies, and the bare price
of **$78** is taken directly from its §7 table. Recorded here so nobody later reads the $90 loaded
price as inconsistent with the doc's modelled **$88** sale. The $88 is a *modelled realisation* at a
$10 premium; $90 is a *list* price at a $12 differential, and with Best Offer the realised figure
should land between them. Both use the same net formula, `net = 0.7845 × P − 11.05 − acquisition`.

### 9.4 The prep checklist has no "not applicable" state

`../PREP_SOP.md` maps to five booleans, all of which must be true for a unit to be "ready to list."
A bare-arm unit legitimately never has programs loaded. Workaround in §3.2; proper fix in §10.

---

## 10. What the inventory app needs — ⛔ DEFERRED, NOT IMPLEMENTED, NOT SCHEDULED

> # ⛔ NONE OF THIS EXISTS. NONE OF IT IS BEING BUILT.
>
> **Decided by the owner, 2026-08-13: the experiment is tracked in a spreadsheet. This app
> integration is deferred indefinitely and no part of it is scheduled.**
>
> **Everything in §10 — every field, every enum, every view, every report, all 20 numbered items — is
> an unbuilt specification.** Do not read any of it as shipped functionality. Do not plan around it.
> Do not wait for it. If you are looking for where the experiment is actually recorded, it is
> **[`AB_TEST_LOG.csv`](AB_TEST_LOG.csv)**, and the instructions are in
> **[`TRACKING_SHEET_NOTES.md`](TRACKING_SHEET_NOTES.md)**.
>
> **The section is retained deliberately, not by neglect.** It is the most complete statement of what
> the app is missing, and the missing pieces are real: items **#1–#5** are genuine structural gaps
> that make the app unable to represent this experiment at all, and **#4 (`listedAt`)** and
> **#14 (the stale `ProgramBundle` enum)** are bugs that hurt the business outside the experiment too.
> When app work is next funded, start here. Until then this is a wish list.
>
> **Why the spreadsheet was the right call.** At 24 rows the app buys nothing the CSV doesn't have,
> the season is short, and §6 shows the statistics are the binding constraint rather than the
> tooling. Building six schema migrations and five report views to analyse 24 rows would be the most
> expensive way available to not run the test in time. **The one thing the spreadsheet loses is the
> `#19` pair-integrity warning** — an automated check that two paired units really do match on grade,
> case, battery and photo count. That check is now a manual line in §11's per-pair checklist, and it
> is the item most worth being disciplined about, because §6 shows matching quality matters more than
> sample size.

**Schema reference, for whoever picks this up.** Schema at `prisma/schema.prisma`; the per-unit
premium maths already exists in `src/lib/profit.ts` (`softwarePremium = revenue − baselinePrice`) and
is surfaced on `/calculators` and the unit detail page. **The gap is not the arithmetic — it is that
nothing records which arm a unit is in, or when it was listed.**

### 10.1 Blocking — without these, the *app* cannot represent the experiment

**⛔ Not built.** "Blocking" below means blocking for an app-based analysis. It is not blocking for the
test, which runs on the spreadsheet.

| # | Change | Where | Why |
|---|---|---|---|
| 1 | `enum ExperimentArm { BARE LOADED PILOT NOT_IN_TEST }` + `arm ExperimentArm @default(NOT_IN_TEST)` | `CalculatorUnit` | The primary grouping variable. Nothing else in this list matters without it |
| 2 | `pairId String?` + `@@index([orgId, pairId])` (via `Item`) | `CalculatorUnit` | The blocking variable. Paired analysis is impossible without it |
| 3 | `armAssignedAt DateTime?` | `CalculatorUnit` | Must predate prep. Audit trail proving randomisation wasn't post-hoc |
| 4 | `listedAt DateTime?` | `CalculatorUnit` (or `Item`) | **Days-to-sale and sell-through are both uncomputable today.** `Sale.soldDate` exists; there is no listing timestamp anywhere. Set it when `status → LISTED`; keep the first value on relist and add `relistedAt` |
| 5 | `cosmeticGrade` enum `A B C D` | `CalculatorUnit` | `Item.condition` (`USED_GOOD`/`USED_FAIR`) is too coarse to match pairs on or to price against `PREP_SOP.md` §8 |
| 6 | `programsLoadedNa Boolean @default(false)`, **or** convert the 5 prep booleans to `enum PrepState { PENDING DONE NOT_APPLICABLE }` | `CalculatorUnit` | §9.4. The enum is the better fix and also lets a plain-CE unit skip the loaded steps honestly |

### 10.2 High value — ⛔ not built

| # | Change | Where | Why |
|---|---|---|---|
| 7 | `enum PhysicalLoadout { NONE P1_CALCULUS P2_ENGINEERING P3_CHEMISTRY P4_PRECALC_TRIG P5_STATS_ALGEBRA P6_STEM_SAMPLER P7_DIFFEQ BUYERS_CHOICE FULL_LIBRARY }` + `loadout`, `programCount Int?`, `payloadBytes Int?` | `CalculatorUnit` | The physical loadout is a different concept from `bundles[]` (digital SKUs). Conflating them makes "which loadout sells best" permanently unanswerable |
| 8 | `enum ListingFormat { FIXED FIXED_BEST_OFFER AUCTION }` + `listingFormat`, `listingUrl String?`, `promotedRate Decimal?` | `CalculatorUnit` | Format is a first-order price driver and a matching factor |
| 9 | `listingPlatformId String?` → `Platform` | `CalculatorUnit` | `Sale.platformId` only exists after a sale, so **unsold units have no platform** — which makes per-platform sell-through uncomputable. This is the same structural bug as #4 |
| 10 | `caseIncluded`, `cableIncluded`, `batteryReplaced` Booleans; `colour String?` | `CalculatorUnit` | Matching factors, and each independently moves price |
| 11 | `osVersionBefore String?` (keep `osVersion` as "after") | `CalculatorUnit` | The OS-5.5-or-older exception in `PREP_SOP.md` §4b is a genuine one-way door and needs recording before the flash |
| 12 | `viewsD7`, `watchersD7`, `viewsD21`, `watchersD21`, `offersReceived`, `questionsAboutPrograms` Ints | `CalculatorUnit` or a small `ListingMetric` child table | Leading indicators. A child table is cleaner if you want arbitrary weekly snapshots |
| 13 | `enum ReturnReason { P2T_DATA_LOSS HARDWARE_FAULT REMORSE INAD_OTHER }` + `returnReason` | `Sale` | `returnedAt` exists but not the reason. `P2T_DATA_LOSS` is the return the *treatment* causes, so it must be separable |
| 14 | Extend `ProgramBundle` with `BIOLOGY`, `FINANCE`, `STATISTICS_PROBABILITY`; reconcile `ALGEBRA_LINEAR_STATS` → `ALGEBRA_PRECALCULUS_TRIG` and `CHEMISTRY_EXAM_TOOLS` → `CHEMISTRY` | schema enum | §9.1. The app cannot currently represent 3 of the 9 shipping products |

### 10.3 Views and reports — ⛔ not built

The spreadsheet covers #15, #16 and #18 by hand ([`TRACKING_SHEET_NOTES.md`](TRACKING_SHEET_NOTES.md)
§4–§5). **#19 has no spreadsheet equivalent and became a manual checklist line** — see §11.

| # | View | Contents |
|---|---|---|
| 15 | **`/analytics/experiment`** — the A/B report | Per arm: n listed, n sold, sell-through @30/45d, mean & median sale price, **mean net revenue per unit listed (unsold = $0)**, median days-to-sale. Then: `Δ̂`, **95% CI**, observed `σ_d`, paired-*t* and Wilcoxon *p*, and the **§7.1 verdict row the numbers land in, rendered as text.** Showing the verdict is the point — it removes the temptation to re-interpret |
| 16 | **Pair-level table** | One row per `pairId`: both units' grade, list price, sale price, days-to-sale, net, and the within-pair difference. This is what you eyeball for a broken pair |
| 17 | **Days-to-sale on the unit detail page** | `listedAt → soldDate`, with a live "days listed" counter for unsold units. Trivial once #4 exists, and useful outside the experiment |
| 18 | **Realised-premium report** | The existing `softwarePremium` per unit, but **grouped by arm** and against `baselinePrice`. Today `/calculators` sums `softwarePremium` across all units with no arm dimension, so a bare unit sold at $78 against a $78 baseline correctly shows $0 — and averages into the same total as a loaded unit. **The aggregate is currently uninterpretable for the experiment** |
| 19 | **Pair-integrity warning** | Flag any `pairId` whose two units differ in `cosmeticGrade`, `caseIncluded`, `batteryReplaced`, `listingFormat`, `photos.length`, or `listedAt` by >24h. Catches broken matching *before* the listing goes live, which is the only time it can be fixed |
| 20 | **CSV export matching §8.1** | Extend `/api/export/items` with an `?experiment=1` mode emitting exactly the §8.1 header. Lets you run §8.2 without hand-assembling a spreadsheet |

### 10.4 Explicitly out of scope

- Automated eBay ingestion of views/watchers/fees. Manual weekly entry is fine at 24 units, and the
  eBay API integration is far more work than the data is worth.
- Any statistical engine in the app beyond mean, SD, and a *t*-interval. Export to R or pandas.
- Backfilling `listedAt` for units listed before the field exists. Set it going forward.
- **The whole of §10, for the 2026 season.** Added 2026-08-13. Revisit after Oct 21, and only if the
  verdict is KEEP LOADING and there is a second cohort worth instrumenting.

---

## 11. Pre-flight checklist

Anything unticked invalidates the corresponding part of the analysis.

**The blocking gate block runs first, on the first unit to arrive — not before Drop 1.** Everything
below it runs before Drop 1 as it always did. The ordering matters: the gate is the one item that can
still stop the loaded arm, and it is cheapest to fail early.

```
*** BLOCKING GATE - BEFORE ANY SECOND UNIT IS LOADED (section 3.5) ***
[ ] All 10 P6 programs run on the FIRST unit, from the qa/ known-answer table
[ ] Each one: launches, accepts input, correct known answer, exits cleanly
[ ] QUAD sent BOTH ways (.8xv and .py); both run
[ ] TRIG and SIMPSON results photographed on-screen
[ ] hw_gate_status / hw_gate_date / payload_format written to AB_TEST_LOG.csv
[ ] Per-program results appended to HW_VALIDATION.md
[ ] payload_format copied to ALL 12 loaded rows - identical across the arm
--> IF THIS FAILS: do NOT load units 2-12. Go to section 3.5.4.

DESIGN LOCKED (by 2026-08-23)
[x] Randomisation sequence generated and COMMITTED - section 2.4, seed 20260813,
    SHA-256 a6fc5cea...  Already done. Do not regenerate.
[ ] Section 7.1 thresholds read and accepted; nothing amended (see 7.3)
[ ] Bare $78 / loaded $90 confirmed against current sold comps in SOURCING_SHORTLIST.md
[ ] Best Offer auto-accept / auto-decline set IDENTICALLY on both arms
[ ] Promoted Listings OFF on all 24 listings
[ ] Loadout frozen at re-derived P6; 8xv sizes re-measured; total <= 34,816 B
[ ] Buyer's-choice option disabled for the duration
[ ] One pair prepped and drafted end-to-end as the shakedown (there is no pilot -
    see section 5.1). Parcel weighed, listing drafted but NOT published

INTAKE - ALL UNITS, BEFORE READING THE ARM COLUMN (section 2.4 stage 2)
[ ] Grade, colour, case, battery, screen notes, serial recorded for every unit
[ ] Pairs formed on the section 2.1 rules ONLY - arm column not consulted
[ ] Pair IDs assigned in ascending order of each pair's LOWER serial
[ ] Unit A = lower serial within each pair
[ ] Arms then READ OFF the section 2.4 table. Not chosen.

PER PAIR
[ ] Both units confirmed CE PYTHON (faceplate AND About screen photographed)
[ ] Same cosmetic grade, and it is A, B, or C
[ ] Case present on both, or absent on both
[ ] Battery replaced on both, or neither
[ ] Same OS version after flash
[ ] PAIR-INTEGRITY CHECK (replaces the unbuilt app warning, section 10.3 #19):
    grade, case_included, battery_replaced, listing_format, photo_count all
    EQUAL within the pair, and listed_at within 24h. Check BEFORE publishing -
    it is the only moment it can still be fixed
[ ] Same photo COUNT, same shot order, same background
[ ] Descriptions differ ONLY in the allowed blocks (section 2.2)
[ ] Same item specifics, handling time, return policy, shipping option
[ ] Both listings live within the same hour, Sunday 7-9 PM ET
[ ] publish_first order followed as drawn (section 2.4)
[ ] listed_at recorded to the hour for BOTH units - no recovery path if missed
[ ] Both listing URLs logged and screenshotted

WEEKLY (every Sunday)
[ ] Views, watchers, offers, program questions recorded for all live listings
[ ] Any protocol deviation logged the day it happens
[ ] CSV committed to git

AT SALE
[ ] platform_fees taken from the REAL payout statement, not the model
[ ] shipping_label_cost from the actual label
[ ] sold_at, sale_price, best_offer_amount, sold=TRUE recorded
[ ] Return, if any, logged with a reason

DAY 45 (2026-10-21)
[ ] hw_gate_status is PASS or PASS_AFTER_SUBSTITUTION - else THERE IS NO VERDICT
[ ] Unsold units recorded as net_revenue = 0, NOT dropped
[ ] Delta-hat, 95% CI, and observed sigma_d computed
[ ] Sell-through overriding condition (section 7.1) checked FIRST
[ ] Verdict row applied as written
[ ] Delivered pair count and dud/unpairable count recorded (section 7.4 item 8)
[ ] Limitations from section 7.4 item 10 written down
```

---

AP®, Advanced Placement®, SAT®, and CLEP® are trademarks registered by the College Board, which is
not affiliated with, and does not endorse, this product. PSAT/NMSQT® is a registered trademark of
the College Board and the National Merit Scholarship Corporation, which are not affiliated with, and
do not endorse, this product. ACT® is a registered trademark of ACT Education Corp., which is not
affiliated with, and does not endorse, this product. NCEES® is a registered trademark of the
National Council of Examiners for Engineering and Surveying, which is not affiliated with, and does
not endorse, this product. TI-84 Plus CE Python™, TI Connect™ CE, and Texas Instruments® are
trademarks of Texas Instruments Incorporated, which is not affiliated with, and does not endorse,
this product. All trademarks are the property of their respective owners. Nothing in this document
is legal, tax, or statistical advice.
