# Physics / Engineering Bundle — TI-84 Plus CE Python

6 standalone TI-84 Plus CE **Python Edition** programs for Physics I/II (mechanics, circuits),
Statics, and Circuits/Engineering fundamentals.

## What's Included

| File | What it does |
|---|---|
| `kinematics_solver.py` | SUVAT kinematics solver: pick the unknown of v0, v, a, t, d and enter the other four. |
| `projectile_motion.py` | Projectile motion: range, max height, time of flight, with optional `ti_plotlib` trajectory plot. |
| `ohms_law_circuits.py` | Ohm's Law/power solver plus a series/parallel resistor combiner. |
| `rlc_impedance.py` | Series RLC impedance magnitude/phase and LC resonant frequency calculator. |
| `statics_vectors.py` | Resultant of 2D force vectors, and 2D torque/moment about a point. |
| `vector3d_toolkit.py` | 3D vector toolkit: dot product, cross product, magnitude, angle between vectors, and projection. |

## What's in This Download

Every program is included **twice**, in two formats. You only need one of them:

```
8xv/   ready-to-install Python AppVars  <- drag these onto TI Connect CE, no conversion needed
py/    the plain-text Python source     <- read it, edit it, or type it in by hand
```

The `.8xv` files are the same programs, already converted into the calculator's native Python
AppVar format. Each one is named after the name it will show up as in the Python App's program
list, so `QUADSOLV.8xv` installs as `QUADSOLV`.

<!-- PROGRAM-NAME-TABLE -->

## Installing on Your Calculator (TI Connect™ CE)

First, the part that's the same either way:

1. Download and install **TI Connect™ CE** (free, from Texas Instruments) on your Windows/Mac computer.
2. Connect your TI-84 Plus CE **Python Edition** to your computer with a USB cable.
3. Open TI Connect CE — your calculator should appear in **Calculator Explorer**.

### Option A — send the ready-made `.8xv` files (fewest steps)

4. Open this bundle's `8xv/` folder, select the files you want (or all of them), and drag them onto
   the Calculator Explorer window — or use **Actions → Send to Calculator**. There's no conversion
   step: these are already Python AppVars.
5. On the calculator, open the **Python App**, pick the program from the list, and select **Run**.

### Option B — send the `.py` source and let TI Connect CE convert it

4. Do exactly the same thing, but drag the files from the `py/` folder instead. TI Connect CE
   converts each `.py` file into a Python AppVar itself as it sends.
5. Open the **Python App**, pick the program, and select **Run**.

Option B uses TI's own converter, so it's the fallback if anything about Option A doesn't work on
your setup. Both produce the same program on the calculator.

### Option C — no computer at all

Open the **Python App** on the calculator, create a new program, and type the source in from the
`py/` folder. These are short, plain-text files, so this is slower but perfectly workable.

### A note on the `.8xv` files

The `.8xv` files were generated with an open-source converter (included in the project repo as
`tools/py_to_8xv.py`) rather than by TI Connect CE itself. Every file is checked byte-for-byte
against the format TI's own software produces, and the converter is validated by reproducing a
TI-generated Python AppVar exactly. If you ever hit a file that won't load, use Option B — the
`.py` source in this bundle is the same program and always works through TI's own converter.

Keep an eye on the ~50 KB / 100-program on-device storage limit; archive or delete programs you're
not actively using to free up space.

## ⚠️ Exam Policy Disclaimer — Read This First

**Many standardized and proctored exams — AP Exams, the FE/PE exams, and many university
midterms/finals — explicitly prohibit calculators that have been loaded with stored notes,
formulas, or "quiz" programs.** Some exams require you to clear your calculator's memory or use
exam mode (e.g. TI's Press-to-Test) before you're allowed to bring it into the room.

**Before bringing any of these programs into a real exam, you MUST verify your specific exam's
calculator and program policy with your instructor or exam administrator.** These tools are
intended strictly as **study and practice aids** for homework, practice exams, and self-review —
they are **not** intended to help with, and must not be used to facilitate, cheating or misconduct
on a live/proctored exam. When in doubt, delete or archive these programs (or reset your
calculator to defaults) before any exam where their presence would violate the rules.
