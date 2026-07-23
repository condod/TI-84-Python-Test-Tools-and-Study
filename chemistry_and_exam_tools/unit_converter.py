# Program: unit_converter
# Purpose: Menu-driven unit conversion toolkit covering length, mass,
#          pressure, temperature, and energy.
# Usage: Pick a category, then pick the "from" and "to" units from the
#        numbered list, then enter the value to convert. Prints the
#        converted result. Temperature uses its own formulas since it
#        is not a simple multiplicative conversion.

LENGTH_TO_M = {"m": 1.0, "km": 1000.0, "cm": 0.01, "mm": 0.001,
               "ft": 0.3048, "in": 0.0254, "mi": 1609.344, "yd": 0.9144}
MASS_TO_KG = {"kg": 1.0, "g": 0.001, "mg": 0.000001,
              "lb": 0.45359237, "oz": 0.028349523}
PRESSURE_TO_PA = {"Pa": 1.0, "kPa": 1000.0, "atm": 101325.0,
                   "bar": 100000.0, "psi": 6894.757}
ENERGY_TO_J = {"J": 1.0, "kJ": 1000.0, "cal": 4.184, "kcal": 4184.0,
               "kWh": 3600000.0, "BTU": 1055.056}

CATEGORIES = {
    "1": ("Length", LENGTH_TO_M),
    "2": ("Mass", MASS_TO_KG),
    "3": ("Pressure", PRESSURE_TO_PA),
    "4": ("Energy", ENERGY_TO_J),
}


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def pick_unit(table, label):
    keys = list(table.keys())
    print("\n" + label + " units:")
    for i, k in enumerate(keys):
        print(str(i + 1) + ". " + k)
    while True:
        raw = input("Choice (1-" + str(len(keys)) + "): ").strip()
        try:
            idx = int(raw) - 1
            if 0 <= idx < len(keys):
                return keys[idx]
        except (ValueError, TypeError):
            pass
        print("Invalid choice.")


def convert_table(table):
    from_unit = pick_unit(table, "Convert FROM")
    to_unit = pick_unit(table, "Convert TO")
    value = get_float("\nValue in " + from_unit + " = ")
    base = value * table[from_unit]
    result = base / table[to_unit]
    print(str(value) + " " + from_unit + " = " + str(round(result, 6)) + " " + to_unit)


def temp_to_celsius(value, unit):
    if unit == "C":
        return value
    if unit == "F":
        return (value - 32) * 5.0 / 9.0
    if unit == "K":
        return value - 273.15
    return None


def celsius_to(value_c, unit):
    if unit == "C":
        return value_c
    if unit == "F":
        return value_c * 9.0 / 5.0 + 32
    if unit == "K":
        return value_c + 273.15
    return None


def convert_temperature():
    units = ["C", "F", "K"]
    print("\nTemperature units: 1=Celsius(C)  2=Fahrenheit(F)  3=Kelvin(K)")
    from_unit = None
    to_unit = None
    while True:
        try:
            f_idx = int(input("From (1-3): ").strip()) - 1
            if 0 <= f_idx < 3:
                from_unit = units[f_idx]
                break
        except (ValueError, TypeError):
            pass
        print("Invalid choice.")
    while True:
        try:
            t_idx = int(input("To (1-3): ").strip()) - 1
            if 0 <= t_idx < 3:
                to_unit = units[t_idx]
                break
        except (ValueError, TypeError):
            pass
        print("Invalid choice.")

    value = get_float("\nValue in " + from_unit + " = ")
    c = temp_to_celsius(value, from_unit)
    result = celsius_to(c, to_unit)
    print(str(value) + " " + from_unit + " = " + str(round(result, 4)) + " " + to_unit)


def main():
    print("=== Unit Conversion Toolkit ===")
    while True:
        print("\n1. Length")
        print("2. Mass")
        print("3. Pressure")
        print("4. Energy")
        print("5. Temperature")
        print("6. Quit")
        choice = input("Category (1-6): ").strip()

        if choice == "6":
            break
        elif choice in CATEGORIES:
            _, table = CATEGORIES[choice]
            convert_table(table)
        elif choice == "5":
            convert_temperature()
        else:
            print("Invalid choice.")
    print("Done.")


main()
