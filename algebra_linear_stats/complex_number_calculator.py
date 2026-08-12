# On-calc name: CMPLX
# Program: complex_number_calculator
# Purpose: Manual complex-number calculator. Performs add/subtract/
#          multiply/divide on two complex numbers, finds a number's
#          magnitude and argument, and converts between rectangular
#          and polar form -- all with plain real-number arithmetic,
#          since this calculator's Python does not include cmath.
# Usage: Pick an operation from the menu. For add/sub/mul/div, enter
#        the real and imaginary parts of z1 and z2. Prints the result
#        as a + bi. Magnitude/angle and polar conversions take one
#        complex number (rectangular) or an r/theta pair (polar).

from math import sqrt, atan2, sin, cos, radians, degrees


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def get_complex(name):
    print("Enter " + name + ":")
    re = get_float("  " + name + " real = ")
    im = get_float("  " + name + " imag = ")
    return (re, im)


def fmt_complex(z):
    re = round(z[0], 6) + 0.0
    im = round(z[1], 6) + 0.0
    if im < 0:
        return str(re) + " - " + str(abs(im)) + "i"
    return str(re) + " + " + str(im) + "i"


def c_add(z1, z2):
    return (z1[0] + z2[0], z1[1] + z2[1])


def c_sub(z1, z2):
    return (z1[0] - z2[0], z1[1] - z2[1])


def c_mul(z1, z2):
    a, b = z1
    c, d = z2
    return (a * c - b * d, a * d + b * c)


def c_div(z1, z2):
    a, b = z1
    c, d = z2
    denom = c * c + d * d
    if denom == 0:
        return None
    return ((a * c + b * d) / denom, (b * c - a * d) / denom)


def magnitude(z):
    return sqrt(z[0] * z[0] + z[1] * z[1])


def argument_degrees(z):
    return degrees(atan2(z[1], z[0]))


def do_add():
    z1 = get_complex("z1")
    z2 = get_complex("z2")
    print("\nz1 + z2 = " + fmt_complex(c_add(z1, z2)))


def do_sub():
    z1 = get_complex("z1")
    z2 = get_complex("z2")
    print("\nz1 - z2 = " + fmt_complex(c_sub(z1, z2)))


def do_mul():
    z1 = get_complex("z1")
    z2 = get_complex("z2")
    print("\nz1 * z2 = " + fmt_complex(c_mul(z1, z2)))


def do_div():
    z1 = get_complex("z1")
    z2 = get_complex("z2")
    result = c_div(z1, z2)
    if result is None:
        print("\nCannot divide by zero.")
        return
    print("\nz1 / z2 = " + fmt_complex(result))


def do_mag_angle():
    z = get_complex("z")
    print("\n|z| = " + str(round(magnitude(z), 6)))
    print("angle(z) = " + str(round(argument_degrees(z), 4)) + " degrees")


def do_rect_to_polar():
    z = get_complex("z")
    r = magnitude(z)
    theta = argument_degrees(z)
    print("\nr = " + str(round(r, 6)))
    print("theta = " + str(round(theta, 4)) + " degrees")
    print("Polar form: " + str(round(r, 6)) + " cis(" + str(round(theta, 4)) + " deg)")


def do_polar_to_rect():
    print("Enter polar form r and theta:")
    r = get_float("  r = ")
    theta = get_float("  theta (degrees) = ")
    rad = radians(theta)
    re = r * cos(rad)
    im = r * sin(rad)
    print("\nRectangular form: " + fmt_complex((re, im)))


def main():
    print("=== CMPLX ===")
    while True:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Magnitude & Angle")
        print("6. Rect -> Polar")
        print("7. Polar -> Rect")
        print("0. Quit")
        choice = input("> ").strip()
        if choice == "1":
            do_add()
        elif choice == "2":
            do_sub()
        elif choice == "3":
            do_mul()
        elif choice == "4":
            do_div()
        elif choice == "5":
            do_mag_angle()
        elif choice == "6":
            do_rect_to_polar()
        elif choice == "7":
            do_polar_to_rect()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
    print("Bye.")


main()
