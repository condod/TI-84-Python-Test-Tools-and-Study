# How To Fill The Tracking Sheet, And Compute The Verdict By Hand

**Companion to [`AB_TEST_LOG.csv`](AB_TEST_LOG.csv). The spreadsheet is the system of record for the
A/B test — there is no app support and none is coming
([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §10 is deferred).**

Written 2026-08-13. Every formula here is plain Excel / Google Sheets and needs no add-ins, no macros
and no statistics package. **Nothing in this document decides anything** — the protocol does that.
This is the arithmetic.

---

## 0. Read this first

**Three columns carry the whole experiment.** If you get sloppy on anything, do not let it be these:

| Column | Why it is load-bearing | Recovery if you miss it |
|---|---|---|
| **`arm`** | The grouping variable. It is **pre-filled and pre-committed** (§2.4 of the protocol) | **None. Never edit it.** Editing it breaks the SHA-256 and voids the randomisation audit trail |
| **`listed_at`** | Days-to-sale, sell-through at 30 and 45 days, and the day-45 cutoff on the primary endpoint are all computed from it | **None.** eBay does not reliably surface an original list time later. Log it the hour you publish |
| **`cosmetic_grade`** | Pairs cannot be matched without it, and unmatched pairs destroy the variance reduction the whole design depends on (§6.4) | Re-grading after cleaning is not the same grade you listed against. Grade once, at intake |

**And one rule about order of operations**, from protocol §2.4: fill in grade, colour, case, battery,
screen notes and serial **before you look at the `arm` column.** The protection against bias is not
the random seed — it is that you graded the units blind to their assignment.

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

The sheet has 70 columns because the protocol pre-registered a wide schema. **You are never filling
70 columns at once.** Six passes, in this order.

### Pass 0 — already done, do not touch

Pre-filled and committed: `pair_id`, `unit_slot`, `arm`, `drop`, `publish_first`, `arm_assigned_at`,
`arm_seed`, `arm_seq_sha256`, `unit_id`, `variant`, `loadout_sku`, `program_count`, `payload_bytes`,
`baseline_price`, `list_price`, `listing_platform`, `listing_format`, `promoted_rate`,
`price_changes`, `excluded`, and `prep_programs_loaded` on the bare rows (`NA_BY_DESIGN`).

`baseline_price` is **$78 on both arms deliberately** — it is your honest bare comp for the grade, not
the arm's asking price. `list_price` is where the arms differ: $78 bare, $90 loaded.

### Pass 1 — as each unit is bought

`acquisition_date`, `acquisition_channel`, `acquisition_cost`, `extra_costs`.

Do this **at the row level even before you know which row the unit will be**, in a scratch list, then
transfer once pairing is done (Pass 3). Buying 24 units in twelve days and reconstructing what you
paid afterwards does not work.

### Pass 2 — the hardware gate, once

On the gate unit's row only: `hw_gate_unit = TRUE`, `hw_gate_status`, `hw_gate_date`. Then copy the
resulting **`payload_format` into all 12 loaded rows** — it is a property of the arm, not of one unit.
Full procedure in protocol §3.5; the per-program record goes in
[`HW_VALIDATION.md`](HW_VALIDATION.md).

**Until `hw_gate_status = PASS`, only one unit gets programs.** That is the blocking rule.

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

`views_d7`, `watchers_d7`, `views_d21`, `watchers_d21`, `offers_received`,
`questions_about_programs`. These age out of eBay Seller Hub, so a missed week is gone.

**These are leading indicators, not endpoints** (protocol §4.3). Watchers in particular track *low
price*, so the bare arm will usually win on them and it means almost nothing.

### Pass 6 — at each sale, and at day 45

At sale: `sold_at`, `sale_price`, `platform_fees`, `shipping_label_cost`, `best_offer_amount`,
`sold = TRUE`, and `returned_at` / `return_reason` if it comes back.

**`platform_fees` comes off the real eBay payout statement**, not the 16.55% model — settling the
actual fee rate is one of the deliverables (protocol §7.4 item 6).

At day 45, compute the derived columns in §3 and leave them in the `PAIRS` tab.

---

## 3. The derived columns

Put these in the `PAIRS` tab or as scratch columns outside the CSV. Assume the log tab is named `LOG`
and data starts on row 2.

### 3.1 `net_revenue` — the primary endpoint, with the day-45 cutoff

**This is the one formula people get wrong.** The endpoint is *net revenue per unit **listed***, and
protocol §4.1 counts a unit as **$0 if it has not sold by day 45.** A unit that sells on day 52 is
still **$0** for the primary endpoint — it did not sell inside the observation window.

```excel
= IF( AND( LOG!BC2 <> "",
           DATEVALUE(LOG!BC2) - DATEVALUE(LEFT(LOG!AT2,10)) <= 45 ),
      LOG!BD2 - LOG!BE2 - LOG!BF2,
      0 )
```

where `BC` = `sold_at`, `AT` = `listed_at`, `BD` = `sale_price`, `BE` = `platform_fees`,
`BF` = `shipping_label_cost`. **Check the column letters against your own file** — verify by name in
row 1 rather than trusting these.

Written in words: *if it sold, and it sold within 45 days of being listed, then sale price minus fees
minus label; otherwise zero.*

A **returned** unit is also `net_revenue = 0` (§4.1), and the return costs are logged separately, not
netted here.

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
G2 = IF( AND( COUNTIFS(LOG!$A:$A,$A2, LOG!$AT:$AT,"<>") = 2,
              COUNTIFS(LOG!$A:$A,$A2, LOG!$BM:$BM,"TRUE") = 0 ), 1, 0)
```

Column `A` of `LOG` is `pair_id`, `C` is `arm`, `AT` is `listed_at`, `BM` is `excluded`.

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

### 4.1 Δ̂, σ_d, and the confidence interval

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
> depends on it.

### 4.2 Sell-through and the override — check this FIRST

Protocol §7.1 applies the override **before** the mean, so compute it first.

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

### 4.3 The paired sell-through test (McNemar, exact)

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

The same construction gives the **sign test** on the continuous endpoint — count pairs with
`diff > 0` against pairs with `diff < 0`, ignore exact ties, and run the identical `BINOM.DIST` line.

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

**Now look at what that example is actually telling you, because it is the trap.** The verdict says
KEEP LOADING off a +$7.67 point estimate — and the confidence interval runs from **−$37 to +$52**.
Two unsold units (P03 and P04) swung σ_d to $42.24, three and a half times the base-case assumption,
and the interval is now wider than the entire range of outcomes the design can produce.

**This is exactly the failure mode protocol §6.5 warns about, and it is why the CI is mandatory in the
write-up.** The verdict table is a screening rule on the point estimate (§7.3); it is not a claim that
the effect has been measured. A sheet that prints "KEEP LOADING" and hides the interval is worse than
no sheet.

Note also how much damage unsold units do to the variance: **each one moves its pair's difference by
$60–$72.** That is the mechanism behind the σ_d = $20 column in §6.2, and it is the strongest argument
for the matching discipline in §2.1 — matched pairs sell or fail *together*, which keeps those swings
out of the differences.

---

## 5. What to write up on 2026-10-21

Protocol §7.4 lists ten required items. Eight come straight off this sheet:

| # | Item | Where |
|---|---|---|
| 1 | Δ̂ and its 95% CI | §4.1 |
| 2 | Observed σ_d | §4.1 — **the most valuable single number this test produces** |
| 3 | Sell-through both arms, 30 and 45 days | §4.2, and `unsold_at_30d` |
| 4 | Median days-to-sale both arms, censoring stated | `MEDIAN` over `days_to_sale` per arm |
| 5 | Realised price conditional on sale | `AVERAGEIFS(sale_price, arm, ..., sold, 1)` |
| 6 | Actual eBay fee rate | `SUM(platform_fees) / SUM(sale_price)` over sold units |
| 7 | Every exclusion, with reason and date | `excluded` / `exclusion_reason` |
| 8 | Delivered pair count and the dud/unpairable count behind it | `n` from §4.1, against the 12 rows |

Items **9** (the hardware gate result) and **10** (stated limitations) are not on the sheet. Item 9 is
in [`HW_VALIDATION.md`](HW_VALIDATION.md); item 10 you write, and protocol §7.4 lists the minimum set.

**One last check before you believe the number.** Recompute the SHA-256 over the
`pair_id,unitA_arm,unitB_arm,publish_first,drop` block and confirm it still equals
`a6fc5ceaa00ba1516adc936b09c10e1b7fbcfaa5e0917fa36d2ada1c5b11dc50`. If it doesn't, the arm column was
edited at some point during the test, and the randomisation audit trail is broken — say so in the
write-up rather than quietly reporting the result.

---

TI-84 Plus CE Python™ and Texas Instruments® are trademarks of Texas Instruments Incorporated, which
is not affiliated with, and does not endorse, this product. Nothing in this document is statistical
advice.
