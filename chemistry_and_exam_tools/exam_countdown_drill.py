# Program: exam_countdown_drill
# Purpose: Two practice-exam helpers in one menu: (1) a simple
#          countdown timer to time yourself on practice problems, and
#          (2) a random mental-math / unit-sanity-check drill
#          generator that creates quick practice problems and checks
#          your answer against the correct value (with a small
#          tolerance for rounding).
# Usage: Pick "Timer" and enter minutes to count down; the remaining
#        time updates once per second (press [on]/break to stop
#        early). Pick "Drill" and choose a category, then answer each
#        generated problem; the program tells you if you're right.

import random
import time

try:
    import ti_system as ti
    def clear_screen():
        ti.disp_clr()
except ImportError:
    def clear_screen():
        print("\n" * 6)


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def get_int(prompt, lo, hi):
    while True:
        try:
            n = int(input(prompt))
            if lo <= n <= hi:
                return n
            print("Enter a number between " + str(lo) + " and " + str(hi) + ".")
        except (ValueError, TypeError):
            print("Please enter a whole number.")


def run_timer():
    minutes = get_float("Countdown minutes (e.g. 5): ")
    if minutes <= 0:
        print("Enter a positive number of minutes.")
        return
    total_seconds = int(minutes * 60)

    print("Starting countdown. Press [on] to stop early if needed.")
    try:
        remaining = total_seconds
        while remaining >= 0:
            mins = remaining // 60
            secs = remaining % 60
            clear_screen()
            print("=== Countdown ===")
            print(str(mins).rjust(2, "0") + ":" + str(secs).rjust(2, "0") + " remaining")
            if remaining == 0:
                break
            time.sleep(1)
            remaining -= 1
        print("\nTime's up!")
    except KeyboardInterrupt:
        print("\nTimer stopped early.")


def gen_arithmetic():
    a = random.randint(2, 50)
    b = random.randint(2, 50)
    op = random.choice(["+", "-", "*"])
    if op == "+":
        answer = a + b
    elif op == "-":
        answer = a - b
    else:
        answer = a * b
    question = str(a) + " " + op + " " + str(b)
    return question, float(answer)


def gen_order_of_magnitude():
    base = random.choice([10 ** e for e in range(-3, 7)])
    factor = round(random.uniform(1.0, 9.9), 1)
    value = base * factor
    question = "Estimate the order of magnitude (power of 10) of: " + str(value)
    answer = 0
    v = value
    while v >= 10:
        v /= 10.0
        answer += 1
    while v < 1:
        v *= 10.0
        answer -= 1
    return question, float(answer)


def gen_percent():
    pct = random.choice([5, 10, 12.5, 20, 25, 50, 75])
    base = random.randint(10, 400)
    question = "What is " + str(pct) + "% of " + str(base) + "?"
    answer = pct / 100.0 * base
    return question, float(answer)


DRILLS = {
    "1": ("Arithmetic", gen_arithmetic, 0.001),
    "2": ("Order-of-magnitude estimate", gen_order_of_magnitude, 0.001),
    "3": ("Percent of a number", gen_percent, 0.01),
}


def run_drill():
    print("\nDrill categories:")
    for key, (name, _, _) in DRILLS.items():
        print(key + ". " + name)
    choice = input("Choice: ").strip()
    if choice not in DRILLS:
        print("Invalid choice.")
        return

    name, generator, tol = DRILLS[choice]
    n_q = get_int("How many problems (1-20)? ", 1, 20)

    score = 0
    for i in range(n_q):
        question, answer = generator()
        print("\nProblem " + str(i + 1) + "/" + str(n_q) + ": " + question)
        user_answer = get_float("Your answer = ")
        if abs(user_answer - answer) <= max(tol, abs(answer) * 0.01):
            print("Correct!")
            score += 1
        else:
            print("Not quite. Correct answer: " + str(round(answer, 4)))

    print("\nScore: " + str(score) + "/" + str(n_q))


def main():
    print("=== Exam-Prep Countdown Timer & Drill Generator ===")
    while True:
        print("\n1. Countdown timer")
        print("2. Mental-math / sanity-check drill")
        print("3. Quit")
        choice = input("Choice (1-3): ").strip()
        if choice == "1":
            run_timer()
        elif choice == "2":
            run_drill()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
    print("Done.")


main()
