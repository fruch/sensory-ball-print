[עברית](he/1-install.md)

# Step 1 - Install OrcaSlicer

A 3D printer can't read a 3D model directly. A **slicer** is a program that
cuts the model into thin layers and turns them into instructions the printer
understands (a `.gcode` file). This guide uses **OrcaSlicer**. It is free,
works on Windows, Mac and Linux, and has the test prints built in.

Use version **2.4.2** (the current stable version). 2.5.0 also works.

## Download

1. Go to the [OrcaSlicer 2.4.2 download page](https://github.com/OrcaSlicer/OrcaSlicer/releases/tag/v2.4.2).
2. Scroll down to **Assets**.
3. Click the file for your computer:

| Your computer | File to download |
|---|---|
| Windows (almost all PCs) | `OrcaSlicer_Windows_Installer_V2.4.2_x64.exe` |
| Windows on ARM (e.g. Surface Pro X, Snapdragon laptops) | `OrcaSlicer_Windows_Installer_V2.4.2_arm64.exe` |
| Mac (Intel or Apple M1/M2/M3/M4) | `OrcaSlicer_Mac_universal_V2.4.2.dmg` |
| Linux | `OrcaSlicer_Linux_AppImage_Ubuntu2404_V2.4.2.AppImage` |

You don't need the other files on that page.

## Install

### Windows

1. Double-click the `.exe` file you downloaded.
2. Maybe a blue box says **"Windows protected your PC"**. If so, click
   **More info**, then **Run anyway**. (OrcaSlicer is safe. Microsoft just
   hasn't signed it.)
3. Keep clicking **Next**, then click **Finish**.
4. Open **OrcaSlicer** from the Start menu.

### Mac

1. Double-click the `.dmg` file you downloaded.
2. Drag the **OrcaSlicer** icon onto the **Applications** folder.
3. Open **Applications** and double-click **OrcaSlicer**.
4. Maybe macOS says it **cannot be opened** or **can't verify the developer**.
   If so, open **System Settings → Privacy & Security**. Scroll down and click
   **Open Anyway** next to the OrcaSlicer message. Type your password to
   confirm.

### Linux

1. Right-click the `.AppImage` file you downloaded → **Properties** →
   **Permissions** → tick **Allow executing file as program**.
2. Double-click it.

## First start: tell Orca about your printer

The first time OrcaSlicer opens, a **setup wizard** appears. It asks a few
questions, one page at a time.

1. **Login** page: click **Skip**. You don't need an account.
2. **Printer** page: find your printer's brand (e.g. **Creality**). Tick your
   model, for example **Ender-3 Pro**, with nozzle **0.4**. (The nozzle is the
   hot metal tip the melted plastic comes out of.)
3. **Filament** page: make sure **Generic PLA** is ticked.
4. Click **Finish**.

Missed the wizard? You can add a printer later. Click the gear icon next to
the printer name (top left, in the **Printer** box).

Next: [Step 2 - Load this project's settings](2-presets.md)
