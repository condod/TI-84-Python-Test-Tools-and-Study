# TI-84 Plus CE Python Edition — Study & Practice-Exam Toolkit

A collection of 52 standalone TI-84 Plus CE **Python Edition** programs for
engineering/math/science students, organized by subject area. Every program
is a single `.py` text file you can type in on the calculator or transfer
with TI Connect™ CE — and every program is also available as a ready-to-install
`.8xv` Python AppVar in [`8xv/`](8xv/). The `.py` source is the portable format:
it is also the route onto a **TI-84 Evo**, which cannot read `.8xv` files.

> **Before you install:** the full library is about 247 KB of source and the
> calculator holds roughly 50 KB of Python, so it is meant to be installed a
> subject at a time. See [Storage Budget](#storage-budget-the-full-library-does-not-fit-at-once).

> **⚠️ Before you buy a calculator for this:** these need a TI-84 Plus CE
> **Python Edition**, or a TI-84 Plus CE with TI's Python App installed. TI
> discontinued the CE Python on **2026-04-27** and the plain TI-84 Plus CE now
> sold does **not** include Python. See
> [Hardware Compatibility](#hardware-compatibility-check-for-python-before-you-buy).

> **Got a TI-84 Evo?** Use the `.py` files, not the `.8xv` files — the Evo uses a
> different AppVar format and a different transfer tool. See
> [Transferring to a TI-84 Evo](#transferring-to-a-ti-84-evo).

## 📦 Pre-Packaged Bundles Available

Ready-to-sell/ready-to-share ZIP bundles of these programs — **seven subject bundles**, a
free 5-program starter pack, and a complete all-in-one toolkit with all 52 — live in
[`bundles/`](bundles/). Each ZIP ships every program twice, as a ready-to-install `.8xv`
AppVar under `8xv/` and as `.py` source under `py/`, and includes its own install guide
covering both routes. Each ZIP also repeats the compatibility warning, the Press-to-Test
backup warning, the exam policy disclaimer below, and the trademark footer — all injected
at build time from [`bundles/readme/_shared.md`](bundles/readme/_shared.md) so the nine
copies cannot drift apart.

| Bundle | Programs | Price |
|---|---|---|
| Free Starter Pack | 5 | $0 |
| Algebra, Precalculus & Trigonometry | 11 | $19 |
| Calculus & Differential Equations | 6 | $12 |
| Statistics, Probability & Discrete Math | 5 | $12 |
| Physics & Engineering | 13 | $19 |
| Chemistry & Exam Tools | 7 | $15 |
| Biology & Lab Science | 6 | $12 |
| Finance & Business Math | 5 | $12 |
| **Complete Toolkit** | **52** | **$49** (vs. $101 separately) |

The `bundles/` folder also holds the pricing rationale and platform fee maths (see
[`bundles/PRICING.md`](bundles/PRICING.md)) and ready-to-paste store listing copy for
Gumroad/Etsy-style storefronts (see [`bundles/LISTING_COPY.md`](bundles/LISTING_COPY.md)).

The seven subject bundles list 53 slots but the library is 52 distinct programs:
`chi_square_genetics.py` sells into both the statistics and the biology bundle, and the
Complete Toolkit ships it once.

## ⚠️ Exam Policy Disclaimer — Read This First

**You are responsible for knowing your own exam's calculator rules.** They differ
significantly between exams, and they change. **Nothing here is "approved" for any exam** —
no exam board operates an approval process for third-party calculator software. Verified
from primary sources on 2026-08-12; re-check before any exam.

- **AP® Exams (College Board).** The TI-84 Plus CE Python Edition appears on College Board's
  list of approved handheld graphing calculators, and College Board's published AP
  calculator policy states: *"You don't need to clear your calculators' memories before or
  after the exam,"* and *"Calculators with built-in physical constants, metric conversions,
  and physics, chemistry, or mathematics formulas are permitted."* College Board approves the
  *calculator* — it does not approve, review, or endorse third-party programs. Note that
  College Board prohibits using calculator memory to remove test material from the room, and
  that AP® Calculus and AP® Precalculus both have sections where no calculator is allowed.
- **SAT®, PSAT/NMSQT®, PSAT™ 10, PSAT™ 8/9.** College Board requires you to *"remove programs
  that have algebra functionality"* and *"remove any stored documents,"* and the Testing
  Rules state that *"Before testing, you will be asked to clear all saved formulas."*
  **Remove these programs before an SAT® Suite test.**
- **ACT®.** ACT requires all documents to be removed and permits only single-purpose math
  programs of **25 logical lines or fewer** — most programs here exceed that. ACT also states
  that Press-to-Test mode is *not* sufficient. **Remove these programs before the ACT®.**
- **NCEES® FE / PE / FS / PS.** The TI-84 is **prohibited outright**, regardless of what is
  stored on it — only Casio fx-115/fx-991, HP 33s/35s, and TI models with "TI-30X" or
  "TI-36X" in the name are permitted. If you are sitting the FE, use a TI-36X Pro.
- **IB® Diploma Programme.** A permitted non-CAS device, but IB requires third-party programs
  and stored notes to be removed or blocked, and schools must clear calculator memories.
- **CLEP®.** No personal calculator at all; CLEP provides an on-screen TI-84 Plus CE.
- **University and course exams.** Your instructor or department sets the rules. Many require
  a memory clear or Press-to-Test. **Ask before test day.**

These tools are intended strictly as **study and practice aids** for homework, practice
exams, and self-review — they are **not** intended to help with, and must not be used to
facilitate, cheating or misconduct on a live/proctored exam. The `formula_flashcards.py`
program in particular is a self-quiz memorization drill, not an answer-lookup tool, and its
own header/prompts repeat this same warning. Where a program's presence would break your
exam's rules, delete it or use exam mode — and back it up first (see
[Press-to-Test](#back-up-before-press-to-test)).

The full per-exam write-up, with policy language quoted verbatim and source URLs, is in
[`COMPLIANCE_RESEARCH.md`](COMPLIANCE_RESEARCH.md); the claim-by-claim
"safe to say / do NOT say" guide is in
[`MARKETING_CLAIMS_GUIDE.md`](MARKETING_CLAIMS_GUIDE.md).

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

Four findings worth knowing even if you never sell a copy:

- **AP Exams:** the TI-84 Plus CE Python is named on College Board's approved calculator list, and
  College Board states that *"You don't need to clear your calculators' memories before or after
  the exam."*
- **NCEES FE/PE:** the TI-84 is **not** an approved calculator in any form — only Casio fx-115/
  fx-991, HP 33s/35s, and TI-30X/TI-36X models are permitted.
- **Press-to-Test deletes Python programs.** It disables Apps and TI-BASIC programs, but AppVars
  (how Python programs are stored) are deleted and do not return. Back up with TI Connect™ CE
  first.
- **The hardware is being discontinued.** TI discontinued the TI-84 Plus CE Python on 2026-04-27,
  and the plain TI-84 Plus CE still on sale has no Python. Check for "Python" before buying a
  calculator for this.

## 🛒 Storefront & Go-to-Market

Everything needed to actually sell these bundles lives in [`storefront/`](storefront/).
**The landing page is live at
<https://condod.github.io/TI-84-Python-Test-Tools-and-Study/>** (GitHub Pages, published from
`main` + `/docs`).

- **[`index.html`](storefront/index.html)** (plus `styles.css` and `main.js`) — a self-contained,
  mobile-responsive sales landing page: bundle lineup, price comparison table, per-bundle
  contents, a free-starter-pack call to action, an FAQ, and the exam-policy disclaimer. No
  build step and no dependencies beyond a CDN font. Purchase links are flagged with `BUY LINK`
  comments and stay as placeholders until real store URLs are pasted in.
- **[`DEPLOY.md`](storefront/DEPLOY.md)** — how the page is published free on GitHub Pages from
  this repo, and how to point a custom domain at it later. Pages can only serve the repo root
  or `/docs`, so [`docs/`](docs/) is a **generated copy** of the page produced by
  [`tools/sync_docs.py`](tools/sync_docs.py) — re-run it after editing `storefront/`, or the
  live site keeps serving the old version.
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
├── COMPLIANCE_RESEARCH.md        per-exam policy research, primary sources
├── MARKETING_CLAIMS_GUIDE.md     safe-to-say / do-NOT-say claims guide
│
├── algebra_linear_stats/         .py source, by subject  (8)
├── astronomy/                    (1)
├── biology/                      (6)
├── calculus/                     (5)
├── chemistry_and_exam_tools/     (7)
├── computer_science/             (1)
├── differential_equations/       (1)
├── finance/                      (5)
├── geometry/                     (1)
├── physics_engineering/          (8)
├── precalculus/                  (3)
├── thermo_materials/             (4)
├── trigonometry/                 (2)
│                                 = 52 programs across 13 subject folders
│
├── 8xv/                          ready-to-install Python AppVars (same subject folders)
├── tools/                        converter, verifier, tests, bundle builder, docs sync
├── qa/                           TI-environment simulator, static checks, functional cases
├── bundles/                      sellable ZIPs, pricing, listing copy, format notes
│   └── readme/                   per-bundle README sources + _shared.md common blocks
├── storefront/                   landing page, deploy/setup guides, SEO, launch plan
├── docs/                         GENERATED GitHub Pages root - copy of storefront/ page
└── business/                     sourcing, unit economics, platform strategy
```

Note that the **subject folders are a filing system, not the product lineup.** The bundles
are grouped by the course a student is enrolled in, so several folders are split across
bundles — the stats programs in `algebra_linear_stats/` sell into the statistics bundle
while the quadratics sell into the precalculus bundle — and the thin folders
(`geometry/`, `astronomy/`, `computer_science/`, `differential_equations/`) are folded into
a larger neighbour rather than shipping as one-program bundles. The authoritative mapping
is the bundle definitions at the top of
[`tools/build_bundles.py`](tools/build_bundles.py).

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
| `confidence_interval_hypothesis_test.py` | One-sample confidence interval for a population mean and a one-sample hypothesis test, using z (σ known) or t (df = n−1) critical values from a built-in table. |

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
- **`confidence_interval_hypothesis_test.py`** — Pick a confidence interval or a hypothesis test, then z or t.
  Enter the sample mean, sample size `n`, and σ (population) or `s` (sample); the hypothesis test also asks for
  the claimed mean `μ₀`, the tail direction, and a significance level. Critical values come from a built-in
  standard-normal / Student's t table, because the calculator has no inverse-CDF function; t degrees of freedom
  above 30 fall back to the normal row, the same as most textbook tables. Outputs the interval, or the test
  statistic, the critical value, and a reject / fail-to-reject conclusion.
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
| `fluid_mechanics_solver.py` | Bernoulli's equation between two points in a flow, plus Reynolds number for pipe flow with a laminar/transitional/turbulent classification. |

**Course fit:** Physics I/II (mechanics, circuits), Statics, Circuits/Engineering fundamentals, Fluid Mechanics, intro Thermodynamics.

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
- **`fluid_mechanics_solver.py`** — Menu for Bernoulli's equation (`P + ½ρv² + ρgh` constant between two points,
  solving for whichever of `P2`, `v2`, or `h2` is unknown given the full state at point 1) or the Reynolds
  number for pipe flow (`Re = ρvD/μ`, or `vD/ν` with kinematic viscosity). Outputs the solved quantity, or the
  Reynolds number with a laminar / transitional / turbulent classification.

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
| `reaction_kinetics.py` | Zero-, first-, and second-order kinetics for a single reactant: half-life, [A] at a given time by the integrated rate law, and the time to reach a target [A]. |

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
- **`reaction_kinetics.py`** — Menu for half-life, concentration at a time, or time to reach a concentration;
  then pick the reaction order (zero, first, or second) and enter the rate constant `k`, the initial
  concentration `[A]₀`, and either a time `t` or a target `[A]`. Outputs the requested half-life,
  concentration, or time from the integrated rate law for that order.

---

## Trigonometry (`trigonometry/`)

| File | Description |
|---|---|
| `oblique_triangle_solver.py` | Non-right-triangle solver using the Law of Sines and Law of Cosines: SSS, SAS, ASA/AAS, and the ambiguous SSA case. |
| `unit_circle_reference.py` | Unit-circle reference and trig evaluator: all six functions at an angle with exact values named, reference angle, quadrant, sign pattern, degree/radian conversion, inverse trig, and identity checks. |

**Course fit:** Trigonometry, Pre-Calculus, Physics I (vector/force triangles).

- **`oblique_triangle_solver.py`** — Menu for SSS (three sides), SAS (two sides + included angle), ASA/AAS (two
  angles + one side), or SSA (two sides + a non-included angle, the classic ambiguous case). Outputs the missing
  sides/angles, or a message if the inputs don't form a triangle — including reporting 0, 1, or 2 valid solutions
  for the ambiguous SSA case.
- **`unit_circle_reference.py`** — Evaluates all six trig functions at an angle entered in degrees or radians,
  naming the exact value (like `sqrt(3)/2`) whenever the angle is one of the standard unit-circle angles, and
  reporting the reference angle, quadrant, and sign pattern. Angles outside 0–360° are wrapped first, and
  undefined values (like `tan 90°`) are reported as undefined rather than crashing. Also converts between
  degrees and radians, evaluates inverse trig, and checks the Pythagorean identities numerically.

---

## Geometry (`geometry/`)

| File | Description |
|---|---|
| `shape_geometry_solver.py` | Area and perimeter for common 2D shapes, and volume and surface area for common 3D solids. |

**Course fit:** Geometry, Precalculus, and the mensuration parts of Physics and Chemistry labs.

- **`shape_geometry_solver.py`** — Pick a shape and enter its dimensions. 2D: circle (area and circumference),
  rectangle, and triangle by Heron's formula, which checks the triangle inequality first and says so when three
  lengths cannot form a triangle. 3D: sphere, cylinder, cone, and rectangular prism, each reporting volume and
  total surface area.

---

## Astronomy (`astronomy/`)

| File | Description |
|---|---|
| `orbital_mechanics_calculator.py` | Circular-orbit speed and period, escape velocity, and Kepler's Third Law converting between orbital period and semi-major axis. |

**Course fit:** Intro Astronomy, Physics I (gravitation), Aerospace/orbital-mechanics fundamentals.

- **`orbital_mechanics_calculator.py`** — Menu for orbital speed and period around a central body, escape
  velocity, or Kepler's Third Law (`T²/a³ = 4π²/GM`) in either direction. Uses the standard gravitational
  parameter `GM` (μ) so you don't enter `G` and a mass separately, with presets for Earth, the Moon, and the
  Sun plus a custom option. SI units throughout (meters, seconds, m³/s² for GM); periods are reported in both
  seconds and days.

---

## Biology (`biology/`)

| File | Description |
|---|---|
| `punnett_square_solver.py` | Monohybrid or dihybrid Punnett-square cross calculator: offspring genotype and phenotype ratios from parent genotypes. |
| `hardy_weinberg.py` | Hardy-Weinberg equilibrium: allele frequencies ↔ genotype frequencies, expected counts, and a chi-square test of whether a population is actually in equilibrium. |
| `population_growth.py` | Exponential and logistic population models: population at a time, time to reach a target, doubling time, instantaneous growth rate, and the inflection point at K/2. |
| `dilution_calculator.py` | Solution prep: C1V1 = C2V2 solved for any variable, dilution factors, serial-dilution plans, and molarity/mass/moles conversions. |
| `chi_square_genetics.py` | Chi-square goodness-of-fit test for genetic crosses against 3:1, 9:3:3:1, 1:1, 1:2:1, or a custom ratio, with a built-in critical-value table. |
| `surface_area_volume.py` | Surface-area-to-volume ratios for cell and organism models, the scaling effect on SA:V, Kleiber's-law metabolic rate, and diffusion distance vs time. |

**Course fit:** Intro Biology, Genetics, AP Biology, Ecology, Lab Methods.

- **`punnett_square_solver.py`** — Menu for a monohybrid cross (one gene, e.g. `Aa` x `Aa`) or a dihybrid cross
  (two independently-assorting genes, e.g. `AaBb` x `AaBb`). Enter the letter(s) used for each gene and each
  parent's genotype. Outputs every offspring genotype and phenotype with their ratios (e.g. the classic 1:2:1
  genotype / 3:1 phenotype monohybrid result, or 9:3:3:1 dihybrid phenotype result), assuming simple dominant/
  recessive inheritance where uppercase is the dominant allele.
- **`hardy_weinberg.py`** — Three ways in: from an allele frequency `p` or `q`, from the recessive *phenotype*
  frequency (which is `q²`, the usual exam wording), or from observed genotype counts. Outputs `p`, `q`, and the
  `p²`/`2pq`/`q²` genotype frequencies, the carrier frequency, and expected counts for a given population size.
  The counts path also runs a chi-square test with 1 degree of freedom against the equilibrium expectation and
  says whether to reject equilibrium at the 0.05 level, warning when an expected count below 5 makes the test
  unreliable.
- **`population_growth.py`** — Exponential mode gives `N = N0·e^(rt)` with doubling time (or half-life for a
  negative `r`), and solves for the time to reach a target population. Logistic mode gives
  `N = K/(1 + ((K−N0)/N0)·e^(−rt))` with the percentage of carrying capacity reached, the instantaneous
  `dN/dt = rN(1 − N/K)`, and the inflection time where growth is fastest at `N = K/2`. It refuses targets at or
  above `K` with an explanation rather than returning a nonsense time.
- **`dilution_calculator.py`** — Solves `C1V1 = C2V2` for whichever of the four you're missing, and for the
  common "how much stock do I take" case also reports the diluent to add and the fold-dilution. Additional tools
  compute a dilution factor from either volumes or concentrations, print a full serial-dilution plan (transfer
  volume per tube and the concentration at every step), and convert between molarity, moles, and grams for a
  known molar mass. Units only need to be self-consistent, since the relation is a ratio.
- **`chi_square_genetics.py`** — Pick a Mendelian ratio preset (3:1, 9:3:3:1, 1:1, 1:2:1) or type a custom one
  like `9,3,3,1`, then enter the observed count per category. Prints a per-category table of observed, expected,
  and each contribution to χ², then the total with its degrees of freedom, and compares it against built-in
  critical values at both the 0.05 and 0.01 levels to give a verdict. Warns when the smallest expected count
  drops below 5.
- **`surface_area_volume.py`** — Surface area, volume, and the SA:V ratio for a sphere, cube, cylinder, or
  rectangular box, with a note on the shape's characteristic ratio (`3/r` for a sphere, `6/s` for a cube). The
  scaling tool shows how scaling every length by `k` multiplies area by `k²` and volume by `k³`, dividing SA:V by
  `k` — the reason large organisms need lungs and circulation. Also estimates basal metabolic rate from body mass
  by Kleiber's law (`BMR = a·M^0.75`) including the mass-specific rate, and computes diffusion time from distance
  via `t ≈ x²/(2D)`.

---

## Precalculus (`precalculus/`)

| File | Description |
|---|---|
| `polynomial_analyzer.py` | Polynomial analysis (real zeros, end behavior, intercepts, turning-point count) and rational-function analysis (vertical/horizontal/oblique asymptotes, holes, intercepts). |
| `sequences_series.py` | Arithmetic and geometric sequences and series: nth term, partial sums, common difference/ratio from two terms, infinite geometric sums, and term listings. |
| `log_exp_solver.py` | Logarithm and exponential toolkit: change of base, solving `b^x = c` and `log_b(x) = c`, the log rules worked with your numbers, and growth/decay with half-life and doubling time. |

**Course fit:** Precalculus, College Algebra, Algebra II, AP Precalculus.

- **`polynomial_analyzer.py`** — Enter a degree (1–6) and the coefficients from the highest power down. For a
  polynomial it prints the reconstructed `f(x)`, the leading coefficient, the y-intercept, the end behavior in
  all four cases, the maximum number of zeros and turning points, and the real zeros. Zeros are located
  numerically: the search is bounded by the Cauchy bound `1 + max|aᵢ|/|aₙ|`, sampled across that interval, and
  each sign change is refined by bisection, with an extra check for even-multiplicity roots that touch the axis
  without crossing it. You can then evaluate `f(x)` at any point. Rational mode takes a numerator and a
  denominator and reports vertical asymptotes, holes where a factor cancels, the horizontal asymptote (`y = 0`
  or the ratio of leading coefficients) or the oblique asymptote by polynomial long division when the numerator
  is exactly one degree higher, plus both intercepts.
- **`sequences_series.py`** — Arithmetic tools give `aₙ` and `Sₙ`, recover the common difference and first term
  from any two known terms, and locate where a given value falls in the sequence (saying so when it isn't a term
  at all). Geometric tools give `aₙ` and `Sₙ`, recover the ratio from two terms (flagging when the even power
  admits a negative ratio too), sum an infinite series when `|r| < 1` and explain the divergence when it doesn't,
  and find how many terms it takes to pass a value. A listing mode prints the first n terms alongside a running
  sum.
- **`log_exp_solver.py`** — Evaluates `log_b(x)` by change of base and cross-checks against `ln` and `log10`,
  solves `b^x = c` and `log_b(x) = c`, and demonstrates the product, quotient, and power rules on numbers you
  supply so you can see both sides agree. The growth/decay tool takes `k` directly or derives it from a half-life
  or doubling time, then finds either the amount at a time or the time to reach an amount. Domain restrictions
  are enforced with an explanation — a base of 1, a non-positive base, a non-positive log argument, and
  `b^x = c` with `c ≤ 0` are all rejected in words rather than raising an error.

---

## Finance (`finance/`)

| File | Description |
|---|---|
| `tvm_solver.py` | Time-value-of-money solver: give any four of PV, FV, PMT, N, and rate, and it finds the fifth, with end- or begin-of-period payments. |
| `loan_amortization.py` | Loan amortization: level payment, full or yearly schedule of interest/principal/balance, lifetime totals, and the effect of paying extra. |
| `compound_interest.py` | Compound growth plus APR ↔ APY conversion at any compounding frequency including continuous, and a head-to-head comparison of two accounts. |
| `npv_irr.py` | Capital budgeting on a cash-flow stream: NPV at a chosen rate, IRR, simple and discounted payback, profitability index, and an NPV-vs-rate table. |
| `break_even_margin.py` | Break-even units and revenue, units for a target profit, margin of safety, contribution margin, and margin ↔ markup conversion. |

**Course fit:** Personal Finance, Business Math, Finance 101, Accounting, Economics, Engineering Economics.

- **`tvm_solver.py`** — The standard five-variable TVM relation
  `PV + PMT·annuity + FV·discount = 0` under the usual sign convention (cash out negative, cash in positive).
  Pick the unknown and enter the other four; the rate is per period as a percent, and payments can be
  end-of-period (ordinary annuity) or begin-of-period (annuity due). PV, FV, and PMT have closed forms; the
  number of periods is solved in logs; the rate has no closed form and is found by bisection, which cannot
  diverge the way Newton's method can on a badly-signed cash flow. Zero-rate cases are handled by their limits
  rather than dividing by zero. A 200,000 loan at 0.5%/month for 360 months returns the textbook 1,199.10 payment.
- **`loan_amortization.py`** — Enter the amount, annual rate, term, and payments per year to get the level
  payment, then choose the full payment-by-payment schedule (paused every 12 rows so it doesn't scroll away), a
  year-by-year summary, or totals only. Reports payments made, total paid, and total interest. You can also
  substitute a payment of your own to see how paying extra shortens the loan — and if the payment doesn't cover
  the first month's interest, it says so instead of looping forever on a growing balance.
- **`compound_interest.py`** — Future value for any compounding frequency, with `0` meaning continuous
  compounding, reporting the interest earned and the effective annual rate. Converts a nominal APR to APY and
  back again, and compares two accounts by APY so different compounding frequencies can be ranked honestly —
  showing, for instance, that 5% compounded monthly (5.11619% APY) beats 5.1% compounded annually.
- **`npv_irr.py`** — Enter the cash flow at time 0 (an investment is negative) then each later period's, up to
  40 flows. Reports NPV at your discount rate with an accept/reject reading, the IRR by bisection, simple and
  discounted payback interpolated within the crossing period, and the profitability index. It counts sign changes
  in the stream and warns when more than one means multiple IRRs may exist and NPV should be trusted instead —
  and says plainly when a stream never changes sign and therefore has no IRR at all. An optional table sweeps NPV
  against rate from 0% to 30%.
- **`break_even_margin.py`** — Break-even in units and revenue from price, variable cost, and fixed costs, plus
  the contribution margin and its ratio; the volume needed to hit a target profit; and the margin of safety
  against expected sales with the resulting profit. A fourth tool converts between gross margin (percent of
  price) and markup (percent of cost) in both directions — the pair students most often mix up. When price does
  not exceed variable cost it explains that no volume ever breaks even rather than returning a negative
  quantity.

---

## Thermodynamics & Materials (`thermo_materials/`)

| File | Description |
|---|---|
| `ideal_gas_processes.py` | Work, heat, and internal-energy change for isothermal, isobaric, isochoric, and adiabatic ideal-gas processes, plus a PV = nRT state solver. |
| `carnot_efficiency.py` | Carnot and actual heat-engine efficiency, refrigerator and heat-pump COP, a second-law sanity check, and a temperature converter. |
| `stress_strain.py` | Axial stress, strain, Young's modulus, deformation `δ = FL/(AE)`, factor of safety, Poisson's ratio, and a material property table. |
| `thermal_expansion.py` | Linear, area, and volume thermal expansion, thermal stress in a restrained member, expansion gaps, and bimetallic-strip mismatch. |

**Course fit:** Thermodynamics, Physics II, Materials Science, Statics & Mechanics of Materials, Chemistry (gas laws).

- **`ideal_gas_processes.py`** — All four standard processes in SI units, using the convention that work done *by*
  the gas is positive and `dU = Q − W`. Isothermal uses `W = nRT·ln(V2/V1)` with `dU = 0`; isobaric uses
  `W = P·ΔV` and derives both temperatures from the state equation; isochoric reports `W = 0` with `Q = dU`; and
  adiabatic uses `PV^γ = const` to get `P2` and `W = (P1V1 − P2V2)/(γ − 1)` with `Q = 0`. Molar heat capacity can
  be taken as monatomic (3/2·R), diatomic (5/2·R), or entered directly, and each result says in words whether the
  gas expanded and did work or was compressed. A fifth menu item solves `PV = nRT` for any single variable.
- **`carnot_efficiency.py`** — Carnot efficiency `1 − Tc/Th` with the maximum work and rejected heat for a given
  heat input, and actual efficiency from either `Qh` and `W` or `Qh` and `Qc`. Given the reservoir temperatures
  it compares the real cycle against the Carnot limit, reporting what fraction of the limit was reached and
  flagging a cycle that claims to beat it as impossible. Refrigerator COP (`Tc/(Th−Tc)`) and heat-pump COP
  (`Th/(Th−Tc)`) come with the minimum work for a given load. Temperatures must be absolute, and a converter is
  included for Celsius and Fahrenheit.
- **`stress_strain.py`** — Normal stress `σ = F/A`, normal strain `ε = ΔL/L0` (from either a change in length or
  a pair of lengths, also reported in percent and microstrain), Young's modulus `E = σ/ε`, and axial deformation
  `δ = FL/(AE)` with the resulting strain, stress, and final length. Cross-sectional area can be entered
  directly or computed from a diameter or a width × height. Factor of safety compares a yield or ultimate
  strength against the actual stress and interprets the result. Poisson's ratio gives the lateral strain and the
  change in a transverse dimension. Every pressure is printed in Pa, MPa, and GPa at once, and a reference table
  lists typical `E` and yield values for six common materials.
- **`thermal_expansion.py`** — Linear (`ΔL = αL0ΔT`), area (`ΔA = 2αA0ΔT`, noting that holes expand exactly like
  solid material), and volume (`ΔV = βV0ΔT` with `β = 3α` for a solid) expansion, with α entered directly or
  picked from a built-in material list. Thermal stress in a member held between rigid supports uses
  `σ = E·α·ΔT` — length cancels — and says whether heating puts it in compression or cooling puts it in tension,
  optionally converting to a force on the supports. Also sizes the expansion gap needed per joint for a run of
  rails or pipe, and computes the mismatch that makes a bimetallic strip bend, naming which way it curves.

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

## Hardware Compatibility: check for "Python" before you buy

**These programs require a TI-84 Plus CE _Python Edition_, or a TI-84 Plus CE with TI's Python App installed.**
A TI-84 Plus CE without Python cannot run them at all.

This is worth stating loudly because the hardware situation changed. Texas Instruments **discontinued the
TI-84 Plus CE Python on 2026-04-27**, and the plain TI-84 Plus CE that TI currently sells does **not** include
Python. TI has named the **TI-84 Evo** as the successor model. A calculator bought new today under the
"TI-84 Plus CE" name may therefore be a unit that cannot run any of this.

Before buying hardware:

- Look for the word **"Python"** printed on the calculator's faceplate or bezel.
- Or switch it on and check that a **Python** app appears in the Apps list.
- If you already own a TI-84 Plus CE without Python, check TI's site for the Python App for your model and OS
  version before assuming these will run.

### The three variants people ask about

| Calculator | Runs these? | How you install |
|---|---|---|
| **TI-84 Plus CE _Python Edition_** | Yes — the model this library is written and tested for | `.8xv` drag-and-drop via TI Connect™ CE |
| **Plain TI-84 Plus CE** | Only if TI's Python App is installed; new units ship without it | Same as above, once Python is present |
| **TI-84 Evo** | Expected to, but not hardware-verified — see below | `.py` files via <https://connectevo.ti.com>; `.8xv` will **not** work |

**On the TI-84 Evo.** Every Evo ships with Python built in, so there is no "Python Edition" variant to look for.
Two things do change, though. The Evo uses a **new AppVar format (`.8xv2`)**, so the `.8xv` files in [`8xv/`](8xv/)
will not transfer to it, and **TI Connect CE does not connect to an Evo at all** — transfers go through TI's web
app at <https://connectevo.ti.com>. The `.py` sources are the portable asset and are what an Evo owner uses; see
[Transferring to a TI-84 Evo](#transferring-to-a-ti-84-evo).

A static audit of all 52 programs found that they import only `math`, `random` and `time`, that the two programs
touching TI-specific modules (`ti_system`, `ti_plotlib`) guard those imports with `try`/`except ImportError` and
working text fallbacks, and that none hardcode pixel coordinates against the CE's screen. TI documents `math`,
`random` and `time` as present on the Evo. On that basis these programs are **expected** to run on an Evo with no
changes — but **none of them have been run on Evo hardware**, so that is an expectation, not a tested claim, and
this README will not state otherwise until a test pass exists. Background and sources:
[`business/EVO_TRANSITION.md`](business/EVO_TRANSITION.md).

They do **not** run on the TI-83 Plus, the monochrome TI-84 Plus, the TI-84 Plus Silver Edition, the TI-Nspire
family, or any Casio or HP calculator.

## Transferring to Your Calculator (TI-84 Plus CE family)

Install **TI Connect™ CE** and connect your TI-84 Plus CE Python Edition over USB, then pick either route:

- **Ready-made AppVars.** Drag files from [`8xv/`](8xv/) onto TI Connect CE's Calculator Explorer. These are
  already in the calculator's native Python AppVar format, so no conversion step is needed. Each file is named
  after the name it installs as, e.g. `8xv/algebra_linear_stats/QUAD.8xv` shows up as `QUAD` — which is also
  the banner the program prints when you run it.
- **Source files.** Drag the `.py` files instead and TI Connect CE converts them as it sends — or type a program
  straight into the on-calculator Python editor.

Then run programs from the calculator's Python App shell by selecting the program and pressing the Run option.

## Transferring to a TI-84 Evo

The Evo route shares nothing with the CE route: different cable, different software, different file format. Do not
try to use TI Connect CE, and do not use the files in [`8xv/`](8xv/) — the Evo cannot read them.

You need a **USB-C cable**, **Google Chrome** (the tool relies on WebUSB, which Safari and Firefox do not support),
and an **internet connection**, since the transfer tool is a web app with no offline mode.

1. Open <https://connectevo.ti.com> in Chrome. Nothing to install, no sign-in.
2. Connect the Evo over USB-C and grant Chrome access to the device when prompted.
3. Choose **Send Files** and select the `.py` files you want. TI Connect Evo converts each `.py` into the Evo's own
   Python format as it sends, so no conversion is needed on your side.
4. Open **Python** on the calculator, pick the program and run it.

Typing a program in by hand on the calculator's own Python editor also works, exactly as it does on the CE.

Two caveats worth knowing. Bulk-sending ~50 files through the web tool has not been tested here, so if you are
preparing a classroom set, expect to verify that workflow yourself. And any keystroke-level instruction or
screenshot in this repository was produced on a TI-84 Plus CE — the Evo's keypad was substantially rearranged, so
keys may not be where CE instructions say they are.

### Back up before Press-to-Test

**Entering Press-to-Test (exam mode) deletes these programs, and they do not come back.**

TI documents that entering Press-to-Test deletes *"All variables stored in RAM and in archived memory,"* and
TI's Press-to-Test Guidebook states that *"Other variables stored in RAM and in archived memory (including
AppVars) are deleted."* Python programs on the CE Python are stored as Python AppVars. Unlike Apps and TI-BASIC
programs — which Press-to-Test only *disables*, restoring them when you exit exam mode — **Python AppVars are
deleted outright and are not restored.**

A full **All-Memory reset** does the same, and additionally removes the **Python App itself**, which then has to
be re-installed with TI Connect™ CE before anything here will run.

The workaround takes about two minutes: keep a copy of the `.py` or `.8xv` files on your computer *before*
entering exam mode or resetting, then re-send them afterwards. Everything in this repository is that backup.

## Storage Budget: the full library does not fit at once

The 52 programs come to roughly **247 KB of `.py` source** and **243 KB of `.8xv` AppVars**. A TI-84 Plus CE
Python holds about **50 KB of Python across at most 100 programs**. So the library is roughly five times what
the calculator can hold — by design.

This is a library to install *from*, one course at a time, not a payload to load in one go.

**By subject folder** — every one of these fits inside the ~50 KB budget:

| Subject folder | Programs | AppVar size |
|---|---|---|
| `algebra_linear_stats/` | 8 | 30.8 KB |
| `physics_engineering/` | 8 | 26.8 KB |
| `chemistry_and_exam_tools/` | 7 | 29.1 KB |
| `biology/` | 6 | 34.0 KB |
| `calculus/` | 5 | 15.3 KB |
| `finance/` | 5 | 28.1 KB |
| `thermo_materials/` | 4 | 27.5 KB |
| `precalculus/` | 3 | 23.1 KB |
| `trigonometry/` | 2 | 13.6 KB |
| `computer_science/` | 1 | 4.0 KB |
| `differential_equations/` | 1 | 4.0 KB |
| `geometry/` | 1 | 3.9 KB |
| `astronomy/` | 1 | 3.3 KB |
| **Total** | **52** | **243.5 KB** |

**By sellable bundle** — most fit; the two largest do not, and that is stated on their listings rather than
discovered after purchase:

| Bundle | Programs | AppVar size | Fits in ~50 KB? |
|---|---|---|---|
| Calculus & Differential Equations | 6 | 19.3 KB | yes |
| Free Starter Pack | 5 | 22.3 KB | yes |
| Statistics, Probability & Discrete Math | 5 | 23.4 KB | yes |
| Finance & Business Math | 5 | 28.1 KB | yes |
| Chemistry & Exam Tools | 7 | 29.1 KB | yes |
| Biology & Lab Science | 6 | 34.0 KB | yes |
| Physics & Engineering | 13 | 57.6 KB | **no — install per course** |
| Algebra, Precalculus & Trigonometry | 11 | 57.8 KB | **no — install per course** |
| Complete Toolkit | 52 | 243.5 KB | **no — install per course** |

The two 11–13 program bundles are deliberately broad: Physics & Engineering spans mechanics, circuits, fluids,
thermodynamics and materials, which in practice are three or four different semesters. Nobody needs all
thirteen at once. Install the six or seven for the course you are actually taking, then archive or delete them
when it ends, per the on-calculator memory management prompts.

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

---

## Quality Assurance (`qa/`)

Every program in this library is checked by an automated harness that lives in
[`qa/`](qa/). It runs on desktop Python 3 with no third-party dependencies, and
has three layers:

- **A strict TI environment simulator** (`qa/ti_runner.py`) that executes a
  program with `math`, `random`, and `time` cut down to only the names TI's
  build actually ships, and with the built-ins narrowed to TI's documented set.
  A program that reaches for `math.factorial`, `math.log10`, `random.shuffle`,
  or `str.ljust` fails here the same way it would fail on the calculator,
  instead of quietly passing on a desktop.
- **A static checker** (`qa/static_check.py`) that parses every file and flags
  unavailable imports and attributes, syntax newer than the calculator's
  CircuitPython base, direct recursion, literals or `range()` bounds above the
  100-element cap, and reports each file's byte size and the library total.
- **A stdin-driven functional harness** (`qa/harness.py` with `qa/cases.py` and
  `qa/cases_new.py`) that feeds scripted keystrokes to each program inside the
  simulator and asserts on the printed output. Expected values are hand-computed
  and the derivation is written in a comment above each group, so the arithmetic
  can be re-checked independently of the code it is testing.

Current status: **52/52 programs load cleanly** under the simulator, **0 static
errors**, and **212/212 functional cases pass**. See [`qa/README.md`](qa/README.md)
for how to run it and how to add cases as the library grows.

---

AP®, Advanced Placement®, SAT®, PSAT™, and CLEP® are trademarks registered by the College Board, which is not
affiliated with, and does not endorse, this product. PSAT/NMSQT® is a registered trademark of the College Board
and the National Merit Scholarship Corporation, which are not affiliated with, and do not endorse, this product.
ACT® and WorkKeys® are registered trademarks of ACT Education Corp., which is not affiliated with, and does not
endorse, this product. IB® and International Baccalaureate® are registered trademarks of the International
Baccalaureate Organization, which is not affiliated with, and does not endorse, this product. NCEES® is a
registered trademark of the National Council of Examiners for Engineering and Surveying, which is not affiliated
with, and does not endorse, this product. TI-84 Plus CE Python™, TI Connect™ CE, and Texas Instruments® are
trademarks of Texas Instruments Incorporated, which is not affiliated with, and does not endorse, this product.
TI-84 Evo™ and TI Connect™ Evo are likewise trademarks of Texas Instruments Incorporated, which is not affiliated
with, and does not endorse, this product.
All trademarks are the property of their respective owners. Exam policies are subject to change; verify current
policy with the relevant exam authority.
