[עברית](he/2-presets.md)

# Step 2 - Load this project's settings

A **preset** is a saved group of settings, so you don't have to type them in
yourself. This project has two presets for each printer:

- a **filament** preset - how hot to melt the plastic, and how far to pull it
  back between moves (this is called retraction)
- a **process** preset - how the ball is printed (how thick the outer walls
  are, and how the nozzle moves between spots)

## Download the presets

1. On this project's GitHub page, click the green **Code** button →
   **Download ZIP**.
2. Unzip the file. On Windows: right-click → **Extract All**. On Mac:
   double-click.
3. Open the `presets` folder.
4. Open the folder for your printer, for example `creality-ender-3-pro`. It
   has two `.json` files.

No folder for your printer yet? Skip this page. Use OrcaSlicer's own
**Generic PLA** and **0.20mm Standard** presets and go to Step 3. The test
prints will tune them for your printer.

## Import them into OrcaSlicer

1. In OrcaSlicer, click **File → Import → Import Configs...**
2. Select **both** `.json` files from your printer's folder.
3. Click **Open**.
4. OrcaSlicer tells you the presets were imported.

## Select them

Go to the **Prepare** tab. At the top left:

1. **Printer**: choose your printer, for example `Creality Ender-3 Pro 0.4 nozzle`.
2. **Filament**: click the filament box and choose
   `PLA Sensory Ball @Ender3Pro` (under **User presets**).
3. **Process** (the box on the right side, at the top): choose
   `Sensory Ball 0.20mm @Ender3Pro`.

Can't see them? They only show up when the right printer is selected. Check
step 1.

## What's in them (Ender 3 Pro)

| Setting | Value | Why |
|---|---|---|
| Nozzle temperature | 195 °C (205 °C first layer) | cooler plastic = fewer thin hairs between the spikes |
| Retraction (pulling the plastic back) | 5 mm at 40 mm/s | printers with a long tube between the motor and the nozzle (called Bowden) need to pull back further |
| Wipe / Z-hop | off / off | both made more hairs in our tests |
| Walls | 3 | the screw threads and spike tips are almost all wall - 3 walls make them strong |
| Avoid crossing walls | on | the nozzle moves over the part, not through the air, so it doesn't leave strings |

These are **starting values**. In Step 3 you replace the first four with
numbers you measure on *your* printer and *your* filament.

Next: [Step 3 - Calibrate](3-calibrate.md)
