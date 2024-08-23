Tic Tac Toe Game using Tkinter
Overview
This project is a simple implementation of the classic Tic Tac Toe game using Python's Tkinter library. The game allows two players to play against each other on the same computer, taking turns to place their marks (X or O) on a 3x3 grid. The first player to align three of their marks horizontally, vertically, or diagonally wins the game. If all cells are filled without a winner, the game ends in a draw.

Features
Player Interaction: Two players can alternate turns to play the game.
Winner Detection: The game automatically detects if a player has won by aligning three of their marks in a row.
Draw Detection: If the grid is filled without any player winning, the game declares a draw.
Game Reset: After a win or draw, the game automatically resets for a new round.
Dynamic Styling: The current player's mark is styled dynamically, with player X's mark appearing in blue and player O's mark in red.
Prerequisites
Python 3.x installed on your system.
Tkinter library (included with standard Python installations).
How to Run
Run the Application:
Execute the Python script to start the Tic Tac Toe game:
python tic_tac_toe.py
The game window will open, and you can start playing immediately.

Game Instructions
Starting the Game: When the game starts, player X will go first.
Making a Move: Click on any empty cell in the 3x3 grid to place your mark (X or O).
Winning: The first player to align three marks (horizontally, vertically, or diagonally) wins the game.
Draw: If all cells are filled without a winner, the game will end in a draw.
New Game: After a win or draw, the game automatically resets for a new round.
File Structure
tic_tac_toe.py: The main Python file containing the code for the Tic Tac Toe game.
README.md: This file provides an overview of the application and instructions on how to run it.
Code Explanation
Main Components:

on_button_click(row, col): Handles the event when a player clicks on a cell. It updates the board and checks for a win or draw.
check_winner(): Checks if there is a winner after each move.
check_draw(): Checks if the game ends in a draw.
reset_board(): Resets the board for a new game after a win or draw.
toggle_player(): Switches turns between player X and player O.
Grid Setup: The grid is represented by a 2D list (board), and buttons are used to create the UI for each cell.
