"""Flow-independent on-device viability smoke test.

Runs every program under the restricted TI environment simulator with empty
stdin. A program that is safe to load on the calculator will get as far as
printing its banner and then die on EOFError (no more keystrokes) - that is a
PASS. Anything that dies with ImportError / NameError / AttributeError /
TypeError instead never even reached the first prompt, which is exactly what
would happen on the calculator: a hard crash on launch.

This does not depend on knowing each program's prompt order, so it can be
pointed at programs written by anyone.

  python smoke.py <dir-or-file> [...]
"""

import os
import subprocess
import sys

RUNNER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ti_runner.py")

FATAL = ("ImportError", "ModuleNotFoundError", "NameError", "AttributeError",
         "TypeError", "SyntaxError", "IndentationError", "KeyError",
         "IndexError", "ZeroDivisionError", "OverflowError", "MemoryError",
         "RecursionError")


def collect(paths):
    out = []
    for p in paths:
        if os.path.isdir(p):
            for root, _d, names in os.walk(p):
                if "__pycache__" in root or ".git" in root:
                    continue
                for n in sorted(names):
                    if n.endswith(".py"):
                        out.append(os.path.join(root, n))
        elif p.endswith(".py"):
            out.append(p)
    return sorted(out)


def main(paths):
    files = collect(paths)
    ok = 0
    bad = []
    for f in files:
        try:
            proc = subprocess.run([sys.executable, RUNNER, f], input="",
                                  capture_output=True, text=True, timeout=60,
                                  cwd=os.path.dirname(RUNNER))
            out = (proc.stdout or "") + (proc.stderr or "")
        except subprocess.TimeoutExpired:
            bad.append((f, "TIMEOUT - runs without waiting for input?"))
            continue

        lines = [l.strip() for l in out.strip().splitlines() if l.strip()]
        last = lines[-1] if lines else ""
        exc = last.split(":")[0].strip()

        if exc in FATAL:
            bad.append((f, last))
        else:
            ok += 1

    for f, why in bad:
        print("FAIL  " + os.path.relpath(f) + "\n        " + why)
    print("")
    print("loadable: " + str(ok) + " / " + str(len(files)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or ["."]))
