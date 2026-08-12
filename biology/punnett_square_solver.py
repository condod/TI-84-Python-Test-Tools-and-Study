# On-calc name: PUNNET
# Program: punnett_square_solver
# Purpose: Cross two parent genotypes and report offspring genotype
#          and phenotype ratios via a Punnett square. Supports a
#          monohybrid cross (1 gene, e.g. Aa x Aa) or a dihybrid cross
#          (2 independently-assorting genes, e.g. AaBb x AaBb).
# Usage: Pick monohybrid or dihybrid. Enter the letter(s) used for
#        each gene, then each parent's genotype using that letter in
#        upper/lower case (e.g. Aa, AABB). Prints the offspring
#        genotype and phenotype ratios (assumes simple dominant/
#        recessive inheritance, uppercase = dominant allele).


def get_letter(prompt):
    while True:
        raw = input(prompt).strip()
        if len(raw) == 1 and raw.isalpha():
            return raw.upper()
        print("Enter a single letter, e.g. A")


def get_allele_pair(prompt, letter):
    lower = letter.lower()
    upper = letter.upper()
    allowed = set([lower, upper])
    while True:
        raw = input(prompt).strip()
        if len(raw) == 2 and set(raw) <= allowed:
            return [raw[0], raw[1]]
        print("Enter two characters using " + upper + "/" + lower + ", e.g. " + upper + lower)


def get_full_dihybrid(prompt, letter1, letter2):
    allowed = set([letter1.upper(), letter1.lower(), letter2.upper(), letter2.lower()])
    while True:
        raw = input(prompt).strip()
        if len(raw) == 4 and set(raw) <= allowed:
            gene1_chars = [ch for ch in raw if ch.upper() == letter1]
            gene2_chars = [ch for ch in raw if ch.upper() == letter2]
            if len(gene1_chars) == 2 and len(gene2_chars) == 2:
                return (gene1_chars, gene2_chars)
        print("Enter 4 letters: two " + letter1.upper() + "/" + letter1.lower() +
              " and two " + letter2.upper() + "/" + letter2.lower() + ".")


def canonical_pair(a1, a2):
    if a1.isupper() and a2.islower():
        return a1 + a2
    if a2.isupper() and a1.islower():
        return a2 + a1
    pair = [a1, a2]
    pair.sort()
    return "".join(pair)


def is_dominant(genotype):
    for ch in genotype:
        if ch.isupper():
            return True
    return False


def cross_one_gene(parent1, parent2):
    results = []
    for a1 in parent1:
        for a2 in parent2:
            results.append(canonical_pair(a1, a2))
    return results


def tally(items):
    counts = {}
    order = []
    for item in items:
        if item not in counts:
            counts[item] = 0
            order.append(item)
        counts[item] += 1
    return counts, order


def print_ratio(title, counts, order):
    print("\n" + title)
    parts = []
    for key in order:
        parts.append(key + "=" + str(counts[key]))
    print(", ".join(parts))
    ratio_parts = [str(counts[key]) for key in order]
    print("Ratio " + ":".join(order) + " = " + ":".join(ratio_parts))


def monohybrid():
    letter = get_letter("\nGene letter (e.g. A): ")
    example = letter + letter.lower()
    p1 = get_allele_pair("Parent 1 genotype (e.g. " + example + "): ", letter)
    p2 = get_allele_pair("Parent 2 genotype (e.g. " + example + "): ", letter)

    offspring = cross_one_gene(p1, p2)
    geno_counts, geno_order = tally(offspring)
    print_ratio("Genotype ratio (out of 4):", geno_counts, geno_order)

    phenotypes = []
    for g in offspring:
        if is_dominant(g):
            phenotypes.append("Dominant")
        else:
            phenotypes.append("Recessive")
    pheno_counts, pheno_order = tally(phenotypes)
    print_ratio("Phenotype ratio (out of 4):", pheno_counts, pheno_order)


def dihybrid():
    letter1 = get_letter("\nGene 1 letter (e.g. A): ")
    while True:
        letter2 = get_letter("Gene 2 letter (e.g. B): ")
        if letter2 != letter1:
            break
        print("Gene 2 must use a different letter than gene 1.")

    example = letter1 + letter1.lower() + letter2 + letter2.lower()
    print("Enter each parent as 4 letters, gene 1 then gene 2 (e.g. " + example + ")")
    p1_genes = get_full_dihybrid("Parent 1 genotype: ", letter1, letter2)
    p2_genes = get_full_dihybrid("Parent 2 genotype: ", letter1, letter2)

    gene1_offspring = cross_one_gene(p1_genes[0], p2_genes[0])
    gene2_offspring = cross_one_gene(p1_genes[1], p2_genes[1])

    combined = []
    phenotypes = []
    for g1 in gene1_offspring:
        for g2 in gene2_offspring:
            combined.append(g1 + g2)
            p1_pheno = "Dom1" if is_dominant(g1) else "Rec1"
            p2_pheno = "Dom2" if is_dominant(g2) else "Rec2"
            phenotypes.append(p1_pheno + "+" + p2_pheno)

    geno_counts, geno_order = tally(combined)
    print_ratio("Genotype ratio (out of 16):", geno_counts, geno_order)

    pheno_counts, pheno_order = tally(phenotypes)
    print_ratio("Phenotype ratio (out of 16):", pheno_counts, pheno_order)


def main():
    print("=== PUNNET ===")
    while True:
        print("\n1. Monohybrid cross (1 gene)")
        print("2. Dihybrid cross (2 genes)")
        print("0. Quit")
        choice = input("> ").strip()
        if choice == "1":
            monohybrid()
        elif choice == "2":
            dihybrid()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
    print("Bye.")


main()
