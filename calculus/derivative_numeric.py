# On-calc name: DERIV
# Program: derivative_numeric
# Purpose: Approximate f'(x0) using the central-difference formula
#          f'(x0) ~= (f(x0+h) - f(x0-h)) / (2h), with a user-controlled
#          step size h so students can see how accuracy changes with h.
# Usage: Enter f(x) using x as the variable, e.g. sin(x)+x**2, exp(x),
#        ln is written as log(x). Then enter x0 and a step size h
#        (defaults to 0.001 if left blank). Prints the derivative
#        estimate plus estimates at h/10 and h*10 for comparison.
#
# Allowed function names: sin, cos, tan, asin, acos, atan, atan2, exp,
# log, log10, sqrt, fabs, pi, e, plus + - * / ** and parentheses.

from math import *


def f_of_x(expr, x):
    return eval(expr)


def get_float(prompt, default=None):
    while True:
        raw = input(prompt).strip()
        if raw == "" and default is not None:
            return default
        try:
            return float(raw)
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def get_expr():
    while True:
        expr = input("f(x) = ").strip()
        if expr == "":
            print("Please enter an expression.")
            continue
        try:
            f_of_x(expr, 1.0)
            return expr
        except Exception:
            print("Could not evaluate that expression. Try again.")
            print("Example: sin(x)+x**2")


def central_diff(expr, x0, h):
    try:
        return (f_of_x(expr, x0 + h) - f_of_x(expr, x0 - h)) / (2 * h)
    except Exception:
        return None


def main():
    print("=== DERIV ===")
    while True:
        expr = get_expr()
        x0 = get_float("x0 = ")
        h = get_float("Step size h (blank = 0.001): ", default=0.001)
        if h == 0:
            print("h cannot be 0, using 0.001 instead.")
            h = 0.001

        print("\nf(x) = " + expr)
        print("x0 = " + str(x0))
        for label, step in (("h/10", h / 10.0), ("h", h), ("h*10", h * 10.0)):
            d = central_diff(expr, x0, step)
            if d is None:
                print(label + " = " + str(step) + " -> error evaluating")
            else:
                print(label + " = " + str(step) + " -> f'(x0) ~= " + str(round(d, 6)))

        print("\n1. Again  0. Quit")
        if input("> ").strip() == "0":
            break
    print("Bye.")


main()
