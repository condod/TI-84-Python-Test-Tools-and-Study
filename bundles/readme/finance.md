# Finance & Business Math Bundle — TI-84 Plus CE Python

5 standalone TI-84 Plus CE **Python Edition** programs that turn a TI-84 into a
financial calculator — the time-value-of-money and capital-budgeting work that a
BA II Plus normally gets bought for.

## What's Included

| File | What it does |
|---|---|
| `tvm_solver.py` | The standard five-variable time-value-of-money solver: give any four of PV, FV, PMT, N and rate and it finds the fifth, with end-of-period (ordinary annuity) or begin-of-period (annuity due) payments. The rate is found by bisection, which cannot diverge the way Newton's method can on an awkward cash flow, and zero-rate cases are handled by their limits. A 200,000 loan at 0.5%/month over 360 months returns the textbook 1,199.10 payment. |
| `loan_amortization.py` | Level payment from amount, rate, term and payments per year, then a full payment-by-payment schedule (paused every 12 rows), a year-by-year summary, or totals only. Shows how paying extra shortens the loan, and says so when a payment does not cover the first month's interest instead of looping forever. |
| `compound_interest.py` | Future value at any compounding frequency including continuous, the interest earned, the effective annual rate, APR ↔ APY conversion, and a head-to-head comparison of two accounts ranked honestly by APY. |
| `npv_irr.py` | NPV at your discount rate with an accept/reject reading, IRR by bisection, simple and discounted payback interpolated within the crossing period, and the profitability index — for up to 40 cash flows. Counts sign changes and warns when multiple IRRs may exist, or says plainly when there is no IRR at all. Optional NPV-vs-rate table from 0% to 30%. |
| `break_even_margin.py` | Break-even in units and revenue, contribution margin and its ratio, the volume needed to hit a target profit, margin of safety against expected sales, and margin ↔ markup conversion in both directions. Explains when no volume ever breaks even rather than returning a negative quantity. |

**Course fit:** Personal Finance, Business Math, Finance 101, Corporate Finance,
Accounting, Economics, and Engineering Economics.

<!-- SHARED: DOWNLOAD-CONTENTS -->

<!-- PROGRAM-NAME-TABLE -->

<!-- SHARED: COMPATIBILITY -->

<!-- SHARED: INSTALL -->

<!-- SHARED: PRESS-TO-TEST -->

<!-- SHARED: EXAM-POLICY -->

<!-- SHARED: TRADEMARK -->
