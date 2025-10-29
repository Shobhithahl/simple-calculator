# Troubleshooting Guide

## GUI Won't Start - "No module named '_tkinter'"

### Problem
You see this error:
```
ModuleNotFoundError: No module named '_tkinter'
```

### Solution

#### For macOS Users (Recommended):

**Option 1: Use System Python**
The easiest solution is to use macOS's built-in Python which has Tkinter:
```bash
/usr/bin/python3 sudoku_gui.py
```

Or use the launcher script:
```bash
./run_gui.sh
```

**Option 2: Install tkinter for Homebrew Python**
If you prefer using Homebrew Python:
```bash
brew install python-tk@3.13
```

#### For Linux Users:

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**Fedora:**
```bash
sudo dnf install python3-tkinter
```

**Arch Linux:**
```bash
sudo pacman -S tk
```

#### For Windows Users:

Tkinter should be included with Python by default. If not, reinstall Python from [python.org](https://www.python.org) and make sure to check "tcl/tk and IDLE" during installation.

## Alternative: Use Terminal Version

If you can't get the GUI working, you can always use the terminal version:
```bash
python3 game.py
```

This version works on all systems without any dependencies!

## GUI is Slow or Unresponsive

- Close and restart the application
- Try the terminal version instead
- Make sure you're not running multiple instances

## Numbers Won't Enter

- Make sure you've selected a cell first (click on it)
- Check that the cell is not part of the original puzzle (black numbers can't be changed)
- Try using keyboard input (1-9 keys) instead of buttons

## Can't See the Full Window

- The window is fixed size (800x600)
- Make sure your screen resolution is at least 1024x768
- Try running in fullscreen mode

## Python Version Issues

The game requires Python 3.6 or higher. Check your version:
```bash
python3 --version
```

If you have an older version, update Python or use the terminal version.

## Still Having Issues?

1. Try running the terminal version: `python3 game.py`
2. Check that all files are in the same directory
3. Make sure you're in the correct directory when running the commands
4. Verify Python is installed correctly: `python3 --version`

## Quick Test

To verify everything is working, try:
```bash
python3 -c "from sudoku import Sudoku; print('✓ Core game works!')"
```

If this works, the game logic is fine and the issue is only with the GUI.

