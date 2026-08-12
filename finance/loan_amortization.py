# On-calc name: LOAN
# Program: loan_amortization
# Purpose: Build a loan amortization schedule. Computes the level
#          payment for a fully-amortizing loan, then reports how each
#          payment splits between interest and principal and how the
#          balance falls, plus lifetime totals.
# Usage: Enter the loan amount, the annual interest rate as a percent,
#        the term in years, and the number of payments per year (12 for
#        monthly). Then pick a view: the full payment-by-payment
#        schedule (paused every 12 rows so it does not scroll away), a
#        year-by-year summary, or just the totals. You can also enter a
#        payment of your own to see the effect of paying extra.

MAX_PAYMENTS = 600


def money(value):
    # Fixed 2-decimal text; str.format() is avoided across this library.
    negative = value < 0
    cents = int(round(abs(value) * 100.0))
    text = str(cents // 100) + "." + ("0" + str(cents % 100))[-2:]
    if negative and cents != 0:
        text = "-" + text
    return text


def pad(text, width):
    # stand-in for str.ljust(), which the calculator's Python lacks
    s = str(text)
    if len(s) >= width:
        return s
    return s + " " * (width - len(s))


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def get_positive(prompt):
    while True:
        value = get_float(prompt)
        if value <= 0:
            print("Please enter a positive number.")
            continue
        return value


def level_payment(principal, i, n):
    # Standard amortization payment; the i == 0 case is a plain split.
    if i == 0:
        return principal / n
    return principal * i / (1.0 - (1.0 + i) ** (-n))


def build_schedule(principal, i, payment, max_rows):
    # Returns (rows, total_interest, paid_off). Rows are built one at a
    # time and never all held at once beyond the display cap.
    rows = []
    balance = principal
    total_interest = 0.0
    count = 0
    while balance > 0.005 and count < max_rows:
        interest = balance * i
        principal_part = payment - interest
        if principal_part <= 0:
            return None, 0.0, False
        if principal_part > balance:
            principal_part = balance
        balance = balance - principal_part
        total_interest += interest
        count += 1
        rows.append((count, interest, principal_part, balance))
    return rows, total_interest, balance <= 0.005


def show_full(rows):
    print("\n Pmt  Interest    Principal   Balance")
    for row in rows:
        print(pad(row[0], 5) + pad(money(row[1]), 12) +
              pad(money(row[2]), 12) + money(row[3]))
        if row[0] % 12 == 0 and row[0] != len(rows):
            input("ENTER for more")


def show_yearly(rows, per_year):
    print("\n Yr   Interest    Principal   Balance")
    year_interest = 0.0
    year_principal = 0.0
    for row in rows:
        year_interest += row[1]
        year_principal += row[2]
        if row[0] % per_year == 0 or row[0] == len(rows):
            year = (row[0] + per_year - 1) // per_year
            print(pad(year, 5) + pad(money(year_interest), 12) +
                  pad(money(year_principal), 12) + money(row[3]))
            year_interest = 0.0
            year_principal = 0.0
            if year % 10 == 0:
                input("ENTER for more")


def main():
    print("=== LOAN ===")
    while True:
        principal = get_positive("Loan amount = ")
        annual_rate = get_float("Annual rate % = ")
        years = get_positive("Term in years = ")
        per_year = get_positive("Payments per year (12=monthly) = ")

        n = int(round(years * per_year))
        if n < 1:
            print("That term is too short to make a payment.")
            continue
        if n > MAX_PAYMENTS:
            print("That is " + str(n) + " payments; this program caps at " +
                  str(MAX_PAYMENTS) + ".")
            continue

        i = annual_rate / 100.0 / per_year
        scheduled = level_payment(principal, i, n)
        print("\nScheduled payment = " + money(scheduled))

        payment = scheduled
        custom = input("Use a different payment? (y/n) ").strip().lower()
        if custom == "y":
            payment = get_positive("Payment = ")
            if payment <= principal * i:
                print("That payment never covers the interest;")
                print("the balance would grow forever.")
                continue

        rows, total_interest, paid_off = build_schedule(
            principal, i, payment, MAX_PAYMENTS)
        if rows is None:
            print("That payment never covers the interest.")
            continue

        print("\n1. Full schedule")
        print("2. Year-by-year summary")
        print("3. Totals only")
        view = input("> ").strip()
        if view == "1":
            show_full(rows)
        elif view == "2":
            show_yearly(rows, int(per_year))

        print("\nPayments made = " + str(len(rows)))
        print("Total paid = " + money(payment * (len(rows) - 1) + rows[-1][1] +
                                      rows[-1][2]))
        print("Total interest = " + money(total_interest))
        if not paid_off:
            print("Balance remaining = " + money(rows[-1][3]))
            print("(hit the " + str(MAX_PAYMENTS) + "-payment cap)")

        again = input("\nAnother loan? (y/n) ").strip().lower()
        if again != "y":
            break

    print("Bye.")


main()
