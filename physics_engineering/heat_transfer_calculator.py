# On-calc name: HEAT
# Program: heat_transfer_calculator
# Purpose: Three heat-transfer tools: (1) specific heat q = m*c*dT,
#          (2) phase-change latent heat q = m*L, and (3) the final
#          equilibrium temperature when two masses at different
#          temperatures are mixed (calorimetry, heat lost = heat
#          gained, no heat lost to surroundings).
# Usage: Pick a tool from the menu and enter the requested masses,
#        specific heats/latent heats, and temperatures (use consistent
#        units, e.g. mass in kg or g, c in J/(unit*K), T in C or K).
#        Prints the computed heat q (positive = absorbed, negative =
#        released) or the equilibrium temperature.


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def specific_heat():
    print("\nq = m*c*(Tfinal - Tinitial)")
    m = get_float("mass m = ")
    c = get_float("specific heat c = ")
    t_i = get_float("initial temperature = ")
    t_f = get_float("final temperature = ")
    q = m * c * (t_f - t_i)
    print("\nq = " + str(round(q, 6)))
    if q > 0:
        print("(Heat absorbed by the substance)")
    elif q < 0:
        print("(Heat released by the substance)")
    else:
        print("(No net heat transfer)")


def latent_heat():
    print("\nq = m*L  (phase change at constant temperature)")
    m = get_float("mass m = ")
    latent = get_float("latent heat L = ")
    q = m * latent
    print("\nq = " + str(round(q, 6)))


def mixing_equilibrium():
    print("\nMixing two masses until they reach the same temperature.")
    print("Substance 1:")
    m1 = get_float("  mass m1 = ")
    c1 = get_float("  specific heat c1 = ")
    t1 = get_float("  temperature T1 = ")
    print("Substance 2:")
    m2 = get_float("  mass m2 = ")
    c2 = get_float("  specific heat c2 = ")
    t2 = get_float("  temperature T2 = ")

    denom = m1 * c1 + m2 * c2
    if denom == 0:
        print("\nCannot solve: m*c is 0 for both substances.")
        return

    t_eq = (m1 * c1 * t1 + m2 * c2 * t2) / denom
    q1 = m1 * c1 * (t_eq - t1)
    q2 = m2 * c2 * (t_eq - t2)
    print("\nEquilibrium temperature = " + str(round(t_eq, 6)))
    print("Heat gained/lost by substance 1 = " + str(round(q1, 6)))
    print("Heat gained/lost by substance 2 = " + str(round(q2, 6)))


def main():
    print("=== HEAT ===")
    while True:
        print("\n1. Specific heat q=mcdT")
        print("2. Latent heat q=mL")
        print("3. Mixing equilibrium temp")
        print("0. Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                specific_heat()
            elif choice == "2":
                latent_heat()
            elif choice == "3":
                mixing_equilibrium()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except Exception:
            print("Could not compute with those values.")
    print("Bye.")


main()
