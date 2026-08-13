# How To Fill The Tracking Sheet, And Compute The Verdict By Hand

**Companion to [`AB_TEST_LOG.csv`](AB_TEST_LOG.csv). The spreadsheet is the system of record for the
A/B test — there is no app support and none is coming
([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §10 is deferred).**

Written 2026-08-13. **Revised the same day** for the owner's decision to demote the test from a
measurement to a **harm screen** (protocol §0). Every formula here is plain Excel / Google Sheets and
needs no add-ins, no macros and no statistics package. **Nothing in this document decides anything** —
the protocol does that. This is the arithmetic.

---

## 0. Read this first

> ### ⚠️ What this sheet is computing, since it changed on 2026-08-13
>
> **The primary endpoint is the sell-through gap (§4.2), not Δ̂ (§4.1).** The test is a screen for the
> loaded arm doing **harm**; it is not a measurement of the software premium, and at 12 pairs it
> cannot be one — protocol §6.3 has the arithmetic, and it is not close.
>
> Concretely, for this sheet:
>
> 1. **Compute §4.2 before §4.1.** The override is the firing rule; the Δ̂ bands only apply if it
>    doesn't fire. §4.4's lookup already enforces the order — don't work around it.
> 2. **Δ̂ is still computed, still reported, and is never a result.** It goes in the write-up **with
>    its confidence interval, always**, labelled descriptive. §4.5 shows you exactly why.
> 3. **σ_d may be the most valuable number in the file** and it is now the *only* thing here that
>    feeds a future decision (protocol §6.3a).
>
> Nothing was removed from the arithmetic. Four columns were removed from the CSV (§2) and the *order*
> of §4 changed. That's it.

**Three columns carry the whole experiment.** If you get sloppy on anything, do not let it be these:

| Column | Why it is load-bearing | Recovery if you miss it |
|---|---|---|
| **`arm`** | The grouping variable. It is **pre-filled and pre-committed** (§2.4 of the protocol) | **None. Never edit it.** Editing it breaks the SHA-256 and voids the randomisation audit trail |
| **`listed_at`** | Days-to-sale, sell-through at 30 and 45 days, and the day-45 cutoff on the primary endpoint are all computed from it | **None.** eBay does not reliably surface an original list time later. Log it the hour you publish |
| **`cosmetic_grade`** | Pairs cannot be matched without it, and unmatched pairs destroy the variance reduction the whole design depends on (§6.4) | Re-grading after cleaning is not the same grade you listed against. Grade once, at intake |
| **`sold`** | **Promoted 2026-08-13.** It *is* the primary endpoint now. The override in §4.2 is a count over this column | Recoverable from eBay's order history, but keep it current weekly — it is what you'd stop the test on |

**And one rule about order of operations**, from protocol §2.4: fill in grade, colour, case, battery,
screen notes and serial **before you look at the `arm` column.** The protection against bias is not
the random seed — it is that you graded the units blind to their assignment. **Demoting the test does
not relax this by one inch** — a screen you allowed yourself to allocate after seeing the units is not
a screen, it is a preference.

---

## 1. Opening the file without breaking it

`AB_TEST_LOG.csv` is committed as CSV so that `git diff` stays readable and the randomisation audit
trail works. **Excel will mangle it if you let it.**

1. **Do not double-click it.** Open Excel first, then **Data → From Text/CSV**, and set every date
   column to **Text** on import. Otherwise Excel rewrites `2026-08-30` into whatever your locale
   prefers and `git diff` fills with noise.
   - Google Sheets: **File → Import → Insert new sheet**, uncheck *Convert text to numbers and dates*.
2. **Keep dates as ISO text**: `YYYY-MM-DD`, and `YYYY-MM-DD HH:MM` for `listed_at`. The formulas in
   §3 use `DATEVALUE`, which parses ISO strings regardless of locale.
3. **Work in a second sheet.** Do the analysis in §3–§4 on a `PAIRS` tab that *references* the log
   tab. Never add formula columns inside the CSV itself — you will eventually save it and commit
   formulas instead of data.
4. **Save back as CSV** (not `.xlsx`) and **commit after every session.** The commit history is what
   §2.4 of the protocol relies on to prove the arm assignments predate the listings.

> **If Excel is more trouble than it is worth**, Google Sheets handles this file cleanly and every
> formula below works there unchanged.

---

## 2. What to fill, and when

The sheet has **66 columns** because the protocol pre-registered a wide schema. **You are never filling
66 columns at once.** Six passes, in this order.

> ### Four columns were removed on 2026-08-13, and your file may still have them
>
> **`baseline_price`, `promoted_rate`, `views_d21`, `watchers_d21` are gone.** Each existed only to
> support a *measurement* of the premium, which protocol §0 has now abandoned as unachievable at this
> sample size. Full reasoning is in protocol §8.1; the short version:
>
> | Removed | Why |
> |---|---|
> | `baseline_price` | Was `78.00` on all 24 rows and identical to `list_price` on every bare row. It existed to express "the premium over the bare comp." **The bare arm's `list_price` of $78 *is* the bare comp** |
> | `promoted_rate` | Was `0` on all 24 rows. Protocol constant, not data. **Still switch Promoted Listings off** — just don't log it |
> | `views_d21`, `watchers_d21` | The day-21 traffic snapshot. Diagnostic for a premium question that no longer has an answerable form. `views_d7` / `watchers_d7` are kept |
>
> **That is 48 fewer cells to fill by hand across nine Sunday sessions**, and nothing the verdict
> depends on. **If you already made a working copy from the 70-column file, delete those four columns
> from it** — or leave them and ignore them, which is also fine. Nothing below reads them.
>
> **The column letters in §3 and §4 shifted.** They were always approximate: **verify every column
> letter by reading row 1 of your own file** rather than trusting the letters printed here. §3.1 says
> this too, and it mattered even before the columns moved.

### Pass 0 — already done, do not touch

Pre-filled and committed: `pair_id`, `unit_slot`, `arm`, `drop`, `publish_first`, `arm_assigned_at`,
`arm_seed`, `arm_seq_sha256`, `unit_id`, `variant`, `loadout_sku`, `program_count`, `payload_bytes`,
`list_price`, `listing_platform`, `listing_format`, `price_changes`, `excluded`, and
`prep_programs_loaded` on the bare rows (`NA_BY_DESIGN`).

`list_price` is where the arms differ: **$78 bare, $90 loaded.** The $78 is also your honest bare comp
for the grade — which is why the separate `baseline_price` column was removable.

### Pass 1 — as each unit is bought

`acquisition_date`, `acquisition_channel`, `acquisition_cost`, `extra_costs`.

Do this **at the row level even before you know which row the unit will be**, in a scratch list, then
transfer once pairing is done (Pass 3). Buying 24 units in a week and reconstructing what you paid
afterwards does not work.

### Pass 2 — the hardware gate, once. **This is now pass *zero-point-five*: it happens on Aug 13.**

**Revised 2026-08-13.** The gate no longer waits for the first shipment — it runs on a unit **bought
locally, in person, on day 0, before the online orders go out.** So in practice this pass comes
*before* most of Pass 1. See [`README.md`](README.md) for the calendar and
[`SOURCING_SHORTLIST.md`](SOURCING_SHORTLIST.md) §7 for how to buy that unit today.

On the gate unit's row only: `hw_gate_unit = TRUE`, `hw_gate_status`, `hw_gate_date`. Then copy the
resulting **`payload_format` into all 12 loaded rows** — it is a property of the arm, not of one unit.
Full procedure in protocol §3.5; the per-program record goes in
[`HW_VALIDATION.md`](HW_VALIDATION.md), which also carries the **hand-derived expected value for
`TRIG`** (§3.0 there) since `TRIG` is the one program with no `qa/` fixture.

**Until `hw_gate_status = PASS`, only one unit gets programs.** That is the blocking rule. **And until
it passes, don't place the online orders** — that is the whole point of moving the gate to day 0.

### Pass 3 — intake and grading, then binding

**Blind to the `arm` column.** For every unit: `variant_confirmed_by`, `serial_last4`,
`os_version_before`, `os_version_after`, `cosmetic_grade`, `colour`, `case_included`,
`cable_included`, `battery_replaced`, `screen_notes`, `defects`.

*Then* apply protocol §2.4 stage 2 — match into pairs, number pairs by lowest serial, unit A = lower
serial — and write `app_sku` (or whatever your physical identifier is) onto the row it now belongs to.
**The `arm` column is read, never written.**

### Pass 4 — prep and listing

`prep_wiped`, `prep_os_updated`, `prep_p2t_cleared`, `prep_programs_loaded`, `prep_device_verified`,
`prep_minutes`, then at publish: `listing_url`, **`listed_at`**, `photo_count`.

`prep_minutes` is worth the ten seconds — it is the only check on the SOP §10 38-minute estimate,
which [`../PREP_SOP.md`](../PREP_SOP.md) calls the most sensitive input in the whole economic model.

### Pass 5 — weekly, every Sunday

**`sold` and `sold_at`, first and every week.** This is the primary endpoint (protocol §4.1) and the
only column the verdict can fire on. Then `views_d7`, `watchers_d7` **at day 7 only**,
`offers_received`, `questions_about_programs`. The traffic figures age out of eBay Seller Hub, so a
missed week is gone.

**The traffic columns are leading indicators, not endpoints** (protocol §4.4). Watchers in particular
track *low price*, so the bare arm will usually win on them and it means almost nothing. **Their
remaining job is to separate two different nulls:** *nobody wanted it at $90* versus *nobody ever saw
it.* That distinction is worth one snapshot, which is why `views_d21` and `watchers_d21` went.

### Pass 6 — at each sale, and at day 45

At sale: `sold_at`, `sale_price`, `platform_fees`, `shipping_label_cost`, `best_offer_amount`,
`sold = TRUE`, and `returned_at` / `return_reason` if it comes back.

**`platform_fees` comes off the real eBay payout statement**, not the 16.55% model — settling the
actual fee rate is one of the deliverables (protocol §7.4 item 7).

At day 45, compute the derived columns in §3 and leave them in the `PAIRS` tab.

---

## 3. The derived columns

Put these in the `PAIRS` tab or as scratch columns outside the CSV. Assume the log tab is named `LOG`
and data starts on row 2.

### 3.1 `net_revenue` — the recorded statistic, with the day-45 cutoff

**This is the one formula people get wrong.** The quantity is *net revenue per unit **listed***, and
protocol §4.2 counts a unit as **$0 if it has not sold by day 45.** A unit that sells on day 52 is
still **$0** — it did not sell inside the observation window.

> **Renamed 2026-08-13: this used to be called "the primary endpoint."** It is now the **recorded
> statistic** (protocol §4.2). The primary endpoint is the sell-through gap in §4.2 of *this* document.
> The formula is unchanged and it is still mandatory — what changed is that Δ̂ built from it is
> descriptive, never a result.

```excel
= IF( AND( sold_at <> "",
           DATEVALUE(sold_at) - DATEVALUE(LEFT(listed_at,10)) <= 45 ),
      sale_price - platform_fees - shipping_label_cost,
      0 )
```

**Written with column names on purpose.** Four columns were removed on 2026-08-13 (§2) so every letter
after `prep_minutes` shifted, and hard-coded letters here would now be wrong. **Resolve each name
against row 1 of your own file** — that was always the instruction, and it is now load-bearing.

Written in words: *if it sold, and it sold within 45 days of being listed, then sale price minus fees
minus label; otherwise zero.*

A **returned** unit is also `net_revenue = 0` (protocol §4.2), and the return costs are logged
separately, not netted here.

### 3.2 The other derived columns

```excel
days_to_sale    = IF(sold_at="", "", DATEVALUE(sold_at) - DATEVALUE(LEFT(listed_at,10)))
sold_within_45  = IF(AND(sold_at<>"", days_to_sale<=45), 1, 0)
unsold_at_30d   = IF(OR(sold_at="", days_to_sale>30), TRUE, FALSE)
unsold_at_45d   = IF(sold_within_45=1, FALSE, TRUE)
```

`sold_within_45` as a **1/0 rather than TRUE/FALSE** is deliberate: it makes every sell-through count
in §4 a plain `SUM`.

### 3.3 The pair table — 12 rows, and everything else comes from it

The log is one row per unit; the analysis is paired. Build a 12-row bridge:

| | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| **1** | `pair_id` | `net_loaded` | `net_bare` | `diff` | `sold_loaded` | `sold_bare` | `usable` |
| **2** | `P01` | ⬇ | ⬇ | `=B2-C2` | ⬇ | ⬇ | ⬇ |

```excel
B2 = SUMIFS(net_revenue_range, LOG!$A:$A, $A2, LOG!$C:$C, "LOADED")
C2 = SUMIFS(net_revenue_range, LOG!$A:$A, $A2, LOG!$C:$C, "BARE")
D2 = B2 - C2
E2 = SUMIFS(sold_within_45_range, LOG!$A:$A, $A2, LOG!$C:$C, "LOADED")
F2 = SUMIFS(sold_within_45_range, LOG!$A:$A, $A2, LOG!$C:$C, "BARE")
G2 = IF( AND( COUNTIFS(LOG!$A:$A,$A2, listed_at_range,"<>") = 2,
              COUNTIFS(LOG!$A:$A,$A2, excluded_range,"TRUE") = 0 ), 1, 0)
```

Column `A` of `LOG` is `pair_id` and `C` is `arm` — those two did not move, because the four removed
columns all sit further right. **`listed_at` and `excluded` did move**; find them by name in row 1.

**Columns `E` and `F` are the primary endpoint** (protocol §4.1). Everything the verdict can fire on
comes out of those two, so if you build only part of this table, build those.

**`usable` is the intent-to-treat guard.** A pair counts if **both** units were actually listed and
neither is excluded. Protocol §6.8 is explicit: a pair is dropped **only** if a unit was never listed
at all — never because the outcome was inconvenient. Every exclusion needs a dated
`exclusion_reason`.

Fill down to row 13. If you delivered fewer than 12 pairs, the unused rows return `usable = 0` and
drop out of everything below automatically — **no renumbering, no reshuffling** (protocol §2.4).

---

## 4. The verdict, computed by hand

All of this reads off `D2:D13` (the pair differences) and `E2:F13` (the sold flags), filtered to
`usable = 1`.

> ### The order to compute these in, which is not the order they are numbered in
>
> **Revised 2026-08-13.** The section numbers are unchanged so that existing cross-references from the
> protocol still land, but the **order of operations is now the protocol's §7.1 order**:
>
> | Step | Section | What |
> |---|---|---|
> | **0** | §4.4 | **`hw_gate_status`.** Not `PASS` → there is no verdict **and no Δ̂**. Don't compute one |
> | **1** | **§4.2** | **The sell-through gap. The primary endpoint.** If the override fires, that is the verdict and you are done |
> | **2** | §4.1 | Δ̂, σ_d, the CI — **only if step 1 did not fire**, and always reported together |
> | **3** | §4.3 | Exact McNemar **for the record**, not for the decision |
>
> **§4.1 is numbered first because it is the longest arithmetic, not because it comes first.**

```excel
n        = SUMIF($G$2:$G$13, 1)
Delta    = SUMIFS($D$2:$D$13, $G$2:$G$13, 1) / n
sigma_d  = STDEV.S( IF($G$2:$G$13=1, $D$2:$D$13) )      <-- Ctrl+Shift+Enter in Excel
SE       = sigma_d / SQRT(n)
t_crit   = T.INV.2T(0.05, n-1)
CI_low   = Delta - t_crit * SE
CI_high  = Delta + t_crit * SE
p_value  = T.DIST.2T( ABS(Delta/SE), n-1 )
```

`sigma_d` is an array formula: in Excel press **Ctrl+Shift+Enter**, or avoid it entirely by adding a
helper column `H2 = IF(G2=1, D2, "")` and using `=STDEV.S(H2:H13)`. Google Sheets needs no special
handling.

`T.INV.2T(0.05, 11)` returns **2.2010** at n=12 — the same critical value used throughout protocol
§6, which is a free sanity check that your `n` is what you think it is.

> **Report Δ̂ with its CI, always, whatever the *p*-value says.** Protocol §6.5 is blunt about why: at
> this sample size a significant result can still leave you unable to tell $2 from $18. The interval
> is the honest output; the *p*-value is decoration.
>
> **And report `sigma_d` even if you report nothing else.** It is the one number this test produces
> that no amount of reasoning could have given you in advance, and every future power calculation
> depends on it — **including the harm-power table in protocol §6.3a**, whose weakest input is the
> assumed σ_d.
>
> **Added 2026-08-13 — the sentence that must accompany Δ̂ wherever it appears:** *Δ̂ is a descriptive
> statistic, not an estimate of the software premium.* Protocol §4.2 forbids the phrase "measured
> premium" outright, and §7.4 item 11 requires the disclaimer in the write-up verbatim. **The
> spreadsheet is where the number is born, so it is the right place to label it.** Put the sentence in
> a cell next to Δ̂.
>
> `p_value` is computed above **because leaving it out invites someone to compute it badly later.**
> It is not consulted by any rule in §4.4. It is not the decision. Protocol §6.3 explains why a
> *p*-value from this design is close to meaningless in the positive direction.

### 4.2 Sell-through and the override — **the primary endpoint. Compute this FIRST.**

**This is step 1 and it is the whole point of the test** (protocol §4.1). Protocol §7.1 applies the
override **before** the mean, so compute it first — and protocol §6.3a is the reason it is first:
against harm at the −$2 threshold, this count fires about **6× more often** than the *t*-test on Δ̂
does.

```excel
st_loaded   = SUMIFS($E$2:$E$13, $G$2:$G$13, 1)      ' loaded units sold, of n
st_bare     = SUMIFS($F$2:$F$13, $G$2:$G$13, 1)      ' bare units sold, of n
gap_units   = st_bare - st_loaded
gap_points  = gap_units / n

override    = IF( OR(gap_units >= 3, gap_points >= 0.30),
                  "STOP LOADING AT $12", "no override" )
```

**≥3 units on 12 pairs, or ≥30 percentage points if you delivered fewer than 12** (protocol §7.3).
If the override fires, **that is the verdict** and Δ̂ does not matter.

> **What a *non*-firing override does and does not tell you.** It does **not** mean loading is safe.
> Protocol §6.3a: this rule catches roughly **33%** of harm sitting at the −$2 threshold and about
> **50%** of harm around −$9. **A quiet result is weak evidence, and the honest write-up says
> "no harm detected," never "no harm."** It is still the right rule, because the alternative at this
> sample size is a *t*-test that catches 5%.

### 4.3 The paired sell-through test (McNemar, exact) — **for the record, not for the decision**

Only the **discordant** pairs — the ones where exactly one arm sold — carry information:

```excel
D_disc   = SUMPRODUCT( ($G$2:$G$13=1) * ($E$2:$E$13 <> $F$2:$F$13) )
k_loaded = SUMPRODUCT( ($G$2:$G$13=1) * ($E$2:$E$13=1) * ($F$2:$F$13=0) )
k_max    = MAX(k_loaded, D_disc - k_loaded)

p_exact  = MIN(1, 2 * (1 - BINOM.DIST(k_max - 1, D_disc, 0.5, TRUE)) )
```

`p_exact` is the exact two-sided binomial *p* on the discordant pairs. Cross-check it against
protocol §6.6: 10–2 should give **0.039**, 11–1 should give **0.006**, 9–3 should give **0.146**. If
your formula disagrees with that table, the formula is wrong.

**Report `p_exact`. Do not decide on it.** Protocol §6.6 carries a correction added 2026-08-13: with
**fewer than 6 discordant pairs no split can reach *p* ≤ 0.05 at all** (5–0 gives *p* = 0.0625), and
moderate harm produces two or three discordant pairs, not six. So this test is **dead on arrival at
exactly the harm levels worth catching** — 1.4% trigger probability at the −$2 threshold, against
32.6% for the §4.2 count. **The count is the rule; this is the description.**

> ### ⚠️ Do NOT run the sign test on the dollar differences. Removed 2026-08-13.
>
> This section used to end by suggesting you reuse the `BINOM.DIST` line on `diff > 0` versus
> `diff < 0`. **That advice was wrong and it has been withdrawn.** Protocol §6.8 has the full
> derivation; the mechanism is simple enough to state here:
>
> A pair where both units sell scores **+$10.37.** A pair where only the *bare* unit sells scores
> **−$61.49.** A sign test throws the magnitude away and counts those two equally. So under real harm
> — 15 points of lost sell-through, true Δ = −$1.96 — **70% of pairs still show a positive
> difference**, and the sign test reaches *p* ≤ 0.05 **pointing at LOADED about 34% of the time.**
>
> **One pair in five is losing you sixty dollars and the sign test calls it a significant win.** The
> mean is negative, the median is positive, and both are right; they answer different questions. Use
> §4.2's count, which counts the direction that matters. If you want a robustness figure, quote the
> **median difference descriptively** and skip the *p*-value.

### 4.4 The verdict lookup

Check the override first, then the mean:

```excel
= IF( LEFT(hw_gate_status,4) <> "PASS", "NO VERDICT - HARDWARE GATE DID NOT PASS",
  IF( override <> "no override", "STOP LOADING AT $12 (sell-through override)",
  IF( Delta >= 6,  "KEEP LOADING",
  IF( Delta >= 2,  "INCONCLUSIVE - LEAN KEEP",
  IF( Delta > -2,  "INCONCLUSIVE - NULL",
                   "STOP LOADING FOR PRICE" )))))
```

The `hw_gate_status` test is not decoration. Protocol §7.1 makes a passed gate a **prerequisite** for
there being a verdict at all: if the programs never ran on hardware, the experiment did not run, and
a Δ̂ computed from it measures nothing. `PASS` and `PASS_AFTER_SUBSTITUTION` both satisfy it.

### 4.5 Worked example — so you can tell a working sheet from a broken one

Plug these six pairs in and confirm you get the same answers. **These are illustrative numbers, not
predictions.**

| pair | net_loaded | net_bare | diff | sold_L | sold_B |
|---|---:|---:|---:|---:|---:|
| P01 | 71.86 | 61.49 | +10.37 | 1 | 1 |
| P02 | 68.00 | 61.49 | +6.51 | 1 | 1 |
| P03 | 0.00 | 61.49 | −61.49 | 0 | 1 |
| P04 | 71.86 | 0.00 | +71.86 | 1 | 0 |
| P05 | 66.40 | 58.00 | +8.40 | 1 | 1 |
| P06 | 71.86 | 61.49 | +10.37 | 1 | 1 |

```
n        = 6
Delta    = (10.37 + 6.51 - 61.49 + 71.86 + 8.40 + 10.37) / 6  =  +7.67
sigma_d  = 42.24
SE       = 42.24 / SQRT(6)  =  17.24
t_crit   = T.INV.2T(0.05, 5)  =  2.5706
CI       = 7.67 +/- 44.33  =  [-36.66, +52.00]
t        = 7.67 / 17.24  =  0.445
p_value  = T.DIST.2T(0.445, 5)  =  0.675

st_loaded = 5/6 , st_bare = 5/6 , gap = 0  ->  no override
D_disc = 2 , k_loaded = 1  ->  1-1 split , p_exact = 1.00

VERDICT: KEEP LOADING   (Delta = +7.67 >= +6.00)
```

**Now look at what that example is actually telling you, because it is the trap — and after the
2026-08-13 reframing it is the single most important paragraph in this document.**

The verdict says **KEEP LOADING** off a **+$7.67** point estimate. The confidence interval runs from
**−$37 to +$52.**

Read those two facts together and the whole design becomes clear:

- **The interval contains −$2.** It contains the STOP threshold. **The same data that produced a KEEP
  LOADING verdict is entirely consistent with loading being actively harmful.**
- **The interval is wider than the entire range of outcomes the design can produce** (protocol §4.2:
  the ceiling is +$10.37). An interval that overflows its own design space is not a measurement of
  anything.
- **And the verdict is still correct.** KEEP LOADING is the right action — not because +$7.67 proved a
  premium, but because loading costs 11 minutes and **nothing here is evidence of harm.** That is what
  a screening rule does. It converts weak evidence into the correct default action without pretending
  the evidence was strong.

**So: "KEEP LOADING, Δ̂ = +$7.67 [−$36.66, +$52.00], descriptive only" is a complete and honest
result. "We measured a $7.67 software premium" is a fabrication built from the same numbers.** The
difference between those two sentences is the entire purpose of the 2026-08-13 revision, and this
example is where you can see it with your own arithmetic.

**A sheet that prints "KEEP LOADING" and hides the interval is worse than no sheet.**

Note also how much damage unsold units do to the variance: **each one moves its pair's difference by
$60–$72.** Two of them here (P03, P04) pushed σ_d to **$42.24 — three and a half times** the base-case
assumption. That is the mechanism behind the σ_d = $20 column in protocol §6.2, the reason §6.3a
recomputes harm power with σ_d rising as harm rises, and the strongest argument for the matching
discipline in §2.1: **matched pairs sell or fail *together*, which keeps those swings out of the
differences.**

> **One thing the example does not show, and you should notice its absence.** Look at `sold_L` and
> `sold_B`: 5 of 6 each, gap = 0. **The primary endpoint is silent here**, which is why the Δ̂ band
> decided the outcome. That is the normal case. The override exists for the run where it *isn't*
> silent, and on that run it fires first and Δ̂ is not consulted at all.

---

## 5. What to write up on 2026-10-21

Protocol §7.4 lists **twelve** required items — it gained two on 2026-08-13 and was reordered so the
primary endpoint leads. Nine come straight off this sheet:

| # | Item | Where |
|---|---|---|
| **1** | **The paired sell-through gap, and whether the override fired** | **§4.2. This leads the write-up** |
| 2 | Sell-through both arms at 30 and 45 days, with the discordant breakdown and exact McNemar *p* | §4.2 and §4.3, and `unsold_at_30d` |
| 3 | Δ̂ **and** its 95% CI, labelled descriptive | §4.1 — **never one without the other** |
| 4 | Observed σ_d | §4.1 — **the most valuable single number this test produces** |
| 5 | Median days-to-sale both arms, censoring stated | `MEDIAN` over `days_to_sale` per arm |
| 6 | Realised price conditional on sale | `AVERAGEIFS(sale_price, arm, ..., sold, 1)` |
| 7 | Actual eBay fee rate | `SUM(platform_fees) / SUM(sale_price)` over sold units |
| 8 | Every exclusion, with reason and date | `excluded` / `exclusion_reason` |
| 9 | Delivered pair count and the dud/unpairable count behind it | `n` from §4.1, against the 12 rows |

Items **10**, **11** and **12** are not on the sheet:

- **10 — the hardware gate result.** In [`HW_VALIDATION.md`](HW_VALIDATION.md).
- **11 — the "this was a harm screen, not a measurement" sentence.** **New.** Protocol §7.4 gives the
  wording and requires it verbatim. It is the item that stops Δ̂ being requoted next season as a
  measured premium, and it costs you one sentence.
- **12 — stated limitations.** You write it; protocol §7.4 lists the minimum set, which now includes
  the §6.3a finding that **the screen misses roughly half the harm sitting at the −$2 threshold.**

**One last check before you believe the number.** Recompute the SHA-256 over the
`pair_id,unitA_arm,unitB_arm,publish_first,drop` block and confirm it still equals
`a6fc5ceaa00ba1516adc936b09c10e1b7fbcfaa5e0917fa36d2ada1c5b11dc50`. If it doesn't, the arm column was
edited at some point during the test, and the randomisation audit trail is broken — say so in the
write-up rather than quietly reporting the result.

> **The canonical form, so the check is reproducible.** Twelve lines, one per pair in `P01`–`P12`
> order, fields `pair_id,unitA_arm,unitB_arm,publish_first,drop` comma-separated, **no header line, LF
> line endings, no trailing newline.** The first line is `P01,LOADED,BARE,BARE,1`.
>
> **The four columns removed on 2026-08-13 did not move the hash and could not have** — it covers the
> sequence, not the file. Verified after the edit. **[COMPUTED 2026-08-13]** The sequence also
> reproduces from the seed: `random.Random(20260813)` then `shuffle` on `["LOADED"]*6 + ["BARE"]*6`
> gives the committed unit-A column, and twelve following `choice(["LOADED","BARE"])` draws give the
> committed `publish_first` column.

---

TI-84 Plus CE Python™ and Texas Instruments® are trademarks of Texas Instruments Incorporated, which
is not affiliated with, and does not endorse, this product. Nothing in this document is statistical
advice.
