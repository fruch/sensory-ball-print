[עברית](README.he.md)

# Sensory Ball - print guide for volunteers

This guide shows you, step by step, how to print the **spiky sensory ball** on
a 3D printer at home. You get ready-made settings, a short set of test prints
to tune your printer, and a check that the parts fit - so you don't spend
5 hours printing pieces that don't go together.

This guide is part of a charity project: [Pastrami Angel](https://pastrami-angel.com/).

The ball has three printed parts: **two spiky halves** and a **screw** (a
threaded connector) that holds them together. On a Creality Ender 3 Pro
printer, all three parts take about **4 hours** and use **30 g of PLA**
plastic. You don't need supports (extra helper plastic that holds up
overhanging parts).

## What you need

- A 3D printer. We tested on a **Creality Ender 3 Pro**. Other printers work
  too if you do the general test prints. Tested settings for more printers are
  coming.
- **Filament** - the plastic "string" on a spool that the printer melts. Use
  PLA, 1.75 mm thick.
- A computer - Windows, Mac or Linux.
- About 1.5 hours for the test prints (you do them only once), then about
  4 hours for each ball.

## Steps

| # | Step | Time |
|---|---|---|
| 1 | [Install the slicer (OrcaSlicer)](docs/1-install.md) | 10 min |
| 2 | [Load this project's settings](docs/2-presets.md) | 5 min |
| 3 | [Tune your printer and filament](docs/3-calibrate.md) - once per printer + filament | about 1.5 h, mostly waiting |
| 4 | [Print and put the ball together](docs/4-print.md) | about 4 h printing |

Optional: [Setting up Python](docs/tools-setup.md) - only needed for the
helper tools that check or convert the model files (Windows, Mac, Linux).

New to 3D printing? No problem. Start at step 1 and do every step in order.
Each page tells you exactly what to click.

## Getting the model

The model is the 3D shape of the ball. Its files are not stored here - for
now they are shared privately. Ask the [Pastrami Angel](https://pastrami-angel.com/)
team for them.

You need **two halves of the same size** plus the screw. For example, for
the 51 mm ball: `senso1_51mm_V12_mono.stl`, `senso2_51mm_V12_mono.stl` and
`Sensory Screw V11.stl`. (The V11 screw is the newest one, and it fits the V12
halves.) The most common mistake is mixing sizes. The pieces print fine, but
they don't make a round ball. Step 4 shows how to check.

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
