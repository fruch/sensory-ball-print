[עברית](he/tools-setup.md)

# Setting up Python (for the helper tools)

You **don't need this to print the ball**. It's only for the two helper tools:

- `tools/check_fit.py` - checks that the three files you got fit together
- `tools/extract_ball.py` - pulls single-colour files out of the multi-colour project

Both are **Python** programs. Python is a free program that runs other small
programs (called scripts). You type commands into a **terminal** - a window
where you type instead of clicking.

## Windows

### 1. Install Python

1. Open the **Microsoft Store** (click Start and type `store`).
2. Search for **Python 3.13** (or the newest **Python 3.x** you see).
3. Click **Get** (or **Install**). Wait until it finishes.

No Microsoft Store? Use the installer from
[python.org/downloads](https://www.python.org/downloads/) instead. On the
first screen of the installer, **tick "Add python.exe to PATH"** before you
click **Install Now**. If you forget this, the commands below won't work.

### 2. Open a terminal in the project folder

1. Open the folder where you unzipped this project (the one with `tools` inside).
2. Click the **address bar** at the top of the folder window.
3. Type `powershell` and press **Enter**. A blue or black window opens - that's
   the terminal, already "inside" your folder.

(On Windows 11 you can also right-click empty space in the folder →
**Open in Terminal**.)

### 3. Check that Python works

Type this and press **Enter**:

```
python --version
```

You should see something like `Python 3.13.1`. If it says the command is not
found, close the terminal and open it again. Still not working? Install
Python again and make sure "Add python.exe to PATH" is ticked.

### 4. Run a tool

On Windows the command is `python` and folders use `\`:

```
python tools\check_fit.py half1.stl half2.stl screw.stl
```

If a file name has spaces, put it in quotes: `"Sensory Screw V11.stl"`.

## Mac

### 1. Open the terminal

Press **Cmd + Space**, type `Terminal`, and press **Enter**.

### 2. Check (or install) Python

Type this and press **Enter**:

```
python3 --version
```

- If you see something like `Python 3.9.6` or newer - you're ready.
- If a window pops up saying the **command line developer tools** are needed,
  click **Install** and wait (it can take 10-20 minutes). Then type the
  command again.

### 3. Go to the project folder

1. Type `cd ` (the letters c, d, then a **space**). Don't press Enter yet.
2. Drag the project folder (the one with `tools` inside) from Finder into the
   terminal window. Its path appears after `cd `.
3. Press **Enter**.

### 4. Run a tool

```
python3 tools/check_fit.py half1.stl half2.stl screw.stl
```

If a file name has spaces, put it in quotes: `"Sensory Screw V11.stl"`.

## Linux

Python 3 is already installed. Open a terminal in the project folder and use
`python3`, like on Mac.

## Tip: file paths

The tools need to find your `.stl` / `.3mf` files. The easiest way: instead of
typing a file name, **drag the file from the folder window into the terminal**.
That pastes its full path, with quotes if needed (on Windows, hold **Shift**,
right-click the file → **Copy as path**, then paste).

## For maintainers: bash

`tools/verify-presets.sh` is a **bash** script. It runs the Linux version of
OrcaSlicer, so it needs **Linux**:

- **Linux:** run it as is.
- **Windows:** install WSL (Linux inside Windows): open PowerShell **as
  administrator**, run `wsl --install`, restart, and use the **Ubuntu** app
  that appears. Download the Linux OrcaSlicer `.AppImage` inside Ubuntu.
- **Mac:** not supported - the script uses the Linux OrcaSlicer. Use a Linux
  machine or a Linux virtual machine.

Volunteers never need this script.
