# On-calc name: BREAKEVN
# Program: break_even_margin
# Purpose: Break-even and margin analysis: break-even point in units
#          and in revenue, units needed to hit a target profit, the
#          contribution margin and its ratio, the margin of safety, and
#          conversions between gross margin and markup.
# Usage: Pick a tool from the menu and enter price per unit, variable
#        cost per unit, and fixed costs in whatever currency you like
#        (the answers come back in the same units). Break-even needs
#        price to exceed variable cost per unit, or no volume ever
#        covers the fixed costs, and the program says so.


def money(value):
    # Fixed 2-decimal text; str.format() is avoided across this library.
    negative = value < 0
    cents = int(round(abs(value) * 100.0))
    text = str(cents // 100) + "." + ("0" + str(cents % 100))[-2:]
    if negative and cents != 0:
        text = "-" + text
    return text


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def contribution(price, variable):
    return price - variable


def break_even():
    price = get_float("Price per unit = ")
    variable = get_float("Variable cost per unit = ")
    fixed = get_float("Total fixed costs = ")

    margin = contribution(price, variable)
    if margin <= 0:
        print("\nContribution margin = " + money(margin))
        print("Price does not exceed variable cost, so there is no")
        print("break-even point: every unit adds to the loss.")
        return

    units = fixed / margin
    print("\nContribution margin = " + money(margin) + " per unit")
    if price != 0:
        print("Contribution margin ratio = " +
              str(round(margin / price * 100.0, 4)) + " %")
    print("Break-even units = " + str(round(units, 4)))
    print("Break-even revenue = " + money(units * price))


def target_profit():
    price = get_float("Price per unit = ")
    variable = get_float("Variable cost per unit = ")
    fixed = get_float("Total fixed costs = ")
    target = get_float("Target profit = ")

    margin = contribution(price, variable)
    if margin <= 0:
        print("\nPrice does not exceed variable cost; the target")
        print("profit cannot be reached at any volume.")
        return

    units = (fixed + target) / margin
    print("\nUnits needed = " + str(round(units, 4)))
    print("Revenue needed = " + money(units * price))


def margin_of_safety():
    price = get_float("Price per unit = ")
    variable = get_float("Variable cost per unit = ")
    fixed = get_float("Total fixed costs = ")
    actual = get_float("Actual (or expected) unit sales = ")

    margin = contribution(price, variable)
    if margin <= 0:
        print("\nPrice does not exceed variable cost; no break-even point.")
        return

    units = fixed / margin
    safety_units = actual - units
    print("\nBreak-even units = " + str(round(units, 4)))
    print("Margin of safety = " + str(round(safety_units, 4)) + " units")
    if actual > 0:
        print("As a percent of sales = " +
              str(round(safety_units / actual * 100.0, 4)) + " %")
    profit = margin * actual - fixed
    print("Profit at that volume = " + money(profit))


def margin_vs_markup():
    print("\n1. Cost and price -> margin and markup")
    print("2. Margin % -> markup %")
    print("3. Markup % -> margin %")
    choice = input("> ").strip()

    if choice == "1":
        cost = get_float("Cost = ")
        price = get_float("Price = ")
        profit = price - cost
        if price != 0:
            print("\nGross margin = " + str(round(profit / price * 100.0, 4)) +
                  " % of price")
        if cost != 0:
            print("Markup = " + str(round(profit / cost * 100.0, 4)) +
                  " % of cost")
        print("Profit per unit = " + money(profit))
    elif choice == "2":
        margin = get_float("Margin % of price = ") / 100.0
        if margin >= 1:
            print("Margin must be below 100%.")
            return
        print("\nMarkup = " + str(round(margin / (1.0 - margin) * 100.0, 4)) +
              " % of cost")
    elif choice == "3":
        markup = get_float("Markup % of cost = ") / 100.0
        if markup <= -1:
            print("Markup must be above -100%.")
            return
        print("\nMargin = " + str(round(markup / (1.0 + markup) * 100.0, 4)) +
              " % of price")
    else:
        print("Invalid choice.")


def main():
    print("=== BREAKEVN ===")
    while True:
        print("\n1. Break-even point")
        print("2. Units for target profit")
        print("3. Margin of safety & profit")
        print("4. Margin vs markup")
        print("0. Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                break_even()
            elif choice == "2":
                target_profit()
            elif choice == "3":
                margin_of_safety()
            elif choice == "4":
                margin_vs_markup()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except (ValueError, OverflowError, ZeroDivisionError):
            print("Could not compute with those values.")
    print("Bye.")


main()
