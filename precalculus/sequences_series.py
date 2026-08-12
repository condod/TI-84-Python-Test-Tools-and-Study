# On-calc name: SEQSER
# Program: sequences_series
# Purpose: Arithmetic and geometric sequences and series. Finds the nth
#          term, the sum of the first n terms, the common difference or
#          ratio from two known terms, the sum of an infinite geometric
#          series when it converges, and can list the first several
#          terms of a sequence.
# Usage: Pick a sequence type and a tool from the menu. Terms are
#        1-indexed, so a1 is the first term. For an infinite geometric
#        series the program checks |r| < 1 and says so when the series
#        diverges instead of returning a meaningless number.

from math import log

MAX_LIST = 60


def pad(text, width):
    # stand-in for str.ljust(), which the calculator's Python lacks
    s = str(text)
    if len(s) >= width:
        return s
    return s + " " * (width - len(s))


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def get_index(prompt):
    while True:
        try:
            n = int(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a whole number.")
            continue
        if n < 1:
            print("Term numbers start at 1.")
            continue
        return n


def arithmetic_term():
    a1 = get_float("First term a1 = ")
    d = get_float("Common difference d = ")
    n = get_index("Which term n = ")
    term = a1 + (n - 1) * d
    total = n / 2.0 * (2.0 * a1 + (n - 1) * d)
    print("\na" + str(n) + " = a1 + (n-1)d = " + str(round(term, 6)))
    print("S" + str(n) + " = n/2 * (a1 + an) = " + str(round(total, 6)))


def arithmetic_from_two():
    print("\nGive any two terms of the sequence.")
    m = get_index("First index m = ")
    am = get_float("Value a_m = ")
    n = get_index("Second index n = ")
    an = get_float("Value a_n = ")
    if m == n:
        print("\nThe two indices must differ.")
        return
    d = (an - am) / (n - m)
    a1 = am - (m - 1) * d
    print("\nCommon difference d = " + str(round(d, 6)))
    print("First term a1 = " + str(round(a1, 6)))
    print("Explicit rule: a_n = " + str(round(a1, 6)) + " + (n-1)*" +
          str(round(d, 6)))


def arithmetic_sum_to_target():
    a1 = get_float("First term a1 = ")
    d = get_float("Common difference d = ")
    target = get_float("Target term value = ")
    if d == 0:
        print("\nWith d = 0 every term equals a1.")
        return
    n = (target - a1) / d + 1.0
    if abs(n - round(n)) > 1e-9:
        print("\n" + str(round(target, 6)) + " is not a term of this")
        print("sequence (it would be term " + str(round(n, 6)) + ").")
        return
    n = int(round(n))
    if n < 1:
        print("\nThat value comes before the first term.")
        return
    total = n / 2.0 * (a1 + target)
    print("\nIt is term number " + str(n) + ".")
    print("Sum of the first " + str(n) + " terms = " + str(round(total, 6)))


def geometric_term():
    a1 = get_float("First term a1 = ")
    r = get_float("Common ratio r = ")
    n = get_index("Which term n = ")
    term = a1 * r ** (n - 1)
    if r == 1:
        total = a1 * n
    else:
        total = a1 * (1.0 - r ** n) / (1.0 - r)
    print("\na" + str(n) + " = a1 * r^(n-1) = " + str(round(term, 6)))
    print("S" + str(n) + " = " + str(round(total, 6)))


def geometric_from_two():
    print("\nGive any two terms of the sequence.")
    m = get_index("First index m = ")
    am = get_float("Value a_m = ")
    n = get_index("Second index n = ")
    an = get_float("Value a_n = ")
    if m == n:
        print("\nThe two indices must differ.")
        return
    if am == 0:
        print("\nA geometric sequence cannot have a zero term.")
        return
    ratio = an / am
    power = n - m
    if ratio < 0 and power % 2 == 0:
        print("\nNo real common ratio fits those two terms.")
        return
    if ratio < 0:
        r = -((-ratio) ** (1.0 / power))
    else:
        r = ratio ** (1.0 / power)
    a1 = am / r ** (m - 1)
    print("\nCommon ratio r = " + str(round(r, 6)))
    print("First term a1 = " + str(round(a1, 6)))
    if power % 2 == 0 and ratio > 0:
        print("(-" + str(round(abs(r), 6)) + " also fits; even power.)")


def geometric_infinite():
    a1 = get_float("First term a1 = ")
    r = get_float("Common ratio r = ")
    if abs(r) >= 1:
        print("\n|r| = " + str(round(abs(r), 6)) + " is not less than 1,")
        print("so the infinite series diverges (no finite sum).")
        return
    total = a1 / (1.0 - r)
    print("\nS(infinite) = a1/(1-r) = " + str(round(total, 6)))
    print("The terms shrink toward 0, so the partial sums")
    print("converge on that value.")


def geometric_terms_to_exceed():
    a1 = get_float("First term a1 = ")
    r = get_float("Common ratio r = ")
    target = get_float("Value to exceed = ")
    if a1 == 0 or r <= 0 or r == 1:
        print("\nThis tool needs a positive ratio other than 1.")
        return
    if target / a1 <= 0:
        print("\nThat target cannot be reached from this first term.")
        return
    n = log(target / a1) / log(r) + 1.0
    print("\nTerm n = " + str(round(n, 6)) + " reaches it exactly;")
    print("the first whole term past it is n = " +
          str(int(n) + 1 if n > 0 else 1))


def list_terms():
    print("\n1. Arithmetic")
    print("2. Geometric")
    kind = input("> ").strip()
    if kind not in ("1", "2"):
        print("Invalid choice.")
        return
    a1 = get_float("First term a1 = ")
    step = get_float("Common difference d = " if kind == "1"
                     else "Common ratio r = ")
    count = get_index("How many terms = ")
    if count > MAX_LIST:
        count = MAX_LIST
        print("Listing the first " + str(MAX_LIST) + " terms.")

    print("\n  n  term         running sum")
    total = 0.0
    term = a1
    for n in range(1, count + 1):
        if kind == "1":
            term = a1 + (n - 1) * step
        else:
            term = a1 * step ** (n - 1)
        total += term
        print(pad(n, 5) + pad(round(term, 6), 13) + str(round(total, 6)))
        if n % 10 == 0 and n != count:
            input("ENTER for more")


def main():
    print("=== SEQSER ===")
    while True:
        print("\n1. Arithmetic: nth term & sum")
        print("2. Arithmetic: d from two terms")
        print("3. Arithmetic: locate a term value")
        print("4. Geometric: nth term & sum")
        print("5. Geometric: r from two terms")
        print("6. Geometric: infinite sum")
        print("7. Geometric: terms to exceed a value")
        print("8. List the first n terms")
        print("0. Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                arithmetic_term()
            elif choice == "2":
                arithmetic_from_two()
            elif choice == "3":
                arithmetic_sum_to_target()
            elif choice == "4":
                geometric_term()
            elif choice == "5":
                geometric_from_two()
            elif choice == "6":
                geometric_infinite()
            elif choice == "7":
                geometric_terms_to_exceed()
            elif choice == "8":
                list_terms()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except (ValueError, OverflowError, ZeroDivisionError):
            print("Could not compute with those values.")
    print("Bye.")


main()
