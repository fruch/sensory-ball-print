# Step 2 - Load this project's settings

Presets are saved settings. This project has two per printer:

- a **filament** preset - temperatures and retraction for PLA on that printer
- a **process** preset - how the ball is printed (walls, travel moves)

## Download the presets

1. On this project's GitHub page, click the green **Code** button →
   **Download ZIP**.
2. Unzip it (Windows: right-click → **Extract All**; Mac: double-click).
3. Open the `presets` folder, then the folder for your printer, e.g.
   `creality-ender-3-pro`. It has two `.json` files.

No folder for your printer yet? Skip this page - use OrcaSlicer's own
**Generic PLA** and **0.20mm Standard** presets and go to Step 3. The
calibration will tune them for your machine.

## Import them into OrcaSlicer

1. In OrcaSlicer: **File → Import → Import Configs...**
2. Select **both** `.json` files from your printer's folder and click **Open**.
3. OrcaSlicer says the presets were imported.

## Select them

At the top left of the **Prepare** tab:

1. **Printer**: your printer, e.g. `Creality Ender-3 Pro 0.4 nozzle`.
2. **Filament**: click the filament box and choose
   `PLA Sensory Ball @Ender3Pro` (under **User presets**).
3. **Process** (the box on the right side, top): choose
   `Sensory Ball 0.20mm @Ender3Pro`.

Can't see them? They only show when the matching printer is selected - check
step 1.

## What's in them (Ender 3 Pro)

| Setting | Value | Why |
|---|---|---|
| Nozzle temperature | 195 °C (205 °C first layer) | lower temperature = fewer hairs between spikes |
| Retraction | 5 mm at 40 mm/s | Bowden-tube printers need long retraction |
| Wipe / Z-hop | off / off | both made stringing worse in our tests |
| Walls | 3 | threads and spike tips are nearly all wall - 3 makes them solid |
| Avoid crossing walls | on | travel moves stay over the part instead of drawing strings through the air |

These are **starting values**. Step 3 replaces the first four with numbers
measured on *your* printer and *your* filament.

Next: [Step 3 - Calibrate](3-calibrate.md)
