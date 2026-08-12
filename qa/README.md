# QA Harness

Automated checks for the TI-84 Plus CE Python program library. Desktop Python 3
only — no third-party packages, no calculator required.

The point of this harness is that a program can pass on a desktop and still fail
the moment it is loaded on a calculator, because TI's Python is a cut-down
CircuitPython build. `math.factorial`, `math.log10`, `random.shuffle`, and
`str.ljust`/`rjust` all exist on a desktop and none of them exist on the device.
Running the library under a simulated version of TI's environment catches that
class of bug before a buyer does.

## Running it

From the repository root:

```bash
# 1. Static analysis + size report over every subject folder
python qa/static_check.py calculus algebra_linear_stats physics_engineering \
    chemistry_and_exam_tools differential_equations trigonometry biology \
    computer_science geometry astronomy finance precalculus thermo_materials

# 2. Does every program at least start cleanly under the restricted environment?
python qa/smoke.py calculus algebra_linear_stats physics_engineering \
    chemistry_and_exam_tools differential_equations trigonometry biology \
    computer_science geometry astronomy finance precalculus thermo_materials

# 3. Full functional suite (run from inside qa/ so the case modules import)
cd qa && python harness.py ..
```

`harness.py` takes an optional second argument that filters cases by label or by
program path, which is what you want while iterating on one program:

```bash
cd qa && python harness.py .. finance
cd qa && python harness.py .. "Carnot"
```

Set `SHOW_OUTPUT=1` to dump the full captured session for every failing case.

Exit status is non-zero when anything fails, so all three are CI-friendly.

## The pieces

| File | What it does |
|---|---|
| `ti_runner.py` | Executes one program with `math`, `random`, and `time` reduced to the names TI's build ships, and built-ins narrowed to TI's documented set. `--device` additionally provides stub `ti_system` / `ti_plotlib` modules and logs the calls a program makes into them. |
| `static_check.py` | Parses every file and reports unavailable imports/attributes, string methods MicroPython lacks, syntax newer than the CircuitPython base (f-strings, walrus, `match`), direct recursion, literals or `range()` bounds above the 100-element cap, and per-file plus total byte size. |
| `smoke.py` | Flow-independent check that each program starts, prints its banner, and reaches its first prompt without an import-time or definition-time error. |
| `harness.py` | Runs each case: feeds scripted keystrokes to a program inside the simulator and asserts on substrings of the output. |
| `cases.py` | Cases for the original library. |
| `cases_new.py` | Cases for the finance / biology / precalculus / trigonometry / thermo_materials expansion. |

## Writing a case

```python
# 200,000 loan, 0.5%/month, 360 months.
# A = (1 - 1.005^-360)/0.005 = 166.791614 ; PMT = -200000/A = -1199.10
case("TVM: mortgage payment = -1199.10",
     "finance/tvm_solver.py", "3\n200000\n0\n360\n0.5\n1\n0\n",
     ["PMT = -1199.10"])
```

Arguments are the label, the program path relative to the repository root, the
scripted stdin, a list of substrings that must appear, and optionally a list of
substrings that must *not* appear.

Two conventions matter:

- **Show the arithmetic in a comment.** An expected value copied out of the
  program's own output only proves the program is consistent with itself. Every
  expected number in these files is hand-computed or taken from a known textbook
  result, and the derivation sits directly above the case so a reviewer can
  check it without running anything.
- **End the script with a quit.** Every program in this library sits in a menu
  loop with a `0. Quit` option, so a script that stops after the interesting
  output leaves the program blocked on an empty stdin and raising `EOFError`. A
  trailing `0` exits, and also reads as "not yes" at a `y/n` prompt.

A program crash (any traceback) fails a case automatically, so a case with an
empty expectation list is still a useful "this input must not blow up" test.
