# On-calc name: HARDYW
# Program: hardy_weinberg
# Purpose: Hardy-Weinberg equilibrium calculator for a single gene with
#          two alleles. Works either forward (allele frequency p ->
#          expected genotype frequencies p^2, 2pq, q^2) or backward
#          (observed genotype counts -> allele frequencies), and tests
#          whether an observed population is actually in equilibrium
#          with a chi-square goodness-of-fit test.
# Usage: Pick a tool from the menu. Frequencies are decimals between 0
#        and 1 (0.6, not 60). For the equilibrium test enter the counts
#        of homozygous dominant (AA), heterozygous (Aa), and
#        homozygous recessive (aa) individuals. Prints allele
#        frequencies, expected counts, chi-square with 1 degree of
#        freedom, and the conclusion at the 0.05 level.

from math import sqrt

CHI2_CRIT_1DF_05 = 3.841


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def get_frequency(prompt):
    while True:
        value = get_float(prompt)
        if value < 0 or value > 1:
            print("Frequency must be between 0 and 1.")
            continue
        return value


def get_count(prompt):
    while True:
        value = get_float(prompt)
        if value < 0:
            print("Counts cannot be negative.")
            continue
        return value


def report_genotypes(p, q):
    print("\np (dominant allele)  = " + str(round(p, 6)))
    print("q (recessive allele) = " + str(round(q, 6)))
    print("p^2  (AA) = " + str(round(p * p, 6)))
    print("2pq  (Aa) = " + str(round(2.0 * p * q, 6)))
    print("q^2  (aa) = " + str(round(q * q, 6)))
    print("Sum = " + str(round(p * p + 2.0 * p * q + q * q, 6)))
    carriers = 2.0 * p * q
    if carriers > 0:
        print("Carrier (Aa) frequency = " + str(round(carriers, 6)))


def from_allele_frequency():
    print("\nEnter one allele frequency; the other is 1 - it.")
    print("1. I have p (dominant)")
    print("2. I have q (recessive)")
    choice = input("> ").strip()
    if choice == "1":
        p = get_frequency("p = ")
        q = 1.0 - p
    elif choice == "2":
        q = get_frequency("q = ")
        p = 1.0 - q
    else:
        print("Invalid choice.")
        return
    report_genotypes(p, q)

    size = get_float("Population size (0 to skip counts) = ")
    if size > 0:
        print("\nExpected counts in " + str(round(size, 4)) + " individuals:")
        print("  AA = " + str(round(p * p * size, 4)))
        print("  Aa = " + str(round(2.0 * p * q * size, 4)))
        print("  aa = " + str(round(q * q * size, 4)))


def from_recessive_phenotype():
    print("\nThe recessive phenotype frequency IS q^2, so q = sqrt(q^2).")
    q2 = get_frequency("Recessive phenotype frequency (q^2) = ")
    q = sqrt(q2)
    p = 1.0 - q
    report_genotypes(p, q)


def from_counts():
    print("\nEnter observed genotype counts:")
    n_aa = get_count("  AA (homozygous dominant) = ")
    n_het = get_count("  Aa (heterozygous) = ")
    n_rec = get_count("  aa (homozygous recessive) = ")

    total = n_aa + n_het + n_rec
    if total <= 0:
        print("No individuals entered.")
        return

    # Each individual carries two alleles; heterozygotes contribute one each.
    p = (2.0 * n_aa + n_het) / (2.0 * total)
    q = 1.0 - p
    print("\nTotal individuals = " + str(round(total, 4)))
    report_genotypes(p, q)

    exp_aa = p * p * total
    exp_het = 2.0 * p * q * total
    exp_rec = q * q * total
    print("\nObserved vs expected:")
    print("  AA: " + str(round(n_aa, 4)) + " vs " + str(round(exp_aa, 4)))
    print("  Aa: " + str(round(n_het, 4)) + " vs " + str(round(exp_het, 4)))
    print("  aa: " + str(round(n_rec, 4)) + " vs " + str(round(exp_rec, 4)))

    chi = 0.0
    ok = True
    for observed, expected in ((n_aa, exp_aa), (n_het, exp_het),
                               (n_rec, exp_rec)):
        if expected <= 0:
            ok = False
            continue
        chi += (observed - expected) ** 2 / expected
    if not ok:
        print("\n(An expected count was 0, so chi-square is not valid.)")
        return

    print("\nchi-square = " + str(round(chi, 6)))
    print("df = 1, critical value at 0.05 = " + str(CHI2_CRIT_1DF_05))
    if chi > CHI2_CRIT_1DF_05:
        print("Reject equilibrium: the population is NOT in")
        print("Hardy-Weinberg equilibrium at the 0.05 level.")
    else:
        print("Fail to reject: the counts are consistent with")
        print("Hardy-Weinberg equilibrium at the 0.05 level.")
    if min(exp_aa, exp_het, exp_rec) < 5:
        print("Caution: an expected count is below 5, so the")
        print("chi-square approximation is unreliable here.")


def main():
    print("=== HARDYW ===")
    while True:
        print("\n1. From allele frequency p or q")
        print("2. From recessive phenotype (q^2)")
        print("3. From genotype counts + HWE test")
        print("0. Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                from_allele_frequency()
            elif choice == "2":
                from_recessive_phenotype()
            elif choice == "3":
                from_counts()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except (ValueError, OverflowError, ZeroDivisionError):
            print("Could not compute with those values.")
    print("Bye.")


main()
