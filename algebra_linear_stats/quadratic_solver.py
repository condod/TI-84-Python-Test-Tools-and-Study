# Program: quadratic_solver
# Purpose: Solve ax^2+bx+c=0. Classifies the discriminant and prints
#          two real roots, one repeated real root, or a complex
#          conjugate pair (written manually as a +/- bi, since this
#          calculator's Python does not include the cmath module).
# Usage: Enter coefficients a, b, c (a cannot be 0). Prints the
#        discriminant, its classification, and the root(s).

from math import sqrt


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def main():
    print("=== Quadratic Equation Solver: ax^2 + bx + c = 0 ===")
    while True:
        while True:
            a = get_float("a = ")
            if a == 0:
                print("a cannot be 0 (not a quadratic). Try again.")
                continue
            break
        b = get_float("b = ")
        c = get_float("c = ")

        disc = b * b - 4 * a * c
        print("\nDiscriminant (b^2-4ac) = " + str(round(disc, 6)))

        if disc > 0:
            print("Two distinct real roots.")
            r1 = (-b + sqrt(disc)) / (2 * a)
            r2 = (-b - sqrt(disc)) / (2 * a)
            print("x1 = " + str(round(r1, 6)))
            print("x2 = " + str(round(r2, 6)))
        elif disc == 0:
            print("One repeated real root.")
            r = -b / (2 * a)
            print("x = " + str(round(r, 6)))
        else:
            print("No real roots; complex conjugate pair.")
            real_part = -b / (2 * a) + 0.0  # avoid printing -0.0
            imag_part = abs(sqrt(-disc) / (2 * a))
            print("x1 = " + str(round(real_part, 6)) + " + " + str(round(imag_part, 6)) + "i")
            print("x2 = " + str(round(real_part, 6)) + " - " + str(round(imag_part, 6)) + "i")

        again = input("\nSolve another? (y/n): ").strip().lower()
        if again != "y":
            break
    print("Done.")


main()
