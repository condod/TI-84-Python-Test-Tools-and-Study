# On-calc name: VECT3D
# Program: vector3d_toolkit
# Purpose: 3D vector operations menu: dot product, cross product,
#          magnitude, angle between two vectors, and scalar/vector
#          projection of one vector onto another.
# Usage: Pick a tool from the menu, then enter vector A (and vector B
#        where needed) as their x, y, z components one at a time.
#        Prints the requested result.

from math import sqrt, acos, degrees


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def get_vector(name):
    print("Enter vector " + name + ":")
    x = get_float("  " + name + "x = ")
    y = get_float("  " + name + "y = ")
    z = get_float("  " + name + "z = ")
    return (x, y, z)


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def magnitude(a):
    return sqrt(dot(a, a))


def fmt_vec(v):
    return "(" + str(round(v[0], 6)) + ", " + str(round(v[1], 6)) + ", " + str(round(v[2], 6)) + ")"


def do_dot():
    a = get_vector("A")
    b = get_vector("B")
    print("\nA . B = " + str(round(dot(a, b), 6)))


def do_cross():
    a = get_vector("A")
    b = get_vector("B")
    c = cross(a, b)
    print("\nA x B = " + fmt_vec(c))
    print("|A x B| = " + str(round(magnitude(c), 6)))


def do_magnitude():
    a = get_vector("A")
    print("\n|A| = " + str(round(magnitude(a), 6)))


def do_angle():
    a = get_vector("A")
    b = get_vector("B")
    mag_a = magnitude(a)
    mag_b = magnitude(b)
    if mag_a == 0 or mag_b == 0:
        print("\nCannot find an angle with a zero vector.")
        return
    cos_theta = dot(a, b) / (mag_a * mag_b)
    # Clamp for tiny floating-point overshoot past +-1.
    if cos_theta > 1:
        cos_theta = 1.0
    elif cos_theta < -1:
        cos_theta = -1.0
    theta = degrees(acos(cos_theta))
    print("\nAngle between A and B = " + str(round(theta, 4)) + " degrees")


def do_projection():
    a = get_vector("A")
    b = get_vector("B")
    mag_b = magnitude(b)
    if mag_b == 0:
        print("\nCannot project onto a zero vector B.")
        return
    scalar_proj = dot(a, b) / mag_b
    proj_factor = dot(a, b) / (mag_b * mag_b)
    vector_proj = (proj_factor * b[0], proj_factor * b[1], proj_factor * b[2])
    print("\nScalar projection of A onto B = " + str(round(scalar_proj, 6)))
    print("Vector projection of A onto B = " + fmt_vec(vector_proj))


def main():
    print("=== VECT3D ===")
    while True:
        print("\n1. Dot A.B")
        print("2. Cross AxB")
        print("3. |A|")
        print("4. Angle A,B")
        print("5. Proj A on B")
        print("0. Quit")
        choice = input("> ").strip()
        if choice == "1":
            do_dot()
        elif choice == "2":
            do_cross()
        elif choice == "3":
            do_magnitude()
        elif choice == "4":
            do_angle()
        elif choice == "5":
            do_projection()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
    print("Bye.")


main()
