# On-calc name: INTEREST
# Program: compound_interest
# Purpose: Compound-interest growth plus APR/APY (nominal vs effective
#          rate) conversions, including continuous compounding. Also
#          compares two accounts on an equal-footing effective-rate
#          basis so different compounding frequencies can be ranked.
# Usage: Pick a tool from the menu. Compounding frequency is entered as
#        times per year (1=annual, 4=quarterly, 12=monthly, 365=daily);
#        enter 0 for continuous compounding. Rates are entered as
#        percents (5 means 5%). Prints the future value, the interest
#        earned, and the effective annual rate (APY).

from math import exp, log

CONTINUOUS = 0


def money(value):
    # Fixed 2-decimal text; str.format() is avoided across this library.
    negative = value < 0
    cents = int(round(abs(value) * 100.0))
    text = str(cents // 100) + "." + ("0" + str(cents % 100))[-2:]
    if negative and cents != 0:
        text = "-" + text
    return text


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def get_frequency(prompt):
    while True:
        value = get_float(prompt)
        if value < 0:
            print("Enter 0 for continuous, or a positive number.")
            continue
        return value


def future_value(principal, rate, freq, years):
    if freq == CONTINUOUS:
        return principal * exp(rate * years)
    return principal * (1.0 + rate / freq) ** (freq * years)


def effective_rate(rate, freq):
    # APY (effective annual rate) from a nominal APR.
    if freq == CONTINUOUS:
        return exp(rate) - 1.0
    return (1.0 + rate / freq) ** freq - 1.0


def nominal_rate(apy, freq):
    # Inverse of effective_rate: the APR that produces a given APY.
    if freq == CONTINUOUS:
        return log(1.0 + apy)
    return freq * ((1.0 + apy) ** (1.0 / freq) - 1.0)


def freq_label(freq):
    if freq == CONTINUOUS:
        return "continuous"
    return str(round(freq, 4)) + "x per year"


def grow_money():
    principal = get_float("Principal = ")
    rate = get_float("Annual rate % (APR) = ") / 100.0
    freq = get_frequency("Compounds per year (0=continuous) = ")
    years = get_float("Years = ")

    fv = future_value(principal, rate, freq, years)
    apy = effective_rate(rate, freq)
    print("\nFuture value = " + money(fv))
    print("Interest earned = " + money(fv - principal))
    print("APY (effective) = " + str(round(apy * 100.0, 6)) + " %")


def apr_to_apy():
    rate = get_float("Nominal APR % = ") / 100.0
    freq = get_frequency("Compounds per year (0=continuous) = ")
    apy = effective_rate(rate, freq)
    print("\nAPR = " + str(round(rate * 100.0, 6)) + " % (" +
          freq_label(freq) + ")")
    print("APY = " + str(round(apy * 100.0, 6)) + " %")
    print("On 1000 for a year that is " + money(1000.0 * apy) + " of interest.")


def apy_to_apr():
    apy = get_float("Effective APY % = ") / 100.0
    freq = get_frequency("Compounds per year (0=continuous) = ")
    if apy <= -1:
        print("APY must be greater than -100%.")
        return
    rate = nominal_rate(apy, freq)
    print("\nAPY = " + str(round(apy * 100.0, 6)) + " %")
    print("Equivalent APR = " + str(round(rate * 100.0, 6)) + " % (" +
          freq_label(freq) + ")")


def compare_accounts():
    print("\nAccount A:")
    rate_a = get_float("  APR % = ") / 100.0
    freq_a = get_frequency("  Compounds per year (0=continuous) = ")
    print("Account B:")
    rate_b = get_float("  APR % = ") / 100.0
    freq_b = get_frequency("  Compounds per year (0=continuous) = ")

    apy_a = effective_rate(rate_a, freq_a)
    apy_b = effective_rate(rate_b, freq_b)
    print("\nA: APY = " + str(round(apy_a * 100.0, 6)) + " %")
    print("B: APY = " + str(round(apy_b * 100.0, 6)) + " %")
    if apy_a > apy_b:
        print("A is better by " + str(round((apy_a - apy_b) * 100.0, 6)) +
              " percentage points.")
    elif apy_b > apy_a:
        print("B is better by " + str(round((apy_b - apy_a) * 100.0, 6)) +
              " percentage points.")
    else:
        print("The two accounts are equivalent.")


def main():
    print("=== INTEREST ===")
    while True:
        print("\n1. Grow money (future value)")
        print("2. APR -> APY")
        print("3. APY -> APR")
        print("4. Compare two accounts")
        print("0. Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                grow_money()
            elif choice == "2":
                apr_to_apy()
            elif choice == "3":
                apy_to_apr()
            elif choice == "4":
                compare_accounts()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except (ValueError, OverflowError, ZeroDivisionError):
            print("Could not compute with those values.")
    print("Bye.")


main()
