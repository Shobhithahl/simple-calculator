#!/bin/bash
# Launcher script for Sudoku GUI
# Uses macOS system Python which has tkinter support

echo "🎮 Starting Sudoku Game..."
/usr/bin/python3 "$(dirname "$0")/sudoku_gui.py"

