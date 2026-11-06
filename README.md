# Sensory Ball - print guide for volunteers

Step-by-step help for printing the **spiky sensory ball** on a home 3D printer
and getting a good result: ready-made slicer settings, a short calibration
routine, and a parts check so you don't spend 5 hours printing pieces that
don't fit.

This guide is part of a charity effort: [Pastrami Angel](https://pastrami-angel.com/).

The ball is three printed parts: **two spiky halves** and a **threaded
connector (screw)** that joins them. On a Creality Ender 3 Pro the whole set
takes about **4.5 hours** and **30 g of PLA**, with no supports.

## You will need

- A 3D printer. Tested: **Creality Ender 3 Pro**. Other printers work with the
  general calibration steps; tested presets for more printers are on the way.
- PLA filament, 1.75 mm.
- A computer - Windows, Mac or Linux.
- About 1.5 hours for the one-time calibration, then about 4.5 hours per ball.

## Steps

| # | Step | Time |
|---|---|---|
| 1 | [Install the slicer (OrcaSlicer)](docs/1-install.md) | 10 min |
| 2 | [Load this project's settings](docs/2-presets.md) | 5 min |
| 3 | [Calibrate your printer and filament](docs/3-calibrate.md) - once per printer + filament | about 1.5 h, mostly waiting |
| 4 | [Print and assemble the ball](docs/4-print.md) | about 4.5 h printing |

Never used a 3D printer or a slicer before? Start at step 1 and follow every
step in order - each page says exactly what to click.

## Getting the model

The model files are not stored here. Download them from the designer's page:
_link coming soon_.

You need **two halves of the same size** plus the screw, e.g. for the 51 mm
ball: `senso1_51mm_V12_mono.stl`, `senso2_51mm_V12_mono.stl` and
`Sensory Screw V11.stl` (the V11 screw is the current one and fits the V12
halves). Mixing sizes is the most common mistake - the pieces print fine but
won't make a round ball. Step 4 shows how to check.

## Printer status

| Printer | Presets | Status |
|---|---|---|
| Creality Ender 3 Pro | `presets/creality-ender-3-pro/` | tested |
| Creality Ender 3 / Ender 3 V2 | use the Ender 3 Pro presets as a start | untested |
| Creality K1 / Ender 3 V3 | coming | - |
| Bambu Lab A1 / P1S / X1C / H2S | coming | - |

## For maintainers

- `tools/check_fit.py` - checks downloaded parts fit together (any OS, plain Python 3).
- `tools/verify-presets.sh` - slices the ball with a printer's presets in a
  throwaway Orca data folder and fails on any warning (Linux, OrcaSlicer 2.5+).
  Adding a printer means: add `presets/<printer>/`, run this, print one ball,
  update the table above.

## Licence

The guide, presets and tools are MIT licensed - see [LICENSE](LICENSE). The
ball model belongs to its designer and is not included.
