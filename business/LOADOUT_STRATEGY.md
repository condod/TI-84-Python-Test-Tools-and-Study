# Loadout Strategy — What Actually Goes On A Physical Unit

The library is **29 programs, 106,409 bytes (103.9 KB)** of `.8xv` AppVars. The calculator's Python
environment holds **50 KB**. The whole library does not fit, and no amount of format tinkering
changes that. Deciding what goes on a unit is therefore a product decision, not a packing decision.

This document defines the physical SKUs, their measured footprints, and how many of them you should
actually stock.

---

## 1. The hard constraint, quoted

TI, *Python Programming for the TI-84 Plus CE* (v5.7 guide) and the Python App Messages eGuide page
(<https://education.ti.com/html/webhelp/EG_TI84PlusCEPY/EN/content/eg_pythonappprog/m_pymessages/m_pymessages.HTML>,
accessed 2026-08-12):

> "The available memory for the Python experience will be a maximum of **100 Python programs
> (PY AppVars) or 50K of memory.** The modules that are bundled with the app in this Python release
> will share the same space with all files."

Two things follow that most people get wrong:

1. **The program-count limit is not the binding one.** 100 programs is far more than 29. Bytes are
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

---

## 2. Per-program footprint

| Program | Bytes | KB | Subject |
|---|---:|---:|---|
| `QUADSOLV` | 2,068 | 2.0 | Algebra |
| `RLCIMPED` | 2,427 | 2.4 | Physics/Eng |
| `DERIVNUM` | 2,474 | 2.4 | Calculus |
| `SIMPSON` | 2,665 | 2.6 | Calculus |
| `LINSOLVE` | 2,673 | 2.6 | Algebra |
| `LIMITEVL` | 2,683 | 2.6 | Calculus |
| `COMBPROB` | 2,700 | 2.6 | Algebra/Stats |
| `HEATXFER` | 3,159 | 3.1 | Physics/Eng |
| `NEWTRAPH` | 3,302 | 3.2 | Calculus |
| `ACIDBASE` | 3,389 | 3.3 | Chemistry |
| `VECTOR3D` | 3,417 | 3.3 | Physics/Eng |
| `OHMSLAW` | 3,429 | 3.3 | Physics/Eng |
| `TAYLOR` | 3,471 | 3.4 | Calculus |
| `KINEMAT` | 3,578 | 3.5 | Physics/Eng |
| `STATICS` | 3,642 | 3.6 | Physics/Eng |
| `ODEEULER` | 3,803 | 3.7 | Diff Eq |
| `PROJECTL` | 3,849 | 3.8 | Physics/Eng |
| `DESCSTAT` | 3,892 | 3.8 | Stats |
| `FLASHCRD` | 3,996 | 3.9 | Study tools |
| `UNITCONV` | 4,025 | 3.9 | Cross-subject |
| `MATRIX` | 4,028 | 3.9 | Linear algebra |
| `COMPLEX` | 4,033 | 3.9 | Algebra |
| `DISCRETE` | 4,100 | 4.0 | CS |
| `MOLARMAS` | 4,334 | 4.2 | Chemistry |
| `EXAMDRIL` | 4,678 | 4.6 | Study tools |
| `IDEALGAS` | 4,850 | 4.7 | Chemistry |
| `QUADVERT` | 4,992 | 4.9 | Algebra |
| `OBLIQUE` | 5,361 | 5.2 | Trig |
| `PUNNETT` | 5,391 | 5.3 | Biology |
| **All 29** | **106,409** | **103.9** | — |

Median program: ~3.7 KB. Practical rule of thumb: **a physical loadout is 8–10 programs.** Twelve
is already crowding the headroom policy; fifteen breaks it.

> **Measurement basis, and drift.** These sizes were measured from the `8xv/` directory as it stood
> on 2026-08-12 (29 AppVars, 106,409 bytes). The repo is actively growing — the `.py` source tree
> already carries programs (geometry, fluid mechanics, orbital mechanics, reaction kinetics,
> confidence intervals) that have no regenerated `.8xv` yet. **Re-run the measurement before each
> production batch:**
>
> ```powershell
> Get-ChildItem -Recurse -File -Filter *.8xv |
>   Select-Object Name, Length | Sort-Object Length
> ```
>
> New programs are candidates for the loadouts below, but every substitution must keep the loadout
> under the headroom policy. Adding without removing is how you end up shipping a full calculator.

---

## 3. The physical SKU loadouts

All seven are defined and measured. §5 says which ones to actually stock.

### P1 — Calculus Unit · 9 programs · 27,253 B / 26.6 KB · ~26.0 KB on-calc · **24.0 KB free (51.9% used)**

`DERIVNUM` · `SIMPSON` · `NEWTRAPH` · `LIMITEVL` · `TAYLOR` · `QUADSOLV` · `LINSOLVE` · `DESCSTAT` · `UNITCONV`

The five calculus tools plus the three cross-subject staples a calculus student still needs
(quadratics, linear systems, one-variable stats) and the unit converter. The lightest loadout and
the one with the most room left over — appropriate, because this buyer is the most likely to write
their own programs.

Fits: AP® Calculus AB/BC coursework, Calculus I/II, first numerical-methods exposure.

### P2 — Engineering Unit · 9 programs · 31,554 B / 30.8 KB · ~30.2 KB on-calc · **19.8 KB free (60.3% used)**

`KINEMAT` · `PROJECTL` · `OHMSLAW` · `RLCIMPED` · `STATICS` · `VECTOR3D` · `HEATXFER` · `MATRIX` · `UNITCONV`

The full physics/engineering set plus matrices and unit conversion, which are the two things an
engineering student reaches for across every course.

Fits: Physics I/II, Statics, Circuits, intro Thermodynamics.

> **Naming warning.** Call this the "Engineering Unit," never anything containing "FE," "PE,"
> "NCEES," or "licensure." The TI-84 is banned outright on NCEES exams. See
> [`LISTING_AND_SUPPORT.md`](LISTING_AND_SUPPORT.md) §3.

### P3 — Chemistry Unit · 8 programs · 32,323 B / 31.6 KB · ~31.0 KB on-calc · **19.0 KB free (62.0% used)**

`IDEALGAS` · `MOLARMAS` · `ACIDBASE` · `UNITCONV` · `HEATXFER` · `DESCSTAT` · `FLASHCRD` · `EXAMDRIL`

The four chemistry tools, plus `HEATXFER` (calorimetry is chemistry as much as physics), stats for
lab data, and the two study-drill tools.

Fits: General/Intro Chemistry, AP® Chemistry coursework.

### P4 — Precalculus & Trigonometry Unit · 9 programs · 33,772 B / 33.0 KB · ~32.3 KB on-calc · **17.7 KB free (64.7% used)**

`OBLIQUE` · `QUADSOLV` · `QUADVERT` · `COMPLEX` · `LINSOLVE` · `MATRIX` · `COMBPROB` · `DESCSTAT` · `UNITCONV`

Fits: Precalculus, Trigonometry, College Algebra, AP® Precalculus coursework.

### P5 — Statistics & Algebra Unit · 8 programs · 28,060 B / 27.4 KB · ~26.8 KB on-calc · **23.2 KB free (53.6% used)**

`DESCSTAT` · `COMBPROB` · `QUADSOLV` · `LINSOLVE` · `MATRIX` · `UNITCONV` · `FLASHCRD` · `EXAMDRIL`

Fits: Intro Statistics, AP® Statistics coursework, College Algebra.

### P6 — STEM Sampler (general-purpose) · 10 programs · 35,015 B / 34.2 KB · ~33.5 KB on-calc · **16.5 KB free (66.9% used)**

`QUADSOLV` · `LINSOLVE` · `DESCSTAT` · `UNITCONV` · `DERIVNUM` · `SIMPSON` · `KINEMAT` · `OHMSLAW` · `IDEALGAS` · `OBLIQUE`

One program from every major subject area. This is the SKU for a buyer who doesn't know what they
need — a parent buying for a kid, or a student taking four different STEM classes. It is at the
headroom ceiling; do not add to it.

### P7 — Differential Equations & Numerical Methods Unit · 9 programs · 29,132 B / 28.4 KB · ~27.8 KB on-calc · **22.2 KB free (55.6% used)**

`ODEEULER` · `NEWTRAPH` · `DERIVNUM` · `SIMPSON` · `LIMITEVL` · `TAYLOR` · `MATRIX` · `LINSOLVE` · `COMPLEX`

Fits: Differential Equations, Calculus III, numerical methods. Narrow audience — build to order.

### Not in any default SKU

`DISCRETE` (4.0 KB) and `PUNNETT` (5.3 KB) don't fit a mainstream physical SKU: discrete math
students rarely buy a TI-84 for the course, and College Board has announced that from 2027 AP®
Biology and AP® Environmental Science will not allow calculators with storage capabilities, which
kills the obvious biology angle. Keep both as **free swap-ins** on the buyer's-choice option (§4) —
they cost nothing to offer and they make the "you pick" option feel genuinely custom.

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

This creates a tempting product: **"all 29 programs on the calculator" — ~10 in RAM, the other ~19
in Archive.** It is a genuinely better story than "10 programs," and it's the only way the
"complete library on a physical unit" claim is even arguably true.

**Do not ship it as the default, for three reasons:**

1. **[INFERRED, not verified]** Whether archived AppVars fully escape the 50 KB Python budget is not
   something TI states unambiguously. If they don't, a 104 KB archive tier simply fails.
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

The digital lineup is **$14 per subject bundle / $35 complete toolkit** (`bundles/PRICING.md`), with
a free 3-program starter bundle. The physical units have to be priced and framed against that,
because a buyer can see both.

**The honest arithmetic a buyer can do:** a bare used CE Python plus the $35 complete digital
toolkit gets them *more programs* than any physical SKU, for the bare price plus $35. So the
physical premium can only be justified by what the digital bundle can't deliver: it's already
installed, the OS is current, every program has been launched and checked on that specific unit, and
the buyer never has to install TI Connect CE. That is a **convenience and assurance** premium, not a
software premium, and it is worth less than $35. [`UNIT_ECONOMICS.md`](UNIT_ECONOMICS.md) §6 puts a
number on it and is not optimistic.

Three rules that follow:

1. **Never price a loaded unit above bare-price + $35.** A buyer who does the arithmetic and finds
   your bundled price exceeds à-la-carte will feel worked, and it's the sort of thing that shows up
   in a review.
2. **Put the free starter bundle in the box.** A card with a link to the free 3-program bundle costs
   nothing, gives the buyer something to do on day one, and is a legitimate on-ramp to a $14/$35
   digital purchase later. The physical unit becomes a customer-acquisition channel for the higher-
   margin digital product, which — given the margins in `UNIT_ECONOMICS.md` — may be the most
   valuable thing the hardware line does.
3. **Offer a discount code, not a free upgrade.** Something like "$10 off the complete toolkit for
   calculator buyers" converts hardware buyers into digital buyers at ~72% margin instead of giving
   away the thing you're trying to sell. It also makes the physical listing more attractive without
   cutting the hardware price.

---

## 8. Loadout summary table

| SKU | Programs | File bytes | On-calc ≈ | % of 50 KB | Free | Stock? |
|---|---:|---:|---:|---:|---:|---|
| P1 Calculus | 9 | 27,253 | 26.0 KB | 51.9% | 24.0 KB | **Yes** |
| P2 Engineering | 9 | 31,554 | 30.2 KB | 60.3% | 19.8 KB | **Yes** |
| P3 Chemistry | 8 | 32,323 | 31.0 KB | 62.0% | 19.0 KB | To order |
| P4 Precalc/Trig | 9 | 33,772 | 32.3 KB | 64.7% | 17.7 KB | To order |
| P5 Stats/Algebra | 8 | 28,060 | 26.8 KB | 53.6% | 23.2 KB | To order |
| P6 STEM Sampler | 10 | 35,015 | 33.5 KB | 66.9% | 16.5 KB | **Yes (default)** |
| P7 DiffEq/Numerical | 9 | 29,132 | 27.8 KB | 55.6% | 22.2 KB | To order |
| Buyer's choice | ≤10 | ≤36,864 | — | ≤72% | ≥14 KB | Option on flagship |
| Full Library (archive tier) | 29 | 106,409 | — | see §6 | — | Experimental only |

---

AP®, Advanced Placement®, and SAT® are trademarks registered by the College Board, which is not
affiliated with, and does not endorse, this product. TI-84 Plus CE Python™, TI Connect™ CE, and
Texas Instruments® are trademarks of Texas Instruments Incorporated, which is not affiliated with,
and does not endorse, this product. All trademarks are the property of their respective owners.
Policies subject to change.
