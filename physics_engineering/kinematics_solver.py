# Program: kinematics_solver
# Purpose: Solve 1D constant-acceleration (SUVAT) motion problems.
#          Given values for 4 of the 5 variables v0 (initial velocity),
#          v (final velocity), a (acceleration), t (time), d
#          (displacement), solves for the missing one.
# Usage: Choose which variable is unknown, then enter the other four
#        when prompted (use 0 for a variable that truly does not
#        apply, e.g. a=0 for constant velocity). Prints the solved
#        value, or a friendly message if the inputs are inconsistent
#        (e.g. division by zero).

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def main():
    print("=== SUVAT Kinematics Solver ===")
    print("Variables: v0=initial velocity, v=final velocity,")
    print("a=acceleration, t=time, d=displacement")
    while True:
        print("\nWhich variable is UNKNOWN?")
        print("1. v0   2. v   3. a   4. t   5. d")
        choice = input("Choice (1-5): ").strip()

        try:
            if choice == "1":
                v = get_float("v = ")
                a = get_float("a = ")
                t = get_float("t = ")
                d = get_float("d = ")
                try:
                    v0 = v - a * t
                    print("\nv0 = " + str(round(v0, 6)) + "  (from v = v0 + a*t)")
                except ZeroDivisionError:
                    print("Could not solve with the given values.")
            elif choice == "2":
                v0 = get_float("v0 = ")
                a = get_float("a = ")
                t = get_float("t = ")
                d = get_float("d = ")
                v = v0 + a * t
                print("\nv = " + str(round(v, 6)) + "  (from v = v0 + a*t)")
            elif choice == "3":
                v0 = get_float("v0 = ")
                v = get_float("v = ")
                t = get_float("t = ")
                d = get_float("d = ")
                if t != 0:
                    a = (v - v0) / t
                    print("\na = " + str(round(a, 6)) + "  (from a = (v-v0)/t)")
                else:
                    print("t = 0, cannot solve for acceleration this way.")
            elif choice == "4":
                v0 = get_float("v0 = ")
                v = get_float("v = ")
                a = get_float("a = ")
                d = get_float("d = ")
                if a != 0:
                    t = (v - v0) / a
                    print("\nt = " + str(round(t, 6)) + "  (from t = (v-v0)/a)")
                elif (v0 + v) != 0:
                    t = d / ((v0 + v) / 2.0)
                    print("\nt = " + str(round(t, 6)) + "  (from d = ((v0+v)/2)*t)")
                else:
                    print("Not enough information to solve for t (a=0 and v0+v=0).")
            elif choice == "5":
                v0 = get_float("v0 = ")
                v = get_float("v = ")
                a = get_float("a = ")
                t = get_float("t = ")
                d = v0 * t + 0.5 * a * t * t
                print("\nd = " + str(round(d, 6)) + "  (from d = v0*t + 0.5*a*t^2)")
            else:
                print("Invalid choice.")
        except Exception:
            print("Something went wrong with those inputs; please try again.")

        again = input("\nSolve another? (y/n): ").strip().lower()
        if again != "y":
            break
    print("Done.")


main()
