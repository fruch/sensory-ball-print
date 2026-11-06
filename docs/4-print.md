# Step 4 - Print and assemble the ball

## 1. Get matching parts

Download the three files from the designer's page (_link coming soon_):
two halves and the screw, **all the same version and size**.

| Good | Bad |
|---|---|
| `senso1_51mm_V12` + `senso2_51mm_V12` + **V12** screw | a 51 mm half with a 47 mm half |
| | a **V11** screw with **V12** halves - its thread is 0.9 mm too big |

Both of these mistakes print without errors and then don't fit together.
If you can run Python, `tools/check_fit.py` checks the files for you - see
[Checking the files](#optional-checking-the-files-before-printing) below.

## 2. Load them

1. OrcaSlicer → **Prepare** tab.
2. Check the three boxes at the top left: your printer, the
   `PLA Sensory Ball` filament, the `Sensory Ball 0.20mm` process
   ([Step 2](2-presets.md)).
3. Drag all three `.stl` files onto the build plate (or **File → Import →
   Import 3MF/STL...**).
4. If OrcaSlicer asks **"load as a single object with multiple parts?"** -
   click **No**.
5. Press **A** (or the **Arrange** button) to space them out.

The halves must sit **flat side down** (spikes up) and the screw **on its
side**. That's how the files come. If something looks rotated, select it and
use **Lay on face** (the **F** key), then click its flat side.

No supports are needed - leave **Support** off.

## 3. Slice

Click **Slice plate** (top right). On an Ender 3 Pro you should see about
**4 h 30 m** and **29-31 g** for all three parts.

## Sending the file to the printer

**Ender 3 / printers with a microSD card:**

1. Put the printer's microSD card into your computer (use an adapter if needed).
2. Click **Export G-code file** (the arrow next to **Print plate**) and save
   it onto the card.
3. Eject the card safely, put it in the printer, and choose the file from
   **Print from TF/SD**.

**Bambu / Wi-Fi printers:** click **Print plate** and choose your printer.

## While it prints

- **Watch the first layer** (the first few minutes). Lines should be slightly
  flattened and stuck down, with no gaps between them. If they curl or don't
  stick: stop, re-level ([Step 3](3-calibrate.md#0-get-ready)) and start again.
- Remove the parts after the bed cools down - they come off much more easily.

## Assemble

1. Remove any hairs between the spikes: a hair dryer on hot, or a quick pass
   with a heat gun, from about 10 cm away. Don't stay on one spot.
2. Screw the connector fully into one half.
3. Screw the second half onto the other end until the two flat faces meet.

Too tight or too loose? See the [fit test](3-calibrate.md#4-fit-test).

## Optional: checking the files before printing

`tools/check_fit.py` measures the downloaded files and tells you whether they
fit together. It needs Python 3:

- **Windows:** install **Python 3** from the Microsoft Store.
- **Mac:** open **Terminal** and type `python3` - if it's missing, macOS
  offers to install it.
- **Linux:** already installed.

Then, in the folder where you unzipped this project, run:

```
python3 tools/check_fit.py half1.stl half2.stl screw.stl
```

(On Windows type `python` instead of `python3`.) Tip: you can drag a file
from your file manager into the terminal window to paste its full path.

It ends with **"OK: these parts fit together."** or tells you which file is wrong.
