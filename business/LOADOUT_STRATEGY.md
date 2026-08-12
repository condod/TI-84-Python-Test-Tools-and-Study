# Loadout Strategy — What Actually Goes On A Physical Unit

The library is **52 programs, 249,322 bytes (243.5 KB)** of `.8xv` AppVars. The calculator's Python
environment holds **50 KB**. The whole library misses the ceiling by roughly **5×**, and no amount of
format tinkering changes that. Deciding what goes on a unit is therefore a product decision, not a
packing decision.

This document defines the physical SKUs, their measured footprints, and how many of them you should
actually stock.

> **Basis: measured 2026-08-12**, from `8xv/` at 52 AppVars / 249,322 bytes. This is a **re-measurement**
> — the earlier version of this document was written against 29 AppVars totalling 106,409 bytes, before
> the converter was re-run across the full library and the on-calculator names were shortened
> (`QUADSOLV` → `QUAD`, `DESCSTAT` → `STATS`, `OBLIQUE` → `TRIG`, and others). **Every footprint below
> was recomputed against the current files; the old figures are not comparable.** The repo is still
> growing, so re-measure before each production batch (commands in §2).

---

## 1. The hard constraint, quoted

TI, *Python Programming for the TI-84 Plus CE* (v5.7 guide) and the Python App Messages eGuide page
(<https://education.ti.com/html/webhelp/EG_TI84PlusCEPY/EN/content/eg_pythonappprog/m_pymessages/m_pymessages.HTML>,
accessed 2026-08-12):

> "The available memory for the Python experience will be a maximum of **100 Python programs
> (PY AppVars) or 50K of memory.** The modules that are bundled with the app in this Python release
> will share the same space with all files."

Two things follow that most people get wrong:

1. **The program-count limit is not the binding one.** 100 programs is far more than 52. Bytes are
   the constraint, every time.
2. **TI's bundled modules eat into the same 50 KB.** So the usable figure for *your* payload is
   less than 50 KB, by an amount TI doesn't publish. This is why the loadouts below target ≤ 34 KB
   rather than creeping up toward 48 KB.

**[VERIFIED]** TI also documents that Python AppVars can be moved to **Archive** for memory
management, and that *"If a PY AppVar Python program is placed in Archive memory, it will not be
available to Run or Edit in the Python App"* until it's moved back to RAM. **[INFERRED]** Since TI
offers archiving specifically as the remedy for running out of Python memory, archived AppVars
presumably don't count against the 50 KB working budget — but TI's wording ("share the same space
with all files") is ambiguous, and this has **not** been tested on hardware. See §6 for how to use
this carefully rather than betting the product on it.

### Sizing method and headroom policy

The numbers below are `.8xv` **file sizes on disk**. On-calculator footprint is slightly smaller —
each `.8xv` carries a 55-byte TI file header plus a small var-entry and a 2-byte checksum, roughly
74 bytes of wrapper per file that doesn't land on the device. Both figures are given; the
difference is under 1 KB per loadout and doesn't change any decision.

**Headroom policy: every physical loadout must leave at least 16 KB free.** Roughly a third of the
Python space stays empty for the student's own programs and class work. A calculator you can't add
your own homework program to is a worse calculator, and "no memory left" is a support ticket and a
one-star review. This policy is why no SKU below exceeds ~67% utilisation.

### The Evo's memory picture is different, and cannot be sized yet

**Everything in this document is a CE Python constraint.** The 50 KB / 100-program ceiling is a limit
TI documents specifically for the **CE** Python App, and it exists partly because that Python
environment ran on a separate 48 MHz ARM coprocessor bolted to an eZ80. The Evo has no coprocessor —
Python runs natively on a 156 MHz ARM CPU — so there is no reason to assume the same number applies.

What [`EVO_TRANSITION.md`](EVO_TRANSITION.md) actually establishes, and nothing beyond it:

- **[RESEARCHED]** Total device memory is **3.5 MB on the Evo vs 3 MB on the CE** (TI product sheet,
  corroborated by Eddie Shore and ti84evo.com). This is the *device* figure, not a Python-environment
  figure.
- **[RESEARCHED, expert]** Available Python memory improved. Adriweb, TI-Planet administrator, asked
  directly what changed on the Evo: *"Performance et mémoire disponible"* — performance and available
  memory.
- **[NOT ESTABLISHED]** **No source gives an Evo equivalent of the 50 KB / 100-program Python ceiling.**
  TI-Planet's Python review episode was still unpublished as of June 2026. **Do not size an Evo loadout
  against any number until it is read off hardware.** "More than the CE" is all that is currently
  supportable, and "more" is not a budget.

One thing that *is* settled and does affect packaging: **an Evo loadout ships as `.py` files, not
`.8xv`.** Python AppVars on the Evo are `.8xv2` and the CE `.8xv` files are rejected outright, but
TI Connect Evo auto-converts `.py` on send. So the loadout *definitions* below carry over unchanged to
an Evo edition; only the payload format and the byte budget would need revisiting.

**Add reading the real ceiling to the Evo test checklist.** The existing checklist
([`EVO_TRANSITION.md`](EVO_TRANSITION.md), "Strategy" §4) covers sending all 52 `.py` files at once,
which would answer the capacity question indirectly — but it does not ask for the documented limit.
Get it explicitly, on hardware, before sizing a single Evo loadout.

---

## 2. Per-program footprint — all 52 AppVars

| Program | Bytes | KB | Subject |
|---|---:|---:|---|
| `QUAD` | 2,033 | 2.0 | Algebra |
| `RLC` | 2,389 | 2.3 | Physics/Eng |
| `DERIV` | 2,441 | 2.4 | Calculus |
| `LINSOLV` | 2,638 | 2.6 | Algebra |
| `SIMPSON` | 2,645 | 2.6 | Calculus |
| `LIMIT` | 2,854 | 2.8 | Calculus |
| `HEAT` | 3,159 | 3.1 | Physics/Eng |
| `KINETIC` | 3,320 | 3.2 | Chemistry |
| `VECT3D` | 3,359 | 3.3 | Physics/Eng |
| `OHMS` | 3,375 | 3.3 | Physics/Eng |
| `ORBIT` | 3,396 | 3.3 | Astronomy |
| `COMBIN` | 3,521 | 3.4 | Algebra/Stats |
| `SUVAT` | 3,523 | 3.4 | Physics/Eng |
| `STATIC` | 3,593 | 3.5 | Physics/Eng |
| `NEWTON` | 3,643 | 3.6 | Calculus |
| `PH` | 3,659 | 3.6 | Chemistry |
| `PROJ` | 3,826 | 3.7 | Physics/Eng |
| `STATS` | 3,859 | 3.8 | Stats |
| `GEOM` | 3,945 | 3.9 | Geometry |
| `MATRIX` | 3,984 | 3.9 | Linear algebra |
| `CMPLX` | 4,033 | 3.9 | Algebra |
| `TAYLOR` | 4,071 | 4.0 | Calculus |
| `DISCRT` | 4,100 | 4.0 | CS |
| `ODE` | 4,116 | 4.0 | Diff Eq |
| `FLUID` | 4,196 | 4.1 | Physics/Eng |
| `MOLAR` | 4,270 | 4.2 | Chemistry |
| `CARDS` | 4,330 | 4.2 | Study tools |
| `UNITS` | 4,422 | 4.3 | Cross-subject |
| `GASLAW` | 4,783 | 4.7 | Chemistry |
| `VERTEX` | 4,974 | 4.9 | Algebra |
| `DRILL` | 5,061 | 4.9 | Study tools |
| `INTEREST` | 5,126 | 5.0 | Finance |
| `SAVOL` | 5,339 | 5.2 | Biology |
| `TRIG` | 5,361 | 5.2 | Trig |
| `PUNNET` | 5,391 | 5.3 | Biology |
| `BREAKEVN` | 5,466 | 5.3 | Finance |
| `HARDYW` | 5,658 | 5.5 | Biology |
| `POPGROW` | 5,661 | 5.5 | Biology |
| `LOAN` | 5,668 | 5.5 | Finance |
| `NPVIRR` | 5,697 | 5.6 | Finance |
| `CHISQ` | 5,947 | 5.8 | Biology |
| `LOGEXP` | 6,164 | 6.0 | Precalculus |
| `CONFINT` | 6,515 | 6.4 | Stats |
| `GASPROC` | 6,674 | 6.5 | Thermo/materials |
| `TVM` | 6,776 | 6.6 | Finance |
| `CARNOT` | 6,827 | 6.7 | Thermo/materials |
| `DILUTION` | 6,845 | 6.7 | Biology |
| `EXPAND` | 7,086 | 6.9 | Thermo/materials |
| `STRESS` | 7,536 | 7.4 | Thermo/materials |
| `SEQSER` | 7,656 | 7.5 | Precalculus |
| `UNITCIRC` | 8,604 | 8.4 | Trig |
| `POLYFUNC` | 9,807 | 9.6 | Precalculus |
| **All 52** | **249,322** | **243.5** | — |

Median program: **4.2 KB.** Practical rule of thumb: **a physical loadout is 8–10 programs.** Twelve is
already crowding the headroom policy; fifteen breaks it.

**The size distribution is much wider than it used to be, and that changes how you substitute.** The
smallest program is 2.0 KB and the largest, `POLYFUNC`, is **9.6 KB — nearly five times** the smallest
and more than double the median. The 23 programs added most recently skew large: they average
**5.9 KB** against **3.7 KB** for the original 29. **A swap is therefore not size-neutral.** Trading
`QUAD` (2.0 KB) for `POLYFUNC` (9.6 KB) costs 7.6 KB of headroom and will break the policy on any
loadout already near the ceiling. Re-check the arithmetic on every substitution.

> **Measurement basis, and drift.** These sizes were measured on **2026-08-12** from `8xv/` (52 AppVars,
> 249,322 bytes). The library is still growing, so **re-run the measurement before each production
> batch:**
>
> ```powershell
> # AppVar footprints, smallest first
> Get-ChildItem -Recurse -File -Filter *.8xv |
>   Sort-Object Length |
>   ForEach-Object { "$($_.BaseName) $($_.Length)" }
>
> # Count and total
> $x = Get-ChildItem -Recurse -File -Filter *.8xv
> $x.Count; ($x | Measure-Object Length -Sum).Sum
> ```
>
> **Also re-check the names.** The on-calculator AppVar names were shortened in the 2026-08-12
> regeneration, and a loadout list that still says `QUADSOLV` or `DESCSTAT` will not match what is in
> `8xv/`. New programs are candidates for the loadouts below, but every substitution must keep the
> loadout under the headroom policy. Adding without removing is how you end up shipping a full
> calculator.

---

## 3. The physical SKU loadouts

All seven are defined and measured. §5 says which ones to actually stock.

### P1 — Calculus Unit · 9 programs · 28,606 B / 27.9 KB · ~27.3 KB on-calc · **22.7 KB free (54.6% used)**

`DERIV` · `SIMPSON` · `NEWTON` · `LIMIT` · `TAYLOR` · `QUAD` · `LINSOLV` · `STATS` · `UNITS`

The five calculus tools plus the three cross-subject staples a calculus student still needs
(quadratics, linear systems, one-variable stats) and the unit converter. The lightest loadout and
the one with the most room left over — appropriate, because this buyer is the most likely to write
their own programs.

Fits: AP® Calculus AB/BC coursework, Calculus I/II, first numerical-methods exposure.

### P2 — Engineering Unit · 9 programs · 31,630 B / 30.9 KB · ~30.2 KB on-calc · **19.8 KB free (60.5% used)**

`SUVAT` · `PROJ` · `OHMS` · `RLC` · `STATIC` · `VECT3D` · `HEAT` · `MATRIX` · `UNITS`

The core physics/engineering set plus matrices and unit conversion, which are the two things an
engineering student reaches for across every course. `FLUID` and the four thermo/materials programs are
swap-ins rather than defaults — see "Not in any default SKU" below.

Fits: Physics I/II, Statics, Circuits, intro Thermodynamics.

> **Naming warning.** Call this the "Engineering Unit," never anything containing "FE," "PE,"
> "NCEES," or "licensure." The TI-84 is banned outright on NCEES exams. See
> [`LISTING_AND_SUPPORT.md`](LISTING_AND_SUPPORT.md) §3.

### P3 — Chemistry Unit · 8 programs · 33,543 B / 32.8 KB · ~32.2 KB on-calc · **17.8 KB free (64.4% used)**

`GASLAW` · `MOLAR` · `PH` · `UNITS` · `HEAT` · `STATS` · `CARDS` · `DRILL`

The core chemistry tools, plus `HEAT` (calorimetry is chemistry as much as physics), stats for
lab data, and the two study-drill tools. **`KINETIC` (reaction kinetics, 3.2 KB) is a natural addition
and does not fit** — adding it would leave only 14.7 KB free and break the headroom policy. Offer it as
a swap for `CARDS` or `DRILL` if a buyer asks.

Fits: General/Intro Chemistry, AP® Chemistry coursework.

### P4 — Precalculus & Trigonometry Unit · 9 programs · 34,825 B / 34.0 KB · ~33.4 KB on-calc · **16.6 KB free (66.7% used)**

`TRIG` · `QUAD` · `VERTEX` · `CMPLX` · `LINSOLV` · `MATRIX` · `COMBIN` · `STATS` · `UNITS`

Fits: Precalculus, Trigonometry, College Algebra, AP® Precalculus coursework.

**This SKU is now at the headroom ceiling — do not add to it.** That is a change from the previous
measurement, and it is awkward, because the three genuinely precalculus-specific programs
(`POLYFUNC` 9.6 KB, `SEQSER` 7.5 KB, `LOGEXP` 6.0 KB) and `UNITCIRC` (8.4 KB) are all new, all large,
and none of them fit here without dropping two of the nine. **If precalculus buyers materialise, this
loadout should be rebuilt around the dedicated programs rather than extended** — a `POLYFUNC` +
`SEQSER` + `LOGEXP` + `UNITCIRC` + `TRIG` core is **36.3 KB on-calc on its own, leaving only 13.7 KB
free at five programs**, so it needs its own design pass against the headroom policy rather than a
substitution.

### P5 — Statistics & Algebra Unit · 8 programs · 29,848 B / 29.1 KB · ~28.6 KB on-calc · **21.4 KB free (57.1% used)**

`STATS` · `COMBIN` · `QUAD` · `LINSOLV` · `MATRIX` · `UNITS` · `CARDS` · `DRILL`

Fits: Intro Statistics, AP® Statistics coursework, College Algebra.

**`CONFINT` (confidence intervals and hypothesis tests, 6.4 KB) is the most obvious upgrade here** and
it fits: swapping it in for `CARDS` lands at 30.7 KB on-calc / **19.3 KB free**. For a genuine statistics
buyer that is a better loadout than the one above, and it is the single best-value substitution
available across all seven SKUs.

### P6 — STEM Sampler (general-purpose) · 10 programs · 35,080 B / 34.3 KB · ~33.5 KB on-calc · **16.5 KB free (67.1% used)**

`QUAD` · `LINSOLV` · `STATS` · `UNITS` · `DERIV` · `SIMPSON` · `SUVAT` · `OHMS` · `GASLAW` · `TRIG`

One program from each of the core STEM subject areas — algebra, stats, calculus, physics, chemistry,
trig, plus the unit converter. This is the SKU for a buyer who doesn't know what they need: a parent
buying for a kid, or a student taking four different STEM classes. It is at the headroom ceiling; do
not add to it.

### P7 — Differential Equations & Numerical Methods Unit · 9 programs · 30,425 B / 29.7 KB · ~29.1 KB on-calc · **20.9 KB free (58.1% used)**

`ODE` · `NEWTON` · `DERIV` · `SIMPSON` · `LIMIT` · `TAYLOR` · `MATRIX` · `LINSOLV` · `CMPLX`

Fits: Differential Equations, Calculus III, numerical methods. Narrow audience — build to order.

### Not in any default SKU — 25 of the 52 programs

The seven SKUs above use only **27 distinct programs** between them. The other **25** are real,
shipping, measured AppVars that no default loadout carries. Four clusters account for 19 of them:

| Cluster | Programs | Why it's not a default SKU |
|---|---|---|
| **Finance** (5) | `TVM` 6.6 · `LOAN` 5.5 · `NPVIRR` 5.6 · `INTEREST` 5.0 · `BREAKEVN` 5.3 | A coherent subject area with **no SKU at all**, and the largest single gap in the lineup. But it is also the area least likely to be why someone buys a *graphing* calculator — a business-maths student is a TI-BA II Plus buyer. **Build-to-order at best**; worth a listing test before it gets a stocked SKU. |
| **Thermo / materials** (4) | `STRESS` 7.4 · `EXPAND` 6.9 · `CARNOT` 6.7 · `GASPROC` 6.5 | Genuinely useful to the P2 Engineering buyer, but these are the **four largest engineering programs** — all four plus a core is over budget. Offer as swap-ins on P2. |
| **Biology** (6) | `DILUTION` 6.7 · `CHISQ` 5.8 · `POPGROW` 5.5 · `HARDYW` 5.5 · `SAVOL` 5.2 · `PUNNET` 5.3 | **The 2027 College Board restriction now bears on six programs, not one.** From 2027 AP® Biology and AP® Environmental Science will not allow calculators with storage capabilities, which kills the exam-season angle for the whole cluster. Better suited to the digital bundles, where storage rules are the buyer's problem rather than a returns liability. |
| **Large precalculus / trig** (4) | `POLYFUNC` 9.6 · `UNITCIRC` 8.4 · `SEQSER` 7.5 · `LOGEXP` 6.0 | The four biggest programs in the library. See the note under P4 — these need a purpose-built loadout, not a substitution. |

The remaining six are worth naming individually, because four of them are the best swap-ins in the
library:

- **`CONFINT`** (6.4 KB) — belongs in P5 for any real statistics buyer. See the note under P5.
- **`KINETIC`** (3.2 KB), **`GEOM`** (3.9 KB), **`FLUID`** (4.1 KB) — **the three best-value swap-ins
  available:** small, broadly useful, and cheap on headroom. Reach for these first when a buyer wants
  something added.
- **`DISCRT`** (4.0 KB) — discrete-math students rarely buy a TI-84 for the course.
- **`ORBIT`** (3.3 KB) — astronomy is not a course with a calculator requirement.

Keep all 25 as **free swap-ins** on the buyer's-choice option (§4). They cost nothing to offer and they
make the "you pick" option feel genuinely custom.

**The structural point worth noticing:** the library grew 79% (29 → 52 programs) while the calculator's
50 KB ceiling did not move. **A physical unit now carries under a fifth of the library.** That does not
make the loadouts worse, but it does further weaken the "buy the loaded unit" argument against "buy a
bare unit plus the $49 digital toolkit" — see §7 and [`UNIT_ECONOMICS.md`](UNIT_ECONOMICS.md) §6.

---

## 4. Buyer's-choice loadout

Offer it, on one SKU only, with tight rules:

- Available on the flagship listing only, as a **free option**, not a paid upgrade. Charging for it
  invites a "you gave me the wrong ones" dispute over money.
- **Cap: 10 programs, 36 KB.** Publish both numbers in the listing. If a buyer picks a set that
  exceeds it, you load the first ten by their stated priority and say so in the shipping note.
- Collected as a message after purchase, with a **48-hour deadline**, after which you ship P6
  (STEM Sampler). Never hold inventory waiting on a buyer to answer; it wrecks your handling-time
  metric, which on eBay directly affects search placement.
- **[ESTIMATE]** Expect fewer than 1 in 5 buyers to use it. Its real function is conversion — it
  makes the listing look bespoke and it makes the software feel like the product rather than a
  bonus. That perception is the entire premium (see [`UNIT_ECONOMICS.md`](UNIT_ECONOMICS.md) §6).

---

## 5. How many SKUs to actually stock

**Stock three. Build the rest to order.**

| Decision | SKU | Why |
|---|---|---|
| **Stock** | **P6 STEM Sampler** | Default for every unit you prep before it's sold. Broadest appeal, no guessing, and it's the fallback when a buyer's-choice deadline lapses. |
| **Stock** | **P1 Calculus** | The largest single addressable group (AP Calculus alone is a very large annual cohort), and the one where College Board's permissive AP memory policy is quotable and true. |
| **Stock** | **P2 Engineering** | Highest willingness to pay per buyer, and the loadout hardest for a buyer to assemble themselves. |
| Build to order | P3 Chemistry, P4 Precalc/Trig, P5 Stats | Real demand, but seasonal and narrow. Loading them takes 5 minutes after the sale (SOP §5), so carrying them as stock only ties up capital. |
| Build to order | P7 Diff Eq | Niche. |

The reasoning is that **a loadout is not inventory.** Reloading a prepped unit from P6 to P3 costs
about five minutes and zero materials. Distinct SKUs cost you listing effort, photo sets, and
inventory-tracking overhead, and they split your sales history across listings — which on eBay
actively hurts you, because a listing with sales history ranks better than three listings with a
third of it each.

**So the right structure is: one flagship multi-quantity listing with a loadout dropdown, plus at
most two dedicated listings for the two loadouts worth their own keywords.** Concretely:

1. **Flagship listing** — "…Pre-Loaded Python Study Programs," quantity 3–6, variation dropdown for
   the loadout, default P6.
2. **Calculus listing** — separate, because "calculus" is a distinct search term worth its own
   title.
3. **Engineering listing** — same reasoning, and it lets you write copy aimed at a different buyer.

Everything else is a message-me option inside those three.

---

## 6. The archive tier — a real option, handle with care

You can send AppVars to **Archive** instead of RAM. Archived Python AppVars don't appear in the
Python App's File Manager and can't be run until the student moves them back
(`[2nd]` `[MEM]` → `2:Mem Management/Delete…` → `B:Var App…` → `[enter]` toggles). Flash archive on
the CE is several megabytes, so space there is not the constraint.

This creates a tempting product: **"all 52 programs on the calculator" — ~10 in RAM, the other ~42
in Archive.** It is a genuinely better story than "10 programs," and it's the only way the
"complete library on a physical unit" claim is even arguably true.

**Do not ship it as the default, for three reasons — and the first one got worse as the library grew:**

1. **[INFERRED, not verified]** Whether archived AppVars fully escape the 50 KB Python budget is not
   something TI states unambiguously. If they don't, the archive tier simply fails — and the tier is
   now **243.5 KB** rather than the 103.9 KB it was when this section was first written, so it overshoots
   the budget by roughly **5× instead of 2×**. The bigger the library gets, the more this option depends
   on an untested inference.
2. It converts a zero-touch product into a two-step one. Every buyer who can't find a program is a
   support message, and some fraction of those become returns.
3. It is fragile in exactly the way this product is already fragile: a memory reset or Press-to-Test
   takes out the archive too, so it doubles the size of the thing the buyer loses.

**Recommended handling:** validate it on your own bench once you have hardware (SOP §5 gives you the
chance). If it works, offer it as a clearly-labelled **"Full Library"** option on the flagship
listing with a plain-language explanation of the two-step access, and see whether anyone chooses it.
If nobody does, you've learned the "more programs" story isn't what buyers are buying — which is
itself the most valuable thing you could learn about this business.

---

## 7. How this interacts with the digital bundles

The digital lineup is **$12–$19 per subject bundle / $49 complete toolkit** (`bundles/PRICING.md`),
with a free 5-program starter pack. The physical units have to be priced and framed against that,
because a buyer can see both.

**The honest arithmetic a buyer can do:** a bare used CE Python plus the $49 complete digital
toolkit gets them *all* the programs rather than a loadout — **52 against 8–10** — for the bare price
plus $49. The gap has widened twice over as the library grew: a physical unit now carries **under a
fifth** of what the digital toolkit delivers, where it used to carry about a third. So the
physical premium can only be justified by what the digital bundle can't deliver: it's already
installed, the OS is current, every program has been launched and checked on that specific unit, and
the buyer never has to install TI Connect CE. That is a **convenience and assurance** premium, not a
software premium, and it is worth far less than $49. [`UNIT_ECONOMICS.md`](UNIT_ECONOMICS.md) §6 puts
a number on it — **$5–$12** — and is not optimistic. Note the toolkit's repricing from $35 to $49
does **not** raise that number; it only widens the gap the physical SKU is arguing against.

Three rules that follow:

1. **Never price a loaded unit above bare-price + $49.** A buyer who does the arithmetic and finds
   your bundled price exceeds à-la-carte will feel worked, and it's the sort of thing that shows up
   in a review. In practice the realistic premium ($5–$12) is nowhere near this ceiling, so treat it as
   a hard stop rather than a target.
2. **Put the free starter pack in the box.** A card with a link to the free 5-program pack costs
   nothing, gives the buyer something to do on day one, and is a legitimate on-ramp to a $12–$19 or
   $49 digital purchase later. The physical unit becomes a customer-acquisition channel for the higher-
   margin digital product, which — given the margins in `UNIT_ECONOMICS.md` §10 — is now clearly the
   most valuable thing the hardware line does.
3. **Offer a discount code, not a free upgrade.** Something like "$10 off the complete toolkit for
   calculator buyers" converts hardware buyers into digital buyers while you still keep ~80% of list
   price, instead of giving away the thing you're trying to sell. It also makes the physical listing
   more attractive without cutting the hardware price.

---

## 8. Loadout summary table

| SKU | Programs | File bytes | On-calc ≈ | % of 50 KB | Free | Stock? |
|---|---:|---:|---:|---:|---:|---|
| P1 Calculus | 9 | 28,606 | 27.3 KB | 54.6% | 22.7 KB | **Yes** |
| P2 Engineering | 9 | 31,630 | 30.2 KB | 60.5% | 19.8 KB | **Yes** |
| P3 Chemistry | 8 | 33,543 | 32.2 KB | 64.4% | 17.8 KB | To order |
| P4 Precalc/Trig | 9 | 34,825 | 33.4 KB | 66.7% | 16.6 KB | To order |
| P5 Stats/Algebra | 8 | 29,848 | 28.6 KB | 57.1% | 21.4 KB | To order |
| P6 STEM Sampler | 10 | 35,080 | 33.5 KB | 67.1% | 16.5 KB | **Yes (default)** |
| P7 DiffEq/Numerical | 9 | 30,425 | 29.1 KB | 58.1% | 20.9 KB | To order |
| Buyer's choice | ≤10 | ≤36,864 | — | ≤72% | ≥14 KB | Option on flagship |
| Full Library (archive tier) | 52 | 249,322 | — | see §6 | — | Experimental only |

**Every row recomputed 2026-08-12** against the regenerated 52-AppVar set; the AppVar names also changed,
so check §2 before building a loadout from an older list. All seven SKUs still satisfy the 16 KB headroom
policy, but **P4 and P6 are now at the ceiling** — neither can take an addition. The seven SKUs use 27 of
the 52 programs; the other 25 are swap-ins.

---

AP®, Advanced Placement®, and SAT® are trademarks registered by the College Board, which is not
affiliated with, and does not endorse, this product. TI-84 Plus CE Python™, TI-84 Evo™,
TI Connect™ CE, TI Connect™ Evo, and Texas Instruments® are trademarks of Texas Instruments
Incorporated, which is not affiliated with, and does not endorse, this product. All trademarks are
the property of their respective owners. Policies subject to change.
