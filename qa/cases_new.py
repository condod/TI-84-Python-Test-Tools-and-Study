"""Test cases for the programs added in the finance / biology / precalculus /
trigonometry / thermo_materials expansion.

Every expected number below is hand-computed; the derivation is in the comment
above each group so the arithmetic can be re-checked independently of the code.
"""

CASES = []


def case(label, prog, stdin, expect=(), reject=(), device=False,
         allow_traceback=False):
    CASES.append({"label": label, "prog": prog, "stdin": stdin,
                  "expect": list(expect), "reject": list(reject),
                  "device": device, "allow_traceback": allow_traceback})


# ------------------------------------------------------------- finance --
# 200,000 loan, 0.5%/month, 360 months.
# A = (1 - 1.005^-360)/0.005 = 166.791614 ; PMT = -200000/A = -1199.10
case("TVM: mortgage payment = -1199.10",
     "finance/tvm_solver.py", "3\n200000\n0\n360\n0.5\n1\n0\n",
     ["PMT = -1199.10"])
# FV of 100/month for 120 months at 0.5%: 100*(1.005^120 - 1)/0.005 = 16387.93
case("TVM: FV of an annuity = 16387.93",
     "finance/tvm_solver.py", "2\n0\n-100\n120\n0.5\n1\n0\n",
     ["16387.9"])
# 1000 doubling to 2000 in 10 periods -> 2^(1/10) - 1 = 7.1773463%
case("TVM: rate to double in 10 periods = 7.177346%",
     "finance/tvm_solver.py", "5\n-1000\n0\n2000\n10\n1\n0\n",
     ["7.177346"])
case("TVM: periods to double at 7.1773463% = 10",
     "finance/tvm_solver.py", "4\n-1000\n0\n2000\n7.1773463\n1\n0\n",
     ["N = 10.0"])
# PV of 1000 in 10 periods at 5% = 1000/1.05^10 = 613.913254
case("TVM: PV of a lump sum = -613.91",
     "finance/tvm_solver.py", "1\n0\n1000\n10\n5\n1\n0\n", ["-613.91"])
# zero-rate edge: 1200 over 12 periods is just 100 a period
case("TVM: zero interest splits evenly",
     "finance/tvm_solver.py", "3\n1200\n0\n12\n0\n1\n0\n", ["PMT = -100.00"])

# 200,000 at 6%/yr for 30 yr monthly: payment 1199.10,
# total paid 431,676 and total interest 231,676
case("LOAN: 30-year mortgage totals",
     "finance/loan_amortization.py", "200000\n6\n30\n12\nn\n3\nn\n",
     ["Scheduled payment = 1199.10", "Payments made = 360",
      "Total interest = 231676"])
case("LOAN: zero-interest loan has no interest",
     "finance/loan_amortization.py", "1200\n0\n1\n12\nn\n3\nn\n",
     ["Scheduled payment = 100.00", "Total interest = 0.00"])
case("LOAN: year-by-year view renders",
     "finance/loan_amortization.py", "200000\n6\n30\n12\nn\n2\n\n\n\nn\n",
     ["Yr", "Total interest = 231676"])
# 1000 at 12%/yr for 1 yr monthly: i = 0.01, payment = 10/(1-1.01^-12) = 88.85
# first payment interest = 1000*0.01 = 10.00, principal = 78.85
# total interest = 12*88.8488 - 1000 = 66.19
case("LOAN: first payment splits 10.00 / 78.85",
     "finance/loan_amortization.py", "1000\n12\n1\n12\nn\n1\nn\n",
     ["Scheduled payment = 88.85", "10.00", "78.85",
      "Total interest = 66.19"])
case("LOAN: payment below interest is rejected",
     "finance/loan_amortization.py",
     "200000\n6\n30\n12\ny\n500\n1200\n0\n1\n12\nn\n3\nn\n",
     ["never covers the interest"])

# 1000 at 5% APR compounded monthly for 10 yr:
# FV = 1000*(1+0.05/12)^120 = 1647.01 ; APY = (1+0.05/12)^12 - 1 = 5.116190%
case("INTEREST: 1000 at 5% monthly for 10 years = 1647.01",
     "finance/compound_interest.py", "1\n1000\n5\n12\n10\n0\n",
     ["1647.01", "5.11619"])
case("INTEREST: APR 5% monthly -> APY 5.11619%",
     "finance/compound_interest.py", "2\n5\n12\n0\n", ["5.11619"])
# continuous: e^0.05 - 1 = 5.127110%
case("INTEREST: APR 5% continuous -> APY 5.12711%",
     "finance/compound_interest.py", "2\n5\n0\n0\n", ["5.1271"])
case("INTEREST: APY 5.116190% monthly -> APR 5%",
     "finance/compound_interest.py", "3\n5.116190\n12\n0\n",
     ["Equivalent APR = 5.0 %"])
case("INTEREST: monthly 5% beats annual 5.1%",
     "finance/compound_interest.py", "4\n5\n12\n5.1\n1\n0\n",
     ["A is better"])

# CF -1000, 500, 500, 500 at 10%:
# NPV = -1000 + 454.545455 + 413.223140 + 375.657400 = 243.43
# IRR solves (1-(1+r)^-3)/r = 2 -> r = 23.375%
# simple payback = 2.0 ; discounted payback = 2 + 132.231/375.657 = 2.352
# profitability index = 1243.426/1000 = 1.243426
case("NPVIRR: NPV 243.43 and IRR 23.37%",
     "finance/npv_irr.py", "-1000\n500\n500\n500\n\n10\nn\nn\n",
     ["243.43", "23.37", "1.243426"])
case("NPVIRR: payback periods",
     "finance/npv_irr.py", "-1000\n500\n500\n500\n\n10\nn\nn\n",
     ["Simple payback = 2.0", "Discounted payback = 2.35"])
# discounting at the IRR must give NPV = 0
case("NPVIRR: NPV at the IRR is zero",
     "finance/npv_irr.py", "-1000\n500\n500\n500\n\n23.375\nn\nn\n",
     ["NPV at 23.375% = 0.00"])
case("NPVIRR: all-positive flows have no IRR",
     "finance/npv_irr.py", "1000\n500\n500\n\n10\nn\nn\n",
     ["no sign change"])
case("NPVIRR: rate table renders",
     "finance/npv_irr.py", "-1000\n500\n500\n500\n\n10\ny\nn\n",
     ["Rate%"])

# price 25, variable 15, fixed 10000: CM = 10, ratio 40%,
# break-even 1000 units = 25000 revenue
case("BREAKEVN: 1000 units / 25000 revenue",
     "finance/break_even_margin.py", "1\n25\n15\n10000\n0\n",
     ["1000.0", "25000.00", "40.0"])
# target profit 5000 -> (10000+5000)/10 = 1500 units
case("BREAKEVN: 1500 units for 5000 profit",
     "finance/break_even_margin.py", "2\n25\n15\n10000\n5000\n0\n",
     ["1500.0"])
# cost 80 price 100 -> margin 20% of price, markup 25% of cost
case("BREAKEVN: margin 20% vs markup 25%",
     "finance/break_even_margin.py", "4\n1\n80\n100\n0\n", ["20.0", "25.0"])
case("BREAKEVN: margin 20% converts to markup 25%",
     "finance/break_even_margin.py", "4\n2\n20\n0\n", ["25.0"])
case("BREAKEVN: no break-even when price <= variable cost",
     "finance/break_even_margin.py", "1\n10\n15\n1000\n0\n",
     ["Contribution margin = -5.00", "break-even point:"])

# ------------------------------------------------------------- biology --
# p = 0.6 -> q = 0.4, p^2 = 0.36, 2pq = 0.48, q^2 = 0.16
case("HARDYW: p=0.6 gives 0.36 / 0.48 / 0.16",
     "biology/hardy_weinberg.py", "1\n1\n0.6\n0\n0\n",
     ["0.36", "0.48", "0.16"])
# recessive phenotype 0.16 -> q = 0.4, p = 0.6
case("HARDYW: q^2=0.16 gives q=0.4",
     "biology/hardy_weinberg.py", "2\n0.16\n0\n", ["0.4", "0.6"])
# AA=30 Aa=50 aa=20: p = (60+50)/200 = 0.55, expected 30.25/49.5/20.25
# chi = 0.0625/30.25 + 0.25/49.5 + 0.0625/20.25 = 0.010203
case("HARDYW: counts give p=0.55 and chi=0.010203",
     "biology/hardy_weinberg.py", "3\n30\n50\n20\n0\n",
     ["0.55", "30.25", "0.010203", "Fail to reject"])
case("HARDYW: rejects a frequency above 1",
     "biology/hardy_weinberg.py", "1\n1\n1.5\n0.6\n0\n0\n",
     ["between 0 and 1"])

# N = 100*e^(0.1*10) = 271.828183 ; doubling time = ln2/0.1 = 6.931472
case("POPGROW: exponential 100 -> 271.828183",
     "biology/population_growth.py", "1\n100\n0.1\n10\n0\n",
     ["271.828183", "6.931472"])
case("POPGROW: time to double = 6.931472",
     "biology/population_growth.py", "2\n100\n200\n0.1\n0\n", ["6.931472"])
# logistic N0=10 K=1000 r=0.5 t=10: A=99, e^-5=0.006737947,
# N = 1000/1.667056753 = 599.8596 ; dN/dt = 0.5*N*(1-N/K) = 120.014
# inflection at t = ln(99)/0.5 = 9.190239
case("POPGROW: logistic reaches 599.86 at t=10",
     "biology/population_growth.py", "3\n10\n1000\n0.5\n10\n0\n",
     ["599.85", "120.01", "9.19"])
case("POPGROW: logistic cannot reach K",
     "biology/population_growth.py", "4\n10\n1000\n1000\n0.5\n0\n",
     ["never attained"])
# dN/dt at N = K/2 is the maximum, r*K/4 = 0.5*1000/4 = 125
case("POPGROW: fastest growth at K/2 is 125",
     "biology/population_growth.py", "5\n500\n1000\n0.5\n0\n", ["125.0"])

# C1=5, C2=0.5, V2=100 -> V1 = 10, diluent 90, 10-fold
case("DILUTION: 5 M to 0.5 M in 100 mL needs 10 mL",
     "biology/dilution_calculator.py", "1\n2\n5\n0.5\n100\n0\n",
     ["10.0", "90.0"])
case("DILUTION: refuses to concentrate",
     "biology/dilution_calculator.py", "1\n2\n0.5\n5\n100\n0\n",
     ["more concentrated"])
# 1:10 serial dilution, 3 steps from 100 -> 10, 1, 0.1 ; 1000-fold total
case("DILUTION: 3-step 1:10 serial = 1000-fold",
     "biology/dilution_calculator.py", "3\n100\n10\n3\n0\n0\n",
     ["1000.0"])
# 0.5 M * 2 L = 1 mol ; 1 mol NaCl (58.44 g/mol) = 58.44 g
case("DILUTION: 0.5 M in 2 L needs 58.44 g NaCl",
     "biology/dilution_calculator.py", "4\n2\n0.5\n2\n58.44\n0\n",
     ["1.0", "58.44"])

# 3:1 with 74/26 of 100: expected 75/25,
# chi = 1/75 + 1/25 = 0.053333, df 1, below 3.841
case("CHISQ: 74:26 fits 3:1 (chi=0.053333)",
     "biology/chi_square_genetics.py", "1\n74\n26\nn\n",
     ["0.053333", "fail to reject"])
# Mendel's 9:3:3:1 data 315/101/108/32 of 556: chi = 0.470024, df 3
case("CHISQ: Mendel 9:3:3:1 gives chi=0.470024",
     "biology/chi_square_genetics.py", "2\n315\n101\n108\n32\nn\n",
     ["0.470024", "df = 3", "fail to reject"])
# 50:50 against 3:1: expected 75/25, chi = 625/75 + 625/25 = 33.333333
case("CHISQ: 50:50 rejects a 3:1 hypothesis",
     "biology/chi_square_genetics.py", "1\n50\n50\nn\n",
     ["33.333333", "reject"])
case("CHISQ: custom ratio accepted",
     "biology/chi_square_genetics.py", "5\n9,3,3,1\n315\n101\n108\n32\nn\n",
     ["0.470024"])
case("CHISQ: warns on small expected counts",
     "biology/chi_square_genetics.py", "1\n3\n1\nn\n",
     ["smallest expected count is 1.0", "Below 5"])

# sphere r=2: SA = 4*pi*4 = 50.265482, V = (4/3)*pi*8 = 33.510322, SA:V = 1.5
case("SAVOL: sphere r=2 ratio 1.5",
     "biology/surface_area_volume.py", "1\n2\n0\n",
     ["50.265482", "33.510322", "1.5"])
# cube s=2: SA = 24, V = 8, ratio 3.0
case("SAVOL: cube s=2 ratio 3.0",
     "biology/surface_area_volume.py", "2\n2\n0\n", ["24.0", "8.0", "3.0"])
# cylinder r=1 h=2: SA = 2pi + 4pi = 18.849556, V = 2pi = 6.283185, ratio 3.0
case("SAVOL: cylinder r=1 h=2 ratio 3.0",
     "biology/surface_area_volume.py", "3\n1\n2\n0\n",
     ["18.849556", "6.283185", "3.0"])
# Kleiber: 70 * 10^0.75 = 70 * 5.623413 = 393.638922
case("SAVOL: Kleiber BMR for 10 kg = 393.64",
     "biology/surface_area_volume.py", "6\n10\n0\n0\n", ["393.63"])
# scaling by k divides SA:V by k
case("SAVOL: doubling size halves SA:V",
     "biology/surface_area_volume.py", "5\n3\n2\n0\n", ["1.5"])

# -------------------------------------------------------- trigonometry --
# 30 deg: sin 0.5, cos 0.866025, tan 0.57735
case("UNITCIRC: 30 degrees exact values",
     "trigonometry/unit_circle_reference.py", "1\n1\n30\n0\n",
     ["sin = 0.5", "0.866025", "0.57735", "sqrt(3)/2", "Quadrant I"])
case("UNITCIRC: tan 90 is undefined, not a crash",
     "trigonometry/unit_circle_reference.py", "1\n1\n90\n0\n",
     ["tan = undefined"])
# 210 deg -> reference 30, Quadrant III
case("UNITCIRC: 210 degrees reference angle 30",
     "trigonometry/unit_circle_reference.py", "1\n1\n210\n0\n",
     ["Reference angle = 30.0", "Quadrant III"])
# 405 deg wraps to 45
case("UNITCIRC: 405 wraps to 45",
     "trigonometry/unit_circle_reference.py", "1\n1\n405\n0\n",
     ["Coterminal angle in 0-360: 45.0"])
# -45 deg wraps to 315 (Quadrant IV)
case("UNITCIRC: negative angle wraps to 315",
     "trigonometry/unit_circle_reference.py", "1\n1\n-45\n0\n",
     ["315.0", "Quadrant IV"])
# 180 deg = pi radians
case("UNITCIRC: 180 deg = 3.141593 rad",
     "trigonometry/unit_circle_reference.py", "3\n1\n180\n0\n",
     ["3.141593", "1.0 * pi"])
case("UNITCIRC: arcsin 0.5 = 30 deg",
     "trigonometry/unit_circle_reference.py", "4\n1\n0.5\n0\n", ["30.0"])
case("UNITCIRC: arcsin rejects out-of-range input",
     "trigonometry/unit_circle_reference.py", "4\n1\n2\n0\n",
     ["between -1 and 1"])
case("UNITCIRC: Pythagorean identity holds",
     "trigonometry/unit_circle_reference.py", "5\n30\n0\n",
     ["sin^2 + cos^2 = 1.0"])

# --------------------------------------------------------- precalculus --
# x^2 - 3x + 2 -> roots 1 and 2, y-intercept 2
case("POLYFUNC: x^2-3x+2 has roots 1 and 2",
     "precalculus/polynomial_analyzer.py", "1\n2\n1\n-3\n2\nn\n0\n",
     ["x = 1.0", "x = 2.0", "y-intercept = (0, 2.0)"])
# x^3 - 6x^2 + 11x - 6 -> roots 1, 2, 3
case("POLYFUNC: cubic has roots 1, 2, 3",
     "precalculus/polynomial_analyzer.py", "1\n3\n1\n-6\n11\n-6\nn\n0\n",
     ["x = 1.0", "x = 2.0", "x = 3.0",
      "As x -> -inf, y -> -inf"])
# x^2 + 1 never crosses the axis
case("POLYFUNC: x^2+1 has no real zeros",
     "precalculus/polynomial_analyzer.py", "1\n2\n1\n0\n1\nn\n0\n",
     ["none"])
# evaluation check: 2*9 - 3*3 + 2 = 11
case("POLYFUNC: evaluates f(3) = 11",
     "precalculus/polynomial_analyzer.py", "1\n2\n2\n-3\n2\ny\n3\n0\n",
     ["f(3.0) = 11.0"])
# (2x^2+3)/(x^2-1): horizontal asymptote y=2, vertical at x = -1 and 1
case("POLYFUNC: rational HA y=2, VA at -1 and 1",
     "precalculus/polynomial_analyzer.py", "2\n2\n2\n0\n3\n2\n1\n0\n-1\n0\n",
     ["y = 2.0", "x = -1.0", "x = 1.0"])
# (x^2+1)/(x-1): oblique asymptote y = x + 1, remainder 2
case("POLYFUNC: oblique asymptote y = x + 1",
     "precalculus/polynomial_analyzer.py", "2\n2\n1\n0\n1\n1\n1\n-1\n0\n",
     ["y = x + 1"])

# a1=3, d=5: a10 = 3 + 45 = 48 ; S10 = 10/2*(3+48) = 255
case("SEQSER: arithmetic a10=48, S10=255",
     "precalculus/sequences_series.py", "1\n3\n5\n10\n0\n",
     ["48.0", "255.0"])
# a3=11, a7=27 -> d = 16/4 = 4, a1 = 3
case("SEQSER: d from two terms = 4",
     "precalculus/sequences_series.py", "2\n3\n11\n7\n27\n0\n",
     ["d = 4.0", "a1 = 3.0"])
# a1=2, r=3: a5 = 162 ; S5 = 2*(1-243)/(1-3) = 242
case("SEQSER: geometric a5=162, S5=242",
     "precalculus/sequences_series.py", "4\n2\n3\n5\n0\n", ["162.0", "242.0"])
# a2=6, a4=54 -> r^2 = 9, r = 3, a1 = 2
case("SEQSER: r from two terms = 3",
     "precalculus/sequences_series.py", "5\n2\n6\n4\n54\n0\n",
     ["r = 3.0", "a1 = 2.0"])
# 1 + 1/2 + 1/4 + ... = 2
case("SEQSER: infinite geometric sum = 2",
     "precalculus/sequences_series.py", "6\n1\n0.5\n0\n", ["2.0"])
case("SEQSER: |r|>=1 diverges",
     "precalculus/sequences_series.py", "6\n1\n2\n0\n", ["diverges"])
# 1+2+3+4+5 = 15
case("SEQSER: term listing sums to 15",
     "precalculus/sequences_series.py", "8\n1\n1\n1\n5\n0\n", ["15.0"])

# log2(8) = 3 ; log2(10) = 3.321928 ; 3^4 = 81
case("LOGEXP: log base 2 of 8 = 3",
     "precalculus/log_exp_solver.py", "1\n2\n8\n0\n", ["= 3.0"])
case("LOGEXP: solve 2^x = 10 -> 3.321928",
     "precalculus/log_exp_solver.py", "2\n2\n10\n0\n", ["3.321928"])
case("LOGEXP: solve log_3(x) = 4 -> 81",
     "precalculus/log_exp_solver.py", "3\n3\n4\n0\n", ["81.0"])
case("LOGEXP: b^x = c has no solution for c <= 0",
     "precalculus/log_exp_solver.py", "2\n2\n-5\n0\n", ["no real solution"])
case("LOGEXP: base 1 rejected",
     "precalculus/log_exp_solver.py", "1\n1\n2\n8\n0\n", ["cannot be 1"])
# carbon-14: k = -ln2/5730 ; after 10000 yr, e^(-1.20968) = 0.29829
case("LOGEXP: carbon-14 after 10000 years",
     "precalculus/log_exp_solver.py", "5\n100\n2\n5730\n1\n10000\n0\n",
     ["29.8", "Half-life = 5730.0"])
# log rules: log2(4*8) = 5 = 2 + 3
case("LOGEXP: product rule checks out",
     "precalculus/log_exp_solver.py", "4\n2\n4\n8\n2\n0\n", ["5.0"])

# ---------------------------------------------------- thermo_materials --
# isothermal n=1 T=300 V1=0.01 V2=0.02:
# W = 1*8.314*300*ln2 = 2494.2*0.6931472 = 1728.85 J
# P1 = 2494.2/0.01 = 249420 Pa ; P2 = 124710 Pa
case("GASPROC: isothermal work = 1728.85 J",
     "thermo_materials/ideal_gas_processes.py", "1\n1\n300\n0.01\n0.02\n0\n",
     ["1728.8", "249420.0", "124710.0"])
# isobaric P=1e5, dV=0.001: W = 100 J ; diatomic dU = 250 J ; Q = 350 J
case("GASPROC: isobaric W=100, dU=250, Q=350",
     "thermo_materials/ideal_gas_processes.py",
     "2\n100000\n0.001\n0.002\n1\n2\n0\n",
     ["100.0", "250.0", "350.0"])
# isochoric monatomic Cv=12.471, dT=100 -> dU = Q = 1247.1 J, W = 0
case("GASPROC: isochoric does no work",
     "thermo_materials/ideal_gas_processes.py", "3\n0.01\n300\n400\n1\n1\n0\n",
     ["1247.1", "W (by the gas) = 0.0"])
# adiabatic gamma=1.4: P2 = 1e5*0.5^1.4 = 37892.91 Pa
# W = (100 - 75.785828)/0.4 = 60.535 J, Q = 0
case("GASPROC: adiabatic P2=37892.91, W=60.535",
     "thermo_materials/ideal_gas_processes.py",
     "4\n1.4\n100000\n0.001\n0.002\n0\n0\n",
     ["37892.9", "60.535", "Q (into the gas) = 0.0"])
# PV=nRT: P = 1*8.314*300/0.01 = 249420 Pa
case("GASPROC: state solver P = 249420 Pa",
     "thermo_materials/ideal_gas_processes.py", "5\n1\n0.01\n1\n300\n0\n",
     ["249420.0"])

# Th=500 Tc=300: eta = 1 - 300/500 = 0.4 ; Qh=1000 -> W=400, Qc=600
case("CARNOT: efficiency 40%, W=400, Qc=600",
     "thermo_materials/carnot_efficiency.py", "1\n500\n300\n1000\n0\n",
     ["0.4", "40.0", "400.0", "600.0"])
# actual Qh=1000 W=300 -> 30% vs Carnot 40% -> 75% of the limit
case("CARNOT: actual 30% is 75% of the limit",
     "thermo_materials/carnot_efficiency.py", "2\n1\n1000\n300\n500\n300\n0\n",
     ["700.0", "30.0", "40.0", "75.0"])
case("CARNOT: flags a cycle that beats the limit",
     "thermo_materials/carnot_efficiency.py", "2\n1\n1000\n900\n500\n300\n0\n",
     ["beats the Carnot limit"])
# refrigerator COP = Tc/(Th-Tc) = 250/50 = 5 ; heat pump = 300/50 = 6
case("CARNOT: refrigerator COP = 5",
     "thermo_materials/carnot_efficiency.py", "3\n300\n250\n0\n0\n", ["5.0"])
case("CARNOT: heat pump COP = 6",
     "thermo_materials/carnot_efficiency.py", "4\n300\n250\n0\n0\n", ["6.0"])
case("CARNOT: rejects Tc >= Th",
     "thermo_materials/carnot_efficiency.py", "1\n300\n400\n0\n",
     ["must be colder"])
case("CARNOT: rejects non-absolute temperature",
     "thermo_materials/carnot_efficiency.py", "1\n-20\n500\n300\n0\n0\n",
     ["use kelvin"])

# F=10000 N, A=1e-4 m^2 -> sigma = 1e8 Pa = 100 MPa
# L0=2 m, E=200 GPa -> dL = FL/(AE) = 0.001 m, strain 0.0005
case("STRESS: axial deformation 1 mm, stress 100 MPa",
     "thermo_materials/stress_strain.py",
     "4\n10000\n2\n1\n0.0001\n200e9\n0\n",
     ["0.001", "1.0", "0.0005", "100.0"])
case("STRESS: 100 MPa tensile from F/A",
     "thermo_materials/stress_strain.py", "1\n10000\n1\n0.0001\n0\n",
     ["100.0", "Tensile"])
# E = sigma/eps = 1e8/0.0005 = 2e11 Pa = 200 GPa
case("STRESS: modulus 200 GPa",
     "thermo_materials/stress_strain.py", "3\n100000000\n0.0005\n0\n",
     ["200.0"])
# FOS = 250 MPa / 100 MPa = 2.5
case("STRESS: factor of safety 2.5",
     "thermo_materials/stress_strain.py", "5\n250e6\n1\n100000000\n0\n",
     ["2.5", "Comfortable margin"])
# round bar d=0.01 -> A = pi*d^2/4 = 7.853982e-5 ; 1000 N -> 12.732395 MPa
case("STRESS: round-bar area from diameter",
     "thermo_materials/stress_strain.py", "1\n1000\n2\n0.01\n0\n",
     ["12.7323"])
# Poisson: nu=0.3, axial 0.001 -> lateral -0.0003
case("STRESS: Poisson lateral strain -0.0003",
     "thermo_materials/stress_strain.py", "6\n0.3\n0.001\n0\n0\n",
     ["-0.0003"])

# steel alpha=12e-6, L0=10 m, dT=50 -> dL = 0.006 m
case("EXPAND: 10 m steel over 50 C grows 6 mm",
     "thermo_materials/thermal_expansion.py", "1\n10\n1\n12e-6\n50\n0\n",
     ["0.006", "10.006", "0.0006"])
# area: dA = 2*alpha*A0*dT = 2*12e-6*1*100 = 0.0024
case("EXPAND: area expansion 0.0024",
     "thermo_materials/thermal_expansion.py", "2\n1\n1\n12e-6\n100\n0\n",
     ["0.0024"])
# volume: beta = 3*alpha = 3.6e-5 ; dV = 3.6e-5*1*100 = 0.0036
case("EXPAND: volume expansion 0.0036",
     "thermo_materials/thermal_expansion.py", "3\n1\n1\n1\n12e-6\n100\n0\n",
     ["0.0036"])
# restrained bar: sigma = E*alpha*dT = 200e9*12e-6*50 = 1.2e8 Pa = 120 MPa
case("EXPAND: thermal stress 120 MPa in compression",
     "thermo_materials/thermal_expansion.py",
     "4\n1\n12e-6\n200e9\n50\n0\n0\n", ["120.0", "COMPRESSION"])
# bimetallic: 23e-6 vs 12e-6 over 1 m and 100 C -> 0.0023 vs 0.0012
case("EXPAND: bimetallic mismatch 0.0011",
     "thermo_materials/thermal_expansion.py",
     "6\n1\n23e-6\n12e-6\n100\n0\n", ["0.0011", "toward metal 2"])
# cooling a restrained bar puts it in tension
case("EXPAND: cooling gives tension",
     "thermo_materials/thermal_expansion.py",
     "4\n1\n12e-6\n200e9\n-50\n0\n0\n", ["TENSION"])
