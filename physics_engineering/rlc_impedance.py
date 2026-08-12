# On-calc name: RLC
# Program: rlc_impedance
# Purpose: Compute the impedance magnitude and phase angle of a
#          series RLC circuit at a given frequency, and compute the
#          resonant frequency of an LC combination. Uses plain real
#          arithmetic (no complex/cmath needed): Z = R + j(XL-XC).
# Usage: Enter R (ohms), L (henries), C (farads), and frequency f (Hz).
#        Prints XL, XC, impedance magnitude |Z|, phase angle, and the
#        resonant frequency f0 = 1/(2*pi*sqrt(L*C)).

from math import pi, sqrt, atan2, degrees


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def main():
    print("=== RLC ===")
    while True:
        r = get_float("Resistance R (ohms) = ")
        l = get_float("Inductance L (henries) = ")
        c = get_float("Capacitance C (farads) = ")
        f = get_float("Frequency f (Hz) = ")

        if r < 0 or l < 0 or c <= 0 or f < 0:
            print("R,L must be >= 0, C must be > 0, f must be >= 0. Try again.")
            continue

        omega = 2 * pi * f
        xl = omega * l
        xc = (1.0 / (omega * c)) if omega > 0 else float("inf")

        x_net = xl - xc
        z_mag = sqrt(r * r + x_net * x_net) if xc != float("inf") else float("inf")
        phase = degrees(atan2(x_net, r)) if z_mag != float("inf") else None

        print("\nX_L (inductive reactance) = " + str(round(xl, 6)) + " ohms")
        if xc == float("inf"):
            print("X_C (capacitive reactance) = infinite (f = 0 Hz)")
            print("Impedance magnitude and phase undefined at f = 0 Hz.")
        else:
            print("X_C (capacitive reactance) = " + str(round(xc, 6)) + " ohms")
            print("|Z| = " + str(round(z_mag, 6)) + " ohms")
            print("Phase angle (V leads I by) = " + str(round(phase, 4)) + " degrees")

        f0 = 1.0 / (2 * pi * sqrt(l * c)) if l > 0 else None
        if f0 is not None:
            print("Resonant frequency f0 = 1/(2*pi*sqrt(LC)) = " + str(round(f0, 6)) + " Hz")
        else:
            print("Resonant frequency undefined (L = 0).")

        print("\n1. Again  0. Quit")
        if input("> ").strip() == "0":
            break
    print("Bye.")


main()
