# On-calc name: SAVOL
# Program: surface_area_volume
# Purpose: Surface-area-to-volume ratio for the shapes used as cell and
#          organism models (sphere, cube, cylinder, flattened box), plus
#          metabolic scaling by Kleiber's law (BMR proportional to
#          M^0.75) and the diffusion-distance argument for why cells
#          stay small.
# Usage: Pick a shape and enter its dimensions in any one length unit;
#        area comes back in that unit squared, volume in that unit
#        cubed, and the SA:V ratio in per-unit. The scaling tool shows
#        how SA:V changes when a shape is scaled up, and the metabolic
#        tool estimates basal metabolic rate from body mass in kg.

from math import pi, sqrt

KLEIBER_COEFFICIENT = 70.0   # kcal/day for mammals when mass is in kg
KLEIBER_EXPONENT = 0.75


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


def report(area, volume, note):
    print("\nSurface area = " + str(round(area, 6)))
    print("Volume = " + str(round(volume, 6)))
    if volume > 0:
        print("SA:V ratio = " + str(round(area / volume, 6)) + " per unit")
        print(note)


def sphere():
    r = get_positive("Radius r = ")
    area = 4.0 * pi * r * r
    volume = 4.0 / 3.0 * pi * r * r * r
    report(area, volume, "(For a sphere SA:V = 3/r, so it falls as r grows.)")


def cube():
    s = get_positive("Edge length s = ")
    area = 6.0 * s * s
    volume = s * s * s
    report(area, volume, "(For a cube SA:V = 6/s.)")


def cylinder():
    r = get_positive("Radius r = ")
    h = get_positive("Height h = ")
    area = 2.0 * pi * r * r + 2.0 * pi * r * h
    volume = pi * r * r * h
    report(area, volume, "(Includes both circular ends.)")


def box():
    length = get_positive("Length = ")
    width = get_positive("Width = ")
    height = get_positive("Height = ")
    area = 2.0 * (length * width + length * height + width * height)
    volume = length * width * height
    report(area, volume,
           "(Flattening a box raises SA:V at the same volume.)")


def scaling():
    print("\nHow SA:V changes when a shape is scaled up.")
    print("Doubling every length multiplies area by k^2")
    print("and volume by k^3, so SA:V is divided by k.")
    ratio = get_positive("Current SA:V ratio = ")
    factor = get_positive("Scale factor k (2 = twice as long) = ")
    print("\nNew SA:V = " + str(round(ratio / factor, 6)) + " per unit")
    print("Area x " + str(round(factor * factor, 4)) +
          ", volume x " + str(round(factor ** 3, 4)))
    print("This is why large organisms need gills, lungs, or")
    print("branching circulation instead of plain diffusion.")


def metabolic():
    print("\nKleiber's law: BMR = a * M^0.75 (M in kg).")
    mass = get_positive("Body mass M (kg) = ")
    coefficient = get_float("Coefficient a (blank-safe default 70) = ")
    if coefficient <= 0:
        coefficient = KLEIBER_COEFFICIENT
        print("Using a = 70 kcal/day.")

    bmr = coefficient * mass ** KLEIBER_EXPONENT
    print("\nBMR = " + str(round(bmr, 6)) + " kcal/day")
    print("Per kg of body mass = " + str(round(bmr / mass, 6)) +
          " kcal/day/kg")
    print("(Mass-specific rate falls as mass rises, matching SA:V.)")


def diffusion():
    print("\nDiffusion time grows with the square of distance:")
    print("t ~ x^2 / (2D).")
    distance = get_positive("Distance x (cm) = ")
    coefficient = get_positive("Diffusion coefficient D (cm^2/s) = ")
    seconds = distance * distance / (2.0 * coefficient)
    print("\nTime ~ " + str(round(seconds, 6)) + " s")
    if seconds > 3600:
        print("        = " + str(round(seconds / 3600.0, 4)) + " hours")
    print("Doubling the distance quadruples the time, which")
    print("is the limit on how thick a diffusing cell can be.")
    print("Distance reachable in 1 s = " +
          str(round(sqrt(2.0 * coefficient), 6)) + " cm")


def main():
    print("=== SAVOL ===")
    while True:
        print("\n1. Sphere")
        print("2. Cube")
        print("3. Cylinder")
        print("4. Rectangular box")
        print("5. Scaling effect on SA:V")
        print("6. Metabolic rate (Kleiber)")
        print("7. Diffusion distance & time")
        print("0. Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                sphere()
            elif choice == "2":
                cube()
            elif choice == "3":
                cylinder()
            elif choice == "4":
                box()
            elif choice == "5":
                scaling()
            elif choice == "6":
                metabolic()
            elif choice == "7":
                diffusion()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except (ValueError, OverflowError, ZeroDivisionError):
            print("Could not compute with those values.")
    print("Bye.")


main()
