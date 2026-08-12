# On-calc name: DILUTION
# Program: dilution_calculator
# Purpose: Solution-prep helper built on C1*V1 = C2*V2. Solves for any
#          one of the four values, reports how much diluent to add,
#          computes dilution factors, plans a serial dilution, and
#          converts between molarity, moles, and mass for a known
#          molar mass.
# Usage: Pick a tool from the menu. Concentrations must share one unit
#        (all molar, or all percent) and volumes must share one unit
#        (all mL, or all L) -- the equation is a ratio, so any
#        consistent pair works and answers come back in the same units.
#        Leave the unknown out; the program asks only for what it needs.

MAX_STEPS = 20


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


def solve_c1v1():
    print("\nC1*V1 = C2*V2   (stock on the left, diluted on the right)")
    print("Solve for:")
    print("1. C1 (stock concentration)")
    print("2. V1 (stock volume to take)")
    print("3. C2 (final concentration)")
    print("4. V2 (final volume)")
    choice = input("> ").strip()

    if choice == "1":
        v1 = get_positive("V1 (stock volume) = ")
        c2 = get_positive("C2 (final concentration) = ")
        v2 = get_positive("V2 (final volume) = ")
        print("\nC1 = C2*V2/V1 = " + str(round(c2 * v2 / v1, 6)))
    elif choice == "2":
        c1 = get_positive("C1 (stock concentration) = ")
        c2 = get_positive("C2 (final concentration) = ")
        v2 = get_positive("V2 (final volume) = ")
        if c2 > c1:
            print("\nC2 is greater than C1: you cannot make a solution")
            print("more concentrated by diluting it.")
            return
        v1 = c2 * v2 / c1
        print("\nV1 = C2*V2/C1 = " + str(round(v1, 6)))
        print("Diluent to add = V2 - V1 = " + str(round(v2 - v1, 6)))
        print("Dilution factor = " + str(round(v2 / v1, 6)) + "-fold")
    elif choice == "3":
        c1 = get_positive("C1 (stock concentration) = ")
        v1 = get_positive("V1 (stock volume) = ")
        v2 = get_positive("V2 (final volume) = ")
        print("\nC2 = C1*V1/V2 = " + str(round(c1 * v1 / v2, 6)))
        print("Dilution factor = " + str(round(v2 / v1, 6)) + "-fold")
    elif choice == "4":
        c1 = get_positive("C1 (stock concentration) = ")
        v1 = get_positive("V1 (stock volume) = ")
        c2 = get_positive("C2 (final concentration) = ")
        if c2 > c1:
            print("\nC2 is greater than C1: you cannot make a solution")
            print("more concentrated by diluting it.")
            return
        v2 = c1 * v1 / c2
        print("\nV2 = C1*V1/C2 = " + str(round(v2, 6)))
        print("Diluent to add = V2 - V1 = " + str(round(v2 - v1, 6)))
    else:
        print("Invalid choice.")


def dilution_factor():
    print("\n1. From stock and final volume")
    print("2. From stock and final concentration")
    choice = input("> ").strip()
    if choice == "1":
        v1 = get_positive("V1 (stock volume) = ")
        v2 = get_positive("V2 (final volume) = ")
        print("\nDilution factor = " + str(round(v2 / v1, 6)) + "-fold")
        print("Written as 1:" + str(round(v2 / v1, 4)))
    elif choice == "2":
        c1 = get_positive("C1 (stock concentration) = ")
        c2 = get_positive("C2 (final concentration) = ")
        print("\nDilution factor = " + str(round(c1 / c2, 6)) + "-fold")
        print("Written as 1:" + str(round(c1 / c2, 4)))
    else:
        print("Invalid choice.")


def serial_dilution():
    print("\nSerial dilution: the same fold-dilution repeated.")
    c1 = get_positive("Starting concentration = ")
    fold = get_positive("Fold dilution per step (10 = 1:10) = ")
    if fold <= 1:
        print("Fold dilution must be greater than 1.")
        return
    while True:
        steps = int(get_positive("Number of steps = "))
        if steps > MAX_STEPS:
            print("Please keep steps at or below " + str(MAX_STEPS) + ".")
            continue
        break

    volume = get_float("Volume per tube (0 to skip) = ")
    if volume > 0:
        transfer = volume / fold
        print("\nPer tube: transfer " + str(round(transfer, 6)) +
              " into " + str(round(volume - transfer, 6)) + " of diluent.")

    print("\nStep  Concentration")
    concentration = c1
    print("   0  " + str(round(concentration, 10)))
    for step in range(1, steps + 1):
        concentration = concentration / fold
        print(("   " + str(step))[-4:] + "  " + str(round(concentration, 10)))
    print("\nTotal dilution = " + str(round(c1 / concentration, 6)) + "-fold")


def molarity_tools():
    print("\n1. Molarity from moles and volume")
    print("2. Mass needed for a target molarity")
    print("3. Moles from molarity and volume")
    choice = input("> ").strip()
    if choice == "1":
        moles = get_positive("Moles of solute (mol) = ")
        litres = get_positive("Volume of solution (L) = ")
        print("\nMolarity = " + str(round(moles / litres, 6)) + " mol/L")
    elif choice == "2":
        molarity = get_positive("Target molarity (mol/L) = ")
        litres = get_positive("Volume to make (L) = ")
        molar_mass = get_positive("Molar mass (g/mol) = ")
        moles = molarity * litres
        print("\nMoles needed = " + str(round(moles, 6)) + " mol")
        print("Mass needed = " + str(round(moles * molar_mass, 6)) + " g")
    elif choice == "3":
        molarity = get_positive("Molarity (mol/L) = ")
        litres = get_positive("Volume (L) = ")
        print("\nMoles = " + str(round(molarity * litres, 6)) + " mol")
    else:
        print("Invalid choice.")


def main():
    print("=== DILUTION ===")
    while True:
        print("\n1. C1V1 = C2V2 solver")
        print("2. Dilution factor")
        print("3. Serial dilution plan")
        print("4. Molarity / mass tools")
        print("0. Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                solve_c1v1()
            elif choice == "2":
                dilution_factor()
            elif choice == "3":
                serial_dilution()
            elif choice == "4":
                molarity_tools()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except (ValueError, OverflowError, ZeroDivisionError):
            print("Could not compute with those values.")
    print("Bye.")


main()
