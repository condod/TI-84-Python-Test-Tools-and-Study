# Program: newton_raphson
# Purpose: Find a root of f(x) = 0 using the Newton-Raphson method,
#          printing each iteration's x value so students can watch
#          convergence happen. Derivative is estimated numerically
#          (central difference) so you only need to type f(x).
# Usage: Enter f(x) using x as the variable (e.g. x**2-2, cos(x)-x).
#        Enter an initial guess x0, a tolerance (blank = 1e-6), and a
#        max number of iterations (blank = 25). Prints an iteration
#        table and the final root estimate.

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


def get_int(prompt, default=None):
    while True:
        raw = input(prompt).strip()
        if raw == "" and default is not None:
            return default
        try:
            n = int(raw)
            if n < 1:
                print("Enter a positive whole number.")
                continue
            return n
        except (ValueError, TypeError):
            print("Please enter a whole number.")


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


def numeric_deriv(expr, x, h=1e-5):
    return (f_of_x(expr, x + h) - f_of_x(expr, x - h)) / (2 * h)


def main():
    print("=== Newton-Raphson Root Finder ===")
    while True:
        expr = get_expr()
        x = get_float("Initial guess x0 = ")
        tol = get_float("Tolerance (blank = 1e-6): ", default=1e-6)
        max_iter = get_int("Max iterations (blank = 25): ", default=25)

        print("\nIter |     x        |    f(x)")
        converged = False
        for i in range(1, max_iter + 1):
            try:
                fx = f_of_x(expr, x)
                dfx = numeric_deriv(expr, x)
            except Exception:
                print("Math error while evaluating f(x) or f'(x). Stopping.")
                break

            print(str(i).rjust(4) + " | " + str(round(x, 8)).ljust(12) + " | " + str(round(fx, 8)))

            if dfx == 0:
                print("Derivative is 0; Newton's method fails here. Try a different x0.")
                break

            x_new = x - fx / dfx
            if abs(x_new - x) < tol:
                x = x_new
                converged = True
                break
            x = x_new

        if converged:
            print("\nConverged! Root estimate: x = " + str(round(x, 8)))
        else:
            print("\nStopped without confirmed convergence. Last x = " + str(round(x, 8)))
            print("Try more iterations, a looser tolerance, or a different x0.")

        again = input("\nFind another root? (y/n): ").strip().lower()
        if again != "y":
            break
    print("Done.")


main()
