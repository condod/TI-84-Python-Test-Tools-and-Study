# On-calc name: STRESS
# Program: stress_strain
# Purpose: Axial stress and strain for a bar in tension or compression:
#          normal stress sigma = F/A, normal strain eps = dL/L0,
#          Young's modulus E = sigma/eps, axial deformation
#          dL = F*L0/(A*E), factor of safety, and lateral strain from
#          Poisson's ratio. Includes a small table of common material
#          moduli so a quick check does not need a textbook.
# Usage: Pick a tool and enter values in consistent SI units: force in
#        newtons, area in m^2, length in m, and modulus in pascals.
#        Answers come back in pascals; the program also prints MPa and
#        GPa because those are what material data is usually quoted in.
#        Area helpers convert a round or rectangular cross-section.

from math import pi, sqrt

MATERIALS = [
    ("Steel", 200e9, 250e6),
    ("Aluminium", 69e9, 95e6),
    ("Copper", 117e9, 70e6),
    ("Concrete", 30e9, 3e6),
    ("Oak (along grain)", 11e9, 40e6),
    ("Glass", 70e9, 50e6),
]


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def get_positive(prompt):
    while True:
        value = get_float(prompt)
        if value <= 0:
            print("Please enter a positive number.")
            continue
        return value


def show_pressure(label, pascals):
    print(label + " = " + str(round(pascals, 4)) + " Pa")
    print("  = " + str(round(pascals / 1e6, 6)) + " MPa")
    print("  = " + str(round(pascals / 1e9, 9)) + " GPa")


def get_area():
    print("\nCross-sectional area:")
    print("1. Enter area directly (m^2)")
    print("2. Round bar from diameter (m)")
    print("3. Rectangle from width x height (m)")
    choice = input("> ").strip()
    if choice == "2":
        d = get_positive("Diameter (m) = ")
        area = pi * d * d / 4.0
        print("Area = " + str(round(area, 10)) + " m^2")
        return area
    if choice == "3":
        w = get_positive("Width (m) = ")
        h = get_positive("Height (m) = ")
        area = w * h
        print("Area = " + str(round(area, 10)) + " m^2")
        return area
    return get_positive("Area A (m^2) = ")


def stress_only():
    force = get_float("Force F (N, negative = compression) = ")
    area = get_area()
    stress = force / area
    print("")
    show_pressure("Stress sigma = F/A", stress)
    if stress < 0:
        print("(Compressive)")
    elif stress > 0:
        print("(Tensile)")


def strain_only():
    print("\n1. From change in length")
    print("2. From original and final length")
    choice = input("> ").strip()
    if choice == "2":
        l0 = get_positive("Original length L0 (m) = ")
        lf = get_positive("Final length Lf (m) = ")
        delta = lf - l0
    else:
        l0 = get_positive("Original length L0 (m) = ")
        delta = get_float("Change in length dL (m) = ")

    strain = delta / l0
    print("\nStrain eps = dL/L0 = " + str(round(strain, 9)))
    print("As a percent = " + str(round(strain * 100.0, 6)) + " %")
    print("In microstrain = " + str(round(strain * 1e6, 4)) + " ue")


def modulus():
    print("\nE = sigma/eps. Enter what you know.")
    stress = get_float("Stress sigma (Pa) = ")
    strain = get_float("Strain eps (unitless) = ")
    if strain == 0:
        print("\nStrain of 0 gives an undefined modulus.")
        return
    print("")
    show_pressure("Young's modulus E", stress / strain)


def deformation():
    print("\ndL = F*L0/(A*E)")
    force = get_float("Force F (N) = ")
    l0 = get_positive("Original length L0 (m) = ")
    area = get_area()
    e_mod = get_positive("Young's modulus E (Pa) = ")

    delta = force * l0 / (area * e_mod)
    stress = force / area
    strain = delta / l0

    print("\nElongation dL = " + str(round(delta, 9)) + " m")
    print("  = " + str(round(delta * 1000.0, 6)) + " mm")
    print("Strain = " + str(round(strain, 9)))
    print("")
    show_pressure("Stress", stress)
    print("Final length = " + str(round(l0 + delta, 9)) + " m")


def safety_factor():
    print("\nFactor of safety = strength / actual stress.")
    strength = get_positive("Yield (or ultimate) strength (Pa) = ")
    print("1. I know the actual stress")
    print("2. Compute it from force and area")
    choice = input("> ").strip()
    if choice == "2":
        force = get_float("Force F (N) = ")
        area = get_area()
        actual = abs(force / area)
    else:
        actual = abs(get_float("Actual stress (Pa) = "))

    if actual == 0:
        print("\nWith no stress the factor of safety is unbounded.")
        return
    fos = strength / actual
    print("")
    show_pressure("Actual stress", actual)
    print("\nFactor of safety = " + str(round(fos, 6)))
    if fos < 1:
        print("Below 1: the part is past its strength and fails.")
    elif fos < 1.5:
        print("Thin margin for most design codes.")
    else:
        print("Comfortable margin.")

    print("\nMaximum safe force for FOS = 1:")
    print("  depends on area; use the deformation tool for details.")


def poisson():
    print("\nLateral strain = -nu * axial strain.")
    nu = get_float("Poisson's ratio nu (steel ~0.30) = ")
    axial = get_float("Axial strain eps = ")
    d0 = get_float("Original diameter/width (m, 0 to skip) = ")

    lateral = -nu * axial
    print("\nLateral strain = " + str(round(lateral, 9)))
    if d0 > 0:
        change = lateral * d0
        print("Change in that dimension = " + str(round(change, 9)) + " m")
        print("New dimension = " + str(round(d0 + change, 9)) + " m")
    if axial > 0:
        print("(Stretching lengthwise, so it thins sideways.)")
    elif axial < 0:
        print("(Squashing lengthwise, so it bulges sideways.)")


def material_table():
    print("\nTypical values (approximate):")
    print("Material            E (GPa)  Yield (MPa)")
    for name, e_mod, yield_strength in MATERIALS:
        line = name
        while len(line) < 20:
            line += " "
        line += str(round(e_mod / 1e9, 1))
        while len(line) < 29:
            line += " "
        line += str(round(yield_strength / 1e6, 1))
        print(line)
    print("\nUse your own course's data sheet when it differs.")


def main():
    print("=== STRESS ===")
    print("SI units: N, m, m^2, Pa.")
    while True:
        print("\n1. Stress from force and area")
        print("2. Strain from lengths")
        print("3. Young's modulus")
        print("4. Axial deformation dL")
        print("5. Factor of safety")
        print("6. Poisson's ratio effect")
        print("7. Material property table")
        print("0. Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                stress_only()
            elif choice == "2":
                strain_only()
            elif choice == "3":
                modulus()
            elif choice == "4":
                deformation()
            elif choice == "5":
                safety_factor()
            elif choice == "6":
                poisson()
            elif choice == "7":
                material_table()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except (ValueError, OverflowError, ZeroDivisionError):
            print("Could not compute with those values.")
    print("Bye.")


main()
