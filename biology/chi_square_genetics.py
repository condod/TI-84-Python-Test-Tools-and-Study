# On-calc name: CHISQ
# Program: chi_square_genetics
# Purpose: Chi-square goodness-of-fit test for genetics crosses. Takes
#          observed offspring counts and an expected Mendelian ratio
#          (3:1, 9:3:3:1, 1:1, or one you type in), computes expected
#          counts, the chi-square statistic, the degrees of freedom,
#          and whether to reject the hypothesis at the 0.05 and 0.01
#          levels using a built-in critical-value table.
# Usage: Pick a ratio preset or enter a custom one as whole numbers
#        separated by commas (e.g. 9,3,3,1). Then enter the observed
#        count for each category in the same order. Prints a per-
#        category table of observed, expected, and contribution to
#        chi-square, then the verdict. Degrees of freedom = categories
#        minus 1 (no parameters are estimated from the data here).

MAX_CATEGORIES = 12

# Critical values for df 1..12; index 0 is unused so df indexes directly.
CHI2_05 = [0.0, 3.841, 5.991, 7.815, 9.488, 11.070, 12.592, 14.067,
           15.507, 16.919, 18.307, 19.675, 21.026]
CHI2_01 = [0.0, 6.635, 9.210, 11.345, 13.277, 15.086, 16.812, 18.475,
           20.090, 21.666, 23.209, 24.725, 26.217]

PRESETS = [
    ("Monohybrid 3:1", [3.0, 1.0]),
    ("Dihybrid 9:3:3:1", [9.0, 3.0, 3.0, 1.0]),
    ("Test cross 1:1", [1.0, 1.0]),
    ("Incomplete dominance 1:2:1", [1.0, 2.0, 1.0]),
    ("Custom ratio", None),
]


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


def get_count(prompt):
    while True:
        value = get_float(prompt)
        if value < 0:
            print("Counts cannot be negative.")
            continue
        return value


def read_custom_ratio():
    while True:
        raw = input("Ratio (e.g. 9,3,3,1) = ").strip()
        parts = raw.split(",")
        ratio = []
        ok = True
        for part in parts:
            part = part.strip()
            if part == "":
                continue
            try:
                value = float(part)
            except (ValueError, TypeError):
                ok = False
                break
            if value <= 0:
                ok = False
                break
            ratio.append(value)
        if not ok or len(ratio) < 2:
            print("Enter at least two positive numbers separated by commas.")
            continue
        if len(ratio) > MAX_CATEGORIES:
            print("At most " + str(MAX_CATEGORIES) + " categories.")
            continue
        return ratio


def pick_ratio():
    print("\nExpected ratio:")
    for i, preset in enumerate(PRESETS):
        print(str(i + 1) + ". " + preset[0])
    choice = input("> ").strip()
    for i, preset in enumerate(PRESETS):
        if choice == str(i + 1):
            if preset[1] is None:
                return read_custom_ratio()
            return preset[1][:]
    print("Invalid choice.")
    return None


def verdict(chi, df):
    if df < 1 or df >= len(CHI2_05):
        print("\nNo critical value on file for df = " + str(df) + ".")
        return
    crit05 = CHI2_05[df]
    crit01 = CHI2_01[df]
    print("\ndf = " + str(df))
    print("Critical value at 0.05 = " + str(crit05))
    print("Critical value at 0.01 = " + str(crit01))
    if chi > crit01:
        print("chi-square exceeds the 0.01 value: reject the")
        print("hypothesis. The data do NOT fit this ratio.")
    elif chi > crit05:
        print("chi-square exceeds the 0.05 value: reject the")
        print("hypothesis at the 0.05 level. The fit is poor.")
    else:
        print("chi-square is below the 0.05 value: fail to reject.")
        print("The data are consistent with this ratio.")


def run_test():
    ratio = pick_ratio()
    if ratio is None:
        return

    print("\nEnter the observed count for each category,")
    print("in the same order as the ratio.")
    observed = []
    for i in range(len(ratio)):
        observed.append(get_count("  Category " + str(i + 1) + " (" +
                                  str(round(ratio[i], 4)) + " parts) = "))

    total = sum(observed)
    ratio_total = sum(ratio)
    if total <= 0:
        print("\nNo offspring counted.")
        return

    print("\nTotal offspring = " + str(round(total, 4)))
    print("\nCat  Obs      Exp      (O-E)^2/E")
    chi = 0.0
    smallest_expected = None
    for i in range(len(ratio)):
        expected = total * ratio[i] / ratio_total
        if smallest_expected is None or expected < smallest_expected:
            smallest_expected = expected
        if expected <= 0:
            print("An expected count is 0; chi-square is undefined.")
            return
        term = (observed[i] - expected) ** 2 / expected
        chi += term
        print(pad(i + 1, 5) + pad(round(observed[i], 2), 9) +
              pad(round(expected, 3), 9) + str(round(term, 6)))

    print("\nchi-square = " + str(round(chi, 6)))
    verdict(chi, len(ratio) - 1)
    if smallest_expected is not None and smallest_expected < 5:
        print("\nCaution: the smallest expected count is " +
              str(round(smallest_expected, 3)) + ".")
        print("Below 5 the chi-square approximation is unreliable.")


def main():
    print("=== CHISQ ===")
    print("Goodness-of-fit test for genetic crosses.")
    while True:
        try:
            run_test()
        except (ValueError, OverflowError, ZeroDivisionError):
            print("Could not compute with those values.")
        again = input("\nAnother cross? (y/n) ").strip().lower()
        if again != "y":
            break
    print("Bye.")


main()
