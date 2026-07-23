# Program: taylor_series
# Purpose: Generate Maclaurin/Taylor series terms for common functions
#          (sin x, cos x, e^x, ln(1+x)) about 0, and show the running
#          partial-sum approximation compared to the true value.
# Usage: Choose a function from the menu, enter x and the number of
#        terms to sum. Prints each term added and the partial sum
#        after each term, then compares the final sum to the exact
#        (math-module) value.

from math import *


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def get_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n < 1:
                print("Enter a positive whole number.")
                continue
            return n
        except (ValueError, TypeError):
            print("Please enter a whole number.")


def series_sin(x, n_terms):
    terms = []
    for k in range(n_terms):
        n = 2 * k + 1
        term = ((-1) ** k) * (x ** n) / factorial(n)
        terms.append(term)
    return terms


def series_cos(x, n_terms):
    terms = []
    for k in range(n_terms):
        n = 2 * k
        term = ((-1) ** k) * (x ** n) / factorial(n)
        terms.append(term)
    return terms


def series_exp(x, n_terms):
    terms = []
    for k in range(n_terms):
        term = (x ** k) / factorial(k)
        terms.append(term)
    return terms


def series_ln1p(x, n_terms):
    if x <= -1:
        return None
    terms = []
    for k in range(1, n_terms + 1):
        term = ((-1) ** (k + 1)) * (x ** k) / k
        terms.append(term)
    return terms


MENU = {
    "1": ("sin(x)", series_sin, sin),
    "2": ("cos(x)", series_cos, cos),
    "3": ("e^x", series_exp, exp),
    "4": ("ln(1+x)", series_ln1p, lambda x: log(1 + x)),
}


def main():
    print("=== Taylor / Maclaurin Series Explorer ===")
    while True:
        print("\nChoose a function:")
        print("1. sin(x)")
        print("2. cos(x)")
        print("3. e^x")
        print("4. ln(1+x)")
        choice = input("Choice (1-4): ").strip()
        if choice not in MENU:
            print("Invalid choice.")
            continue

        name, series_fn, exact_fn = MENU[choice]
        x = get_float("x = ")
        n_terms = get_int("Number of terms (e.g. 6): ")

        terms = series_fn(x, n_terms)
        if terms is None:
            print("ln(1+x) requires x > -1. Try a different x.")
            continue

        print("\nMaclaurin series for " + name + " at x = " + str(x))
        running = 0.0
        for i, t in enumerate(terms):
            running += t
            print("Term " + str(i + 1) + ": " + str(round(t, 6)) +
                  "   Partial sum: " + str(round(running, 6)))

        try:
            exact = exact_fn(x)
            print("\nApproximation: " + str(round(running, 6)))
            print("True value (math module): " + str(round(exact, 6)))
            print("Absolute error: " + str(round(abs(exact - running), 8)))
        except Exception:
            print("\nApproximation: " + str(round(running, 6)))
            print("(Could not compute exact value for comparison.)")

        again = input("\nTry another? (y/n): ").strip().lower()
        if again != "y":
            break
    print("Done.")


main()
