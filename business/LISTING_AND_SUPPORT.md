# Listing & Support Playbook — Physical Units

Marketplace copy, photography, the Press-to-Test warning, returns policy, exam-claim rules, and the
legal operating rules for selling a used calculator with your own software on it.

**This document is subordinate to [`COMPLIANCE_RESEARCH.md`](../COMPLIANCE_RESEARCH.md) and
[`MARKETING_CLAIMS_GUIDE.md`](../MARKETING_CLAIMS_GUIDE.md).** Where anything here conflicts with
those, they win. Everything in §3 below is lifted directly from the claims guide's "safe to
say / do NOT say" tables and is not negotiable.

---

## 1. Listing titles

### The rules that shape the title

From `MARKETING_CLAIMS_GUIDE.md` §6.2, all of which apply to marketplace titles:

- Never lead a title with a College Board mark. "AP® Calculus Bundle" is out; "…for AP® Calculus
  coursework" inside the description is fine.
- **No exam-brand terms in titles, tags, keywords, or item specifics at all.** No "AP," no "SAT,"
  no "ACT," no "FE," no "NCEES." This costs you some search volume. Pay it.
- "TI-84 Plus CE Python" in the title is nominative compatibility use and is fine — you literally
  cannot describe the item otherwise. Never build "TI" or "TI-84" into your shop name or handle.
- No TI logos, no TI product photography. Your own photos only.

### eBay (80-character limit)

Front-load the model, then condition signals, then the differentiator. eBay's search weights the
first words most.

```
TI-84 Plus CE Python Graphing Calculator - Tested, Wiped, Updated OS, Preloaded
```
(78 chars)

Variants:

```
TI-84 Plus CE Python Calculator - Preloaded Study Programs, New Battery, Tested
TI-84 Plus CE Python Graphing Calculator + Case + Cable - Refurbished & Loaded
TI-84 Plus CE Python Calculator - Calculus Programs Preloaded, Latest OS 5.8.5
TI-84 Plus CE Python Calculator - Engineering Programs Loaded, Tested, w/ Cable
```

Words that earn their place: **Python** (this is the variant distinction most buyers search and
most sellers get wrong), **tested**, **wiped**, **preloaded**, **new battery** if true, **case**,
**cable**. Words to avoid: "cheat," "hack," "exam-legal," "AP," "SAT," "ACT," "guaranteed," "Evo."

> **On "Latest OS 5.8.5."** Still literally true, and now likely to stay true permanently: with the CE
> Python discontinued and TI marking "Continued OS support" as an Evo-only feature, **[INFERRED]**
> 5.8.5 is probably the final CE release ([`PREP_SOP.md`](PREP_SOP.md) §1). The wording is safe as
> written, but "Latest" reads as a perishable freshness claim on a frozen platform. **Once TI's end of
> CE OS support is actually confirmed** — it has not been announced, only inferred from a product
> sheet — switch to **"OS 5.8.5 (final CE release)"**, which is both more honest and a stronger
> reassurance: the buyer will never be told their calculator is out of date. Do not make that change
> before there is something to cite.

### Mercari (80-character limit, more casual)

```
TI-84 Plus CE Python Graphing Calculator - Tested + Preloaded Study Programs
```

### Facebook Marketplace (short, plain, local)

```
TI-84 Plus CE Python Graphing Calculator - Tested, Charged, Ready for Class
```

Facebook buyers search short generic strings. "TI 84" and "graphing calculator" carry the query;
everything after that is reassurance.

### Item specifics / attributes (eBay)

Fill every one. eBay's search demonstrably favours completeness.

| Field | Value |
|---|---|
| Brand | Texas Instruments |
| Model | TI-84 Plus CE Python |
| MPN | as printed on the unit |
| Type | Graphing Calculator |
| Condition | Used (or "Seller refurbished" — see §6) |
| Colour | as applicable |
| Power source | Rechargeable battery |
| Connectivity | USB |
| Bundled items | Slide case, USB cable, quick-start card |
| Custom: OS Version | e.g. 5.8.5 |

### One title note on the TI-84 Evo

TI replaced the CE Python with the **TI-84 Evo** in April 2026 ([`SOURCING.md`](SOURCING.md) §0).
Buyers will increasingly search "Evo," and some will land on your listing by mistake. Don't chase
that traffic — **never put "Evo" in a CE Python title**, since it isn't one and the mismatch is an
"item not as described" case waiting to happen. Keep "evo" out of tags, keywords, and item specifics
too, for the same reason.

Address it in the **description** instead, and address the part that actually generates disputes.
The first version of this note suggested mentioning TI Connect CE and the Mini-B cable, which is
true but incomplete: **an Evo owner cannot use the program files at all.** Python AppVars on the Evo
use a different extension (`.8xv2`) and the Evo rejects legacy files outright
([`EVO_TRANSITION.md`](EVO_TRANSITION.md) Q2). That is the fact a mistaken buyer needs before they
pay, not after.

**Recommended description line** — honest, short, and it doubles as a filter:

```
NOTE ON THE TI-84 EVO: this is the TI-84 Plus CE Python Edition, the model the
TI-84 Evo replaced in 2026. It is not an Evo. It charges and connects with the
included USB Mini-B cable and TI Connect CE (free from TI). If you specifically
own or need a TI-84 Evo, this is not the right listing for you - the Evo uses a
different cable, different connection software, and a different program file
format, so the preloaded programs would not transfer to it.
```

### Telling the three live variants apart — put this in front of the buyer

**Stop treating the model name as the compatibility unit.** There are now three things on the market
that a buyer might call "a TI-84 CE," and the model name no longer determines whether your programs
run. The determinant is simply **"does this calculator have the Python app."**

| Variant | Runs Python? | Runs *these* programs? | How the buyer identifies it |
|---|---|---|---|
| **TI-84 Plus CE Python Edition** (what you sell) | Yes | **Yes** | Faceplate reads "TI-84 Plus CE **PYTHON**". Mini-B charge port. |
| **Plain TI-84 Plus CE** | **No**, and cannot be upgraded | No | Faceplate reads "TI-84 Plus CE" with no PYTHON wordmark. Note TI began shipping *new* CE units without Python in early 2026, so "recently bought" proves nothing. |
| **TI-84 Evo** | Yes — **every** Evo has Python, there is no separate Python edition | **Not yet supported.** The `.py` sources are expected to work; the `.8xv` files definitely do not. | USB-**C** port. Icon-based UI. Connects at `connectevo.ti.com`, not TI Connect CE. |

**Give buyers a calculator-side self-check rather than a model number.** One line in the listing turns
the most likely refund cause into a pre-sale filter:

```
NOT SURE IF YOUR CALCULATOR CAN RUN THESE? Press [prgm] and look for a Python
app in the list. If there's no Python app, the programs will not run on it.
```

State supported hardware explicitly as the **CE Python family** — TI-84 Plus CE Python Edition,
TI-84 Plus CE-T Python Edition, TI-83 Premium CE Edition Python — and name the **Evo as not yet
supported**. Never write a bare "TI-84 family," and **never claim tested Evo compatibility until it
has actually been tested on an Evo.** No "should work."

---

## 2. Photo shot list

Twelve photos, same order every time, same background every time. Consistency across your listings
reads as "this person does this properly," and that perception is a meaningful part of what you're
charging for. Neutral light-grey background, diffuse daylight, no flash, no props, no filters.

| # | Shot | Why |
|---|---|---|
| 1 | Front, straight on, screen **on**, home screen, brightness up | Hero image. Proves it powers on. |
| 2 | Front at a slight angle showing screen clarity and no glare | Screen condition is the #1 buyer worry. |
| 3 | **Python App File Manager showing the loaded programs by name** | This is the shot that sells the product. Nothing else communicates "preloaded" credibly. |
| 4 | **A program actually running with output on screen** (e.g. `QUADSOLV` showing roots) | Proof it works, not just that files exist. |
| 5 | `[2nd]` `[MEM]` `1:About` screen showing model name and OS version | Proves the variant is Python **and** that the OS is current. Kills the two biggest pre-purchase questions at once. |
| 6 | Back of unit, full, showing serial number **partially masked** | Proves you have the actual unit. Mask enough that it can't be used to impersonate your listing. |
| 7 | Keypad close-up, raking light | Shows key legend wear honestly. |
| 8 | Mini-B charge port close-up | The most common failure point; buyers who know, look. |
| 9 | Slide case, front and back | |
| 10 | Everything that ships, laid out flat: calculator, case, cable, quick-start card | Sets expectations exactly and prevents "where's the charger" cases. |
| 11 | **Any and every defect, close-up, in focus** | One per flaw. Non-negotiable — see §6. |
| 12 | Battery/charging indicator at full | |

Photograph shots 1–5 during SOP §4c and §6, while the unit is on the bench. Do not re-open a packed
box to take a photo.

---

## 3. Description template

Use this structure on every platform; trim for Mercari/Facebook.

```
TI-84 Plus CE PYTHON EDITION graphing calculator - fully refurbished, tested,
and preloaded with a curated set of Python study programs.

WHAT THIS IS
This is the Python Edition of the TI-84 Plus CE - the version with the built-in
Python programming environment. (The plain TI-84 Plus CE cannot run Python and
cannot be upgraded to it.) Check the faceplate in the photos, and photo 5 shows
the on-device model/OS screen.

WHAT I DID TO IT
- Full memory reset: every trace of the previous owner's data removed
  (2nd MEM > 7:Reset > ALL > All Memory).
- Updated to the current Texas Instruments operating system and app bundle
  (version shown in photo 5).
- Confirmed NOT in Press-to-Test / exam mode.
- Preloaded with [LOADOUT NAME]: [N] Python programs I wrote myself
  ([list program names]).
- Every single program launched and test-run on THIS calculator before it
  was packed - see photos 3 and 4.
- Cleaned inside and out. [New battery installed. / Battery tested and holds
  a full charge.]
- Full key-by-key test, screen test, and charge-port test.

WHAT'S IN THE BOX
- The calculator
- Slide-on hard case [if included]
- A new USB Standard-A to Mini-B charging/data cable
- A printed quick-start card, including how to restore the programs
- A link to re-download the programs any time, free, for the life of the unit

CONDITION: [Grade + one honest sentence + "all flaws photographed"]

ABOUT THE PROGRAMS
These are [N] Python programs I wrote for the TI-84 Plus CE Python: [short
plain-language list, e.g. "a quadratic solver, a numeric derivative and
integral tool, a kinematics solver, a unit converter..."]. They're built for
homework, labs, problem sets, and practice exams - to save you time and let
you check your own work.

*** READ THIS BEFORE YOU USE EXAM MODE ***
Press-to-Test (exam mode) DELETES Python programs. Texas Instruments documents
that entering Press-to-Test deletes variables stored in RAM and archived memory
"including AppVars," and Python programs on this calculator are stored as
Python AppVars. Unlike Apps and TI-BASIC programs, they do NOT come back when
you exit exam mode. A full memory reset erases them too.

This is not a defect and it is not specific to my programs - it is how the
calculator works. The included card tells you how to re-download and re-install
everything in about two minutes with TI Connect CE, free, any time.

EXAM POLICIES - PLEASE READ
Calculator rules differ sharply by exam and it is your responsibility to check
yours before test day.
- AP(R) Exams: the TI-84 Plus CE Python Edition is on College Board's list of
  approved handheld graphing calculators, and College Board's published AP
  calculator policy states "You don't need to clear your calculators' memories
  before or after the exam." Verify current policy at collegeboard.org.
- SAT(R), PSAT/NMSQT(R), and ACT(R): these require you to remove stored
  programs and clear saved formulas. Remove these programs before those tests.
- NCEES FE/PE engineering exams: the TI-84 is NOT an approved calculator, in
  any configuration. Only Casio fx-115/fx-991, HP 33s/35s, and TI-30X/TI-36X
  models are permitted. If you are sitting the FE, buy a TI-36X Pro instead -
  this calculator will be refused at check-in.
- IB, and university/course exams: your school or instructor sets the rules.
  Many require a memory clear or Press-to-Test. Ask first, and back up before
  you do it.

These are study and practice tools. They are not intended to be used, and must
not be used, to gain an unfair advantage on any exam where they are not
permitted.

SHIPPING & RETURNS
[Per section 6.]

---
AP(R), Advanced Placement(R), SAT(R), and CLEP(R) are trademarks registered by
the College Board, which is not affiliated with, and does not endorse, this
product. PSAT/NMSQT(R) is a registered trademark of the College Board and the
National Merit Scholarship Corporation, which are not affiliated with, and do
not endorse, this product. ACT(R) is a registered trademark of ACT Education
Corp., which is not affiliated with, and does not endorse, this product. IB(R)
and International Baccalaureate(R) are registered trademarks of the
International Baccalaureate Organization, which is not affiliated with, and
does not endorse, this product. NCEES(R) is a registered trademark of the
National Council of Examiners for Engineering and Surveying, which is not
affiliated with, and does not endorse, this product. TI-84 Plus CE Python(TM),
TI Connect(TM) CE, and Texas Instruments(R) are trademarks of Texas Instruments
Incorporated, which is not affiliated with, and does not endorse, this product.
All trademarks are the property of their respective owners. Exam policies are
subject to change; verify current policy with the relevant exam authority.
```

### Why the FE/PE warning stays in

It looks like it costs you sales. It doesn't. Engineering students cannot use this calculator on the
FE regardless of what your listing says, so you were never going to keep that sale — you were only
going to receive a return, a negative review, and, if the buyer had already paid an FE registration
fee, a genuine grievance. Proactively naming the calculator they actually need is verifiably true,
costs nothing, and makes every other claim on the page more credible. This is the claims guide's
position (§3.4) and it is correct.

### Keywords: what to use and what to leave on the table

**Use:** `TI-84 Plus CE Python`, `graphing calculator`, `Python calculator`, `preloaded`,
`programs installed`, `refurbished`, `tested`, `new battery`, `student calculator`,
`calculus programs`, `engineering programs`, `chemistry programs`, `back to school`,
`college calculator`, `high school math`.

**Never use, anywhere, including hidden fields:** `AP`, `SAT`, `PSAT`, `ACT`, `NCEES`, `FE exam`,
`PE exam`, `exam legal`, `test approved`, `cheat`, `cheat sheet`, `hack`, `answers`,
`beat the test`. College Board's guidelines explicitly bar its marks in "meta tags," ACT's terms bar
any use of its marks without written consent, and the cheating terms are what get a listing pulled
and an account flagged.

**Also never use, for a different reason:** `evo`, `TI-84 Evo`. Not a compliance problem — an accuracy
one. While the product is CE-only, Evo search traffic is traffic you cannot serve, and every mistaken
buyer it brings in is a return. Revisit only if an Evo edition actually ships.

---

## 4. The quick-start card (goes in every box)

One card, printed both sides. This is the highest-leverage support document you have: almost every
avoidable message is answered by something on it.

**Front:**

```
YOUR TI-84 PLUS CE PYTHON IS READY TO GO

Turn it on -> press [apps] -> choose Python -> your programs are in
the File Manager. Highlight one and Run it.

LOADED ON THIS UNIT: [loadout name]
[program list, one per line, with a five-word description each]

OS version on this unit: [x.x.x]
Serial (last 4): [xxxx]
Charging: any USB charger + the included Standard-A to Mini-B cable.
First charge from empty takes 4-6 hours.
```

**Back:**

```
!!! IMPORTANT: EXAM MODE WILL ERASE THESE PROGRAMS !!!

Press-to-Test (exam mode) and a full memory reset both DELETE Python
programs. They do not come back when you leave exam mode. This is how
the calculator works, not a fault.

BEFORE an exam that requires exam mode: that's fine - go ahead.
AFTER the exam: put the programs back in about two minutes.

TO RESTORE YOUR PROGRAMS, FREE, ANY TIME:
  1. Go to [restore URL]  and enter code [UNIT CODE]
  2. Install TI Connect CE (free, from education.ti.com)
  3. Connect the calculator with the USB cable
  4. Drag the program files onto Calculator Explorer
Full illustrated instructions are at that link.

Questions or a problem? [support email]. I answer within one business day.
I would much rather fix something than have you leave a bad review.

Study tool. Exam rules vary - check your exam's calculator policy.
Not permitted on NCEES FE/PE exams. Not affiliated with or endorsed by
College Board, ACT, or Texas Instruments.
```

---

## 5. Press-to-Test: the support problem, and how to actually handle it

### The fact

`COMPLIANCE_RESEARCH.md` §7.1 chains two TI statements:

- TI Press-to-Test Guidebook: *"Other variables stored in RAM and in archived memory (including
  AppVars) are deleted."*
- TI CE Python eGuide: *"Python programs stored or created as Python AppVars will execute from
  RAM."*

Conclusion: **entering Press-to-Test destroys the customer's Python programs.** Flash Apps and
TI-BASIC programs are merely *disabled* and return on exit; AppVars are deleted and do not. TI
never writes that exact sentence on a CE Python page, so the repo labels it a strongly-supported
inference — but the buyer instruction is identical either way, so give it unconditionally.

### Why this is a business problem, not just a documentation problem

Your buyer is a student. Some non-trivial fraction of them will be told by an instructor to enter
Press-to-Test before a midterm. They will do it, the programs will vanish, and the very next thing
that happens is either a support email or an eBay "item not as described" case. **[ESTIMATE]** I'd
model 5–10% of loaded units generating a Press-to-Test support contact within the first term. If
you have no answer ready, a meaningful share of those become returns, and a return on a used
calculator eats several units' worth of margin.

Handled well, the same fact is a selling point: *"designed to be stripped for a proctored exam and
restored in two minutes."*

### Recommendation: ship a restore link with every unit. Yes, definitely.

**Do it.** The objection — "they'll share the link and I'll lose digital sales" — does not survive
contact with the numbers. The programs on a physical unit are a subset (8–10 of 52), they're already
in the buyer's hands, and the person who bought a $90 calculator was never a likely $35 digital
customer. Meanwhile a single prevented return is worth more than several hypothetical leaked
downloads.

**Recommended mechanism, in order of preference:**

1. **Best: a per-unit code on a static page.** Host a single unlisted page (GitHub Pages is free and
   you already have the repo) containing a ZIP of that unit's exact loadout, the install
   instructions, and the Press-to-Test explanation. Print a short unit code on the card that maps to
   the loadout — so the page can say "Engineering loadout — these 9 files." Costs nothing, no
   account required, no login friction, works forever. Requiring a login or an email signup to
   restore something the buyer already paid for is how you earn a one-star review.
2. **Acceptable: a QR code to the same page.** Add it to the card. Do not make it the *only* route;
   print the URL too.
3. **Also do this: put a copy of the loadout on the calculator's own Archive.** If a buyer archives
   a second copy of each AppVar, a *Press-to-Test* event still kills it (archive is wiped too) — so
   this is not a real backup. Mention it only as convenience, never as protection.
4. **Do not** ship a USB stick. It adds cost, it dates, and it invites you to put TI's software on
   it, which you must not do (§5.1).

**What must be on that page:** your programs, install instructions, the Press-to-Test explanation, a
link to TI's own site for TI Connect CE and the OS. **What must never be on that page:** TI's OS
file, TI's apps, or TI's guidebook PDFs.

### 5.1 The legal operating rules

**Reselling the hardware is fine.** The first-sale doctrine (17 U.S.C. §109) means that once a
lawfully-made copy of a copyrighted work is sold, the owner of that copy may resell it without the
copyright holder's permission. You bought a used calculator; you may sell the used calculator. This
is the same doctrine that makes every used-book store and every used-phone listing lawful.
**[INFERRED]** — this is settled general law, not a TI-specific finding, and this document is not
legal advice.

**Bundling your own original software with it is fine.** These are original works you authored.
Nothing restricts selling them, on their own or installed on hardware you also own. `COMPLIANCE_RESEARCH.md`
§8.1 reaches the same conclusion: *"The risk in this business is not whether you may sell it — it is
what you say about it."*

**Redistributing TI's software is NOT fine.** TI's OS licence
(<https://education.ti.com/en/customer-support/end-user-license-agreement-for-os>, accessed
2026-08-12) states:

> "TI grants you a license to copy and use the software program(s) **on a TI calculator** and copy
> and use the documentation… In addition to the copy resident on your calculator, you may keep a
> copy on your computer **for backup / archive purposes only.**"
>
> "You may **not sell, rent or lease copies** of the Licensed Materials."

**Operating rules that follow — treat these as absolute:**

| Allowed | Not allowed |
|---|---|
| Download TI's OS/Apps bundle from TI and flash it onto a calculator you own and are servicing | Put TI's OS file, apps, or guidebook PDFs on a USB stick in the box |
| Keep one archival copy of the bundle on your bench computer | Host TI's OS or apps on your own site, GitHub repo, or restore page |
| Link buyers to TI's own download pages for TI Connect CE and the OS | Email a buyer a copy of TI's OS or TI Connect CE installer |
| Sell the calculator with TI's factory OS and apps on it, as TI shipped it | Advertise "includes TI software" as if it were something you're supplying |
| State the OS version the unit is running | Sell an OS update as a separately-priced add-on line item |

The clean framing: **you are servicing a device, not distributing software.** Updating a calculator
you own before selling it is ordinary refurbishment. The moment a TI file leaves your bench on
anything other than a calculator, you've crossed the line.

### 5.2 The "I have an Evo" support answer

You will get this message, and increasingly often: someone bought the digital bundle, or was gifted a
new calculator, and now owns a **TI-84 Evo**. Have the answer ready. It costs nothing to write once and
it prevents both a bad review and a refund.

**The three facts to convey, in this order** (evidence in [`EVO_TRANSITION.md`](EVO_TRANSITION.md)):

1. **The `.8xv` files will not work.** This is definite, not a maybe. Python AppVars on the Evo use a
   new `.8xv2` extension and the Evo rejects legacy TI-84 files outright.
2. **The `.py` files are expected to work, and that is what they should send.** TI Connect Evo
   auto-converts `.py` on send. Say "expected," not "will" — we have not tested it on hardware.
3. **The transfer tool is different.** `connectevo.ti.com` in Chrome over USB-C, not TI Connect CE.
   TI Connect CE will not connect to an Evo at all.

**Support macro, ready to send:**

```
Thanks for writing - and good news, mostly.

The .8xv files in the bundle are for the TI-84 Plus CE Python and will NOT
transfer to a TI-84 Evo. TI changed the file format on the Evo (Python files
there use a .8xv2 extension), and the Evo rejects the older files. So please
ignore the 8xv folder entirely.

What you want are the .py files, which are the same programs in plain Python
source. Texas Instruments' own transfer tool for the Evo converts .py files
automatically when you send them, so those should work as-is:

  1. Open Chrome and go to connectevo.ti.com  (no install, no sign-in)
  2. Connect the calculator with a USB-C cable
  3. Choose Send Files, pick the .py files, and send
  4. Open the Python app on the calculator to run them

One honest caveat: I have not yet tested this library on physical Evo hardware,
so I can't promise it end to end - I'm telling you what TI's documentation and
the transfer tool's behaviour say. If anything doesn't work, tell me exactly
what happened and I'll either fix it or refund you. I'd genuinely like the
report.

Note that TI Connect CE (the desktop app for the older calculators) will not
connect to an Evo at all, so don't spend time on that.
```

**Two rules on this macro.** Never upgrade "expected to work" to "works" until the hardware test pass
in [`EVO_TRANSITION.md`](EVO_TRANSITION.md) is done — the offer to refund is what makes the honest
version safe to send. And never send an Evo owner the `8xv/` folder as though it might work; that is
the version of this conversation that ends in a dispute.

**For a hardware buyer who turns out to want an Evo,** the answer is shorter: this is a CE Python, it
is not an Evo, the programs won't transfer to one, and if they haven't bought yet they should not.
Take the pre-sale loss; it is far cheaper than the return.

Two further notes:

- **Do not use "refurbished by Texas Instruments," "TI Certified," "factory refurbished," or any
  wording implying TI did the work.** "Seller refurbished" or "professionally refurbished by me" is
  accurate. TI's own terms bar suggesting "that TI promotes, endorses, or has any relationship with
  any third party."
- **No TI logos and no TI product photography.** Your own photos only. This is the claims guide's
  rule and it is also just correct.

---

## 6. Returns, refunds, and condition disclosure

### Policy stance: 30-day returns, buyer pays return shipping

Recommended on eBay. Reasoning:

- eBay's Money Back Guarantee covers buyers for "item not as described" regardless of your stated
  policy, so a no-returns policy on used electronics buys you very little actual protection — it
  mostly signals "difficult seller" and suppresses conversion.
- 30-day returns is the threshold that qualifies a listing for eBay's better search treatment and
  Top Rated Seller benefits, and the conversion lift is real.
- Buyer-paid return shipping filters out casual remorse returns while leaving genuine defect cases
  intact (where you should just pay it anyway).
- Free 30-day returns is the safest possible policy but adds a return-shipping liability against a
  thin per-unit margin. Not recommended until the volume supports it.

### The four specific return scenarios, and what to do

| Scenario | Response |
|---|---|
| **"The programs disappeared."** Almost always Press-to-Test or a memory reset. | Never treat as a defect. Reply within a day with the restore link and a two-line explanation, and offer to walk them through it on a call. This should close ~90% of these without a return. **[ESTIMATE]** This is also why the warning has to be prominent in the *listing*, not just the box — a buyer who was warned reads it as their mistake; one who wasn't reads it as your defect. |
| **Genuine hardware fault inside 30 days.** | Full refund including return shipping, no argument, immediately. On a used-electronics business the cost of a fast refund is always lower than the cost of a defended case. Then diagnose the unit and fix your QC. |
| **Buyer's remorse / "I meant to buy the cheaper one."** | Accept the return, buyer pays return shipping, restock and relist. Do not fight it. |
| **"I wanted / already have a TI-84 Evo."** | Accept the return without argument — this one is partly on the listing, and fighting it looks bad in a category where the variants genuinely confuse people. Then fix the cause: the Evo note and the `[prgm]` self-check in §1 exist precisely to catch this buyer *before* they pay. If you see this twice, your description is at fault, not the buyer. For a **digital** customer in this position, don't refund reflexively — send the §5.2 macro first; the `.py` files may well solve it. |

### The INAD math — why one dispute hurts far more than it looks

**One not-as-described case on an $88 sale costs roughly $95**: the refund, your original shipping
(unrecoverable), the return label you must pay for, and the packaging. Against a ~$28 net per unit,
**a single INAD wipes out the profit on about three and a half good sales.** That asymmetry, not the
refund itself, is why the disclosure discipline below is worth real time.

**Worse, eBay's seller metrics are peer-relative and your denominator is tiny.** eBay benchmarks you
against sellers in your category, price band, condition, and return policy rather than an absolute
number — its own worked example shows a peer-group average INAD rate of **1.3%**, with **7.8%**
flagged as "Very High," and its guidance elsewhere uses **0.83%** as an illustrative average.
Critically, there is a **safe harbour: eBay does not penalise you below 1% of transactions** in most
categories. At 10–50 units a month, **one or two disputes in a quarter can statistically flag you**
purely because you have so few transactions to average against — and a Very High INAD rating adds
**+5% to your fees** (§3 of [`UNIT_ECONOMICS.md`](UNIT_ECONOMICS.md)).
(<https://www.ebay.com.au/help/policies/selling-policies/service-metrics-policy?id=4769>, accessed
2026-08-12.) [RESEARCHED]

### Money Back Guarantee mechanics — know the clocks

If a case does open, the timings decide the outcome more than the merits do:

1. The buyer has **30 days from delivery** to open a not-as-described return.
2. **You must respond within 3 business days.** eBay may accept the return on your behalf if you
   don't.
3. For damaged, faulty, or not-as-described items, **you pay return shipping even if you offer no
   returns.** eBay can issue the label and bill you.
4. Once the item is back, you have **3 business days to refund**, or eBay may refund automatically.
5. **If you provide no return method and eBay steps in, it may refund the buyer and let them keep the
   item.** That is the worst outcome available and it is entirely self-inflicted — it only happens
   when you don't respond.
6. Appeals must be filed within **30 calendar days** of eBay's decision, with photos.

(<https://www.ebay.com.au/help/buying/returns-refunds/ebay-money-back-guarantee-policy?id=4210>,
accessed 2026-08-12.)

**Operational rule: answer every case the same day. Never let one age.**

### Always buy shipping labels through the platform

This is worth a paragraph because the temptation to save a dollar at Pirate Ship is real. Buy the
label through eBay and ship before the estimated delivery date, and eBay's Seller Protection handles
item-not-received reports on orders up to $750 **without you refunding**, removes the defect from
your service metrics, and removes related negative and neutral feedback.
(<https://www.ebay.com.au/help/policies/selling-policies/seller-protection-policy?id=4345>, accessed
2026-08-12.) **A dollar of label savings is not worth forfeiting INR protection on an $88 item.**

### Condition disclosure

- Photograph **every** flaw individually (shot 11) and describe each in words as well. A flaw you
  photographed is a flaw the buyer accepted; a flaw you didn't is an INAD case you will lose.
- Use the exact grade language from [`PREP_SOP.md`](PREP_SOP.md) §8 so grades mean the same thing
  across listings.
- On eBay, "Seller refurbished" requires you to actually meet eBay's definition for that condition
  in the category; if you're not certain you qualify, list as **Used** and describe the refurb work
  in the description. Used + a thorough description beats a condition-grade dispute.
- **Never** describe a plain TI-84 Plus CE as a Python unit, even by omission. It is the single most
  likely INAD claim in this category, it is unambiguous, and you will lose it.

---

## 7. Platform-by-platform notes

| Platform | Verdict | Notes |
|---|---|---|
| **eBay** | **Primary channel.** | Best buyer intent for a specific model, best search for "TI-84 Plus CE Python," and buyers there accept used-electronics norms. Fees are the highest, and the return exposure is real. Fee model in [`UNIT_ECONOMICS.md`](UNIT_ECONOMICS.md) §3. |
| **Mercari** | **Secondary, but the best margin of the shipped channels.** | Flat **10%** seller fee, no listing fee, no per-order fee, no seller payment processing [RESEARCHED — see [`UNIT_ECONOMICS.md`](UNIT_ECONOMICS.md) §3] — about **$6/unit better than eBay** on an $88 sale. Traffic for this specific model is much thinner, and the browse-driven audience responds less to the preloaded story. Cross-list everything and take the Mercari sale when it comes. |
| **Facebook Marketplace** | **Best margin, worst scale.** | Local pickup means no shipping cost and no platform fee, and it's the single highest-margin channel per unit. But it's slow, buyers haggle hard, no-shows are routine, and August is the only month with real volume. Use it to clear bare and grade-C/D units. |
| **Etsy** | **Avoid for hardware.** | `COMPLIANCE_RESEARCH.md` §8.4: Etsy requires everything listed to be "made, designed, handpicked, or sourced by a seller," and how Etsy classifies "mass-produced device + seller's software" is **unverified**. The digital bundles are fine there; the calculators are a takedown risk for no upside. |
| **Your own storefront (Gumroad/direct)** | **For digital only.** | Selling hardware direct means you eat payment processing, fraud risk, and all your own traffic acquisition, with no marketplace demand. Not worth it at this volume. |
| **Whatnot / live selling** | **Not yet.** | Works for volume lots and impulse categories. A single-model calculator at ~$90 is a poor fit until you have real inventory depth. |

---

## 8. Seasonality and timing the listings

Calculator demand is violently seasonal. **[ESTIMATE — directionally certain, magnitudes are my
modelling, see [`SOURCING.md`](SOURCING.md) §4 for the sourcing side]**

- **Late July → mid September:** peak sell-side. List everything. Do not discount. This is when a
  loaded unit has its best chance of clearing at the top of your range.
- **Early January:** secondary spring-semester peak. Real, smaller than August.
- **May → June:** worst time to sell, **best time to buy** — graduating students dump units. Build
  inventory here, hold it, list it in August. The spread between June acquisition and August sale
  prices is one of the few genuinely reliable edges in this business, and it is larger than the
  software premium.
- **October–November, February–April:** thin. Keep listings live, don't add inventory.

The operational implication is that this is a **capital-timing business more than a labour
business**: money made buying in June and selling in August is money made for holding inventory,
not for prepping it.

---

## 9. Pre-publish checklist

Run against every listing before it goes live. This is the claims guide's §8 checklist, adapted for
physical units.

- [ ] Title contains "TI-84 Plus CE Python" and no exam-brand term.
- [ ] No exam-brand terms in tags, keywords, item specifics, or hidden fields.
- [ ] No claim that any program is "approved," "certified," "legal," or "compliant" for any exam.
- [ ] AP claims are about the **calculator's** approval and the **memory rule** only — never about
      program approval.
- [ ] SAT/PSAT/ACT appear only in an explicit *remove the programs* warning.
- [ ] FE/PE/NCEES appear only in an explicit *not permitted* warning.
- [ ] Press-to-Test data-loss warning is in the listing body, above the fold, not only on the card.
- [ ] Non-affiliation footer present in the description.
- [ ] No TI, College Board, or ACT logos; no vendor product photography; own photos only.
- [ ] Photo 3 (File Manager) and photo 5 (About screen) are present — these two do the most work.
- [ ] Every flaw photographed **and** described in words.
- [ ] Variant stated unambiguously as Python Edition, and true.
- [ ] Supported hardware named as the **CE Python family**; no bare "TI-84 family."
- [ ] The TI-84 Evo note and the `[prgm]` Python self-check are in the description (§1).
- [ ] No "Evo" anywhere in the title, tags, keywords, or item specifics.
- [ ] No claim, hedged or otherwise, that the programs work on a TI-84 Evo.
- [ ] Return policy stated.
- [ ] Nothing anywhere sells concealment, evasion, or "beating" an exam.
- [ ] Nothing in the box or on the restore page is TI's software.

---

AP®, Advanced Placement®, SAT®, and CLEP® are trademarks registered by the College Board, which is
not affiliated with, and does not endorse, this product. PSAT/NMSQT® is a registered trademark of
the College Board and the National Merit Scholarship Corporation, which are not affiliated with,
and do not endorse, this product. ACT® is a registered trademark of ACT Education Corp., which is
not affiliated with, and does not endorse, this product. IB® and International Baccalaureate® are
registered trademarks of the International Baccalaureate Organization, which is not affiliated
with, and does not endorse, this product. NCEES® is a registered trademark of the National Council
of Examiners for Engineering and Surveying, which is not affiliated with, and does not endorse,
this product. TI-84 Plus CE Python™, TI-84 Evo™, TI Connect™ CE, TI Connect™ Evo, and Texas
Instruments® are trademarks of Texas Instruments Incorporated, which is not affiliated with, and does
not endorse, this product. All trademarks are the property of their respective owners. Exam policies
are subject to change; verify current policy with the relevant exam authority. Nothing in this
document is legal advice.
