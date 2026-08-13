# A/B Test Protocol — Is The Software Premium Real?

**Pre-registered design for a 10-matched-pair test of loaded vs. bare TI-84 Plus CE Python units.**

Written 2026-08-12. This document is the pre-registration. **Fill in the decision rule and the
randomisation sequence before you buy the first unit, and do not change them after listings go
live.** Changing a decision rule after seeing data is the single easiest way to fool yourself, and
it is the failure mode this whole document exists to prevent.

**Labelling convention, matching the rest of `business/`:** **[RESEARCHED]** = a figure with a
citable source. **[ESTIMATE]** = my modelling assumption. Statistical results below are computed,
not cited, and are marked **[COMPUTED]** with the inputs shown so you can check them.

**Companion docs:** [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §6 poses this question and
explicitly asks for this test. [`../PREP_SOP.md`](../PREP_SOP.md) governs the prep.
[`LISTING_TEMPLATES.md`](LISTING_TEMPLATES.md) contains the exact copy for both arms.
[`SOURCING_SHORTLIST.md`](SOURCING_SHORTLIST.md) tells you what to pay.

---

## 0. The one-page version

| | |
|---|---|
| **Question** | Does a used CE Python loaded with my Python study programs realise more net revenue than an identical bare one? |
| **Design** | 10 matched pairs. 20 units. Within each pair, one unit is loaded, one is bare, assigned by a coin flip made *before* prep. |
| **Price differential** | Bare listed at **$78**, loaded at **$90**. A **$12** gross differential. |
| **Platform** | eBay, fixed price with Best Offer, 30-day GTC. Both arms identical format. |
| **Primary endpoint** | Realised **net revenue per unit listed** = `sale price − platform fees − shipping label`, counted as **$0 if unsold at day 45**. |
| **Decision statistic** | `mean(loaded) − mean(bare)`, paired within pair. |
| **Decide at** | Day 45 after the last pair is listed. Not before. |
| **Keep loading if** | ≥ **+$6.00**/unit |
| **Stop loading if** | ≤ **+$2.00**/unit |
| **Otherwise** | Inconclusive → run 10 more pairs |
| **Honest power** | At n=10 this test **cannot** distinguish a $0 premium from a $10 one. It *can* detect a ≥$15 premium (~93% power) and it *can* detect the loaded arm actively underperforming. See §6 — read that section before you believe any result. |

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
| *Δ* ≥ **+$6** | **Keep loading. Make it the default SKU.** | Every prepped CE Python gets P6 loaded before listing. Continue to a 20–30 pair cumulative estimate to tighten the number. Consider testing a *higher* differential ($18) on the next 10 pairs. |
| *Δ* between **+$2 and +$6** | **Inconclusive. Keep loading, run 10 more pairs.** | Loading is cheap and the point estimate is positive; continue, but stop treating the premium as a planning input. Price at bare + $8 rather than bare + $12. |
| *Δ* between **−$2 and +$2** | **Inconclusive-null. Keep loading only as a differentiator, not a price lever.** | Load units because it makes the listing distinctive and it costs 11 minutes — but **price them at the bare comp.** Stop building the premium into `baselinePrice`/`listPrice` planning. Redirect effort to acquisition cost, which §8 of the economics doc says dominates anyway. |
| *Δ* ≤ **−$2** | **Stop loading for price. Sell bare.** | The preload is costing you money. Sell bare units at the bare comp, and push the software as the $12–$49 digital product it already is. Put a discount card in the box instead of programs on the device. |
| **Loaded sell-through ≥ 3 units worse** than bare, at any *Δ* | **Stop loading at $12 regardless of the mean.** | Slow inventory in a seasonal business is a real cost the mean doesn't capture. Retest at a $6 differential or not at all. |

### 1.4 What this test does *not* answer

Be clear about the boundaries so you don't over-read it:

- It tests **one differential ($12) on one platform (eBay) in one season (late 2026)**. It does not
  produce a demand curve.
- It does not test the **digital** product. That business is separately established and better
  (§10 of the economics doc: one $49 toolkit download nets more than one shipped calculator).
- It does not test **Mercari or local**, where both the fee structure and the buyer are different.
  [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §3 shows Mercari nets ~$5/unit more; a premium
  might land differently with a browse-driven audience. Note it as future work.
- It does not test **loadout choice** (P1 vs P2 vs P6). Ten pairs cannot resolve two questions.
  **Hold loadout constant at P6** — see §3.4.

---

## 2. Matching — the design decisions that actually determine whether this works

At n=10 your entire ability to learn anything comes from **variance reduction**, not sample size.
§6 shows that halving the within-pair standard deviation is worth more than doubling the number of
pairs. Every rule in this section exists to shrink the noise.

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
  standard deviation. High variance at n=10 means you learn nothing.
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

### 2.4 Randomisation

**Generate the assignment sequence before you buy anything, write it down, and follow it.**

```powershell
# Run once. Paste the output into the log's arm column and never regenerate it.
1..10 | ForEach-Object {
  $flip = Get-Random -Minimum 0 -Maximum 2
  "Pair {0}: unit A = {1}, unit B = {2}" -f $_,
    $(if ($flip) {"LOADED"} else {"BARE"}),
    $(if ($flip) {"BARE"} else {"LOADED"})
}
```

Within each pair, "unit A" is whichever unit has the **lower serial number** — an arbitrary but
objective rule, decided in advance, that you cannot bend.

**Why this matters more than it looks:** if you choose which unit to load after handling both, you
will load the nicer one. Not deliberately — you just will. Pre-committed randomisation on an
objective tiebreak removes the opportunity.

Also randomise, by a second coin flip per pair, **which arm's listing you publish first** within the
drop hour. Record it.

### 2.5 Blocking, and how to allocate pairs across drops

Ten pairs at once from a new seller looks like a dropshipper and invites eBay's duplicate-listing
suppression. Split into **two drops of five pairs, one week apart**, both on Sunday evening.

- Drop is a **blocking factor**. Record it. Analyse with drop as a paired block (it already is one,
  since both arms of a pair are always in the same drop).
- **Do not** change anything between drops — not the template, not the photos, not the price. If you
  must change something, drop 1 becomes a pilot and is excluded, and you run drop 2 and drop 3
  instead. Say so in the log.

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
| Units needed for the test | **20** (10 pairs) |
| Recommended purchase to yield 20 test-grade units | **24** — budget a 10–20% write-off rate on untested buys ([`../SOURCING.md`](../SOURCING.md) §6), plus rejects that fail SOP §2 triage or can't be matched |
| Target acquisition | **≤$32/unit** ([`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §7 max-pay table, $88 target / $25 target profit) |
| Capital at risk, 24 units at $30–$40 | **$720 – $960** |
| Expected gross recovery at 85% sell-through | **~$1,400 – $1,500** |

**The test is not a research expense — it is your inventory.** You were going to buy and sell these
units anyway. The only true cost of running the experiment is the price differential you may be
leaving on the table on the bare arm: 10 units × up to $12 = **≤$120**, and less than that after
fees. Frame it that way when it starts to feel expensive.

### 3.2 Prep

Run [`../PREP_SOP.md`](../PREP_SOP.md) unchanged on **both arms**, including all five checklist
steps, with one difference: on bare-arm units, step 4 (programs loaded) is skipped and recorded as
**deliberately skipped**, not as incomplete.

> **App note:** the current schema models the prep checklist as five booleans with no "N/A" state,
> so a bare unit can never show as fully prepped. Until that's fixed (§10), tick `programsLoaded` on
> bare units and write `ARM=BARE, no programs loaded by design` in `Item.notes`. Ugly, but it keeps
> the "ready to list" logic working. Do **not** leave it unticked, or you will lose track of which
> units are actually ready.

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
test, no P1/P2 substitutions. Ten pairs cannot answer "is loading worth it" *and* "which loadout
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
> load a single unit — and **use the same 10 files on all 10 loaded units.**

---

## 4. Metrics

### 4.1 Primary endpoint

> **Realised net revenue per unit listed**
> `net = sale_price − platform_fees − shipping_label_cost`
> **`net = 0` if the unit has not sold by day 45.** A returned unit is `net = 0` and the return
> costs are logged separately.

**Decision statistic:** `Δ̂ = mean(net_loaded) − mean(net_bare)`, computed on the 10 within-pair
differences.

Three deliberate choices worth defending:

1. **Actual fees, not modelled fees.** Pull `platform_fees` and `shipping_label_cost` from the real
   eBay payout statement per order. The app already stores both on `Sale`. Do not use the 16.55%
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
| **Sell-through at 45 days** | Sold / listed, per arm | The metric with the most decision value at n=10 (§6.4). Slow inventory in a seasonal business is a real cost. | Discordant pairs, exact binomial (McNemar) |
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
| **Buy** | Aug 12 – Aug 24 | Acquire 24 units per [`SOURCING_SHORTLIST.md`](SOURCING_SHORTLIST.md). Log every purchase. |
| **Pilot** | Aug 15 – Aug 22 | 2 pairs, prepped and listed **outside the experiment** (`arm = PILOT`). Shake down prep, photos, listing, packing, shipping. Fix everything that's wrong. |
| **Freeze** | Aug 23 | Template, photos, prices, thresholds and randomisation **locked**. Nothing changes after this date. |
| **Prep** | Aug 23 – Aug 30 | Two batches of ~10 units. SOP §10 timings. |
| **Drop 1** | Sun **Aug 30**, 7–9 PM ET | Pairs 1–5. 10 listings. |
| **Drop 2** | Sun **Sep 6**, 7–9 PM ET | Pairs 6–10. 10 listings. |
| **Observation** | to **Oct 21** | 45 days after drop 2. Collect data weekly. Change nothing. |
| **Interim look** | Oct 6 | Descriptive only. **No decisions.** See §5.3. |
| **Decide** | **Oct 21** | Apply §7. Write it up. |

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
  loaded arm has sold **≤1 of 10** while the bare arm has sold **≥6 of 10**, stop, relist the
  remaining loaded units at the bare price, and record a *Δ* ≤ −$2 outcome. That is a large enough
  gap to be real, and continuing would cost you inventory turns in a declining season.
- **You may not** stop early because the result looks good, extend the test because it doesn't,
  change the price, change the thresholds, or drop a pair.

**Why the rule is strict:** repeatedly testing accumulating data ("optional stopping") drives the
false-positive rate far above 5% — with a few looks it can exceed 20%. With n=10 and a true effect
you can't resolve anyway, optional stopping would essentially guarantee you conclude whatever you
were hoping for. The one asymmetric exception above is deliberate: it only triggers on the outcome
where continuing costs real money, and it requires a gap far larger than noise.

---

## 6. Statistical power at n=10 — the honest treatment

**This is the section to read if you read only one.** It is also the section that will make you want
a bigger test, and you should let it.

### 6.1 The design

Ten matched pairs is a **paired** design, analysed on the 10 within-pair differences
*d*ᵢ = net(loaded)ᵢ − net(bare)ᵢ. Pairing is the right choice: it removes between-unit variation
(condition, colour, accessories, listing week) from the error term, which is why the matching rules
in §2.1 are not optional bureaucracy — they *are* the power of the study.

### 6.2 What n=10 can detect **[COMPUTED]**

For a two-sided paired *t*-test at α = 0.05 with 80% power and n = 10 (df = 9):

```
required standardised effect  d_z = (t₀.₀₂₅,₉ + t₀.₂₀,₉) / √n
                                  = (2.262 + 0.883) / 3.162
                                  = 0.995
```

So the **minimum detectable effect is about 1.0 × the standard deviation of the pair differences.**
Everything then hinges on that standard deviation, σ_d — which you do not know yet, and which this
test will measure as a by-product. Three scenarios:

| σ_d scenario | Plausible if… | **Minimum detectable Δ** |
|---|---|---:|
| **$6** | Tight matching, fixed price, most units sell, little haggling | **≈ $6** |
| **$12** | Realistic base case — some haggling, 1–2 unsold per arm | **≈ $12** |
| **$20** | Loose matching, or 3+ unsold units per arm swinging pairs by $60+ | **≈ $20** |

**[ESTIMATE]** — the σ_d values are my modelling, not measured. There is no published variance
figure for this. Report your observed σ_d in the write-up; it is the most valuable number the test
produces, because it tells you how many pairs a *real* measurement would need.

### 6.3 Power against the effect sizes we actually expect **[COMPUTED]**

At the base-case σ_d = $12, α = 0.05 two-sided, n = 10:

| True Δ | Standardised (d_z) | **Power** | Plain reading |
|---:|---:|---:|---|
| $2 | 0.17 | **~8%** | Invisible |
| **$5** | 0.42 | **~18%** | **A real $5 premium is missed 4 times out of 5** |
| **$10** | 0.83 | **~62%** | Coin flip, slightly favourable |
| $15 | 1.25 | **~93%** | Detectable |
| $20 | 1.67 | **~99%** | Obvious |

**Put that next to the prior.** [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §6 expects
**$5–$12**. Compare with the table: **the entire base-case range sits at or below this test's
detection threshold.** Ten pairs is well-powered against exactly the effect sizes we do *not* expect
and poorly powered against the ones we do.

That is not a reason to skip the test. It is a reason to know in advance what a "not significant"
result means: **absence of evidence, not evidence of absence.**

### 6.4 How many pairs a real measurement would take **[COMPUTED]**

Pairs needed for 80% power, two-sided α = 0.05:

| True Δ | σ_d = $6 | σ_d = $12 | σ_d = $20 |
|---:|---:|---:|---:|
| $5 | ~14 | **~47** | ~128 |
| $10 | ~6 | **~14** | ~34 |
| $15 | ~4 | ~8 | ~16 |

**Read the σ_d = $12 column.** Confirming a $5 premium would take **~47 pairs — 94 units** and most
of a season's capital. That is not a decision you should fund, and knowing so is genuinely
actionable: **stop trying to measure a $5 premium and go work on acquisition cost instead**, which
§8 of the economics doc says moves profit far more anyway.

**Now read across the rows.** Halving σ_d from $12 to $6 cuts the pairs needed for a $10 effect from
14 to 6 — **a bigger gain than doubling the sample.** This is the whole argument for §2's matching
discipline, the auto-accept thresholds, and the identical photo counts. **Variance reduction is the
cheapest statistical power available to you, and it is free.**

### 6.5 The confidence interval is the number to report

Significance testing is the wrong frame for a business decision. Report the interval.

95% CI half-width = `t₀.₀₂₅,₉ × σ_d / √n = 2.262 × σ_d / 3.162 = 0.715 × σ_d` **[COMPUTED]**

| σ_d | Half-width | If you observe Δ̂ = **+$10**, the 95% CI is… | What you can honestly say |
|---:|---:|---|---|
| $6 | ±$4.3 | **[+$5.7, +$14.3]** | "Between $6 and $14. Above my $6 keep-loading threshold across the whole interval. **Act on it.**" |
| $12 | ±$8.6 | **[+$1.4, +$18.6]** | "Somewhere between negligible and excellent. Technically significant, **practically useless.**" |
| $20 | ±$14.3 | **[−$4.3, +$24.3]** | "I learned nothing." |

**Stare at the middle row.** A statistically significant *p* < 0.05 result at n=10 with realistic
variance still leaves you unable to tell $1 from $19. **A significant result is not the same as an
answer**, and this is exactly how a small A/B test fools a careful person: the *p*-value gives
permission to believe a point estimate the data cannot support.

### 6.6 Sell-through is the better-powered endpoint at n=10 **[COMPUTED]**

Because sell-through is binary, the paired analysis (McNemar / exact binomial on discordant pairs)
has clean small-sample properties:

| Discordant pairs | Split needed for two-sided *p* < 0.05 | Exact *p* |
|---:|---|---:|
| 6 | 6–0 | 0.031 |
| 7 | 7–0 | 0.016 |
| 8 | 8–0 or 7–1 | 0.008 / 0.070 |
| 10 | 10–0, 9–1 | 0.002 / 0.021 |

And on the simple "which arm sold more units" sign test over all 10 pairs: **9 of 10 in the same
direction gives *p* = 0.021; 8 of 10 gives *p* = 0.11.**

So sell-through needs **near-total consistency** to be significant — but that is exactly the
signature of the result that matters most. **If pricing $12 higher genuinely breaks sell-through, it
will break it in most pairs, and this test will see it.** That asymmetry is the strongest thing
about the design: it is well-powered against disaster and poorly powered against a small win. Given
that loading costs 11 minutes and the default is to keep doing it, **being well-powered against
disaster is the correct thing to be well-powered against.**

### 6.7 Seven ways to fool yourself, and the countermeasure for each

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

Compute `Δ̂ = mean(net_loaded) − mean(net_bare)` over 10 pairs, unsold = $0, and its 95% CI.

| Condition | Verdict | Action |
|---|---|---|
| `Δ̂ ≥ +$6.00` | **KEEP LOADING** | P6 becomes the default on every prepped CE Python. List at bare + $12. Run pairs 11–20 to tighten the estimate. |
| `+$2.00 ≤ Δ̂ < +$6.00` | **INCONCLUSIVE — LEAN KEEP** | Keep loading. Drop the differential to **+$8**. Run 10 more pairs before treating the premium as a planning input. |
| `−$2.00 < Δ̂ < +$2.00` | **INCONCLUSIVE — NULL** | Keep loading (11 min, listing differentiation) but **price at the bare comp**. Set `baselinePrice = listPrice`. Stop modelling a premium. Redirect effort to acquisition cost. |
| `Δ̂ ≤ −$2.00` | **STOP LOADING FOR PRICE** | Sell bare at the bare comp. Push the digital bundles instead; put the discount card in every box. |

**Overriding condition, applied first:** if **loaded sell-through is ≥3 units below bare**
(e.g. bare 9/10, loaded 6/10), the verdict is **STOP LOADING AT $12** regardless of `Δ̂`. Retest at
a $6 differential or not at all. Rationale: a mean that looks acceptable while inventory sits is
hiding a carrying-cost problem the endpoint doesn't price, and this is a seasonal business where
unsold stock in October is worth less than unsold stock in August.

### 7.2 Why the thresholds are $6 and $2

Both are grounded in the marginal labour, not picked for roundness. Loading adds **~11 min/unit**
([`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §6) = 0.183 h.

| Δ̂ | Marginal $/hr on 11 min | Compare to | Verdict |
|---:|---:|---|---|
| $6.00 | **$32.7/hr** | The whole unit's average, **$31.80/hr** (economics §7) | Loading at least matches the rest of your work. Worth continuing |
| $2.00 | **$10.9/hr** | Below any sensible floor | Not worth the minutes |

So the rule reads plainly: **keep loading if it pays at least as well per hour as the refurb work
itself; stop if it pays less than $11/hr.** The inconclusive band between them is exactly the range
this test cannot resolve (§6.3), which is why it resolves to "run more pairs" rather than to a
decision.

### 7.3 What to report alongside the verdict

Non-negotiable, because a verdict without these is not auditable:

1. `Δ̂` and its **95% CI**.
2. The observed **σ_d** — the input every future power calculation needs.
3. **Sell-through, both arms**, at 30 and 45 days.
4. **Median days-to-sale**, both arms, with the censoring stated.
5. **Realised price conditional on sale**, both arms, and how much of the $12 survived Best Offer.
6. The **actual eBay fee rate** backed out of a real payout statement — settles the open
   [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §3 question about the 5% used-goods rate.
7. Every **exclusion**, with the reason and date.
8. **Stated limitations**, minimum: within-seller interference (§2.6), the post-peak tail (§5.2),
   single platform, single loadout, and n=10 power (§6).

---

## 8. Data-logging schema

### 8.1 CSV columns

One row per **unit** (so a pair is two rows sharing a `pair_id`). Keep it in the repo at
`business/hardware-launch/data/ab_test_log.csv`, or export it from the app once §9's fields exist.

The `App field` column shows where each value lives in the inventory app today.
**`— NEW —`** means the app cannot store it yet; §9 specifies what to add.

```csv
pair_id,unit_id,arm,arm_assigned_at,drop,variant,variant_confirmed_by,serial_last4,os_version_before,os_version_after,cosmetic_grade,colour,case_included,cable_included,battery_replaced,screen_notes,defects,loadout_sku,program_count,payload_bytes,bundles_loaded,acquisition_date,acquisition_channel,acquisition_cost,extra_costs,baseline_price,list_price,listing_platform,listing_format,listing_url,listed_at,photo_count,promoted_rate,views_d7,watchers_d7,views_d21,watchers_d21,offers_received,best_offer_amount,questions_about_programs,price_changes,sold_at,sale_price,platform_fees,shipping_label_cost,net_revenue,days_to_sale,unsold_at_30d,unsold_at_45d,returned_at,return_reason,prep_wiped,prep_os_updated,prep_p2t_cleared,prep_programs_loaded,prep_device_verified,prep_minutes,excluded,exclusion_reason,notes
```

| Column | Type / values | App field | Notes |
|---|---|---|---|
| `pair_id` | `P01`–`P10`, or `PILOT1` | — NEW — | The blocking variable. Without it there is no paired analysis |
| `unit_id` | e.g. `CALC-000017` | `Item.sku` | ✅ exists |
| `arm` | `BARE` \| `LOADED` \| `PILOT` \| `CONTROL_NA` | — NEW — | **The single most important missing field** |
| `arm_assigned_at` | ISO date | — NEW — | Must predate prep. Proves the randomisation wasn't post-hoc |
| `drop` | `1` \| `2` | — NEW — | Blocking factor |
| `variant` | `TI84_PLUS_CE_PYTHON` | `CalculatorUnit.variant` | ✅ exists |
| `variant_confirmed_by` | `FACEPLATE+ABOUT` \| `ABOUT` \| `FACEPLATE` \| `PYTHON_RAN` | — NEW — | Provenance of the variant claim. See `SOURCING_SHORTLIST.md` |
| `serial_last4` | 4 chars | `CalculatorUnit.serialNumber` | ✅ exists. Also the pair A/B tiebreak (§2.4) |
| `os_version_before` / `_after` | e.g. `5.8.4` / `5.8.5` | `CalculatorUnit.osVersion` (after only) | ⚠️ only one field exists; "before" matters for the OS-5.5 exception in SOP §4b |
| `cosmetic_grade` | `A` \| `B` \| `C` \| `D` | ✗ | `Item.condition` is `USED_GOOD`/`USED_FAIR` — **too coarse to match on** |
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
| `listed_at` | ISO datetime | ✗ | **Required for days-to-sale. The app has no listing timestamp at all** |
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
  becomes a story.

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

## 10. What the inventory app needs — specification only

**Not implemented here.** This is the handoff spec for the pass that will implement it. Schema at
`prisma/schema.prisma`; the per-unit premium maths already exists in `src/lib/profit.ts`
(`softwarePremium = revenue − baselinePrice`) and is surfaced on `/calculators` and the unit detail
page. **The gap is not the arithmetic — it is that nothing records which arm a unit is in, or when
it was listed.**

### 10.1 Blocking — without these, there is no experiment

| # | Change | Where | Why |
|---|---|---|---|
| 1 | `enum ExperimentArm { BARE LOADED PILOT NOT_IN_TEST }` + `arm ExperimentArm @default(NOT_IN_TEST)` | `CalculatorUnit` | The primary grouping variable. Nothing else in this list matters without it |
| 2 | `pairId String?` + `@@index([orgId, pairId])` (via `Item`) | `CalculatorUnit` | The blocking variable. Paired analysis is impossible without it |
| 3 | `armAssignedAt DateTime?` | `CalculatorUnit` | Must predate prep. Audit trail proving randomisation wasn't post-hoc |
| 4 | `listedAt DateTime?` | `CalculatorUnit` (or `Item`) | **Days-to-sale and sell-through are both uncomputable today.** `Sale.soldDate` exists; there is no listing timestamp anywhere. Set it when `status → LISTED`; keep the first value on relist and add `relistedAt` |
| 5 | `cosmeticGrade` enum `A B C D` | `CalculatorUnit` | `Item.condition` (`USED_GOOD`/`USED_FAIR`) is too coarse to match pairs on or to price against `PREP_SOP.md` §8 |
| 6 | `programsLoadedNa Boolean @default(false)`, **or** convert the 5 prep booleans to `enum PrepState { PENDING DONE NOT_APPLICABLE }` | `CalculatorUnit` | §9.4. The enum is the better fix and also lets a plain-CE unit skip the loaded steps honestly |

### 10.2 High value

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

### 10.3 Views and reports

| # | View | Contents |
|---|---|---|
| 15 | **`/analytics/experiment`** — the A/B report | Per arm: n listed, n sold, sell-through @30/45d, mean & median sale price, **mean net revenue per unit listed (unsold = $0)**, median days-to-sale. Then: `Δ̂`, **95% CI**, observed `σ_d`, paired-*t* and Wilcoxon *p*, and the **§7.1 verdict row the numbers land in, rendered as text.** Showing the verdict is the point — it removes the temptation to re-interpret |
| 16 | **Pair-level table** | One row per `pairId`: both units' grade, list price, sale price, days-to-sale, net, and the within-pair difference. This is what you eyeball for a broken pair |
| 17 | **Days-to-sale on the unit detail page** | `listedAt → soldDate`, with a live "days listed" counter for unsold units. Trivial once #4 exists, and useful outside the experiment |
| 18 | **Realised-premium report** | The existing `softwarePremium` per unit, but **grouped by arm** and against `baselinePrice`. Today `/calculators` sums `softwarePremium` across all units with no arm dimension, so a bare unit sold at $78 against a $78 baseline correctly shows $0 — and averages into the same total as a loaded unit. **The aggregate is currently uninterpretable for the experiment** |
| 19 | **Pair-integrity warning** | Flag any `pairId` whose two units differ in `cosmeticGrade`, `caseIncluded`, `batteryReplaced`, `listingFormat`, `photos.length`, or `listedAt` by >24h. Catches broken matching *before* the listing goes live, which is the only time it can be fixed |
| 20 | **CSV export matching §8.1** | Extend `/api/export/items` with an `?experiment=1` mode emitting exactly the §8.1 header. Lets you run §8.2 without hand-assembling a spreadsheet |

### 10.4 Explicitly out of scope

- Automated eBay ingestion of views/watchers/fees. Manual weekly entry is fine at 20 units, and the
  eBay API integration is far more work than the data is worth.
- Any statistical engine in the app beyond mean, SD, and a *t*-interval. Export to R or pandas.
- Backfilling `listedAt` for units listed before the field exists. Set it going forward; the pilot
  pairs are outside the experiment anyway.

---

## 11. Pre-flight checklist

Run this **before Drop 1**. Anything unticked invalidates the corresponding part of the analysis.

```
DESIGN LOCKED (by 2026-08-23)
[ ] Randomisation sequence generated, printed, dated, and filed
[ ] Section 7.1 thresholds read and accepted; nothing amended
[ ] Bare $78 / loaded $90 confirmed against current sold comps in SOURCING_SHORTLIST.md
[ ] Best Offer auto-accept / auto-decline set IDENTICALLY on both arms
[ ] Promoted Listings OFF on all 20 listings
[ ] Loadout frozen at re-derived P6; 8xv sizes re-measured; total <= 34,816 B
[ ] Buyer's-choice option disabled for the duration
[ ] Pilot pairs listed, process fixed, and pilot marked arm=PILOT (excluded)

PER PAIR
[ ] Both units confirmed CE PYTHON (faceplate AND About screen photographed)
[ ] Same cosmetic grade, and it is A, B, or C
[ ] Case present on both, or absent on both
[ ] Battery replaced on both, or neither
[ ] Same OS version after flash
[ ] Arm assigned from the pre-generated sequence; unit A = lower serial
[ ] arm_assigned_at logged BEFORE prep started
[ ] Same photo COUNT, same shot order, same background
[ ] Descriptions differ ONLY in the allowed blocks (section 2.2)
[ ] Same item specifics, handling time, return policy, shipping option
[ ] Both listings live within the same hour, Sunday 7-9 PM ET
[ ] Both listing URLs logged and screenshotted

WEEKLY (every Sunday)
[ ] Views, watchers, offers, program questions recorded for all live listings
[ ] Any protocol deviation logged the day it happens

AT SALE
[ ] platform_fees taken from the REAL payout statement, not the model
[ ] shipping_label_cost from the actual label
[ ] sold_at, sale_price, best_offer_amount recorded
[ ] Return, if any, logged with a reason

DAY 45 (2026-10-21)
[ ] Unsold units recorded as net_revenue = 0, NOT dropped
[ ] Delta-hat, 95% CI, and observed sigma_d computed
[ ] Sell-through overriding condition (section 7.1) checked FIRST
[ ] Verdict row applied as written
[ ] Limitations from section 7.3 item 8 written down
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
