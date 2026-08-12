# File Format Research — Why These Bundles Ship `.py`, Not a Compiled Binary

Before packaging these bundles, we researched exactly what file format TI-84 Plus CE
**Python Edition** programs actually use on-device, and whether producing that format is
something that can be automated in a scripted/command-line environment. Findings:

## What the on-calculator format actually is

- TI-84 Plus CE Python programs are **not** `.8xp` files. `.8xp` is the file extension for
  compiled **TI-BASIC** programs on TI-83/84-series calculators.
- On-device, a Python program is stored as a **Python AppVar**, with the file extension
  **`.8xv`** (confirmed via Texas Instruments' own TI Connect™ CE documentation and the
  TI-84 Plus CE Python eGuide).
- The normal workflow is: you write/keep a plain `.py` text file on your computer, then
  TI Connect CE converts it into a `.8xv` Python AppVar automatically when you send it to
  a connected calculator (drag-and-drop, or Actions → Send to Calculator). Going the other
  direction, TI Connect CE can pull a program off the calculator back to your computer as
  either `.8xv` (binary AppVar) or `.py` (re-editable text) — TI's own docs recommend
  saving as `.py` for anything you intend to keep editing.

## Is producing `.8xv` scriptable outside TI's GUI?

Officially, no — Texas Instruments does not ship a documented command-line converter;
`.py` → `.8xv` conversion is a TI Connect CE **GUI** feature. There are unofficial,
community-reverse-engineered open-source tools (e.g. `tivars_lib_py` / the `tivars` CLI,
and small scripts like `tipyto8xv`) that can construct `.8xv` files programmatically. We
did **not** use them to pre-convert these bundles, for two reasons:

1. They are unofficial/undocumented-by-TI reverse-engineering projects, not something TI
   supports or has certified against the Python Edition's on-device format — using them to
   ship a "converted" binary to paying customers would mean shipping a file whose validity
   we can't independently verify.
2. This environment has no physical TI-84 Plus CE Python calculator (or emulator) attached
   to actually test that a programmatically-generated `.8xv` loads and runs correctly on
   real hardware. Shipping an untested binary conversion as if it were a verified,
   ready-to-run compiled program would be dishonest.

## What we shipped instead

Every bundle contains the **plain `.py` source files** (the same files already in this
repo) plus a step-by-step install guide for TI Connect™ CE. This is:

- **Exactly the input format TI's own official tooling expects** — buyers drag the `.py`
  files onto TI Connect CE and it handles the `.8xv` conversion automatically and reliably,
  using TI's own certified converter rather than an unverified third-party one.
- **A legitimate, common distribution model** — plenty of calculator-program sellers
  (including in this same niche) ship source files with an install guide rather than a
  pre-converted binary, especially since the `.py` → `.8xv` step is a single drag-and-drop
  that takes seconds in TI Connect CE.
- **More flexible for the buyer** — a `.py` file can be inspected, tweaked, or typed
  directly into the on-calculator Python editor if someone doesn't have TI Connect CE
  installed yet, whereas a `.8xv` binary cannot be edited as text at all.

If a future revision wants to ship pre-converted `.8xv` files, that would require either
(a) installing and validating TI's official TI Connect CE software in a Windows/Mac GUI
environment with a real or emulated calculator to confirm each converted file actually
runs, or (b) adopting `tivars_lib_py` with real hardware/emulator validation of every
output file — neither of which is something we can respons­ibly do headlessly in this
environment.
