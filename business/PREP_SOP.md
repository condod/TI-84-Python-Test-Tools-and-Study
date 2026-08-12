# Prep SOP — Acquired Unit → Sellable Unit

**Standard operating procedure for the pre-loaded TI-84 Plus CE Python resale line.**

This maps onto the five checklist steps tracked per unit in the inventory app:
**wiped → OS updated → Press-to-Test cleared → programs loaded → device verified.**

> **Scope: this SOP is for TI-84 Plus CE Python hardware, and every procedure in it assumes
> TI Connect™ CE over a Mini-B cable.** That is correct for the units this business actually buys and
> resells. It is **wrong for a TI-84 Evo**, which uses a browser-based tool over USB-C and a different
> file format — TI Connect CE will not connect to an Evo at all. If an Evo enters inventory, read
> **§1.1** first. See [`EVO_TRANSITION.md`](EVO_TRANSITION.md) for the full evidence.

> **The single most important thing in this document:** the five steps are in that order for a
> reason, and **programs are loaded LAST**. Every step before "programs loaded" destroys Python
> AppVars. Load first and you will ship an empty calculator. See §0.

Sources for every calculator procedure below are TI's own documentation, cited inline. Time
estimates are marked **[ESTIMATE]** — they are my own modelling, not measured, and you should
replace them with your real stopwatch numbers after your first ten units.

---

## 0. The ordering constraint — read before anything else

Three separate operations wipe Python programs. All three happen during refurb. All three must
happen **before** the programs go on.

| Operation | What it does to Python AppVars | Source |
|---|---|---|
| **Reset → ALL → All Memory** | Deletes them. Also deletes the **Python App itself** (it is a Flash App) and every other user-installed app. | TI Exam Prep Guide / KB 34871: "All Memory — Clears everything from RAM and Archive, leaving only the Calculator OS and its components." |
| **Entering Press-to-Test** | Deletes them. They do **not** come back on exit. | TI Press-to-Test Guidebook: "Other variables stored in RAM and in archived memory (including AppVars) are deleted." |
| **Sending an OS / OS+Apps bundle** | RAM is reset by the transfer. | TI KB 37042: "back up any calculator files you wish to save as 'RAM' is reset after the calculator is updated" |

So the fixed order is:

```
1. WIPE            (Reset > ALL > All Memory)          <- destroys AppVars AND the Python App
2. EXAM MODE CLEAR (confirm not in Press-to-Test)      <- destroys AppVars
3. OS + APPS       (Send OS/Bundle to Calculators...)  <- resets RAM; restores the Python App
4. PROGRAMS        (send .8xv / .py)                   <- the payload
5. VERIFY          (launch each program on-device)     <- proves 1-4 worked
```

**Never** run steps 1–3 after step 4. In particular, **never demo Press-to-Test on a finished
unit** to "prove it's clean" — that erases the product you just built. If you want a
press-to-test-clean photo for the listing, take it during step 2.

There is one non-obvious trap inside this: **an All-Memory reset removes the Python App.** The
Python App on the TI-84 Plus CE Python is a Flash application, and TI's own documentation says an
All-Memory reset leaves "only the Calculator OS and its components." A unit that has been wiped
but not re-bundled will boot, look completely normal, and have no Python. Step 3 (sending the
**OS *and* Apps bundle**, not the bare OS file) is what puts it back. Do not skip it, and do not
substitute the OS-only download for the bundle.

---

## 0.1 Which units are even candidates

**Only the TI-84 Plus CE Python can run this product.** The plain TI-84 Plus CE cannot be
upgraded to Python — the Python interpreter runs on a physically separate ARM coprocessor
(an Atmel ATSAMD21E18A) that plain CE units do not have. TI states it plainly: *"Only the Python
version of the TI-84 Plus CE graphing calculator has Python programming capability."*
(<https://education.ti.com/en-au/products/calculators/graphing-calculators/ti-84-plus-ce-python/product-support>,
accessed 2026-08-12.)

Practical consequence for this SOP: a plain CE that lands in your inventory goes through steps
1–3 and 5 only, and is sold **bare**. It is not a candidate for the loaded SKU at any price. See
[`SOURCING.md`](SOURCING.md) §3 for how to tell them apart before you buy.

---

## 1. Bench setup (one-time)

| Item | Notes |
|---|---|
| Windows or Mac computer with **TI Connect™ CE** (6.0.3, 2025-03-26) | Free from TI. Install **before** first connecting a calculator so drivers are in place. |
| 2–4 × USB **Standard-A to Mini-B** cables | The CE family uses a **Mini-B** port, not micro-USB and not USB-C. TI's spec sheet: "Standard A to Mini-B USB cable included." Cheap generic mini-B cables work for data + charge. |
| Powered USB hub or multi-port wall charger | You will be charging 4–10 units at once. Charging from a laptop port is slow and laptop sleep kills the charge. |
| Current **TI-84 Plus CE OS and Apps Bundle** (`.b84`), downloaded once from TI | Latest as of research date: **5.8.5 (April 2026)**; TI's US download page still listed 5.8.4 (2025-09-02) at time of writing. **5.8.5 is probably the last CE release there will ever be — see the note below.** |
| Local folder with your `8xv/` payloads, organised by loadout | See [`LOADOUT_STRATEGY.md`](LOADOUT_STRATEGY.md). |
| 70–91% isopropyl alcohol, microfibre cloths, cotton swabs, plastic spudger, soft brush | |
| Small Phillips #00 driver | Back cover / battery access |
| Spare batteries (TI part **3.7L1200SPB**, 3.7 V 1200 mAh) | Buy in 10-packs. |
| Spare slide cases and mini-B cables | The two most commonly missing accessories. |
| Camera / phone on a small light tent | Same background and framing every time — see [`LISTING_AND_SUPPORT.md`](LISTING_AND_SUPPORT.md) §2. |

### Archive the `.b84` bundle locally, and relax the per-batch version check

The CE Python is discontinued, and TI's Evo-T product sheet marks **"Continued OS support" as an Evo
feature while leaving it blank for the CE-T Python Edition**
(<https://justmore.dk/images/media/ProductsDocs/TI10014_PRODUCTSHEET.pdf>). **[INFERRED, not
announced]** CE OS development has ended and **5.8.5 is the effective terminal release.**

Two practical changes follow:

- **"Verify at education.ti.com before each batch" can relax to a periodic check** — quarterly is
  plenty. A new CE OS is unlikely to appear, and re-checking before every batch is wasted bench time.
- **Keep your own archived copy of the `.b84` bundle**, because TI's CE download pages may eventually
  be retired and you would then have no way to restore the Python App on a wiped unit (§0). TI's
  licence explicitly permits **one backup copy on your computer** — see the rule below. Store it with
  the version number in the filename. Do **not** confuse this with redistribution: the archive lives on
  your bench and never ships.

It also means "updated to the latest TI operating system" is likely to stay true indefinitely rather
than being a perishable claim — but the end of CE OS support has been **inferred, not announced**, so
don't yet advertise 5.8.5 as "final." See [`LISTING_AND_SUPPORT.md`](LISTING_AND_SUPPORT.md) §1 for the
wording and the trigger for changing it.

### The OS licence rule — non-negotiable

TI's OS licence lets you **copy and use the OS on a TI calculator** and keep **one backup copy on
your computer**, and states: *"You may not sell, rent or lease copies of the Licensed Materials."*
(<https://education.ti.com/en/customer-support/end-user-license-agreement-for-os>, accessed
2026-08-12.)

**Operating rule:** you may download TI's OS/Apps bundle and flash it onto a calculator you own
and are servicing. You may **not** put TI's OS file, TI's apps, or TI's guidebook PDFs on a USB
stick in the box, host them on your own site, or include them in any download link you give a
buyer. **The only software you ever distribute is your own.** If a buyer needs the OS, you link
them to TI's own download page. This is expanded in
[`LISTING_AND_SUPPORT.md`](LISTING_AND_SUPPORT.md) §5.

---

## 1.1 If a TI-84 Evo enters inventory — a separate, non-overlapping toolchain

Nothing in the rest of this SOP applies to an Evo unit. **Do not try to unify the two flows**;
document and run them separately. All of the following is [RESEARCHED] from TI and TI-Planet unless
marked otherwise — sources in [`EVO_TRANSITION.md`](EVO_TRANSITION.md) Q2 and Q3.

| | CE Python (this SOP) | TI-84 Evo |
|---|---|---|
| Transfer software | **TI Connect™ CE** desktop app | **TI Connect™ Evo**, a web app at **`connectevo.ti.com`** — no install, no sign-in |
| Cable | USB Standard-A to **Mini-B** | **USB-C** (box includes USB-C to USB-A; a C-to-C cable is needed for a USB-C-only computer) |
| Python payload | `.8xv` AppVars, or `.py` converted on send | **`.py` only** — the Evo's Python AppVar extension is **`.8xv2`** and our `.8xv` files are rejected outright |
| Requirements | Local install, works offline | **Active internet connection and WebUSB.** Windows 11 64-bit, macOS 15/26, or ChromeOS 143+ |
| Browser | n/a | **Chrome.** TI-Planet found only Chrome worked in their tests; WebUSB is unsupported in Safari and Firefox. **[UNVERIFIED]** whether Edge works, though as Chromium it likely does |
| Functions available | Full explorer, OS/bundle send, batch exam-mode exit | Capture Screen, Send Files, Install OS, Exit Test Mode |

**The three consequences that actually change how you'd work:**

1. **Send `.py`, never `.8xv`.** TI Connect Evo auto-converts `.py` files on send and builds the
   `.8xv2` itself. This is the whole reason no new converter is needed — **do not** build an `.8xv2`
   writer or try to reverse-engineer the format; TI-Toolkit, who are best equipped to, have not
   documented it. The `8xv/` folder is a CE-only artifact.
2. **The offline prep bench stops working.** The CE flow runs entirely local; **every Evo unit you
   flash needs live internet and a Chrome session.** For volume work that is a real operational
   regression and it is the least obvious consequence of the transition. Budget for it before
   committing to any Evo batch.
3. **[UNVERIFIED] Bulk-loading ergonomics are unknown.** The documented Evo flow is a file-picker
   "SEND TO CALCULATOR." Whether multi-selecting ~52 files is practical at volume has not been tested
   by anyone. **Make it an explicit test item on the first unit** — it is the single biggest unknown
   for a pre-loaded-hardware business on this platform.

**Also invalidated for an Evo unit, and easy to miss:** every keystroke sequence and screenshot in
this document. The Evo's keypad was substantially remapped — the arithmetic keys all shifted up a row,
`[apps]` was replaced by a fraction template, `matrix` moved, and `[x^-1]` became `[x^n]`. And the
mini-B cable stock in the prep kit is CE-only.

**Current policy: do not stock Evo units** ([`SOURCING.md`](SOURCING.md) §5). This section exists so
that if one arrives inside a lot — or once the R&D unit is on the bench — nobody follows a CE
procedure and concludes the calculator is broken.

---

## 2. Step 0 — Intake and triage (before the five checklist steps)

**Target: 4 minutes/unit. [ESTIMATE]**

1. Assign the unit an internal ID and open a record in the inventory app. Record acquisition
   cost, source channel, and date.
2. **Photograph the unit exactly as received**, all six faces, before you clean anything. This is
   your evidence if a lot arrives worse than described and you need a partial refund from the
   seller.
3. Record the **serial number** (back of unit, and via `[2nd]` `[MEM]` `1:About`). The app tracks
   this per unit. It is your warranty/dispute anchor and your defence against "this isn't the one
   you sent me" claims.
4. **Confirm variant.** Faceplate reads "TI-84 Plus CE **PYTHON**" on Python units. Cross-check
   on-device: `[2nd]` `[MEM]` `1:About` shows the model name, and the Python App appears in
   `[apps]`. Record variant in the app. If it's a plain CE, reroute to the bare-resale flow.
5. **Reject/part-out screen.** Do not spend labour on a unit that fails any of these:
   - Cracked or delaminated LCD, dead columns/rows, or a pressure bruise larger than a fingernail.
   - Mini-B port physically loose, bent, or not retaining a cable.
   - Any sign of liquid ingress (corrosion crust around the port, discoloured PCB visible through
     the battery bay, tide-line stains under the screen).
   - Swollen battery **bulging the back cover** — the cell is replaceable, but a swell that has
     deformed the housing usually means the housing is done too.
   - School asset engraving that cannot be removed without visible damage — see
     [`SOURCING.md`](SOURCING.md) §6.
6. **Battery and charge check.** Plug in. Confirm the charge LED behaves, then leave the unit on
   the hub. Full first charge from flat is 4–6 hours per TI's own charging FAQ; plan an overnight
   soak for a batch. Next morning, unplug and check `[2nd]` `[MEM]` `1:About` / the battery icon
   after ~30 minutes of screen-on idle. A unit that drops from full to under ~75% in an hour of
   idle gets a new **3.7L1200SPB** cell.

Grade cosmetically now (see §8) and record it. Everything after this is the five tracked steps.

---

## 3. Checklist step 1 — WIPED

**Target: 3 minutes/unit. [ESTIMATE]**

Purpose: remove the previous owner's data completely, and start from a known state.

1. If the unit is **currently in Press-to-Test** (a banner/indicator is showing, or files display
   with the "not equal" sign in Mem Management), do §4 **first**, then come back. You cannot
   meaningfully assess memory contents through exam mode.
2. Before wiping, spend 30 seconds looking at what's on it. Occasionally a used unit carries
   somebody's personal notes, contact details, or photos as Pic/Image vars. You are about to
   delete them, which is correct — but note in the record that the unit came with prior-owner
   data, because a unit stuffed with a school's programs is a signal about provenance
   ([`SOURCING.md`](SOURCING.md) §6).
3. Perform the full reset, per TI's Exam Prep Guide:

   ```
   [2nd] [MEM]  ->  7:Reset  ->  [>] [>]  (ALL tab)  ->  1:All Memory  ->  2:Reset
   ```

   The screen confirms **`Mem cleared`** (some OS versions display `MEM Cleared`). Anything else
   means it didn't take — repeat.

4. Expect the calculator to now be missing every app, including the **Python App**. That is
   correct and expected at this stage. TI: resetting all memory *"permanently deletes all
   user-installed applications from the calculator."* Step 3 restores them.
5. Tick **wiped** in the app.

> **Do not** use `1:All RAM` here. It leaves archived AppVars and apps in place, which means the
> previous owner's archived Python programs survive. You want the ALL tab.

---

## 4. Checklist step 2 in the app is *OS updated*; do exam-mode clearing around it

The app's checklist stores these as "OS updated" then "Press-to-Test cleared." Operationally you
touch exam mode twice: once **before** the OS flash if the unit arrived in exam mode, and once
**after** the OS flash as a verification pass. Both are before programs load, so the app's order
is safe as written. Do not reorder the checkboxes.

### 4a. Clear exam mode if the unit arrived in it

**Target: 2 minutes/unit. [ESTIMATE]**

Bought-used units from schools frequently arrive in Press-to-Test. Two documented ways out:

- **TI Connect CE → Actions → Quit Exam Mode on Connected CE Calculators.** Preferred; it's a
  single click for the whole connected batch.
- **Send any file to the unit from another CE calculator over a unit-to-unit cable.** Fallback if
  you're away from the bench.

Confirm exit: the exam-mode indicator is gone and `[2nd]` `[MEM]` `Mem Management` shows no files
flagged with the "not equal" sign.

### 4b. Checklist step 2 — OS UPDATED

**Target: 6 minutes/unit active, ~4 minutes of that unattended. [ESTIMATE]** Batch 4 units at a
time and this collapses to ~2 minutes each.

1. Check current version: `[2nd]` `[MEM]` → `1:About`. Record the **before** version in the app.
2. Connect over mini-B, confirm the unit appears in TI Connect CE's **Connected Calculators**
   panel.
3. **Actions → Send OS/Bundle to Calculators…** → select the **`.b84` OS *and Apps* bundle** →
   **Send**.
4. Do not disconnect during transfer. The unit will show `RAM Cleared` afterwards; that's normal.
5. Re-check `1:About` and record the **after** version (target: the current TI release — 5.8.5 as
   of April 2026). Record it in the app's `osVersion` field.
6. Confirm the **Python App is back**: press `[apps]`, find `Python`, launch it, confirm the Shell
   opens. If the Python App is missing, you flashed the OS-only file instead of the bundle — get
   the bundle and redo.

**Why update at all?** Three reasons, all of which show up in listings: it standardises every unit
you ship so support is one script instead of many; it guarantees the current Python App and the
current module set; and "updated to the latest TI operating system" is a real, checkable,
zero-cost differentiator against every other used-calculator listing on the platform.

**One exception — check the "before" version before you flash.** Units still running **OS 5.5 or
older** retain the ASM/C program capability TI removed in 5.6, and are specifically sought by the
calculator homebrew and gaming community. Those units can be worth **more left alone** than
updated, sold as-is to that audience with the OS version stated prominently in the title. Updating
is irreversible in practice — TI does not support downgrading. **So: read `1:About` first, and if it
says 5.5 or lower, stop and decide deliberately.** This is rare, but it's a genuine one-way door and
it costs nothing to check. [RESEARCHED]

### 4b-i. If a unit soft-bricks during an OS transfer

An interrupted OS send can leave a unit apparently dead — blank screen, no response to `[on]`. **This
is usually recoverable and the unit is usually not scrap.**

1. Remove the battery for ~30 seconds, reinsert, and press `[on]`.
2. If still unresponsive, press the **RESET** button in the pinhole on the back with a paperclip.
3. If the screen shows a "Waiting… Please install operating system now" prompt or stays blank, hold
   `[2nd]` + `[del]` while pressing **RESET** to force the boot-code recovery mode, then push the OS
   bundle again from TI Connect CE.
4. Only after all three fail should you grade the unit as parts.

Do this before writing anything off — a unit that looks bricked mid-flash is a fifteen-minute
recovery far more often than it is a loss. [RESEARCHED]

### 4c. Checklist step 3 — PRESS-TO-TEST CLEARED

**Target: 2 minutes/unit. [ESTIMATE]**

Purpose: prove, on this specific unit, that it is not in exam mode and will not surprise the
buyer, **and** capture the evidence photo now while it is free to do so.

1. Confirm no exam-mode indicator on the home screen.
2. `[2nd]` `[MEM]` → `2:Mem Management/Delete…` → skim the list. No file should show the "not
   equal" sign (TI's documented marker for exam-mode-disabled files).
3. If you want an "exam mode works on this unit" test — and on a unit with an unknown history it
   is worth doing once — **do it now, in this step, with nothing loaded**: enter Press-to-Test,
   confirm the banner appears, then exit via TI Connect CE. It costs you nothing at this point
   because the programs aren't on yet.
4. Take the listing photo of the clean home screen now.
5. Tick **Press-to-Test cleared**.

> **After this step, exam mode is off-limits for the rest of the unit's life in your hands.**
> Entering it in step 5 or 6 silently destroys the payload and the unit will ship empty. If you
> ever need to re-enter exam mode on a finished unit, you must redo §5 and §6 afterwards.

---

## 5. Checklist step 4 — PROGRAMS LOADED

**Target: 5 minutes/unit. [ESTIMATE]**

1. Pick the loadout SKU for this unit from [`LOADOUT_STRATEGY.md`](LOADOUT_STRATEGY.md) and record
   it in the app's bundle field.
2. Open TI Connect CE → **Calculator Explorer**.
3. Drag the loadout's files onto the connected calculator.
   - **Destination: RAM**, not Archive. TI: *"The Python App will only edit and run Python AppVars
     in RAM."* An archived AppVar does not appear in the Python App's File Manager and cannot be
     run until the student moves it back — which is a support ticket you don't want. Ship
     everything RAM-resident.
   - Confirm each file lands and the names are what you expect (e.g. `QUAD.8xv` installs as
     `QUAD`). The on-calculator names were shortened in the 2026-08-12 AppVar regeneration, so check
     the current list in [`LOADOUT_STRATEGY.md`](LOADOUT_STRATEGY.md) §2 rather than working from
     memory.
4. Confirm you are under budget: `[2nd]` `[MEM]` → `2:Mem Management` and, more importantly, the
   Python App's own memory behaviour. TI's documented ceiling is *"a maximum of 100 Python
   programs (PY AppVars) or 50K of memory,"* shared with the bundled modules. Every loadout in
   `LOADOUT_STRATEGY.md` is sized to sit at or under ~34 KB so the student has real working room.
5. Tick **programs loaded**.

### `.8xv` vs `.py` — send `.py` by default

The repo ships both. **Default: send the `.py` files and let TI Connect CE do the conversion.** There
are now two independent reasons, and the second one is new:

1. **It's the validated path.** The repo's own README states the `.8xv` AppVars are generated by this
   project's converter, not by TI's software, and **"have not been tested on physical hardware."**
   Letting TI's software build the AppVar removes our converter from the trust chain entirely.
2. **It's the forward-compatible path.** TI Connect Evo also auto-converts `.py` on send, so `.py` is
   the one payload format that works on both platforms. The `.8xv` files are a CE-only convenience
   layer — the Evo's Python AppVar extension is `.8xv2` and will not accept them
   ([`EVO_TRANSITION.md`](EVO_TRANSITION.md) Q2, §1.1 above). **`.py` is the durable asset; treat it as
   the product and `.8xv` as a shortcut.**

You now have physical hardware, so still run the validation the repo has been missing — the result is
worth feeding back to `bundles/FILE_FORMAT_NOTES.md` either way:

1. On unit #1, send **one** `.8xv` and one `.py`. Open both in the Python App. Confirm both appear
   in File Manager, both open in the Editor with correct source, and both run.
2. If the `.8xv` behaves identically, you may switch to `.8xv` for CE units where the extra speed and
   the deterministic on-calc name are worth it. Record that hardware validation happened.
3. If it doesn't, stay on `.py` permanently. It costs a few extra seconds per unit and nothing else.

Either way, **never ship a unit whose programs you have not personally launched** (§6).

---

## 6. Checklist step 5 — DEVICE VERIFIED

**Target: 8 minutes/unit. [ESTIMATE]** This is the longest step and the one most tempting to skip.
Don't. A dead program on a "pre-loaded" calculator is a guaranteed return plus a negative review,
and it costs more than the whole unit's margin.

### 6a. Program verification

For **every** program in the loadout:

1. Launch it from the Python App Shell.
2. Enter one known-answer input. Keep a printed card of one canonical input/output per program at
   the bench so this is a glance, not a calculation. Examples:
   - `QUAD`: a=1, b=-3, c=2 → roots 2 and 1.
   - `STATS`: 1,2,3,4,5 → mean 3, sample sd ≈ 1.5811.
   - `SUVAT`: v0=0, a=9.81, t=2, solve d → 19.62.
   - `UNITS`: 1 inch → 2.54 cm.
   - `OHMS`: V=12, R=4 → I=3, P=36.
3. Exit cleanly back to the Shell.

Anything that errors, hangs, or returns a wrong number: pull the unit from the line, don't ship.

### 6b. Hardware verification

- **Screen:** run a full-screen colour test (the Python Shell filled with text is adequate; a
  `ti_plotlib` sketch from `PROJ` is better) and check for dead pixels and backlight
  uniformity at max brightness.
- **Every key:** press all 50 keys and confirm each registers. A sticky `[ENTER]` or a dead `[2nd]`
  is a return.
- **Charge port:** wiggle-test a connected cable; the charge indicator must not flicker.
- **Battery hold:** the unit should be at/near full and hold it overnight on the shelf. Re-check
  the morning of shipping.
- **Reset resilience:** power-cycle. Confirm the loadout is still present in the Python App File
  Manager.

### 6c. Record

Tick **device verified** in the app, record the cosmetic grade, and record the final photo set.

---

## 7. Battery replacement (as needed)

**Target: 10 minutes/unit. [ESTIMATE]** Only when §2.6 flagged it.

1. Power off. Remove the slide case and the back cover screw(s), lift the battery door.
2. Disconnect the existing cell's connector with a plastic spudger — do not pull on the wires.
3. Fit a new **3.7L1200SPB** (3.7 V, 1200 mAh Li-ion). `3.7L1200SPA` is the older revision of the
   same part and is generally treated as compatible; buy the SPB.
4. Reassemble, charge to full, then run the §2.6 hold test again before the unit re-enters the
   line.
5. Dispose of the old cell at a battery recycling point. Do **not** ship a swollen cell, and do not
   put lithium cells in household waste.
6. Record the replacement in the unit's notes. "New battery installed" is a legitimate and valuable
   listing claim, and it's one of the few things that genuinely moves price on a used calculator.

---

## 8. Cleaning and cosmetic grading

**Target: 6 minutes/unit. [ESTIMATE]**

### Cleaning

1. Soft brush the keypad seams and the port; blow out grit before any liquid.
2. Microfibre + 70% IPA on the case, sparingly. Cotton swab around the key edges.
3. **Screen:** IPA on the cloth, never sprayed on the screen, never pooled at the bezel.
4. Adhesive residue (name labels, tape) — IPA and patience, or a plastic razor at a shallow angle.
   Do not use acetone; it hazes the plastic.
5. Clean the slide case separately; they are usually filthier than the calculator.
6. Let everything dry fully before the unit goes back on charge.

### Grading scale (use these exact words in listings so grades stay consistent)

| Grade | Definition | Typical price position |
|---|---|---|
| **A — Like new** | No visible wear at conversational distance. Screen flawless. Keys crisp. Case unmarked. Original slide case present and clean. | Top of your range |
| **B — Very good** | Light surface scuffs on the back or case only. Screen flawless. Keys crisp. | Median |
| **C — Good** | Visible scuffs/scratches on the case, possible faint screen scuffs that do not affect readability, keypad lettering intact. Fully functional. | Below median; state every flaw with a photo |
| **D — Functional / rough** | Heavy cosmetic wear, worn key legends, marker/label residue, or a missing slide case. Fully functional. | Bare unit only — do **not** load software onto a D. |

**Rule: never sell a loaded SKU below grade C.** The software premium depends entirely on the unit
reading as "prepared, checked, cared for." A scuffed unit with a $40 software story on it looks
like a scam and attracts the exact buyer who opens a return case.

---

## 9. What goes in the box

| Item | Include? | Notes |
|---|---|---|
| The calculator | Yes | Fully charged. |
| Slide/hard case | Yes, if present | Source spares; a missing case is a real value hit and cheap to fix. |
| USB Standard-A to Mini-B cable | Yes — a **new generic** one | Do not ship a filthy used cable. This is a ~$1–2 line item that removes an entire class of "it won't charge" tickets. |
| TI wall adapter | Only if it came with one | Never ship a random third-party wall wart; TI voids warranty on non-approved adapters and a bad one can damage a unit. USB-cable charging from the buyer's existing phone charger is fine and is what you should tell them to do. |
| **Your** printed quick-start card | Yes | One card, both sides. Content in [`LISTING_AND_SUPPORT.md`](LISTING_AND_SUPPORT.md) §4. Must include the Press-to-Test warning and the restore instructions. |
| Restore/download card with a link to **your** programs | Yes | See §5 of the listing doc for the recommended mechanism. |
| **TI's OS file, TI's apps, or TI's manuals** | **NO — never** | Licence prohibits distributing copies. Link buyers to education.ti.com instead. |
| Original TI retail box | Only if it came with one | Don't fake one. |
| Packaging | **#1 (7.25×12) bubble mailer with a cut-cardboard stiffener behind the calculator** | See the weight note below — this is a real money decision, not just a packing preference. |

### Weigh the finished parcel, and keep it under 12 oz

A bare CE is **0.44 lb**. Packed as above — calculator, case, cable, cards, mailer, stiffener — you
should land at **9–12 oz**. In a 9×5×3 box you land at 12–15 oz and risk crossing **1 lb**, which is
a real price break on USPS Ground Advantage.

**The stiffener is what makes the mailer safe.** A calculator in a bare poly mailer will eventually
arrive with a cracked screen; a calculator sandwiched between the mailer's bubble layer and a piece
of corrugated cut to the calculator's footprint will not. The stiffener costs nothing (cut it from
inbound boxes) and it is the difference between this being a cost saving and being a false economy.

**Put a scale on the bench and weigh every parcel.** On Mercari especially, rates round *up* to the
tier ceiling — a 12.1 oz package pays the 1 lb price. The economics are in
[`UNIT_ECONOMICS.md`](UNIT_ECONOMICS.md) §4.

---

## 10. Time and labour summary

| Step | Minutes/unit (single) | Minutes/unit (batch of 6) |
|---|---|---|
| Intake, triage, serial, photos-as-received | 4 | 3 |
| Wipe | 3 | 2 |
| Exam-mode clear (if needed, ~30% of units) | 2 | 1 |
| OS + Apps bundle | 6 | 2 |
| Press-to-Test verify + clean-screen photo | 2 | 2 |
| Load programs | 5 | 4 |
| Verify programs + hardware | 8 | 8 |
| Clean and grade | 6 | 5 |
| Battery swap (~20% of units) | 10 | 10 |
| Listing photos (final set) | 6 | 4 |
| Write/clone listing, publish | 5 | 3 |
| Pack and label | 5 | 4 |
| **Weighted total** | **~50 min** | **~38 min** |

**[ESTIMATE]** — all of it. Weighted total includes the exam-clear step at 30% incidence and the
battery swap at 20% incidence.

Batching is where the money is: OS flashing, charging, and photography all parallelise, program
verification does not. **~38 minutes per unit at a batch of six** is the number carried into
[`UNIT_ECONOMICS.md`](UNIT_ECONOMICS.md). If you can't hit it, the economics in that document get
worse fast — it is the single most sensitive input in the model.

---

## 11. Quick reference card (print for the bench)

```
CANDIDATE?      Faceplate must read "TI-84 Plus CE PYTHON". Plain CE = bare resale only.
                A TI-84 EVO IS NOT A CANDIDATE. Nothing below applies to it -> see SOP 1.1
                (connectevo.ti.com in Chrome, USB-C, .py only - TI Connect CE will not connect)

1  WIPE         [2nd][MEM] 7:Reset  [>][>]  1:All Memory  2:Reset    -> "Mem cleared"
                (this also deletes the Python App - expected)

2a EXAM MODE    If it arrived in Press-to-Test:
                TI Connect CE > Actions > Quit Exam Mode on Connected CE Calculators

2b OS+APPS      TI Connect CE > Actions > Send OS/Bundle to Calculators... > *.b84 > Send
                Verify [2nd][MEM] 1:About  AND  [apps] > Python opens

3  P2T CLEAR    No exam banner. Mem Management shows no "not equal" flags. Photo now.
                *** LAST MOMENT EXAM MODE IS SAFE ***

4  PROGRAMS     TI Connect CE > Calculator Explorer > drag loadout > destination RAM
                Send the .py files (TI Connect CE converts) - .py works on CE AND Evo

5  VERIFY       Launch EVERY program, one known-answer input each.
                All keys. Screen. Charge port. Battery hold overnight.

NEVER: enter Press-to-Test after step 3.  NEVER: ship TI's OS or apps in the box.
```
