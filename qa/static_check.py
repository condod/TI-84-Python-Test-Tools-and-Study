"""Static on-device-viability checker for TI-84 Plus CE Python programs.

Checks each .py file for:
  * syntax (py_compile) and AST parse
  * imports outside the TI-available module set
  * math/random names that TI's build does NOT ship (factorial, log10, shuffle, ...)
  * string methods MicroPython/CircuitPython does not implement (ljust/rjust/...)
  * built-ins outside TI's documented built-ins table (open, reversed, ...)
  * syntax features newer than TI's CircuitPython base (f-strings, walrus, match)
  * direct recursion
  * literal lists / range() bounds above the 100-element on-device cap
  * file byte size, for the ~50 KB storage budget
"""

import ast
import os
import py_compile
import sys
import tempfile

from ti_runner import TI_MATH, TI_RANDOM, TI_BUILTINS

TI_MODULES = {"math", "random", "time", "ti_system", "ti_plotlib",
              "ti_hub", "ti_rover"}

# math names people reach for that TI's math module does not have
MATH_MISSING = {
    "factorial", "log10", "log2", "hypot", "gcd", "lcm", "comb", "perm",
    "dist", "sinh", "cosh", "tanh", "asinh", "acosh", "atanh", "erf", "erfc",
    "gamma", "lgamma", "inf", "nan", "tau", "isqrt", "prod", "remainder",
    "expm1", "log1p", "nextafter", "ulp", "cbrt", "exp2",
}
RANDOM_MISSING = {"shuffle", "sample", "choices", "gauss", "normalvariate",
                  "expovariate", "betavariate", "triangular", "vonmisesvariate",
                  "paretovariate", "weibullvariate", "lognormvariate",
                  "gammavariate", "randbytes"}

# str methods absent from MicroPython/CircuitPython builds
STR_MISSING = {"ljust", "rjust", "zfill", "casefold", "expandtabs",
               "isnumeric", "isdecimal", "isalnum", "istitle", "swapcase",
               "title", "removeprefix", "removesuffix", "maketrans",
               "translate", "rindex", "splitlines", "format_map"}

# "complex" is deliberately NOT in this set. It is missing from the appendix
# "Selected TI-Python Built-in..." table, but that table says outright that it
# is not exhaustive, and TI's programming guide documents complex(real, imag)
# as Module: Built-in, puts it on [Fns...] > Type > 5, documents .real/.imag,
# and gives the keypad an imaginary-j key. cmath is the part that is absent.
BUILTIN_MISSING = {"open", "reversed", "frozenset", "vars",
                   "format", "compile", "breakpoint", "bytes_", "delattr",
                   "aiter", "anext", "exit", "quit"}

MAX_LIST = 100


class Report:
    def __init__(self, path):
        self.path = path
        self.errors = []
        self.warnings = []
        self.info = []
        self.size = os.path.getsize(path)

    def err(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)


def check_file(path):
    rep = Report(path)

    # 1. compiles at all?
    try:
        with tempfile.TemporaryDirectory() as td:
            py_compile.compile(path, cfile=os.path.join(td, "out.pyc"),
                               doraise=True)
    except py_compile.PyCompileError as exc:
        rep.err("does not compile: " + str(exc).strip())
        return rep

    src = open(path, "r", encoding="utf-8").read()
    tree = ast.parse(src, path)

    star_math = False
    star_random = False

    # Names the module defines itself shadow anything from `import *`, so a
    # locally-defined factorial()/log10() helper is a fix, not a bug.
    local_defs = set()
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            local_defs.add(node.name)
        elif isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name):
                    local_defs.add(tgt.id)

    for node in ast.walk(tree):
        # --- imports ---
        if isinstance(node, ast.Import):
            for al in node.names:
                root = al.name.split(".")[0]
                if root not in TI_MODULES:
                    rep.err("imports unavailable module '" + al.name + "'")
        elif isinstance(node, ast.ImportFrom):
            mod = (node.module or "").split(".")[0]
            if mod not in TI_MODULES:
                rep.err("imports from unavailable module '" + str(node.module) + "'")
            for al in node.names:
                if al.name == "*":
                    if mod == "math":
                        star_math = True
                    if mod == "random":
                        star_random = True
                    continue
                if mod == "math" and al.name not in TI_MATH:
                    rep.err("'from math import " + al.name +
                            "' - not in TI's math module")
                if mod == "random" and al.name not in TI_RANDOM:
                    rep.err("'from random import " + al.name +
                            "' - not in TI's random module")

        # --- attribute access: module.name and str methods ---
        elif isinstance(node, ast.Attribute):
            attr = node.attr
            base = node.value
            if isinstance(base, ast.Name):
                if base.id == "math" and attr in MATH_MISSING:
                    rep.err("math." + attr + "() not available on TI-84 Python")
                if base.id == "random" and attr in RANDOM_MISSING:
                    rep.err("random." + attr + "() not available on TI-84 Python")
            if attr in STR_MISSING:
                rep.err("str." + attr + "() not implemented in "
                        "MicroPython/CircuitPython (TI-84 Python base)")

        # --- bare names from `import *` ---
        elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
            if node.id in local_defs:
                continue
            if node.id in MATH_MISSING and star_math:
                rep.err("uses '" + node.id + "' from `from math import *` "
                        "- not in TI's math module")
            if node.id in RANDOM_MISSING and star_random:
                rep.err("uses '" + node.id + "' - not in TI's random module")
            if node.id in BUILTIN_MISSING:
                rep.err("uses built-in '" + node.id +
                        "' which is not in TI's built-ins table")

        # --- syntax level ---
        elif isinstance(node, ast.JoinedStr):
            rep.err("f-string used; TI's CircuitPython base may not support it")
        elif isinstance(node, ast.NamedExpr):
            rep.err("walrus operator ':=' not supported")
        elif hasattr(ast, "Match") and isinstance(node, ast.Match):
            rep.err("match statement not supported")
        elif isinstance(node, (ast.AsyncFunctionDef, ast.Await)):
            rep.err("async/await not supported")

        # --- oversized literals ---
        elif isinstance(node, (ast.List, ast.Tuple)):
            if len(node.elts) > MAX_LIST:
                rep.err("literal sequence of " + str(len(node.elts)) +
                        " elements exceeds the 100-element cap")

        elif isinstance(node, ast.Call):
            fn = node.func
            if isinstance(fn, ast.Name) and fn.id == "range" and node.args:
                last = node.args[-1] if len(node.args) > 1 else node.args[0]
                if isinstance(last, ast.Constant) and isinstance(last.value, int):
                    if last.value > 5000:
                        rep.warn("range() up to " + str(last.value) +
                                 " may be slow on-device")

    # --- direct recursion ---
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            for sub in ast.walk(node):
                if (isinstance(sub, ast.Call) and isinstance(sub.func, ast.Name)
                        and sub.func.id == node.name):
                    rep.err("function '" + node.name + "' is recursive")

    # --- unbounded `while True:` with no break/return ---
    for node in ast.walk(tree):
        if isinstance(node, ast.While):
            test = node.test
            is_true = isinstance(test, ast.Constant) and test.value is True
            if is_true:
                has_exit = any(isinstance(s, (ast.Break, ast.Return))
                               for s in ast.walk(node))
                if not has_exit:
                    rep.err("`while True:` with no break/return (unbounded loop)")

    return rep


def main(paths):
    files = []
    for p in paths:
        if os.path.isdir(p):
            for root, _dirs, names in os.walk(p):
                if "__pycache__" in root or ".git" in root:
                    continue
                for n in sorted(names):
                    if n.endswith(".py"):
                        files.append(os.path.join(root, n))
        else:
            files.append(p)

    total = 0
    bad = 0
    rows = []
    for f in sorted(files):
        rep = check_file(f)
        total += rep.size
        rows.append(rep)
        rel = os.path.relpath(f)
        if rep.errors or rep.warnings:
            print("--- " + rel)
            for e in rep.errors:
                print("   ERROR:   " + e)
                bad += 1
            for w in rep.warnings:
                print("   WARNING: " + w)

    print("")
    print("SIZE TABLE")
    print("bytes   file")
    for rep in sorted(rows, key=lambda r: -r.size):
        print(str(rep.size).rjust(6) + "  " + os.path.relpath(rep.path))
    print("")
    print("files: " + str(len(rows)) + "   total bytes: " + str(total) +
          "  (" + str(round(total / 1024.0, 1)) + " KB)")
    print("errors: " + str(bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or ["."]))
