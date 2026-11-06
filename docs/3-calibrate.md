[עברית](he/3-calibrate.md)

# Step 3 - Calibrate your printer and filament

**Calibrate** means: tune the settings so they match your printer. Every
printer and every spool of plastic is a little different. These short test
prints find the right numbers for **yours**. Do them once for each printer.
Do them again when you switch to a different brand of filament.

All the tests are built into OrcaSlicer, in the top menu **Calibration**. Each
test opens a new plate (a new empty work area). So **save your current
project first**, if you have one.

| # | Test | Time | What it fixes |
|---|---|---|---|
| 0 | Get ready | 10 min | everything else |
| 1 | Temperature tower | ~30 min | thin hairs (stringing), weak layers |
| 2 | Flow rate (2 rounds) | ~40 min | gaps or bumps on the top surfaces |
| 3 | Retraction test | ~25 min | hairs between the spikes |
| 4 | Fit test (print one half + the screw) | ~2.5 h | screw too tight or too loose |

**How to save a result:**

1. Next to the **Filament** box, click the **edit** (pencil) icon.
2. Change the value.
3. Click the **save** icon at the top of that window.
4. Keep the same name.

Every test below ends with this.

---

## 0. Get ready

1. **Dry the filament if the spool has been open for weeks.** Plastic soaks up
   water from the air. Damp PLA makes hairs at every setting, and then you
   can't read any of the tests below. Dry it for 4-6 hours at 45-50 °C in a
   filament dryer or a food dehydrator. Or: put the spool on the printer's bed
   (the flat plate it prints on) at 60 °C, under an upside-down cardboard box.
   Quick check: bend 10 cm of filament. Dry PLA bends. Damp PLA snaps.
2. **Clean the bed** with a little rubbing alcohol. (If your bed is textured
   PEI - a rough-feeling sheet - use dish soap and water instead.) After that,
   don't touch it with your fingers.
3. **Level the bed.** This means: make the nozzle the same small distance from
   the bed in every corner. Do this on the Ender 3 and other printers that
   can't level by themselves:
   - Heat the bed to 60 °C and the nozzle to 200 °C.
   - On the printer's screen, choose **Prepare → Auto Home**, then
     **Prepare → Disable steppers**. Now you can move the nozzle by hand.
   - Move the nozzle by hand over one corner.
   - Slide a sheet of plain paper under the nozzle.
   - Turn that corner's knob until the paper drags a little when you move it.
   - Do this for all four corners. Then do all four again. Then check the
     middle.

## 1. Temperature tower

This test prints a tower of blocks, each one at a different temperature, so
you can see which temperature works best.

1. Click **Calibration → Temperature**.
2. Choose **PLA**. Set **Start 220**, **End 190**, **Step 5**. Click **OK**.
3. Click **Slice plate**.
4. Send it to the printer (see
   [Step 4 - Sending the file](4-print.md#sending-the-file-to-the-printer)).
5. Each block prints hotter or cooler. Its temperature is written on it.

**Choosing:** look at the gap between the two pillars of each block. Pick the
**coolest block with no hairs and a smooth surface**. Then try to snap that
block off the tower with your fingers. If it breaks easily between layers,
use the next hotter block instead.

**Save:** in the Filament settings, set the **Nozzle** temperature. Set
**Initial layer** about 10 °C hotter - the first layer sticks to the bed
better when it's hotter.

> On our Ender 3 Pro: 225 and 215 made lots of hairs, 205 had small blobs, 195
> and 190 were clean. We picked 195.

## 2. Flow rate

Flow rate is how much plastic comes out of the nozzle, compared to how much
the slicer asks for. Too much makes bumps. Too little makes gaps.

1. Click **Calibration → Flow rate → Pass 1**. Slice and print.
   You get 9 squares. Each one has a number on it, from -20 to +20.
2. Look at the **top surfaces** in good light. Run a finger over them.
3. Pick the smoothest one - no gaps between lines, no ridges.
4. Click **Calibration → Flow rate → Pass 2**. Slice and print.
5. Pick the smoothest square again (these have numbers from -9 to 0).
6. **Calculate:** new flow = current flow × (100 + the number you picked) ÷ 100.
   Example: flow 0.98, you picked -2 → 0.98 × 98 ÷ 100 = 0.96.
   OrcaSlicer's flow rate window explains the same formula.

**Save:** in the Filament settings, set **Flow ratio**.

## 3. Retraction test

Retraction means the printer pulls the plastic back a little before the
nozzle moves to a new spot. This stops melted plastic from dripping and
leaving thin hairs. The ball's spikes make **thousands** of these moves, so
this test matters a lot.

1. Click **Calibration → Retraction test**.
2. Set the range for your printer. "Bowden" printers have a long tube between
   the motor and the nozzle. "Direct drive" printers have the motor right on
   top of the nozzle.

   | Printer type | Start | End | Step |
   |---|---|---|---|
   | Bowden tube (Ender 3, Ender 3 Pro/V2, CR-10) | 2 | 7 | 0.5 |
   | Direct drive (Ender 3 V3, K1, Bambu, Prusa) | 0 | 2 | 0.2 |

3. Slice and print. The higher the tower gets, the more the plastic is pulled
   back. The value changes every 1 mm of height (the window shows this).
4. Find the **lowest point where the hairs stop**.
5. Measure how high that point is above the base, in mm, with a ruler.
6. Calculate: retraction = Start + height × Step. Example: 6 mm up, start 2,
   step 0.5 → 2 + 6 × 0.5 = **5 mm**.
7. Use the **shortest** clean value. Pulling back more than needed wears out
   the filament and can block the nozzle.

**Save:** in the Filament settings, set **Retraction length** (under
**Setting overrides**).

**Still getting hairs at every value?**

1. Dry the filament (see step 0). This is the most common cause.
2. Lower the temperature by 5 °C.
3. Ender 3 family: check the white tube (PTFE) where it goes into the hot end
   (the hot part that holds the nozzle). If its tip is brown or cut at an
   angle, cut it straight. Heat the hot end. Push the tube firmly down into
   the nozzle while it's hot. Then put the clip back.
4. A few thin hairs are normal on a spiky ball. A hair dryer on hot, or a
   quick pass with a heat gun, removes them in seconds.

## 4. Fit test

The screw threads are the only part of the ball that must be exact. Before
you print a whole ball, print **one half and the screw** (about 2.5 hours, see
[Step 4](4-print.md)). Then try to screw them together.

| Result | Fix (Process → **Quality** → **Precision**) |
|---|---|
| Screws in smoothly, holds tight | done - print the second half |
| Too tight / won't go in | **X-Y hole compensation** → `0.1`, print the half again |
| Loose / wobbles | **X-Y contour compensation** → `0.05`, print the screw again |

Change the value by 0.05 mm at a time. Save it in the **process** preset (the
save icon next to the process box).

---

## Not needed for the ball

- **Pressure advance** - skip. The Ender 3's built-in software ignores it, and
  Bambu printers set it by themselves.
- **Max flowrate** - skip. The ball prints far below any printer's limit.

Next: [Step 4 - Print and assemble the ball](4-print.md)
