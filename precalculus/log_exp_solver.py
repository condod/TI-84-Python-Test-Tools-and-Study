# On-calc name: LOGEXP
# Program: log_exp_solver
# Purpose: Logarithm and exponential toolkit. Evaluates a log to any
#          base by change of base, solves b^x = c and log_b(x) = c,
#          expands the log rules with worked numbers, and handles
#          exponential growth/decay including half-life and doubling
#          time.
# Usage: Pick a tool from the menu. Bases must be positive and not 1,
#        and log arguments must be positive -- the program checks both
#        and explains the domain instead of raising an error. The
#        calculator's math module has log() but no log10(), so base-10
#        logs here are computed as log(x)/log(10).

from math import log, exp

LN10 = log(10.0)
LN2 = log(2.0)


def log10(x):
    return log(x) / LN10


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def get_base(prompt):
    while True:
        base = get_float(prompt)
        if base <= 0:
            print("The base must be positive.")
            continue
        if abs(base - 1.0) < 1e-12:
            print("The base cannot be 1.")
            continue
        return base


def get_positive(prompt):
    while True:
        value = get_float(prompt)
        if value <= 0:
            print("That value must be positive.")
            continue
        return value


def evaluate_log():
    base = get_base("Base b = ")
    x = get_positive("Argument x (must be > 0) = ")
    result = log(x) / log(base)
    print("\nlog_" + str(round(base, 6)) + "(" + str(round(x, 6)) + ") = " +
          str(round(result, 6)))
    print("Change of base: ln(x)/ln(b) = " + str(round(log(x), 6)) + " / " +
          str(round(log(base), 6)))
    print("\nFor reference:")
    print("  ln(x)    = " + str(round(log(x), 6)))
    print("  log10(x) = " + str(round(log10(x), 6)))
    print("Check: b^result = " + str(round(base ** result, 6)))


def solve_exponential():
    print("\nSolve b^x = c for x.")
    base = get_base("Base b = ")
    c = get_float("c = ")
    if c <= 0:
        print("\nb^x is always positive for a positive base,")
        print("so there is no real solution when c <= 0.")
        return
    x = log(c) / log(base)
    print("\nx = log_b(c) = ln(c)/ln(b) = " + str(round(x, 6)))
    print("Check: " + str(round(base, 6)) + "^" + str(round(x, 6)) + " = " +
          str(round(base ** x, 6)))


def solve_logarithmic():
    print("\nSolve log_b(x) = c for x.")
    base = get_base("Base b = ")
    c = get_float("c = ")
    x = base ** c
    print("\nx = b^c = " + str(round(x, 6)))
    print("Check: log_b(x) = " + str(round(log(x) / log(base), 6)))


def log_rules():
    print("\nLog rules demonstrated with your numbers.")
    base = get_base("Base b = ")
    m = get_positive("m (must be > 0) = ")
    n = get_positive("n (must be > 0) = ")
    log_m = log(m) / log(base)
    log_n = log(n) / log(base)

    print("\nlog_b(m) = " + str(round(log_m, 6)))
    print("log_b(n) = " + str(round(log_n, 6)))
    print("\nProduct rule:")
    print("  log_b(m*n) = " + str(round(log(m * n) / log(base), 6)))
    print("  log_b m + log_b n = " + str(round(log_m + log_n, 6)))
    print("Quotient rule:")
    print("  log_b(m/n) = " + str(round(log(m / n) / log(base), 6)))
    print("  log_b m - log_b n = " + str(round(log_m - log_n, 6)))
    power = get_float("Power p for the power rule = ")
    print("Power rule:")
    if m > 0:
        print("  log_b(m^p) = " + str(round(log(m ** power) / log(base), 6)))
        print("  p * log_b m = " + str(round(power * log_m, 6)))


def growth_decay():
    print("\nA = A0 * e^(k*t)")
    a0 = get_positive("Initial amount A0 = ")
    print("1. I know the rate k")
    print("2. I know the half-life")
    print("3. I know the doubling time")
    choice = input("> ").strip()

    if choice == "1":
        k = get_float("Rate k (negative for decay) = ")
    elif choice == "2":
        half = get_positive("Half-life = ")
        k = -LN2 / half
        print("k = -ln(2)/half-life = " + str(round(k, 8)))
    elif choice == "3":
        double = get_positive("Doubling time = ")
        k = LN2 / double
        print("k = ln(2)/doubling time = " + str(round(k, 8)))
    else:
        print("Invalid choice.")
        return

    print("\n1. Find the amount at a time t")
    print("2. Find the time to reach an amount")
    what = input("> ").strip()

    if what == "1":
        t = get_float("Time t = ")
        amount = a0 * exp(k * t)
        print("\nA(" + str(round(t, 6)) + ") = " + str(round(amount, 6)))
        print("Fraction remaining = " + str(round(amount / a0, 6)))
    elif what == "2":
        target = get_positive("Target amount A = ")
        if k == 0:
            print("\nWith k = 0 the amount never changes.")
            return
        t = log(target / a0) / k
        print("\nt = ln(A/A0)/k = " + str(round(t, 6)))
    else:
        print("Invalid choice.")
        return

    if k > 0:
        print("Doubling time = " + str(round(LN2 / k, 6)))
    elif k < 0:
        print("Half-life = " + str(round(-LN2 / k, 6)))


def main():
    print("=== LOGEXP ===")
    while True:
        print("\n1. Evaluate log_b(x)")
        print("2. Solve b^x = c")
        print("3. Solve log_b(x) = c")
        print("4. Log rules with numbers")
        print("5. Growth / decay & half-life")
        print("0. Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                evaluate_log()
            elif choice == "2":
                solve_exponential()
            elif choice == "3":
                solve_logarithmic()
            elif choice == "4":
                log_rules()
            elif choice == "5":
                growth_decay()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except (ValueError, OverflowError, ZeroDivisionError):
            print("Could not compute with those values.")
    print("Bye.")


main()
