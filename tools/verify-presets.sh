#!/usr/bin/env bash
# Maintainers only: prove a printer's presets load and slice the ball cleanly.
#
#   tools/verify-presets.sh <orca-appimage> <printer-dir> <model files...>
#   tools/verify-presets.sh ~/Downloads/OrcaSlicer_*.AppImage presets/creality-ender-3-pro \
#       ~/Downloads/senso1_51mm_V12_mono.stl ~/Downloads/senso2_51mm_V12_mono.stl ~/Downloads/screw.stl
#
# Orca 2.5's CLI only resolves user presets that are installed in its data
# folder, so this builds a throwaway one: a copy of your system presets plus
# this repo's presets under user/default/. Your real Orca config is untouched.
# --strict fails the run on warnings such as "this model needs support".
set -Eeuo pipefail

ORCA="${1:?orca appimage}"; PRINTER_DIR="${2:?presets/<printer> dir}"; shift 2
(( $# )) || { echo "Error: give at least one model file" >&2; exit 1; }
SYS="${ORCA_SYSTEM:-$HOME/.config/OrcaSlicer/system}"
[[ -d "$SYS" ]] || { echo "Error: no Orca system presets at $SYS - open Orca once first" >&2; exit 1; }

WORK="$(mktemp -d)"; trap 'rm -rf "$WORK"' EXIT
mkdir -p "$WORK/data/user/default/filament" "$WORK/data/user/default/process" "$WORK/out"
cp -r "$SYS" "$WORK/data/system"

FILAMENT=""; PROCESS=""; MACHINE=""
for f in "$PRINTER_DIR"/*.json; do
    type=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["type"])' "$f")
    cp "$f" "$WORK/data/user/default/$type/"
    case "$type" in
      filament) FILAMENT="$WORK/data/user/default/filament/$(basename "$f")" ;;
      process)
        PROCESS="$WORK/data/user/default/process/$(basename "$f")"
        printer=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["compatible_printers"][0])' "$f")
        MACHINE=$(find "$WORK/data/system" -path "*/machine/$printer.json" | head -1) ;;
    esac
done
[[ -n "$FILAMENT" && -n "$PROCESS" && -n "$MACHINE" ]] || { echo "Error: need a filament and a process preset in $PRINTER_DIR" >&2; exit 1; }

# The Creality Ender chain leaves use_relative_e_distances unset, and the CLI
# (not the GUI) then refuses to slice without a G92 E0 at each layer change.
"$ORCA" --datadir "$WORK/data" --load-settings "$MACHINE;$PROCESS" --load-filaments "$FILAMENT" \
    --layer-change-gcode $'G92 E0\n' --strict --export-statistics \
    --slice 0 --arrange 1 --outputdir "$WORK/out" "$@" >"$WORK/log" 2>&1 || { cat "$WORK/log" >&2; exit 1; }

python3 - "$WORK/out" <<'PY'
import json, sys
out = sys.argv[1]
r = json.load(open(f"{out}/result.json"))
if r["return_code"] != 0 or r.get("warnings"):
    sys.exit(f"Error: slice failed: {r['error_string']} {r.get('warnings')}")
s = json.load(open(f"{out}/plate_1.statistics.json"))["summary"]
g = open(f"{out}/plate_1.gcode").read(400_000)
want = {"nozzle_temperature": None, "filament_retraction_length": None, "filament_wipe": None,
        "wall_loops": None, "reduce_crossing_wall": None}
for line in open(f"{out}/plate_1.gcode"):
    for k in want:
        if line.startswith(f"; {k} = "):
            want[k] = line.split("=", 1)[1].strip()
t = int(s["time"])
print(f"OK  {t // 3600}h {t % 3600 // 60}m, {s['weight']:.1f} g, no warnings")
print("    " + ", ".join(f"{k}={v}" for k, v in want.items()))
PY
