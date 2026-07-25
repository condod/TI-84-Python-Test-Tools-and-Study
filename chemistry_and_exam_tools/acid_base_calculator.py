# Program: acid_base_calculator
# Purpose: Three acid/base tools in one menu: (1) pH and pOH from a
#          given [H+] or [OH-] concentration (mol/L), (2) [H+]/[OH-]
#          back-calculated from a given pH or pOH, and (3) buffer pH
#          via the Henderson-Hasselbalch equation, pH = pKa +
#          log10([A-]/[HA]).
# Usage: Pick a tool from the menu and enter the requested value(s).
#        Prints the computed result(s). Assumes 25 C (Kw = 1.0e-14).

from math import log10

KW = 1.0e-14  # water autoionization constant at 25 C


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def ph_poh_from_concentration():
    print("\n1. From [H+] (mol/L)")
    print("2. From [OH-] (mol/L)")
    choice = input("Choice (1-2): ").strip()
    if choice == "1":
        h = get_float("[H+] (mol/L) = ")
        if h <= 0:
            print("[H+] must be a positive number.")
            return
        ph = -log10(h)
    elif choice == "2":
        oh = get_float("[OH-] (mol/L) = ")
        if oh <= 0:
            print("[OH-] must be a positive number.")
            return
        poh = -log10(oh)
        ph = 14.0 - poh
        h = KW / oh
    else:
        print("Invalid choice.")
        return

    poh = 14.0 - ph
    oh = KW / h
    print("\npH  = " + str(round(ph, 4)))
    print("pOH = " + str(round(poh, 4)))
    print("[H+]  = " + str(h) + " mol/L")
    print("[OH-] = " + str(oh) + " mol/L")
    if ph < 7:
        print("Solution is acidic.")
    elif ph > 7:
        print("Solution is basic.")
    else:
        print("Solution is neutral.")


def concentration_from_ph_poh():
    print("\n1. From pH")
    print("2. From pOH")
    choice = input("Choice (1-2): ").strip()
    if choice == "1":
        ph = get_float("pH = ")
        poh = 14.0 - ph
    elif choice == "2":
        poh = get_float("pOH = ")
        ph = 14.0 - poh
    else:
        print("Invalid choice.")
        return

    h = 10 ** (-ph)
    oh = 10 ** (-poh)
    print("\npH  = " + str(round(ph, 4)))
    print("pOH = " + str(round(poh, 4)))
    print("[H+]  = " + str(h) + " mol/L")
    print("[OH-] = " + str(oh) + " mol/L")


def henderson_hasselbalch():
    print("\nHenderson-Hasselbalch: pH = pKa + log10([A-]/[HA])")
    pka = get_float("pKa = ")
    a_minus = get_float("[A-] (conjugate base, mol/L) = ")
    ha = get_float("[HA] (weak acid, mol/L) = ")
    if a_minus <= 0 or ha <= 0:
        print("Both concentrations must be positive numbers.")
        return
    ph = pka + log10(a_minus / ha)
    print("\nBuffer pH = " + str(round(ph, 4)))


def main():
    print("=== Acid/Base Calculator ===")
    while True:
        print("\n1. pH/pOH from [H+] or [OH-]")
        print("2. [H+]/[OH-] from pH or pOH")
        print("3. Buffer pH (Henderson-Hasselbalch)")
        print("4. Quit")
        choice = input("Choice (1-4): ").strip()
        if choice == "1":
            ph_poh_from_concentration()
        elif choice == "2":
            concentration_from_ph_poh()
        elif choice == "3":
            henderson_hasselbalch()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
    print("Done.")


main()
