#!/usr/bin/env python3
"""Rebuild the sellable ZIP bundles in ``bundles/``.

Each bundle ships every program twice: the ready-to-install ``.8xv`` Python AppVar
under ``8xv/`` and the plain-text source under ``py/``. Bundle READMEs live in
``bundles/readme/`` as tracked source files (so they can be reviewed and diffed like
anything else) and get a program-name table injected at build time, which keeps the
documented on-calculator names in sync with what the converter actually produced.

Zip entries use a fixed timestamp so rebuilding without content changes produces an
identical archive instead of a spurious binary diff.

Usage::

    python build_bundles.py --repo .. [--out ../bundles]
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from py_to_8xv import derive_var_name, validate_var_name  # noqa: E402

FIXED_TIMESTAMP = (2026, 1, 1, 0, 0, 0)
TABLE_PLACEHOLDER = "<!-- PROGRAM-NAME-TABLE -->"

CALCULUS = [
    "calculus/derivative_numeric.py",
    "calculus/simpsons_rule.py",
    "calculus/taylor_series.py",
    "calculus/newton_raphson.py",
    "calculus/limit_evaluator.py",
    "differential_equations/ode_solver_euler.py",
]
ALGEBRA = [
    "algebra_linear_stats/quadratic_solver.py",
    "algebra_linear_stats/quadratic_vertex_analyzer.py",
    "algebra_linear_stats/linear_system_solver.py",
    "algebra_linear_stats/matrix_toolkit.py",
    "algebra_linear_stats/descriptive_stats.py",
    "algebra_linear_stats/combinatorics_probability.py",
]
PHYSICS = [
    "physics_engineering/kinematics_solver.py",
    "physics_engineering/projectile_motion.py",
    "physics_engineering/ohms_law_circuits.py",
    "physics_engineering/rlc_impedance.py",
    "physics_engineering/statics_vectors.py",
    "physics_engineering/vector3d_toolkit.py",
]
CHEMISTRY = [
    "chemistry_and_exam_tools/ideal_gas_law.py",
    "chemistry_and_exam_tools/stoichiometry_molar_mass.py",
    "chemistry_and_exam_tools/unit_converter.py",
    "chemistry_and_exam_tools/formula_flashcards.py",
    "chemistry_and_exam_tools/exam_countdown_drill.py",
    "chemistry_and_exam_tools/acid_base_calculator.py",
]
FREE = [
    "chemistry_and_exam_tools/unit_converter.py",
    "algebra_linear_stats/quadratic_solver.py",
    "algebra_linear_stats/descriptive_stats.py",
]

BUNDLES = {
    "free_starter": {"programs": FREE, "nested": False},
    "calculus": {"programs": CALCULUS, "nested": False},
    "algebra_linear_stats": {"programs": ALGEBRA, "nested": False},
    "physics_engineering": {"programs": PHYSICS, "nested": False},
    "chemistry_and_exam_tools": {"programs": CHEMISTRY, "nested": False},
    "complete_toolkit": {"programs": CALCULUS + ALGEBRA + PHYSICS + CHEMISTRY, "nested": True},
}


def load_names(repo: str) -> dict:
    with open(os.path.join(repo, "tools", "varnames.json"), encoding="utf-8") as handle:
        return json.load(handle)


def var_name_for(rel_py: str, names: dict) -> str:
    stem = os.path.splitext(os.path.basename(rel_py))[0]
    return validate_var_name(names[stem].upper()) if stem in names else derive_var_name(stem)


def bundle_paths(rel_py: str, names: dict, nested: bool):
    """Return the (py, 8xv) arcnames and the source 8xv path for one program."""
    subject, filename = rel_py.split("/", 1)
    var_name = var_name_for(rel_py, names)
    src_8xv = os.path.join("8xv", subject, var_name + ".8xv")
    if nested:
        return f"py/{subject}/{filename}", f"8xv/{subject}/{var_name}.8xv", src_8xv, var_name
    return f"py/{filename}", f"8xv/{var_name}.8xv", src_8xv, var_name


def build_table(entries, nested: bool) -> str:
    lines = [
        "| Program | On-calculator name | Ready-to-install file |",
        "|---|---|---|",
    ]
    for rel_py, py_arc, xv_arc, var_name in entries:
        label = rel_py if nested else os.path.basename(rel_py)
        lines.append(f"| `{label}` | `{var_name}` | `{xv_arc}` |")
    return "\n".join(lines)


def build_bundle(repo: str, out_dir: str, name: str, spec: dict, names: dict) -> dict:
    nested = spec["nested"]
    entries = []
    for rel_py in spec["programs"]:
        py_arc, xv_arc, src_8xv, var_name = bundle_paths(rel_py, names, nested)
        entries.append((rel_py, py_arc, xv_arc, var_name))

    readme_path = os.path.join(repo, "bundles", "readme", name + ".md")
    with open(readme_path, encoding="utf-8") as handle:
        readme = handle.read()
    if TABLE_PLACEHOLDER not in readme:
        raise SystemExit(f"{readme_path}: missing {TABLE_PLACEHOLDER}")
    readme = readme.replace(TABLE_PLACEHOLDER, build_table(entries, nested))

    zip_path = os.path.join(out_dir, name + "_bundle.zip")
    os.makedirs(out_dir, exist_ok=True)

    members = [("README.md", readme.encode("utf-8"))]
    for rel_py, py_arc, xv_arc, _ in entries:
        with open(os.path.join(repo, rel_py.replace("/", os.sep)), "rb") as handle:
            members.append((py_arc, handle.read()))
        subject = rel_py.split("/", 1)[0]
        var_name = var_name_for(rel_py, names)
        src = os.path.join(repo, "8xv", subject, var_name + ".8xv")
        if not os.path.exists(src):
            raise SystemExit(f"missing converted AppVar {src}; run py_to_8xv.py first")
        with open(src, "rb") as handle:
            members.append((xv_arc, handle.read()))

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for arcname, payload in sorted(members):
            info = zipfile.ZipInfo(arcname, date_time=FIXED_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, payload)

    return {
        "name": name,
        "path": zip_path,
        "programs": len(entries),
        "files": len(members),
        "bytes": os.path.getsize(zip_path),
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Rebuild the sellable ZIP bundles.")
    parser.add_argument("--repo", required=True, help="repository root")
    parser.add_argument("--out", help="output directory (defaults to <repo>/bundles)")
    args = parser.parse_args(argv)

    out_dir = args.out or os.path.join(args.repo, "bundles")
    names = load_names(args.repo)

    for name, spec in BUNDLES.items():
        result = build_bundle(args.repo, out_dir, name, spec, names)
        print(
            f"{result['name']:<26} {result['programs']:>2} programs  "
            f"{result['files']:>2} files  {result['bytes']:>7} B  {result['path']}"
        )

    bundled = {rel for spec in BUNDLES.values() for rel in spec["programs"]}
    available = {
        f"{subject}/{filename}"
        for subject in sorted(os.listdir(args.repo))
        if os.path.isdir(os.path.join(args.repo, subject))
        and subject not in {"8xv", "tools", "bundles", ".git"}
        for filename in sorted(os.listdir(os.path.join(args.repo, subject)))
        if filename.endswith(".py")
    }
    unbundled = sorted(available - bundled)
    if unbundled:
        print(
            f"\nNote: {len(unbundled)} program(s) exist in the repo but are not in any bundle. "
            "Add them to the lists at the top of this script if they should ship:"
        )
        for rel in unbundled:
            print(f"  - {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
