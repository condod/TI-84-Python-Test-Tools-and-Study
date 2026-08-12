# On-calc name: NPVIRR
# Program: npv_irr
# Purpose: Capital-budgeting tools for a stream of cash flows: net
#          present value (NPV) at a chosen discount rate, internal rate
#          of return (IRR, the rate that makes NPV zero), discounted
#          and simple payback periods, and the profitability index.
# Usage: Enter the cash flow at time 0 first (an investment is
#        negative), then each later period's cash flow, blank to
#        finish (max 40 flows). Rates are entered as percents. IRR is
#        found by bisection, so it reports the single sign-change root;
#        a stream that changes sign more than once can have several
#        IRRs and the program warns when it sees that.

MAX_FLOWS = 40


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


def read_flows():
    print("\nEnter cash flows. Time 0 first (investment negative).")
    print("Blank line to finish (max " + str(MAX_FLOWS) + ").")
    flows = []
    while len(flows) < MAX_FLOWS:
        raw = input("CF" + str(len(flows)) + " = ").strip()
        if raw == "":
            break
        try:
            flows.append(float(raw))
        except (ValueError, TypeError):
            print("Please enter a valid number.")
    return flows


def npv(rate, flows):
    total = 0.0
    for t in range(len(flows)):
        total += flows[t] / (1.0 + rate) ** t
    return total


def sign_changes(flows):
    changes = 0
    last = 0
    for value in flows:
        if value > 0:
            current = 1
        elif value < 0:
            current = -1
        else:
            current = 0
        if current != 0 and last != 0 and current != last:
            changes += 1
        if current != 0:
            last = current
    return changes


def irr(flows):
    # Bisection between -99.99% and a rate high enough to flip the sign.
    lo = -0.9999
    hi = 1.0
    f_lo = npv(lo, flows)
    f_hi = npv(hi, flows)
    tries = 0
    while f_lo * f_hi > 0 and tries < 20:
        hi = hi * 2.0
        f_hi = npv(hi, flows)
        tries += 1
    if f_lo * f_hi > 0:
        return None
    for _ in range(100):
        mid = (lo + hi) / 2.0
        f_mid = npv(mid, flows)
        if f_lo * f_mid <= 0:
            hi = mid
            f_hi = f_mid
        else:
            lo = mid
            f_lo = f_mid
    return (lo + hi) / 2.0


def payback(flows, rate):
    # Period at which the running (discounted) total first turns positive,
    # interpolated inside the period that crosses zero.
    running = 0.0
    for t in range(len(flows)):
        step = flows[t] / (1.0 + rate) ** t
        if running + step >= 0 and step != 0 and t > 0:
            return t - 1 + (-running) / step
        running += step
    return None


def show_results(flows, rate):
    value = npv(rate, flows)
    print("\nNPV at " + str(round(rate * 100.0, 4)) + "% = " + money(value))
    if value > 0:
        print("Positive NPV: accept at this rate.")
    elif value < 0:
        print("Negative NPV: reject at this rate.")
    else:
        print("NPV is exactly zero: this rate is the IRR.")

    changes = sign_changes(flows)
    rate_irr = irr(flows)
    if rate_irr is None:
        print("IRR: no sign change found; IRR does not exist.")
    else:
        print("IRR = " + str(round(rate_irr * 100.0, 6)) + " %")
        if changes > 1:
            print("Warning: " + str(changes) + " sign changes, so there may")
            print("be more than one IRR. Trust NPV over IRR here.")

    simple = payback(flows, 0.0)
    disc = payback(flows, rate)
    if simple is None:
        print("Simple payback: never repays.")
    else:
        print("Simple payback = " + str(round(simple, 4)) + " periods")
    if disc is None:
        print("Discounted payback: never repays.")
    else:
        print("Discounted payback = " + str(round(disc, 4)) + " periods")

    if flows[0] != 0:
        inflow_pv = value - flows[0]
        index = inflow_pv / abs(flows[0])
        print("Profitability index = " + str(round(index, 6)))


def npv_table(flows):
    print("\n Rate%   NPV")
    percent = 0.0
    while percent <= 30.0:
        print(pad(round(percent, 1), 8) + money(npv(percent / 100.0, flows)))
        percent += 5.0


def main():
    print("=== NPVIRR ===")
    while True:
        flows = read_flows()
        if len(flows) < 2:
            print("Enter at least two cash flows.")
            again = input("Try again? (y/n) ").strip().lower()
            if again != "y":
                break
            continue

        rate = get_float("Discount rate % = ") / 100.0
        try:
            show_results(flows, rate)
            if input("\nShow NPV vs rate table? (y/n) ").strip().lower() == "y":
                npv_table(flows)
        except (ValueError, OverflowError, ZeroDivisionError):
            print("Could not compute with those values.")

        again = input("\nAnother project? (y/n) ").strip().lower()
        if again != "y":
            break
    print("Bye.")


main()
