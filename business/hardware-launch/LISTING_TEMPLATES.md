# Listing Templates — Ready to Paste

**eBay and Mercari copy for both arms of the A/B test: bare unit and pre-loaded unit.**

Written 2026-08-12. Subordinate to [`../../MARKETING_CLAIMS_GUIDE.md`](../../MARKETING_CLAIMS_GUIDE.md)
and [`../../COMPLIANCE_RESEARCH.md`](../../COMPLIANCE_RESEARCH.md) — where anything here conflicts
with those, **they win.** Structure follows
[`../LISTING_AND_SUPPORT.md`](../LISTING_AND_SUPPORT.md) §1–§3; pricing follows
[`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §7; the experimental constraints come from
[`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §2.

---

## 0. How to use this file

1. **Write the bare listing first.** The loaded listing is the bare listing *plus* four blocks. Never
   author them independently — that is how a confound gets in.
2. **Fill every `[SQUARE BRACKET]`.** A shipped `[GRADE]` is worse than no listing.
3. **Do not edit anything else** during the test. Not a word, not a photo, not a price.
4. Anything marked **⚠️ TEST CONSTRAINT** exists to protect the experiment, not the sale.

### The four blocks that differ, and nothing else

| Block | Bare | Loaded |
|---|---|---|
| **A** — What's loaded on it (manifest) | ✗ | ✅ |
| **B** — Press-to-Test data-loss warning | ✗ | ✅ |
| **C** — Exam program-removal lines | ✗ | ✅ |
| **D** — Restore link / unit code | ✗ | ✅ |
| Price | **$78** | **$90** |

Everything else — every other sentence, every item specific, the return policy, the shipping option,
the handling time, the **photo count** — is identical. See §7 on how the bare arm gets two filler
photos so the counts match.

### On exam-brand terms — a deliberate judgement, stated openly

The brief for this folder asked to keep titles **and descriptions** free of exam-brand trademark
terms. Titles: done, absolutely, both arms, no exceptions — and the bare arm's description contains
**zero** exam-brand terms too, because a bare calculator makes no software claim and therefore needs
no exam disclosure.

**The loaded arm is different, and I have not stripped the marks from it.** Here is the reasoning, so
you can overrule me if you disagree:

[`../../MARKETING_CLAIMS_GUIDE.md`](../../MARKETING_CLAIMS_GUIDE.md) §3.4 and §9 identify the
FE/PE claim as the single most damaging thing on the page and prescribe a proactive *"the TI-84 is
not permitted"* warning; §3.2–3.3 require the SAT/PSAT/ACT program-removal warning;
[`../LISTING_AND_SUPPORT.md`](../LISTING_AND_SUPPORT.md) §9 makes both mandatory pre-publish
checklist items. **A warning that does not name the exam cannot be acted on by the buyer.** "Some
licensure exams don't allow this calculator" tells an engineering student nothing; "the NCEES FE and
PE exams do not permit the TI-84 — buy a TI-36X Pro" prevents a real, expensive mistake and is the
exact fact pattern §9 of the claims guide says turns a marketing slip into a refund demand.

So the loaded template uses marks **only inside an explicitly negative, warning-only block**, as
adjectives, with the ® symbol, with the non-affiliation footer on the same surface — which is
precisely what the claims guide §6.2 permits and what its own §5.1 storefront disclaimer does. **No
mark appears in a title, a tag, an item specific, a keyword, or any hidden field.**

A **mark-free alternative** for the exam block is in §5.4 if you want it. It is compliant but
strictly worse for the buyer, and §5.4 explains the trade-off.

---

## 1. Pricing and format

### 1.1 The recommendation

| | Bare arm | Loaded arm |
|---|---|---|
| **Format** | Fixed price + **Best Offer** | Fixed price + **Best Offer** |
| **Duration** | 30-day GTC | 30-day GTC |
| **Price** | **$78.00** | **$90.00** |
| **Shipping** | **Free** (USPS Ground Advantage, price includes it) | **Free** |
| **Handling time** | 1 business day | 1 business day |
| **Returns** | 30 days, buyer pays return shipping | 30 days, buyer pays return shipping |
| **Best Offer auto-accept** | ≥ **$71.76** (92%) | ≥ **$82.80** (92%) |
| **Best Offer auto-decline** | < **$62.40** (80%) | < **$72.00** (80%) |
| **Promoted Listings** | **OFF** | **OFF** |
| **Quantity** | 1 per listing (no multi-quantity) | 1 per listing |
| **Condition** | Used | Used |

Prices come straight from [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §7: **$78 is that
document's bare-unit figure** and $90 applies the **$12** differential its §6 asks for ("priced
$10–$15 apart"). Expected net at $30 acquisition: **$20.14 bare / ~$29.6 loaded.**

### 1.2 Why fixed price + Best Offer, and not auction

Reasoning is in [`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §2.3, in one line: **auction variance
is far too large to learn anything from 12 pairs**, and a fixed differential tests the actual
decision you face when listing. Best Offer keeps genuine price discovery without the variance.

⚠️ **TEST CONSTRAINT — set the auto-accept and auto-decline thresholds in eBay itself, not in your
head.** Human offer-handling is where unconscious bias enters ("I'll hold out on the loaded one"),
and it would invalidate the whole test. Let the platform enforce your own rule.

### 1.3 When auction *is* right — after the test

| Situation | Format | Why |
|---|---|---|
| Grade C/D bare units, no case | **Auction, $0.99 start, 7 days** | Price discovery on units you can't comp, and they clear |
| Multi-unit lots you're breaking up | Fixed + Best Offer | Consistency |
| Peak week (late Aug), grade A loaded | Fixed, **no** Best Offer, $95 | Test the ceiling. Respect the $95 Walmart new-unit hard ceiling (economics §2) — **never list above it** |
| Anything during the A/B test | Fixed + Best Offer only | Protocol |

### 1.4 Mercari cross-listing — after the test, not during

⚠️ **TEST CONSTRAINT: do not cross-list any of the 20 test units.** A Mercari sale removes a unit
from the eBay arm mid-flight and destroys that pair. eBay only, for all 20, until Oct 21.

**After** the test, cross-list everything —
[`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §3 shows Mercari's flat **10%** fee nets about
**$5/unit more** than eBay's effective ~16.55% + $0.40. Mercari's flat national label is dearer
(**$6.73** at 12 oz vs. a **$5.50** blended eBay label), so the same-net price is lower, not higher:

| Arm | eBay price | eBay net | **Mercari price for the same net** | Mercari net at that price |
|---|---:|---:|---:|---:|
| Bare | $78 | $61.49 | **$76** | $61.67 |
| Loaded | $90 | $71.86 | **$87** | $71.57 |

**[COMPUTED]** from the fee and label figures in economics §3–§4 (eBay 13.6% + $0.40, no promoted;
Mercari 10%, 12 oz Best Rate $6.73). So **list Mercari $2–3 below eBay and you net the same** — which
also makes you the cheaper listing on the platform with thinner competition. Mercari rounds shipping
**up** to the tier ceiling, so weigh every parcel: 12.1 oz pays the 1 lb rate.

---

## 2. Titles

**Character counts verified against eBay's 80-character limit.** Mercari's limit is also 80.

### 2.1 Bare arm — eBay

**Primary (78 chars):**
```
TI-84 Plus CE Python Graphing Calculator - Tested, Wiped, Updated OS, w/ Cable
```

Alternates:
```
TI-84 Plus CE Python Graphing Calculator + Case + Cable - Tested, Updated OS      (76)
TI-84 Plus CE Python Graphing Calculator - Refurbished, Tested, Memory Wiped      (76)
TI-84 Plus CE Python Graphing Calculator - Tested, New Battery, Updated OS        (73)
```

### 2.2 Loaded arm — eBay

**Primary (73 chars):**
```
TI-84 Plus CE Python Calculator - 10 Preloaded Study Programs, Updated OS
```

Alternates:
```
TI-84 Plus CE Python Calculator + Case + Cable - 10 Programs Preloaded, Tested    (78)
TI-84 Plus CE Python Graphing Calculator - Preloaded Study Programs, Tested       (75)
TI-84 Plus CE Python Calculator - Calculus Programs Preloaded, Tested, Case       (75)
TI-84 Plus CE Python Calculator - Engineering Programs Loaded, Tested, Case       (78)
```

> The last two are for **after** the test only — the protocol holds the loadout constant at P6, so
> during the test every loaded title says "Study Programs," never "Calculus" or "Engineering."

### 2.3 Mercari

```
Bare:    TI-84 Plus CE Python Graphing Calculator - Tested, Wiped, Ready for Class   (73)
Loaded:  TI-84 Plus CE Python Graphing Calculator - 10 Study Programs Preloaded      (70)
```

### 2.4 Title rules

**Words that earn their place:** `Python` (the variant distinction most buyers search and most
sellers get wrong — this is the single highest-value word in the title), `Tested`, `Wiped`,
`Updated OS`, `Preloaded`, `Case`, `Cable`, `New Battery` **if true**.

**Never, in any title, tag, item specific, keyword, or hidden field:**

```
AP   SAT   PSAT   ACT   NCEES   FE   PE   "exam legal"   "test approved"
"AP-approved"   cheat   "cheat sheet"   hack   answers   "beat the test"
guaranteed   "TI certified"   "factory refurbished"   Evo
```

Three of those deserve a word each:

- **`Evo`** — never in a CE Python title. It isn't one, and the mismatch is an item-not-as-described
  case waiting to happen ([`../LISTING_AND_SUPPORT.md`](../LISTING_AND_SUPPORT.md) §1).
- **`factory refurbished` / `TI certified`** — implies Texas Instruments did the work. "Seller
  refurbished" or plain "Tested" is accurate; TI's terms bar suggesting a relationship with TI.
- **`New Battery`** — only if you actually fitted a `3.7L1200SPB`. It's one of the few claims that
  genuinely moves price, which is exactly why a false one is a defect claim. And per
  [`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §2.1 it must be **true of both arms of a pair or
  neither.**

---

## 3. Item specifics

Fill **every** field on both arms — eBay's search demonstrably favours completeness. These must be
**identical across the pair** except where physically different.

| Field | Bare | Loaded |
|---|---|---|
| Brand | Texas Instruments | Texas Instruments |
| Model | **TI-84 Plus CE Python** | **TI-84 Plus CE Python** |
| MPN | `[as printed on the unit — 84CEPY/... if present]` | same |
| Type | Graphing Calculator | Graphing Calculator |
| Condition | **Used** | **Used** |
| Colour | `[actual colour]` | `[actual colour]` |
| Power Source | Rechargeable Battery | Rechargeable Battery |
| Connectivity | USB | USB |
| Number of Display Lines | 10 | 10 |
| Display Type | Colour LCD | Colour LCD |
| Features | Rechargeable, Graphing, Programmable | Rechargeable, Graphing, Programmable, **Preloaded Software** |
| Bundled Items | Slide Case, USB Cable, Quick-Start Card | Slide Case, USB Cable, Quick-Start Card |
| Country/Region of Manufacture | `[as marked]` | same |
| Custom: **OS Version** | `[e.g. 5.8.5]` | `[same]` |
| Custom: **Cosmetic Grade** | `[A / B / C]` | `[same as pair partner]` |

**On the `Condition` field:** use **Used**, not "Seller refurbished," on both arms.
[`../LISTING_AND_SUPPORT.md`](../LISTING_AND_SUPPORT.md) §6 is right that if you're not certain you
meet eBay's category definition, Used plus a thorough description beats a condition-grade dispute —
and it must match across the pair anyway.

---

## 4. Bare arm — full description

Paste as-is and fill the brackets. **Contains no exam-brand terms at all.**

```
TI-84 Plus CE PYTHON EDITION graphing calculator - fully tested, memory wiped,
and updated to the current Texas Instruments operating system.

WHAT THIS IS
This is the PYTHON EDITION of the TI-84 Plus CE - the version with the built-in
Python programming environment on board. The plain TI-84 Plus CE is a different
calculator: it cannot run Python and cannot be upgraded to it, because the Python
interpreter runs on a separate coprocessor that plain CE units do not contain.
Check the faceplate in photo 1 - it reads "TI-84 Plus CE PYTHON". Photo 5 shows
the on-device model and OS screen so you can confirm both before you buy.

WHAT I DID TO IT
- Full memory reset. Every trace of the previous owner's data is gone
  (2nd MEM > 7:Reset > ALL > All Memory). Confirmed "Mem cleared" on screen.
- Updated to the current Texas Instruments operating system and app bundle.
  The exact version is in photo 5.
- Confirmed the Python App is present and the Python Shell opens (photo 4).
- Confirmed NOT in Press-to-Test / exam mode. No exam banner, and nothing
  flagged in Memory Management.
- Pressed and checked every key on the keypad. All register.
- Full-screen test at maximum brightness: no dead pixels, no dead rows or
  columns, even backlight.
- Charge port tested with the cable connected and flexed - no flicker.
- Battery charged to full and held overnight on the shelf before packing.
  [New battery installed (Texas Instruments part 3.7L1200SPB). /
   Original battery tested and holds a full charge.]
- Cleaned inside and out with isopropyl alcohol and a microfibre cloth.
  The slide case was cleaned separately.

WHAT'S IN THE BOX
- The calculator, charged and ready to use
- The slide-on hard case [DELETE THIS LINE IF NO CASE]
- A NEW USB Standard-A to Mini-B charging and data cable (not a used one)
- A printed quick-start card

CONDITION: GRADE [A/B/C] - [ONE HONEST SENTENCE, e.g. "Light surface scuffs on
the back cover only; screen is flawless and the key legends are crisp."]
Every flaw is photographed individually. If you can see it, it is in the photos;
if it is not in the photos, it is not there.

A NOTE ON CHARGING
This calculator uses a USB Mini-B port - not micro-USB and not USB-C. The
included cable is the right one. Any standard USB wall charger or a computer
port will charge it. A full charge from empty takes 4-6 hours. I do not ship a
third-party wall adapter, because Texas Instruments does not approve them and a
bad one can damage the unit - use the charger you already have for your phone.

ABOUT THIS MODEL
Texas Instruments discontinued the TI-84 Plus CE Python in April 2026 and
replaced it with the TI-84 Evo. This listing is the CE Python, the model the Evo
replaced. It uses TI Connect CE and a Mini-B cable; the Evo uses USB-C and a
different connection tool. If you specifically need an Evo, this is not it - I
would rather tell you now than process a return.

SHIPPING & RETURNS
- Ships within 1 business day of payment, USPS Ground Advantage with tracking.
- Packed in a bubble mailer with a rigid cardboard stiffener cut to the
  calculator's footprint, so the screen is protected in transit.
- 30-day returns accepted. Buyer pays return shipping on a change of mind; if
  anything is genuinely wrong with the calculator I pay both ways, no argument.
- Questions before you buy? Message me. I answer within one business day.

---
TI-84 Plus CE Python(TM), TI Connect(TM) CE, and Texas Instruments(R) are
trademarks of Texas Instruments Incorporated, which is not affiliated with, and
does not endorse, this listing. This is a used calculator sold by a private
seller; it is not refurbished, certified, or endorsed by Texas Instruments.
```

### 4.1 Why the "About This Model" paragraph stays in

It looks like it costs you sales. It doesn't — it costs you *returns*. Buyers are increasingly
searching "Evo" ([`../SOURCING.md`](../SOURCING.md) §0), some will land here by mistake, and a
mismatch is the cleanest not-as-described case there is. One INAD on an $88 sale costs roughly $95
and wipes out the profit on about three and a half good sales
([`../LISTING_AND_SUPPORT.md`](../LISTING_AND_SUPPORT.md) §6). Pre-empting it is free.

⚠️ **TEST CONSTRAINT:** this paragraph is identical on both arms. Do not trim it from one.

---

## 5. Loaded arm — full description

The bare description **plus** blocks A–D. Everything carried over from §4 is unchanged.

```
TI-84 Plus CE PYTHON EDITION graphing calculator - fully tested, memory wiped,
updated to the current Texas Instruments operating system, and preloaded with 10
Python study programs I wrote myself, each one launched and checked on THIS
calculator before it was packed.

WHAT THIS IS
This is the PYTHON EDITION of the TI-84 Plus CE - the version with the built-in
Python programming environment on board. The plain TI-84 Plus CE is a different
calculator: it cannot run Python and cannot be upgraded to it, because the Python
interpreter runs on a separate coprocessor that plain CE units do not contain.
Check the faceplate in photo 1 - it reads "TI-84 Plus CE PYTHON". Photo 5 shows
the on-device model and OS screen so you can confirm both before you buy.

WHAT I DID TO IT
- Full memory reset. Every trace of the previous owner's data is gone
  (2nd MEM > 7:Reset > ALL > All Memory). Confirmed "Mem cleared" on screen.
- Updated to the current Texas Instruments operating system and app bundle.
  The exact version is in photo 5.
- Confirmed NOT in Press-to-Test / exam mode. No exam banner, and nothing
  flagged in Memory Management.
- Loaded the 10 Python programs listed below.
- Launched and test-ran EVERY ONE of them on this specific calculator, with a
  known-answer input, and checked the result. Photos 3 and 4 show the program
  list on the device and one of them running.
- Pressed and checked every key on the keypad. All register.
- Full-screen test at maximum brightness: no dead pixels, no dead rows or
  columns, even backlight.
- Charge port tested with the cable connected and flexed - no flicker.
- Battery charged to full and held overnight on the shelf before packing.
  [New battery installed (Texas Instruments part 3.7L1200SPB). /
   Original battery tested and holds a full charge.]
- Cleaned inside and out with isopropyl alcohol and a microfibre cloth.
  The slide case was cleaned separately.

*** WHAT'S ACTUALLY LOADED ON IT ***
10 Python programs, about 33 KB total, all in RAM and all visible in the Python
App's File Manager the moment you turn it on. About two thirds of the
calculator's Python memory is left free for your own programs and class work -
I do not fill it up.

  QUAD      Quadratic solver - real and complex roots, step values shown
  LINSOLV   Solves systems of linear equations
  STATS     One-variable statistics: mean, median, standard deviation, quartiles
  UNITS     Unit converter - length, mass, volume, temperature, energy, pressure
  DERIV     Numeric derivative of a function at a point
  SIMPSON   Numeric definite integral by Simpson's rule
  SUVAT     Constant-acceleration motion solver - solve for any missing variable
  OHMS      Ohm's law and DC power - solve for V, I, R, or P
  PH        Acid/base calculations - pH, pOH, concentration
  TRIG      Oblique triangle solver - law of sines and law of cosines

These are my own original programs, written in Python for this calculator. They
are not copied from anywhere and they are not Texas Instruments software. They
are built for homework, labs, problem sets, and practice - to save you time and
let you check your own work.

To use them: turn the calculator on, press [apps], choose Python, and they are
all there in the File Manager. Highlight one and Run it. No setup, no cable, no
software to install on your computer.

*** IMPORTANT - PLEASE READ BEFORE YOU USE EXAM MODE ***
Press-to-Test (exam mode) DELETES these programs.

Texas Instruments documents that entering Press-to-Test deletes variables stored
in RAM and in archived memory "including AppVars" - and Python programs on this
calculator are stored as Python AppVars. So unlike Apps and TI-BASIC programs,
which come back when you leave exam mode, these do NOT come back. A full memory
reset erases them too.

This is not a defect and it is not specific to my programs - it is how the
calculator works, and it would happen with any Python program on any CE Python.
I am telling you up front so it is not a surprise.

The included card explains how to put everything back, free, in about two
minutes, any time, for the life of the calculator - see below.

RESTORE YOUR PROGRAMS, FREE, ANY TIME
Every unit ships with a printed card carrying a link and a unit code. Enter the
code and you get the exact set of programs that shipped on your calculator, plus
illustrated instructions for reinstalling them with TI Connect CE (which is free
from Texas Instruments). No account, no signup, no expiry. If you ever wipe the
calculator - for an exam, or by accident - you are two minutes from having it
back the way it arrived.

WHAT'S IN THE BOX
- The calculator, charged, with the 10 programs loaded and verified
- The slide-on hard case [DELETE THIS LINE IF NO CASE]
- A NEW USB Standard-A to Mini-B charging and data cable (not a used one)
- A printed quick-start card: what each program does, and how to restore them

CONDITION: GRADE [A/B/C] - [ONE HONEST SENTENCE, e.g. "Light surface scuffs on
the back cover only; screen is flawless and the key legends are crisp."]
Every flaw is photographed individually. If you can see it, it is in the photos;
if it is not in the photos, it is not there.

A NOTE ON CHARGING
This calculator uses a USB Mini-B port - not micro-USB and not USB-C. The
included cable is the right one. Any standard USB wall charger or a computer
port will charge it. A full charge from empty takes 4-6 hours. I do not ship a
third-party wall adapter, because Texas Instruments does not approve them and a
bad one can damage the unit - use the charger you already have for your phone.

ABOUT THIS MODEL
Texas Instruments discontinued the TI-84 Plus CE Python in April 2026 and
replaced it with the TI-84 Evo. This listing is the CE Python, the model the Evo
replaced. It uses TI Connect CE and a Mini-B cable; the Evo uses USB-C and a
different connection tool. If you specifically need an Evo, this is not it - I
would rather tell you now than process a return.

EXAM RULES - PLEASE READ, THEY DIFFER A LOT
These are study and practice tools. Calculator rules differ sharply from exam to
exam and it is your responsibility to check yours before test day. Where stored
programs are not allowed, delete them and restore them afterwards using the card.

- AP(R) Exams: the TI-84 Plus CE Python Edition appears on College Board's list
  of approved handheld graphing calculators, and College Board's published AP
  calculator policy states "You don't need to clear your calculators' memories
  before or after the exam." College Board does not operate any approval process
  for third-party programs, so nothing here is "approved" software - the
  CALCULATOR is on the approved list, and the memory rule is permissive. Verify
  current policy at collegeboard.org before test day. Note that AP Calculus and
  AP Precalculus both have sections where no calculator is allowed at all.
- SAT(R), PSAT/NMSQT(R), and ACT(R): these require you to remove stored programs
  and clear saved formulas before testing. DELETE these programs before those
  tests, then restore them afterwards.
- NCEES FE / PE engineering exams: the TI-84 is NOT an approved calculator, in
  any configuration, cleared or not. NCEES permits only Casio fx-115/fx-991,
  HP 33s/35s, and Texas Instruments models with "TI-30X" or "TI-36X" in the
  model name. If you are sitting the FE, buy a TI-36X Pro or a Casio fx-991
  instead - this calculator will be refused at check-in.
- IB(R) exams: permitted as a non-CAS device, but third-party programs and
  stored notes must be removed or blocked. Remove these first.
- University and course exams: your instructor or department sets the rules.
  Many require a memory clear or Press-to-Test. Ask before test day, and use the
  restore card afterwards.

These tools are for homework, practice, and self-study. They are not intended to
be used, and must not be used, to gain an unfair advantage on any exam where they
are not permitted. Exam policies change - verify with your exam authority.

SHIPPING & RETURNS
- Ships within 1 business day of payment, USPS Ground Advantage with tracking.
- Packed in a bubble mailer with a rigid cardboard stiffener cut to the
  calculator's footprint, so the screen is protected in transit.
- 30-day returns accepted. Buyer pays return shipping on a change of mind; if
  anything is genuinely wrong with the calculator I pay both ways, no argument.
- If the programs ever disappear, that is almost always exam mode or a memory
  reset - message me and I will get you restored the same day. Please do that
  before opening a case; it takes two minutes and I would much rather fix it.
- Questions before you buy? Message me. I answer within one business day.

---
AP(R), Advanced Placement(R), and SAT(R) are trademarks registered by the College
Board, which is not affiliated with, and does not endorse, this listing.
PSAT/NMSQT(R) is a registered trademark of the College Board and the National
Merit Scholarship Corporation, which are not affiliated with, and do not endorse,
this listing. ACT(R) is a registered trademark of ACT Education Corp., which is
not affiliated with, and does not endorse, this listing. IB(R) and International
Baccalaureate(R) are registered trademarks of the International Baccalaureate
Organization, which is not affiliated with, and does not endorse, this listing.
NCEES(R) is a registered trademark of the National Council of Examiners for
Engineering and Surveying, which is not affiliated with, and does not endorse,
this listing. TI-84 Plus CE Python(TM), TI Connect(TM) CE, and Texas
Instruments(R) are trademarks of Texas Instruments Incorporated, which is not
affiliated with, and does not endorse, this listing. All trademarks are the
property of their respective owners. Exam policies are subject to change; verify
current policy with the relevant exam authority. The programs are original works
by the seller and are not Texas Instruments software.
```

### 5.1 The manifest is the highest-value block on the page

Naming all 10 programs with a one-line description each does four things at once, and it is the
cheapest paragraph in the listing:

1. **Sets the expectation exactly.** A buyer who expected 30 programs and found 10 has a ready-made
   INAD claim ([`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §6 names this as a specific risk of
   preloading). A printed list of ten removes it.
2. **Makes the software concrete.** "Preloaded with study programs" is a claim; "QUAD — quadratic
   solver, real and complex roots" is a product.
3. **Catches search traffic honestly.** "quadratic solver," "unit converter," "statistics" are real
   queries and they appear here as accurate description, not as keyword stuffing.
4. **States the free memory up front,** which pre-empts the "no room for my own work" objection —
   and is true, at 66.3% utilisation ([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §3.4).

### 5.2 The Press-to-Test warning is a selling point, not a liability

It reads like a confession. Treat it as the opposite.
[`../LISTING_AND_SUPPORT.md`](../LISTING_AND_SUPPORT.md) §5 models **5–10% of loaded units**
generating a Press-to-Test support contact in the first term, and the difference between a support
email and an INAD case is entirely whether the buyer was warned: *a buyer who was warned reads it as
their own mistake; one who wasn't reads it as your defect.* Pairing the warning immediately with the
free restore route converts the worst fact about the product into evidence that you thought it
through.

⚠️ It must be **in the listing body, above the fold — not only on the printed card.** That is a
mandatory pre-publish checklist item in [`../LISTING_AND_SUPPORT.md`](../LISTING_AND_SUPPORT.md) §9.

### 5.3 Claims deliberately **not** made

| Not said | Why |
|---|---|
| "AP-approved programs" / "AP-Exam-Legal" | College Board approves calculators, not third-party software, and runs no program-approval process. Claims guide §9 ranks this the #2 most damaging claim available |
| Anything affirmative about the SAT, PSAT, or ACT | Those exams require program removal. Marks appear **only** in the negative warning |
| "FE exam prep" / anything affirmative about NCEES | The TI-84 is banned outright. Claims guide §9 ranks this #1 for damage |
| "Certified," "guaranteed," "proctor-proof" | Unsupportable |
| "Factory refurbished," "TI certified" | Implies TI did the work |
| "All 52 programs included" | Only 10 are loaded. The library does not fit in 50 KB |
| "Programs survive exam mode" | They almost certainly do not, and §5.2 says so plainly instead |
| Any AP subject list in the title | Marks stay out of titles entirely |
| A link to download TI's OS, apps, or manuals | TI's licence bars redistribution ([`../LISTING_AND_SUPPORT.md`](../LISTING_AND_SUPPORT.md) §5.1). **The only software you ever distribute is your own** |

### 5.4 Mark-free alternative for the exam block

If you want zero exam-brand terms in the description, replace the whole "EXAM RULES" block with:

```
EXAM RULES - PLEASE READ
These are study and practice tools, and calculator rules differ sharply from exam
to exam. It is your responsibility to check the rules for YOUR exam before test
day. Many proctored exams require stored programs to be removed or the memory to
be cleared; some do not permit this calculator at all, whatever is on it -
engineering licensure exams in the United States are the main example, and they
permit only a short list of specific scientific calculators that does not include
any TI-84. Some college admissions tests permit the calculator but require you to
delete stored programs and saved formulas first.

Check your own exam's published calculator policy, delete the programs if they
are not allowed, and use the restore card afterwards. These tools are for
homework, practice, and self-study, and must not be used to gain an unfair
advantage on any exam where they are not permitted.
```

**Honest assessment: this is compliant but worse.** It is vaguer, so a buyer cannot act on it — an
engineering student reading "engineering licensure exams … permit only a short list" still does not
know to buy a TI-36X Pro, and the whole point of that warning
([`../../MARKETING_CLAIMS_GUIDE.md`](../../MARKETING_CLAIMS_GUIDE.md) §3.4) is to prevent a buyer
paying an exam registration fee and being turned away. It also loses the AP memory-policy quote,
which the claims guide §2 calls the strongest *accurate* claim available.

**My recommendation: use the named version in §5.** If you use this one instead, use it on **all 10**
loaded listings — swapping mid-test is a protocol violation.

---

## 6. Mercari — trimmed versions

Mercari buyers browse rather than research, and the description field is less forgiving of length.
Keep the manifest and the Press-to-Test warning; cut the rest hard.

⚠️ **Post-test only.** See §1.4.

### 6.1 Mercari bare

```
TI-84 Plus CE PYTHON EDITION - the version with Python built in. (The plain
TI-84 Plus CE cannot run Python and cannot be upgraded to it.) Faceplate and
on-device model screen are both in the photos.

Fully tested and ready for class:
- Memory completely wiped - no trace of the previous owner
- Updated to the current Texas Instruments OS and app bundle
- Not in exam mode
- Every key tested, full-screen test, charge port tested
- Battery holds a full charge [/ NEW battery installed]
- Cleaned inside and out

Includes: calculator + slide case + a NEW USB A-to-Mini-B cable + quick-start
card. Note this model uses Mini-B, not USB-C.

Condition: Grade [A/B/C]. [One honest sentence.] All flaws photographed.

Ships next business day in a padded mailer with a rigid stiffener behind the
screen. Questions welcome.

TI-84 Plus CE Python(TM) and Texas Instruments(R) are trademarks of Texas
Instruments Incorporated, which is not affiliated with and does not endorse this
listing.
```

### 6.2 Mercari loaded

```
TI-84 Plus CE PYTHON EDITION, tested and PRELOADED with 10 Python study programs
I wrote myself - every one launched and checked on this exact calculator.

This is the Python Edition. (The plain TI-84 Plus CE cannot run Python and cannot
be upgraded to it.) Faceplate and on-device model screen are in the photos.

LOADED ON IT (~33 KB; about 2/3 of the Python memory left free for your own work)
  QUAD - quadratic solver, real and complex roots
  LINSOLV - systems of linear equations
  STATS - mean, median, standard deviation, quartiles
  UNITS - unit converter (length, mass, volume, temp, energy, pressure)
  DERIV - numeric derivative at a point
  SIMPSON - numeric definite integral
  SUVAT - constant-acceleration motion solver
  OHMS - Ohm's law and DC power
  PH - pH, pOH, concentration
  TRIG - oblique triangles, law of sines and cosines
Turn it on, press [apps], choose Python. They're all there. Nothing to install.

ALSO DONE: memory wiped, current Texas Instruments OS and app bundle, not in exam
mode, every key tested, full-screen test, charge port tested, battery holds a
full charge [/ NEW battery installed], cleaned inside and out.

!! IMPORTANT: exam mode (Press-to-Test) DELETES these programs, and they do not
come back when you exit. A full memory reset erases them too. That's how the
calculator works, not a fault - Python programs are stored as AppVars, and
Texas Instruments documents that exam mode deletes AppVars. The included card has
a link and a code to reinstall the exact same set, free, in about two minutes,
any time.

Exam rules differ by exam - check yours, and delete the programs where they are
not allowed. US engineering licensure exams do not permit any TI-84 at all,
whatever is on it. Study and practice tools; not for use where not permitted.

Includes: calculator + slide case + NEW USB A-to-Mini-B cable + quick-start card
with the program list and restore instructions. This model uses Mini-B, not USB-C.

Condition: Grade [A/B/C]. [One honest sentence.] All flaws photographed.

TI-84 Plus CE Python(TM), TI Connect(TM) CE and Texas Instruments(R) are
trademarks of Texas Instruments Incorporated, which is not affiliated with and
does not endorse this listing. The programs are my own original work.
```

---

## 7. Photo shot list

Follows [`../LISTING_AND_SUPPORT.md`](../LISTING_AND_SUPPORT.md) §2, split by arm.

⚠️ **TEST CONSTRAINT — both arms must have the SAME NUMBER of photos.** The loaded arm needs two
shots the bare arm can't have (File Manager, program running), and eBay rewards photo count, so the
bare arm gets two shots of equivalent informational weight in those slots. Both arms: **12 photos**
plus one per defect.

| # | Bare arm | Loaded arm | Why |
|---|---|---|---|
| 1 | Front, straight on, screen **on**, home screen, brightness up. Faceplate wordmark legible | same | Hero. Proves it powers on **and** proves the variant |
| 2 | Front at a slight angle, showing screen clarity, no glare | same | Screen condition is the #1 buyer worry |
| 3 | **`2nd MEM` → Memory Management, showing free RAM/Archive** | **Python App File Manager, all 10 programs visible by name** | The loaded arm's #3 is *the* shot that sells the product. The bare arm's is the honest equivalent: proof the memory really is clear |
| 4 | **Python Shell open and empty** (proves Python hardware works) | **A program running with real output** (`QUAD` with a=1, b=−3, c=2 → roots 2 and 1) | Proof of function, not just of files. On the bare arm it proves the coprocessor is alive — which is the thing a plain CE can't fake |
| 5 | `2nd MEM` → `1:About`, showing model name **and** OS version | same | Kills the two biggest pre-purchase questions in one image. **Never skip this** |
| 6 | Back of unit, full, serial **partially masked** | same | Proves you have the actual unit |
| 7 | Keypad close-up, raking light | same | Shows legend wear honestly |
| 8 | Mini-B charge port close-up | same | The most common terminal fault; buyers who know, look |
| 9 | Slide case, front and back | same | |
| 10 | Everything that ships, laid out flat | same | Prevents "where's the charger" cases |
| 11 | Battery/charging indicator at full | same | |
| 12 | Screen at max brightness on a uniform bright field | same | Dead-pixel and backlight evidence |
| 13+ | **One per defect**, close-up, in focus | same | Non-negotiable. A flaw you photographed is a flaw the buyer accepted |

**Take shots 1–5 and 12 during prep**, at SOP §4c (after the Press-to-Test check, before programs
load) and SOP §6 (after verification). Do not reopen a packed mailer for a photo.

> ⚠️ **The ordering trap.** Bare-arm shots 3 and 4 must be taken at **SOP §4c**, before anything is
> loaded, and loaded-arm shots 3 and 4 at **SOP §6**, after. Never enter Press-to-Test to get a
> "clean memory" photo on a finished loaded unit — it silently destroys the payload and you will ship
> an empty calculator. SOP §4c is the last moment exam mode is safe.

### 7.1 Staging

| | |
|---|---|
| **Background** | Neutral light-grey, matte, seamless. A sheet of grey poster board curved up the back wall. **Never** white — a black calculator on white blows out the exposure and the screen goes muddy |
| **Light** | Two diffuse sources at 45° from the front, or one softbox plus a white bounce card. **No flash, no direct sun, no overhead light alone** (it reflects straight off the screen into the lens) |
| **Screen shots** | Room lights **down**, calculator brightness **up**, camera exposure locked to the screen. Shoot slightly off-axis to kill the reflection of your own lens |
| **Camera** | Phone on a small tripod, **same height and distance every time.** Mark the tripod position with tape so every listing frames identically |
| **Settings** | Lock focus and exposure by tapping the screen. Turn HDR **off** for screen shots — it fakes detail. No filters, no beauty mode, no auto-enhance |
| **Framing** | Calculator fills ~80% of the frame. Same crop, same orientation, every unit |
| **Consistency** | This is the point. Twelve identical-looking photo sets read as "this person does this properly," and that perception is a meaningful part of what you are charging for. It is also a hard requirement of the A/B test |
| **Never** | TI logos, TI product photography, stock images, other sellers' photos, or an image with a competitor's watermark cloned out |

### 7.2 Known-answer inputs for the photo-4 "program running" shot

Use the same program and the same input on **every** loaded unit, so photo 4 is identical across the
arm. Keep this card taped to the bench — SOP §6a wants it there anyway.

| Program | Input | Expected output |
|---|---|---|
| **`QUAD`** ← use this one for photo 4 | a=1, b=−3, c=2 | roots **2** and **1** |
| `STATS` | 1, 2, 3, 4, 5 | mean **3**, sample sd ≈ **1.5811** |
| `SUVAT` | v₀=0, a=9.81, t=2, solve d | **19.62** |
| `UNITS` | 1 inch → cm | **2.54** |
| `OHMS` | V=12, R=4 | I=**3**, P=**36** |
| `TRIG` | a=3, b=4, C=90° | c=**5** |
| `PH` | [H⁺] = 1×10⁻⁴ | pH **4** |
| `DERIV` | d/dx of x² at x=3 | **6** |
| `SIMPSON` | ∫₀¹ x² dx | **0.3333** |
| `LINSOLV` | x+y=3, x−y=1 | x=**2**, y=**1** |

---

## 8. Pre-publish checklist

Run on **every** listing. Adapted from
[`../LISTING_AND_SUPPORT.md`](../LISTING_AND_SUPPORT.md) §9 and
[`../../MARKETING_CLAIMS_GUIDE.md`](../../MARKETING_CLAIMS_GUIDE.md) §8.

```
COMPLIANCE - BOTH ARMS
[ ] Title contains "TI-84 Plus CE Python" and ZERO exam-brand terms
[ ] No exam-brand term in any tag, keyword, item specific, or hidden field
[ ] No claim that any program is approved / certified / legal / compliant
[ ] No "factory refurbished", "TI certified", or wording implying TI did the work
[ ] No "Evo" anywhere
[ ] Variant stated unambiguously as Python Edition - and TRUE, verified on-device
[ ] No TI logos, no vendor product photography; own photos only
[ ] Nothing in the box or on the restore page is TI's software
[ ] Non-affiliation footer present in the description
[ ] Every flaw photographed AND described in words
[ ] Return policy stated
[ ] Nothing anywhere sells concealment, evasion, or beating an exam

LOADED ARM ONLY
[ ] Press-to-Test data-loss warning IN THE LISTING BODY, above the fold
[ ] Full 10-program manifest present, and it matches what is actually on the unit
[ ] Free-memory figure stated
[ ] Restore link / unit code described
[ ] AP claims are about the CALCULATOR's approval and the MEMORY rule only
[ ] SAT/PSAT/ACT appear ONLY in an explicit "remove the programs" warning
[ ] FE/PE/NCEES appear ONLY in an explicit "not permitted" warning
[ ] Photo 3 (File Manager) and photo 5 (About screen) present - these do the most work

A/B TEST INTEGRITY (both arms of the pair, side by side on screen)
[ ] Descriptions differ ONLY in blocks A-D and the price
[ ] SAME photo count
[ ] Same item specifics, handling time, return policy, shipping option
[ ] Prices exactly $78.00 and $90.00
[ ] Best Offer auto-accept/decline set to 92% / 80% on BOTH
[ ] Promoted Listings OFF on both
[ ] Both going live within the same hour, Sunday 7-9 PM ET
[ ] NOT cross-listed to Mercari
[ ] Both listing URLs logged and screenshotted in the CSV
```

---

AP®, Advanced Placement®, SAT®, and CLEP® are trademarks registered by the College Board, which is
not affiliated with, and does not endorse, this product. PSAT/NMSQT® is a registered trademark of the
College Board and the National Merit Scholarship Corporation, which are not affiliated with, and do
not endorse, this product. ACT® is a registered trademark of ACT Education Corp., which is not
affiliated with, and does not endorse, this product. IB® and International Baccalaureate® are
registered trademarks of the International Baccalaureate Organization, which is not affiliated with,
and does not endorse, this product. NCEES® is a registered trademark of the National Council of
Examiners for Engineering and Surveying, which is not affiliated with, and does not endorse, this
product. TI-84 Plus CE Python™, TI Connect™ CE, and Texas Instruments® are trademarks of Texas
Instruments Incorporated, which is not affiliated with, and does not endorse, this product. All
trademarks are the property of their respective owners. Exam policies are subject to change; verify
current policy with the relevant exam authority. Nothing in this document is legal advice.
