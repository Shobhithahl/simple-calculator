#!/usr/bin/python3
"""
Sudoku Game - GUI Version with Tkinter
Beautiful graphical interface for playing Sudoku

Note: On macOS, this requires Tkinter which comes with the system Python.
Run with: /usr/bin/python3 sudoku_gui.py
"""

import tkinter as tk
from tkinter import messagebox, ttk
from sudoku import Sudoku

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Game")
        self.root.resizable(False, False)
        
        # Colors
        self.bg_color = "#f0f0f0"
        self.grid_color = "#000000"
        self.original_color = "#2c3e50"
        self.player_color = "#3498db"
        self.selected_color = "#e8f4f8"
        self.error_color = "#e74c3c"
        self.hint_color = "#27ae60"
        
        self.game = None
        self.selected_cell = None
        self.cells = {}
        self.cell_values = {}
        
        # Configure root
        self.root.configure(bg=self.bg_color)
        
        # Create main container
        main_frame = tk.Frame(root, bg=self.bg_color, padx=20, pady=20)
        main_frame.pack()
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="🎮 SUDOKU GAME 🎮",
            font=("Arial", 24, "bold"),
            bg=self.bg_color,
            fg="#2c3e50"
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Game board frame
        self.board_frame = tk.Frame(main_frame, bg=self.bg_color)
        self.board_frame.grid(row=1, column=0, padx=(0, 20))
        
        # Control panel
        control_frame = tk.Frame(main_frame, bg=self.bg_color)
        control_frame.grid(row=1, column=1, sticky="n")
        
        self.create_control_panel(control_frame)
        
        # Show difficulty selection
        self.show_difficulty_selection()
    
    def create_control_panel(self, parent):
        """Create the control panel with buttons and number pad."""
        # Difficulty label
        tk.Label(
            parent,
            text="Controls",
            font=("Arial", 16, "bold"),
            bg=self.bg_color,
            fg="#2c3e50"
        ).pack(pady=(0, 10))
        
        # Number pad
        number_frame = tk.Frame(parent, bg=self.bg_color)
        number_frame.pack(pady=10)
        
        tk.Label(
            number_frame,
            text="Number Pad",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            fg="#34495e"
        ).grid(row=0, column=0, columnspan=3, pady=(0, 5))
        
        # Create number buttons 1-9
        for i in range(1, 10):
            row = (i - 1) // 3 + 1
            col = (i - 1) % 3
            btn = tk.Button(
                number_frame,
                text=str(i),
                font=("Arial", 14, "bold"),
                width=3,
                height=1,
                bg="#3498db",
                fg="white",
                activebackground="#2980b9",
                cursor="hand2",
                command=lambda num=i: self.place_number(num)
            )
            btn.grid(row=row, column=col, padx=2, pady=2)
        
        # Clear button
        clear_btn = tk.Button(
            number_frame,
            text="Clear",
            font=("Arial", 12, "bold"),
            width=10,
            bg="#e74c3c",
            fg="white",
            activebackground="#c0392b",
            cursor="hand2",
            command=lambda: self.place_number(0)
        )
        clear_btn.grid(row=4, column=0, columnspan=3, pady=(5, 0))
        
        # Action buttons
        button_frame = tk.Frame(parent, bg=self.bg_color)
        button_frame.pack(pady=20)
        
        buttons = [
            ("💡 Hint", self.get_hint, "#27ae60"),
            ("✓ Check", self.check_solution, "#f39c12"),
            ("🔄 Restart", self.restart_game, "#9b59b6"),
            ("🆕 New Game", self.show_difficulty_selection, "#e67e22"),
        ]
        
        for text, command, color in buttons:
            btn = tk.Button(
                button_frame,
                text=text,
                font=("Arial", 11, "bold"),
                width=12,
                height=2,
                bg=color,
                fg="white",
                activebackground=color,
                cursor="hand2",
                command=command
            )
            btn.pack(pady=5)
        
        # Instructions
        instructions = tk.Text(
            parent,
            width=25,
            height=10,
            font=("Arial", 9),
            bg="#ecf0f1",
            fg="#2c3e50",
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        instructions.pack(pady=(20, 0))
        instructions.insert("1.0", """📖 HOW TO PLAY:

• Click a cell to select it
• Use number pad or keyboard (1-9)
• Click Clear or press 0 to erase
• Press 'h' for hint
• Blue numbers = your moves
• Black numbers = original puzzle

🎯 Fill all cells correctly!""")
        instructions.config(state=tk.DISABLED)
    
    def create_board(self):
        """Create the Sudoku board grid."""
        # Clear existing board
        for widget in self.board_frame.winfo_children():
            widget.destroy()
        
        self.cells = {}
        self.cell_values = {}
        
        # Create canvas for better visual control
        canvas_size = 450
        cell_size = canvas_size // 9
        
        canvas = tk.Canvas(
            self.board_frame,
            width=canvas_size,
            height=canvas_size,
            bg="white",
            highlightthickness=2,
            highlightbackground="#2c3e50"
        )
        canvas.pack()
        
        # Draw grid lines
        for i in range(10):
            line_width = 3 if i % 3 == 0 else 1
            color = "#2c3e50" if i % 3 == 0 else "#bdc3c7"
            
            # Vertical lines
            canvas.create_line(
                i * cell_size, 0,
                i * cell_size, canvas_size,
                width=line_width,
                fill=color
            )
            
            # Horizontal lines
            canvas.create_line(
                0, i * cell_size,
                canvas_size, i * cell_size,
                width=line_width,
                fill=color
            )
        
        # Create cells
        for row in range(9):
            for col in range(9):
                x1 = col * cell_size
                y1 = row * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                
                # Cell background
                cell_bg = canvas.create_rectangle(
                    x1 + 2, y1 + 2, x2 - 2, y2 - 2,
                    fill="white",
                    outline=""
                )
                
                # Cell text
                value = self.game.board[row][col]
                display_text = str(value) if value != 0 else ""
                
                is_original = self.game.is_cell_original(row, col)
                text_color = self.original_color if is_original else self.player_color
                font_weight = "bold" if is_original else "normal"
                
                cell_text = canvas.create_text(
                    (x1 + x2) // 2,
                    (y1 + y2) // 2,
                    text=display_text,
                    font=("Arial", 20, font_weight),
                    fill=text_color
                )
                
                self.cells[(row, col)] = (cell_bg, cell_text)
                self.cell_values[(row, col)] = value
                
                # Bind click event
                canvas.tag_bind(cell_bg, "<Button-1>", lambda e, r=row, c=col: self.select_cell(r, c))
                canvas.tag_bind(cell_text, "<Button-1>", lambda e, r=row, c=col: self.select_cell(r, c))
        
        self.canvas = canvas
        
        # Bind keyboard events
        self.root.bind("<Key>", self.on_key_press)
    
    def select_cell(self, row, col):
        """Select a cell on the board."""
        # Don't allow selection of original cells
        if self.game.is_cell_original(row, col):
            return
        
        # Deselect previous cell
        if self.selected_cell:
            prev_row, prev_col = self.selected_cell
            cell_bg, _ = self.cells[(prev_row, prev_col)]
            self.canvas.itemconfig(cell_bg, fill="white")
        
        # Select new cell
        self.selected_cell = (row, col)
        cell_bg, _ = self.cells[(row, col)]
        self.canvas.itemconfig(cell_bg, fill=self.selected_color)
    
    def place_number(self, num):
        """Place a number in the selected cell."""
        if not self.selected_cell:
            messagebox.showinfo("No Cell Selected", "Please select a cell first!")
            return
        
        row, col = self.selected_cell
        
        # Update game state
        success, message = self.game.make_move(row, col, num)
        
        if success:
            # Update display
            _, cell_text = self.cells[(row, col)]
            display_text = str(num) if num != 0 else ""
            self.canvas.itemconfig(cell_text, text=display_text, fill=self.player_color)
            self.cell_values[(row, col)] = num
            
            # Check if game is complete
            if self.game.is_complete():
                self.show_victory()
        else:
            messagebox.showerror("Invalid Move", message)
    
    def on_key_press(self, event):
        """Handle keyboard input."""
        if event.char in '123456789':
            self.place_number(int(event.char))
        elif event.char == '0' or event.keysym == 'BackSpace' or event.keysym == 'Delete':
            self.place_number(0)
        elif event.char.lower() == 'h':
            self.get_hint()
        elif event.keysym in ['Up', 'Down', 'Left', 'Right']:
            self.move_selection(event.keysym)
    
    def move_selection(self, direction):
        """Move cell selection with arrow keys."""
        if not self.selected_cell:
            self.select_cell(0, 0)
            return
        
        row, col = self.selected_cell
        
        if direction == 'Up' and row > 0:
            row -= 1
        elif direction == 'Down' and row < 8:
            row += 1
        elif direction == 'Left' and col > 0:
            col -= 1
        elif direction == 'Right' and col < 8:
            col += 1
        
        self.select_cell(row, col)
    
    def get_hint(self):
        """Get a hint for the puzzle."""
        row, col, num = self.game.get_hint()
        
        if row is None:
            messagebox.showinfo("No Hints", "No empty cells left!")
            return
        
        # Place the hint
        self.game.board[row][col] = num
        _, cell_text = self.cells[(row, col)]
        self.canvas.itemconfig(cell_text, text=str(num), fill=self.hint_color)
        self.cell_values[(row, col)] = num
        
        # Flash the cell
        cell_bg, _ = self.cells[(row, col)]
        original_color = self.canvas.itemcget(cell_bg, "fill")
        self.canvas.itemconfig(cell_bg, fill="#d5f4e6")
        self.root.after(500, lambda: self.canvas.itemconfig(cell_bg, fill=original_color))
        
        messagebox.showinfo("Hint", f"Placed {num} at position ({row}, {col})")
        
        if self.game.is_complete():
            self.show_victory()
    
    def check_solution(self):
        """Check the current solution."""
        if self.game.is_complete():
            self.show_victory()
        else:
            # Check for errors
            errors = 0
            for row in range(9):
                for col in range(9):
                    if self.game.board[row][col] != 0:
                        if self.game.board[row][col] != self.game.solution[row][col]:
                            errors += 1
            
            if errors > 0:
                messagebox.showwarning(
                    "Not Quite!",
                    f"You have {errors} error(s). Keep trying!"
                )
            else:
                empty = sum(1 for row in range(9) for col in range(9) if self.game.board[row][col] == 0)
                messagebox.showinfo(
                    "Good Progress!",
                    f"No errors so far! {empty} cells remaining."
                )
    
    def restart_game(self):
        """Restart the current puzzle."""
        if messagebox.askyesno("Restart Game", "Are you sure you want to restart?"):
            self.game.board = [row[:] for row in self.game.original_board]
            self.selected_cell = None
            self.create_board()
    
    def show_victory(self):
        """Show victory message."""
        result = messagebox.askyesno(
            "🎉 Congratulations! 🎉",
            "You solved the puzzle!\n\nWould you like to play again?"
        )
        if result:
            self.show_difficulty_selection()
    
    def show_difficulty_selection(self):
        """Show difficulty selection dialog."""
        dialog = tk.Toplevel(self.root)
        dialog.title("Select Difficulty")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center the dialog
        dialog.geometry("300x250")
        dialog.resizable(False, False)
        dialog.configure(bg=self.bg_color)
        
        # Center on parent
        dialog.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - (dialog.winfo_width() // 2)
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - (dialog.winfo_height() // 2)
        dialog.geometry(f"+{x}+{y}")
        
        tk.Label(
            dialog,
            text="Select Difficulty Level",
            font=("Arial", 16, "bold"),
            bg=self.bg_color,
            fg="#2c3e50"
        ).pack(pady=20)
        
        difficulties = [
            ("🟢 Easy", "easy", "#27ae60"),
            ("🟡 Medium", "medium", "#f39c12"),
            ("🔴 Hard", "hard", "#e74c3c")
        ]
        
        for text, level, color in difficulties:
            btn = tk.Button(
                dialog,
                text=text,
                font=("Arial", 14, "bold"),
                width=15,
                height=2,
                bg=color,
                fg="white",
                activebackground=color,
                cursor="hand2",
                command=lambda l=level: self.start_new_game(l, dialog)
            )
            btn.pack(pady=5)
    
    def start_new_game(self, difficulty, dialog):
        """Start a new game with selected difficulty."""
        dialog.destroy()
        
        # Show loading message
        loading = tk.Label(
            self.board_frame,
            text="Generating puzzle...",
            font=("Arial", 16),
            bg=self.bg_color,
            fg="#2c3e50"
        )
        loading.pack()
        self.root.update()
        
        # Create new game
        self.game = Sudoku(difficulty)
        self.game.create_puzzle()
        self.selected_cell = None
        
        # Remove loading message and create board
        loading.destroy()
        self.create_board()

def main():
    """Main entry point for the GUI application."""
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

