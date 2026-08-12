"""TI-84 Plus CE Python environment simulator / program runner.

Usage:  python ti_runner.py <program.py> [--loose]

Executes a TI-84 Python program under a *restricted* interpreter environment
that mirrors the officially documented TI-Python surface:

  math   -> only the names in TI's math module table
  random -> only the names in TI's random module table
  time   -> only monotonic / sleep / struct_time (sleep is a no-op so timer
            programs can be tested without burning wall-clock time)
  builtins -> only the names in TI's built-ins table

ti_plotlib / ti_system are provided as recording stubs only when --device is
passed; otherwise they are absent (so programs must take their ImportError
fallback path, which is what happens on a non-Python TI-84 too).

Anything the program touches outside that surface raises NameError /
AttributeError / ImportError here, exactly as it would on the calculator.
"""

import importlib.machinery
import importlib.util
import sys
import types

# --- names TI documents (education.ti.com "Selected TI-Python ... Module Content") ---

TI_MATH = [
    "e", "pi", "sqrt", "pow", "exp", "log", "cos", "sin", "tan",
    "acos", "asin", "atan", "atan2", "ceil", "copysign", "fabs", "floor",
    "fmod", "frexp", "ldexp", "modf", "isfinite", "isinf", "isnan", "trunc",
    "radians", "degrees",
]

TI_RANDOM = ["seed", "getrandbits", "randrange", "randint", "choice",
             "random", "uniform"]

TI_TIME = ["monotonic", "sleep", "struct_time"]

TI_BUILTINS = """
    __build_class__ __import__ __name__ __repl_print__
    abs all any bin bool bytearray bytes callable chr classmethod dict dir
    divmod enumerate eval exec filter float getattr globals hasattr hash help
    hex id input int isinstance issubclass iter len list locals map max
    memoryview min next object oct ord pow print property range repr round set
    setattr slice sorted staticmethod str sum super tuple type zip Ellipsis
    BaseException ArithmeticError AssertionError AttributeError EOFError
    Exception GeneratorExit ImportError IndentationError IndexError
    KeyboardInterrupt KeyError LookupError MemoryError NameError
    NotImplementedError OSError OverflowError RuntimeError StopIteration
    SyntaxError SystemExit TypeError UnicodeError ValueError ZeroDivisionError
""".split()


def _load_builtin(name):
    """Load a compiled-in module fresh, bypassing sys.modules."""
    spec = importlib.machinery.BuiltinImporter.find_spec(name)
    if spec is None:
        return __import__(name)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _load_source(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def build_restricted_math():
    real = _load_builtin("math")
    mod = types.ModuleType("math")
    for n in TI_MATH:
        setattr(mod, n, getattr(real, n))
    return mod


def build_restricted_random():
    import random as _r
    real = _load_source("_ti_real_random", _r.__file__)
    mod = types.ModuleType("random")
    for n in TI_RANDOM:
        setattr(mod, n, getattr(real, n))
    return mod


def build_restricted_time():
    real = _load_builtin("time")
    mod = types.ModuleType("time")
    mod.monotonic = real.monotonic
    mod.struct_time = real.struct_time
    mod.sleep = lambda _s: None          # keep countdown tests instant
    return mod


def build_stub_plotlib(log):
    mod = types.ModuleType("ti_plotlib")

    def _rec(name):
        def fn(*a, **k):
            log.append(name + str(a))
        return fn

    for n in ("cls", "window", "axes", "labels", "pen", "color", "line",
              "show_plot", "plot", "scatter", "title", "text_at", "grid",
              "auto_window", "lin_reg"):
        setattr(mod, n, _rec(n))
    return mod


def build_stub_system(log):
    mod = types.ModuleType("ti_system")

    def _rec(name):
        def fn(*a, **k):
            log.append(name + str(a))
        return fn

    for n in ("disp_clr", "disp_at", "disp_wait", "disp_cursor", "wait_key",
              "escape", "sleep", "wait", "recall_list", "store_list",
              "recall_RegEQ"):
        setattr(mod, n, _rec(n))
    return mod


def main():
    args = [a for a in sys.argv[1:]]
    device = "--device" in args
    loose = "--loose" in args
    paths = [a for a in args if not a.startswith("--")]
    if not paths:
        print("usage: ti_runner.py <program.py> [--device] [--loose]")
        return 2
    prog = paths[0]

    with open(prog, "r", encoding="utf-8") as fh:
        source = fh.read()

    calls = []
    if not loose:
        # build these while the real stdlib is still intact, then swap in
        r_math = build_restricted_math()
        r_random = build_restricted_random()
        r_time = build_restricted_time()
        sys.modules["math"] = r_math
        sys.modules["random"] = r_random
        sys.modules["time"] = r_time
    if device:
        sys.modules["ti_plotlib"] = build_stub_plotlib(calls)
        sys.modules["ti_system"] = build_stub_system(calls)

    allowed = {}
    import builtins as _b
    for n in TI_BUILTINS:
        if hasattr(_b, n):
            allowed[n] = getattr(_b, n)
    # __import__ must honour our restricted sys.modules entries
    allowed["__import__"] = _b.__import__
    allowed["__name__"] = "__main__"

    glb = {"__name__": "__main__", "__builtins__": allowed if not loose else _b}

    code = compile(source, prog, "exec")
    try:
        exec(code, glb)
    except SystemExit:
        pass
    if device and calls:
        print("[ti_plotlib/ti_system calls: " + str(len(calls)) + "]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
