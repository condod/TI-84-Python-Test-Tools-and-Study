#!/usr/bin/env python3
"""Build storefront/catalog.js from the three program libraries."""
from __future__ import annotations

import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PRIVATE = r"C:\Users\condo\Downloads\TI-84-Python-Private"
ARCADE = r"C:\Users\condo\Downloads\TI Python programs"


def js_dump(obj) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)


def parse_readme_tables(text: str) -> dict[str, list[dict]]:
    sections: dict[str, list[dict]] = {}
    current = None
    for line in text.splitlines():
        if line.startswith("## ") and not line.startswith("###"):
            current = line[3:].strip()
            sections[current] = []
            continue
        if current is None or not line.startswith("| `"):
            continue
        m = re.match(r"\| `([^`]+)` \| (\S+) \| (.+) \|", line)
        if not m:
            continue
        path, name, blurb = m.group(1), m.group(2), m.group(3).strip()
        sections[current].append(
            {"file": os.path.basename(path), "oncalc": name, "blurb": blurb}
        )
    return sections


def academic_from_index(html: str) -> list[dict]:
    """Pull the existing 52-program listings out of index.html."""
    bundles = []
    for m in re.finditer(
        r'<article class="card include-card">\s*<header class="include-head">\s*'
        r"<h3>(.*?)</h3>\s*<span class=\"pill\">(.*?)</span>\s*</header>\s*"
        r'<ul class="prog-list">(.*?)</ul>',
        html,
        re.S,
    ):
        title = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        title = (
            title.replace("&amp;", "&")
            .replace("&nbsp;", " ")
            .replace("&#39;", "'")
        )
        pill = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        items = []
        for li in re.finditer(
            r"<li><code>([^<]+)</code><span>(.*?)</span></li>", m.group(3), re.S
        ):
            items.append(
                {
                    "file": li.group(1).strip(),
                    "oncalc": "",
                    "blurb": re.sub(r"\s+", " ", li.group(2)).strip(),
                }
            )
        bundles.append({"title": title, "pill": pill, "programs": items})
    return bundles


def take(sections, *heads):
    out = []
    for h in heads:
        out.extend(sections.get(h, []))
    return out


def main() -> None:
    with open(os.path.join(HERE, "index.html"), encoding="utf-8") as f:
        html = f.read()
    academic = academic_from_index(html)
    with open(os.path.join(PRIVATE, "README.md"), encoding="utf-8") as f:
        priv = parse_readme_tables(f.read())

    arcade = [
        {"file": "snake.py", "oncalc": "SNAKE", "blurb": "Turn-based snake on a 16x8 field."},
        {"file": "g2048.py", "oncalc": "G2048", "blurb": "2048 with arrow-key slides."},
        {"file": "minesweeper.py", "oncalc": "MINES", "blurb": "8x8 minesweeper."},
        {"file": "wordle.py", "oncalc": "WORDLE", "blurb": "5-letter word game."},
        {"file": "lights_out.py", "oncalc": "LIGHTS", "blurb": "5x5 Lights Out. Always solvable."},
    ]

    new_bundles = [
        {
            "sku": "arcade",
            "name": "Arcade Pack",
            "short": "Snake · 2048 · Mines · Wordle · Lights Out",
            "best": "Games on the keypad",
            "price": 9,
            "programs": arcade,
        },
        {
            "sku": "classroom",
            "name": "Classroom & Everyday",
            "short": "Caller · GPA · flashcards · tip · wage · lab regression",
            "best": "Teachers, homework, daily calc",
            "price": 19,
            "programs": take(priv, "Classroom", "Life / lab"),
        },
        {
            "sku": "shop_hobby",
            "name": "Shop, Hobby & Tabletop",
            "short": "Plates · stairs · resistors · Morse · D&D",
            "best": "Shop math, hobbies, tabletop",
            "price": 15,
            "programs": take(priv, "Shop", "Hobby", "Tabletop"),
        },
        {
            "sku": "algebra_steps",
            "name": "Algebra Steps",
            "short": "Synthetic division · partial fractions · conics",
            "best": "Algebra II / college algebra steps",
            "price": 15,
            "programs": take(priv, "Algebra steps"),
        },
        {
            "sku": "calc3",
            "name": "Calc Steps & Calc 3",
            "short": "Related rates · gradient · Hessian · line integrals",
            "best": "Calc I–III homework steppers",
            "price": 19,
            "programs": take(priv, "Calc steps", "Calc 3"),
        },
        {
            "sku": "diffeq",
            "name": "Differential Equations & Numerical",
            "short": "Laplace · variation of parameters · bisection",
            "best": "ODE course + root finding",
            "price": 15,
            "programs": take(priv, "Differential equations", "Numerical analysis"),
        },
        {
            "sku": "linalg",
            "name": "Linear Algebra & Complex",
            "short": "RREF · Gram-Schmidt · Cauchy-Riemann",
            "best": "Lin alg, complex analysis",
            "price": 12,
            "programs": take(priv, "Linear algebra", "Complex analysis"),
        },
        {
            "sku": "phys2",
            "name": "Physics Extras",
            "short": "Optics · relativity · SHM · Doppler · Bohr",
            "best": "Physics I/II extras beyond SUVAT",
            "price": 12,
            "programs": take(priv, "Physics"),
        },
        {
            "sku": "chem2",
            "name": "Chemistry Extras",
            "short": "ICE tables · Nernst · Beer-Lambert · empirical",
            "best": "Gen chem labs and electrochem",
            "price": 12,
            "programs": take(priv, "Chemistry", "Chem steps"),
        },
        {
            "sku": "discrete",
            "name": "Visual Math, Stats Extras & CS",
            "short": "Slope field · ANOVA · Bayes · bases · Collatz",
            "best": "Visual calc, extra stats, CS, number theory",
            "price": 19,
            "programs": take(
                priv,
                "Visual math",
                "Stats",
                "Computer science",
                "Number theory",
                "Trig",
            ),
        },
    ]

    sku_map = {
        "Algebra, Precalculus & Trigonometry": "algebra",
        "Calculus & Differential Equations": "calculus",
        "Statistics, Probability & Discrete Math": "stats",
        "Physics & Engineering": "physics",
        "Chemistry & Exam Tools": "chemistry",
        "Biology & Lab Science": "biology",
        "Finance & Business Math": "finance",
    }
    price_map = {
        "algebra": 19,
        "calculus": 12,
        "stats": 12,
        "physics": 19,
        "chemistry": 15,
        "biology": 12,
        "finance": 12,
    }
    best_map = {
        "algebra": "College algebra, precalc, trig, geometry",
        "calculus": "Calc I/II/III, intro ODEs",
        "stats": "Intro statistics, probability, discrete math",
        "physics": "Physics I/II, statics, circuits, thermo",
        "chemistry": "General chemistry + study drilling",
        "biology": "Intro bio, genetics, ecology, lab methods",
        "finance": "Personal finance, business math, eng. economics",
    }
    short_map = {
        "algebra": "Quadratics · Matrices · Polynomials · Unit circle",
        "calculus": "Derivatives · Integrals · Series · ODEs",
        "stats": "Confidence intervals · Hypothesis tests · Chi-square",
        "physics": "Kinematics · Circuits · Fluids · Thermo · Materials",
        "chemistry": "Gas laws · Stoichiometry · pH · Kinetics · Drills",
        "biology": "Punnett · Hardy-Weinberg · Dilutions · Growth",
        "finance": "TVM · Amortization · NPV/IRR · Break-even",
    }

    original = []
    for b in academic:
        sku = sku_map[b["title"]]
        original.append(
            {
                "sku": sku,
                "name": b["title"],
                "short": short_map[sku],
                "best": best_map[sku],
                "price": price_map[sku],
                "programs": b["programs"],
            }
        )

    free = {
        "sku": "free",
        "name": "Free Starter Pack",
        "short": "Unit converter · Quadratics · Stats · Unit circle · Geometry",
        "best": "Trying it out on any course",
        "price": 0,
        "programs": [
            {"file": "unit_converter.py", "oncalc": "", "blurb": "Length, mass, pressure, temperature, energy."},
            {"file": "quadratic_solver.py", "oncalc": "", "blurb": "Real and complex roots with discriminant."},
            {"file": "descriptive_stats.py", "oncalc": "", "blurb": "Mean, median, mode, variance, standard deviation."},
            {"file": "unit_circle_reference.py", "oncalc": "", "blurb": "Exact trig values, reference angle, quadrant."},
            {"file": "shape_geometry_solver.py", "oncalc": "", "blurb": "2D area/perimeter, 3D volume/surface area."},
        ],
    }

    all_paid = original + new_bundles
    n_orig = sum(len(b["programs"]) for b in original)
    # chi_square is in two original bundles
    orig_files = []
    seen = set()
    for b in original:
        for p in b["programs"]:
            if p["file"] not in seen:
                seen.add(p["file"])
                orig_files.append(p["file"])
    n_new = sum(len(b["programs"]) for b in new_bundles)
    n_unique = len(orig_files) + n_new
    separate = sum(b["price"] for b in all_paid)

    catalog = {
        "totalPrograms": n_unique,
        "subjectAreas": 22,
        "completePrice": 79,
        "separateTotal": separate,
        "originalCount": len(orig_files),
        "companionCount": n_new,
        "free": free,
        "bundles": all_paid,
        "complete": {
            "sku": "complete",
            "name": "Complete Toolkit",
            "short": "All %d programs + master reference" % n_unique,
            "best": "Every subject and the arcade pack",
            "price": 79,
            "count": n_unique,
        },
    }

    out = os.path.join(HERE, "catalog.js")
    with open(out, "w", encoding="utf-8") as f:
        f.write("/* generated by build_catalog.py — do not edit by hand */\n")
        f.write("window.TI84_CATALOG = ")
        f.write(js_dump(catalog))
        f.write(";\n")

    print("wrote", out)
    print("unique programs", n_unique)
    print("original unique", len(orig_files), "listed slots", n_orig)
    print("companion", n_new)
    print("separate $", separate)
    for b in all_paid:
        print(" ", b["sku"], len(b["programs"]), "$" + str(b["price"]))


if __name__ == "__main__":
    main()
