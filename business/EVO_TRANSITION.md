# TI-84 Evo Transition: Research Findings and Strategy

**Research date:** 2026-08-12
**Scope:** What the April 2026 TI-84 Evo launch and the TI-84 Plus CE Python discontinuation mean for this 52-program library.
**Status:** Research pass. Every finding below is tagged **VERIFIED** (primary or recognized-expert source, URL cited), **UNVERIFIED** (single/weak source), or **INFERRED** (my reasoning from verified facts).

---

## Executive summary (read this first)

**The CE Python market is fine for several years. Do not panic. Do not rewrite the library.**

Three findings drive that conclusion:

1. **The Evo runs Python with what appears to be the same module set** (`math`, `random`, `time`, `ti_system`, `ti_plotlib`, `ti_hub`, `ti_rover`), now natively on an ARM CPU instead of the CE Python's separate CircuitPython coprocessor. Faster, more memory, same API surface as far as expert testers can tell.
2. **The `.8xp2` report is TRUE and confirmed by TI itself** — and the corresponding AppVar extension is **`.8xv2`**, so the repo's `.8xv` files are *not* Evo-compatible. **But this barely matters**, because TI Connect Evo (the new web-based transfer tool) **auto-converts plain `.py` files to Evo format on send**. The repo already ships `.py` source for every program. The portable asset was always the `.py`.
3. **TI Connect CE does *not* work with the Evo.** The Evo uses a browser-based tool at `connectevo.ti.com` over WebUSB, with a USB-C cable. Any install instructions that say "TI Connect CE" are correct for CE hardware and wrong for Evo hardware.

Net: the CE Python installed base is millions of units with 5 years of production behind it and a normal 4-8 year student device life ahead of it. That is a **stable-to-slowly-shrinking market through roughly 2030-2031**, not a cliff. Meanwhile the Evo Python program archives are **nearly empty** — one hobby game — so there is a real, cheap first-mover window that costs a `.py`-only bundle variant, not a rewrite.

---

## Q1. Does the TI-84 Evo run Python, and in what environment?

### It runs Python. VERIFIED.

> "We've confirmed that the Evo does have both Python and TI-BASIC programmability, like the TI-84 Plus CE Python Edition before it... we are confident that no user C programmability or assembly programmability is included."
> — Cemetech news, "TI-84 Evo Calculator Released," 2026-04
> https://www.cemetech.net/news/2026/4/1062/_/ti-84-evo-calculator-released-fast-graphing-new-ui-new-hardware

TI's own product sheet for the Evo-T lists "Python programming" as present on the Evo-T, same as the CE-T Python Edition it replaces:
https://justmore.dk/images/media/ProductsDocs/TI10014_PRODUCTSHEET.pdf (TI product sheet, "Introducing TI-84 Evo-T")

TI Connect Evo's own marketing page lists "Python programs" among the file types you send to the calculator — direct confirmation from TI that Python programs are a first-class Evo file type:
https://education.ti.com/en-au/products/calculators/graphing-calculators/ti-84-evo/ti-connect-evo

**Important commercial note (VERIFIED):** Python is on **every** Evo unit. There is no separate "Evo Python Edition." Per the CE-vs-Evo comparison, "TI-BASIC and Python programming are built into all Evo units (no separate Python edition needed)."
https://ti84evo.com/ti-84-plus-ce-vs-ti-84-evo-a-complete-comparison-2026/
This is the opposite of the current CE situation, where TI now sells plain CE units *without* Python. It means the Evo installed base is 100% Python-capable — a *larger* addressable fraction than the CE line ever had.

### Native on the new processor, not a coprocessor. VERIFIED (hardware) / UNVERIFIED (exact interpreter build).

The CE Python's architecture was a genuine kludge: an **Atmel ATSAMD21E18A ARM Cortex-M0+ at 48 MHz** running CircuitPython as a *coprocessor*, with the eZ80 acting as a thin serial terminal over UART. Documented at Datamath (teardown-level primary source):
http://www.datamath.org/Graphing/TI-84PLUS_CEPE_II2021.htm
and Cemetech's confirmation of CircuitPython:
https://www.cemetech.net/forum/viewtopic.php?t=15430

The Evo drops the eZ80 entirely for an **ARM Cortex CPU at 156 MHz** (TI's product sheet confirms 156 MHz vs 48 MHz, and 3.5 MB memory vs 3 MB). Cemetech and Hacker News commentary both read this as the OS being reimplemented natively on ARM rather than emulating eZ80:

> "It appears likely that in an unexpected break from over 30 years of TI's operating system codebase, the OS has been re-implemented with new features natively on the ARM CPU rather than using an ez80 emulator."
> https://news.ycombinator.com/item?id=47980624

**UNVERIFIED:** that the Evo's interpreter is still specifically *CircuitPython* built into the main OS. The claim appears at https://ti84evo.com/ti-84-plus-ce-vs-ti-84-evo-a-complete-comparison-2026/ ("CircuitPython support is integrated natively, built on the ARM Cortex CPU") but that is an affiliate/SEO comparison site, not a primary source or a teardown. **INFERRED, high confidence:** whatever the interpreter lineage, it is a MicroPython-family interpreter running on the main ARM CPU with no separate Python coprocessor, because the coprocessor existed *only* to work around the eZ80's lack of a viable C toolchain — a problem that vanishes on ARM.

### Modules: apparently unchanged. VERIFIED (expert, informal).

The most valuable source here is **Adriweb** — TI-Planet administrator and a maintainer in the TI-Toolkit/tivars orbit — answering a direct reader question about Evo Python improvements, modules, and numpy:

> "Performance et mémoire disponible. Module, pas de changement il me semble. Et numpy non visiblement ils n'ont pas assez [...] de demande pour mettre ça en place à priori..."
> ("Performance and available memory [are what improved]. Modules, no change it seems. And numpy no — apparently they don't have enough demand to implement it.")
> — Adriweb, TI-Planet, 2026-06-06
> https://tiplanet.org/forum/viewtopic.php?f=41&lang=en&t=27399

Earlier in the same thread Adriweb confirms "les performances Python sont mieux" (Python performance is better) based on testing and user reports.

So the expected Evo module set is the same seven as the CE Python — `math`, `random`, `time`, `ti_system`, `ti_plotlib`, `ti_hub`, `ti_rover` (the CE Python set per TI's eGuide, https://education.ti.com/html/eguides/graphing/84PlusCEPy/EN/content/eg_pythonappprog/m_pygetstart/m_84ce_pyobapp.HTML and the Wikipedia TI-84 Plus CE series article, https://en.wikipedia.org/wiki/TI-84_Plus_CE_series).

**Caveat, marked clearly:** Adriweb hedges ("il me semble" / "it seems"), and as of the date of that post TI-Planet's own review series had **not yet published its Python episode** — the index at https://tiplanet.org/forum/viewtopic.php?f=10&t=27361 runs to episode 10 (online calculator & TI Connect Evo) with the Python deep-dive still promised. **There is therefore no published, systematic module-by-module or API-by-API diff of Evo Python vs CE Python yet.** Treat "modules unchanged" as expert impression, not audited fact.

### Language/API differences that could break existing programs

- **UNVERIFIED / likely low risk for Python.** No reported Python API breakage. Performance and available heap improved, which can only help.
- **VERIFIED for TI-BASIC, and worth noting as a warning sign:** TI-BASIC *did* get subtle semantic changes. TI-Planet's converter has a "Smart CE to Evo conversion" option that "adds Evo-safe `DelVar` separators where CE programs used compact syntax that no longer parses the same way" (https://tiplanet.org/scripts/EvoConv/). So the Evo is not a bit-for-bit behavioral clone of the CE. **INFERRED:** analogous small Python-side surprises (screen dimensions being the obvious one) are plausible and must be tested on hardware, not assumed.
- **INFERRED, moderate confidence — the single most likely real breakage for this library:** the graphing area grew from 264x165 to 319x209 pixels (TI product sheet; ti84evo.com comparison; Cemetech). Any program that hardcodes pixel coordinates, assumes a 26-character line width, or lays out `ti_plotlib` output against CE screen dimensions may render wrong or clipped on the Evo — even with an identical API. This is a *layout* problem, not a *language* problem, which is the cheap kind.

---

## Q2. File format — is `.8xp2` real, and do `.8xv` AppVars work?

### `.8xp2` is REAL. VERIFIED by Texas Instruments directly. The report is CONFIRMED, not refuted.

TI's own knowledge base article "Solution 29430: File Types That Can Be Sent to a Calculator" now carries a dedicated **TI-84 Evo** column with a parallel, incompatible extension for every file type:

| Type | TI-83 Plus / TI-84 Plus family | **TI-84 Evo** |
| --- | --- | --- |
| Application Variables (AppVars) | `.8xv` | **`.8xv2`** |
| Program | `.8xp` | **`.8xp2`** |
| List | `.8xl` | `.8xl2` |
| Matrix | `.8xm` | `.8xm2` |
| Equation | `.8xy` | `.8xy2` |
| Group | `.8xg` | `.8xg2` |
| Picture | `.8xi` | `.8ca2` |

Source (primary, TI): https://education.ti.com/en/customer-support/knowledge-base/ti-83-84-plus-family/product-usage/29430

**The finding that matters most to this repo is the AppVar row, which the original report did not mention: Python AppVars on the Evo are `.8xv2`, not `.8xv`.**

### Do the repo's `.8xv` files work on the Evo? NO. VERIFIED.

The Evo does not accept legacy files. Confirmed by TI-Toolkit, the maintainers of the reference `tivars` libraries:

> "The TI-84 Evo uses an entirely new & non-backwards compatible file format that has not yet been fully documented, and thus the Evo is not yet supported."
> — TI-Toolkit/tivars_lib_py README
> https://github.com/TI-Toolkit/tivars_lib_py

And confirmed behaviorally by an educator walkthrough: in TI Connect Evo, "if we try to import `.8xp` files ... nothing shows up ... the Evo doesn't actually use `.8xp` files ... you cannot use the exact files from your old calculator on this calculator."
https://supertutortv.com/videos/how-to-transfer-ti-84-ce-programs-to-the-ti-84-evo-calculator-converting-8xp-to-8xp2-and-uploading-with-ti-connect-software/

### But this is a near-non-problem for us, because `.py` source is auto-converted. VERIFIED.

**This is the most important operational finding in this document.**

TI's own TI Connect Evo materials list "Python programs" as sendable files, and TI-Planet's hands-on review states plainly:

> "Note that TI Connect Evo automatically converts images to the Evo format, as well as Python scripts (`.py` files)."
> — TI-Planet review/test TI-84 Evo-T, episode 10
> https://tiplanet.org/forum/viewtopic.php?f=41&lang=en&t=27399

TI-Planet notes the same auto-conversion happens in the *online* Evo calculator's transfer view. This mirrors long-standing CE behavior, where TI Connect CE converts `.py` to the right AppVar on send (https://education.ti.com/html/eguides/connectivity/TI-Connect-CE/EN/Content/EG_84_TIConnect/M_UsePython/M_UsePython.HTML).

**INFERRED, high confidence:** to put this library on an Evo you ship the `.py` files and let TI Connect Evo build the `.8xv2`. No `.8xv2` writer, no format reverse-engineering, and no new converter tool are required on our side. The in-repo `.8xv` converter remains correct and necessary for CE Python hardware and simply does not apply to Evo.

### Is there a published or community spec for the Evo format? NO. VERIFIED.

- TI has published no format spec (only the extension table above).
- TI-Toolkit explicitly states the format "has not yet been fully documented" and `tivars_lib_py` does not support the Evo: https://github.com/TI-Toolkit/tivars_lib_py
- Partial practical progress exists: TI-Planet's browser-based **TI-Basic CE / Evo Program Converter** (built on `tivars_lib_cpp`) can already read `.8xp` and write `.8xp2`: https://tiplanet.org/scripts/EvoConv/. **UNVERIFIED:** whether that tool handles AppVars/`.8xv2` at all — its UI is described purely in terms of TI-BASIC *program* files (`.8xp` / `.8xp2`), so assume it does **not** cover Python AppVars.

**Bottom line on Q2:** the `.8xp2` claim is proven true, our `.8xv` artifacts are Evo-incompatible, no spec exists, and none of that blocks us because `.py` is the shipping format that works.

---

## Q3. Transfer software — does TI Connect CE still apply?

### No. The Evo uses a new web-based tool. VERIFIED, primary source.

> "TI Connect™ Evo is a web-based app that provides connectivity between a computer and a TI-84 Evo graphing calculator. It allows you to capture the calculator screen, transfer files to and from the calculator, and update the operating system (OS)."
> — TI Connect Evo User Guide (education.ti.com)
> https://education.ti.com/en/product-resources/eguides/eguide-84-evo/evo-connect-user-guide

Key operational facts, all VERIFIED from TI:

- **URL:** `connectevo.ti.com` — no install, no sign-in required (TI KB 40490, https://education.ti.com/en/customer-support/knowledge-base/ti-83-84-plus-family/computer-software-installation-activation/40490)
- **Requirements:** active internet connection, **WebUSB enabled**, browser access to files/clipboard (TI Connect Evo User Guide)
- **Supported platforms:** Windows 11 64-bit, macOS 15 / macOS 26, ChromeOS 143+ (https://education.ti.com/en-au/products/calculators/graphing-calculators/ti-84-evo/ti-connect-evo)
- **Capabilities:** Capture Screen, Send Files, Install OS, Exit Test Mode
- **TI Connect CE does not work with the Evo:** "the Evo will not plug in to TI Connect software if you already have that downloaded for the CE or for older versions of the calculator" (https://supertutortv.com/videos/how-to-transfer-ti-84-ce-programs-to-the-ti-84-evo-calculator-converting-8xp-to-8xp2-and-uploading-with-ti-connect-software/)

TI-Planet frames the shift as a strategic break, and this is worth internalizing:

> "The Evo platform appears to mark a major turning point for Texas Instruments. There is no trace of dedicated software for Windows or Mac. Everything is handled online in your browser (only Google Chrome worked in our tests)."
> — TI-Planet review/test episode 1, https://tiplanet.org/forum/viewtopic.php?f=41&t=27360

### Does USB-C change the workflow?

**VERIFIED, mildly.** The Evo ships with a USB-C cable (TI product sheet) versus the CE's USB mini-B. TI notes: "If your computer only has a USB-C port, you will need a USB-C to USB-C cable to connect your calculator" (TI Connect Evo User Guide). So the Evo needs a USB-C cable that will **not** be interchangeable with the CE mini-USB cables already in the prep kit.

**Workflow implications for the pre-loaded-hardware SOP (INFERRED):**

1. **Two parallel toolchains, permanently.** CE Python units: TI Connect CE desktop + mini-USB + `.8xv`. Evo units: Chrome/Edge at `connectevo.ti.com` + USB-C + `.py` auto-convert. Do not try to unify them.
2. **New dependency risk on the Evo path:** batch prep now requires *internet access and a compatible browser* for every unit flashed. An offline prep bench works for CE and does not work for Evo. That is a genuine operational regression for volume work.
3. **Browser reality check (UNVERIFIED but likely):** TI-Planet found only Chrome worked in testing, and WebUSB is unsupported in Safari and Firefox. Plan on Chrome.
4. **Bulk-loading efficiency is unknown (UNVERIFIED).** TI Connect Evo's documented flow is a file-picker "SEND TO CALCULATOR." Whether multi-select of 52 files, or anything resembling grouping, is practical at volume has not been tested. This should be an explicit test item on first Evo hardware.

---

## Q4. Market window — how long is the CE Python installed base viable?

**Conclusion: effectively stable for 3-5 years, with slow decline beginning around 2029-2031. Shrinking only at the very margin. INFERRED throughout, from verified anchor facts.**

Anchor facts (VERIFIED): CE Python produced 2021-07-27 through 2026-04-27, roughly **five full school years** of production; the Evo launched 2026-04-28 as its replacement; TI additionally still sells plain CE units without Python (so the CE *platform* continues to exist in stores even now).

Reasoning:

1. **Five years of production at graphing-calculator scale is a very large installed base.** The TI-84 line is the default required calculator across US high-school math, and the CE Python was the flagship CE variant for the entire 2021-2026 window. Every one of those units is Python-capable and every one of them is still in a backpack, a classroom set, or a resale channel.
2. **Student device life is long, because these calculators barely age.** A graphing calculator bought in grade 9 is typically used through grade 12 and often into first-year college — a 4-6 year primary life — then hand-me-down or resold for another 2-4 years. Units sold in the final CE Python production year (2025-26) are therefore in *active primary use into roughly 2030*, and in secondary/resale use well beyond that. Nothing about the Evo's release removes a single CE Python unit from a student's hands.
3. **School refresh cycles are slow and budget-bound.** Districts that bought CE Python classroom sets in 2021-2025 will not discard working units because a faster model exists; classroom-set replacement runs on multi-year capital cycles, and the CE's continued availability means mixed CE/Evo classrooms will be normal for years.
4. **The resale channel — which is this business's actual channel — is *fed* by the transition, not starved by it.** New-model launches push used prior-generation inventory into eBay/Mercari/Facebook at lower prices, increasing the volume of CE Python units changing hands. **INFERRED:** the discontinuation plausibly *increases* CE Python resale supply and transaction count over the next 2-3 years, which is favorable for a seller of pre-loaded CE Python hardware and CE Python software, even as it softens per-unit hardware prices.
5. **The one genuine headwind:** new-buyer share shifts to Evo immediately, and TI selling Python-less plain CE units means "buy a new CE and get Python" is no longer reliable advice. Over time the marginal buyer of *new* hardware is an Evo buyer. That erodes the top of the CE Python funnel starting now, but it does not touch the millions of units already in circulation.

**Practical read:** treat the CE Python line as a **harvest asset with a solid 3-5 year runway** (comfortably through 2029-2030, with a thinning tail after), and treat the Evo as a **cheap option to acquire now** rather than an emergency migration.

---

## Q5. First-mover opportunity

### Is anyone selling or publishing Evo Python programs? Essentially no. VERIFIED.

Both major archives created Evo sections, and the Python sections are **nearly empty** roughly 3.5 months after launch:

- **Cemetech, TI-84 Evo Python programs:** https://www.cemetech.net/downloads/browse/84evo/python — the only file visible is **"High Low: Evo"**, described as "the average High Low program, but size-optimized in Python for the TI-84 Evo." A hobby number-guessing game.
- **ticalc.org, TI-84 Evo archive:** https://ticalc.org/pub/84evo/ — `basic` and `python` folders exist; the Evo tree is brand new and sparse.
- **TI-Planet** has an Evo download category and early uploads are appearing, but they are TI-BASIC-leaning (e.g. "ASTROCALC ... [Cours et Formulaires TI-84 Evo]", per the sidebar at https://tiplanet.org/forum/viewtopic.php?f=10&t=27361).

**INFERRED:** there is **no** competing library of educational/study/exam Python tools for the Evo. Early Evo community effort has gone into TI-BASIC conversion (TI-Planet's `.8xp2` converter) and hardware/UI reviews, not Python content. Commercially, no evidence surfaced of anyone *selling* Evo Python program bundles.

Additional structural tailwind (VERIFIED): the Evo has **no C or assembly programmability** (Cemetech, confident). The classic gap-filler for TI calculators — flashy ASM/C games — cannot exist on Evo without a jailbreak that does not yet exist. **INFERRED:** Python is therefore the *only* meaningful third-party content channel on the Evo, and every Evo owner has Python. That is a structurally better content market than the CE ever offered.

### How much of the library ports vs. needs rewriting?

**INFERRED estimate; must be validated on hardware before it is quoted to anyone.**

| Category | Rough share | Work required |
| --- | --- | --- |
| Pure computation / text-output programs (`math`, `random`, `time`, `ti_system` text I/O, `input`/`print`) | Majority | **Likely zero code change.** Re-ship the same `.py`; TI Connect Evo converts on send. |
| Programs with `ti_plotlib` graphing or coordinate/pixel layout | Meaningful minority | **Layout tuning** for 319x209 vs 264x165, and re-checking line/column assumptions. Mechanical, per-program, not architectural. |
| Programs using `ti_hub` / `ti_rover` | Very small or zero | Unverifiable without hardware and peripherals. |
| Anything relying on CE-specific screen size, key codes, or timing quirks | Unknown until tested | Case-by-case. |

**Effort estimate (INFERRED):** if modules truly are unchanged, an Evo-compatible edition is **days of work, not a rewrite** — dominated by (a) actually testing all 52 programs on real Evo hardware, (b) screen-layout fixes for the graphing subset, (c) new install documentation for the `connectevo.ti.com` workflow, and (d) a `.py`-only Evo bundle variant. The honest blocker is **hardware access and test time**, not engineering difficulty. Do not commit to a public Evo compatibility claim before that testing exists.

---

## Strategy

### 1. Proceed with the CE Python line as-is. Yes.

The evidence does not support a pivot. The installed base is five production years deep, student hardware lifespans are long, school refresh is slow, and the resale channel that this business actually sells into is being *fed* additional CE Python supply by the transition. Plan on a solid 3-5 year runway. Keep building, listing, and selling CE Python.

What has genuinely changed is narrower than it feels: **new** CE hardware may lack Python, and **Evo** is now the new-buyer default. Both are top-of-funnel facts, not installed-base facts.

### 2. What specifically to change in storefront / bundle compatibility claims

The reconciliation pass already added the warning that new plain-CE units lack Python and that Evo compatibility is unconfirmed. Beyond that, do these:

- **Never claim or imply Evo compatibility until tested.** Not "should work," not "TI-84 family." The Evo genuinely rejects `.8xv` files, so a buyer with an Evo who follows the current instructions will fail outright and open a dispute. State supported hardware as **TI-84 Plus CE Python Edition / TI-83 Premium CE Edition Python** (CE Python family) explicitly, and name the Evo as **not supported at this time**.
- **Stop using bare "TI-84" / "TI-84 Plus CE" as the compatibility unit.** With three live variants — CE Python, plain CE (no Python), and Evo — the model name alone no longer determines compatibility. The determinant is "does it have the Python app."
- **Add a pre-purchase self-check for buyers**, phrased as a calculator-side test rather than a model number: press the apps/Python entry point and confirm a Python app exists. This converts the most likely refund cause into a pre-sale filter.
- **Do not advertise `.8xv` as a feature.** Frame the deliverable as "Python programs (`.py` source) plus ready-to-send CE AppVars." The `.py` source is the durable, forward-compatible asset and is the honest basis for any future Evo claim.
- **Add a short "I have an Evo" note** for both storefront and support: the Evo uses `connectevo.ti.com` and `.8xv2`/`.8xp2` files, our current CE AppVars will not transfer, and Evo support is under evaluation. Offering that clearly costs nothing and prevents bad reviews.
- **Flag the mini-USB assumption.** Anywhere a cable is mentioned or included, it is a CE-only mini-USB cable and does not fit an Evo.

### 3. Port to the Evo? Yes — but as a low-cost option, on a deliberate schedule.

Recommended sequencing:

1. **Now (no hardware needed, hours):** publish the "I have an Evo" support note; make the `.py` files the headline deliverable; tighten compatibility wording. All upside, no risk.
2. **Next (one Evo unit, days):** buy one Evo, send the `.py` files via `connectevo.ti.com`, and run all 52 programs. This single test answers nearly every open question in this document — real module list via `help('modules')`, real screen behavior, real bulk-send ergonomics.
3. **Then (days, conditional on step 2):** fix the graphing/layout subset, write Evo install instructions, and release an "Evo Edition" or a dual-compatibility bundle. If modules are unchanged as Adriweb suggests, this is genuinely cheap.
4. **Do not** build an `.8xv2` writer or reverse-engineer the Evo format. TI Connect Evo already converts `.py` for free, and TI-Toolkit — the people best equipped to do it — have not documented the format yet. That is a fight with no payoff.

The first-mover case is strong and unusual: the Evo Python archives contain approximately one hobby game, every Evo has Python, and C/ASM are locked out so Python is the *only* third-party content channel. A serious 52-program educational library would be, as far as this research can tell, the first of its kind on the platform.

### 4. Hardware to buy and test first

**Buy one TI-84 Evo (US model, not Evo-T) plus a USB-C to USB-C cable and a USB-A to USB-C cable.** ~$130-160 per the CE-vs-Evo comparison. Highest information-per-dollar purchase available; nearly every UNVERIFIED item above collapses to VERIFIED after one afternoon with it.

Test checklist for that first unit, in priority order:

1. `help('modules')` in the Evo Python shell — get the **actual** module list and settle Q1 definitively.
2. Send one `.py` via `connectevo.ti.com` and confirm auto-conversion works end to end.
3. Try sending many `.py` files at once — establish whether batch prep at volume is viable.
4. Run the graphing-heavy programs and record what breaks at 319x209.
5. Check `ti_system` text-layout behavior (rows/columns, `disp_at` ranges) against CE assumptions.
6. Verify behavior in Press-to-Test / exam mode, since exam-mode Python access is a core selling point of these tools.
7. Note whether the CE-era prep bench (offline, TI Connect CE) can coexist with the online-only Evo flow.

**Do not** buy Evo hardware in quantity for resale prep until step 2-4 above are done. And keep sourcing CE Python units: that is the market with proven demand, proven tooling, and a validated 52-program library today.

---

## Stale claims elsewhere in the repo (list only — no edits made here)

Per instructions, I did not edit these; the reconciliation pass owns them. It has already added the warning about plain-CE units lacking Python and Evo compatibility being unconfirmed, so the items below are **beyond** that.

**To be filled in by a follow-up read of the repo files.**

---

## Open questions this research could not settle

1. **The actual Evo Python module list**, from `help('modules')` on hardware. Adriweb's "no change it seems" is the best available answer and is explicitly hedged. TI-Planet's Python review episode was still unpublished as of June 2026 — **check https://tiplanet.org/forum/viewtopic.php?f=10&t=27361 periodically; it is the single highest-value pending source.**
2. **Whether the interpreter is still CircuitPython** or a different MicroPython derivative.
3. **Whether any `ti_plotlib` / `ti_system` API signatures changed** to accommodate the larger screen.
4. **Whether TI publishes an Evo-specific Python guidebook** with a module reference (the CE equivalent lives under `education.ti.com/html/eguides/`); an Evo eGuide exists at https://education.ti.com/en/product-resources/eguides/eguide-84-evo/ and should be re-checked for a Python section.
5. **Bulk-transfer ergonomics** of TI Connect Evo for 52 files.
6. **Whether `.8xv2` AppVars can be produced offline at all**, which would matter only if TI Connect Evo's auto-conversion turns out to be impractical at volume.
