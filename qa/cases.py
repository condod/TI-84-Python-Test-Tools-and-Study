"""Test cases for the TI-84 program library.

Each case: label, prog (path relative to repo root), stdin keystrokes,
expect (substrings that MUST appear), reject (substrings that must NOT appear).

Expected numbers are hand-computed; the derivation is noted in a comment above
each group so the arithmetic can be re-checked without running anything.
"""

CASES = []


def case(label, prog, stdin, expect=(), reject=(), device=False,
         allow_traceback=False):
    CASES.append({"label": label, "prog": prog, "stdin": stdin,
                  "expect": list(expect), "reject": list(reject),
                  "device": device, "allow_traceback": allow_traceback})


# ---------------------------------------------------------------- calculus --
# d/dx x^3 at 2 = 12. Central difference on x^3 gives exactly 3x^2 + h^2,
# so h=0.001 -> 12.000001, h=0.01 -> 12.0001, h=0.0001 -> 12.00000001 -> 12.0
case("derivative x^3 at 2 (h-scaling exact for cubic)",
     "calculus/derivative_numeric.py", "x**3\n2\n0.001\nn\n",
     ["12.0", "12.000001", "12.0001"])
case("derivative sin at 0 -> cos(0)=1",
     "calculus/derivative_numeric.py", "sin(x)\n0\n0.001\nn\n", ["1.0"])
case("derivative rejects garbage expression then recovers",
     "calculus/derivative_numeric.py", "x**\n\nx**2\n3\n0.001\nn\n",
     ["Could not evaluate", "Please enter an expression", "6.0"])
case("derivative h=0 falls back to 0.001",
     "calculus/derivative_numeric.py", "x**2\n1\n0\nn\n",
     ["h cannot be 0", "2.0"])
case("derivative non-numeric x0 re-prompts",
     "calculus/derivative_numeric.py", "x**2\nabc\n1\n0.001\nn\n",
     ["Please enter a valid number", "2.0"])

# integral of x^2 from 0 to 3 = 9 exactly (Simpson is exact for quadratics)
case("Simpson x^2 on [0,3] = 9 exactly",
     "calculus/simpsons_rule.py", "x**2\n0\n3\n6\nn\n", ["9.0"])
# integral sin x from 0 to pi = 2
case("Simpson sin on [0,pi] = 2",
     "calculus/simpsons_rule.py",
     "sin(x)\n0\n3.141592653589793\n100\nn\n", ["2.0"])
case("Simpson odd n bumps to even",
     "calculus/simpsons_rule.py", "x**2\n0\n3\n5\nn\n",
     ["n must be even, using n = 6", "9.0"])
case("Simpson a==b gives 0",
     "calculus/simpsons_rule.py", "x**2\n2\n2\n4\nn\n", ["integral is 0"])
case("Simpson n<=0 re-prompts",
     "calculus/simpsons_rule.py", "x**2\n0\n3\n0\n6\nn\n",
     ["n must be a positive integer", "9.0"])
case("Simpson 1/x across singularity reports error, no crash",
     "calculus/simpsons_rule.py", "1/x\n-1\n1\n4\nn\n",
     ["Error evaluating"])

# sum_{k=0}^{9} 1/k! = 2.7182815255... -> 2.718282 ; e = 2.718281828
case("Taylor e^x at x=1, 10 terms -> 2.718282",
     "calculus/taylor_series.py", "3\n1\n10\nn\n",
     ["2.718282", "True value"])
# sin(pi/2) = 1
case("Taylor sin at pi/2, 8 terms -> 1.0",
     "calculus/taylor_series.py", "1\n1.5707963267948966\n8\nn\n", ["1.0"])
case("Taylor ln(1+x) rejects x <= -1",
     "calculus/taylor_series.py", "4\n-2\n5\n3\n1\n10\nn\n",
     ["requires x > -1"])
case("Taylor invalid menu choice re-prompts",
     "calculus/taylor_series.py", "9\n3\n1\n10\nn\n", ["Invalid choice"])

# sqrt(2) = 1.41421356 ; root of cos(x)-x = 0.7390851332
case("Newton x^2-2 -> 1.41421356",
     "calculus/newton_raphson.py", "x**2-2\n1\n\n\nn\n", ["1.41421356"])
case("Newton cos(x)-x -> 0.73908513",
     "calculus/newton_raphson.py", "cos(x)-x\n1\n\n\nn\n", ["0.73908513"])
case("Newton flags zero derivative at x0=0 for x^2",
     "calculus/newton_raphson.py", "x**2\n0\n\n\nn\n", ["Derivative is 0"])

# lim (x^2-4)/(x-2) as x->2 is 4 ; lim sin(x)/x as x->0 is 1
case("limit (x^2-4)/(x-2) at 2 -> 4",
     "calculus/limit_evaluator.py", "(x**2-4)/(x-2)\n2\nn\n",
     ["Estimated limit", "4.0"])
case("limit sin(x)/x at 0 -> 1",
     "calculus/limit_evaluator.py", "sin(x)/x\n0\nn\n",
     ["Estimated limit", "1.0"])
case("limit 1/x at 0 correctly reports no agreement",
     "calculus/limit_evaluator.py", "1/x\n0\nn\n",
     ["do not clearly agree"])
case("limit of undefined expression does not crash",
     "calculus/limit_evaluator.py", "log(x)\n-5\nn\n", ["undefined"])

# ------------------------------------------------- differential equations --
# y' = y, y(0)=1, h=0.1 to x=1: Euler -> 1.1^10 = 2.5937424601
# Improved Euler -> (1+h+h^2/2)^10 = 1.105^10 = 2.7140808...
case("Euler y'=y to x=1 -> 2.593742",
     "differential_equations/ode_solver_euler.py", "y\n0\n1\n1\n0.1\n1\nn\n",
     ["2.593742"])
case("Improved Euler y'=y to x=1 -> 2.714081",
     "differential_equations/ode_solver_euler.py", "y\n0\n1\n1\n0.1\n2\nn\n",
     ["2.71408"])
case("ODE target == x0 needs no steps",
     "differential_equations/ode_solver_euler.py", "y\n0\n1\n0\n0.1\n1\nn\n",
     ["no steps needed"])
case("ODE backward integration works",
     "differential_equations/ode_solver_euler.py", "y\n0\n1\n-1\n0.1\n1\nn\n",
     ["Approximate y(-1.0)"])
case("ODE negative h falls back to 0.1",
     "differential_equations/ode_solver_euler.py", "y\n0\n1\n1\n-5\n1\nn\n",
     ["Step size must be positive"])

# ------------------------------------------------ algebra / linear / stats --
# x^2-3x+2 -> roots 2 and 1 ; x^2+2x+1 -> -1 twice ; x^2+2x+5 -> -1 +/- 2i
case("quadratic two real roots 2 and 1",
     "algebra_linear_stats/quadratic_solver.py", "1\n-3\n2\nn\n",
     ["x1 = 2.0", "x2 = 1.0", "Two distinct real roots"])
case("quadratic repeated root -1",
     "algebra_linear_stats/quadratic_solver.py", "1\n2\n1\nn\n",
     ["One repeated real root", "x = -1.0"])
case("quadratic complex pair -1 +/- 2i",
     "algebra_linear_stats/quadratic_solver.py", "1\n2\n5\nn\n",
     ["-1.0 + 2.0i", "-1.0 - 2.0i"])
case("quadratic rejects a=0",
     "algebra_linear_stats/quadratic_solver.py", "0\n1\n-3\n2\nn\n",
     ["a cannot be 0"])
case("quadratic re-prompts on garbage",
     "algebra_linear_stats/quadratic_solver.py", "abc\n1\n-3\n2\nn\n",
     ["Please enter a valid number", "x1 = 2.0"])

# vertex (1,-4) through (3,0): a = (0-(-4))/(3-1)^2 = 1
# -> y = (x-1)^2 - 4 = x^2 - 2x - 3 ; x-int -1 and 3 ; y-int -3
case("vertex analyzer (1,-4) through (3,0)",
     "algebra_linear_stats/quadratic_vertex_analyzer.py",
     "1\n-4\n3\n0\n\n\n\n\n0\n",
     ["y=(x-1)^2 - 4", "y=x^2 - 2x - 3", "(-1,0)", "(3,0)", "(0,-3)",
      "Minimum y=-4"])
case("vertex analyzer rejects point with same x as vertex",
     "algebra_linear_stats/quadratic_vertex_analyzer.py",
     "1\n-4\n1\n0\n0\n",
     ["INPUT ERROR", "Point x must differ from vertex x"])
case("vertex analyzer downward parabola range",
     "algebra_linear_stats/quadratic_vertex_analyzer.py",
     "0\n4\n2\n0\n\n\n\n\n0\n", ["Maximum y=4", "y <= 4"])

# x+y=3, x-y=1 -> (2,1) ; classic 3x3 -> (2,3,-1)
case("2x2 system -> x=2 y=1",
     "algebra_linear_stats/linear_system_solver.py",
     "2\n1\n1\n3\n1\n-1\n1\nn\n", ["x = 2.0", "y = 1.0"])
case("3x3 system -> x=2 y=3 z=-1",
     "algebra_linear_stats/linear_system_solver.py",
     "3\n2\n1\n-1\n8\n-3\n-1\n2\n-11\n-2\n1\n2\n-3\nn\n",
     ["x = 2.0", "y = 3.0", "z = -1.0"])
case("singular system reported, not crashed",
     "algebra_linear_stats/linear_system_solver.py",
     "2\n1\n1\n1\n2\n2\n2\nn\n", ["no unique solution"])
case("system size validation",
     "algebra_linear_stats/linear_system_solver.py",
     "7\n2\n1\n1\n3\n1\n-1\n1\nn\n", ["Please enter 2 or 3"])

# det[[1,2],[3,4]] = -2 ; inv[[4,7],[2,6]] = [[0.6,-0.7],[-0.2,0.4]]
# det[[6,1,1],[4,-2,5],[2,8,7]] = -306
case("2x2 determinant = -2",
     "algebra_linear_stats/matrix_toolkit.py", "3\n2\n1\n2\n3\n4\n5\n",
     ["Determinant = -2.0"])
case("3x3 determinant = -306",
     "algebra_linear_stats/matrix_toolkit.py",
     "3\n3\n6\n1\n1\n4\n-2\n5\n2\n8\n7\n5\n", ["Determinant = -306.0"])
case("2x2 inverse",
     "algebra_linear_stats/matrix_toolkit.py", "4\n2\n4\n7\n2\n6\n5\n",
     ["0.6", "-0.7", "-0.2", "0.4"])
case("singular matrix inverse reported",
     "algebra_linear_stats/matrix_toolkit.py", "4\n2\n1\n2\n2\n4\n5\n",
     ["singular"])
case("matrix multiply by identity",
     "algebra_linear_stats/matrix_toolkit.py",
     "2\n2\n1\n2\n3\n4\n1\n0\n0\n1\n5\n", ["1.0, 2.0", "3.0, 4.0"])
# inverse of [[2,0,0],[0,4,0],[0,0,5]] = diag(0.5,0.25,0.2)
case("3x3 diagonal inverse",
     "algebra_linear_stats/matrix_toolkit.py",
     "4\n3\n2\n0\n0\n0\n4\n0\n0\n0\n5\n5\n", ["0.5", "0.25", "0.2"])

# 2,4,4,4,5,5,7,9 : mean 5, median 4.5, mode 4, pop var 4, sample var 32/7
case("descriptive stats classic data set",
     "algebra_linear_stats/descriptive_stats.py", "2,4,4,4,5,5,7,9\nn\n",
     ["Mean = 5.0", "Median = 4.5", "Population variance (n) = 4.0",
      "Population std dev (n) = 2.0", "4.571429", "2.13809"])
case("descriptive stats single value",
     "algebra_linear_stats/descriptive_stats.py", "5\n\nn\n",
     ["n = 1", "Mean = 5.0", "Population variance (n) = 0.0"])
case("descriptive stats rejects garbage list",
     "algebra_linear_stats/descriptive_stats.py", "a,b\n2,4\nn\n",
     ["Could not parse", "Mean = 3.0"])
case("descriptive stats all-unique -> no mode",
     "algebra_linear_stats/descriptive_stats.py", "1,2,3\nn\n",
     ["Mode = none"])

# 5P2=20, 5C2=10, C(10,3)*0.5^10 = 120/1024 = 0.1171875
case("nPr / nCr / binomial",
     "algebra_linear_stats/combinatorics_probability.py",
     "1\n5\n2\n2\n5\n2\n3\n10\n3\n0.5\n4\n",
     ["nPr = 20", "nCr = 10", "0.117188"])
case("combinatorics rejects r > n",
     "algebra_linear_stats/combinatorics_probability.py", "2\n3\n5\n4\n",
     ["r cannot be greater than n"])
case("combinatorics rejects p outside 0..1",
     "algebra_linear_stats/combinatorics_probability.py",
     "3\n10\n3\n5\n0.5\n4\n", ["Probability must be between 0 and 1"])
# C(52,5) = 2598960 - large-n check (no factorial blowup allowed)
case("nCr(52,5) = 2598960",
     "algebra_linear_stats/combinatorics_probability.py", "2\n52\n5\n4\n",
     ["2598960"])

# ------------------------------------------------------ physics/engineering --
# v = 0 + 9.81*2 = 19.62 ; d = 0*2 + 0.5*9.81*4 = 19.62
# v^2 = v0^2 + 2ad = 2*9.81*19.62 = 384.9444 -> v = 19.62
case("kinematics solve v from v0,a,t",
     "physics_engineering/kinematics_solver.py", "2\n0\n9.81\n2\n\nn\n",
     ["19.62"])
# the solver asks for every other variable and uses one named formula per
# branch, so unused values are entered as 0 rather than left blank
case("kinematics solve d from v0,v,a,t",
     "physics_engineering/kinematics_solver.py", "5\n0\n19.62\n9.81\n2\n0\n",
     ["d = 19.62"])
case("kinematics solve v0 from v,a,t",
     "physics_engineering/kinematics_solver.py", "1\n19.62\n9.81\n2\n0\n0\n",
     ["v0 = 0.0"])
case("kinematics solve a from v0,v,t",
     "physics_engineering/kinematics_solver.py", "3\n0\n19.62\n2\n\nn\n",
     ["9.81"])
case("kinematics solve t from v0,v,a",
     "physics_engineering/kinematics_solver.py", "4\n0\n19.62\n9.81\n\nn\n",
     ["2.0"])
# a = 0 and v0 + v = 0 leaves no equation for t
case("kinematics reports when knowns are insufficient",
     "physics_engineering/kinematics_solver.py", "4\n0\n0\n0\n5\n0\n",
     ["Not enough information"])

# v0=20 at 45 deg: t = 2*v0*sin45/g = 2.883129 ; R = v0^2/g = 40.774719
# H = (v0 sin45)^2/(2g) = 200/19.62 = 10.193680
case("projectile 20 m/s at 45 deg",
     "physics_engineering/projectile_motion.py", "20\n45\n0\nn\n",
     ["2.883", "40.774", "10.193"])
# straight up: v0=10, 90 deg -> t = 2*10/9.81 = 2.038736, H = 100/19.62 = 5.09684
case("projectile straight up (90 deg) has zero range",
     "physics_engineering/projectile_motion.py", "10\n90\n0\nn\n",
     ["2.038", "5.096"])
# horizontal from 20 m: t = sqrt(2*20/9.81) = 2.019275 ; R = 10*t = 20.19275
case("projectile horizontal launch from height 20 m",
     "physics_engineering/projectile_motion.py", "10\n0\n20\nn\n",
     ["2.019", "20.19"])
case("projectile rejects negative speed",
     "physics_engineering/projectile_motion.py", "-5\n45\n0\n20\n45\n0\nn\n",
     ["non-negative"])
case("projectile plot path runs with ti_plotlib present",
     "physics_engineering/projectile_motion.py", "20\n45\n0\ny\nn\n",
     ["ti_plotlib/ti_system calls"], device=True)

case("ohms law V = I*R = 10",
     "physics_engineering/ohms_law_circuits.py", "1\n1\n2\n5\n3\n", ["10.0"])
case("ohms law rejects R=0",
     "physics_engineering/ohms_law_circuits.py", "1\n2\n10\n0\n3\n",
     ["R cannot be 0"])
case("two 10 ohm resistors in parallel = 5",
     "physics_engineering/ohms_law_circuits.py", "2\n2\n10\n10\n\n3\n",
     ["5.0"])
case("resistors in series 10+20+30 = 60",
     "physics_engineering/ohms_law_circuits.py", "2\n1\n10\n20\n30\n\n3\n",
     ["60.0"])
case("resistor combiner rejects non-positive resistance",
     "physics_engineering/ohms_law_circuits.py", "2\n1\n-5\n10\n\n3\n",
     ["must be positive", "10.0"])

# R=10, L=0.1 H, C=1 uF, f=1000 Hz:
# XL = 2*pi*1000*0.1 = 628.318531 ; XC = 1/(2*pi*1000*1e-6) = 159.154943
# X = 469.163588 ; |Z| = sqrt(100 + 220114.5) = 469.270...
# phase = atan2(469.163588,10) = 88.7788 deg ; f0 = 1/(2*pi*sqrt(1e-7)) = 503.292
case("series RLC at 1 kHz",
     "physics_engineering/rlc_impedance.py", "10\n0.1\n0.000001\n1000\nn\n",
     ["628.318531", "159.154943", "469.27", "88.77", "503.29"])
case("RLC at f=0 handled",
     "physics_engineering/rlc_impedance.py", "10\n0.1\n0.000001\n0\nn\n",
     ["f = 0 Hz"])
case("RLC rejects C<=0",
     "physics_engineering/rlc_impedance.py",
     "10\n0.1\n0\n1000\n10\n0.1\n0.000001\n1000\nn\n", ["C must be > 0"])
# at resonance f=f0 the reactances cancel and |Z| = R
case("RLC at resonance gives |Z| = R",
     "physics_engineering/rlc_impedance.py",
     "10\n0.1\n0.000001\n503.2921210448704\nn\n", ["|Z| = 10.0"])

# 3 at 0 deg + 4 at 90 deg -> magnitude 5, angle atan(4/3) = 53.130102 deg
case("force resultant 3@0 + 4@90 = 5 at 53.13 deg",
     "physics_engineering/statics_vectors.py", "1\n3\n0\n4\n90\n\n3\n",
     ["5.0", "53.13"])
# r=(2,0), F=(0,10) -> torque = 2*10 - 0*0 = 20 (counterclockwise)
case("torque r=(2,0) F=(0,10) = 20 CCW",
     "physics_engineering/statics_vectors.py", "2\n2\n0\n0\n10\n\n3\n",
     ["20.0", "counterclockwise"])
# equal and opposite forces cancel
case("opposing forces cancel to zero resultant",
     "physics_engineering/statics_vectors.py", "1\n5\n0\n5\n180\n\n3\n",
     ["Resultant magnitude = 0.0"])
case("statics handles no forces entered",
     "physics_engineering/statics_vectors.py", "1\n\n3\n", ["No forces"])

# A=(1,2,3) B=(4,5,6): dot=32 ; cross=(-3,6,-3) ; |A|=3.741657
# angle = acos(32/(sqrt14*sqrt77)) = 12.933154 deg
# scalar proj of A on B = 32/sqrt(77) = 3.646738
case("3D dot product = 32",
     "physics_engineering/vector3d_toolkit.py", "1\n1\n2\n3\n4\n5\n6\n6\n",
     ["32.0"])
case("3D cross product = (-3,6,-3)",
     "physics_engineering/vector3d_toolkit.py", "2\n1\n2\n3\n4\n5\n6\n6\n",
     ["(-3.0, 6.0, -3.0)"])
case("3D magnitude sqrt(14)",
     "physics_engineering/vector3d_toolkit.py", "3\n1\n2\n3\n6\n", ["3.741657"])
case("3D angle between = 12.9332 deg",
     "physics_engineering/vector3d_toolkit.py", "4\n1\n2\n3\n4\n5\n6\n6\n",
     ["12.933"])
case("3D projection scalar 3.646738",
     "physics_engineering/vector3d_toolkit.py", "5\n1\n2\n3\n4\n5\n6\n6\n",
     ["3.646738"])
case("3D angle with zero vector handled",
     "physics_engineering/vector3d_toolkit.py", "4\n0\n0\n0\n1\n1\n1\n6\n",
     ["zero vector"])
# parallel vectors -> 0 degrees, and clamping must not blow up acos
case("3D angle of parallel vectors = 0 deg (acos clamp)",
     "physics_engineering/vector3d_toolkit.py", "4\n1\n1\n1\n2\n2\n2\n6\n",
     ["= 0.0 degrees"])

# ----------------------------------------------- chemistry & exam tools --
# P = nRT/V = 1*8.314*273.15/22.414 = 101.319225 kPa
case("ideal gas P at STP-ish = 101.319 kPa",
     "chemistry_and_exam_tools/ideal_gas_law.py",
     "1\n1\n22.414\n1\n273.15\n3\n", ["101.319"])
# n = PV/RT = 101.325*22.414/(8.314*273.15) = 1.0000
case("ideal gas n = 1 mol",
     "chemistry_and_exam_tools/ideal_gas_law.py",
     "1\n3\n101.325\n22.414\n273.15\n3\n", ["1.0"])
case("ideal gas rejects V=0",
     "chemistry_and_exam_tools/ideal_gas_law.py",
     "1\n1\n0\n1\n273.15\n3\n", ["V cannot be 0"])
# P1V1/T1 = P2V2/T2 -> V2 = 100*1*600/(300*200) = 1.0
case("combined gas law solves V2 = 1.0",
     "chemistry_and_exam_tools/ideal_gas_law.py",
     "2\n100\n1\n300\n200\n\n600\n3\n", ["V2 = 1.0"])
case("combined gas law rejects two blanks",
     "chemistry_and_exam_tools/ideal_gas_law.py",
     "2\n100\n1\n\n\n100\n1\n300\n200\n\n600\n3\n",
     ["Only one value can be blank"])

# CH4 = 12.011 + 4*1.008 = 16.043 g/mol ; 32.086 g / 16.043 = 2.0 mol
case("molar mass of CH4 = 16.043",
     "chemistry_and_exam_tools/stoichiometry_molar_mass.py",
     "1\nC\n1\nH\n4\n\nn\n3\n", ["16.043"])
case("mass to moles using computed molar mass",
     "chemistry_and_exam_tools/stoichiometry_molar_mass.py",
     "1\nC\n1\nH\n4\n\ny\ny\n1\n32.086\n3\n", ["2.0"])
# H2SO4 = 2*1.008 + 32.06 + 4*15.999 = 98.072
case("molar mass of H2SO4 = 98.072",
     "chemistry_and_exam_tools/stoichiometry_molar_mass.py",
     "1\nH\n2\nS\n1\nO\n4\n\nn\n3\n", ["98.072"])
case("unknown element symbol rejected",
     "chemistry_and_exam_tools/stoichiometry_molar_mass.py",
     "1\nXX\nC\n1\n\nn\n3\n", ["Unknown element symbol"])

# 100 C = 212 F ; 1 mile = 5280 ft ; 1 atm = 101.325 kPa
case("temperature 100 C -> 212 F",
     "chemistry_and_exam_tools/unit_converter.py", "5\n1\n2\n100\n6\n",
     ["212.0"])
case("temperature -40 C -> -40 F",
     "chemistry_and_exam_tools/unit_converter.py", "5\n1\n2\n-40\n6\n",
     ["-40.0"])
case("length 1 mi -> 5280 ft",
     "chemistry_and_exam_tools/unit_converter.py", "1\n7\n5\n1\n6\n",
     ["5280.0"])
case("pressure 1 atm -> 101.325 kPa",
     "chemistry_and_exam_tools/unit_converter.py", "3\n3\n2\n1\n6\n",
     ["101.325"])
case("unit converter invalid category",
     "chemistry_and_exam_tools/unit_converter.py", "9\n6\n", ["Invalid choice"])

case("flashcards run and score",
     "chemistry_and_exam_tools/formula_flashcards.py", "1\n2\n\ny\n\nn\nn\n",
     ["Score: 1/2"])
case("flashcards validates question count",
     "chemistry_and_exam_tools/formula_flashcards.py",
     "1\n99\n1\n\ny\nn\n", ["Enter a number between"])

case("countdown timer completes",
     "chemistry_and_exam_tools/exam_countdown_drill.py", "1\n0.05\n3\n",
     ["Time's up!"])
case("countdown rejects non-positive minutes",
     "chemistry_and_exam_tools/exam_countdown_drill.py", "1\n-1\n3\n",
     ["positive number of minutes"])
case("drill generator runs and scores",
     "chemistry_and_exam_tools/exam_countdown_drill.py", "2\n1\n2\n0\n0\n3\n",
     ["Score:"])

# [H+] = 1e-3 -> pH 3, pOH 11, [OH-] = 1e-11
case("pH from [H+] = 0.001 -> pH 3",
     "chemistry_and_exam_tools/acid_base_calculator.py", "1\n1\n0.001\n4\n",
     ["pH  = 3.0", "pOH = 11.0", "acidic"])
# [OH-] = 1e-3 -> pOH 3, pH 11 (basic)
case("pOH from [OH-] = 0.001 -> pH 11",
     "chemistry_and_exam_tools/acid_base_calculator.py", "1\n2\n0.001\n4\n",
     ["pH  = 11.0", "pOH = 3.0", "basic"])
case("[H+] from pH 3 = 0.001",
     "chemistry_and_exam_tools/acid_base_calculator.py", "2\n1\n3\n4\n",
     ["0.001"])
# Henderson-Hasselbalch with equal concentrations -> pH = pKa
case("buffer pH = pKa when [A-] = [HA]",
     "chemistry_and_exam_tools/acid_base_calculator.py",
     "3\n4.76\n0.1\n0.1\n4\n", ["4.76"])
# pH = 4.76 + log10(0.2/0.1) = 4.76 + 0.30103 = 5.06103
case("buffer pH with 2:1 ratio = 5.061",
     "chemistry_and_exam_tools/acid_base_calculator.py",
     "3\n4.76\n0.2\n0.1\n4\n", ["5.061"])
case("acid/base rejects non-positive concentration",
     "chemistry_and_exam_tools/acid_base_calculator.py", "1\n1\n-1\n4\n",
     ["must be a positive number"])
case("acid/base survives absurd pH input",
     "chemistry_and_exam_tools/acid_base_calculator.py", "2\n1\n-400\n4\n",
     [])


# The whole library was normalized so that every program sits in a loop that
# ends with a "0. Quit" choice. These scripts were written against the earlier
# "Again? (y/n)" convention, so a trailing "n" now lands on a menu prompt and
# the program loops instead of exiting. Swapping that last "n" for "0" quits,
# and the extra "0"s cover programs that nest one menu inside another.
QUIT_SUFFIX = "0\n" * 3

for _case in CASES:
    stdin = _case["stdin"]
    if stdin.endswith("n\n"):
        stdin = stdin[:-2] + "0\n"
    _case["stdin"] = stdin + QUIT_SUFFIX
