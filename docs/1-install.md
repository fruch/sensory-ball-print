# Step 1 - Install OrcaSlicer

A **slicer** turns a 3D model into instructions your printer understands
(a `.gcode` file). This guide uses **OrcaSlicer**: free, works on Windows, Mac
and Linux, and has the calibration tests built in.

Use version **2.4.2** (the current stable release). 2.5.0 also works.

## Download

Go to the [OrcaSlicer 2.4.2 download page](https://github.com/OrcaSlicer/OrcaSlicer/releases/tag/v2.4.2),
scroll down to **Assets**, and click the file for your computer:

| Your computer | File to download |
|---|---|
| Windows (almost all PCs) | `OrcaSlicer_Windows_Installer_V2.4.2_x64.exe` |
| Windows on ARM (e.g. Surface Pro X, Snapdragon laptops) | `OrcaSlicer_Windows_Installer_V2.4.2_arm64.exe` |
| Mac (Intel or Apple M1/M2/M3/M4) | `OrcaSlicer_Mac_universal_V2.4.2.dmg` |
| Linux | `OrcaSlicer_Linux_AppImage_Ubuntu2404_V2.4.2.AppImage` |

Ignore the other files on that page.

## Install

### Windows

1. Double-click the downloaded `.exe`.
2. If a blue **"Windows protected your PC"** box appears: click **More info**,
   then **Run anyway**. (OrcaSlicer is safe; it is just not signed by Microsoft.)
3. Click **Next** through the installer and **Finish**.
4. Open **OrcaSlicer** from the Start menu.

### Mac

1. Double-click the downloaded `.dmg`.
2. Drag the **OrcaSlicer** icon onto the **Applications** folder.
3. Open **Applications** and double-click **OrcaSlicer**.
4. If macOS says it **cannot be opened** or **can't verify the developer**:
   open **System Settings → Privacy & Security**, scroll down, and click
   **Open Anyway** next to the OrcaSlicer message. Confirm with your password.

### Linux

1. Right-click the downloaded `.AppImage` → **Properties** → **Permissions** →
   tick **Allow executing file as program**.
2. Double-click it.

## First start: tell Orca about your printer

The first time OrcaSlicer opens, a **setup wizard** appears.

1. **Login** page: click **Skip** (no account needed).
2. **Printer** page: find your brand (e.g. **Creality**) and tick your model,
   for example **Ender-3 Pro**, nozzle **0.4**.
3. **Filament** page: make sure **Generic PLA** is ticked.
4. Click **Finish**.

Missed the wizard? Click the gear icon next to the printer name (top left,
**Printer** box) to add a printer later.

Next: [Step 2 - Load this project's settings](2-presets.md)
