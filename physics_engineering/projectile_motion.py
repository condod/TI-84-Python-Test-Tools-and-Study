# Program: projectile_motion
# Purpose: Given launch speed and angle (and optional launch height),
#          compute range, max height, and time of flight for
#          projectile motion (no air resistance, g = 9.81 m/s^2).
#          Optionally sketches the trajectory using the ti_plotlib
#          module if it is available on this calculator; otherwise
#          falls back to a text summary only.
# Usage: Enter initial speed (m/s), launch angle (degrees), and
#        launch height (m, 0 for ground level). Prints range, max
#        height, and flight time. If ti_plotlib is available, offers
#        to draw the trajectory (press [clear] on the graph to return).

from math import sin, cos, radians, sqrt

G = 9.81

try:
    import ti_plotlib as plt
    HAS_PLOTLIB = True
except ImportError:
    HAS_PLOTLIB = False


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except (ValueError, TypeError):
            print("Please enter a valid number.")


def solve(v0, angle_deg, h0):
    theta = radians(angle_deg)
    vx = v0 * cos(theta)
    vy = v0 * sin(theta)

    disc = vy * vy + 2 * G * h0
    if disc < 0:
        return None
    t_flight = (vy + sqrt(disc)) / G
    if t_flight <= 0:
        return None

    x_range = vx * t_flight
    t_apex = vy / G if vy > 0 else 0.0
    if t_apex > t_flight:
        t_apex = t_flight
    max_height = h0 + vy * t_apex - 0.5 * G * t_apex * t_apex

    return {
        "vx": vx, "vy": vy, "t_flight": t_flight,
        "range": x_range, "max_height": max_height,
    }


def draw_trajectory(v0, angle_deg, h0, result):
    theta = radians(angle_deg)
    vx = v0 * cos(theta)
    vy = v0 * sin(theta)
    t_flight = result["t_flight"]

    steps = 40
    dt = t_flight / steps

    x_max = max(result["range"], 1.0)
    y_max = max(result["max_height"] * 1.2, h0 + 1.0)

    plt.cls()
    plt.window(0, x_max * 1.05, 0, y_max)
    plt.axes("on")
    plt.labels("x (m)", "y (m)", 1, 1)
    plt.pen("medium", "solid")
    plt.color(0, 0, 255)

    x0, y0 = 0.0, h0
    t = 0.0
    for _ in range(steps):
        t += dt
        x1 = vx * t
        y1 = h0 + vy * t - 0.5 * G * t * t
        if y1 < 0:
            y1 = 0.0
        plt.line(x0, y0, x1, y1, "")
        x0, y0 = x1, y1

    plt.show_plot()


def main():
    print("=== Projectile Motion Simulator ===")
    if not HAS_PLOTLIB:
        print("(ti_plotlib not found on this calculator; text output only.)")
    while True:
        v0 = get_float("Initial speed v0 (m/s) = ")
        angle = get_float("Launch angle (degrees, 0-90) = ")
        h0 = get_float("Launch height above ground (m, 0 if ground level) = ")

        if v0 < 0 or h0 < 0:
            print("Speed and height should be non-negative. Try again.")
            continue

        result = solve(v0, angle, h0)
        if result is None:
            print("No valid trajectory for those inputs (check angle/height).")
        else:
            print("\nTime of flight: " + str(round(result["t_flight"], 4)) + " s")
            print("Range: " + str(round(result["range"], 4)) + " m")
            print("Max height: " + str(round(result["max_height"], 4)) + " m")

            if HAS_PLOTLIB:
                show = input("\nShow trajectory plot? (y/n): ").strip().lower()
                if show == "y":
                    try:
                        draw_trajectory(v0, angle, h0, result)
                        print("(Press [clear] on the plot screen to return.)")
                    except Exception:
                        print("Could not draw the plot on this calculator.")

        again = input("\nAnother projectile? (y/n): ").strip().lower()
        if again != "y":
            break
    print("Done.")


main()
