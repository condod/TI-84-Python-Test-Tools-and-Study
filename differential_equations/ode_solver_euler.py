# On-calc name: ODE
# Program: ode_solver_euler
# Purpose: Numerically solve a first-order ODE dy/dx = f(x, y) given an
#          initial condition (x0, y0), using either Euler's method or
#          the improved Euler / Heun's method (a simple predictor-
#          corrector that averages the slope at the start and end of
#          each step for better accuracy).
# Usage: Enter f(x,y) using x and y as variables (e.g. x+y, x*y-y**2).
#        Enter x0, y0, a step size h, and a target x value to solve
#        toward. Pick Euler or Improved Euler from the menu. Prints a
#        step-by-step table of x, y and the final approximate y.

from math import *


def f_of_xy(expr, x, y):
    return eval(expr)


def pad(text, width):
    # str.ljust() is not available in the calculator's Python build.
    s = str(text)
    if len(s) >= width:
        return s
    return s + " " * (width - len(s))


def pad_left(text, width):
    # stand-in for str.rjust()
    s = str(text)
    if len(s) >= width:
        return s
    return " " * (width - len(s)) + s


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
        expr = input("f(x,y) = ").strip()
        if expr == "":
            print("Please enter an expression.")
            continue
        try:
            f_of_xy(expr, 1.0, 1.0)
            return expr
        except Exception:
            print("Could not evaluate that expression. Try again.")


def run_euler(expr, x, y, h, x_target, improved):
    steps = 0
    print("\n Step |    x        |    y")
    print(" " + pad_left(steps, 4) + "  | " + pad(round(x, 6), 11) +
          " | " + str(round(y, 6)))

    # Cap the number of steps so a tiny h / large range can't run away.
    max_steps = 500
    going_up = x_target >= x

    while steps < max_steps:
        remaining = x_target - x
        if going_up and remaining <= 1e-12:
            break
        if (not going_up) and remaining >= -1e-12:
            break

        step_h = h if going_up else -h
        if abs(remaining) < abs(step_h):
            step_h = remaining

        try:
            slope1 = f_of_xy(expr, x, y)
            if improved:
                y_predict = y + step_h * slope1
                slope2 = f_of_xy(expr, x + step_h, y_predict)
                y = y + step_h * (slope1 + slope2) / 2.0
            else:
                y = y + step_h * slope1
        except Exception:
            print("Math error while evaluating f(x,y). Stopping early.")
            return

        x = x + step_h
        steps += 1
        print(" " + pad_left(steps, 4) + "  | " + pad(round(x, 6), 11) +
              " | " + str(round(y, 6)))

    if steps >= max_steps:
        print("\nStopped: reached the " + str(max_steps) + "-step safety limit.")
    print("\nApproximate y(" + str(round(x_target, 6)) + ") = " + str(round(y, 6)))


def main():
    print("=== ODE ===")
    print("Solves dy/dx = f(x,y) given y(x0) = y0.")
    while True:
        expr = get_expr()
        x0 = get_float("x0 = ")
        y0 = get_float("y0 = ")
        x_target = get_float("Solve for y at x = ")
        h = get_float("Step size h (blank = 0.1): ", default=0.1)
        if h <= 0:
            print("Step size must be positive; using 0.1 instead.")
            h = 0.1

        print("\n1. Euler's method")
        print("2. Improved Euler (Heun's method)")
        method = input("Choice (1-2, blank = 1): ").strip()
        improved = (method == "2")

        if x_target == x0:
            print("\nx target equals x0, so y(x0) = " + str(round(y0, 6)) + " (no steps needed).")
        else:
            run_euler(expr, x0, y0, h, x_target, improved)

        print("\n1. Again  0. Quit")
        if input("> ").strip() == "0":
            break
    print("Bye.")


main()
