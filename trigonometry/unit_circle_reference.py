# On-calc name: UNITCIRC
# Program: unit_circle_reference
# Purpose: Unit-circle reference and trig evaluator. Evaluates all six
#          trig functions at an angle, naming the exact value (like
#          sqrt(3)/2) whenever the angle is one of the standard
#          unit-circle angles, and reports the reference angle,
#          quadrant, and sign pattern. Also converts degrees and
#          radians, evaluates inverse trig, and checks the Pythagorean
#          identities numerically.
# Usage: Pick a tool from the menu and enter an angle in degrees or
#        radians as prompted. Angles outside 0-360 are wrapped into
#        that range first, and undefined values (like tan 90) are
#        reported as undefined instead of crashing.

from math import pi, sin, cos, tan, asin, acos, atan, sqrt, degrees, radians

TINY = 1e-10

# Exact values on the unit circle, keyed by degrees in 0..330.
EXACT = [
    (0.0, "0", "1", "0"),
    (30.0, "1/2", "sqrt(3)/2", "sqrt(3)/3"),
    (45.0, "sqrt(2)/2", "sqrt(2)/2", "1"),
    (60.0, "sqrt(3)/2", "1/2", "sqrt(3)"),
    (90.0, "1", "0", "undefined"),
    (120.0, "sqrt(3)/2", "-1/2", "-sqrt(3)"),
    (135.0, "sqrt(2)/2", "-sqrt(2)/2", "-1"),
    (150.0, "1/2", "-sqrt(3)/2", "-sqrt(3)/3"),
    (180.0, "0", "-1", "0"),
    (210.0, "-1/2", "-sqrt(3)/2", "sqrt(3)/3"),
    (225.0, "-sqrt(2)/2", "-sqrt(2)/2", "1"),
    (240.0, "-sqrt(3)/2", "-1/2", "sqrt(3)"),
    (270.0, "-1", "0", "undefined"),
    (300.0, "-sqrt(3)/2", "1/2", "-sqrt(3)"),
    (315.0, "-sqrt(2)/2", "sqrt(2)/2", "-1"),
    (330.0, "-1/2", "sqrt(3)/2", "-sqrt(3)/3"),
]


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def wrap_degrees(angle):
    wrapped = angle - 360.0 * int(angle / 360.0)
    if wrapped < 0:
        wrapped += 360.0
    return wrapped


def exact_row(deg):
    for row in EXACT:
        if abs(deg - row[0]) < 1e-9:
            return row
    return None


def quadrant_of(deg):
    if abs(deg) < TINY or abs(deg - 360.0) < TINY:
        return "on the +x axis"
    if abs(deg - 90.0) < TINY:
        return "on the +y axis"
    if abs(deg - 180.0) < TINY:
        return "on the -x axis"
    if abs(deg - 270.0) < TINY:
        return "on the -y axis"
    if deg < 90.0:
        return "Quadrant I (sin+ cos+ tan+)"
    if deg < 180.0:
        return "Quadrant II (sin+ cos- tan-)"
    if deg < 270.0:
        return "Quadrant III (sin- cos- tan+)"
    return "Quadrant IV (sin- cos+ tan-)"


def reference_angle(deg):
    if deg <= 90.0:
        return deg
    if deg <= 180.0:
        return 180.0 - deg
    if deg <= 270.0:
        return deg - 180.0
    return 360.0 - deg


def clean(value):
    if abs(value) < TINY:
        return 0.0
    return value


def show_reciprocal(name, value):
    if abs(value) < TINY:
        print(name + " = undefined (division by zero)")
    else:
        print(name + " = " + str(round(1.0 / value, 6)))


def evaluate_angle():
    print("\n1. Angle in degrees")
    print("2. Angle in radians")
    mode = input("> ").strip()
    if mode == "1":
        raw = get_float("Angle (degrees) = ")
        deg = raw
    elif mode == "2":
        raw = get_float("Angle (radians) = ")
        deg = degrees(raw)
    else:
        print("Invalid choice.")
        return

    wrapped = wrap_degrees(deg)
    rad = radians(wrapped)
    sine = clean(sin(rad))
    cosine = clean(cos(rad))

    print("\nAngle = " + str(round(deg, 6)) + " deg")
    print("      = " + str(round(radians(deg), 6)) + " rad")
    if abs(wrapped - deg) > TINY:
        print("Coterminal angle in 0-360: " + str(round(wrapped, 6)) + " deg")
    print(quadrant_of(wrapped))
    print("Reference angle = " + str(round(reference_angle(wrapped), 6)) +
          " deg")

    print("\nsin = " + str(round(sine, 6)))
    print("cos = " + str(round(cosine, 6)))
    if abs(cosine) < TINY:
        print("tan = undefined (cos = 0)")
    else:
        print("tan = " + str(round(sine / cosine, 6)))
    show_reciprocal("csc", sine)
    show_reciprocal("sec", cosine)
    if abs(sine) < TINY:
        print("cot = undefined (sin = 0)")
    elif abs(cosine) < TINY:
        print("cot = 0")
    else:
        print("cot = " + str(round(cosine / sine, 6)))

    row = exact_row(wrapped)
    if row is not None:
        print("\nExact unit-circle values:")
        print("  sin = " + row[1])
        print("  cos = " + row[2])
        print("  tan = " + row[3])


def show_table():
    print("\nDeg  sin          cos          tan")
    count = 0
    for row in EXACT:
        print(("   " + str(int(row[0])))[-4:] + " " +
              row[1] + " / " + row[2] + " / " + row[3])
        count += 1
        if count % 8 == 0 and count != len(EXACT):
            input("ENTER for more")


def convert_angle():
    print("\n1. Degrees -> radians")
    print("2. Radians -> degrees")
    choice = input("> ").strip()
    if choice == "1":
        deg = get_float("Degrees = ")
        rad = radians(deg)
        print("\n" + str(round(deg, 6)) + " deg = " + str(round(rad, 6)) +
              " rad")
        if abs(deg) > TINY:
            print("           = " + str(round(deg / 180.0, 6)) + " * pi rad")
    elif choice == "2":
        rad = get_float("Radians = ")
        print("\n" + str(round(rad, 6)) + " rad = " +
              str(round(degrees(rad), 6)) + " deg")
    else:
        print("Invalid choice.")


def inverse_trig():
    print("\n1. arcsin")
    print("2. arccos")
    print("3. arctan")
    choice = input("> ").strip()
    if choice not in ("1", "2", "3"):
        print("Invalid choice.")
        return

    value = get_float("Value = ")
    if choice in ("1", "2") and (value < -1 or value > 1):
        print("arcsin and arccos need a value between -1 and 1.")
        return

    if choice == "1":
        rad = asin(value)
        name = "arcsin"
    elif choice == "2":
        rad = acos(value)
        name = "arccos"
    else:
        rad = atan(value)
        name = "arctan"

    print("\n" + name + "(" + str(round(value, 6)) + ") = " +
          str(round(degrees(rad), 6)) + " deg")
    print("        = " + str(round(rad, 6)) + " rad")
    if choice == "1":
        other = 180.0 - degrees(rad)
        print("Second solution in 0-360: " + str(round(wrap_degrees(other), 6))
              + " deg")
    elif choice == "2":
        print("Second solution in 0-360: " +
              str(round(360.0 - degrees(rad), 6)) + " deg")
    else:
        print("Second solution in 0-360: " +
              str(round(wrap_degrees(degrees(rad) + 180.0), 6)) + " deg")


def check_identities():
    deg = get_float("Angle (degrees) = ")
    rad = radians(deg)
    s = sin(rad)
    c = cos(rad)
    print("\nsin^2 + cos^2 = " + str(round(s * s + c * c, 10)) + "  (= 1)")
    if abs(c) > TINY:
        t = s / c
        print("1 + tan^2 = " + str(round(1.0 + t * t, 10)))
        print("sec^2     = " + str(round(1.0 / (c * c), 10)))
    else:
        print("tan and sec are undefined here (cos = 0).")
    if abs(s) > TINY:
        cot = c / s
        print("1 + cot^2 = " + str(round(1.0 + cot * cot, 10)))
        print("csc^2     = " + str(round(1.0 / (s * s), 10)))
    else:
        print("cot and csc are undefined here (sin = 0).")
    print("\nDouble angle checks:")
    print("sin(2a) = " + str(round(sin(2.0 * rad), 10)))
    print("2 sin a cos a = " + str(round(2.0 * s * c, 10)))
    print("cos(2a) = " + str(round(cos(2.0 * rad), 10)))
    print("cos^2 - sin^2 = " + str(round(c * c - s * s, 10)))


def main():
    print("=== UNITCIRC ===")
    while True:
        print("\n1. Evaluate an angle")
        print("2. Unit-circle exact table")
        print("3. Degrees <-> radians")
        print("4. Inverse trig")
        print("5. Check identities")
        print("0. Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                evaluate_angle()
            elif choice == "2":
                show_table()
            elif choice == "3":
                convert_angle()
            elif choice == "4":
                inverse_trig()
            elif choice == "5":
                check_identities()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except (ValueError, OverflowError, ZeroDivisionError):
            print("Could not compute with those values.")
    print("Bye.")


main()
