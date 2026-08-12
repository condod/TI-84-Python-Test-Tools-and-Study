"""Automated stdin-driven test harness for the TI-84 Python program library.

Every case feeds a scripted keystroke sequence to a program running inside the
restricted TI environment simulator (ti_runner.py) and asserts on substrings of
the printed output. Expected values are hand-computed or checked against an
independent reference implementation (see reference.py).

  python harness.py <repo-root> [name-filter]
"""

import os
import subprocess
import sys

import cases as case_mod
import cases_new

ALL_CASES = case_mod.CASES + cases_new.CASES

RUNNER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ti_runner.py")


def run_case(repo, prog, stdin, device=False, timeout=60):
    path = os.path.join(repo, prog)
    if not os.path.exists(path):
        return None, "MISSING FILE: " + path
    cmd = [sys.executable, RUNNER, path]
    if device:
        cmd.append("--device")
    try:
        proc = subprocess.run(cmd, input=stdin, capture_output=True, text=True,
                              timeout=timeout,
                              cwd=os.path.dirname(RUNNER))
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT (possible unbounded loop)"
    out = (proc.stdout or "") + (proc.stderr or "")
    return proc.returncode, out


def main():
    repo = sys.argv[1] if len(sys.argv) > 1 else "."
    filt = sys.argv[2] if len(sys.argv) > 2 else ""

    passed = 0
    failed = 0
    failures = []

    for case in ALL_CASES:
        label = case["label"]
        if filt and filt.lower() not in label.lower() and filt.lower() not in case["prog"].lower():
            continue
        rc, out = run_case(repo, case["prog"], case["stdin"],
                           device=case.get("device", False))
        problems = []
        if rc is None:
            problems.append(out)
        else:
            tb = "Traceback (most recent call last)" in out
            if tb and not case.get("allow_traceback"):
                last = [l for l in out.strip().splitlines() if l.strip()][-1]
                problems.append("CRASHED: " + last)
            for want in case.get("expect", []):
                if want not in out:
                    problems.append("missing expected " + repr(want))
            for bad in case.get("reject", []):
                if bad in out:
                    problems.append("unexpected present " + repr(bad))

        if problems:
            failed += 1
            failures.append((label, problems, out))
            print("FAIL  " + label)
            for p in problems:
                print("        " + p)
        else:
            passed += 1
            print("pass  " + label)

    print("")
    print("passed: " + str(passed) + "   failed: " + str(failed))
    if failures and os.environ.get("SHOW_OUTPUT"):
        for label, _p, out in failures:
            print("\n===== " + label + " =====\n" + out)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
