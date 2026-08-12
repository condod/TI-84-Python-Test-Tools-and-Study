# On-calc name: GASLAW
# Program: ideal_gas_law
# Purpose: Two tools: (1) Ideal Gas Law PV=nRT solver for P, V, n, or T
#          given the other three (SI-ish units: P in kPa, V in L,
#          n in mol, T in K, R = 8.314 L*kPa/(mol*K)); (2) Combined Gas
#          Law solver for P1V1/T1 = P2V2/T2 given five of six values.
# Usage: Pick a tool from the menu and enter the requested known
#        values (any consistent units for the combined gas law, since
#        it uses ratios). Prints the solved unknown.

R = 8.314  # L*kPa / (mol*K)


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def ideal_gas():
    print("\nIdeal Gas Law: P*V = n*R*T   (P in kPa, V in L, n in mol, T in K)")
    print("Solve for: 1=P  2=V  3=n  4=T")
    choice = input("Choice (1-4): ").strip()
    try:
        if choice == "1":
            v = get_float("V (L) = ")
            n = get_float("n (mol) = ")
            t = get_float("T (K) = ")
            if v == 0:
                print("V cannot be 0.")
                return
            print("P = nRT/V = " + str(round(n * R * t / v, 6)) + " kPa")
        elif choice == "2":
            p = get_float("P (kPa) = ")
            n = get_float("n (mol) = ")
            t = get_float("T (K) = ")
            if p == 0:
                print("P cannot be 0.")
                return
            print("V = nRT/P = " + str(round(n * R * t / p, 6)) + " L")
        elif choice == "3":
            p = get_float("P (kPa) = ")
            v = get_float("V (L) = ")
            t = get_float("T (K) = ")
            if t == 0:
                print("T cannot be 0.")
                return
            print("n = PV/RT = " + str(round(p * v / (R * t), 6)) + " mol")
        elif choice == "4":
            p = get_float("P (kPa) = ")
            v = get_float("V (L) = ")
            n = get_float("n (mol) = ")
            if n == 0:
                print("n cannot be 0.")
                return
            print("T = PV/nR = " + str(round(p * v / (n * R), 6)) + " K")
        else:
            print("Invalid choice.")
    except Exception:
        print("Could not compute with those values.")


def combined_gas():
    print("\nCombined Gas Law: P1*V1/T1 = P2*V2/T2")
    print("Enter 5 known values; leave the UNKNOWN one blank when prompted.")
    labels = ["P1", "V1", "T1", "P2", "V2", "T2"]

    while True:
        vals = {}
        blank_label = None
        bad_entry = False
        for label in labels:
            raw = input(label + " (blank if this is the unknown) = ").strip()
            if raw == "":
                if blank_label is not None:
                    print("Only one value can be blank. Let's try again.")
                    bad_entry = True
                    break
                blank_label = label
            else:
                try:
                    vals[label] = float(raw)
                except (ValueError, TypeError):
                    print("Invalid number. Let's try again.")
                    bad_entry = True
                    break

        if bad_entry:
            continue
        if blank_label is None:
            print("Please leave exactly one field blank (the unknown). Let's try again.")
            continue
        break

    try:
        p1 = vals.get("P1")
        v1 = vals.get("V1")
        t1 = vals.get("T1")
        p2 = vals.get("P2")
        v2 = vals.get("V2")
        t2 = vals.get("T2")

        if blank_label == "P1":
            result = p2 * v2 * t1 / (t2 * v1)
        elif blank_label == "V1":
            result = p2 * v2 * t1 / (t2 * p1)
        elif blank_label == "T1":
            result = p1 * v1 * t2 / (p2 * v2)
        elif blank_label == "P2":
            result = p1 * v1 * t2 / (t1 * v2)
        elif blank_label == "V2":
            result = p1 * v1 * t2 / (t1 * p2)
        else:
            result = p2 * v2 * t1 / (p1 * v1)

        print("\n" + blank_label + " = " + str(round(result, 6)))
    except ZeroDivisionError:
        print("Cannot solve: one of the known values is 0 in a way that causes division by zero.")
    except Exception:
        print("Could not compute with those values.")


def main():
    print("=== GASLAW ===")
    while True:
        print("\n1. Ideal Gas PV=nRT")
        print("2. Combined Gas")
        print("0. Quit")
        choice = input("> ").strip()
        if choice == "1":
            ideal_gas()
        elif choice == "2":
            combined_gas()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
    print("Bye.")


main()
