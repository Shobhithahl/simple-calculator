#!/usr/bin/env python3
"""
Simple Sudoku Game - Terminal Interface
Play sudoku directly in your terminal!
"""

from sudoku import Sudoku
import os
import sys

def clear_screen():
    """Clear the terminal screen."""
    os.system('clear' if os.name == 'posix' else 'cls')

def print_menu():
    """Display the main menu."""
    clear_screen()
    print("=" * 50)
    print("        WELCOME TO SUDOKU GAME!        ")
    print("=" * 50)
    print("\nSelect Difficulty Level:")
    print("  1. Easy")
    print("  2. Medium")
    print("  3. Hard")
    print("  4. Exit")
    print("=" * 50)

def print_game_commands():
    """Display available game commands."""
    print("\nCommands:")
    print("  [row] [col] [num] - Place number (e.g., '0 0 5')")
    print("  hint              - Get a hint")
    print("  solution          - Show solution (gives up)")
    print("  restart           - Start a new game")
    print("  quit              - Exit game")
    print("-" * 50)

def play_game(difficulty):
    """Main game loop."""
    game = Sudoku(difficulty)
    print(f"\nGenerating {difficulty} puzzle...")
    game.create_puzzle()
    
    while True:
        clear_screen()
        print("=" * 50)
        print(f"    SUDOKU - {difficulty.upper()} MODE    ")
        print("=" * 50)
        
        game.display()
        print_game_commands()
        
        if game.is_complete():
            print("\n" + "=" * 50)
            print("   CONGRATULATIONS! YOU SOLVED THE PUZZLE!   ")
            print("=" * 50)
            input("\nPress Enter to return to main menu...")
            return
        
        user_input = input("\nYour move: ").strip().lower()
        
        if user_input == "quit":
            return
        
        elif user_input == "restart":
            return play_game(difficulty)
        
        elif user_input == "hint":
            row, col, num = game.get_hint()
            if row is not None:
                game.board[row][col] = num
                print(f"\nHint: Placed {num} at position ({row}, {col})")
                input("Press Enter to continue...")
            else:
                print("\nNo more hints available!")
                input("Press Enter to continue...")
        
        elif user_input == "solution":
            confirm = input("Are you sure you want to see the solution? (yes/no): ").strip().lower()
            if confirm == "yes":
                clear_screen()
                print("=" * 50)
                print("           SOLUTION           ")
                print("=" * 50)
                game.board = game.solution
                game.display()
                print("\n" + "=" * 50)
                input("Press Enter to return to main menu...")
                return
        
        else:
            try:
                parts = user_input.split()
                if len(parts) != 3:
                    print("\nInvalid input! Use format: row col number")
                    input("Press Enter to continue...")
                    continue
                
                row, col, num = map(int, parts)
                
                if row < 0 or row >= 9 or col < 0 or col >= 9:
                    print("\nInvalid position! Row and column must be between 0 and 8.")
                    input("Press Enter to continue...")
                    continue
                
                success, message = game.make_move(row, col, num)
                if not success:
                    print(f"\n{message}")
                    input("Press Enter to continue...")
                
            except ValueError:
                print("\nInvalid input! Please enter numbers only.")
                input("Press Enter to continue...")

def main():
    """Main application entry point."""
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            play_game("easy")
        elif choice == "2":
            play_game("medium")
        elif choice == "3":
            play_game("hard")
        elif choice == "4":
            print("\nThanks for playing! Goodbye!")
            sys.exit(0)
        else:
            print("\nInvalid choice! Please select 1-4.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
        sys.exit(0)

