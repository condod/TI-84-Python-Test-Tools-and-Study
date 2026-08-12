# On-calc name: CARNOT
# Program: carnot_efficiency
# Purpose: Heat-engine and refrigeration cycle analysis. Computes the
#          Carnot (maximum possible) efficiency from reservoir
#          temperatures, the actual efficiency from heat and work,
#          coefficients of performance for refrigerators and heat
#          pumps, and compares a real cycle against the Carnot limit
#          to flag second-law violations.
# Usage: Pick a tool from the menu. Temperatures MUST be absolute
#        (kelvin) -- the program refuses Celsius-looking negatives and
#        offers a converter. Heat and work can be in any single energy
#        unit (J, kJ, BTU) as long as they match, since efficiency is
#        a ratio.


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def get_kelvin(prompt):
    while True:
        value = get_float(prompt)
        if value <= 0:
            print("Temperature must be above absolute zero (use kelvin).")
            continue
        return value


def get_positive(prompt):
    while True:
        value = get_float(prompt)
        if value <= 0:
            print("Please enter a positive number.")
            continue
        return value


def check_order(t_hot, t_cold):
    if t_cold >= t_hot:
        print("\nThe cold reservoir must be colder than the hot one.")
        return False
    return True


def carnot_engine():
    t_hot = get_kelvin("Hot reservoir Th (K) = ")
    t_cold = get_kelvin("Cold reservoir Tc (K) = ")
    if not check_order(t_hot, t_cold):
        return

    efficiency = 1.0 - t_cold / t_hot
    print("\nCarnot efficiency = 1 - Tc/Th")
    print("  = " + str(round(efficiency, 6)))
    print("  = " + str(round(efficiency * 100.0, 4)) + " %")
    print("\nNo engine between these reservoirs can beat that.")

    q_hot = get_float("Heat absorbed Qh (0 to skip) = ")
    if q_hot > 0:
        work = efficiency * q_hot
        print("\nMaximum work = " + str(round(work, 6)))
        print("Heat rejected Qc = " + str(round(q_hot - work, 6)))


def actual_engine():
    print("\n1. I know Qh and W")
    print("2. I know Qh and Qc")
    choice = input("> ").strip()

    if choice == "1":
        q_hot = get_positive("Heat absorbed Qh = ")
        work = get_float("Work output W = ")
        q_cold = q_hot - work
    elif choice == "2":
        q_hot = get_positive("Heat absorbed Qh = ")
        q_cold = get_float("Heat rejected Qc = ")
        work = q_hot - q_cold
    else:
        print("Invalid choice.")
        return

    efficiency = work / q_hot
    print("\nWork W = " + str(round(work, 6)))
    print("Heat rejected Qc = " + str(round(q_cold, 6)))
    print("Efficiency = W/Qh = " + str(round(efficiency, 6)))
    print("  = " + str(round(efficiency * 100.0, 4)) + " %")

    if q_cold < 0:
        print("\nQc is negative: that engine converts more than all")
        print("its input heat to work, which the first law forbids.")

    t_hot = get_float("Th (K, 0 to skip Carnot check) = ")
    if t_hot > 0:
        t_cold = get_kelvin("Tc (K) = ")
        if not check_order(t_hot, t_cold):
            return
        ideal = 1.0 - t_cold / t_hot
        print("\nCarnot limit = " + str(round(ideal * 100.0, 4)) + " %")
        if efficiency > ideal + 1e-9:
            print("This cycle beats the Carnot limit, which is")
            print("impossible: re-check the numbers.")
        else:
            print("Second law satisfied.")
            if ideal > 0:
                print("Fraction of the limit reached = " +
                      str(round(efficiency / ideal * 100.0, 4)) + " %")


def refrigerator():
    print("\nRefrigerator: COP = Qc/W (Carnot: Tc/(Th-Tc)).")
    t_hot = get_kelvin("Hot reservoir Th (K) = ")
    t_cold = get_kelvin("Cold reservoir Tc (K) = ")
    if not check_order(t_hot, t_cold):
        return

    cop = t_cold / (t_hot - t_cold)
    print("\nCarnot COP (cooling) = " + str(round(cop, 6)))
    print("Best case: every 1 unit of work moves " + str(round(cop, 4)))
    print("units of heat out of the cold space.")

    q_cold = get_float("Cooling load Qc (0 to skip) = ")
    if q_cold > 0:
        work = q_cold / cop
        print("\nMinimum work = " + str(round(work, 6)))
        print("Heat dumped to the hot side = " + str(round(q_cold + work, 6)))


def heat_pump():
    print("\nHeat pump: COP = Qh/W (Carnot: Th/(Th-Tc)).")
    t_hot = get_kelvin("Hot reservoir Th (K) = ")
    t_cold = get_kelvin("Cold reservoir Tc (K) = ")
    if not check_order(t_hot, t_cold):
        return

    cop = t_hot / (t_hot - t_cold)
    print("\nCarnot COP (heating) = " + str(round(cop, 6)))
    print("(Always exactly 1 more than the cooling COP.)")

    q_hot = get_float("Heating load Qh (0 to skip) = ")
    if q_hot > 0:
        work = q_hot / cop
        print("\nMinimum work = " + str(round(work, 6)))
        print("Heat drawn from the cold side = " + str(round(q_hot - work, 6)))


def convert_temperature():
    print("\n1. Celsius -> kelvin")
    print("2. Kelvin -> Celsius")
    print("3. Fahrenheit -> kelvin")
    choice = input("> ").strip()
    value = get_float("Value = ")
    if choice == "1":
        print("\n" + str(round(value, 4)) + " C = " +
              str(round(value + 273.15, 4)) + " K")
    elif choice == "2":
        print("\n" + str(round(value, 4)) + " K = " +
              str(round(value - 273.15, 4)) + " C")
    elif choice == "3":
        celsius = (value - 32.0) * 5.0 / 9.0
        print("\n" + str(round(value, 4)) + " F = " +
              str(round(celsius, 4)) + " C = " +
              str(round(celsius + 273.15, 4)) + " K")
    else:
        print("Invalid choice.")


def main():
    print("=== CARNOT ===")
    print("Temperatures in kelvin.")
    while True:
        print("\n1. Carnot efficiency (max possible)")
        print("2. Actual engine efficiency")
        print("3. Refrigerator COP")
        print("4. Heat pump COP")
        print("5. Temperature converter")
        print("0. Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                carnot_engine()
            elif choice == "2":
                actual_engine()
            elif choice == "3":
                refrigerator()
            elif choice == "4":
                heat_pump()
            elif choice == "5":
                convert_temperature()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except (ValueError, OverflowError, ZeroDivisionError):
            print("Could not compute with those values.")
    print("Bye.")


main()
