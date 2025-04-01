# Tic-Tac-Toe-Game

Tic Tac Toe - Python Console Game
This is a simple command-line Tic Tac Toe game implemented in Python. Two players (X and O) take turns selecting positions on a 3x3 grid until one wins or the game ends in a draw.

Features
✅ Two-player gameplay (X and O)
✅ Interactive user input for moves
✅ Board updates and displays after each turn
✅ Automatic win checking for both players
✅ Handles invalid input and occupied positions

How to Play
Run the Python script:

bash
Copy
Edit
python tic_tac_toe.py
Players take turns entering a number (0-8) corresponding to a position on the board.

The board updates automatically, and the game checks for a winner.

The game ends when a player wins or all positions are filled (draw).

Example Gameplay
diff
Copy
Edit
Welcome to Tic Tac Toe
0 | 1 | 2 
--|---|---
3 | 4 | 5 
--|---|---
6 | 7 | 8 

X's Chance
Please enter a value (0-8): 0

X | 1 | 2 
--|---|---
3 | 4 | 5 
--|---|---
6 | 7 | 8 
...
Implementation Details
The board is represented using two lists (xState and zState), tracking X and O moves.

The game alternates turns using a turn variable.

The printBoard function displays the grid with updated moves.

The checkWin function verifies if either player has won.

The game runs for a maximum of 9 turns, ending in a draw if no winner is found.

Requirements
Python 3.x
