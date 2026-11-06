#!/usr/bin/env python3
"""Pull single-colour STLs for ONE ball out of a multi-colour sensory-ball 3mf.

    python3 tools/extract_ball.py "Sanso 51 U1.3mf" model/

Takes the meshes only - none of the 3mf's slicer settings. Each text part is
merged into the half it belongs to, so a single-colour printer prints it as
part of that half. Writes half1.stl, half2.stl and screw.stl, each sitting on
z=0 exactly as oriented on the 3mf's plate.

Works on Windows, macOS and Linux with plain Python 3.
"""
import os
import re
import struct
import sys
import zipfile


def mat(t):
    """3mf transform string -> (3x3 rows, translation), row-vector convention."""
    v = list(map(float, t.split()))
    return [v[0:3], v[3:6], v[6:9]], v[9:12]


def apply(m, p):
    r, t = m
    return tuple(p[0] * r[0][i] + p[1] * r[1][i] + p[2] * r[2][i] + t[i] for i in range(3))


def group_of(name):
    """senso1 / Text1 -> half1, senso2 / text2 -> half2, screw -> screw."""
    n = name.lower()
    if "screw" in n:
        return "screw"
    m = re.search(r"(?:senso|text)_?(\d)", n)
    if not m:
        sys.exit(f"Error: don't know which half part '{name}' belongs to")
    return f"half{m.group(1)}"


def main(src, outdir):
    z = zipfile.ZipFile(src)
    model = z.read("3D/3dmodel.model").decode()
    settings = z.read("Metadata/model_settings.config").decode()
    names = dict(re.findall(r'<part id="(\d+)"[^>]*>\s*<metadata key="name" value="([^"]+)"', settings))

    # First assembly on the plate: an object made of components.
    asm = re.search(r'<object id="(\d+)"[^>]*>\s*<components>(.*?)</components>', model, re.S)
    if not asm:
        sys.exit("Error: no multi-part object found in this 3mf")
    item = re.search(rf'<item objectid="{asm.group(1)}"[^>]*?transform="([^"]+)"', model)
    placed = mat(item.group(1)) if item else mat("1 0 0 0 1 0 0 0 1 0 0 0")

    groups = {}
    for oid, t in re.findall(r'<component objectid="(\d+)"[^>]*?transform="([^"]+)"', asm.group(2)):
        body = re.search(rf'<object id="{oid}"[^>]*>(.*?)</object>', model, re.S).group(1)
        v = [tuple(map(float, p)) for p in re.findall(r'<vertex x="([^"]+)" y="([^"]+)" z="([^"]+)"', body)]
        comp = mat(t)
        w = [apply(placed, apply(comp, p)) for p in v]
        tris = [(w[int(a)], w[int(b)], w[int(c)]) for a, b, c in
                re.findall(r'<triangle v1="(\d+)" v2="(\d+)" v3="(\d+)"', body)]
        name = names.get(oid, f"object {oid}")
        groups.setdefault(group_of(name), []).append((name, tris))

    os.makedirs(outdir, exist_ok=True)
    for g, parts in sorted(groups.items()):
        tris = [t for _, ts in parts for t in ts]
        pts = [p for t in tris for p in t]
        lo = [min(p[i] for p in pts) for i in range(3)]
        hi = [max(p[i] for p in pts) for i in range(3)]
        off = (-(lo[0] + hi[0]) / 2, -(lo[1] + hi[1]) / 2, -lo[2])
        path = os.path.join(outdir, f"{g}.stl")
        with open(path, "wb") as f:
            f.write(b"\0" * 80 + struct.pack("<I", len(tris)))
            for t in tris:
                f.write(struct.pack("<12fH", 0, 0, 0, *(c + o for p in t for c, o in zip(p, off)), 0))
        size = " x ".join(f"{hi[i] - lo[i]:.1f}" for i in range(3))
        print(f"  {path}: {size} mm  <- {', '.join(n for n, _ in parts)}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
