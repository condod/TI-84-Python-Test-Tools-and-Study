# Program: quadratic_vertex_analyzer
# Purpose: Determine and analyze a quadratic from its vertex and one
#          other point on the parabola.
# Usage: Enter vertex (h, k) and point (x, y). Prints equation forms,
#        domain, range, symmetry, extrema, intercepts, and behavior.
#
# Two arbitrary points do not determine one unique quadratic. Requiring
# the first point to be the vertex provides the missing condition.

from math import isfinite, sqrt


EPS = 1e-10


def clean(value):
    if abs(value) < EPS:
        return 0.0
    return value


def number(value):
    value = clean(value)
    if value == int(value):
        return str(int(value))
    return str(round(value, 6))


def signed_term(coef, variable):
    if coef < 0:
        sign = " - "
    else:
        sign = " + "

    size = abs(coef)
    if variable != "" and abs(size - 1.0) < EPS:
        return sign + variable
    return sign + number(size) + variable


def leading_term(coef, variable):
    if abs(coef - 1.0) < EPS:
        return variable
    if abs(coef + 1.0) < EPS:
        return "-" + variable
    return number(coef) + variable


def quadratic_from_vertex(h, k, x, y):
    if not (isfinite(h) and isfinite(k) and
            isfinite(x) and isfinite(y)):
        raise ValueError("Coordinates must be finite numbers.")

    dx = x - h
    if abs(dx) < EPS:
        raise ValueError("Point x must differ from vertex x.")

    denominator = dx * dx
    if not isfinite(denominator):
        raise ValueError("Coordinates are too large.")

    a = (y - k) / denominator
    if abs(a) < EPS:
        raise ValueError("The two points make a line, not a quadratic.")

    b = -2.0 * a * h
    c = a * h * h + k
    if not (isfinite(a) and isfinite(b) and isfinite(c)):
        raise ValueError("Coordinates are too large.")
    return clean(a), clean(b), clean(c)


def x_intercepts(a, h, k):
    root_value = -k / a
    if root_value < -EPS:
        return ()
    if abs(root_value) < EPS:
        return (clean(h),)

    distance = sqrt(root_value)
    return (clean(h - distance), clean(h + distance))


def standard_equation(a, b, c):
    equation = "y=" + leading_term(a, "x^2")
    if abs(b) >= EPS:
        equation += signed_term(b, "x")
    if abs(c) >= EPS:
        equation += signed_term(c, "")
    return equation


def vertex_equation(a, h, k):
    if h < 0:
        inside = "x+" + number(-h)
    elif h > 0:
        inside = "x-" + number(h)
    else:
        inside = "x"

    equation = "y=" + leading_term(a, "(" + inside + ")^2")
    if abs(k) >= EPS:
        equation += signed_term(k, "")
    return equation


def pause():
    input("ENTER for more")


def show_results(h, k, x, y):
    a, b, c = quadratic_from_vertex(h, k, x, y)
    roots = x_intercepts(a, h, k)

    print("")
    print("VERTEX FORM")
    print(vertex_equation(a, h, k))
    print("")
    print("STANDARD FORM")
    print(standard_equation(a, b, c))
    pause()

    print("")
    print("DOMAIN")
    print("All real numbers")
    print("(-inf,inf)")
    print("")
    print("RANGE")
    if a > 0:
        print("y >= " + number(k))
        print("[" + number(k) + ",inf)")
    else:
        print("y <= " + number(k))
        print("(-inf," + number(k) + "]")
    pause()

    print("")
    print("VERTEX")
    print("(" + number(h) + "," + number(k) + ")")
    print("AXIS OF SYMMETRY")
    print("x=" + number(h))
    print("OPENS")
    if a > 0:
        print("Up")
        print("Minimum y=" + number(k))
    else:
        print("Down")
        print("Maximum y=" + number(k))
    pause()

    print("")
    print("Y-INTERCEPT")
    print("(0," + number(c) + ")")
    print("")
    print("X-INTERCEPTS")
    if len(roots) == 0:
        print("None (no real zeros)")
    elif len(roots) == 1:
        print("(" + number(roots[0]) + ",0)")
    else:
        print("(" + number(roots[0]) + ",0)")
        print("(" + number(roots[1]) + ",0)")
    pause()

    print("")
    print("BEHAVIOR")
    if a > 0:
        print("Decreasing to x=" + number(h))
        print("Increasing after x=" + number(h))
    else:
        print("Increasing to x=" + number(h))
        print("Decreasing after x=" + number(h))
    print("")
    print("CHECKED POINT")
    print("(" + number(x) + "," + number(y) + ")")


def main():
    print("QUADRATIC INFO")
    print("Use vertex + one")
    print("point on parabola.")

    while True:
        try:
            print("")
            h = float(input("Vertex x: "))
            k = float(input("Vertex y: "))
            x = float(input("Point x: "))
            y = float(input("Point y: "))
            show_results(h, k, x, y)
        except ValueError as error:
            print("")
            print("INPUT ERROR")
            print(str(error))

        print("")
        again = input("Again? Y/N: ")
        if again.upper() != "Y":
            print("Done.")
            break


main()
