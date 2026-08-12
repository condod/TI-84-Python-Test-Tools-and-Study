# On-calc name: DISCRT
# Program: discrete_math_toolkit
# Purpose: Two discrete-math/CS tools: (1) a number base converter
#          between binary, octal, decimal, and hex, and (2) a boolean
#          truth-table generator for a typed expression of up to 3
#          variables (A, B, C) using and/or/not/^ (xor).
# Usage: Pick a tool from the menu. The base converter asks for the
#        from/to bases and a value in the from-base. The truth table
#        asks for a variable count and an expression, e.g.
#        "A and not B" or "A ^ B", then prints every input/output row.

BASE_NAMES = {2: "Binary", 8: "Octal", 10: "Decimal", 16: "Hex"}


def get_base(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            b = int(raw)
        except (ValueError, TypeError):
            print("Enter 2, 8, 10, or 16.")
            continue
        if b in BASE_NAMES:
            return b
        print("Enter 2, 8, 10, or 16.")


def to_base(n, base):
    if n == 0:
        return "0"
    digits = "0123456789ABCDEF"
    negative = n < 0
    n = abs(n)
    result = ""
    count = 0
    while n > 0 and count < 64:
        result = digits[n % base] + result
        n = n // base
        count += 1
    if negative:
        result = "-" + result
    return result


def base_converter():
    print("\nBases: 2=Binary  8=Octal  10=Decimal  16=Hex")
    from_base = get_base("Convert FROM base: ")
    to_base_choice = get_base("Convert TO base: ")
    while True:
        raw = input("Value (in base " + str(from_base) + ") = ").strip()
        try:
            value = int(raw, from_base)
            break
        except (ValueError, TypeError):
            print("Invalid digits for base " + str(from_base) + ".")

    print("\n" + BASE_NAMES[from_base] + " " + raw + " = " +
          BASE_NAMES[to_base_choice] + " " + to_base(value, to_base_choice))


def get_var_count():
    while True:
        raw = input("\nNumber of variables (1-3): ").strip()
        if raw in ("1", "2", "3"):
            return int(raw)
        print("Enter 1, 2, or 3.")


def evaluate(expr, A, B, C):
    return eval(expr)


def valid_expr(expr):
    try:
        evaluate(expr, True, True, True)
        return True
    except Exception:
        return False


def truth_table():
    n = get_var_count()
    names = ["A", "B", "C"][:n]
    print("Enter a boolean expression using " + ", ".join(names) + ".")
    print("Operators: and, or, not, ^ (xor). Example: A and not B")
    while True:
        expr = input("Expression = ").strip()
        if expr == "":
            print("Please enter an expression.")
            continue
        if valid_expr(expr):
            break
        print("Could not evaluate that expression. Try again.")

    print("\n" + "  ".join(names) + " | Result")
    rows = 2 ** n
    count = 0
    while count < rows:
        values = []
        i = 0
        while i < n:
            bit = (count >> (n - 1 - i)) & 1
            values.append(bit == 1)
            i += 1
        a = values[0] if n >= 1 else False
        b = values[1] if n >= 2 else False
        c = values[2] if n >= 3 else False

        try:
            result = evaluate(expr, a, b, c)
        except Exception:
            result = None

        line_parts = []
        for v in values:
            line_parts.append("T" if v else "F")
        if result is True:
            line_parts.append("| T")
        elif result is False:
            line_parts.append("| F")
        else:
            line_parts.append("| ERR")
        print("  ".join(line_parts))
        count += 1


def main():
    print("=== DISCRT ===")
    while True:
        print("\n1. Base converter")
        print("2. Truth table")
        print("0. Quit")
        choice = input("> ").strip()
        if choice == "1":
            base_converter()
        elif choice == "2":
            truth_table()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
    print("Bye.")


main()
