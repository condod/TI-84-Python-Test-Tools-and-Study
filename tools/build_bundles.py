#!/usr/bin/env python3
"""Rebuild the sellable ZIP bundles in ``bundles/``.

Each bundle ships every program twice: the ready-to-install ``.8xv`` Python AppVar
under ``8xv/`` and the plain-text source under ``py/``. Bundle READMEs live in
``bundles/readme/`` as tracked source files (so they can be reviewed and diffed like
anything else) and get a program-name table injected at build time, which keeps the
documented on-calculator names in sync with what the converter actually produced.

The install guide and the compliance text — hardware compatibility, the Press-to-Test
data-loss warning, the exam-policy disclaimer and the trademark footer — live once in
``bundles/readme/_shared.md`` and are injected into every bundle README through
``<!-- SHARED: NAME -->`` placeholders. The build fails if a bundle omits one, which
is what stops the nine copies drifting apart again.

Zip entries use a fixed timestamp so rebuilding without content changes produces an
identical archive instead of a spurious binary diff.

Usage::

    python build_bundles.py --repo .. [--out ../bundles]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from py_to_8xv import derive_var_name, validate_var_name  # noqa: E402

FIXED_TIMESTAMP = (2026, 1, 1, 0, 0, 0)
TABLE_PLACEHOLDER = "<!-- PROGRAM-NAME-TABLE -->"

# The top-level folders that hold sellable programs. Anything else at the repo root
# (qa/, storefront/, business/, tools/, ...) is not part of the product.
SUBJECT_DIRS = [
    "algebra_linear_stats",
    "astronomy",
    "biology",
    "calculus",
    "chemistry_and_exam_tools",
    "computer_science",
    "differential_equations",
    "finance",
    "geometry",
    "physics_engineering",
    "precalculus",
    "thermo_materials",
    "trigonometry",
]

# --- The product lineup ------------------------------------------------------
#
# Bundles are grouped by the course a student is actually enrolled in, not by the
# repository's folder layout. That is why several folders are split across bundles
# (the stats programs in algebra_linear_stats sell to a statistics course, the
# quadratics sell to a precalculus course) and why the thinner folders are folded
# into a larger neighbour instead of shipping as a one-program bundle.

ALGEBRA_PRECALC_TRIG = [
    "algebra_linear_stats/quadratic_solver.py",
    "algebra_linear_stats/quadratic_vertex_analyzer.py",
    "algebra_linear_stats/complex_number_calculator.py",
    "algebra_linear_stats/linear_system_solver.py",
    "algebra_linear_stats/matrix_toolkit.py",
    "precalculus/polynomial_analyzer.py",
    "precalculus/sequences_series.py",
    "precalculus/log_exp_solver.py",
    "trigonometry/oblique_triangle_solver.py",
    "trigonometry/unit_circle_reference.py",
    "geometry/shape_geometry_solver.py",
]
CALCULUS = [
    "calculus/derivative_numeric.py",
    "calculus/simpsons_rule.py",
    "calculus/taylor_series.py",
    "calculus/newton_raphson.py",
    "calculus/limit_evaluator.py",
    "differential_equations/ode_solver_euler.py",
]
STATISTICS = [
    "algebra_linear_stats/descriptive_stats.py",
    "algebra_linear_stats/confidence_interval_hypothesis_test.py",
    "algebra_linear_stats/combinatorics_probability.py",
    "biology/chi_square_genetics.py",
    "computer_science/discrete_math_toolkit.py",
]
PHYSICS = [
    "physics_engineering/kinematics_solver.py",
    "physics_engineering/projectile_motion.py",
    "physics_engineering/statics_vectors.py",
    "physics_engineering/vector3d_toolkit.py",
    "physics_engineering/ohms_law_circuits.py",
    "physics_engineering/rlc_impedance.py",
    "physics_engineering/fluid_mechanics_solver.py",
    "physics_engineering/heat_transfer_calculator.py",
    "thermo_materials/ideal_gas_processes.py",
    "thermo_materials/carnot_efficiency.py",
    "thermo_materials/stress_strain.py",
    "thermo_materials/thermal_expansion.py",
    "astronomy/orbital_mechanics_calculator.py",
]
CHEMISTRY = [
    "chemistry_and_exam_tools/ideal_gas_law.py",
    "chemistry_and_exam_tools/stoichiometry_molar_mass.py",
    "chemistry_and_exam_tools/acid_base_calculator.py",
    "chemistry_and_exam_tools/reaction_kinetics.py",
    "chemistry_and_exam_tools/unit_converter.py",
    "chemistry_and_exam_tools/formula_flashcards.py",
    "chemistry_and_exam_tools/exam_countdown_drill.py",
]
BIOLOGY = [
    "biology/punnett_square_solver.py",
    "biology/hardy_weinberg.py",
    "biology/chi_square_genetics.py",
    "biology/population_growth.py",
    "biology/dilution_calculator.py",
    "biology/surface_area_volume.py",
]
FINANCE = [
    "finance/tvm_solver.py",
    "finance/loan_amortization.py",
    "finance/compound_interest.py",
    "finance/npv_irr.py",
    "finance/break_even_margin.py",
]

# The lead magnet is deliberately cross-subject: every program in it is useful in
# more than one course, and each one also ships inside a paid bundle.
FREE = [
    "chemistry_and_exam_tools/unit_converter.py",
    "algebra_linear_stats/quadratic_solver.py",
    "algebra_linear_stats/descriptive_stats.py",
    "trigonometry/unit_circle_reference.py",
    "geometry/shape_geometry_solver.py",
]

SUBJECT_BUNDLES = [
    ALGEBRA_PRECALC_TRIG,
    CALCULUS,
    STATISTICS,
    PHYSICS,
    CHEMISTRY,
    BIOLOGY,
    FINANCE,
]


def dedupe(*groups) -> list:
    """Concatenate program lists, keeping the first occurrence of each path.

    chi_square_genetics.py sells into both the statistics and the biology bundle,
    so the complete toolkit has to collapse the repeat rather than ship it twice.
    """
    seen = set()
    out = []
    for group in groups:
        for rel in group:
            if rel not in seen:
                seen.add(rel)
                out.append(rel)
    return out


COMPLETE = dedupe(*SUBJECT_BUNDLES)

BUNDLES = {
    "free_starter": {"programs": FREE, "nested": False},
    "algebra_precalculus_trig": {"programs": ALGEBRA_PRECALC_TRIG, "nested": False},
    "calculus": {"programs": CALCULUS, "nested": False},
    "statistics_probability": {"programs": STATISTICS, "nested": False},
    "physics_engineering": {"programs": PHYSICS, "nested": False},
    "chemistry": {"programs": CHEMISTRY, "nested": False},
    "biology": {"programs": BIOLOGY, "nested": False},
    "finance": {"programs": FINANCE, "nested": False},
    "complete_toolkit": {"programs": COMPLETE, "nested": True},
}


SHARED_SOURCE = "_shared.md"
BLOCK_START_RE = re.compile(r"^<!-- BLOCK: ([A-Z0-9-]+) -->$", re.MULTILINE)
BLOCK_END = "<!-- END BLOCK -->"


def load_names(repo: str) -> dict:
    with open(os.path.join(repo, "tools", "varnames.json"), encoding="utf-8") as handle:
        return json.load(handle)


def load_shared_blocks(repo: str) -> dict:
    """Parse ``bundles/readme/_shared.md`` into ``{NAME: markdown}``.

    The compliance text (exam policy, Press-to-Test, hardware compatibility, the
    trademark footer) has to read identically in every bundle, so it is stored once
    and injected rather than duplicated nine times.
    """
    path = os.path.join(repo, "bundles", "readme", SHARED_SOURCE)
    with open(path, encoding="utf-8") as handle:
        text = handle.read()

    blocks = {}
    for match in BLOCK_START_RE.finditer(text):
        name = match.group(1)
        end = text.find(BLOCK_END, match.end())
        if end == -1:
            raise SystemExit(f"{path}: block {name} is never closed with {BLOCK_END}")
        blocks[name] = text[match.end():end].strip("\n")
    if not blocks:
        raise SystemExit(f"{path}: no <!-- BLOCK: NAME --> sections found")
    return blocks


def inject_shared(readme: str, blocks: dict, label: str) -> str:
    """Replace every ``<!-- SHARED: NAME -->`` placeholder with its block."""
    used = set()

    def substitute(match):
        name = match.group(1)
        if name not in blocks:
            raise SystemExit(f"{label}: unknown shared block {name!r}")
        used.add(name)
        return blocks[name]

    result = re.sub(r"<!-- SHARED: ([A-Z0-9-]+) -->", substitute, readme)

    # These carry the legal and support text a buyer must see; a bundle that omits
    # one is a defect, so fail the build rather than shipping it.
    for required in ("COMPATIBILITY", "PRESS-TO-TEST", "EXAM-POLICY", "TRADEMARK"):
        if required not in used:
            raise SystemExit(f"{label}: missing required shared block {required}")
    return result


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


def build_bundle(repo: str, out_dir: str, name: str, spec: dict, names: dict, blocks: dict) -> dict:
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
    readme = inject_shared(readme, blocks, readme_path)

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
    blocks = load_shared_blocks(args.repo)

    for name, spec in BUNDLES.items():
        result = build_bundle(args.repo, out_dir, name, spec, names, blocks)
        print(
            f"{result['name']:<26} {result['programs']:>2} programs  "
            f"{result['files']:>2} files  {result['bytes']:>7} B  {result['path']}"
        )

    bundled = {rel for spec in BUNDLES.values() for rel in spec["programs"]}
    available = {
        f"{subject}/{filename}"
        for subject in SUBJECT_DIRS
        if os.path.isdir(os.path.join(args.repo, subject))
        for filename in sorted(os.listdir(os.path.join(args.repo, subject)))
        if filename.endswith(".py")
    }

    print(f"\nlibrary: {len(available)} programs across {len(SUBJECT_DIRS)} subject folders")
    print(f"complete toolkit: {len(COMPLETE)} programs")

    problems = 0
    unbundled = sorted(available - bundled)
    if unbundled:
        problems += len(unbundled)
        print(
            f"\nERROR: {len(unbundled)} program(s) exist in the repo but are in no bundle. "
            "Add them to the lists at the top of this script:"
        )
        for rel in unbundled:
            print(f"  - {rel}")

    missing = sorted(bundled - available)
    if missing:
        problems += len(missing)
        print(f"\nERROR: {len(missing)} bundled path(s) do not exist on disk:")
        for rel in missing:
            print(f"  - {rel}")

    if set(COMPLETE) != available:
        problems += 1
        print("\nERROR: the complete toolkit does not contain exactly the whole library.")

    if problems:
        return 1

    print("every program in the library ships in at least one bundle.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
