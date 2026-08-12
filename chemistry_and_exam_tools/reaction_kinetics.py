# On-calc name: KINETIC
# Program: reaction_kinetics
# Purpose: Chemical reaction kinetics for zero, first, or second order
#          reactions in a single reactant A: half-life, concentration
#          [A] at a given time t (integrated rate law), and the time
#          needed to reach a given [A], from the rate constant k and
#          initial concentration [A]0.
# Usage: Pick a tool from the menu, then the reaction order (0, 1, or
#        2), and enter k, [A]0, and (depending on the tool) t or a
#        target [A]. Prints the requested half-life, concentration, or
#        time.

from math import log, exp


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


def pick_order():
    print("Reaction order:  1. Zero   2. First   3. Second")
    choice = input("> ").strip()
    if choice == "2":
        return 1
    if choice == "3":
        return 2
    return 0


def half_life():
    order = pick_order()
    k = get_positive("Rate constant k = ")
    if order == 1:
        t_half = log(2) / k
        print("\nHalf-life (first order, independent of [A]0) = "
              + str(round(t_half, 6)))
        return
    a0 = get_positive("Initial concentration [A]0 = ")
    if order == 0:
        t_half = a0 / (2 * k)
    else:
        t_half = 1.0 / (k * a0)
    print("\nHalf-life = " + str(round(t_half, 6)))


def concentration_at_time():
    order = pick_order()
    k = get_positive("Rate constant k = ")
    a0 = get_positive("Initial concentration [A]0 = ")
    t = get_positive("Time t = ")
    if order == 0:
        a_t = a0 - k * t
        if a_t < 0:
            print("\n[A] has already reached 0 before this time; [A](t) = 0")
            return
    elif order == 1:
        a_t = a0 * exp(-k * t)
    else:
        a_t = 1.0 / (1.0 / a0 + k * t)
    print("\n[A](t) = " + str(round(a_t, 6)))


def time_to_reach():
    order = pick_order()
    k = get_positive("Rate constant k = ")
    a0 = get_positive("Initial concentration [A]0 = ")
    a_t = get_positive("Target concentration [A] = ")
    if a_t >= a0:
        print("\nTarget [A] must be less than [A]0 for a decaying reactant.")
        return
    if order == 0:
        t = (a0 - a_t) / k
    elif order == 1:
        t = log(a0 / a_t) / k
    else:
        t = (1.0 / a_t - 1.0 / a0) / k
    print("\nTime to reach [A] = " + str(round(t, 6)))


def main():
    print("=== KINETIC ===")
    while True:
        print("\n1. Half-life")
        print("2. [A] at time t")
        print("3. Time to reach [A]")
        print("0. Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                half_life()
            elif choice == "2":
                concentration_at_time()
            elif choice == "3":
                time_to_reach()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except Exception:
            print("Could not compute with those values.")
    print("Bye.")


main()
