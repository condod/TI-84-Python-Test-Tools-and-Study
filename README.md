# TI-84 Plus CE Python Edition — Study & Practice-Exam Toolkit

A collection of 29 standalone TI-84 Plus CE **Python Edition** programs for
engineering/math/science students, organized by subject area. Every program
is a single `.py` text file you can type in on the calculator or transfer
with TI Connect™ CE — and every program is also available as a ready-to-install
`.8xv` Python AppVar in [`8xv/`](8xv/).

## 📦 Pre-Packaged Bundles Available

Ready-to-sell/ready-to-share ZIP bundles of these programs — organized by subject, plus a
free starter pack and a complete all-in-one toolkit — live in [`bundles/`](bundles/). Each
ZIP ships every program twice, as a ready-to-install `.8xv` AppVar under `8xv/` and as `.py`
source under `py/`, and includes its own install guide covering both routes. Each ZIP also
repeats the exam policy disclaimer below. The
`bundles/` folder also includes suggested USD pricing per bundle (see
[`bundles/PRICING.md`](bundles/PRICING.md)) and ready-to-paste store listing copy for
Gumroad/Etsy-style storefronts (see [`bundles/LISTING_COPY.md`](bundles/LISTING_COPY.md)).

## ⚠️ Exam Policy Disclaimer — Read This First

**Many standardized and proctored exams — AP Exams, the FE/PE exams, and many
university midterms/finals — explicitly prohibit calculators that have been
loaded with stored notes, formulas, or "quiz" programs.** Some exams require
you to clear your calculator's memory or use exam mode (e.g. TI's Press-to-Test)
before you're allowed to bring it into the room.

**Before bringing any of these programs into a real exam, you MUST verify
your specific exam's calculator and program policy with your instructor or
exam administrator.** These tools are intended strictly as **study and
practice aids** for homework, practice exams, and self-review — they are
**not** intended to help with, and must not be used to facilitate, cheating
or misconduct on a live/proctored exam. The `formula_flashcards.py` program
in particular is a self-quiz memorization drill, not an answer-lookup tool,
and its own header/prompts repeat this same warning. When in doubt, delete
or archive these programs (or reset your calculator to defaults) before any
exam where their presence would violate the rules.

## Exam Policy Research & Marketing Claims

Two reference documents at the repo root work out, from primary sources, exactly which exams
permit what — and, for anyone selling or sharing these bundles, exactly which claims are
accurate:

- **[`COMPLIANCE_RESEARCH.md`](COMPLIANCE_RESEARCH.md)** — the full findings, organized by exam
  authority (College Board AP, SAT/PSAT, ACT, NCEES FE/PE, IB, CLEP, GED, university courses),
  with the operative policy language quoted verbatim plus source URLs and access dates. Findings
  verified from a primary source are separated from inferences, and everything that could not be
  confirmed is flagged. Also covers what TI's Press-to-Test mode actually does to Python AppVars,
  plus seller-side legal, platform, and trademark considerations.
- **[`MARKETING_CLAIMS_GUIDE.md`](MARKETING_CLAIMS_GUIDE.md)** — a practical "safe to say / do NOT
  say" claims guide, per-exam nuance, ready-to-paste storefront and bundle-README disclaimer text,
  and a trademark / non-affiliation footer.

Three findings worth knowing even if you never sell a copy:

- **AP Exams:** the TI-84 Plus CE Python is named on College Board's approved calculator list, and
  College Board states that *"You don't need to clear your calculators' memories before or after
  the exam."*
- **NCEES FE/PE:** the TI-84 is **not** an approved calculator in any form — only Casio fx-115/
  fx-991, HP 33s/35s, and TI-30X/TI-36X models are permitted.
- **Press-to-Test deletes Python programs.** It disables Apps and TI-BASIC programs, but AppVars
  (how Python programs are stored) are deleted and do not return. Back up with TI Connect™ CE
  first.

## 🛒 Storefront & Go-to-Market

Everything needed to actually sell these bundles lives in [`storefront/`](storefront/):

- **[`index.html`](storefront/index.html)** (plus `styles.css` and `main.js`) — a self-contained,
  mobile-responsive sales landing page: bundle lineup, price comparison table, per-bundle
  contents, a free-starter-pack call to action, an FAQ, and the exam-policy disclaimer. No
  build step and no dependencies beyond a CDN font. Purchase links are flagged with `BUY LINK`
  comments and stay as placeholders until real store URLs are pasted in.
- **[`DEPLOY.md`](storefront/DEPLOY.md)** — publishing the landing page free on GitHub Pages
  from this repo, and pointing a custom domain at it later.
- **[`SETUP_CHECKLIST.md`](storefront/SETUP_CHECKLIST.md)** — step-by-step Gumroad and Etsy
  setup: accounts, listings, what assets to upload, the real (and widely misquoted) fee maths
  on both platforms, and the policy considerations that apply to selling study tools.
- **[`LAUNCH_PLAN.md`](storefront/LAUNCH_PLAN.md)** — a channel-by-channel traffic plan with
  effort and impact estimates, the researched norms of the relevant student and calculator
  communities, and a two-week launch sequence.
- **[`DEMO_SCRIPTS.md`](storefront/DEMO_SCRIPTS.md)** — short-form video scripts, community
  post drafts, and a three-email free-starter-pack nurture sequence.
- **[`SEO_KEYWORDS.md`](storefront/SEO_KEYWORDS.md)** — keyword research with per-bundle Etsy
  13-tag sets, Gumroad tags, and landing-page titles and meta descriptions.

All storefront copy is written against
[`MARKETING_CLAIMS_GUIDE.md`](MARKETING_CLAIMS_GUIDE.md): no exam-legality claims, no
exam-brand terms in tags or metadata, no invented reviews or download numbers, and buyers are
always directed to check their own exam's calculator policy.

## About the TI-84 Plus CE Python Environment

TI-84 Plus CE Python Edition runs a restricted CircuitPython-based
environment, **not** full desktop CPython. These programs were written
against the confirmed, currently-documented constraints of that environment:

- **Available modules:** `math`, `random`, `time`, plus TI's own
  `ti_system`, `ti_plotlib`, `ti_hub`, and `ti_rover`. There is **no**
  `cmath`, `numpy`, `matplotlib`, or other third-party/desktop-only
  libraries, and no general file I/O or internet access.
- `complex` is a built-in type on-device, but since `cmath` is not
  available, any program here that deals with complex results (e.g. the
  quadratic solver) computes and formats real/imaginary parts manually
  instead of relying on `cmath`.
- `ti_plotlib` (aliased `plt` in TI's examples) is confirmed available and
  is used optionally in `projectile_motion.py` for a trajectory sketch; it
  degrades gracefully to text-only output if unavailable.
- **Memory/performance limits:** roughly 50 KB / 100 programs of on-device
  storage, and list lengths are capped at 100 elements. Programs here avoid
  deep recursion, huge loops, and large data structures, and cap user-entered
  list sizes accordingly (e.g. stats and vector tools cap at 90/20 entries).
- All programs use plain `input()`/`print()` text I/O, wrap numeric parsing
  in `try/except` so bad input re-prompts instead of crashing, and use
  simple menus.
- Several calculus programs (derivative, integral, Newton-Raphson, limit)
  let you type a function of `x` as a string (e.g. `sin(x)+x**2`,
  `exp(-x)`), which is evaluated with `eval()` after `from math import *`,
  matching TI's own documented `eval()` usage pattern. Supported names
  include `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `atan2`, `exp`,
  `log`, `log10`, `sqrt`, `pi`, `e`, `abs`, plus `+ - * / **` and
  parentheses. `ode_solver_euler.py` uses the same pattern for a function
  of both `x` and `y`. `discrete_math_toolkit.py`'s truth-table generator
  uses the same `eval()`-on-a-typed-expression pattern for a boolean
  expression of up to three variables (`A`, `B`, `C`).
- `complex_number_calculator.py` is the second program (after
  `quadratic_solver.py`) that deals with complex numbers; since `cmath`
  is not available, it implements add/subtract/multiply/divide/magnitude/
  argument/polar-conversion manually on `(real, imag)` float pairs instead
  of using the built-in `complex` type's operators.

## Folder Structure

```
ti84-python-programs/
├── README.md                     (this file)
├── calculus/                     .py source, by subject
├── differential_equations/
├── algebra_linear_stats/
├── physics_engineering/
├── chemistry_and_exam_tools/
├── trigonometry/
├── biology/
├── computer_science/
├── 8xv/                          ready-to-install Python AppVars (same subject folders)
├── tools/                        converter, verifier, tests, bundle builder
└── bundles/                      sellable ZIPs, pricing, listing copy, format notes
```

---

## Calculus (`calculus/`)

| File | Description |
|---|---|
| `derivative_numeric.py` | Numeric derivative approximator using the central-difference formula with adjustable step size. |
| `simpsons_rule.py` | Definite integral approximator using composite Simpson's Rule. |
| `taylor_series.py` | Maclaurin/Taylor series term generator & partial-sum approximator for sin, cos, e^x, and ln(1+x). |
| `newton_raphson.py` | Newton-Raphson root finder with a full iteration table (derivative estimated numerically). |
| `limit_evaluator.py` | Numeric limit evaluator: evaluates f(x) approaching a target value from both sides. |

**Course fit:** Calculus I/II, introductory numerical methods.

- **`derivative_numeric.py`** — Prompts for `f(x)` (as a string using `x`), a point `x0`, and a step size `h`
  (blank defaults to 0.001). Outputs central-difference derivative estimates at `h/10`, `h`, and `h*10` so you can
  see how the estimate stabilizes as `h` shrinks.
- **`simpsons_rule.py`** — Prompts for `f(x)`, bounds `a` and `b`, and an even subinterval count `n` (auto-rounded
  up if odd). Outputs the Simpson's Rule estimate of the definite integral.
- **`taylor_series.py`** — Prompts you to pick sin/cos/e^x/ln(1+x), then `x` and a number of terms. Outputs each
  term, the running partial sum, and a comparison against the calculator's exact `math` value.
- **`newton_raphson.py`** — Prompts for `f(x)`, an initial guess `x0`, tolerance, and max iterations (blank uses
  sensible defaults). Outputs an iteration table of `x` and `f(x)` and the final root estimate.
- **`limit_evaluator.py`** — Prompts for `f(x)` and a target value `c`. Outputs `f(c-eps)`/`f(c+eps)` for shrinking
  `eps` and a best-guess limit if both sides agree.

---

## Differential Equations (`differential_equations/`)

| File | Description |
|---|---|
| `ode_solver_euler.py` | First-order ODE numerical solver for dy/dx = f(x,y): Euler's method or Improved Euler (Heun's method). |

**Course fit:** Calculus II/III, introductory Differential Equations, numerical methods.

- **`ode_solver_euler.py`** — Prompts for `f(x,y)` (as a string using `x` and `y`), an initial condition `x0`/`y0`,
  a target `x` value to solve toward, and a step size `h` (blank defaults to 0.1). Pick Euler's method or
  Improved Euler (Heun's method) from the menu. Outputs a step-by-step table of `x` and `y` and the final
  approximate `y` at the target `x` (capped at 500 steps as a safety limit).

---

## Algebra / Linear Algebra / Stats (`algebra_linear_stats/`)

| File | Description |
|---|---|
| `quadratic_solver.py` | Quadratic equation solver with discriminant classification and real/complex roots. |
| `quadratic_vertex_analyzer.py` | Derives a quadratic from its vertex plus one other point, then reports vertex/standard form, domain/range, intercepts, and behavior. |
| `linear_system_solver.py` | 2x2 or 3x3 linear system solver via Gaussian elimination with partial pivoting. |
| `matrix_toolkit.py` | Matrix add, multiply, determinant, and inverse for 2x2/3x3 matrices you enter. |
| `descriptive_stats.py` | Mean, median, mode, sample/population variance & standard deviation from a data list. |
| `combinatorics_probability.py` | nPr, nCr, and binomial probability calculator. |
| `complex_number_calculator.py` | Manual complex-number arithmetic (add/subtract/multiply/divide), magnitude/argument, and rectangular ↔ polar conversion. |

**Course fit:** College Algebra, Linear Algebra, Intro Statistics/Probability.

- **`quadratic_solver.py`** — Prompts for `a`, `b`, `c`. Outputs the discriminant, its classification, and either
  two real roots, one repeated root, or a complex conjugate pair written as `a ± bi`.
- **`quadratic_vertex_analyzer.py`** — Prompts for a vertex `(h, k)` and one other point `(x, y)` on the parabola
  (two arbitrary points don't uniquely determine a quadratic, so the vertex supplies the missing condition).
  Outputs vertex form, standard form, domain/range, axis of symmetry, min/max, intercepts, and increasing/
  decreasing behavior.
- **`linear_system_solver.py`** — Prompts for system size (2 or 3) then each equation's coefficients and constant.
  Outputs the solved variables, or a message if the system is inconsistent/dependent.
- **`matrix_toolkit.py`** — Menu for add/multiply/determinant/inverse; prompts for matrix size and entries.
  Outputs the resulting matrix or scalar, or a friendly message for singular matrices.
- **`descriptive_stats.py`** — Prompts for a comma-separated (or one-at-a-time) list of numbers (up to 90 values).
  Outputs mean, median, mode, min/max/range, sample variance/stdev, and population variance/stdev.
- **`combinatorics_probability.py`** — Menu for nPr, nCr, or binomial probability; prompts for `n`, `r`, and/or
  probability `p`. Outputs the computed value.
- **`complex_number_calculator.py`** — Menu for add/subtract/multiply/divide of two complex numbers (entered as
  real/imaginary parts), magnitude & argument of one complex number, rectangular → polar, or polar → rectangular.
  All arithmetic is computed manually on real/imaginary float pairs (no `cmath`). Outputs the result as `a + bi`
  or the requested magnitude/angle/polar form.

---

## Physics / Engineering (`physics_engineering/`)

| File | Description |
|---|---|
| `kinematics_solver.py` | SUVAT kinematics solver: pick the unknown of v0, v, a, t, d and enter the other four. |
| `projectile_motion.py` | Projectile motion: range, max height, time of flight, with optional `ti_plotlib` trajectory plot. |
| `ohms_law_circuits.py` | Ohm's Law/power solver plus a series/parallel resistor combiner. |
| `rlc_impedance.py` | Series RLC impedance magnitude/phase and LC resonant frequency calculator. |
| `statics_vectors.py` | Resultant of 2D force vectors, and 2D torque/moment about a point. |
| `vector3d_toolkit.py` | 3D vector toolkit: dot product, cross product, magnitude, angle between vectors, and projection. |
| `heat_transfer_calculator.py` | Specific heat (q=mcΔT), phase-change latent heat (q=mL), and two-mass mixing/equilibrium temperature (calorimetry). |

**Course fit:** Physics I/II (mechanics, circuits), Statics, Circuits/Engineering fundamentals, intro Thermodynamics.

- **`kinematics_solver.py`** — Choose which of v0/v/a/t/d is unknown, then enter the other four. Outputs the
  solved value with the formula used, or a friendly message if the inputs are inconsistent.
- **`projectile_motion.py`** — Prompts for launch speed, angle, and launch height. Outputs time of flight, range,
  and max height as text; if `ti_plotlib` is available it offers an on-calculator trajectory sketch.
- **`ohms_law_circuits.py`** — Menu for Ohm's Law (solve V/I/R/P from two knowns) or resistor combining. Outputs
  the solved quantity, or the series/parallel equivalent resistance for a list of resistors you enter.
- **`rlc_impedance.py`** — Prompts for R, L, C, and frequency `f`. Outputs `X_L`, `X_C`, impedance magnitude,
  phase angle, and the LC resonant frequency (computed with plain real arithmetic, no `cmath` needed).
- **`statics_vectors.py`** — Menu for force resultant (magnitude+angle pairs) or torque about a point
  (position + force components). Outputs the resultant magnitude/angle, or net torque with rotation sense.
- **`vector3d_toolkit.py`** — Menu for dot product, cross product, magnitude, angle between two vectors, or
  scalar/vector projection of one vector onto another. Enter each vector as `x`, `y`, `z` components. Outputs
  the requested result(s).
- **`heat_transfer_calculator.py`** — Menu for specific heat `q = m*c*ΔT` (enter mass, specific heat, initial/final
  temperature), phase-change latent heat `q = m*L` (enter mass and latent heat), or the equilibrium temperature
  of two masses mixed together (enter each substance's mass, specific heat, and temperature). Outputs the
  computed heat `q` (with an absorbed/released note) or the equilibrium temperature and each substance's heat
  gained/lost for a quick energy-conservation check.

---

## Chemistry & Exam Tools (`chemistry_and_exam_tools/`)

| File | Description |
|---|---|
| `ideal_gas_law.py` | Ideal Gas Law solver (P, V, n, or T) plus a Combined Gas Law (state 1 → state 2) solver. |
| `stoichiometry_molar_mass.py` | Molar mass calculator from element counts, plus mass ↔ moles conversion. |
| `unit_converter.py` | Menu-driven unit converter: length, mass, pressure, temperature, energy. |
| `formula_flashcards.py` | Self-quiz flashcards: random formula-name recall drill by subject category. **Self-study only.** |
| `exam_countdown_drill.py` | Countdown timer plus a random mental-math/sanity-check practice drill with answer checking. |
| `acid_base_calculator.py` | pH/pOH from [H+] or [OH-] (and back), plus Henderson-Hasselbalch buffer pH. |

**Course fit:** General/Intro Chemistry, and general practice-exam time management for any STEM course.

- **`ideal_gas_law.py`** — Menu for Ideal Gas Law (enter any 3 of P/V/n/T) or Combined Gas Law (enter 5 of the 6
  state-1/state-2 values, leaving the unknown blank). Outputs the solved quantity.
- **`stoichiometry_molar_mass.py`** — Enter element symbol/count pairs (e.g. `C`,`1` then `H`,`4` for CH₄) to get
  molar mass from a built-in table of common elements, then optionally convert mass ↔ moles using that molar mass
  (or one you supply directly).
- **`unit_converter.py`** — Pick a category (length, mass, pressure, energy, temperature), pick from/to units from
  a numbered list, and enter a value. Outputs the converted result.
- **`formula_flashcards.py`** — **Self-study memorization aid only — do not use as an answer-lookup tool during an
  actual exam.** Pick a subject (Calculus, Physics, Algebra, Chemistry) and a number of questions; the program
  shows a formula name, waits for you to recall it, then reveals the answer and tracks your self-graded score.
- **`exam_countdown_drill.py`** — Menu for a countdown timer (enter minutes; updates every second) or a random
  drill generator (arithmetic, order-of-magnitude estimation, or percent-of-a-number problems) that checks your
  typed answer against the correct value.
- **`acid_base_calculator.py`** — Menu for pH/pOH from a given [H+] or [OH-] (mol/L), [H+]/[OH-] back-calculated
  from a given pH or pOH, or buffer pH via the Henderson-Hasselbalch equation (enter pKa, [A-], and [HA]).
  Outputs the computed value(s) and an acidic/basic/neutral classification where applicable.

---

## Trigonometry (`trigonometry/`)

| File | Description |
|---|---|
| `oblique_triangle_solver.py` | Non-right-triangle solver using the Law of Sines and Law of Cosines: SSS, SAS, ASA/AAS, and the ambiguous SSA case. |

**Course fit:** Trigonometry, Pre-Calculus, Physics I (vector/force triangles).

- **`oblique_triangle_solver.py`** — Menu for SSS (three sides), SAS (two sides + included angle), ASA/AAS (two
  angles + one side), or SSA (two sides + a non-included angle, the classic ambiguous case). Outputs the missing
  sides/angles, or a message if the inputs don't form a triangle — including reporting 0, 1, or 2 valid solutions
  for the ambiguous SSA case.

---

## Biology (`biology/`)

| File | Description |
|---|---|
| `punnett_square_solver.py` | Monohybrid or dihybrid Punnett-square cross calculator: offspring genotype and phenotype ratios from parent genotypes. |

**Course fit:** Intro Biology, Genetics.

- **`punnett_square_solver.py`** — Menu for a monohybrid cross (one gene, e.g. `Aa` x `Aa`) or a dihybrid cross
  (two independently-assorting genes, e.g. `AaBb` x `AaBb`). Enter the letter(s) used for each gene and each
  parent's genotype. Outputs every offspring genotype and phenotype with their ratios (e.g. the classic 1:2:1
  genotype / 3:1 phenotype monohybrid result, or 9:3:3:1 dihybrid phenotype result), assuming simple dominant/
  recessive inheritance where uppercase is the dominant allele.

---

## Computer Science (`computer_science/`)

| File | Description |
|---|---|
| `discrete_math_toolkit.py` | Number base converter (binary/octal/decimal/hex) plus a boolean logic truth-table generator for a typed expression of up to 3 variables. |

**Course fit:** Discrete Math, Intro Computer Science/Digital Logic.

- **`discrete_math_toolkit.py`** — Menu for a base converter (pick from/to base among binary, octal, decimal, hex,
  then enter a value in the from-base) or a truth-table generator (pick 1-3 variables `A`/`B`/`C`, then type a
  boolean expression using `and`/`or`/`not`/`^` for XOR, e.g. `A and not B`). Outputs the converted value, or a
  full truth table of every input combination and the expression's result for each row.

---

## Transferring to Your Calculator

Install **TI Connect™ CE** and connect your TI-84 Plus CE Python Edition over USB, then pick either route:

- **Ready-made AppVars.** Drag files from [`8xv/`](8xv/) onto TI Connect CE's Calculator Explorer. These are
  already in the calculator's native Python AppVar format, so no conversion step is needed. Each file is named
  after the name it installs as, e.g. `8xv/algebra_linear_stats/QUADSOLV.8xv` shows up as `QUADSOLV`.
- **Source files.** Drag the `.py` files instead and TI Connect CE converts them as it sends — or type a program
  straight into the on-calculator Python editor.

Then run programs from the calculator's Python App shell by selecting the program and pressing the Run option.

Keep an eye on the ~50 KB / 100-program on-device storage limit; archive or delete programs you're not actively
using to free up space, per the on-calculator memory management prompts. All 29 AppVars together come to about
104 KB, so install the subjects you need rather than everything at once.

### About the `.8xv` files

The `.8xv` files are generated by [`tools/py_to_8xv.py`](tools/py_to_8xv.py), a dependency-free converter written
for this repo, and not by TI Connect CE. It is validated by reproducing a Python AppVar that TI's own software
produced, byte for byte, and every generated file is re-parsed, round-tripped against its source, and
cross-checked with `tivars_lib_py`. **They have not been tested on physical hardware** — see
[`bundles/FILE_FORMAT_NOTES.md`](bundles/FILE_FORMAT_NOTES.md) for the full format write-up, the verification
evidence, and precisely what remains unproven. The `.py` route above always works regardless.

If you edit any `.py` file, regenerate the AppVars and bundles:

```bash
python tools/py_to_8xv.py --batch . --out ./8xv --names tools/varnames.json --name-by-var \
    --comment "TI-84 CE Python Study Toolkit"
python tools/build_bundles.py --repo .
python tools/verify_8xv.py --src . --out ./8xv --names tools/varnames.json --name-by-var \
    --bundles ./bundles
```
