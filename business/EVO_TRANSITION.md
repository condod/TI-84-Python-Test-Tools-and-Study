# TI-84 Evo Transition: Research Findings and Strategy

**Research date:** 2026-08-12
**Scope:** What the April 2026 TI-84 Evo launch and the TI-84 Plus CE Python discontinuation mean for this 52-program library.
**Method:** Web research against primary and expert sources, plus a static audit of the repo's own 52 `.py` programs. No Evo hardware was available.

Every finding is tagged **VERIFIED** (primary or recognized-expert source, URL cited), **UNVERIFIED** (single or weak source), or **INFERRED** (my reasoning from verified facts). Nothing about the Evo file format is asserted beyond what a cited source states.

---

## Executive summary — read this first

**Do not panic, and do not rewrite anything. The CE Python market is fine for years, and the library is very probably already Evo-compatible as written.**

Four findings drive that:

1. **The Evo runs Python, natively on an ARM CPU** instead of the CE Python's separate CircuitPython coprocessor. It is faster, has more memory, and appears to carry the same module set. Python is on **every** Evo unit — there is no separate "Python Edition" any more.
2. **The `.8xp2` report is TRUE**, confirmed by TI's own knowledge base — and the AppVar equivalent is **`.8xv2`**, so the repo's `.8xv` files will **not** transfer to an Evo. **But the breakage is specifically a TI-BASIC problem, not a Python problem.** Eddie Shore, who owns both calculators, states that TI rewrote the *TI-BASIC* language engine, and separately that *"Python programs can be transferred easily between the 84 Python and 84 Evo."* TI Connect Evo auto-converts plain `.py` files on send.
3. **TI Connect CE does not work with the Evo at all.** The Evo uses a browser-based tool at `connectevo.ti.com` over WebUSB with a USB-C cable. Every install instruction in the repo is CE-correct and Evo-wrong.
4. **A static audit of all 52 programs found that they import only `math` (30 files), `random` (2), and `time` (1).** Zero programs require `ti_system`, `ti_plotlib`, `ti_hub`, `ti_rover`, or `turtle`. The only two files that touch TI-proprietary modules do so inside `try/except ImportError` with working text fallbacks. **This library is about as portable as a TI calculator program can be.**

Net: the CE Python installed base is five production years deep with a normal multi-year student device life ahead of it — **stable-to-slowly-shrinking through roughly 2030**, not a cliff. Meanwhile the Evo Python archives at Cemetech and ticalc.org are **nearly empty** (one hobby game), every Evo has Python, and C/assembly are locked out so Python is the *only* third-party content channel. The first-mover window is real and the entry cost is one calculator plus a test pass.

---

## Q1. Does the TI-84 Evo run Python, and in what environment?

### It runs Python, on every unit. VERIFIED.

> "We've confirmed that the Evo does have both Python and TI-BASIC programmability, like the TI-84 Plus CE Python Edition before it... we are confident that no user C programmability or assembly programmability is included."
> — Cemetech news, "TI-84 Evo Calculator Released," April 2026
> https://www.cemetech.net/news/2026/4/1062/_/ti-84-evo-calculator-released-fast-graphing-new-ui-new-hardware

TI publishes an **official TI-84 Evo Python App user guide**, which settles the question from the primary source:

> "Using the TI-84 Evo Python App, learn to code with your graphing calculator. Do what online graphing calculators can't by writing and running programs directly on the calculator..."
> — TI-84 Evo User Guide, Python section
> https://education.ti.com/en/product-resources/eguides/eguide-84-evo/python

TI's own Evo-T product sheet lists "Python programming" as present, and TI Connect Evo's product page lists "Python programs" among the file types you send to the calculator:
- https://justmore.dk/images/media/ProductsDocs/TI10014_PRODUCTSHEET.pdf (TI product sheet, "Introducing TI-84 Evo-T")
- https://education.ti.com/en-au/products/calculators/graphing-calculators/ti-84-evo/ti-connect-evo

**Commercially important (VERIFIED):** there is no separate "Evo Python Edition." Python and TI-BASIC are "built into all Evo units (no separate Python edition needed)" (https://ti84evo.com/ti-84-plus-ce-vs-ti-84-evo-a-complete-comparison-2026/), and Eddie Shore's hands-on notes simply list Python as one of the Evo's built-in apps (https://edspi31415.blogspot.com/2026/05/the-new-ti-84-evo.html). This is the **opposite** of the current CE situation, where TI now ships plain CE units without Python. **The entire Evo installed base is Python-capable** — a larger addressable fraction than the CE line ever had.

### Native on the new processor, not a coprocessor. VERIFIED (hardware).

The CE Python's Python support was a genuine kludge: an **Atmel ATSAMD21E18A ARM Cortex-M0+ at 48 MHz** running CircuitPython as a *coprocessor*, with the eZ80 acting as a thin serial terminal over UART. Teardown-level documentation:
- Datamath hardware analysis: http://www.datamath.org/Graphing/TI-84PLUS_CEPE_II2021.htm
- Cemetech, confirming CircuitPython on that adapter: https://www.cemetech.net/forum/viewtopic.php?t=15430

The Evo drops the eZ80 entirely for an **ARM Cortex CPU at 156 MHz**, with 3.5 MB memory vs the CE's 3 MB (TI product sheet; corroborated by Eddie Shore and ti84evo.com). Cemetech and Hacker News commentary both read this as a native ARM OS rewrite rather than eZ80 emulation:

> "It appears likely that in an unexpected break from over 30 years of TI's operating system codebase, the OS has been re-implemented with new features natively on the ARM CPU rather than using an ez80 emulator."
> https://news.ycombinator.com/item?id=47980624

**UNVERIFIED:** that the Evo's interpreter is still specifically *CircuitPython*. That claim appears only at https://ti84evo.com/ti-84-plus-ce-vs-ti-84-evo-a-complete-comparison-2026/ ("CircuitPython support is integrated natively, built on the ARM Cortex CPU"), which is an affiliate/SEO comparison site, not a primary source or a teardown. **INFERRED, high confidence:** whatever its lineage, it is a MicroPython-family interpreter on the main ARM CPU with no separate Python coprocessor — the coprocessor existed *only* to work around the eZ80's lack of a viable C toolchain, a problem that disappears on ARM.

**VERIFIED (expert):** performance improved. Adriweb, TI-Planet administrator, after testing: *"les performances Python sont mieux"* (Python performance is better), and when asked what changed: *"Performance et mémoire disponible"* (performance and available memory).
https://tiplanet.org/forum/viewtopic.php?f=41&lang=en&t=27399

### Modules: same set, with a small addition. VERIFIED (two independent expert sources).

**Source 1 — Adriweb (TI-Planet admin), answering a direct reader question about Evo Python modules and numpy:**

> "Performance et mémoire disponible. Module, pas de changement il me semble. Et numpy non visiblement ils n'ont pas assez [...] de demande pour mettre ça en place à priori..."
> ("Performance and available memory [are what improved]. Modules, no change it seems. And numpy no — apparently they don't have enough demand to implement it.")
> — 2026-06-06, https://tiplanet.org/forum/viewtopic.php?f=41&lang=en&t=27399

**Source 2 — Eddie Shore, who owns a white Evo, listing the Evo's Python modules:**

> "Two programming languages: the classic TI-Basic and Python. Python modules include math, random, plotlib (TI version), time, specialized modules for the TI hub, TI rover, and import processing."
> — https://edspi31415.blogspot.com/2026/05/the-new-ti-84-evo.html

That is the CE Python set — `math`, `random`, `time`, `ti_plotlib`, `ti_hub`, `ti_rover` (plus `ti_system`, which Eddie does not enumerate but which is the module the on-calc menus are built around). For comparison, the CE Python set is documented by TI at https://education.ti.com/html/eguides/graphing/84PlusCEPy/EN/content/eg_pythonappprog/m_pygetstart/m_84ce_pyobapp.HTML and in the Wikipedia TI-84 Plus CE series article, https://en.wikipedia.org/wiki/TI-84_Plus_CE_series.

**One additive change, VERIFIED:** *"The Time Module adds two additional functions: ticks_ms and ticks_diff."* (Eddie Shore, same post.) Additive, so non-breaking.

**Caveats, stated plainly:**
- Adriweb hedges ("il me semble" / "it seems"), and TI-Planet's review series had **not yet published its Python episode** as of June 2026 — the index at https://tiplanet.org/forum/viewtopic.php?f=10&t=27361 runs to episode 10 with the Python deep-dive still promised. **There is still no published, systematic module-by-module API diff.**
- **`turtle` may be gone (UNVERIFIED, and the strongest available hint of a real module regression).** Eddie lists, among his *reasons to buy the older CE Python instead of the Evo*: **"You work with the Turtle Module in Python."** On the CE Python, `turtle` was an add-on module rather than one of the seven built-ins (TI-Planet's module survey, https://tiplanet.org/forum/viewtopic.php?t=24174). **INFERRED:** the Evo probably lacks the `turtle` add-on. Irrelevant to this library — no program uses it (see the audit in Q5) — but it is direct evidence that the Evo's module story is *not* strictly a superset of the CE's.
- `numpy` is not present on either platform (Adriweb, above).

### Language/API differences that would break existing programs

- **Python language level: no reported breakage.** No source in this research reports a Python syntax or semantic regression. Performance and heap both improved.
- **TI-BASIC *did* break, and it is worth understanding why, because it is the source of the `.8xp2` confusion.** Eddie Shore: backwards compatibility with TI-83/84 TI-BASIC programs is *"No (.8xp2). Why? Texas Instruments rewrote the Basic language engine."* TI-Planet's converter correspondingly offers a "Smart CE to Evo conversion" that *"adds Evo-safe `DelVar` separators where CE programs used compact syntax that no longer parses the same way"* (https://tiplanet.org/scripts/EvoConv/). **The rewrite was of the BASIC engine. Python is a separate interpreter and was not part of that rewrite.**
- **Screen geometry changed (VERIFIED), which is the main theoretical risk to a Python program.** The graphing area grew from **264x165 to 319x209** pixels, and per Eddie the Evo graph now fills the screen with no border. Any program hardcoding pixel coordinates or `ti_plotlib` layout against CE dimensions could render wrong. **Per the Q5 audit, no program in this library does this.**
- **The keypad was remapped substantially (VERIFIED).** Eddie documents the arithmetic keys all shifting up a row, `[apps]` replaced by a fraction template, `matrix` moving, `[x^-1]` becoming `[x^n]`, and more. This does not affect Python code, but it **does** invalidate any keystroke-level instructions or screenshots in our documentation for an Evo user.
- **The built-in clock was removed (VERIFIED).** Eddie: *"Evo: No clock option present."* The `time` module still exists and in fact gained `ticks_ms`/`ticks_diff`, so relative timing still works; wall-clock date/time features would not. No program here depends on wall-clock date.

---

## Q2. File format — is `.8xp2` real, and do `.8xv` AppVars work?

### `.8xp2` is REAL. CONFIRMED, not refuted — by Texas Instruments directly.

TI's knowledge base article "Solution 29430: File Types That Can Be Sent to a Calculator" now carries a dedicated **TI-84 Evo** column with a parallel, incompatible extension for every file type:

| Type | TI-83 Plus / TI-84 Plus family | **TI-84 Evo** |
| --- | --- | --- |
| Application Variables (AppVars) | `.8xv` | **`.8xv2`** |
| Program | `.8xp` | **`.8xp2`** |
| List | `.8xl` | `.8xl2` |
| Matrix | `.8xm` | `.8xm2` |
| Equation | `.8xy` | `.8xy2` |
| Group | `.8xg` | `.8xg2` |
| Picture | `.8xi` | `.8ca2` |

Primary source (TI): https://education.ti.com/en/customer-support/knowledge-base/ti-83-84-plus-family/product-usage/29430

**The row the original report missed is the one that matters to us: Python AppVars on the Evo are `.8xv2`, not `.8xv`.**

### Do the repo's `.8xv` files work on an Evo? NO. VERIFIED.

The Evo does not accept legacy files. Confirmed by TI-Toolkit, maintainers of the reference `tivars` libraries:

> "The TI-84 Evo uses an entirely new & non-backwards compatible file format that has not yet been fully documented, and thus the Evo is not yet supported."
> — TI-Toolkit/tivars_lib_py README, https://github.com/TI-Toolkit/tivars_lib_py

And behaviorally, from an educator walkthrough of TI Connect Evo: if you try to import `.8xp` files "nothing shows up ... the Evo doesn't actually use `.8xp` files ... you cannot use the exact files from your old calculator on this calculator."
https://supertutortv.com/videos/how-to-transfer-ti-84-ce-programs-to-the-ti-84-evo-calculator-converting-8xp-to-8xp2-and-uploading-with-ti-connect-software/

**So: the `.8xv` artifacts in `8xv/` are CE-only. An Evo owner handed those files gets nothing.** That is a real and immediate customer-support liability, and the reason the storefront must name supported hardware precisely.

### But `.py` source transfers fine — and this is the finding that saves the product line. VERIFIED.

**Most important sentence in this entire document**, from Eddie Shore, who owns both calculators and wrote a side-by-side comparison of exactly this:

> "Note: Python programs can be transferred easily between the 84 Python and 84 Evo."
> — https://edspi31415.blogspot.com/2026/05/the-new-ti-84-evo.html

Mechanism, confirmed independently by TI-Planet's hands-on review of TI Connect Evo:

> "Note that TI Connect Evo automatically converts images to the Evo format, as well as Python scripts (`.py` files)."
> — TI-Planet review/test TI-84 Evo-T, episode 10, https://tiplanet.org/forum/viewtopic.php?f=41&lang=en&t=27399

TI-Planet notes the same auto-conversion in the *online* Evo calculator's transfer view, and TI's own TI Connect Evo page lists Python programs as a supported send type. This mirrors long-standing CE behavior, where TI Connect CE converts `.py` to the correct AppVar on send (https://education.ti.com/html/eguides/connectivity/TI-Connect-CE/EN/Content/EG_84_TIConnect/M_UsePython/M_UsePython.HTML).

**INFERRED, high confidence:** to put this library on an Evo, ship the `.py` files and let TI Connect Evo build the `.8xv2`. **No `.8xv2` writer, no format reverse-engineering, and no new converter are needed on our side.** The in-repo `.8xv` converter remains correct and necessary for CE Python hardware, and simply does not apply to the Evo. The `.py` source was always the durable asset; the `.8xv` files are a CE-specific convenience layer.

### Is there a published or community spec for the Evo format? NO. VERIFIED.

- TI has published no format specification — only the extension table above.
- TI-Toolkit states explicitly that the format "has not yet been fully documented" and `tivars_lib_py` does not support the Evo: https://github.com/TI-Toolkit/tivars_lib_py
- Partial practical progress does exist for **TI-BASIC only**: TI-Planet's browser-based **TI-Basic CE / Evo Program Converter**, built on `tivars_lib_cpp`, reads `.8xp` and writes `.8xp2`: https://tiplanet.org/scripts/EvoConv/
- **UNVERIFIED:** whether that converter handles AppVars/`.8xv2` at all. Its interface is described purely in terms of TI-BASIC *program* files, so **assume it does not cover Python AppVars.** We do not need it to.

**Q2 verdict:** the `.8xp2` claim is proven true; our `.8xv` files are genuinely Evo-incompatible; no spec exists and reverse-engineering one would be wasted effort; and none of it blocks the product, because `.py` is the format that transfers.

---

## Q3. Transfer software — does TI Connect CE still apply?

### No. There is replacement software, and it is web-based. VERIFIED, primary source.

> "TI Connect™ Evo is a web-based app that provides connectivity between a computer and a TI-84 Evo graphing calculator. It allows you to capture the calculator screen, transfer files to and from the calculator, and update the operating system (OS) on the calculator."
> — TI Connect Evo User Guide, https://education.ti.com/en/product-resources/eguides/eguide-84-evo/evo-connect-user-guide

All VERIFIED from TI:

- **URL:** `connectevo.ti.com` — no install, no sign-in (TI KB 40490, https://education.ti.com/en/customer-support/knowledge-base/ti-83-84-plus-family/computer-software-installation-activation/40490)
- **Requirements:** active internet connection, **WebUSB enabled**, browser access to files/clipboard
- **Platforms:** Windows 11 64-bit, macOS 15 / macOS 26, ChromeOS 143+ (https://education.ti.com/en-au/products/calculators/graphing-calculators/ti-84-evo/ti-connect-evo)
- **Functions:** Capture Screen, Send Files, Install OS, Exit Test Mode
- **TI Connect CE does not work with the Evo:** "the Evo will not plug in to TI Connect software if you already have that downloaded for the CE or for older versions of the calculator" (SupertutorTV, above). Eddie Shore's comparison table puts it flatly — CE Python: "TI Connect CE"; Evo: "https://connectevo.ti.com/ ... (online connection, like TI-nSpire CX II)."

TI-Planet frames this as a strategic break, and it is worth internalizing as an operator:

> "The Evo platform appears to mark a major turning point for Texas Instruments. There is no trace of dedicated software for Windows or Mac. Everything is handled online in your browser (only Google Chrome worked in our tests)."
> — TI-Planet review/test episode 1, https://tiplanet.org/forum/viewtopic.php?f=41&t=27360

### Does USB-C change the workflow? Yes, in ways that matter for batch prep.

**VERIFIED:** the Evo ships with a USB-C to USB-A cable (Eddie Shore; TI product sheet) versus the CE's TI-specific USB-A/USB-mini cable, and TI notes "if your computer only has a USB-C port, you will need a USB-C to USB-C cable."

**Implications for the pre-loaded-hardware SOP (INFERRED):**

1. **Two permanently separate toolchains.** CE Python: TI Connect CE desktop + mini-USB + `.8xv`. Evo: Chrome at `connectevo.ti.com` + USB-C + `.py` auto-convert. Do not try to unify them; document them separately.
2. **The Evo path introduces an internet dependency for every unit flashed.** An offline prep bench works for CE and does **not** work for Evo. For volume work that is a real operational regression, and it is the least obvious consequence of the transition.
3. **Plan on Chrome.** TI-Planet found only Chrome worked; WebUSB is unsupported in Safari and Firefox. **UNVERIFIED** whether Edge (also Chromium/WebUSB) works, though it likely does.
4. **Bulk-loading ergonomics are unknown (UNVERIFIED).** The documented flow is a file-picker "SEND TO CALCULATOR." Whether multi-selecting 52 files — or anything like CE grouping — is practical at volume has not been tested by anyone in this research. Make it an explicit test item on first hardware.
5. **Cables do not carry over.** Any mini-USB cable stock in the prep kit is CE-only.

---

## Q4. Market window — how long does the CE Python installed base stay viable?

**Conclusion: effectively stable for 3-5 years, thinning from roughly 2030. Shrinking only at the margin, and the near term is arguably *better* than before the transition. INFERRED throughout, reasoning from verified anchors.**

Verified anchors: CE Python produced 2021-07-27 to 2026-04-27 — roughly **five full school years**; Evo launched 2026-04-28 at **$160** retail (Eddie Shore) with a 4-year online-emulator license; TI still sells plain CE units, now without Python.

1. **Five years of production at TI-84 scale is a very large installed base.** The TI-84 line is the default required calculator across US high-school math, and the CE Python was the flagship CE variant for that entire window. Every one of those units is Python-capable and nearly all are still in a backpack, a classroom set, or a resale channel. The Evo's launch removed exactly zero of them from students' hands.
2. **These devices have unusually long lives because they barely age.** A graphing calculator bought in grade 9 is typically used through grade 12 and often into first-year college — a 4-6 year primary life — then handed down or resold for another 2-4 years. Units sold in the final production year (2025-26) are therefore in **active primary use into roughly 2030**, with a secondary tail beyond that.
3. **School refresh cycles are slow and budget-bound.** Districts that bought CE Python classroom sets in 2021-2025 will not bin working calculators because a faster model exists. Classroom-set replacement runs on multi-year capital cycles, so mixed CE/Evo classrooms will be normal for years — and mixed classrooms are precisely where a *CE-compatible* study tool keeps mattering.
4. **The resale channel — this business's actual channel — is fed by the transition, not starved by it.** New-model launches push prior-generation inventory into eBay/Mercari/Facebook at lower prices, raising the *volume of units changing hands*. **INFERRED:** the discontinuation plausibly *increases* CE Python resale transactions over the next 2-3 years. Good for a seller of pre-loaded CE Python hardware and CE Python software, even as per-unit hardware prices soften.
5. **Genuine headwinds, honestly stated.** New-buyer share shifts to Evo immediately. TI selling Python-less plain CE units means "buy a new CE and get Python" is no longer safe advice, so the top of the funnel erodes starting now. And per TI's own Evo-T product sheet, **"Continued OS support" is marked as a feature of the Evo-T and left blank for the CE-T Python Edition** (https://justmore.dk/images/media/ProductsDocs/TI10014_PRODUCTSHEET.pdf) — **INFERRED:** CE OS updates are ending, so OS 5.8.5 is likely the effective terminal CE release. That freezes the platform (fine for compatibility — our target stops moving) but it also means "we update it to the latest OS" stops being an evolving value-add, and TI's CE download pages may eventually be retired.

**Practical read:** treat the CE Python line as a **harvest asset with a solid 3-5 year runway** — comfortably through 2029-2030, thinning after — and treat the Evo as a **cheap option to acquire now**, not an emergency migration. This is meaningfully less pessimistic than a hard 2028 cliff.

---

## Q5. First-mover opportunity

### Is anyone publishing or selling Evo Python programs? Essentially nobody. VERIFIED.

Both major archives created Evo sections, and the Python sections are **nearly empty** roughly 3.5 months after launch:

- **Cemetech, TI-84 Evo Python programs:** https://www.cemetech.net/downloads/browse/84evo/python — the only file visible is **"High Low: Evo"**, "the average High Low program, but size-optimized in Python for the TI-84 Evo." A hobby number-guessing game.
- **ticalc.org, TI-84 Evo archive:** https://ticalc.org/pub/84evo/ — `basic` and `python` folders exist; the tree is brand new and sparse.
- **TI-Planet** has an Evo download category with early uploads appearing, but they skew TI-BASIC (e.g. "ASTROCALC ... [Cours et Formulaires TI-84 Evo]", per the sidebar at https://tiplanet.org/forum/viewtopic.php?f=10&t=27361).

**INFERRED:** there is **no** competing library of educational, study, or exam-oriented Python tools for the Evo, and no evidence surfaced of anyone *selling* Evo Python bundles. Early community effort has gone into TI-BASIC conversion tooling and hardware reviews, not Python content.

Three structural tailwinds make this better than a typical first-mover claim:

- **Python is the only third-party content channel on the Evo.** C and assembly are absent and Cemetech is "confident" they are not coming without a jailbreak that does not exist. The historic gap-filler for TI calculators — flashy ASM/C games — cannot exist here.
- **Every Evo owner has Python.** No edition-matching problem, unlike the CE line.
- **The Evo dropped apps we substitute for.** Among Eddie Shore's *reasons to buy the CE Python instead*: "You work with the SciTools and Periodic Table apps a lot." **INFERRED:** the Evo lacks those built-in apps, which makes a Python chemistry/unit-conversion toolkit *more* valuable on the Evo than it was on the CE, not less.

### How much of the library ports versus needs rewriting?

**I audited the repo's 52 program files directly. The result is better than the research questions assumed.**

Complete import inventory across all 52 programs (excluding `tools/` and `qa/`):

| Import | Files |
| --- | --- |
| `from math ...` | 30 |
| `import random` | 2 |
| `import time` | 1 |
| **`ti_system` / `ti_plotlib` / `ti_hub` / `ti_rover` / `turtle` — required** | **0** |

Only two files reference TI-proprietary modules at all, and both guard them:

- `chemistry_and_exam_tools/exam_countdown_drill.py` — `try: import ti_system as ti` for `disp_clr()`, falling back to printing newlines on `ImportError`.
- `physics_engineering/projectile_motion.py` — `try: import ti_plotlib as plt` with `HAS_PLOTLIB` flag; prints "(ti_plotlib not found on this calculator; text output only.)" otherwise.

Consequences (**INFERRED**, but from a direct reading of the actual source):

| Category | Share | Work required |
| --- | --- | --- |
| Pure builtins + `math`/`random`/`time`, text I/O via `input`/`print` | **50 of 52** | **Zero code change expected.** These modules are standard, confirmed present on the Evo, and `time` only gained functions. |
| Guarded optional `ti_system` / `ti_plotlib` use | **2 of 52** | **Zero code change required to run.** Worst case they take the fallback path and still work. Best case they work better on the larger screen. |
| Programs with hardcoded pixel layout or `ti_plotlib` coordinate geometry | **0** | None. The 319x209 screen change has nothing to break here. |
| Programs needing `ti_hub` / `ti_rover` / `turtle` / wall-clock date | **0** | None. This sidesteps the one likely module regression (`turtle`). |

**Effort estimate (INFERRED):** an Evo-compatible edition is **hours of packaging plus one hardware test pass — not a port and not a rewrite.** The work is (a) actually running all 52 programs on real Evo hardware, (b) writing Evo install instructions for the `connectevo.ti.com` workflow, (c) shipping a `.py`-only Evo bundle variant with no `8xv/` folder, and (d) re-checking text output for line-width/wrapping differences in the Evo shell. The binding constraint is **hardware access and test time**, not engineering.

**Do not make a public Evo compatibility claim before that test pass exists.** The evidence is strong but it is still inference plus one expert's general statement; "we tested all 52 on an Evo" is a different and much more defensible claim.

---

## Strategy

### 1. Proceed with the CE Python line as-is. Yes — and with more confidence than before this research.

Nothing here supports a pivot. The installed base is five production years deep, student hardware lifespans run to 2030 and beyond, school refresh is slow, and the resale channel this business sells into is being *fed* extra CE Python supply by the transition. Keep building, listing, and selling CE Python on a 3-5 year runway.

What actually changed is narrower than it feels: **new** CE hardware may lack Python, and **Evo** is the new-buyer default. Both are top-of-funnel facts. Neither touches the installed base, and the platform freezing (no more CE OS updates) actually makes our compatibility target stop moving.

### 2. What specifically to change in storefront / bundle compatibility claims

The reconciliation pass already added the plain-CE-lacks-Python warning and the "Evo compatibility unconfirmed" note. Beyond that:

- **Replace "Evo compatibility is unconfirmed" with something more accurate and more useful.** The blunt truth is now two-sided and both halves matter: **the `.8xv` AppVars definitely do not transfer to an Evo**, and **the `.py` sources very likely do** (with TI Connect Evo converting on send), pending our own hardware test. A flat "unconfirmed" understates the AppVar problem and undersells the `.py` solution.
- **Never claim tested Evo compatibility until it is tested.** No "should work," no bare "TI-84 family."
- **Stop using model names as the compatibility unit.** With three live variants — CE Python, plain CE (no Python), Evo — the model name no longer determines compatibility. The determinant is "does this calculator have the Python app." State supported hardware explicitly as the **CE Python family** (TI-84 Plus CE Python Edition / TI-84 Plus CE-T Python Edition / TI-83 Premium CE Edition Python) and name the **Evo as not-yet-supported**.
- **Add a pre-purchase self-check phrased as a calculator-side test,** not a model number: press `[prgm]` and confirm a Python app is listed. This turns the single most likely refund cause into a pre-sale filter.
- **Do not advertise `.8xv` as the headline feature.** Lead with "52 Python programs (`.py` source) plus ready-to-send CE AppVars." The `.py` source is the durable, forward-compatible asset and the honest basis for any future Evo claim.
- **Add a short "I have an Evo" note** to storefront and support macros: the Evo uses `connectevo.ti.com` and `.8xv2` files, our CE AppVars will not transfer, the `.py` sources are expected to work via TI Connect Evo's automatic conversion, and formal Evo support is in evaluation. This costs nothing and prevents bad reviews.
- **Flag the cable and keystroke assumptions.** Any included or referenced cable is CE-only mini-USB. Any keystroke-level instructions or screenshots are CE-only — the Evo's keypad was substantially remapped.

### 3. Port to the Evo? Yes. It is cheap, and the first-mover case is unusually good.

1. **Now (no hardware, hours):** publish the "I have an Evo" support note; promote the `.py` files to headline deliverable; tighten compatibility wording per above. Pure upside.
2. **Next (one Evo, ~$160, days):** buy one unit and run the test checklist below. This single purchase converts nearly every UNVERIFIED item in this document to VERIFIED.
3. **Then (hours, conditional on step 2):** ship an "Evo Edition" — the same 52 `.py` files, no `8xv/` folder, new install instructions. Given the audit, expect **no code changes**. If a text-wrapping issue appears, fix it globally.
4. **Then consider publishing 2-3 free programs to the Cemetech and ticalc.org Evo Python archives.** Those archives are almost empty; being early and visible there is close to free marketing into exactly the right audience, and it establishes the library's name on the platform.
5. **Do not** build an `.8xv2` writer or reverse-engineer the Evo format. TI Connect Evo converts `.py` for free, and TI-Toolkit — the people best equipped to do it — have not documented the format. That is a fight with no payoff.

### 4. Hardware to buy and test first

**Buy one TI-84 Evo (US model, not the Evo-T), plus a USB-C-to-USB-C cable.** ~$160 retail (Eddie Shore); the box includes a USB-C to USB-A cable, so the C-to-C is only needed for a USB-C-only computer. Highest information-per-dollar purchase available to this business.

Test checklist, in priority order:

1. **`help('modules')` in the Evo Python shell** — get the actual module list and settle Q1 definitively. Confirm `ti_system` is present and note whether `turtle` is absent.
2. **Send one `.py` via `connectevo.ti.com`** and confirm the automatic conversion works end to end.
3. **Try sending all 52 `.py` files at once** — establishes whether Evo batch prep is viable at volume. This is the biggest unknown for the pre-loaded-hardware business.
4. **Run all 52 programs** and record anything that misbehaves. Pay attention to **text wrapping and line width** in the Evo shell, which is now the most plausible failure mode.
5. **Check the two guarded programs specifically** — `exam_countdown_drill.py` (does `ti_system.disp_clr()` work?) and `projectile_motion.py` (does `ti_plotlib` draw correctly at 319x209?).
6. **Verify behavior in Press-to-Test / exam mode**, since exam-mode availability is a core selling point of these tools.
7. **Confirm the CE prep bench and the online-only Evo flow can coexist** on one machine.

**Do not** buy Evo units in quantity for resale prep until steps 2-4 are done. And keep sourcing CE Python units: that is the market with proven demand, proven tooling, and a validated 52-program library today.

---

## Stale claims elsewhere in the repo — list only, no edits made

Per instructions I did not edit any of these. The reconciliation pass owns them and has already added the plain-CE-lacks-Python warning plus an "Evo compatibility unconfirmed" note, so everything below is **beyond that baseline**. Ordered by how misleading it is now.

1. **`business/SOURCING.md` §0, item 3 — the central claim is now resolved, and resolved favorably.** It reads: *"Whether they carry to the Evo is [UNVERIFIED] — one write-up says the Evo's new OS architecture is not natively backward compatible with CE programs. Do not assume your product transfers."* Two corrections: the non-backward-compatibility is **verified and specific** (`.8xv`→`.8xv2`, TI KB 29430) but it applies to the **file container and the rewritten TI-BASIC engine**, and Eddie Shore states Python programs transfer easily between the two calculators. The `.py` sources are the thing that carries; the `.8xv` files are the thing that does not.
2. **`business/UNIT_ECONOMICS.md` §10.5 — the open question it poses is now substantially answered, and its outlook table is more pessimistic than the evidence supports.** Line 532-533 lists `.8xv` Evo compatibility as `[UNVERIFIED]`; it is now verifiably **incompatible**, with `.py` as the working path. The 2028+ row — "the software line probably doesn't survive it unless the programs are ported" — should be re-read against Q4 and Q5: the installed base runs to ~2030, and the "port" is a packaging change, not a rewrite. Item 2 under "Two decisions follow" ("Find out whether the programs run on the Evo, soon") is still the right action but is no longer an open unknown.
3. **`business/README.md` lines 40-44, 60, and open question 5 (line 121)** — all frame Evo program compatibility as unknown and as the pivotal unanswered question. It is now largely answered; the residual unknown is narrow (our own hardware test pass), and the README's framing of it as existential should soften.
4. **`business/SOURCING.md` §0 item 4 and the "TI-84 Evo" section (~line 350) — "Do not buy Evo units for this line"** is right for *inventory* and wrong as stated for *R&D*. It cites "unproven compatibility" as a reason not to buy, when buying exactly one unit is how that gets proven. Worth splitting explicitly into "do not stock Evo for resale" versus "buy one Evo now as R&D."
5. **`bundles/FILE_FORMAT_NOTES.md` opening section — needs scoping to the CE family.** It states Python programs are stored "as a Python AppVar with the extension `.8xv`" as a general fact about TI-84-series Python. That is now CE-specific: the Evo uses `.8xv2`. The document's `.8xv` research and converter validation remain entirely correct for CE hardware; only the scope statement is stale.
6. **All six `bundles/readme/*.md` install guides and the root `README.md` install section (~lines 498-513) assume TI Connect CE exclusively.** An Evo buyer following "drag files from `8xv/` onto TI Connect CE's Calculator Explorer" fails twice over: TI Connect CE will not connect to an Evo at all, and the `.8xv` files would be rejected anyway. Each needs at minimum a one-line "if you have a TI-84 Evo, these instructions do not apply" pointer.
7. **`business/PREP_SOP.md` — three items.** (a) The whole SOP assumes TI Connect CE and mini-B connection (lines ~178, 192, 448-456); it is CE-only and should say so in its scope header. (b) Line 74's OS-bundle guidance ("Latest as of research date: 5.8.5... Verify at education.ti.com before each batch") should note that with the CE discontinued and TI marking "Continued OS support" as Evo-only, 5.8.5 is likely the terminal CE release — so "verify before each batch" can relax to a periodic check, and TI's CE download pages may eventually be retired (worth archiving the `.b84` locally). (c) Line ~276 already recommends sending `.py` and letting TI Connect CE convert for first production units; that instinct is now vindicated as the forward-compatible choice and could be stated as the default.
8. **`business/LISTING_AND_SUPPORT.md` §"One title note on the TI-84 Evo" (lines 82-89)** — the advice (never put "Evo" in a CE Python title; add an honest clarifying line) is sound and should be kept. What is missing is the buyer-facing consequence: an Evo owner cannot use the `.8xv` files at all. The suggested clarifying line mentions TI Connect CE and a Mini-B cable but not the file-format incompatibility, which is the part that actually generates disputes.
9. **`business/LISTING_AND_SUPPORT.md` line 42 and similar "Latest OS 5.8.5" title copy** — still literally true and likely to *stay* true permanently, but "Latest" reads as a freshness claim on a discontinued platform. Consider "OS 5.8.5 (final CE release)" once TI's end of CE OS support is confirmed, since that is both honest and a stronger reassurance.
10. **`bundles/LISTING_COPY.md` keyword/tag sets** — every bundle's tags include "ti connect ce" and "ti-84 plus ce python," which is correct targeting, but there is no guidance on Evo search traffic. Worth a note that "evo" should be excluded from tags while the product is CE-only, matching the §"One title note" policy in `LISTING_AND_SUPPORT.md`.
11. **`business/README.md` line 148 trademark line** — lists TI-84 Plus CE Python™, TI-84 Evo™, and TI Connect™ CE. If Evo material gets added anywhere buyer-facing, **TI Connect™ Evo** should join that list.

---

## Open questions this research could not settle

1. **The actual Evo Python module list**, from `help('modules')` on hardware. Two expert sources agree it is unchanged, but one hedges and the other is a prose summary. **Highest-value pending public source: TI-Planet's unpublished Python review episode — watch https://tiplanet.org/forum/viewtopic.php?f=10&t=27361.**
2. **Whether `turtle` (and any other CE add-on modules) survived.** Eddie's "reasons to buy the CE" list implies `turtle` did not. Irrelevant to this library, relevant to any future program that wants graphics.
3. **Whether the interpreter is still CircuitPython** or another MicroPython derivative.
4. **Whether any `ti_system` / `ti_plotlib` signatures changed** for the larger screen. Matters only to the two guarded programs.
5. **Text output width in the Evo Python shell** versus the CE — the most plausible remaining break for this library, and completely untested.
6. **Bulk-transfer ergonomics of TI Connect Evo** for ~52 files, and whether Edge works alongside Chrome.
7. **Whether TI has formally announced end of OS support for the CE Python.** The Evo-T product sheet's "Continued OS support" row is strong circumstantial evidence but is not an announcement.
8. **Whether `.8xv2` can be produced offline at all** — matters only if TI Connect Evo's auto-conversion proves impractical at volume.
