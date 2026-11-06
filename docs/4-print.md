[עברית](he/4-print.md)

# Step 4 - Print and assemble the ball

## 1. Get matching parts

Get the three files from the [Pastrami Angel](https://pastrami-angel.com/)
team (they are shared privately for now): two halves **of the same size**,
and the screw.

| Good | Bad |
|---|---|
| `senso1_51mm_V12` + `senso2_51mm_V12` + `Sensory Screw V11` | a 51 mm half with a 47 mm half |

All sizes use the same screw thread. So two halves of different sizes still
screw together - but the ball comes out lopsided.

**Only have the multi-colour project (a `.3mf` file with text parts)?** If
your printer prints one colour, `tools/extract_ball.py` can pull one ball out
of it. You get `half1.stl`, `half2.stl` and `screw.stl`, with the text joined
into each half. (See [Checking the files](#optional-checking-the-files-before-printing)
for how to run Python.)

```
python3 tools/extract_ball.py "Sanso 51 U1.3mf" model
```

If you can run Python, `tools/check_fit.py` can check the files for you - see
[Checking the files](#optional-checking-the-files-before-printing) below.

## 2. Load them

1. In OrcaSlicer, open the **Prepare** tab.
2. Check the three boxes at the top left: your printer, the
   `PLA Sensory Ball` filament, and the `Sensory Ball 0.20mm` process
   ([Step 2](2-presets.md)).
3. Drag all three `.stl` files onto the build plate (or use **File → Import →
   Import 3MF/STL...**).
4. If OrcaSlicer asks **"load as a single object with multiple parts?"** -
   click **No**.
5. Press **A** (or click the **Arrange** button) to spread them out.

The halves must sit **flat side down** (spikes up). The screw must lie **on
its side**. That's how the files come. If something looks turned the wrong
way, select it and use **Lay on face** (the **F** key). Then click its flat
side.

You don't need supports - leave **Support** off.

## 3. Slice

Click **Slice plate** (top right). This turns the model into printer
instructions. On an Ender 3 Pro you should see about **4 h 30 m** and
**29-31 g** for all three parts.

## Sending the file to the printer

**Ender 3 / printers with a microSD card:**

1. Put the printer's microSD card into your computer (use an adapter if
   needed).
2. Click **Export G-code file** (the arrow next to **Print plate**).
3. Save the file onto the card.
4. Eject the card safely and put it in the printer.
5. Choose the file from **Print from TF/SD**.

**Bambu / Wi-Fi printers:** click **Print plate** and choose your printer.

## While it prints

- **Watch the first layer** (the first few minutes). The lines should be a
  little flat and stuck to the bed, with no gaps between them. If they curl
  up or don't stick: stop the print, level the bed again
  ([Step 3](3-calibrate.md#0-get-ready)) and start over.
- Wait for the bed to cool down before you take the parts off. They come off
  much more easily.

## Assemble

1. Remove any hairs between the spikes. Use a hair dryer on hot, or a quick
   pass with a heat gun, from about 10 cm away. Keep it moving - don't stay
   on one spot.
2. Screw the screw all the way into one half.
3. Screw the second half onto the other end, until the two flat sides touch.

Too tight or too loose? See the [fit test](3-calibrate.md#4-fit-test).

## Optional: checking the files before printing

`tools/check_fit.py` measures the files you downloaded and tells you if they
fit together. It needs Python 3 (a free program):

- **Windows:** install **Python 3** from the Microsoft Store.
- **Mac:** open **Terminal** and type `python3`. If it's missing, macOS
  offers to install it.
- **Linux:** it's already installed.

Then open a terminal in the folder where you unzipped this project, and run:

```
python3 tools/check_fit.py half1.stl half2.stl screw.stl
```

(On Windows, type `python` instead of `python3`.) Tip: you can drag a file
from your folder window into the terminal window. That pastes its full path.

At the end it says **"OK: these parts fit together."** or tells you which file
is wrong.
