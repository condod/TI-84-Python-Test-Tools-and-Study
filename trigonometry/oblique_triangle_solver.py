# On-calc name: TRIG
# Program: oblique_triangle_solver
# Purpose: Solve non-right (oblique) triangles using the Law of Sines
#          and Law of Cosines. Menu covers the four solvable cases:
#          SSS, SAS, ASA/AAS, and the ambiguous SSA case.
# Usage: Pick a case from the menu and enter the known sides/angles
#        (angles in degrees). Prints the missing sides/angles, or a
#        message if the given values do not form a valid triangle
#        (including 0, 1, or 2 solutions for the ambiguous SSA case).

from math import sin, cos, asin, acos, radians, degrees, sqrt


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def get_positive(prompt):
    while True:
        value = get_float(prompt)
        if value > 0:
            return value
        print("Value must be positive.")


def get_angle(prompt):
    while True:
        value = get_float(prompt)
        if 0 < value < 180:
            return value
        print("Angle must be between 0 and 180 degrees.")


def clamp(value):
    return max(-1.0, min(1.0, value))


def solve_sss():
    print("\nEnter the three side lengths:")
    a = get_positive("a = ")
    b = get_positive("b = ")
    c = get_positive("c = ")
    if a + b <= c or a + c <= b or b + c <= a:
        print("Those sides do not form a triangle.")
        return

    angle_a = degrees(acos(clamp((b * b + c * c - a * a) / (2 * b * c))))
    angle_b = degrees(acos(clamp((a * a + c * c - b * b) / (2 * a * c))))
    angle_c = 180.0 - angle_a - angle_b

    print("\nAngle A (opposite a) = " + str(round(angle_a, 4)) + " deg")
    print("Angle B (opposite b) = " + str(round(angle_b, 4)) + " deg")
    print("Angle C (opposite c) = " + str(round(angle_c, 4)) + " deg")


def solve_sas():
    print("\nEnter two sides and the INCLUDED angle C (between them):")
    a = get_positive("a = ")
    b = get_positive("b = ")
    angle_c = get_angle("C (degrees) = ")

    c = sqrt(a * a + b * b - 2 * a * b * cos(radians(angle_c)))
    if c <= 0:
        print("Those values do not form a triangle.")
        return

    angle_a = degrees(acos(clamp((b * b + c * c - a * a) / (2 * b * c))))
    angle_b = 180.0 - angle_c - angle_a

    print("\nSide c (opposite C) = " + str(round(c, 6)))
    print("Angle A (opposite a) = " + str(round(angle_a, 4)) + " deg")
    print("Angle B (opposite b) = " + str(round(angle_b, 4)) + " deg")


def solve_asa():
    print("\nEnter angle A, angle B, and side a (opposite angle A):")
    angle_a = get_angle("A (degrees) = ")
    angle_b = get_angle("B (degrees) = ")
    a = get_positive("a = ")

    angle_c = 180.0 - angle_a - angle_b
    if angle_c <= 0:
        print("Those angles do not leave room for a third angle.")
        return

    sin_a = sin(radians(angle_a))
    if sin_a == 0:
        print("Angle A is too small to compute a ratio.")
        return
    ratio = a / sin_a
    b = ratio * sin(radians(angle_b))
    c = ratio * sin(radians(angle_c))

    print("\nAngle C = " + str(round(angle_c, 4)) + " deg")
    print("Side b (opposite B) = " + str(round(b, 6)))
    print("Side c (opposite C) = " + str(round(c, 6)))


def solve_ssa():
    print("\nEnter side a, side b, and angle A (opposite side a):")
    a = get_positive("a = ")
    b = get_positive("b = ")
    angle_a = get_angle("A (degrees) = ")

    sin_a = sin(radians(angle_a))
    sin_b = b * sin_a / a
    if sin_b > 1.0000001:
        print("\nNo triangle: side a is too short to reach side b.")
        return

    sin_b = clamp(sin_b)
    angle_b1 = degrees(asin(sin_b))
    solutions = []

    angle_c1 = 180.0 - angle_a - angle_b1
    if angle_c1 > 0:
        solutions.append((angle_b1, angle_c1))

    angle_b2 = 180.0 - angle_b1
    angle_c2 = 180.0 - angle_a - angle_b2
    if angle_b2 != angle_b1 and angle_c2 > 0:
        solutions.append((angle_b2, angle_c2))

    if len(solutions) == 0:
        print("\nNo valid triangle from those values.")
        return

    print("\n" + str(len(solutions)) + " solution(s) found:")
    index = 0
    while index < len(solutions):
        angle_b, angle_c = solutions[index]
        c = a * sin(radians(angle_c)) / sin_a
        print("\nSolution " + str(index + 1) + ":")
        print("Angle B = " + str(round(angle_b, 4)) + " deg")
        print("Angle C = " + str(round(angle_c, 4)) + " deg")
        print("Side c (opposite C) = " + str(round(c, 6)))
        index += 1


def main():
    print("=== TRIG ===")
    while True:
        print("\n1. SSS (3 sides)")
        print("2. SAS (2 sides + angle)")
        print("3. ASA/AAS (2 angles + side)")
        print("4. SSA (ambiguous case)")
        print("0. Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                solve_sss()
            elif choice == "2":
                solve_sas()
            elif choice == "3":
                solve_asa()
            elif choice == "4":
                solve_ssa()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except Exception:
            print("Could not compute with those values.")
    print("Bye.")


main()
