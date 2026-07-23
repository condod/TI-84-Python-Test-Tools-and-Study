# Program: formula_flashcards
# Purpose: Self-study flashcard quiz. Pick a subject category and the
#          program randomly shows a formula NAME; you try to recall
#          the formula from memory, then press Enter to reveal it and
#          self-grade. This is a MEMORIZATION STUDY AID ONLY -- it is
#          not meant to be used as an answer-lookup tool during an
#          actual exam. Only use it while practicing/studying, and
#          always follow your exam's calculator/program policy.
# Usage: Choose a subject category, then how many questions to try.
#        For each one: read the formula name, think of (or say aloud)
#        the formula, press Enter to reveal the answer, then mark
#        whether you got it right. Prints a final score.

import random

CARDS = {
    "Calculus": [
        ("Derivative of x^n", "d/dx[x^n] = n*x^(n-1)"),
        ("Derivative of sin(x)", "d/dx[sin(x)] = cos(x)"),
        ("Derivative of e^x", "d/dx[e^x] = e^x"),
        ("Product rule", "d/dx[uv] = u'v + uv'"),
        ("Quotient rule", "d/dx[u/v] = (u'v - uv')/v^2"),
        ("Chain rule", "d/dx[f(g(x))] = f'(g(x))*g'(x)"),
        ("Power rule for integrals", "Integral x^n dx = x^(n+1)/(n+1) + C"),
        ("Fundamental Theorem of Calculus", "Integral(a,b) f'(x)dx = f(b)-f(a)"),
    ],
    "Physics": [
        ("Newton's Second Law", "F = m*a"),
        ("Kinetic energy", "KE = 0.5*m*v^2"),
        ("Gravitational PE", "PE = m*g*h"),
        ("Momentum", "p = m*v"),
        ("Ohm's Law", "V = I*R"),
        ("Work", "W = F*d*cos(theta)"),
        ("Coulomb's Law", "F = k*q1*q2 / r^2"),
        ("Ideal Gas Law", "P*V = n*R*T"),
    ],
    "Algebra": [
        ("Quadratic Formula", "x = (-b +/- sqrt(b^2-4ac)) / (2a)"),
        ("Slope formula", "m = (y2-y1)/(x2-x1)"),
        ("Distance formula", "d = sqrt((x2-x1)^2+(y2-y1)^2)"),
        ("Point-slope form", "y - y1 = m(x - x1)"),
        ("Sum of arithmetic series", "S_n = n/2 * (a1 + a_n)"),
        ("Sum of geometric series", "S_n = a1*(1-r^n)/(1-r), r!=1"),
    ],
    "Chemistry": [
        ("Moles from mass", "n = mass / molar mass"),
        ("Molarity", "M = moles of solute / liters of solution"),
        ("Combined Gas Law", "P1V1/T1 = P2V2/T2"),
        ("pH", "pH = -log10[H+]"),
        ("Density", "density = mass / volume"),
    ],
}


def get_int(prompt, lo, hi):
    while True:
        try:
            n = int(input(prompt))
            if lo <= n <= hi:
                return n
            print("Enter a number between " + str(lo) + " and " + str(hi) + ".")
        except (ValueError, TypeError):
            print("Please enter a whole number.")


def main():
    print("=== Formula Flashcard Self-Quiz ===")
    print("STUDY TOOL ONLY: use this to practice recall before an exam,")
    print("not to look up answers during an actual exam.\n")

    categories = list(CARDS.keys())
    while True:
        print("Categories:")
        for i, cat in enumerate(categories):
            print(str(i + 1) + ". " + cat)
        idx = get_int("Choice: ", 1, len(categories)) - 1
        cat = categories[idx]
        deck = CARDS[cat][:]

        max_q = len(deck)
        n_q = get_int("How many questions (1-" + str(max_q) + ")? ", 1, max_q)

        random.shuffle(deck)
        chosen = deck[:n_q]

        score = 0
        for i, (name, formula) in enumerate(chosen):
            print("\nQuestion " + str(i + 1) + "/" + str(n_q) + ": " + name)
            input("Think of the formula, then press Enter to reveal...")
            print("Answer: " + formula)
            ans = input("Did you get it right? (y/n): ").strip().lower()
            if ans == "y":
                score += 1

        print("\nScore: " + str(score) + "/" + str(n_q))

        again = input("\nQuiz another category? (y/n): ").strip().lower()
        if again != "y":
            break
    print("Keep practicing! Done.")


main()
