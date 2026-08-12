# On-calc name: CONFINT
# Program: confidence_interval_hypothesis_test
# Purpose: One-sample confidence interval for a population mean, and a
#          one-sample hypothesis test for a mean, using either a z
#          (population sigma known) or t (sample stdev s, df = n-1)
#          critical value. Critical values come from a built-in
#          standard-normal / Student's t table (no inverse-CDF
#          function is available on-device); t degrees of freedom
#          above 30 fall back to the normal (z) row, same as most
#          textbook t-tables.
# Usage: Pick confidence interval or hypothesis test from the menu,
#        then z or t. Enter the sample mean, sample size n, and sigma
#        (population) or s (sample). The hypothesis test also asks for
#        the claimed mean mu0, the tail direction, and a significance
#        level. Prints the interval, or the test statistic, critical
#        value, and a reject/fail-to-reject conclusion.

from math import sqrt

# Student's t critical values: (df, t.10, t.05, t.025, t.01, t.005)
T_TABLE = [
    (1, 3.078, 6.314, 12.706, 31.821, 63.657),
    (2, 1.886, 2.920, 4.303, 6.965, 9.925),
    (3, 1.638, 2.353, 3.182, 4.541, 5.841),
    (4, 1.533, 2.132, 2.776, 3.747, 4.604),
    (5, 1.476, 2.015, 2.571, 3.365, 4.032),
    (6, 1.440, 1.943, 2.447, 3.143, 3.707),
    (7, 1.415, 1.895, 2.365, 2.998, 3.499),
    (8, 1.397, 1.860, 2.306, 2.896, 3.355),
    (9, 1.383, 1.833, 2.262, 2.821, 3.250),
    (10, 1.372, 1.812, 2.228, 2.764, 3.169),
    (11, 1.363, 1.796, 2.201, 2.718, 3.106),
    (12, 1.356, 1.782, 2.179, 2.681, 3.055),
    (13, 1.350, 1.771, 2.160, 2.650, 3.012),
    (14, 1.345, 1.761, 2.145, 2.624, 2.977),
    (15, 1.341, 1.753, 2.131, 2.602, 2.947),
    (16, 1.337, 1.746, 2.120, 2.583, 2.921),
    (17, 1.333, 1.740, 2.110, 2.567, 2.898),
    (18, 1.330, 1.734, 2.101, 2.552, 2.878),
    (19, 1.328, 1.729, 2.093, 2.539, 2.861),
    (20, 1.325, 1.725, 2.086, 2.528, 2.845),
    (21, 1.323, 1.721, 2.080, 2.518, 2.831),
    (22, 1.321, 1.717, 2.074, 2.508, 2.819),
    (23, 1.319, 1.714, 2.069, 2.500, 2.807),
    (24, 1.318, 1.711, 2.064, 2.492, 2.797),
    (25, 1.316, 1.708, 2.060, 2.485, 2.787),
    (26, 1.315, 1.706, 2.056, 2.479, 2.779),
    (27, 1.314, 1.703, 2.052, 2.473, 2.771),
    (28, 1.313, 1.701, 2.048, 2.467, 2.763),
    (29, 1.311, 1.699, 2.045, 2.462, 2.756),
    (30, 1.310, 1.697, 2.042, 2.457, 2.750),
]
Z_ROW = (1.282, 1.645, 1.960, 2.326, 2.576)

# Column index for one-tailed alpha, and for two-tailed alpha (uses alpha/2).
ONE_TAIL_COL = {"1": 0, "2": 1, "3": 3}
TWO_TAIL_COL = {"1": 1, "2": 2, "3": 4}
ALPHA_LABEL = {"1": "0.10", "2": "0.05", "3": "0.01"}


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def get_sample_size(prompt):
    while True:
        try:
            value = int(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a whole number.")
            continue
        if value < 2:
            print("Sample size must be at least 2.")
            continue
        return value


def t_row(df):
    if df > 30:
        return Z_ROW
    index = 0
    while index < len(T_TABLE):
        if T_TABLE[index][0] >= df:
            return T_TABLE[index][1:]
        index += 1
    return T_TABLE[-1][1:]


def pick_mode():
    print("1. Z (population sigma known)  2. T (sample stdev s)")
    return input("> ").strip()


def pick_alpha():
    print("Significance level:  1. 0.10   2. 0.05   3. 0.01")
    choice = input("> ").strip()
    if choice not in ALPHA_LABEL:
        choice = "2"
    return choice


def confidence_interval():
    mode = pick_mode()
    xbar = get_float("Sample mean xbar = ")
    n = get_sample_size("Sample size n = ")
    if mode == "1":
        spread = get_float("Population sigma = ")
        row = Z_ROW
        label = "z"
    else:
        spread = get_float("Sample stdev s = ")
        row = t_row(n - 1)
        label = "t"
    print("Confidence level:  1. 90%   2. 95%   3. 99%")
    level = input("> ").strip()
    if level == "1":
        crit = row[1]
    elif level == "3":
        crit = row[4]
    else:
        crit = row[2]

    margin = crit * spread / sqrt(n)
    print("\nCritical " + label + "* = " + str(round(crit, 4)))
    print("Margin of error = " + str(round(margin, 6)))
    print("Confidence interval = (" + str(round(xbar - margin, 6)) + ", "
          + str(round(xbar + margin, 6)) + ")")


def hypothesis_test():
    mode = pick_mode()
    mu0 = get_float("Claimed mean mu0 = ")
    xbar = get_float("Sample mean xbar = ")
    n = get_sample_size("Sample size n = ")
    if mode == "1":
        spread = get_float("Population sigma = ")
        row = Z_ROW
        label = "z"
    else:
        spread = get_float("Sample stdev s = ")
        row = t_row(n - 1)
        label = "t"

    print("Alternative hypothesis:")
    print("1. Two-tailed (mu != mu0)")
    print("2. Left-tailed (mu < mu0)")
    print("3. Right-tailed (mu > mu0)")
    tail = input("> ").strip()
    if tail not in ("1", "2", "3"):
        tail = "1"
    alpha_choice = pick_alpha()
    if tail == "1":
        crit = row[TWO_TAIL_COL[alpha_choice]]
    else:
        crit = row[ONE_TAIL_COL[alpha_choice]]

    stat = (xbar - mu0) / (spread / sqrt(n))
    print("\nTest statistic " + label + " = " + str(round(stat, 4)))
    print("Critical value = " + str(round(crit, 4)))

    if tail == "1":
        reject = abs(stat) > crit
    elif tail == "2":
        reject = stat < -crit
    else:
        reject = stat > crit

    if reject:
        print("Reject H0 at alpha = " + ALPHA_LABEL[alpha_choice] + ".")
    else:
        print("Fail to reject H0 at alpha = " + ALPHA_LABEL[alpha_choice] + ".")


def main():
    print("=== CONFINT ===")
    while True:
        print("\n1. Confidence interval for a mean")
        print("2. Hypothesis test for a mean")
        print("0. Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                confidence_interval()
            elif choice == "2":
                hypothesis_test()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except Exception:
            print("Could not compute with those values.")
    print("Bye.")


main()
