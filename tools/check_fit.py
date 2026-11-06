#!/usr/bin/env python3
"""Check that downloaded sensory-ball parts actually fit together - before printing.

    python3 tools/check_fit.py half1.stl half2.stl screw.stl

Works on Windows, macOS and Linux with plain Python 3 (no extra packages).
It measures:
  - each half's size and the threaded hole in its flat face
  - the screw's thread
and tells you if the halves are different sizes or the screw will not go in.

Assumes the parts are as downloaded: halves flat side down (hole along Z),
screw lying on its side with its axis along X.
"""
import math
import struct
import sys

CLEARANCE = 0.2   # mm the screw's thread needs below the hole's on each side
SIZE_TOL = 0.5    # mm two halves may differ in diameter


def read_stl(path):
    data = open(path, "rb").read()
    if data[:5] == b"solid" and b"facet" in data[:400]:
        v = [tuple(map(float, l.split()[1:4])) for l in data.decode(errors="replace").splitlines()
             if l.strip().startswith("vertex")]
        return v
    n = struct.unpack("<I", data[80:84])[0]
    return [struct.unpack("<3f", data[84 + 50 * i + 12 + 12 * k: 84 + 50 * i + 24 + 12 * k])
            for i in range(n) for k in range(3)]


def box(pts):
    lo = [min(p[i] for p in pts) for i in range(3)]
    hi = [max(p[i] for p in pts) for i in range(3)]
    return lo, hi, [(lo[i] + hi[i]) / 2 for i in range(3)]


def measure_half(pts):
    """(diameter, hole thread inner d, hole thread outer d)."""
    lo, hi, c = box(pts)
    # Away from the hole's chamfered mouth and its closed end.
    rs = [math.hypot(p[0] - c[0], p[1] - c[1]) for p in pts
          if 2.0 < p[2] - lo[2] < 7.0 and math.hypot(p[0] - c[0], p[1] - c[1]) < 11]
    if not rs:
        return hi[0] - lo[0], None, None
    return hi[0] - lo[0], 2 * min(rs), 2 * max(rs)


def measure_screw(pts):
    """(thread root d, thread crest d) - radius about the X axis, near the
    equator so the printing flats on top and bottom don't count.

    The screw has a wider stop collar in the middle, so the crest is the
    MEDIAN of the per-0.5 mm-slice maxima along the axis, not the overall max.
    """
    lo, hi, c = box(pts)
    # ponytail: assumes the screw lies along X with flats on Z, as the V11
    # file is published; a screw stored standing up needs a rotation first.
    # The screw is hollow; its core wall sits inside 37% of the width.
    bins = {}
    for p in pts:
        r = abs(p[1] - c[1])
        if abs(p[2] - c[2]) < 2 and r > 0.37 * (hi[1] - lo[1]):
            bins.setdefault(int((p[0] - lo[0]) // 0.5), []).append(r)
    tops = sorted(max(v) for v in bins.values())
    root = min(min(v) for v in bins.values())
    return 2 * root, 2 * tops[len(tops) // 2]


def main(paths):
    if len(paths) != 3:
        sys.exit(__doc__)
    halves, screw_path = paths[:2], paths[2]
    ok = True
    sizes = []
    holes = []
    for p in halves:
        d, inner, outer = measure_half(read_stl(p))
        sizes.append(d)
        name = p.replace("\\", "/").split("/")[-1]
        if inner is None:
            print(f"  {name}: {d:.1f} mm wide, NO threaded hole found - is this a half?")
            ok = False
            continue
        holes.append(outer)
        print(f"  {name}: {d:.1f} mm wide, hole thread {inner:.2f}-{outer:.2f} mm")
    root, crest = measure_screw(read_stl(screw_path))
    print(f"  {screw_path.replace(chr(92), '/').split('/')[-1]}: thread {root:.2f}-{crest:.2f} mm")

    if abs(sizes[0] - sizes[1]) > SIZE_TOL:
        print(f"\nPROBLEM: the halves are different sizes ({sizes[0]:.1f} vs {sizes[1]:.1f} mm)."
              " Download two halves of the same size.")
        ok = False
    for outer in holes:
        if crest > outer - 2 * CLEARANCE:
            print(f"\nPROBLEM: the screw thread ({crest:.2f} mm) is too big for the hole ({outer:.2f} mm)."
                  " The screw and halves are probably different versions - download the matching screw.")
            ok = False
            break
    print("\nOK: these parts fit together." if ok else "\nDo not print yet - fix the problem above first.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
