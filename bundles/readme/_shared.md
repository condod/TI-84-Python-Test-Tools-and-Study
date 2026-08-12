# Shared bundle-README blocks

Every block below is injected into each bundle README by `tools/build_bundles.py` at
build time, wherever the matching placeholder comment appears. Nothing in this file
ships as-is; only the blocks do.

Keeping the install guide, the compatibility warning, the Press-to-Test warning, the
exam-policy disclaimer and the trademark footer in **one** file is deliberate. These
paragraphs were previously copy-pasted into every bundle README, and they drifted out
of sync with each other and with the research in `MARKETING_CLAIMS_GUIDE.md`. Edit
them here and every bundle picks the change up on the next build.

The disclaimer text tracks `MARKETING_CLAIMS_GUIDE.md` §5.2, the Press-to-Test warning
tracks §4, and the trademark footer is §6.1 verbatim.

<!-- BLOCK: DOWNLOAD-CONTENTS -->
## What's in This Download

Every program is included **twice**, in two formats. You only need one of them:

```
8xv/   ready-to-install Python AppVars  <- drag these onto TI Connect CE, no conversion needed
py/    the plain-text Python source     <- read it, edit it, or type it in by hand
```

The `.8xv` files are the same programs, already converted into the calculator's native Python
AppVar format. Each one is named after the name it will show up as in the Python App's program
list, so `QUAD.8xv` installs as `QUAD`.

**Which folder you need depends on your calculator.** The `8xv/` folder is for the TI-84 Plus CE
family. The `py/` folder is the portable one: it is what you use on a **TI-84 Evo**, which does not
accept `.8xv` files at all. See the install guide below.
<!-- END BLOCK -->

<!-- BLOCK: COMPATIBILITY -->
## ⚠️ Before You Buy a Calculator — Check for "Python"

**These programs require a TI-84 Plus CE _Python Edition_, or a TI-84 Plus CE that has TI's
Python App installed.** A TI-84 Plus CE without Python cannot run them at all.

This matters more than it used to. Texas Instruments **discontinued the TI-84 Plus CE Python on
2026-04-27**, and the plain TI-84 Plus CE that TI currently sells does **not** include Python.
TI has named the **TI-84 Evo** as the successor model. So a calculator bought new today under
the "TI-84 Plus CE" name may well be a unit that cannot run these programs.

Before you buy hardware:

- Look for the word **"Python"** printed on the calculator's faceplate or bezel.
- Or switch the calculator on and check that a **Python** app appears in the Apps list.
- If you already own a TI-84 Plus CE without Python, check TI's site for the Python App for your
  model and OS version before assuming these will run.

### The three calculators people ask about

**TI-84 Plus CE _Python Edition_ — the model this bundle is built and tested for.** Install the
`8xv/` files with TI Connect™ CE and you are running in a couple of minutes.

**Plain TI-84 Plus CE — only if it has TI's Python App.** Check the Apps list first. If Python is
missing, the programs cannot run until you install TI's Python App for your model and OS version.
New units sold today are the ones to watch out for, per the warning above.

**TI-84 Evo — use the `py/` folder, not `8xv/`.** Every Evo has Python built in, so there is no
"Python Edition" to look for. But the Evo uses a **new AppVar format (`.8xv2`)** and a **different
transfer tool**, so the `.8xv` files in this bundle will **not** transfer to it and TI Connect CE
will not connect to it at all. Send the plain `.py` files through TI's web app at
<https://connectevo.ti.com> instead — it converts `.py` on the fly. Install steps are below.

> **Honest status on the Evo:** every program here is written in plain Python using only `math`,
> `random` and `time`, with the two optional TI-specific imports wrapped in a fallback, and none of
> them depend on the screen size — so we **expect** them to run on an Evo. **We have not yet tested
> them on Evo hardware and cannot promise it.** If you are buying specifically for an Evo, take the
> free starter pack first and confirm on your own calculator before paying for anything.

These programs do **not** run on the TI-83 Plus, the monochrome TI-84 Plus, the TI-84 Plus Silver
Edition, the TI-Nspire family, or any Casio or HP calculator.
<!-- END BLOCK -->

<!-- BLOCK: INSTALL -->
## Installing on Your Calculator

There are two completely separate routes, and which one you need depends on your hardware:

- **TI-84 Plus CE family** (Python Edition, or a plain CE with TI's Python App) — TI Connect™ CE on
  your computer, USB cable, `8xv/` or `py/` files. That is the section immediately below.
- **TI-84 Evo** — TI's web app at <https://connectevo.ti.com> in Chrome, USB-C cable, `py/` files
  only. Skip to *[If you have a TI-84 Evo](#if-you-have-a-ti-84-evo)*.

Don't mix them: TI Connect CE cannot talk to an Evo, and the Evo cannot read `.8xv` files.

### TI-84 Plus CE family (TI Connect™ CE)

First, the part that's the same either way:

1. Download and install **TI Connect™ CE** (free, from Texas Instruments) on your Windows/Mac computer.
2. Connect your TI-84 Plus CE **Python Edition** to your computer with a USB cable.
3. Open TI Connect CE — your calculator should appear in **Calculator Explorer**.

#### Option A — send the ready-made `.8xv` files (fewest steps)

4. Open this bundle's `8xv/` folder, select the files you want (or all of them), and drag them onto
   the Calculator Explorer window — or use **Actions → Send to Calculator**. There's no conversion
   step: these are already Python AppVars.
5. On the calculator, open the **Python App**, pick the program from the list, and select **Run**.

#### Option B — send the `.py` source and let TI Connect CE convert it

4. Do exactly the same thing, but drag the files from the `py/` folder instead. TI Connect CE
   converts each `.py` file into a Python AppVar itself as it sends.
5. Open the **Python App**, pick the program, and select **Run**.

Option B uses TI's own converter, so it's the fallback if anything about Option A doesn't work on
your setup. Both produce the same program on the calculator.

#### Option C — no computer at all

Open the **Python App** on the calculator, create a new program, and type the source in from the
`py/` folder. These are short, plain-text files, so this is slower but perfectly workable.

#### A note on the `.8xv` files

The `.8xv` files were generated with an open-source converter (included in the project repo as
`tools/py_to_8xv.py`) rather than by TI Connect CE itself. Every file is checked byte-for-byte
against the format TI's own software produces, and the converter is validated by reproducing a
TI-generated Python AppVar exactly. If you ever hit a file that won't load, use Option B — the
`.py` source in this bundle is the same program and always works through TI's own converter.

Keep an eye on the ~50 KB / 100-program on-device storage limit; archive or delete programs you're
not actively using to free up space.

### If you have a TI-84 Evo

**Ignore everything above — none of it applies.** TI Connect CE will not connect to an Evo, and the
Evo cannot read the `.8xv` files in this bundle (it uses a newer AppVar format, `.8xv2`). What you
use instead is the `py/` folder and TI's browser-based transfer tool.

You need: a **USB-C cable**, **Google Chrome** (WebUSB is required, so Safari and Firefox will not
work), and an **internet connection** — the Evo tool is a web app, so there is no offline route.

1. Go to <https://connectevo.ti.com> in Chrome. There is nothing to install and no sign-in.
2. Connect the Evo to your computer with a USB-C cable and allow the browser to access it when
   Chrome asks for permission.
3. Choose **Send Files**, and pick the `.py` files you want from this bundle's `py/` folder. TI
   Connect Evo converts each `.py` into the Evo's own Python format as it sends.
4. On the calculator, open **Python**, pick the program, and run it.

If you would rather not use a computer at all, Option C above works on an Evo too — open the Python
app and type a program in from the `py/` source.

**What we can and cannot promise here.** The programs in this bundle use only plain Python plus the
standard `math`, `random` and `time` modules, which TI documents on the Evo, and nothing in them
depends on the screen size or on the CE's key layout. On that basis we **expect** them to run
correctly on an Evo. **They have not been tested on Evo hardware, so that is an expectation and not
a tested claim.** If you hit a problem on an Evo, email and we will sort it out — and try the free
starter pack first if you have not bought yet.

One related warning: any keystroke-by-keystroke instruction or screenshot you find for these
programs, here or elsewhere, was written on a TI-84 Plus CE. The Evo's keypad was substantially
rearranged, so the keys may not be where the instructions say.
<!-- END BLOCK -->

<!-- BLOCK: PRESS-TO-TEST -->
## ⚠️ Back Up Before Press-to-Test — It Deletes These Programs

**Entering Press-to-Test (exam mode) deletes the programs in this bundle. They do not come back.**

TI documents that entering Press-to-Test deletes *"All variables stored in RAM and in archived
memory,"* and TI's Press-to-Test Guidebook states that *"Other variables stored in RAM and in
archived memory (including AppVars) are deleted."* Python programs on the TI-84 Plus CE Python are
stored as Python AppVars. Unlike Apps and TI-BASIC programs — which Press-to-Test only *disables*
and then restores when you exit exam mode — **these are deleted outright and are not restored.**

A full **All-Memory reset** does the same thing, and additionally removes the Python App itself,
which then has to be re-installed with TI Connect™ CE before any of these will run.

**The workaround, which takes about two minutes:**

1. **Before** entering Press-to-Test or resetting memory, connect the calculator and copy this
   bundle's files somewhere safe — your computer, or just keep this ZIP.
2. Enter exam mode and sit your exam with a clean calculator.
3. Afterwards, exit exam mode and re-send the `.8xv` (or `.py`) files exactly as you did when you
   first installed them.

Your download stays available in your account, so you can always re-install from scratch — but
keeping a local copy saves you the trip. Being able to strip the calculator for a proctored exam
and restore it in two minutes is arguably a feature, not a bug.
<!-- END BLOCK -->

<!-- BLOCK: EXAM-POLICY -->
## ⚠️ Exam Policy Disclaimer — Read Before Test Day

**You are responsible for knowing your own exam's calculator rules.** They differ significantly
between exams, and they change. Here is where things stood as of 2026-08-12 — verify current
policy yourself before any exam. **Nothing in this bundle is "approved" for any exam:** no exam
board operates an approval process for third-party calculator software.

**AP® Exams (College Board).** The TI-84 Plus CE Python Edition appears on College Board's list of
approved handheld graphing calculators. College Board's published AP calculator policy states:
*"You don't need to clear your calculators' memories before or after the exam,"* and *"Calculators
with built-in physical constants, metric conversions, and physics, chemistry, or mathematics
formulas are permitted."* College Board approves the *calculator*; it does not approve, review, or
endorse third-party programs. Note also that College Board prohibits using calculator memory to
remove test material from the exam room, and that AP® Calculus and AP® Precalculus both have
sections where no calculator is allowed at all. Confirm current policy with your AP® coordinator:
<https://apstudents.collegeboard.org/exam-policies-guidelines/calculator-policies>

**SAT®, PSAT/NMSQT®, PSAT™ 10, PSAT™ 8/9.** College Board requires you to *"remove programs that
have algebra functionality"* and *"remove any stored documents,"* and the Testing Rules state that
*"Before testing, you will be asked to clear all saved formulas on a calculator you bring."*
**Remove these programs before an SAT® Suite test.**
<https://satsuite.collegeboard.org/sat/what-to-bring-do/calculator-policy>

**ACT® (and ACT® WorkKeys® Applied Math).** ACT requires all documents to be removed, and permits
only single-purpose math programs of **25 logical lines or fewer**. Most programs in this bundle
exceed that. ACT also states that putting the calculator in Press-to-Test mode is *not* sufficient
— the programs must actually be removed. **Remove these programs before the ACT®.**
<https://www.act.org/content/act/en/products-and-services/the-act/test-day/calculator-policy.html>

**NCEES® FE / PE / FS / PS exams.** The TI-84 is **prohibited outright** — not because of what is
stored on it, but because the model itself is not permitted. NCEES allows only Casio fx-115 and
fx-991 models, HP 33s and HP 35s, and Texas Instruments models whose name contains "TI-30X" or
"TI-36X". If you are sitting the FE or PE, use a TI-36X Pro or a Casio fx-991 — these programs
cannot be used there in any form. <https://ncees.org/exams/>

**IB® Diploma Programme.** The TI-84 Plus CE Python is a permitted non-CAS device, but IB requires
that third-party programs and stored notes be removed (via reset) or blocked (via examination
mode), and schools must clear calculator memories. **Remove or block these programs for IB® exams.**

**CLEP®.** You may not bring your own calculator at all; CLEP provides an on-screen TI-84 Plus CE
for its Calculus and Precalculus exams.

**University and course exams.** Your instructor or department sets the rules. Many require a
memory clear or TI's Press-to-Test mode. **Ask before test day.**

### These are study tools

This bundle is intended for homework, practice problems, self-review, and practice exams. It is
**not** intended to help with, and must not be used to facilitate, cheating or academic misconduct
on any exam. `formula_flashcards.py`, where included, is a self-quiz recall drill, not an
answer-lookup tool. Where a program's presence would break your exam's rules, delete it or use
exam mode — and back it up first, as described above.
<!-- END BLOCK -->

<!-- BLOCK: TRADEMARK -->
---

AP®, Advanced Placement®, SAT®, PSAT™, and CLEP® are trademarks registered by the College Board,
which is not affiliated with, and does not endorse, this product. PSAT/NMSQT® is a registered
trademark of the College Board and the National Merit Scholarship Corporation, which are not
affiliated with, and do not endorse, this product. ACT® and WorkKeys® are registered trademarks of
ACT Education Corp., which is not affiliated with, and does not endorse, this product. IB® and
International Baccalaureate® are registered trademarks of the International Baccalaureate
Organization, which is not affiliated with, and does not endorse, this product. NCEES® is a
registered trademark of the National Council of Examiners for Engineering and Surveying, which is
not affiliated with, and does not endorse, this product. TI-84 Plus CE Python™, TI Connect™ CE,
and Texas Instruments® are trademarks of Texas Instruments Incorporated, which is not affiliated
with, and does not endorse, this product. TI-84 Evo™ and TI Connect™ Evo are likewise trademarks of
Texas Instruments Incorporated, which is not affiliated with, and does not endorse, this product.
All trademarks are the property of their respective owners. Exam policies are subject to change; verify current policy with the relevant exam
authority.
<!-- END BLOCK -->
