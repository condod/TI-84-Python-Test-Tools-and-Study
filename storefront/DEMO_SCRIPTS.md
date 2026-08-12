# Demo & Marketing Content Scripts

Ready-to-shoot short-form video scripts, community post drafts, and the free-pack email
sequence. Everything here is written to be honest: no invented testimonials, no fake
download counts, no exam-legality claims. Where a script needs a number or a personal
detail, it is marked `[YOUR …]` for you to fill in truthfully or cut.

---

## Part 1 — Short-form video scripts

### Production notes (read once, applies to all five)

- **Shoot vertical, 1080×1920.** Phone on a small tripod or propped against books,
  pointing straight down at the calculator on a plain desk. Daylight or a desk lamp
  off to one side. Do not use a ring light directly overhead — the CE's screen is glossy
  and will mirror it.
- **The calculator screen is small.** Punch in with a digital zoom in the edit so the
  screen fills 60–70% of the frame during the demo beats, and put a large on-screen text
  duplicate of any number that matters.
- **First frame is the whole ballgame.** Frame 1 should already show the calculator with
  something on the screen. No logo intro, no "hey guys."
- **Captions burned in, always.** Most viewing is muted.
- **Audio:** your own voice beats a robot voice. If you won't speak, use trending audio at
  low volume and rely on the on-screen text.
- **Length:** aim for the stated target; cutting 5 seconds usually helps.
- **Every video ends with the free pack, not the paid bundle.** The free thing is what
  earns the click; the funnel does the selling.
- **Caption/description template** for all of them:

  > Free 3-program starter pack (unit converter, quadratic solver, stats) — link in bio.
  > Works on TI-84 Plus CE Python Edition only. Study/practice tool — always check your
  > own exam's calculator policy.
  > #ti84 #ti84pluce #calculus #enginerdingstudent #studytok #mathhelp #python

---

### Script 1 — "You already own a Python computer" (≈30 s)

*The awareness video. Most students with a CE Python Edition have never opened the Python
app. This is the widest-reach concept and should be the first one you post.*

| Time | Visual | On-screen text | Voiceover |
|---|---|---|---|
| 0:00–0:03 | Close-up, thumb pressing the `prgm`/apps key, Python app icon visible | **You've had this the whole time** | "If your TI-84 says 'Python Edition' on the front, you own a tiny computer and you've probably never used it." |
| 0:03–0:08 | Open Python app, empty program list | *nothing* | "This is the Python app. Mine was empty for a year." |
| 0:08–0:16 | Scroll a list of ~10 loaded programs | **24 programs I wrote for it** | "So I filled it. Derivatives, matrices, kinematics, gas laws." |
| 0:16–0:26 | Run `quadratic_solver`, type 2, -7, 3, results appear | **x = 3 and x = 0.5** ← big text | "Quadratic with complex-root support. Three keystrokes instead of three lines of algebra I'd get wrong at midnight." |
| 0:26–0:30 | Hold on the result screen | **3 of them free — link in bio** | "Three of them are free. Link's in my bio." |

**Hook alternatives to A/B test:** "Your TI-84 has a Python app you've never opened." /
"Nobody told me the TI-84 could do this." / "POV: you find out in week 12 that your
calculator runs Python."

---

### Script 2 — "3×3 matrix inverse, by hand vs. by program" (≈35 s)

*The tedium video. Strongest conversion concept, because the pain is vivid and universal
in linear algebra. Split-screen contrast does the work.*

| Time | Visual | On-screen text | Voiceover |
|---|---|---|---|
| 0:00–0:04 | Paper covered in a half-finished cofactor expansion, pen tapping | **Inverting a 3×3 by hand: attempt #2** | "Second attempt at this inverse. I've made an arithmetic error somewhere and I don't know where." |
| 0:04–0:10 | Speed-ramp of writing minors, then crossing it out | **9 minors. 9 chances to drop a sign.** | "Nine cofactors, nine chances to drop a minus sign." |
| 0:10–0:14 | Hard cut to the calculator, `matrix_toolkit` menu | **Or:** | *(let the cut land, no VO)* |
| 0:14–0:28 | Enter the same 3×3, pick "inverse," results print row by row | **same matrix** → **inverse, 9 seconds** | "Same matrix. Pick inverse. Type the nine entries. Done — and it tells you if it's singular instead of just producing garbage." |
| 0:28–0:35 | Hold on output beside the paper | **It's the checking that saves you, not the answer** | "I still do it by hand for the practice. I just check it before I hand it in. Free starter pack's in my bio." |

**Why this framing matters:** "check your work" is both the honest use case and the one
that doesn't attract "isn't that cheating?" comments. Lead with it.

---

### Script 3 — "Watch Newton-Raphson converge" (≈25 s)

*The satisfying-visual video. The iteration table filling in is genuinely nice to watch and
this one has the best chance of reaching people outside the student audience.*

| Time | Visual | On-screen text | Voiceover |
|---|---|---|---|
| 0:00–0:03 | Calculator screen, prompt `f(x)?` | **Solve cos(x) = x** | "There's no algebra that solves cos x equals x. So you don't solve it — you converge on it." |
| 0:03–0:08 | Type `cos(x)-x`, then `1` for the guess | **Start with a guess: x = 1** | "Start anywhere near the answer." |
| 0:08–0:20 | Iteration table prints line by line, digits stabilising | **n=1 → 0.7503**<br>**n=2 → 0.7391**<br>**n=3 → 0.73908513** | "One step, two decimal places. Two steps, four. Three steps, ten. It roughly doubles the correct digits every iteration — that's what quadratic convergence looks like." |
| 0:20–0:25 | Final root highlighted | **0.7390851332** | "Full iteration table, on the calculator you already bring to class. Free programs in my bio." |

**Note:** the numbers above are the real convergence of Newton-Raphson on cos(x) − x from
x₀ = 1. Don't fake the table; it converges fast enough to be impressive on its own.

---

### Script 4 — "Projectile motion, plotted on the calculator" (≈40 s)

*The prettiest one. `projectile_motion.py` draws an actual trajectory via `ti_plotlib`,
which reads as impossible to people who think of the TI-84 as a 1990s device.*

| Time | Visual | On-screen text | Voiceover |
|---|---|---|---|
| 0:00–0:04 | Calculator on a physics problem set | **Physics problem sets, every single week** | "Every physics problem set: something gets launched at an angle and you have to find where it lands." |
| 0:04–0:12 | Run the program, enter speed 25, angle 40, height 1.5 | **v = 25 m/s · θ = 40° · h = 1.5 m** | "Speed, angle, launch height." |
| 0:12–0:22 | Text output: time of flight, range, max height | **t = 3.36 s**<br>**range = 64.3 m**<br>**max h = 14.7 m** | "Time of flight, range, max height." |
| 0:22–0:33 | Answer "yes" to the plot prompt; the trajectory draws across the screen | **and it draws it** | "And then it plots the trajectory. On a TI-84. This thing has a graphics library and nobody uses it." |
| 0:33–0:40 | Hold on the curve | **ti_plotlib · 24 programs · 3 free** | "Free starter pack in my bio if you want to try the install." |

*Fill the numbers above with your actual outputs when you shoot — don't publish
placeholder values.*

---

### Script 5 — "Install a program on your TI-84 in 60 seconds" (≈45 s)

*The utility video. This is the one that ranks and keeps getting views, because "how do I
put programs on my TI-84" is an evergreen search. Least exciting, highest long-tail value.*

| Time | Visual | On-screen text | Voiceover |
|---|---|---|---|
| 0:00–0:04 | USB cable plugging into the calculator | **How to put a Python program on a TI-84 Plus CE** | "Fastest way to get a Python program onto a TI-84 Plus CE." |
| 0:04–0:10 | TI Connect CE window on the laptop | **1. TI Connect CE — free from Texas Instruments** | "Download TI Connect CE. It's free from TI, it's the official one." |
| 0:10–0:16 | Explorer window with `.8xv` files visible | **2. Find your `.8xv` file** | "If you've got a `.8xv` file, this takes ten seconds. That's the calculator's own Python format." |
| 0:16–0:26 | Drag the `.8xv` onto the TI Connect CE device window; transfer bar | **3. Drag it onto the calculator. Done.** | "Drag it across. No copy-pasting code, no retyping." |
| 0:26–0:36 | On the calculator, open Python app, program is listed, run it | **4. Python app → Run** | "Python app, it's already there, run it." |
| 0:36–0:45 | Cut to Program Editor showing the `.py` | **Only got a `.py`? Program Editor → New → Python → paste → send** | "If all you've got is a `.py` text file, use the Program Editor instead — new Python file, paste, keep the name under 8 characters, send. Free 3-program pack in my bio if you want something to practise on." |

**Post this one on YouTube as a regular video too, not just as a Short**, with the title
`How to Put Python Programs on a TI-84 Plus CE (TI Connect CE, 2026)`. It will collect
search traffic for years, and every viewer is by definition someone who wants programs.

---

## Part 2 — Community post drafts

**Before posting any of these, read `LAUNCH_PLAN.md` for the per-subreddit rules.** Several
of the obvious communities ban or restrict self-promotion outright, and the free-first
framing below is what makes these postable at all. Never post the same text to two
communities on the same day.

---

### Draft A — the free-tools post (for communities that permit sharing free resources)

> **Title:** I wrote 24 Python programs for the TI-84 Plus CE — here are three of them, free
>
> The CE Python Edition has a full Python environment that, judging by everyone I've asked,
> approximately nobody uses. I spent [YOUR TIMEFRAME] filling mine up, and figured I'd
> share the generally useful ones.
>
> The three free ones:
>
> - **Unit converter** — length, mass, pressure, temperature, energy, from a menu.
> - **Quadratic solver** — discriminant classification, and it handles complex roots
>   properly (`cmath` doesn't exist on-device, so it splits real and imaginary parts by hand).
> - **Descriptive stats** — mean, median, mode, sample and population variance/SD from a
>   list you type in.
>
> Each one ships as both a ready-to-install `.8xv` Python AppVar and the plain `.py` source,
> so you can drag them straight across and still read what they're doing. [LINK]
>
> Things I learned that might save you time if you write your own:
>
> - You get `math`, `random`, `time`, and TI's `ti_system` / `ti_plotlib` / `ti_hub` /
>   `ti_rover`. No `cmath`, no `numpy`.
> - `ti_plotlib` genuinely works and can draw on the screen — this is the most
>   underused thing on the device.
> - Roughly 50 KB and 100 programs of space, and lists cap at 100 elements, so cap any
>   user-entered list yourself or you'll get a memory error mid-run.
> - `eval()` after `from math import *` is TI's own documented pattern for letting a user
>   type a function of x. That's how the calculus ones take `sin(x)+x**2` as input.
>
> Obvious but worth saying: these are homework and practice tools. Loads of exams don't
> allow stored programs and some make you clear memory first — check your own exam's rules
> before you walk in with them.
>
> There are paid bundles of the other 21 if they're useful to you, but the three above are
> free with no email required and that's the point of the post. Happy to answer questions
> about the Python environment; it's poorly documented and I hit most of the walls already.

**Why this works:** the technical detail is the actual value, and it's information you
genuinely have and most readers don't. The paid mention is one sentence, near the end,
after you've given something away. Answer every comment.

---

### Draft B — the answer-a-question comment (highest value-to-risk ratio in the whole plan)

Don't post this. Keep it as a template for when someone asks "how do I get programs on my
TI-84" or "does the CE Python actually do anything useful," which happens constantly.

> The Python app on the CE Python Edition is a real (restricted) Python — you get `math`,
> `random`, `time`, plus TI's own modules. Easiest path:
>
> 1. Install TI Connect CE (free from TI).
> 2. Program Editor → New → Python.
> 3. Paste in the code, keep the name under 8 characters, hit send.
> 4. Open the Python app on the calculator and run it.
>
> For what it's worth, `ti_plotlib` works and will draw graphs from your own program,
> which is the part people don't expect.
>
> If you want something to test the process with, I put three of mine up for free —
> [LINK]. Not trying to spam the thread, just happens to be exactly what you're asking
> about.

**Rules for using this:** only where it directly answers the question, only once per
thread, and always give the complete answer *before* the link so the comment stands on its
own if the link is removed. This single template will outperform every submitted post you
make.

---

### Draft C — Cemetech / ticalc.org project post (enthusiast communities, different norms)

These are programmer communities, not student communities. They will read your code, they
will notice if it's bad, and they are historically cool on commercial calculator software.
Lead with the engineering, publish something genuinely free, and never post a bare
advertisement.

> **Title:** [Project] 24 Python programs for the CE Python Edition — numerical methods,
> physics, chemistry
>
> I've been building out a library of TI-84 Plus CE Python programs, mostly numerical
> methods and course-support tools, and wanted to put it in front of people who'd actually
> critique the code.
>
> Repo: <https://github.com/condod/TI-84-Python-Test-Tools-and-Study>
>
> What's in it: central-difference derivatives, composite Simpson's, Newton-Raphson with a
> full iteration table, two-sided numeric limits, Euler and Heun ODE solvers, 2×2/3×3
> Gaussian elimination with partial pivoting, a 3×3 matrix toolkit, SUVAT and projectile
> motion (with an optional `ti_plotlib` trajectory), series RLC impedance, 3D vector ops,
> gas laws, molar mass, Henderson-Hasselbalch.
>
> Constraints I worked under, in case they're useful to anyone else targeting the CE
> Python environment:
>
> - No `cmath`, so the quadratic solver formats complex conjugate pairs manually from the
>   real and imaginary parts.
> - `ti_plotlib` is available but I guard the import and degrade to text-only output,
>   since not every setup has it.
> - ~50 KB / 100-program storage and a 100-element list cap, so user-entered data is
>   capped explicitly (90 for stats, 20 for vectors) rather than letting the runtime throw.
> - All numeric input goes through `try`/`except` and re-prompts rather than crashing out
>   of the program.
>
> Source is on GitHub and readable. There are paid bundles for people who'd rather have it
> zipped up with an install guide, which I'll mention once and not bring up again — I know
> how this community feels about commercial calculator software, and the code's there
> either way.
>
> Genuinely after critique on the numerics, particularly the step-size defaults on the
> derivative program and whether the Heun implementation is doing anything stupid.

**Norms to respect here:** post in the right subforum, use their file-archive submission
process if you upload anything, respond to technical criticism without getting defensive,
and stick around for other people's threads. A one-and-done promo post is remembered.

---

## Part 3 — Free starter pack email sequence

Three emails, sent from Gumroad Workflows (setup steps in `SETUP_CHECKLIST.md`). Written
to be useful even to someone who never buys anything, because that's what keeps the open
rate high enough for email 3 to work.

Sender name: your real name or the shop name — not "no-reply." Set a real reply-to
address and read the replies; they're your best product feedback and your only source of
honest objections.

---

### Email 1 — immediate, on download

**Subject:** Your 3 TI-84 Python programs (+ the install bit people get stuck on)

**Preview text:** Download link inside, plus the one step that trips everyone up.

> Hi — thanks for grabbing the starter pack.
>
> **Download:** [LINK]
>
> Inside: a unit converter, a quadratic solver and a descriptive-statistics tool — each one
> as both a ready-to-install `.8xv` and the plain `.py` source — plus an install guide.
>
> **The 30-second install**
>
> 1. Install TI Connect CE (free, from Texas Instruments) and plug the calculator in.
> 2. Drag the three `.8xv` files onto the calculator in TI Connect CE.
> 3. Open the Python app on the calculator. They're already there. Run one.
>
> That's it — the `.8xv` files are the calculator's own native Python format, so there's no
> copy-pasting involved. The `.py` files in the same folder are the readable source, in case
> you want to see how they work or change something. If you'd rather install that way:
> Program Editor → New → Python, paste the contents in, and **name it 8 characters or
> fewer** — that's the step people get stuck on, because longer names get truncated and two
> programs end up colliding.
>
> **Quick check:** these need a TI-84 Plus **CE Python Edition**, or a CE with the Python
> app installed. They won't run on a TI-83, an older monochrome TI-84, an Nspire, or a
> Casio. If you're not sure which you have, reply with a photo of the front and I'll tell you.
>
> One thing I say everywhere and will say here too: these are for homework, practice and
> checking your own work. Plenty of exams don't allow stored programs, and some make you
> clear memory beforehand. Check your specific exam's rules with your instructor before
> bringing anything stored into a test.
>
> If something doesn't work, just reply to this email. It comes to me.
>
> — [YOUR NAME]

---

### Email 2 — day 3

**Subject:** The TI-84 feature nobody uses (it draws graphs from your own code)

**Preview text:** ti_plotlib, and why your calculator is more capable than you think.

> Did the three programs install OK? If you hit a wall, reply and tell me where — I've
> probably hit the same one.
>
> Something worth knowing while you've got the Python app open: the CE ships with a
> module called `ti_plotlib`. It lets a Python program draw on the calculator screen —
> axes, lines, points, plotted curves — from your own code, not from the built-in grapher.
>
> Try this. New Python program, paste it, run it:
>
> ```python
> import ti_plotlib as plt
> plt.cls()
> plt.window(-1, 7, -1, 30)
> plt.axes("on")
> for i in range(0, 61):
>     x = i / 10
>     plt.plot(x, x * x, "o")
> plt.show_plot()
> ```
>
> That's y = x² drawn point by point by a program you control. Once you can do that, you
> can plot the output of anything you write — which is how the projectile-motion program
> in the full library sketches its trajectory.
>
> **A few things I wish I'd known earlier:**
>
> - Available modules are `math`, `random`, `time`, plus TI's `ti_system`, `ti_plotlib`,
>   `ti_hub`, `ti_rover`. There is no `numpy` and no `cmath`.
> - You get roughly 50 KB and 100 programs of space. Archive what you're not using.
> - Lists cap at 100 elements — relevant the moment you write anything statistical.
>
> If you want the rest of what I've built, the subject bundles are six programs each and
> the complete toolkit is all 24: [LINK]. No pressure — the three you have are yours
> regardless.
>
> — [YOUR NAME]

*(Verify that plotting snippet on your own device before sending it. Shipping code that
doesn't run is the fastest way to lose the reader.)*

---

### Email 3 — day 7

**Subject:** Which one of these are you actually taking this term?

**Preview text:** Plus 25% off the complete toolkit until [DATE].

> Last one from me for a while.
>
> A week in — did the starter pack turn out useful, or did it sit in your downloads
> folder? Genuinely useful either way to know, and replies come straight to me.
>
> If it was useful, the rest of the library splits by what you're actually enrolled in:
>
> - **Calculus & Differential Equations** — numeric derivatives, Simpson's rule, Taylor
>   series, Newton-Raphson with an iteration table, two-sided limits, Euler/Heun ODEs.
> - **Algebra, Linear Algebra & Stats** — quadratics, vertex analysis, 2×2/3×3 systems,
>   matrix determinant and inverse, descriptive stats, nPr/nCr/binomial.
> - **Physics & Engineering** — SUVAT, projectile motion with a plot, Ohm's law and
>   resistor combining, RLC impedance and resonance, 2D statics, 3D vectors.
> - **Chemistry & Exam Tools** — gas laws, molar mass and stoichiometry, unit conversion,
>   a formula self-quiz drill, a countdown timer with mental-maths practice, pH and buffers.
>
> $14 each, or all 24 in the Complete Toolkit for $35 — which is less than three of the
> subject bundles.
>
> **`STARTER25` takes 25% off the complete toolkit through [DATE].** [LINK]
>
> And if none of it fits what you're studying: reply and tell me what's missing. Several
> of the programs in there exist because somebody asked.
>
> — [YOUR NAME]
>
> *Study and practice tools. Check your own exam's calculator and stored-program policy
> before an exam.*

---

### Sequence notes

- **Don't add a fourth email** unless you have something real to say. A new program, a
  fixed bug, a genuinely new bundle. Cadence-for-its-own-sake burns the list.
- **Segment out buyers** so nobody who already bought the complete toolkit receives the
  day-7 discount for it. Gumroad Workflows can filter on prior purchases.
- **The discount code must actually expire.** A permanent "limited time" offer trains
  people to ignore you, and it's a lie.
- **Track reply rate, not just opens.** Every reply is a support conversation, a possible
  review, and a feature request. At this list size, replies are worth more than open rate.
