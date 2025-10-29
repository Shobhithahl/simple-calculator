import random
import copy

class Sudoku:
    def __init__(self, difficulty="medium"):
        """Initialize a Sudoku game with specified difficulty."""
        self.size = 9
        self.box_size = 3
        self.difficulty = difficulty
        self.solution = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.original_board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        
    def is_valid(self, board, row, col, num):
        """Check if placing num at (row, col) is valid."""
        # Check row
        if num in board[row]:
            return False
        
        # Check column
        if num in [board[i][col] for i in range(self.size)]:
            return False
        
        # Check 3x3 box
        box_row, box_col = row - row % self.box_size, col - col % self.box_size
        for i in range(box_row, box_row + self.box_size):
            for j in range(box_col, box_col + self.box_size):
                if board[i][j] == num:
                    return False
        
        return True
    
    def solve(self, board):
        """Solve the sudoku puzzle using backtracking."""
        for row in range(self.size):
            for col in range(self.size):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(board, row, col, num):
                            board[row][col] = num
                            if self.solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True
    
    def generate_solution(self):
        """Generate a complete valid sudoku solution."""
        # Fill diagonal 3x3 boxes first (they don't affect each other)
        for box in range(0, self.size, self.box_size):
            nums = list(range(1, 10))
            random.shuffle(nums)
            idx = 0
            for i in range(box, box + self.box_size):
                for j in range(box, box + self.box_size):
                    self.solution[i][j] = nums[idx]
                    idx += 1
        
        # Fill remaining cells
        self.solve(self.solution)
    
    def create_puzzle(self):
        """Create a puzzle by removing numbers from the solution."""
        self.generate_solution()
        self.board = copy.deepcopy(self.solution)
        
        # Determine how many cells to remove based on difficulty
        difficulty_levels = {
            "easy": 35,
            "medium": 45,
            "hard": 55
        }
        cells_to_remove = difficulty_levels.get(self.difficulty, 45)
        
        # Remove numbers randomly
        positions = [(i, j) for i in range(self.size) for j in range(self.size)]
        random.shuffle(positions)
        
        for i in range(cells_to_remove):
            row, col = positions[i]
            self.board[row][col] = 0
        
        # Store the original puzzle state
        self.original_board = copy.deepcopy(self.board)
    
    def is_cell_original(self, row, col):
        """Check if a cell is part of the original puzzle."""
        return self.original_board[row][col] != 0
    
    def make_move(self, row, col, num):
        """Place a number on the board if valid."""
        if self.is_cell_original(row, col):
            return False, "This cell is part of the original puzzle!"
        
        if num < 0 or num > 9:
            return False, "Number must be between 0 (to clear) and 9!"
        
        self.board[row][col] = num
        return True, "Move successful!"
    
    def get_hint(self):
        """Provide a hint by revealing one empty cell."""
        empty_cells = [(i, j) for i in range(self.size) for j in range(self.size) 
                       if self.board[i][j] == 0]
        
        if not empty_cells:
            return None, None, None
        
        row, col = random.choice(empty_cells)
        return row, col, self.solution[row][col]
    
    def is_complete(self):
        """Check if the puzzle is completely and correctly solved."""
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] != self.solution[i][j]:
                    return False
        return True
    
    def display(self):
        """Display the current board state."""
        print("\n    " + "  ".join([str(i) for i in range(9)]))
        print("  +" + "-" * 25 + "+")
        
        for i in range(self.size):
            if i % 3 == 0 and i != 0:
                print("  |" + "-" * 7 + "+" + "-" * 7 + "+" + "-" * 7 + "|")
            
            row_str = str(i) + " | "
            for j in range(self.size):
                if self.board[i][j] == 0:
                    row_str += ". "
                else:
                    # Mark original numbers differently (they can't be changed)
                    if self.is_cell_original(i, j):
                        row_str += str(self.board[i][j]) + " "
                    else:
                        row_str += str(self.board[i][j]) + " "
                
                if (j + 1) % 3 == 0 and j != 8:
                    row_str += "| "
            
            row_str += "|"
            print(row_str)
        
        print("  +" + "-" * 25 + "+")

