# On-calc name: COMBIN
# Program: combinatorics_probability
# Purpose: Menu-driven calculator for permutations (nPr), combinations
#          (nCr), and binomial probability P(X=k) for n trials with
#          success probability p.
# Usage: Choose an operation from the menu, enter n and r (and p and k
#        for binomial probability). Prints the computed value.

MAX_N = 200


def get_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n < 0:
                print("Please enter a non-negative whole number.")
                continue
            if n > MAX_N:
                print("Please keep n at or below " + str(MAX_N) +
                      " so the calculator stays responsive.")
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
    # Built up as a running product instead of factorial(n)//factorial(n-r):
    # math.factorial does not exist on the TI-84, and the huge intermediate
    # values it would create are a memory risk on-device.
    if r > n:
        return None
    result = 1
    for i in range(r):
        result *= (n - i)
    return result


def nCr(n, r):
    if r > n:
        return None
    if r > n - r:
        r = n - r
    result = 1
    for i in range(1, r + 1):
        # exact at every step: result is always a valid binomial coefficient
        result = result * (n - r + i) // i
    return result


def binomial_prob(n, k, p):
    if k > n:
        return None
    c = nCr(n, k)
    return c * (p ** k) * ((1 - p) ** (n - k))


def main():
    print("=== COMBIN ===")
    while True:
        print("\n1. nPr (permutations)")
        print("2. nCr (combinations)")
        print("3. Binomial probability P(X=k)")
        print("0. Quit")
        choice = input("> ").strip()

        if choice == "0":
            break
        elif choice == "1":
            n = get_int("n = ")
            r = get_int("r = ")
            result = nPr(n, r)
            if result is None:
                print("r cannot be greater than n.")
            else:
                print("nPr = " + str(result))
        elif choice == "2":
            n = get_int("n = ")
            r = get_int("r = ")
            result = nCr(n, r)
            if result is None:
                print("r cannot be greater than n.")
            else:
                print("nCr = " + str(result))
        elif choice == "3":
            n = get_int("Number of trials n = ")
            k = get_int("Number of successes k = ")
            p = get_prob("Probability of success p (0-1) = ")
            result = binomial_prob(n, k, p)
            if result is None:
                print("k cannot be greater than n.")
            elif 0 < result < 1e-6:
                # too small for 6-decimal rounding to show anything but 0.0
                print("P(X=" + str(k) + ") = " + str(result))
            else:
                print("P(X=" + str(k) + ") = " + str(round(result, 6)))
        else:
            print("Invalid choice.")

    print("Bye.")


main()
