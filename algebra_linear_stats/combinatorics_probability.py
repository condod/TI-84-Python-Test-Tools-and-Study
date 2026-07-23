# Program: combinatorics_probability
# Purpose: Menu-driven calculator for permutations (nPr), combinations
#          (nCr), and binomial probability P(X=k) for n trials with
#          success probability p.
# Usage: Choose an operation from the menu, enter n and r (and p and k
#        for binomial probability). Prints the computed value.

from math import factorial


def get_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n < 0:
                print("Please enter a non-negative whole number.")
                continue
            return n
        except (ValueError, TypeError):
            print("Please enter a whole number.")


def get_prob(prompt):
    while True:
        try:
            p = float(input(prompt))
            if p < 0 or p > 1:
                print("Probability must be between 0 and 1.")
                continue
            return p
        except (ValueError, TypeError):
            print("Please enter a number between 0 and 1.")


def nPr(n, r):
    if r > n:
        return None
    return factorial(n) // factorial(n - r)


def nCr(n, r):
    if r > n:
        return None
    return factorial(n) // (factorial(r) * factorial(n - r))


def binomial_prob(n, k, p):
    if k > n:
        return None
    c = nCr(n, k)
    return c * (p ** k) * ((1 - p) ** (n - k))


def main():
    print("=== Combinatorics & Probability Calculator ===")
    while True:
        print("\n1. nPr (permutations)")
        print("2. nCr (combinations)")
        print("3. Binomial probability P(X=k)")
        print("4. Quit")
        choice = input("Choice (1-4): ").strip()

        if choice == "4":
            break
        elif choice == "1":
            n = get_int("n = ")
            r = get_int("r = ")
            result = nPr(n, r)
            print("nPr = " + str(result) if result is not None else "r cannot be greater than n.")
        elif choice == "2":
            n = get_int("n = ")
            r = get_int("r = ")
            result = nCr(n, r)
            print("nCr = " + str(result) if result is not None else "r cannot be greater than n.")
        elif choice == "3":
            n = get_int("Number of trials n = ")
            k = get_int("Number of successes k = ")
            p = get_prob("Probability of success p (0-1) = ")
            result = binomial_prob(n, k, p)
            if result is None:
                print("k cannot be greater than n.")
            else:
                print("P(X=" + str(k) + ") = " + str(round(result, 6)))
        else:
            print("Invalid choice.")

    print("Done.")


main()
