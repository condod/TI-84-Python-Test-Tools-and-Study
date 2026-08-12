# On-calc name: TVM
# Program: tvm_solver
# Purpose: Time-value-of-money solver. Given any four of present value
#          (PV), future value (FV), payment (PMT), periodic interest
#          rate, and number of periods (N), solves for the fifth using
#          the standard cash-flow convention
#          PV + PMT*annuity + FV*discount = 0.
# Usage: Pick the unknown from the menu, then enter the other four
#        values. Money flowing OUT of your pocket is negative and money
#        coming IN is positive (a loan you receive is +PV with -PMT).
#        Rate is entered as a percent PER PERIOD (0.5 = 0.5%/month).
#        Choose end-of-period (ordinary annuity) or begin-of-period
#        (annuity due) payments. The rate solve uses bisection.

from math import log

MAX_PERIODS = 1200
TINY = 1e-12


def money(value):
    # Fixed 2-decimal text; str.format() is avoided across this library.
    negative = value < 0
    cents = int(round(abs(value) * 100.0))
    text = str(cents // 100) + "." + ("0" + str(cents % 100))[-2:]
    if negative and cents != 0:
        text = "-" + text
    return text


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def get_periods(prompt):
    while True:
        n = get_float(prompt)
        if n <= 0:
            print("Number of periods must be positive.")
            continue
        if n > MAX_PERIODS:
            print("Please keep N at or below " + str(MAX_PERIODS) + ".")
            continue
        return n


def get_timing():
    print("Payment timing: 1 = end of period (ordinary)")
    print("                2 = begin of period (annuity due)")
    choice = input("> ").strip()
    return 1.0 if choice == "2" else 0.0


def annuity_factor(i, n, begin):
    # Present-value factor for n payments of 1 at rate i per period.
    if abs(i) < TINY:
        return n
    return (1.0 - (1.0 + i) ** (-n)) / i * (1.0 + i * begin)


def discount_factor(i, n):
    if abs(i) < TINY:
        return 1.0
    return (1.0 + i) ** (-n)


def residual(i, pv, pmt, fv, n, begin):
    return pv + pmt * annuity_factor(i, n, begin) + fv * discount_factor(i, n)


def solve_rate(pv, pmt, fv, n, begin):
    # Bisection on the residual; no derivative needed and it cannot diverge.
    lo = -0.9999
    hi = 1.0
    f_lo = residual(lo, pv, pmt, fv, n, begin)
    f_hi = residual(hi, pv, pmt, fv, n, begin)
    tries = 0
    while f_lo * f_hi > 0 and tries < 20:
        hi = hi * 2.0
        f_hi = residual(hi, pv, pmt, fv, n, begin)
        tries += 1
    if f_lo * f_hi > 0:
        return None
    for _ in range(100):
        mid = (lo + hi) / 2.0
        f_mid = residual(mid, pv, pmt, fv, n, begin)
        if f_lo * f_mid <= 0:
            hi = mid
            f_hi = f_mid
        else:
            lo = mid
            f_lo = f_mid
    return (lo + hi) / 2.0


def solve_periods(pv, pmt, fv, i, begin):
    if abs(i) < TINY:
        if pmt == 0:
            return None
        return -(pv + fv) / pmt
    k = pmt * (1.0 + i * begin) / i
    denom = fv - k
    if denom == 0:
        return None
    ratio = -(pv + k) / denom
    if ratio <= 0:
        return None
    return -log(ratio) / log(1.0 + i)


def ask_rate():
    return get_float("Rate % per period = ") / 100.0


def main():
    print("=== TVM ===")
    print("Sign convention: cash out is negative,")
    print("cash in is positive.")
    while True:
        print("\nSolve for:")
        print("1. PV (present value)")
        print("2. FV (future value)")
        print("3. PMT (payment)")
        print("4. N (number of periods)")
        print("5. Rate per period")
        print("0. Quit")
        choice = input("> ").strip()

        if choice == "0":
            break
        if choice not in ("1", "2", "3", "4", "5"):
            print("Invalid choice.")
            continue

        try:
            if choice == "1":
                pmt = get_float("PMT = ")
                fv = get_float("FV = ")
                n = get_periods("N (periods) = ")
                i = ask_rate()
                begin = get_timing()
                pv = -(pmt * annuity_factor(i, n, begin) +
                       fv * discount_factor(i, n))
                print("\nPV = " + money(pv))

            elif choice == "2":
                pv = get_float("PV = ")
                pmt = get_float("PMT = ")
                n = get_periods("N (periods) = ")
                i = ask_rate()
                begin = get_timing()
                d = discount_factor(i, n)
                if d == 0:
                    print("\nCannot solve with those values.")
                    continue
                fv = -(pv + pmt * annuity_factor(i, n, begin)) / d
                print("\nFV = " + money(fv))

            elif choice == "3":
                pv = get_float("PV = ")
                fv = get_float("FV = ")
                n = get_periods("N (periods) = ")
                i = ask_rate()
                begin = get_timing()
                a = annuity_factor(i, n, begin)
                if a == 0:
                    print("\nCannot solve with those values.")
                    continue
                pmt = -(pv + fv * discount_factor(i, n)) / a
                print("\nPMT = " + money(pmt))

            elif choice == "4":
                pv = get_float("PV = ")
                pmt = get_float("PMT = ")
                fv = get_float("FV = ")
                i = ask_rate()
                begin = get_timing()
                n = solve_periods(pv, pmt, fv, i, begin)
                if n is None or n <= 0:
                    print("\nNo positive number of periods fits those values.")
                    print("Check the signs: cash out must be negative.")
                    continue
                print("\nN = " + str(round(n, 4)) + " periods")

            else:
                pv = get_float("PV = ")
                pmt = get_float("PMT = ")
                fv = get_float("FV = ")
                n = get_periods("N (periods) = ")
                begin = get_timing()
                i = solve_rate(pv, pmt, fv, n, begin)
                if i is None:
                    print("\nNo rate fits those values.")
                    print("Check the signs: cash out must be negative.")
                    continue
                print("\nRate = " + str(round(i * 100.0, 6)) + " % per period")
                print("Annual (x12) = " + str(round(i * 1200.0, 6)) + " %")
        except (ValueError, OverflowError, ZeroDivisionError):
            print("Could not compute with those values.")

    print("Bye.")


main()
