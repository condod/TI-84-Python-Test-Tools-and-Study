# On-calc name: GASPROC
# Program: ideal_gas_processes
# Purpose: Work, heat, and internal-energy change for the four standard
#          ideal-gas processes: isothermal (constant T), isobaric
#          (constant P), isochoric (constant V), and adiabatic (Q = 0).
#          Reports the missing state variables as well, so a P-V
#          diagram problem can be worked end to end.
# Usage: Pick a process and enter the state values it asks for. Use SI
#        units throughout: pressure in Pa, volume in m^3, temperature
#        in K, and n in mol; work and heat then come out in joules.
#        The sign convention is work done BY the gas is positive, and
#        the first law is dU = Q - W.

from math import log

R = 8.314          # J/(mol*K)
MONATOMIC_CV = 1.5 * R
DIATOMIC_CV = 2.5 * R


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


def get_cv():
    print("\nMolar heat capacity at constant volume Cv:")
    print("1. Monatomic gas (3/2 R = 12.471)")
    print("2. Diatomic gas (5/2 R = 20.785)")
    print("3. Enter my own Cv")
    choice = input("> ").strip()
    if choice == "1":
        return MONATOMIC_CV
    if choice == "2":
        return DIATOMIC_CV
    return get_positive("Cv in J/(mol*K) = ")


def report(work, heat, delta_u):
    print("\nW (by the gas) = " + str(round(work, 4)) + " J")
    print("Q (into the gas) = " + str(round(heat, 4)) + " J")
    print("dU = Q - W = " + str(round(delta_u, 4)) + " J")
    if work > 0:
        print("The gas expanded and did work on its surroundings.")
    elif work < 0:
        print("The surroundings did work compressing the gas.")
    else:
        print("No work was done (volume did not change).")


def isothermal():
    print("\nIsothermal: T constant, dU = 0, so Q = W.")
    n = get_positive("Moles n = ")
    temperature = get_positive("Temperature T (K) = ")
    v1 = get_positive("Initial volume V1 (m^3) = ")
    v2 = get_positive("Final volume V2 (m^3) = ")

    work = n * R * temperature * log(v2 / v1)
    print("\nW = n*R*T*ln(V2/V1)")
    report(work, work, 0.0)
    print("\nP1 = " + str(round(n * R * temperature / v1, 4)) + " Pa")
    print("P2 = " + str(round(n * R * temperature / v2, 4)) + " Pa")


def isobaric():
    print("\nIsobaric: P constant, W = P*(V2-V1).")
    pressure = get_positive("Pressure P (Pa) = ")
    v1 = get_positive("Initial volume V1 (m^3) = ")
    v2 = get_positive("Final volume V2 (m^3) = ")
    n = get_positive("Moles n = ")
    cv = get_cv()

    work = pressure * (v2 - v1)
    t1 = pressure * v1 / (n * R)
    t2 = pressure * v2 / (n * R)
    delta_u = n * cv * (t2 - t1)
    heat = delta_u + work

    print("\nW = P*(V2 - V1)")
    report(work, heat, delta_u)
    print("\nT1 = " + str(round(t1, 4)) + " K")
    print("T2 = " + str(round(t2, 4)) + " K")
    print("Cp = Cv + R = " + str(round(cv + R, 4)) + " J/(mol*K)")


def isochoric():
    print("\nIsochoric: V constant, so W = 0 and Q = dU.")
    volume = get_positive("Volume V (m^3) = ")
    t1 = get_positive("Initial temperature T1 (K) = ")
    t2 = get_positive("Final temperature T2 (K) = ")
    n = get_positive("Moles n = ")
    cv = get_cv()

    delta_u = n * cv * (t2 - t1)
    report(0.0, delta_u, delta_u)
    print("\nP1 = " + str(round(n * R * t1 / volume, 4)) + " Pa")
    print("P2 = " + str(round(n * R * t2 / volume, 4)) + " Pa")


def adiabatic():
    print("\nAdiabatic: Q = 0, P*V^gamma constant.")
    gamma = get_positive("gamma = Cp/Cv (1.67 mono, 1.4 diatomic) = ")
    if gamma <= 1:
        print("gamma must be greater than 1.")
        return
    p1 = get_positive("Initial pressure P1 (Pa) = ")
    v1 = get_positive("Initial volume V1 (m^3) = ")
    v2 = get_positive("Final volume V2 (m^3) = ")

    p2 = p1 * (v1 / v2) ** gamma
    work = (p1 * v1 - p2 * v2) / (gamma - 1.0)

    print("\nP2 = P1*(V1/V2)^gamma = " + str(round(p2, 4)) + " Pa")
    print("W = (P1*V1 - P2*V2)/(gamma - 1)")
    report(work, 0.0, -work)

    n = get_float("Moles n (0 to skip temperatures) = ")
    if n > 0:
        t1 = p1 * v1 / (n * R)
        t2 = p2 * v2 / (n * R)
        print("\nT1 = " + str(round(t1, 4)) + " K")
        print("T2 = " + str(round(t2, 4)) + " K")
        print("(T*V^(gamma-1) is constant for this process.)")


def state_solver():
    print("\nIdeal gas law PV = nRT; leave the unknown blank.")
    print("1. Solve P")
    print("2. Solve V")
    print("3. Solve n")
    print("4. Solve T")
    choice = input("> ").strip()
    if choice == "1":
        v = get_positive("V (m^3) = ")
        n = get_positive("n (mol) = ")
        t = get_positive("T (K) = ")
        print("\nP = " + str(round(n * R * t / v, 4)) + " Pa")
    elif choice == "2":
        p = get_positive("P (Pa) = ")
        n = get_positive("n (mol) = ")
        t = get_positive("T (K) = ")
        print("\nV = " + str(round(n * R * t / p, 8)) + " m^3")
    elif choice == "3":
        p = get_positive("P (Pa) = ")
        v = get_positive("V (m^3) = ")
        t = get_positive("T (K) = ")
        print("\nn = " + str(round(p * v / (R * t), 6)) + " mol")
    elif choice == "4":
        p = get_positive("P (Pa) = ")
        v = get_positive("V (m^3) = ")
        n = get_positive("n (mol) = ")
        print("\nT = " + str(round(p * v / (n * R), 4)) + " K")
    else:
        print("Invalid choice.")


def main():
    print("=== GASPROC ===")
    print("SI units: Pa, m^3, K, mol, J.")
    while True:
        print("\n1. Isothermal (T constant)")
        print("2. Isobaric (P constant)")
        print("3. Isochoric (V constant)")
        print("4. Adiabatic (Q = 0)")
        print("5. Ideal gas state solver")
        print("0. Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                isothermal()
            elif choice == "2":
                isobaric()
            elif choice == "3":
                isochoric()
            elif choice == "4":
                adiabatic()
            elif choice == "5":
                state_solver()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except (ValueError, OverflowError, ZeroDivisionError):
            print("Could not compute with those values.")
    print("Bye.")


main()
