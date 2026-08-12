# On-calc name: STATIC
# Program: statics_vectors
# Purpose: Two statics tools in one menu: (1) resultant magnitude and
#          direction of a set of 2D force vectors entered as
#          magnitude+angle, and (2) net 2D torque/moment about a point
#          from a set of forces applied at given position vectors
#          (torque_z = rx*Fy - ry*Fx).
# Usage: Pick a tool. For resultant force, enter each force's
#        magnitude and angle (degrees from +x axis), blank to finish.
#        For torque, enter each force's position (rx, ry) relative to
#        the pivot and its components (Fx, Fy), blank to finish.

from math import sin, cos, radians, sqrt, atan2, degrees


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def resultant_force():
    print("\nEnter forces as magnitude and angle (degrees from +x axis).")
    print("Leave magnitude blank to finish (max 20 forces).")
    fx_total = 0.0
    fy_total = 0.0
    count = 0
    while count < 20:
        raw = input("Force " + str(count + 1) + " magnitude (blank to finish) = ").strip()
        if raw == "":
            break
        try:
            mag = float(raw)
        except (ValueError, TypeError):
            print("Please enter a valid number.")
            continue
        angle = get_float("  angle (degrees) = ")
        theta = radians(angle)
        fx_total += mag * cos(theta)
        fy_total += mag * sin(theta)
        count += 1

    if count == 0:
        print("No forces entered.")
        return

    magnitude = sqrt(fx_total ** 2 + fy_total ** 2)
    angle_out = degrees(atan2(fy_total, fx_total))
    print("\nSum Fx = " + str(round(fx_total, 6)))
    print("Sum Fy = " + str(round(fy_total, 6)))
    print("Resultant magnitude = " + str(round(magnitude, 6)))
    print("Resultant angle = " + str(round(angle_out, 4)) + " degrees from +x axis")


def torque_calc():
    print("\nEnter each force's position (rx, ry) relative to the pivot")
    print("and force components (Fx, Fy). Leave rx blank to finish (max 20).")
    total_torque = 0.0
    count = 0
    while count < 20:
        raw = input("Force " + str(count + 1) + " rx (blank to finish) = ").strip()
        if raw == "":
            break
        try:
            rx = float(raw)
        except (ValueError, TypeError):
            print("Please enter a valid number.")
            continue
        ry = get_float("  ry = ")
        fx = get_float("  Fx = ")
        fy = get_float("  Fy = ")
        torque = rx * fy - ry * fx
        print("  torque_" + str(count + 1) + " = " + str(round(torque, 6)))
        total_torque += torque
        count += 1

    if count == 0:
        print("No forces entered.")
        return

    print("\nNet torque about the point = " + str(round(total_torque, 6)))
    if total_torque > 0:
        print("(Positive = counterclockwise)")
    elif total_torque < 0:
        print("(Negative = clockwise)")
    else:
        print("(Zero = balanced)")


def main():
    print("=== STATIC ===")
    while True:
        print("\n1. Force resultant")
        print("2. Torque/moment")
        print("0. Quit")
        choice = input("> ").strip()
        if choice == "1":
            resultant_force()
        elif choice == "2":
            torque_calc()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
    print("Bye.")


main()
