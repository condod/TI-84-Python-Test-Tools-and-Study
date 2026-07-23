# Program: limit_evaluator
# Purpose: Numerically estimate the limit of f(x) as x approaches a
#          target value c, evaluating from the left and right sides
#          with a shrinking gap so students can see one-sided behavior
#          and spot discontinuities (also useful for related-rates
#          "plug in a value" sanity checks).
# Usage: Enter f(x) using x as the variable (e.g. (sin(x))/x,
#        (x**2-4)/(x-2)). Enter the value c that x approaches.
#        Prints a table of f(c-eps) and f(c+eps) for shrinking eps,
#        plus a best-guess limit if left/right values agree closely.

from math import *


def f_of_x(expr, x):
    return eval(expr)


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def get_expr():
    while True:
        expr = input("f(x) = ").strip()
        if expr == "":
            print("Please enter an expression.")
            continue
        return expr


def safe_eval(expr, x):
    try:
        return f_of_x(expr, x)
    except ZeroDivisionError:
        return None
    except Exception:
        return None


def main():
    print("=== Numeric Limit Evaluator ===")
    print("Evaluates f(x) as x -> c from both sides.")
    while True:
        expr = get_expr()
        c = get_float("x approaches c = ")

        eps_list = [0.1, 0.01, 0.001, 0.0001, 0.00001]
        print("\n   eps    |   f(c-eps)   |   f(c+eps)")
        last_left = None
        last_right = None
        for eps in eps_list:
            left = safe_eval(expr, c - eps)
            right = safe_eval(expr, c + eps)
            last_left, last_right = left, right
            lstr = "undefined" if left is None else str(round(left, 6))
            rstr = "undefined" if right is None else str(round(right, 6))
            print(str(eps).ljust(9) + "| " + lstr.ljust(13) + "| " + rstr)

        print()
        if last_left is not None and last_right is not None and abs(last_left - last_right) < 1e-3:
            approx = (last_left + last_right) / 2.0
            print("Left and right sides agree closely.")
            print("Estimated limit as x -> " + str(c) + ": " + str(round(approx, 6)))
        else:
            print("Left and right sides do not clearly agree (or f is undefined nearby).")
            print("The limit may not exist, or may need more terms/algebraic simplification.")

        again = input("\nAnother limit? (y/n): ").strip().lower()
        if again != "y":
            break
    print("Done.")


main()
