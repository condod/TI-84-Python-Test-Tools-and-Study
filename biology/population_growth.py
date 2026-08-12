# On-calc name: POPGROW
# Program: population_growth
# Purpose: Population growth models. Exponential growth N = N0*e^(rt)
#          with doubling time, and logistic growth
#          N = K/(1 + ((K-N0)/N0)*e^(-rt)) with carrying capacity K,
#          plus the instantaneous growth rate dN/dt = rN(1 - N/K) and
#          the inflection point where growth is fastest.
# Usage: Pick a model from the menu. N0 is the starting population, r
#        is the intrinsic growth rate per unit time (0.1 means 10% per
#        time unit, negative for decline), t is elapsed time, and K is
#        the carrying capacity. You can solve for the population at a
#        time, or for the time needed to reach a target population.

from math import exp, log


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def get_positive(prompt):
    while True:
        value = get_float(prompt)
        if value <= 0:
            print("Please enter a positive number.")
            continue
        return value


def exponential_population():
    n0 = get_positive("Starting population N0 = ")
    rate = get_float("Growth rate r per time unit = ")
    time = get_float("Time t = ")

    n = n0 * exp(rate * time)
    print("\nN(" + str(round(time, 4)) + ") = " + str(round(n, 6)))
    print("Change = " + str(round(n - n0, 6)))
    if rate > 0:
        print("Doubling time = " + str(round(log(2.0) / rate, 6)))
    elif rate < 0:
        print("Half-life = " + str(round(log(0.5) / rate, 6)))
    else:
        print("r = 0, so the population is constant.")


def exponential_time():
    n0 = get_positive("Starting population N0 = ")
    target = get_positive("Target population N = ")
    rate = get_float("Growth rate r per time unit = ")

    if rate == 0:
        print("\nWith r = 0 the population never changes.")
        return
    ratio = target / n0
    if ratio <= 0:
        print("\nPopulations must be positive.")
        return
    time = log(ratio) / rate
    if time < 0:
        print("\nThat target is in the past for this growth rate:")
    print("t = " + str(round(time, 6)))


def logistic_population():
    n0 = get_positive("Starting population N0 = ")
    capacity = get_positive("Carrying capacity K = ")
    rate = get_float("Growth rate r per time unit = ")
    time = get_float("Time t = ")

    # N = K / (1 + A e^(-rt)) with A = (K - N0)/N0
    a = (capacity - n0) / n0
    denom = 1.0 + a * exp(-rate * time)
    if denom == 0:
        print("\nCannot evaluate the model at that time.")
        return
    n = capacity / denom

    print("\nN(" + str(round(time, 4)) + ") = " + str(round(n, 6)))
    print("Percent of K = " + str(round(n / capacity * 100.0, 4)) + " %")
    growth = rate * n * (1.0 - n / capacity)
    print("dN/dt now = " + str(round(growth, 6)))
    if n0 < capacity and rate > 0:
        # Growth is fastest at N = K/2; solve K/2 = K/(1+A e^-rt) for t.
        if a > 0:
            t_infl = log(a) / rate
            print("Fastest growth at N = K/2 = " +
                  str(round(capacity / 2.0, 6)))
            print("  which happens at t = " + str(round(t_infl, 6)))


def logistic_time():
    n0 = get_positive("Starting population N0 = ")
    capacity = get_positive("Carrying capacity K = ")
    target = get_positive("Target population N = ")
    rate = get_float("Growth rate r per time unit = ")

    if rate == 0:
        print("\nWith r = 0 the population never changes.")
        return
    if target >= capacity:
        print("\nLogistic growth approaches K but never reaches it,")
        print("so a target at or above K is never attained.")
        return
    a = (capacity - n0) / n0
    if a <= 0:
        print("\nN0 is at or above K; this branch needs N0 < K.")
        return
    inner = (capacity / target - 1.0) / a
    if inner <= 0:
        print("\nCannot solve for that target.")
        return
    time = -log(inner) / rate
    print("\nt = " + str(round(time, 6)))


def growth_rate_now():
    n = get_positive("Current population N = ")
    capacity = get_positive("Carrying capacity K = ")
    rate = get_float("Growth rate r per time unit = ")

    growth = rate * n * (1.0 - n / capacity)
    print("\ndN/dt = r*N*(1 - N/K) = " + str(round(growth, 6)))
    print("Percent of K = " + str(round(n / capacity * 100.0, 4)) + " %")
    if n > capacity:
        print("Above carrying capacity, so the population shrinks.")
    elif growth > 0:
        print("Population is still growing.")


def main():
    print("=== POPGROW ===")
    while True:
        print("\n1. Exponential: population at time t")
        print("2. Exponential: time to reach N")
        print("3. Logistic: population at time t")
        print("4. Logistic: time to reach N")
        print("5. Logistic: growth rate right now")
        print("0. Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                exponential_population()
            elif choice == "2":
                exponential_time()
            elif choice == "3":
                logistic_population()
            elif choice == "4":
                logistic_time()
            elif choice == "5":
                growth_rate_now()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except (ValueError, OverflowError, ZeroDivisionError):
            print("Could not compute with those values.")
    print("Bye.")


main()
