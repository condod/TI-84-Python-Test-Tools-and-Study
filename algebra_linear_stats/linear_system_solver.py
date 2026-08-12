# On-calc name: LINSOLV
# Program: linear_system_solver
# Purpose: Solve a system of 2 or 3 linear equations in 2 or 3
#          unknowns using Gaussian elimination with partial pivoting.
# Usage: Choose system size (2 or 3). Enter each equation's
#        coefficients and constant term (row of the augmented matrix)
#        when prompted. Prints the solution, or reports if the system
#        is inconsistent or has infinitely many solutions.

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def read_augmented(n):
    rows = []
    letters = "xyz"
    for i in range(n):
        print("\nEquation " + str(i + 1) + ":")
        row = []
        for j in range(n):
            row.append(get_float("  coefficient of " + letters[j] + " = "))
        row.append(get_float("  constant (right side) = "))
        rows.append(row)
    return rows


def gaussian_eliminate(mat, n):
    for col in range(n):
        pivot_row = col
        best = abs(mat[col][col])
        for r in range(col + 1, n):
            if abs(mat[r][col]) > best:
                best = abs(mat[r][col])
                pivot_row = r
        if best < 1e-12:
            return None
        mat[col], mat[pivot_row] = mat[pivot_row], mat[col]

        pivot = mat[col][col]
        for j in range(col, n + 1):
            mat[col][j] /= pivot

        for r in range(n):
            if r != col:
                factor = mat[r][col]
                for j in range(col, n + 1):
                    mat[r][j] -= factor * mat[col][j]
    return [mat[i][n] for i in range(n)]


def main():
    print("=== LINSOLV ===")
    while True:
        n = None
        while n not in (2, 3):
            raw = input("System size, 2 or 3: ").strip()
            if raw in ("2", "3"):
                n = int(raw)
            else:
                print("Please enter 2 or 3.")

        mat = read_augmented(n)
        solution = gaussian_eliminate([row[:] for row in mat], n)

        letters = "xyz"
        if solution is None:
            print("\nThis system has no unique solution.")
            print("It may be inconsistent (no solution) or dependent (infinitely many solutions).")
        else:
            print("\nSolution:")
            for i in range(n):
                print(letters[i] + " = " + str(round(solution[i], 6)))

        print("\n1. Again  0. Quit")
        if input("> ").strip() == "0":
            break
    print("Bye.")


main()
