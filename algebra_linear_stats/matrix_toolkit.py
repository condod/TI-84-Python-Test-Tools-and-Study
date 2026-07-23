# Program: matrix_toolkit
# Purpose: Menu-driven matrix calculator for 2x2 and 3x3 matrices:
#          addition, multiplication, determinant, and inverse.
# Usage: Pick an operation from the menu, then enter the size (2 or 3)
#        and the matrix entries row by row when prompted. Prints the
#        resulting matrix, determinant, or a friendly error if an
#        operation is not defined (e.g. singular matrix inverse).

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def get_size():
    while True:
        raw = input("Matrix size, 2 or 3: ").strip()
        if raw in ("2", "3"):
            return int(raw)
        print("Please enter 2 or 3.")


def read_matrix(n, label="Matrix"):
    print(label + " (" + str(n) + "x" + str(n) + "):")
    mat = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(get_float("  [" + str(i + 1) + "][" + str(j + 1) + "] = "))
        mat.append(row)
    return mat


def print_matrix(mat):
    for row in mat:
        print("  " + str([round(v, 4) for v in row]))


def mat_add(a, b, n):
    return [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]


def mat_mul(a, b, n):
    result = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            total = 0.0
            for k in range(n):
                total += a[i][k] * b[k][j]
            result[i][j] = total
    return result


def det2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def determinant(m, n):
    return det2(m) if n == 2 else det3(m)


def inverse2(m):
    d = det2(m)
    if abs(d) < 1e-12:
        return None
    return [[m[1][1] / d, -m[0][1] / d],
            [-m[1][0] / d, m[0][0] / d]]


def cofactor3(m, r, c):
    rows = [i for i in range(3) if i != r]
    cols = [j for j in range(3) if j != c]
    sub = [[m[rows[0]][cols[0]], m[rows[0]][cols[1]]],
           [m[rows[1]][cols[0]], m[rows[1]][cols[1]]]]
    sign = 1 if (r + c) % 2 == 0 else -1
    return sign * det2(sub)


def inverse3(m):
    d = det3(m)
    if abs(d) < 1e-12:
        return None
    cof = [[cofactor3(m, r, c) for c in range(3)] for r in range(3)]
    adj = [[cof[c][r] for c in range(3)] for r in range(3)]
    return [[adj[i][j] / d for j in range(3)] for i in range(3)]


def main():
    print("=== Matrix Toolkit (2x2 / 3x3) ===")
    while True:
        print("\n1. Add two matrices")
        print("2. Multiply two matrices")
        print("3. Determinant")
        print("4. Inverse")
        print("5. Quit")
        choice = input("Choice (1-5): ").strip()

        if choice == "5":
            break
        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice.")
            continue

        n = get_size()

        if choice == "1":
            a = read_matrix(n, "Matrix A")
            b = read_matrix(n, "Matrix B")
            print("\nA + B =")
            print_matrix(mat_add(a, b, n))
        elif choice == "2":
            a = read_matrix(n, "Matrix A")
            b = read_matrix(n, "Matrix B")
            print("\nA * B =")
            print_matrix(mat_mul(a, b, n))
        elif choice == "3":
            a = read_matrix(n, "Matrix")
            print("\nDeterminant = " + str(round(determinant(a, n), 6)))
        elif choice == "4":
            a = read_matrix(n, "Matrix")
            inv = inverse2(a) if n == 2 else inverse3(a)
            if inv is None:
                print("\nMatrix is singular (determinant = 0); no inverse exists.")
            else:
                print("\nInverse =")
                print_matrix(inv)

    print("Done.")


main()
