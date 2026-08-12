# On-calc name: FLUID
# Program: fluid_mechanics_solver
# Purpose: Two fluid-mechanics tools: (1) Bernoulli's equation between
#          two points in a flow (P + 0.5*rho*v^2 + rho*g*h = constant),
#          solving for whichever of P2, v2, or h2 is unknown given the
#          full state at point 1 and the rest of point 2, and (2) the
#          Reynolds number for pipe flow, Re = rho*v*D/mu (or v*D/nu
#          with kinematic viscosity), with a laminar/transitional/
#          turbulent classification.
# Usage: Pick a tool from the menu. For Bernoulli, enter fluid density
#        rho, g (blank defaults to 9.81), P1/v1/h1, then two of the
#        three point-2 values (leave the unknown to be solved for out
#        by following the prompts). For Reynolds number, enter flow
#        speed, pipe diameter, and either dynamic viscosity mu (plus
#        rho) or kinematic viscosity nu directly.

from math import sqrt


def get_float(prompt, default=None):
    while True:
        raw = input(prompt).strip()
        if raw == "" and default is not None:
            return default
        try:
            return float(raw)
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def get_positive(prompt):
    while True:
        value = get_float(prompt)
        if value > 0:
            return value
        print("Value must be positive.")


def bernoulli():
    print("\nPoint 1 (fully known):")
    rho = get_positive("  Fluid density rho = ")
    g = get_float("  g (blank = 9.81) = ", default=9.81)
    p1 = get_float("  Pressure P1 = ")
    v1 = get_float("  Velocity v1 = ")
    h1 = get_float("  Height h1 = ")
    e1 = p1 + 0.5 * rho * v1 * v1 + rho * g * h1

    print("\nWhich point-2 value is unknown?")
    print("1. Pressure P2 (enter v2, h2)")
    print("2. Velocity v2 (enter P2, h2)")
    print("3. Height h2 (enter P2, v2)")
    choice = input("> ").strip()

    if choice == "1":
        v2 = get_float("  Velocity v2 = ")
        h2 = get_float("  Height h2 = ")
        p2 = e1 - 0.5 * rho * v2 * v2 - rho * g * h2
        print("\nP2 = " + str(round(p2, 6)))
    elif choice == "2":
        p2 = get_float("  Pressure P2 = ")
        h2 = get_float("  Height h2 = ")
        inside = 2 * (e1 - p2 - rho * g * h2) / rho
        if inside < 0:
            print("\nNo real solution: those values imply a negative v2^2.")
            return
        print("\nv2 = " + str(round(sqrt(inside), 6)))
    elif choice == "3":
        p2 = get_float("  Pressure P2 = ")
        v2 = get_float("  Velocity v2 = ")
        if rho * g == 0:
            print("\nCannot solve for h2 with rho*g = 0.")
            return
        h2 = (e1 - p2 - 0.5 * rho * v2 * v2) / (rho * g)
        print("\nh2 = " + str(round(h2, 6)))
    else:
        print("Invalid choice.")


def reynolds_number():
    v = get_positive("Flow speed v = ")
    d = get_positive("Pipe diameter D = ")
    print("\n1. Use dynamic viscosity mu (needs density rho)")
    print("2. Use kinematic viscosity nu directly")
    choice = input("> ").strip()
    if choice == "2":
        nu = get_positive("Kinematic viscosity nu = ")
        re = v * d / nu
    else:
        rho = get_positive("Fluid density rho = ")
        mu = get_positive("Dynamic viscosity mu = ")
        re = rho * v * d / mu

    print("\nReynolds number Re = " + str(round(re, 4)))
    if re < 2300:
        print("Flow regime: laminar")
    elif re <= 4000:
        print("Flow regime: transitional")
    else:
        print("Flow regime: turbulent")


def main():
    print("=== FLUID ===")
    while True:
        print("\n1. Bernoulli's equation")
        print("2. Reynolds number")
        print("0. Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                bernoulli()
            elif choice == "2":
                reynolds_number()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except Exception:
            print("Could not compute with those values.")
    print("Bye.")


main()
