# On-calc name: STATS
# Program: descriptive_stats
# Purpose: Compute descriptive statistics (mean, median, mode, sample
#          and population variance/standard deviation, min, max, range)
#          from a list of numbers the user enters.
# Usage: Enter numbers one at a time (blank line to finish), or as a
#        single comma-separated line, e.g. 3,5,5,7,9. Prints all the
#        summary statistics for the entered data set (up to 90 values).

MAX_VALUES = 90


def read_data():
    while True:
        raw = input("Enter numbers separated by commas (or one at a time,\nblank line to finish):\n> ").strip()
        values = []
        if "," in raw:
            parts = raw.split(",")
            ok = True
            for p in parts:
                p = p.strip()
                if p == "":
                    continue
                try:
                    values.append(float(p))
                except (ValueError, TypeError):
                    ok = False
                    break
            if not ok:
                print("Could not parse one of the values. Try again.")
                continue
        elif raw != "":
            try:
                values.append(float(raw))
            except (ValueError, TypeError):
                print("Could not parse that value. Try again.")
                continue
            while len(values) < MAX_VALUES:
                more = input("> ").strip()
                if more == "":
                    break
                try:
                    values.append(float(more))
                except (ValueError, TypeError):
                    print("Could not parse that value; skipped.")

        if len(values) < 1:
            print("Please enter at least one number.")
            continue
        if len(values) > MAX_VALUES:
            print("Too many values; using first " + str(MAX_VALUES) + ".")
            values = values[:MAX_VALUES]
        return values


def mean_of(values):
    return sum(values) / len(values)


def median_of(values):
    s = sorted(values)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2.0


def mode_of(values):
    counts = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1
    best_count = max(counts.values())
    if best_count == 1:
        return None
    modes = [v for v in counts if counts[v] == best_count]
    return sorted(modes)


def variance_of(values, m, ddof):
    n = len(values)
    if n - ddof <= 0:
        return None
    total = 0.0
    for v in values:
        total += (v - m) ** 2
    return total / (n - ddof)


def main():
    print("=== STATS ===")
    while True:
        data = read_data()
        n = len(data)
        m = mean_of(data)
        med = median_of(data)
        modes = mode_of(data)

        print("\nn = " + str(n))
        print("Sum = " + str(round(sum(data), 6)))
        print("Mean = " + str(round(m, 6)))
        print("Median = " + str(round(med, 6)))
        if modes is None:
            print("Mode = none (all values unique)")
        else:
            print("Mode = " + str(modes))
        print("Min = " + str(min(data)) + "   Max = " + str(max(data)) + "   Range = " + str(max(data) - min(data)))

        if n >= 2:
            sample_var = variance_of(data, m, 1)
            print("Sample variance (n-1) = " + str(round(sample_var, 6)))
            print("Sample std dev (n-1) = " + str(round(sample_var ** 0.5, 6)))
        pop_var = variance_of(data, m, 0)
        print("Population variance (n) = " + str(round(pop_var, 6)))
        print("Population std dev (n) = " + str(round(pop_var ** 0.5, 6)))

        print("\n1. Again  0. Quit")
        if input("> ").strip() == "0":
            break
    print("Bye.")


main()
