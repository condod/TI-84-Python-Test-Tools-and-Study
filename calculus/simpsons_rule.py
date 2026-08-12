# On-calc name: SIMPSON
# Program: simpsons_rule
# Purpose: Approximate a definite integral, integral of f(x) dx from a to b,
#          using composite Simpson's Rule.
# Usage: Enter f(x) using x as the variable (e.g. x**2+1, sin(x), exp(-x)).
#        Enter bounds a and b, and an even number of subintervals n
#        (n is auto-bumped up by 1 if you enter an odd number).
#        Prints the Simpson's Rule estimate of the integral.

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
        try:
            f_of_x(expr, 1.0)
            return expr
        except Exception:
            print("Could not evaluate that expression. Try again.")


def get_even_int(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            n = int(raw)
            if n <= 0:
                print("n must be a positive integer.")
                continue
            if n % 2 != 0:
                n += 1
                print("n must be even, using n = " + str(n))
            return n
        except (ValueError, TypeError):
            print("Please enter a whole number.")


def simpson(expr, a, b, n):
    h = (b - a) / n
    total = f_of_x(expr, a) + f_of_x(expr, b)
    for i in range(1, n):
        x = a + i * h
        coeff = 4 if i % 2 == 1 else 2
        total += coeff * f_of_x(expr, x)
    return total * h / 3.0


def main():
    print("=== SIMPSON ===")
    while True:
        expr = get_expr()
        a = get_float("Lower bound a = ")
        b = get_float("Upper bound b = ")
        n = get_even_int("Number of subintervals n (even, e.g. 10): ")

        if a == b:
            print("a and b are equal; integral is 0.")
        else:
            try:
                result = simpson(expr, a, b, n)
                print("\nIntegral of " + expr + " dx from " + str(a) + " to " + str(b))
                print("Simpson's Rule estimate (n=" + str(n) + "): " + str(round(result, 6)))
            except Exception:
                print("Error evaluating the integral. Check your function and bounds (e.g. avoid division by zero in range).")

        print("\n1. Again  0. Quit")
        if input("> ").strip() == "0":
            break
    print("Bye.")


main()
