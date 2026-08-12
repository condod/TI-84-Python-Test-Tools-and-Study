# On-calc name: ORBIT
# Program: orbital_mechanics_calculator
# Purpose: Circular-orbit mechanics: orbital speed and period around a
#          central body, escape velocity, and Kepler's Third Law
#          (T^2/a^3 = 4*pi^2/GM) converting between orbital period T
#          and semi-major axis a. Uses the standard gravitational
#          parameter GM (mu) so no separate G and mass entry is
#          needed; presets are provided for Earth, the Moon, and the
#          Sun.
# Usage: Pick a tool from the menu, then pick a body (or enter a
#        custom GM) and the orbital radius/axis or period. Prints the
#        computed speed, period (seconds and days), or axis, using
#        SI units (meters, seconds, m^3/s^2 for GM) throughout.

from math import pi, sqrt

GM_PRESETS = {
    "1": ("Earth", 3.986004418e14),
    "2": ("Moon", 4.9048695e12),
    "3": ("Sun", 1.32712440018e20),
}


def get_positive(prompt):
    while True:
        try:
            value = float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")
            continue
        if value > 0:
            return value
        print("Value must be positive.")


def get_gm():
    print("Central body:")
    print("1. Earth   2. Moon   3. Sun   4. Custom GM")
    choice = input("> ").strip()
    if choice in GM_PRESETS:
        name, gm = GM_PRESETS[choice]
        print(name + ": GM = " + str(gm) + " m^3/s^2")
        return gm
    return get_positive("GM (m^3/s^2) = ")


def print_period(seconds):
    print("Period = " + str(round(seconds, 4)) + " s ("
          + str(round(seconds / 86400.0, 6)) + " days)")


def orbital_speed_period():
    gm = get_gm()
    r = get_positive("Orbital radius r (from body's center) = ")
    v = sqrt(gm / r)
    t = 2 * pi * sqrt(r ** 3 / gm)
    print("\nOrbital speed v = " + str(round(v, 6)) + " m/s")
    print_period(t)


def escape_velocity():
    gm = get_gm()
    r = get_positive("Radius r (from body's center) = ")
    v_esc = sqrt(2 * gm / r)
    print("\nEscape velocity = " + str(round(v_esc, 6)) + " m/s")


def kepler_third_law():
    gm = get_gm()
    print("\n1. Semi-major axis a -> period T")
    print("2. Period T -> semi-major axis a")
    choice = input("> ").strip()
    if choice == "2":
        t = get_positive("Period T (seconds) = ")
        a = (gm * t * t / (4 * pi * pi)) ** (1.0 / 3.0)
        print("\nSemi-major axis a = " + str(round(a, 6)) + " m")
    else:
        a = get_positive("Semi-major axis a (meters) = ")
        t = 2 * pi * sqrt(a ** 3 / gm)
        print()
        print_period(t)


def main():
    print("=== ORBIT ===")
    while True:
        print("\n1. Orbital speed & period (circular orbit)")
        print("2. Escape velocity")
        print("3. Kepler's Third Law (T <-> a)")
        print("0. Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                orbital_speed_period()
            elif choice == "2":
                escape_velocity()
            elif choice == "3":
                kepler_third_law()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except Exception:
            print("Could not compute with those values.")
    print("Bye.")


main()
