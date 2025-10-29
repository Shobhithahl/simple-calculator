# Simple Sudoku Game

A fun and interactive terminal-based Sudoku game written in Python!

## Features

- 🎮 Three difficulty levels: Easy, Medium, and Hard
- 💡 Hint system to help when you're stuck
- ✅ Automatic puzzle validation
- 🔄 Restart game at any time
- 👁️ View solution option
- 🎯 Clean terminal interface

## Requirements

- Python 3.6 or higher
- No external dependencies needed! Uses only Python standard library

## Installation

1. Clone or download this repository
2. Navigate to the game directory:
```bash
cd simple-calculator
```

## How to Play

### 🌐 Web Version (Recommended - No Installation!) 

**The easiest way to play!** Just open the HTML file in your browser:

**Option 1 - Double-click the file:**
- Find `sudoku_standalone.html` in the folder
- Double-click to open in your default browser

**Option 2 - Command line:**
```bash
open sudoku_standalone.html
```

**Features:**
- ✨ Beautiful, modern web interface
- 🎨 Click-to-play with visual animations
- 🔢 Number pad + keyboard support (1-9, arrows)
- 💡 Hint system with visual feedback
- ✓ Error checking with highlighting
- 📱 Works on any device with a browser
- ⚡ No installation or dependencies needed!

### 🖥️ GUI Version (Tkinter - macOS/Linux/Windows)

Run the graphical desktop interface:

**macOS:**
```bash
./run_gui.sh
```

Or directly:
```bash
/usr/bin/python3 sudoku_gui.py
```

> **Note**: Requires Tkinter. macOS system Python has it built-in.

### ⌨️ Terminal Version

Run the text-based version:
```bash
python3 game.py
```

### Game Instructions

1. Select your difficulty level:
   - **Easy**: 35 cells removed (46 given numbers)
   - **Medium**: 45 cells removed (36 given numbers)
   - **Hard**: 55 cells removed (26 given numbers)

3. Game commands:
   - **Place a number**: Enter `row col number` (e.g., `0 0 5` to place 5 at row 0, column 0)
   - **Get a hint**: Type `hint`
   - **Show solution**: Type `solution` (gives up on current puzzle)
   - **Restart game**: Type `restart`
   - **Quit**: Type `quit`

## Game Rules

Sudoku is played on a 9x9 grid, divided into nine 3x3 boxes. The objective is to fill the grid so that:

1. Each **row** contains the digits 1-9 without repetition
2. Each **column** contains the digits 1-9 without repetition
3. Each **3x3 box** contains the digits 1-9 without repetition

## Example Gameplay

```
    0  1  2  3  4  5  6  7  8
  +-------------------------+
0 | 5 3 . | . 7 . | . . . |
1 | 6 . . | 1 9 5 | . . . |
2 | . 9 8 | . . . | . 6 . |
  |-------+-------+-------|
3 | 8 . . | . 6 . | . . 3 |
4 | 4 . . | 8 . 3 | . . 1 |
5 | 7 . . | . 2 . | . . 6 |
  |-------+-------+-------|
6 | . 6 . | . . . | 2 8 . |
7 | . . . | 4 1 9 | . . 5 |
8 | . . . | . 8 . | . 7 9 |
  +-------------------------+

Your move: 0 2 4
```

## Files

- **`sudoku_standalone.html`** - 🌐 **Web version (RECOMMENDED!)** - Just open in browser!
- `sudoku.py` - Core game logic (board generation, validation, solving)
- `sudoku_gui.py` - Desktop GUI (Tkinter)
- `sudoku_web.py` - Flask web server (optional)
- `game.py` - Terminal interface
- `requirements.txt` - Dependencies info
- `README.md` - This file

## Tips for Playing

1. Start by finding cells with only one possible number
2. Use the process of elimination
3. Check each row, column, and 3x3 box carefully
4. Don't hesitate to use hints when stuck!
5. Practice makes perfect - start with Easy and work your way up

## Technical Details

- Uses backtracking algorithm for puzzle generation and solving
- Generates puzzles by creating a complete solution and removing numbers
- Validates moves in real-time
- Original puzzle cells are protected from modification

## Future Enhancements

Potential features that could be added:
- Save/load game progress
- Timer and scoring system
- Undo/redo functionality
- GUI version with Tkinter or Pygame
- Multiple puzzle save slots
- Statistics tracking

## License

Feel free to use, modify, and distribute this game as you wish!

## Author

Created with ❤️ for Sudoku enthusiasts everywhere!

Enjoy the game! 🎉
