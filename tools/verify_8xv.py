#!/usr/bin/env python3
"""Verification harness for the ``.py`` -> ``.8xv`` converter in ``py_to_8xv.py``.

Runs four independent classes of check:

1. **Reference reproduction.** Rebuild a Python AppVar that TI's own TI-SmartView CE
   5.3.0.384 produced and require a byte-for-byte match. This is the strongest
   available evidence that the container and payload layout are correct, because the
   expected bytes came from TI's software rather than from our own assumptions.
2. **Structural checks.** Re-parse every generated file and validate the signature,
   export bytes, header length, var-type byte, both variable-data length fields, the
   payload length prefix, the ``PYCD`` magic, the metadata terminator, and the
   trailing checksum.
3. **Round-trip.** Confirm the script recovered from each ``.8xv`` is byte-identical
   to the normalised source.
4. **Cross-validation.** If ``tivars`` (tivars_lib_py) is installed, have it parse
   each generated file independently and compare the name, type ID, and data bytes.

None of this can prove the files run on real hardware; no calculator or emulator is
available here. See ``bundles/FILE_FORMAT_NOTES.md`` for the honest scope of what
these checks do and do not establish.

Usage::

    python verify_8xv.py --src .. --out ../8xv [--reference python_HELLO.8xv]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from py_to_8xv import (  # noqa: E402
    ARCHIVE_FLAG_RAM,
    CHECKSUM_LENGTH,
    ENTRY_META_LENGTH,
    HEADER_LENGTH,
    PY_MAGIC_CODE,
    TYPE_ID_APPVAR,
    build_8xv,
    derive_var_name,
    iter_sources,
    normalize_script,
    output_path_for,
    parse_8xv,
    validate_var_name,
)

# The exact bytes TI-SmartView CE 5.3.0.384 wrote for a program named HELLO,
# taken from testData/python_HELLO.8xv in adriweb/tivars_lib_cpp.
REFERENCE_NAME = "HELLO"
REFERENCE_COMMENT = "Created by TI-Smartview CE 5.3.0.384"
REFERENCE_SCRIPT = b"import sys\nprint(sys.version)\n"


ONCALC_HEADER_RE = re.compile(r"^#\s*On-calc name:\s*([A-Za-z0-9]+)\s*$", re.MULTILINE)


class Failure(Exception):
    pass


def check_header_name(src_path: str, var_name: str):
    """Require the program's own ``# On-calc name:`` header to match its AppVar name.

    Each program prints that same short name as its on-screen banner, so if the two
    drift apart a student picks ``QUADSOLV`` out of the Python App list and the program
    announces itself as ``QUAD``. The header is the authoritative side; ``varnames.json``
    mirrors it.
    """
    with open(src_path, "r", encoding="utf-8") as handle:
        head = handle.read(1024)
    match = ONCALC_HEADER_RE.search(head)
    check(match is not None, "source has no '# On-calc name:' header comment")
    declared = match.group(1).upper()
    check(
        declared == var_name,
        f"source header declares '{declared}' but the AppVar installs as '{var_name}'; "
        "update tools/varnames.json or the header so they agree",
    )


def check(condition: bool, message: str):
    if not condition:
        raise Failure(message)


def check_reference(reference_path: str) -> str:
    """Rebuild TI's own Python AppVar and require an exact byte match."""
    with open(reference_path, "rb") as handle:
        expected = handle.read()

    parsed = parse_8xv(expected)
    check(parsed["name"] == REFERENCE_NAME, f"reference name is {parsed['name']!r}")
    check(parsed["script"] == REFERENCE_SCRIPT, "reference script differs from the expected constant")

    rebuilt = build_8xv(
        REFERENCE_SCRIPT,
        REFERENCE_NAME,
        comment=REFERENCE_COMMENT,
        archived=False,
        version=parsed["version"],
        product_id=parsed["product_id"],
    )
    check(
        rebuilt == expected,
        "rebuilt reference does not match TI's bytes:\n"
        f"  expected {expected.hex()}\n  actual   {rebuilt.hex()}",
    )
    return f"reproduced TI-SmartView's {len(expected)}-byte {REFERENCE_NAME} AppVar byte-for-byte"


def check_structure(blob: bytes, source_script: bytes) -> dict:
    parsed = parse_8xv(blob)  # already validates lengths, magic, and checksum
    check(blob[:8] == b"**TI83F*", "bad file signature")
    check(blob[8:10] == b"\x1a\x0a", "bad export bytes")
    check(parsed["type_id"] == TYPE_ID_APPVAR, f"var type 0x{parsed['type_id']:02X} != 0x15")
    check(parsed["magic"] == PY_MAGIC_CODE, f"payload magic {parsed['magic']!r} != b'PYCD'")
    check(parsed["archive_flag"] == ARCHIVE_FLAG_RAM, "expected an unarchived (RAM) entry")
    check(
        parsed["declared_data_length"] == len(blob) - HEADER_LENGTH - 2 - CHECKSUM_LENGTH,
        "declared data length disagrees with file size",
    )
    check(parsed["var_data_length"] == parsed["payload_length"] + 2, "var data length != payload + 2")
    check(parsed["script"] == source_script, "round-trip script mismatch")
    check(ENTRY_META_LENGTH == 13, "entry meta length constant changed")
    return parsed


def cross_validate(path: str, expected_name: str, expected_payload_prefix: bytes):
    """Independently parse a generated file with tivars_lib_py, if it is installed."""
    try:
        from tivars.var import TIVarFile
    except ImportError:
        return None

    var = TIVarFile.open(path)
    check(len(var.entries) == 1, f"tivars found {len(var.entries)} entries, expected 1")
    entry = var.entries[0]
    check(entry.name == expected_name, f"tivars read name {entry.name!r} != {expected_name!r}")
    check(entry.type_id == TYPE_ID_APPVAR, f"tivars read type 0x{entry.type_id:02X} != 0x15")
    check(
        bytes(entry.data).startswith(expected_payload_prefix),
        "tivars read a data section that does not start with the expected payload",
    )
    with open(path, "rb") as handle:
        original = handle.read()
    check(var.bytes() == original, "tivars re-serialisation differs from our bytes")
    return True


def check_bundles(bundles_dir: str, failures: list) -> int:
    """Open every shipped zip and confirm each .8xv matches the .py beside it.

    This checks the artifact a buyer actually downloads, rather than the intermediate
    tree, so it catches packaging mistakes such as a stale or mismatched AppVar.
    """
    import zipfile

    checked = 0
    zips = sorted(
        os.path.join(bundles_dir, f) for f in os.listdir(bundles_dir) if f.endswith(".zip")
    )
    if not zips:
        failures.append(f"no bundle zips found in {bundles_dir}")
        return 0

    for zip_path in zips:
        label = os.path.basename(zip_path)
        try:
            with zipfile.ZipFile(zip_path) as archive:
                members = archive.namelist()
                check("README.md" in members, "bundle has no README.md")

                readme = archive.read("README.md").decode("utf-8")
                check(
                    "Exam Policy Disclaimer" in readme,
                    "bundle README is missing the exam policy disclaimer",
                )
                check(
                    "PROGRAM-NAME-TABLE" not in readme,
                    "bundle README still contains an unexpanded table placeholder",
                )

                sources = {m for m in members if m.startswith("py/") and m.endswith(".py")}
                appvars = {m for m in members if m.startswith("8xv/") and m.endswith(".8xv")}
                check(
                    len(sources) == len(appvars),
                    f"{len(sources)} .py but {len(appvars)} .8xv in the bundle",
                )

                # Pair them by recovered script, which is naming-independent.
                by_script = {}
                for member in sources:
                    by_script[normalize_script(archive.read(member))] = member

                for member in sorted(appvars):
                    parsed = parse_8xv(archive.read(member))
                    check(
                        parsed["script"] in by_script,
                        f"{member} does not match any .py source in the same bundle",
                    )
                    check(
                        f"`{parsed['name']}`" in readme,
                        f"{member} installs as {parsed['name']}, which the README never mentions",
                    )
                    checked += 1

            print(f"[ok]   bundle {label:<34} {len(appvars)} AppVars matched to their sources")
        except Exception as exc:  # noqa: BLE001
            failures.append(f"bundle {label}: {exc}")
            print(f"[FAIL] bundle {label}: {exc}")

    return checked


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Verify generated .8xv Python AppVars.")
    parser.add_argument("--src", required=True, help="root of the .py sources")
    parser.add_argument("--out", required=True, help="root of the generated .8xv tree")
    parser.add_argument("--reference", help="path to TI's python_HELLO.8xv for exact-match testing")
    parser.add_argument("--skip", action="append", default=[], metavar="DIR",
                        help="extra directory name to exclude (repeatable)")
    parser.add_argument("--only", action="append", default=[], metavar="DIR",
                        help="restrict verification to this top-level subdirectory (repeatable)")
    parser.add_argument("--names", help="JSON file mapping source stems to variable names")
    parser.add_argument("--name-by-var", action="store_true",
                        help="outputs are named after the variable, not the source stem")
    parser.add_argument("--bundles", help="also verify the shipped zip bundles in this directory")
    args = parser.parse_args(argv)

    names = {}
    if args.names:
        with open(args.names, "r", encoding="utf-8") as handle:
            names = json.load(handle)

    failures = []

    if args.reference:
        try:
            print(f"[ok]   reference match: {check_reference(args.reference)}")
        except Exception as exc:  # noqa: BLE001
            failures.append(f"reference match: {exc}")
            print(f"[FAIL] reference match: {exc}")
    else:
        print("[skip] reference match: no --reference file supplied")

    verified = 0
    cross_validated = 0
    sources = list(iter_sources(args.src, skip_dirs=args.skip, only_dirs=args.only))
    if not sources:
        print(f"[FAIL] no .py sources found under {args.src}")
        return 1

    taken: set = set()
    expected_outputs = []
    for src_path in sources:
        rel = os.path.relpath(src_path, args.src)
        stem = os.path.splitext(os.path.basename(src_path))[0]
        var_name = validate_var_name(names[stem].upper()) if stem in names else derive_var_name(stem, taken)
        taken.add(var_name)
        out_path = output_path_for(src_path, args.src, args.out, var_name, args.name_by_var)
        expected_outputs.append(out_path)
        label = rel.replace("\\", "/")
        try:
            check(os.path.exists(out_path), f"missing output {out_path}")
            with open(src_path, "rb") as handle:
                script = normalize_script(handle.read())
            with open(out_path, "rb") as handle:
                blob = handle.read()

            parsed = check_structure(blob, script)
            check(parsed["name"] == var_name, f"name is {parsed['name']!r}, expected {var_name!r}")
            check_header_name(src_path, var_name)
            result = cross_validate(out_path, parsed["name"], PY_MAGIC_CODE)
            if result:
                cross_validated += 1
            verified += 1
            print(
                f"[ok]   {label:<52} {parsed['name']:<8} "
                f"{len(script):>6} B src  {len(blob):>6} B 8xv  cksum 0x{parsed['checksum']:04X}"
            )
        except Exception as exc:  # noqa: BLE001
            failures.append(f"{label}: {exc}")
            print(f"[FAIL] {label}: {exc}")

    produced = {
        os.path.normcase(os.path.join(dirpath, filename))
        for dirpath, _, filenames in os.walk(args.out)
        for filename in filenames
        if filename.endswith(".8xv")
    }
    orphans = sorted(produced - {os.path.normcase(p) for p in expected_outputs})
    for orphan in orphans:
        failures.append(f"orphan output: {orphan}")
        print(f"[FAIL] orphan .8xv with no matching source: {orphan}")

    bundled = check_bundles(args.bundles, failures) if args.bundles else 0

    print()
    print(f"programs structurally verified and round-tripped: {verified}/{len(sources)}")
    if args.bundles:
        print(f"AppVars verified inside shipped bundles: {bundled}")
    if cross_validated:
        print(f"cross-validated with tivars_lib_py: {cross_validated}/{len(sources)}")
    else:
        print("cross-validation with tivars_lib_py: SKIPPED (package not installed)")

    if failures:
        print(f"\nFAILURES ({len(failures)}):")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print("\nAll structural, round-trip, and cross-validation checks passed.")
    print("NOTE: this does not prove on-device behaviour; no calculator or emulator was available.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
