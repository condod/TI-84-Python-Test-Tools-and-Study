# On-calc name: GEOM
# Program: shape_geometry_solver
# Purpose: Area/perimeter calculator for common 2D shapes (circle,
#          rectangle, triangle via Heron's formula) and volume/surface
#          area calculator for common 3D solids (sphere, cylinder,
#          cone, rectangular prism).
# Usage: Pick a shape from the menu and enter its dimensions. Prints
#        the area and perimeter (2D) or volume and surface area (3D).
#        The triangle option checks the triangle inequality first.

from math import pi, sqrt


def get_positive(prompt):
    while True:
        try:
            value = float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")
            continue
        if value > 0:
            return value
        print("Value must be positive.")


def circle():
    r = get_positive("Radius = ")
    area = pi * r * r
    circumference = 2 * pi * r
    print("\nArea = " + str(round(area, 6)))
    print("Circumference = " + str(round(circumference, 6)))


def rectangle():
    l = get_positive("Length = ")
    w = get_positive("Width = ")
    print("\nArea = " + str(round(l * w, 6)))
    print("Perimeter = " + str(round(2 * (l + w), 6)))


def triangle():
    print("Enter the three side lengths:")
    a = get_positive("a = ")
    b = get_positive("b = ")
    c = get_positive("c = ")
    if a + b <= c or a + c <= b or b + c <= a:
        print("\nThose sides do not form a triangle.")
        return
    perimeter = a + b + c
    s = perimeter / 2.0
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    print("\nPerimeter = " + str(round(perimeter, 6)))
    print("Area = " + str(round(area, 6)))


def sphere():
    r = get_positive("Radius = ")
    volume = (4.0 / 3.0) * pi * r ** 3
    surface = 4 * pi * r * r
    print("\nVolume = " + str(round(volume, 6)))
    print("Surface area = " + str(round(surface, 6)))


def cylinder():
    r = get_positive("Radius = ")
    h = get_positive("Height = ")
    volume = pi * r * r * h
    surface = 2 * pi * r * h + 2 * pi * r * r
    print("\nVolume = " + str(round(volume, 6)))
    print("Surface area = " + str(round(surface, 6)))


def cone():
    r = get_positive("Radius = ")
    h = get_positive("Height = ")
    slant = sqrt(r * r + h * h)
    volume = (1.0 / 3.0) * pi * r * r * h
    surface = pi * r * slant + pi * r * r
    print("\nSlant height = " + str(round(slant, 6)))
    print("Volume = " + str(round(volume, 6)))
    print("Surface area = " + str(round(surface, 6)))


def rectangular_prism():
    l = get_positive("Length = ")
    w = get_positive("Width = ")
    h = get_positive("Height = ")
    volume = l * w * h
    surface = 2 * (l * w + l * h + w * h)
    print("\nVolume = " + str(round(volume, 6)))
    print("Surface area = " + str(round(surface, 6)))


def main():
    print("=== GEOM ===")
    while True:
        print("\n-- 2D shapes --")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Triangle (SSS)")
        print("-- 3D solids --")
        print("4. Sphere")
        print("5. Cylinder")
        print("6. Cone")
        print("7. Rectangular Prism")
        print("0. Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                circle()
            elif choice == "2":
                rectangle()
            elif choice == "3":
                triangle()
            elif choice == "4":
                sphere()
            elif choice == "5":
                cylinder()
            elif choice == "6":
                cone()
            elif choice == "7":
                rectangular_prism()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except Exception:
            print("Could not compute with those values.")
    print("Bye.")


main()
