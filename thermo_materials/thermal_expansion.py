# On-calc name: EXPAND
# Program: thermal_expansion
# Purpose: Thermal expansion in one, two, and three dimensions:
#          dL = alpha*L0*dT, dA = 2*alpha*A0*dT, dV = beta*V0*dT, plus
#          the thermal stress that builds up when a bar is held between
#          rigid supports and cannot expand (sigma = E*alpha*dT), and
#          the bimetallic-strip mismatch between two materials.
# Usage: Pick a tool and enter the coefficient of linear expansion
#        alpha in per-degree (steel is about 12e-6 /C, entered as
#        0.000012 or 12e-6). Temperature change dT can be in C or K
#        since only the difference matters. Lengths, areas, and volumes
#        come back in the units you entered them in.

# alpha in 1/C, E in Pa
MATERIALS = [
    ("Steel", 12e-6, 200e9),
    ("Aluminium", 23e-6, 69e9),
    ("Copper", 17e-6, 117e9),
    ("Concrete", 12e-6, 30e9),
    ("Glass (common)", 9e-6, 70e9),
    ("Invar", 1.2e-6, 141e9),
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


def get_alpha():
    print("\n1. Enter alpha directly")
    print("2. Pick a material")
    choice = input("> ").strip()
    if choice == "2":
        return pick_material()[1]
    return get_float("alpha (per degree, e.g. 12e-6) = ")


def pick_material():
    print("")
    for i, item in enumerate(MATERIALS):
        print(str(i + 1) + ". " + item[0] + "  alpha=" +
              str(round(item[1] * 1e6, 2)) + "e-6")
    while True:
        choice = input("> ").strip()
        for i, item in enumerate(MATERIALS):
            if choice == str(i + 1):
                return item
        print("Invalid choice.")


def linear():
    print("\ndL = alpha * L0 * dT")
    l0 = get_positive("Original length L0 = ")
    alpha = get_alpha()
    dt = get_float("Temperature change dT = ")

    delta = alpha * l0 * dt
    print("\ndL = " + str(round(delta, 9)))
    print("New length = " + str(round(l0 + delta, 9)))
    print("Strain = " + str(round(alpha * dt, 9)))
    if delta > 0:
        print("(Heated, so it grows.)")
    elif delta < 0:
        print("(Cooled, so it shrinks.)")


def area():
    print("\ndA = 2 * alpha * A0 * dT  (holes expand too)")
    a0 = get_positive("Original area A0 = ")
    alpha = get_alpha()
    dt = get_float("Temperature change dT = ")

    delta = 2.0 * alpha * a0 * dt
    print("\ndA = " + str(round(delta, 9)))
    print("New area = " + str(round(a0 + delta, 9)))
    print("A hole in a plate expands exactly like the")
    print("solid material would, so gaps get bigger too.")


def volume():
    print("\ndV = beta * V0 * dT, with beta = 3 * alpha for a solid")
    v0 = get_positive("Original volume V0 = ")
    print("1. I have alpha (linear)")
    print("2. I have beta (volumetric)")
    choice = input("> ").strip()
    if choice == "2":
        beta = get_float("beta (per degree) = ")
    else:
        beta = 3.0 * get_alpha()
        print("beta = 3*alpha = " + str(round(beta, 10)))
    dt = get_float("Temperature change dT = ")

    delta = beta * v0 * dt
    print("\ndV = " + str(round(delta, 9)))
    print("New volume = " + str(round(v0 + delta, 9)))


def thermal_stress():
    print("\nHeld between rigid supports: sigma = E * alpha * dT")
    print("(The bar cannot expand, so the strain it 'wants'")
    print("becomes stress instead. Length cancels out.)")
    print("\n1. Enter E and alpha")
    print("2. Pick a material")
    choice = input("> ").strip()
    if choice == "2":
        material = pick_material()
        alpha = material[1]
        e_mod = material[2]
        print("Using " + material[0] + ": E = " +
              str(round(e_mod / 1e9, 2)) + " GPa")
    else:
        alpha = get_float("alpha (per degree) = ")
        e_mod = get_positive("Young's modulus E (Pa) = ")
    dt = get_float("Temperature change dT = ")

    stress = e_mod * alpha * dt
    print("\nsigma = " + str(round(stress, 4)) + " Pa")
    print("  = " + str(round(stress / 1e6, 6)) + " MPa")
    if stress > 0:
        print("Heating a restrained bar puts it in COMPRESSION.")
    elif stress < 0:
        print("Cooling a restrained bar puts it in TENSION.")

    force_area = get_float("Cross-section area (m^2, 0 to skip) = ")
    if force_area > 0:
        print("Force on the supports = " +
              str(round(abs(stress) * force_area, 4)) + " N")


def gap_needed():
    print("\nExpansion gap for a run of segments (rails, pipes).")
    l0 = get_positive("Length of one segment = ")
    alpha = get_alpha()
    dt = get_float("Largest expected temperature rise dT = ")

    gap = alpha * l0 * dt
    print("\nGap needed per joint = " + str(round(gap, 9)))
    count = get_float("Number of segments (0 to skip) = ")
    if count > 0:
        print("Total expansion over " + str(round(count, 0)) +
              " segments = " + str(round(gap * count, 9)))


def bimetallic():
    print("\nBimetallic strip: two metals bonded together bend")
    print("because they expand by different amounts.")
    l0 = get_positive("Strip length L0 = ")
    print("Metal 1:")
    alpha1 = get_float("  alpha 1 (per degree) = ")
    print("Metal 2:")
    alpha2 = get_float("  alpha 2 (per degree) = ")
    dt = get_float("Temperature change dT = ")

    d1 = alpha1 * l0 * dt
    d2 = alpha2 * l0 * dt
    print("\nMetal 1 grows by " + str(round(d1, 9)))
    print("Metal 2 grows by " + str(round(d2, 9)))
    print("Mismatch = " + str(round(abs(d1 - d2), 9)))
    if abs(d1 - d2) < 1e-15:
        print("Equal expansion, so the strip stays flat.")
    elif d1 > d2:
        print("Metal 1 grows more, so the strip curves toward metal 2.")
    else:
        print("Metal 2 grows more, so the strip curves toward metal 1.")


def main():
    print("=== EXPAND ===")
    while True:
        print("\n1. Linear expansion dL")
        print("2. Area expansion dA")
        print("3. Volume expansion dV")
        print("4. Thermal stress (restrained)")
        print("5. Expansion gap needed")
        print("6. Bimetallic strip")
        print("0. Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                linear()
            elif choice == "2":
                area()
            elif choice == "3":
                volume()
            elif choice == "4":
                thermal_stress()
            elif choice == "5":
                gap_needed()
            elif choice == "6":
                bimetallic()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except (ValueError, OverflowError, ZeroDivisionError):
            print("Could not compute with those values.")
    print("Bye.")


main()
