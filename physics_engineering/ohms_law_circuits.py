# On-calc name: OHMS
# Program: ohms_law_circuits
# Purpose: Menu-driven DC circuit helper. Part 1 solves Ohm's Law /
#          power relations for V, I, R, or P given two of the four
#          quantities. Part 2 combines a list of resistors in series
#          or parallel.
# Usage: Pick "Ohm's Law" and choose the unknown, then enter two known
#        values from V (volts), I (amps), R (ohms), P (watts).
#        Pick "Resistor combiner" to enter several resistor values and
#        get the series or parallel equivalent resistance.

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def solve_ohms():
    print("\nSolve for: 1=V  2=I  3=R  4=P")
    choice = input("Choice (1-4): ").strip()
    try:
        if choice == "1":
            i = get_float("I (amps) = ")
            r = get_float("R (ohms) = ")
            print("V = I*R = " + str(round(i * r, 6)) + " V")
        elif choice == "2":
            v = get_float("V (volts) = ")
            r = get_float("R (ohms) = ")
            if r == 0:
                print("R cannot be 0.")
                return
            print("I = V/R = " + str(round(v / r, 6)) + " A")
        elif choice == "3":
            v = get_float("V (volts) = ")
            i = get_float("I (amps) = ")
            if i == 0:
                print("I cannot be 0.")
                return
            print("R = V/I = " + str(round(v / i, 6)) + " ohms")
        elif choice == "4":
            v = get_float("V (volts) = ")
            i = get_float("I (amps) = ")
            print("P = V*I = " + str(round(v * i, 6)) + " W")
        else:
            print("Invalid choice.")
    except Exception:
        print("Could not compute with those values.")


def combine_resistors():
    print("\n1=Series  2=Parallel")
    mode = input("Choice (1-2): ").strip()
    if mode not in ("1", "2"):
        print("Invalid choice.")
        return

    values = []
    print("Enter resistor values (blank line to finish, max 20):")
    while len(values) < 20:
        raw = input("R" + str(len(values) + 1) + " (ohms) = ").strip()
        if raw == "":
            break
        try:
            r = float(raw)
            if r <= 0:
                print("Resistance must be positive.")
                continue
            values.append(r)
        except (ValueError, TypeError):
            print("Please enter a valid number.")

    if len(values) < 1:
        print("No resistors entered.")
        return

    if mode == "1":
        total = sum(values)
        print("Series equivalent R = " + str(round(total, 6)) + " ohms")
    else:
        recip_sum = sum(1.0 / r for r in values)
        total = 1.0 / recip_sum
        print("Parallel equivalent R = " + str(round(total, 6)) + " ohms")


def main():
    print("=== OHMS ===")
    while True:
        print("\n1. Ohm/Power")
        print("2. Series/Parallel R")
        print("0. Quit")
        choice = input("> ").strip()
        if choice == "1":
            solve_ohms()
        elif choice == "2":
            combine_resistors()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
    print("Bye.")


main()
