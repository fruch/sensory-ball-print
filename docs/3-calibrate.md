# Step 3 - Calibrate your printer and filament

Every printer and every spool behaves a little differently. These short test
prints find the right numbers for **yours**. Do them once per printer, and
again when you switch to a different brand of filament.

All tests are built into OrcaSlicer: top menu **Calibration**. Each one
creates a new test plate - **save your current project first** if you have one.

| # | Test | Time | What it fixes |
|---|---|---|---|
| 0 | Get ready | 10 min | everything else |
| 1 | Temperature tower | ~30 min | stringing, weak layers |
| 2 | Flow rate (2 passes) | ~40 min | gaps or bumps on top surfaces |
| 3 | Retraction test | ~25 min | stringing between the spikes |
| 4 | Fit test (print one half + screw) | ~2.5 h | screw too tight or too loose |

**How to save a result:** next to the **Filament** box click the **edit**
(pencil) icon, change the value, then click the **save** icon at the top of
that window and keep the same name. Every test below ends with this.

---

## 0. Get ready

1. **Dry the filament if the spool has been open for weeks.** Damp PLA
   strings at every setting and makes every test below unreadable. 4-6 hours
   at 45-50 °C in a filament dryer or food dehydrator - or put the spool on the
   bed at 60 °C under an upturned cardboard box.
   Quick check: bend 10 cm of filament. Dry PLA bends; damp PLA snaps.
2. **Clean the bed** with a little rubbing alcohol (or dish soap and water for
   textured PEI). Don't touch it with your fingers afterwards.
3. **Level the bed** (Ender 3 and other printers without automatic leveling):
   - Heat the bed to 60 °C and the nozzle to 200 °C.
   - **Prepare → Auto Home**, then **Prepare → Disable steppers**.
   - Move the nozzle by hand over each corner. Slide a sheet of plain paper
     under it and turn that corner's knob until the paper drags slightly.
   - Go round all four corners twice, then check the middle.

## 1. Temperature tower

1. **Calibration → Temperature**.
2. Choose **PLA**. Set **Start 220**, **End 190**, **Step 5**. Click **OK**.
3. **Slice plate**, then send it to the printer (see
   [Step 4 - Sending the file](4-print.md#sending-the-file-to-the-printer)).
4. Each block is printed hotter or cooler, and its temperature is printed on it.

**Choosing:** look at the gap between the two pillars of each block.
Pick the **coolest block with no hairs and a smooth surface**. Then try to
snap that block off the tower with your fingers - if it breaks easily between
layers, use the next block hotter.

**Save:** Filament → **Nozzle** temperature (and **Initial layer** about 10 °C
hotter for better sticking).

> On our Ender 3 Pro: 225 and 215 strung badly, 205 had small blobs, 195 and
> 190 were clean. We picked 195.

## 2. Flow rate

Flow rate is how much plastic comes out compared to what the slicer asks for.

1. **Calibration → Flow rate → Pass 1**. Slice and print.
   You get 9 squares, each labeled with a number from -20 to +20.
2. Look at the **top surfaces** in good light. Run a finger over them.
   Pick the smoothest one - no gaps between lines, no ridges.
3. **Calibration → Flow rate → Pass 2**. Slice and print. Pick the smoothest
   square again (labeled -9 to 0).
4. **Calculate:** new flow = current flow × (100 + the number you picked) ÷ 100.
   Example: flow 0.98, you picked -2 → 0.98 × 98 ÷ 100 = 0.96.
   OrcaSlicer's flow rate dialog explains the same formula.

**Save:** Filament → **Flow ratio**.

## 3. Retraction test

Retraction pulls the filament back before each travel move so the nozzle
doesn't leak. The ball's spikes make **thousands** of travel moves, so this
test matters more than usual.

1. **Calibration → Retraction test**.
2. Set the range for your printer:

   | Printer type | Start | End | Step |
   |---|---|---|---|
   | Bowden tube (Ender 3, Ender 3 Pro/V2, CR-10) | 2 | 7 | 0.5 |
   | Direct drive (Ender 3 V3, K1, Bambu, Prusa) | 0 | 2 | 0.2 |

3. Slice and print. The tower gets taller as the retraction gets longer.
   The value changes every 1 mm of height (the dialog shows this).
4. Find the **lowest point where the strings stop**. Measure its height from
   the base in mm with a ruler.
   Retraction = Start + height × Step. Example: 6 mm up, start 2, step 0.5 →
   2 + 6 × 0.5 = **5 mm**.
5. Use the **shortest** clean value. More than needed wears the filament and
   can clog.

**Save:** Filament → **Retraction length** (under **Setting overrides**).

**Still stringing at every value?**

1. Dry the filament (see step 0) - this is the most common cause.
2. Lower the temperature by 5 °C.
3. Ender 3 family: check the white tube (PTFE) at the hot end. If its tip is
   brown or not cut square, trim it flat and push it firmly down into the
   nozzle while the hot end is hot, then refit the clip.
4. A few thin hairs are normal on a spiky ball - a hair dryer on hot, or a
   quick pass with a heat gun, removes them in seconds.

## 4. Fit test

The threads are the one part of the ball that must be accurate. Before
printing a whole ball, print **one half and the screw** (about 2.5 hours, see
[Step 4](4-print.md)) and try screwing them together.

| Result | Fix (Process → **Quality** → **Precision**) |
|---|---|
| Screws in smoothly, holds tight | done - print the second half |
| Too tight / won't go in | **X-Y hole compensation** → `0.1`, reprint the half |
| Loose / wobbles | **X-Y contour compensation** → `0.05`, reprint the screw |

Change in steps of 0.05 mm. Save it in the **process** preset (the save icon
next to the process box).

---

## Not needed for the ball

- **Pressure advance** - skip. Stock Ender 3 firmware ignores it; Bambu
  printers calibrate it automatically.
- **Max flowrate** - skip. The ball prints well below any printer's limit.

Next: [Step 4 - Print and assemble the ball](4-print.md)
