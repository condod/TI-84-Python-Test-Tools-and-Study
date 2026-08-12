# On-calc name: POLYFUNC
# Program: polynomial_analyzer
# Purpose: Analyze a polynomial or a rational function. For a
#          polynomial (degree 1-6) it reports the y-intercept, end
#          behavior, real zeros found by bracketing and bisection, and
#          can evaluate the function at a point. For a rational
#          function it reports vertical asymptotes, the horizontal or
#          oblique asymptote, holes, and intercepts.
# Usage: Enter the degree, then the coefficients from the highest power
#        down to the constant (for 2x^2 - 3x + 1 enter 2, -3, 1). Real
#        zeros are located numerically inside the Cauchy bound
#        1 + max|a_i|/|a_n|, so repeated roots that never cross the
#        axis (like x^2) are reported as touch points where found.

MAX_DEGREE = 6
SAMPLES = 400
TINY = 1e-9


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def get_degree(prompt):
    while True:
        try:
            n = int(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a whole number.")
            continue
        if n < 1 or n > MAX_DEGREE:
            print("Degree must be between 1 and " + str(MAX_DEGREE) + ".")
            continue
        return n


def read_coefficients(degree, label):
    print("\n" + label + " coefficients, highest power first:")
    coefficients = []
    for power in range(degree, -1, -1):
        coefficients.append(get_float("  x^" + str(power) + " coeff = "))
    if coefficients[0] == 0:
        print("Leading coefficient cannot be 0; using 1 instead.")
        coefficients[0] = 1.0
    return coefficients


def evaluate(coefficients, x):
    # Horner's method: fewer multiplications and better rounding behaviour.
    total = 0.0
    for c in coefficients:
        total = total * x + c
    return total


def describe(coefficients):
    degree = len(coefficients) - 1
    text = ""
    for i, c in enumerate(coefficients):
        power = degree - i
        if c == 0:
            continue
        if text != "":
            text += " + " if c > 0 else " - "
            shown = abs(c)
        else:
            text += "" if c > 0 else "-"
            shown = abs(c)
        if power == 0:
            text += str(round(shown, 6))
        else:
            if abs(shown - 1.0) > TINY:
                text += str(round(shown, 6))
            text += "x"
            if power > 1:
                text += "^" + str(power)
    return text if text != "" else "0"


def cauchy_bound(coefficients):
    lead = abs(coefficients[0])
    biggest = 0.0
    for c in coefficients[1:]:
        if abs(c) > biggest:
            biggest = abs(c)
    if lead == 0:
        return 10.0
    bound = 1.0 + biggest / lead
    if bound > 1000.0:
        bound = 1000.0
    return bound


def bisect(coefficients, lo, hi):
    f_lo = evaluate(coefficients, lo)
    for _ in range(80):
        mid = (lo + hi) / 2.0
        f_mid = evaluate(coefficients, mid)
        if f_lo * f_mid <= 0:
            hi = mid
        else:
            lo = mid
            f_lo = f_mid
    return (lo + hi) / 2.0


def find_roots(coefficients):
    bound = cauchy_bound(coefficients)
    step = 2.0 * bound / SAMPLES
    roots = []
    x = -bound
    previous = evaluate(coefficients, x)
    if abs(previous) < TINY:
        roots.append(x)
    for _ in range(SAMPLES):
        nxt = x + step
        value = evaluate(coefficients, nxt)
        if abs(value) < TINY:
            roots.append(nxt)
        elif previous * value < 0:
            roots.append(bisect(coefficients, x, nxt))
        else:
            # A minimum that just touches zero (even multiplicity root).
            mid = (x + nxt) / 2.0
            mid_value = evaluate(coefficients, mid)
            if (abs(mid_value) < abs(previous) and abs(mid_value) < abs(value)
                    and abs(mid_value) < 1e-6):
                roots.append(mid)
        x = nxt
        previous = value

    unique = []
    for r in roots:
        duplicate = False
        for u in unique:
            if abs(r - u) < 1e-6:
                duplicate = True
        if not duplicate:
            unique.append(r)
    return sorted(unique), bound


def end_behavior(coefficients):
    degree = len(coefficients) - 1
    lead = coefficients[0]
    even = (degree % 2 == 0)
    if even and lead > 0:
        return "As x -> -inf, y -> +inf;  as x -> +inf, y -> +inf"
    if even and lead < 0:
        return "As x -> -inf, y -> -inf;  as x -> +inf, y -> -inf"
    if lead > 0:
        return "As x -> -inf, y -> -inf;  as x -> +inf, y -> +inf"
    return "As x -> -inf, y -> +inf;  as x -> +inf, y -> -inf"


def analyze_polynomial():
    degree = get_degree("Degree (1-" + str(MAX_DEGREE) + ") = ")
    coefficients = read_coefficients(degree, "Polynomial")

    print("\nf(x) = " + describe(coefficients))
    print("Degree = " + str(degree))
    print("Leading coefficient = " + str(round(coefficients[0], 6)))
    print("y-intercept = (0, " + str(round(coefficients[-1], 6)) + ")")
    print("\n" + end_behavior(coefficients))
    print("At most " + str(degree) + " real zeros and " +
          str(degree - 1) + " turning points.")

    roots, bound = find_roots(coefficients)
    print("\nReal zeros found in [-" + str(round(bound, 4)) + ", " +
          str(round(bound, 4)) + "]:")
    if len(roots) == 0:
        print("  none (the graph may not cross the x-axis)")
    else:
        for r in roots:
            shown = r
            if abs(shown - round(shown)) < 1e-7:
                shown = float(round(shown))
            print("  x = " + str(round(shown, 6)))

    if input("\nEvaluate at a point? (y/n) ").strip().lower() == "y":
        x = get_float("x = ")
        print("f(" + str(round(x, 6)) + ") = " +
              str(round(evaluate(coefficients, x), 6)))


def analyze_rational():
    print("\nRational function f(x) = N(x) / D(x)")
    num_degree = get_degree("Numerator degree (1-" + str(MAX_DEGREE) + ") = ")
    numerator = read_coefficients(num_degree, "Numerator")
    den_degree = get_degree("Denominator degree (1-" + str(MAX_DEGREE) + ") = ")
    denominator = read_coefficients(den_degree, "Denominator")

    print("\nN(x) = " + describe(numerator))
    print("D(x) = " + describe(denominator))

    num_roots, _b1 = find_roots(numerator)
    den_roots, _b2 = find_roots(denominator)

    holes = []
    true_vertical = []
    for d in den_roots:
        shared = False
        for n in num_roots:
            if abs(d - n) < 1e-6:
                shared = True
        if shared:
            holes.append(d)
        else:
            true_vertical.append(d)

    print("\nVertical asymptotes:")
    if len(true_vertical) == 0:
        print("  none")
    else:
        for v in true_vertical:
            print("  x = " + str(round(v, 6)))

    if len(holes) > 0:
        print("Holes (factor cancels) at:")
        for h in holes:
            print("  x = " + str(round(h, 6)))

    print("\nEnd behavior:")
    if num_degree < den_degree:
        print("  Numerator degree is smaller, so y = 0")
    elif num_degree == den_degree:
        ratio = numerator[0] / denominator[0]
        print("  Degrees match, so y = " + str(round(ratio, 6)) +
              " (ratio of leading coefficients)")
    elif num_degree == den_degree + 1:
        quotient, remainder = divide(numerator, denominator)
        print("  Numerator is one degree higher, so there is an")
        print("  oblique asymptote: y = " + describe(quotient))
        print("  Remainder: " + describe(remainder))
    else:
        print("  Numerator degree exceeds denominator by " +
              str(num_degree - den_degree) + ", so the tail follows a")
        print("  polynomial curve, not a line.")

    if evaluate(denominator, 0.0) != 0:
        print("\ny-intercept = (0, " +
              str(round(evaluate(numerator, 0.0) /
                        evaluate(denominator, 0.0), 6)) + ")")
    else:
        print("\nNo y-intercept (denominator is 0 at x = 0).")

    print("x-intercepts (numerator zeros that are not holes):")
    printed = False
    for n in num_roots:
        is_hole = False
        for h in holes:
            if abs(n - h) < 1e-6:
                is_hole = True
        if not is_hole:
            print("  x = " + str(round(n, 6)))
            printed = True
    if not printed:
        print("  none")


def divide(numerator, denominator):
    # Long division of coefficient lists; returns (quotient, remainder).
    work = numerator[:]
    den_degree = len(denominator) - 1
    steps = len(numerator) - len(denominator) + 1
    quotient = []
    for i in range(steps):
        factor = work[i] / denominator[0]
        quotient.append(factor)
        for j in range(len(denominator)):
            work[i + j] -= factor * denominator[j]
    remainder = work[steps:]
    if len(remainder) == 0:
        remainder = [0.0]
    if len(quotient) == 0:
        quotient = [0.0]
    return quotient, remainder


def main():
    print("=== POLYFUNC ===")
    while True:
        print("\n1. Polynomial analysis")
        print("2. Rational function analysis")
        print("0. Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                analyze_polynomial()
            elif choice == "2":
                analyze_rational()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except (ValueError, OverflowError, ZeroDivisionError):
            print("Could not compute with those values.")
    print("Bye.")


main()
