#!/usr/bin/env python3
"""
Sudoku Game - Web Interface using Flask
Run this to play Sudoku in your web browser!
"""

from flask import Flask, render_template, jsonify, request, session
from sudoku import Sudoku
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Store games in session
games = {}

@app.route('/')
def index():
    """Main page - serve the game interface."""
    return render_template('sudoku.html')

@app.route('/new_game/<difficulty>')
def new_game(difficulty):
    """Start a new game with specified difficulty."""
    if difficulty not in ['easy', 'medium', 'hard']:
        return jsonify({'error': 'Invalid difficulty'}), 400
    
    # Create new game
    game = Sudoku(difficulty)
    game.create_puzzle()
    
    # Store in session
    session_id = secrets.token_hex(8)
    games[session_id] = game
    session['game_id'] = session_id
    
    # Return game state
    return jsonify({
        'board': game.board,
        'original': game.original_board,
        'difficulty': difficulty,
        'session_id': session_id
    })

@app.route('/make_move', methods=['POST'])
def make_move():
    """Make a move on the board."""
    data = request.json
    session_id = session.get('game_id')
    
    if not session_id or session_id not in games:
        return jsonify({'error': 'No active game'}), 400
    
    game = games[session_id]
    row = data.get('row')
    col = data.get('col')
    num = data.get('num')
    
    success, message = game.make_move(row, col, num)
    
    return jsonify({
        'success': success,
        'message': message,
        'board': game.board,
        'complete': game.is_complete()
    })

@app.route('/get_hint')
def get_hint():
    """Get a hint for the current game."""
    session_id = session.get('game_id')
    
    if not session_id or session_id not in games:
        return jsonify({'error': 'No active game'}), 400
    
    game = games[session_id]
    row, col, num = game.get_hint()
    
    if row is None:
        return jsonify({'error': 'No hints available'})
    
    # Apply the hint
    game.board[row][col] = num
    
    return jsonify({
        'row': row,
        'col': col,
        'num': num,
        'board': game.board,
        'complete': game.is_complete()
    })

@app.route('/check_solution')
def check_solution():
    """Check if the current solution is correct."""
    session_id = session.get('game_id')
    
    if not session_id or session_id not in games:
        return jsonify({'error': 'No active game'}), 400
    
    game = games[session_id]
    
    if game.is_complete():
        return jsonify({
            'complete': True,
            'errors': 0,
            'message': 'Congratulations! You solved it!'
        })
    
    # Count errors and empty cells
    errors = 0
    empty = 0
    for row in range(9):
        for col in range(9):
            if game.board[row][col] == 0:
                empty += 1
            elif game.board[row][col] != game.solution[row][col]:
                errors += 1
    
    return jsonify({
        'complete': False,
        'errors': errors,
        'empty': empty,
        'message': f'{errors} error(s), {empty} cell(s) remaining'
    })

@app.route('/restart')
def restart():
    """Restart the current game."""
    session_id = session.get('game_id')
    
    if not session_id or session_id not in games:
        return jsonify({'error': 'No active game'}), 400
    
    game = games[session_id]
    game.board = [row[:] for row in game.original_board]
    
    return jsonify({
        'board': game.board,
        'message': 'Game restarted'
    })

if __name__ == '__main__':
    print("\n" + "=" * 50)
    print("🎮 SUDOKU WEB GAME STARTING...")
    print("=" * 50)
    print("\n📱 Open your browser and go to:")
    print("\n   👉 http://localhost:5000")
    print("\n💡 Press Ctrl+C to stop the server")
    print("=" * 50 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)

