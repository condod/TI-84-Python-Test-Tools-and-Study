# On-calc name: MOLAR
# Program: stoichiometry_molar_mass
# Purpose: Two tools: (1) compute a compound's molar mass from element
#          symbols and atom counts you enter (using a built-in table
#          of common element molar masses), and (2) convert between
#          mass (g) and moles (mol) using a molar mass you provide or
#          one just calculated.
# Usage: Pick "Molar mass from formula" and enter element symbol/count
#        pairs (blank symbol to finish), e.g. C,1 then H,4 for CH4.
#        Pick "Mass <-> moles" and enter molar mass plus either mass
#        or moles to get the other.

ELEMENTS = {
    "H": 1.008, "HE": 4.003, "LI": 6.94, "BE": 9.012, "B": 10.81,
    "C": 12.011, "N": 14.007, "O": 15.999, "F": 18.998, "NE": 20.180,
    "NA": 22.990, "MG": 24.305, "AL": 26.982, "SI": 28.085, "P": 30.974,
    "S": 32.06, "CL": 35.45, "AR": 39.948, "K": 39.098, "CA": 40.078,
    "TI": 47.867, "CR": 51.996, "MN": 54.938, "FE": 55.845, "NI": 58.693,
    "CU": 63.546, "ZN": 65.38, "BR": 79.904, "AG": 107.868, "SN": 118.71,
    "I": 126.904, "BA": 137.327, "PT": 195.084, "AU": 196.967, "HG": 200.59,
    "PB": 207.2,
}


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def get_positive_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n <= 0:
                print("Enter a positive whole number.")
                continue
            return n
        except (ValueError, TypeError):
            print("Please enter a whole number.")


def molar_mass_from_formula():
    print("\nEnter element symbol and atom count, one at a time.")
    print("Blank symbol to finish (max 15 elements). Example: C then 1")
    total = 0.0
    count = 0
    summary = []
    while count < 15:
        sym = input("Element symbol (blank to finish) = ").strip().upper()
        if sym == "":
            break
        if sym not in ELEMENTS:
            print("Unknown element symbol '" + sym + "'. Try a common element like C, H, O, N, CL, NA...")
            continue
        n = get_positive_int("  atom count = ")
        mass = ELEMENTS[sym] * n
        total += mass
        summary.append(sym + str(n) + " (" + str(round(mass, 3)) + " g/mol)")
        count += 1

    if count == 0:
        print("No elements entered.")
        return None

    print("\nFormula parts: " + ", ".join(summary))
    print("Molar mass = " + str(round(total, 4)) + " g/mol")
    return total


def mass_moles_conversion(molar_mass=None):
    print("\nMass <-> Moles Conversion")
    if molar_mass is None:
        molar_mass = get_float("Molar mass (g/mol) = ")
    else:
        use_it = input("Use molar mass just calculated (" + str(round(molar_mass, 4)) + " g/mol)? (y/n): ").strip().lower()
        if use_it != "y":
            molar_mass = get_float("Molar mass (g/mol) = ")

    if molar_mass <= 0:
        print("Molar mass must be positive.")
        return

    print("1. I have mass (g), find moles")
    print("2. I have moles (mol), find mass")
    choice = input("Choice (1-2): ").strip()
    if choice == "1":
        mass = get_float("Mass (g) = ")
        print("Moles = mass / molar mass = " + str(round(mass / molar_mass, 6)) + " mol")
    elif choice == "2":
        moles = get_float("Moles (mol) = ")
        print("Mass = moles * molar mass = " + str(round(moles * molar_mass, 6)) + " g")
    else:
        print("Invalid choice.")


def main():
    print("=== MOLAR ===")
    while True:
        print("\n1. Molar mass")
        print("2. Mass <-> moles")
        print("0. Quit")
        choice = input("> ").strip()
        if choice == "1":
            mm = molar_mass_from_formula()
            if mm is not None:
                again = input("\nConvert mass/moles using this molar mass? (y/n): ").strip().lower()
                if again == "y":
                    mass_moles_conversion(mm)
        elif choice == "2":
            mass_moles_conversion()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
    print("Bye.")


main()
