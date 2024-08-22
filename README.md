# Tic-Tac-Toe Game
This is a command-line implementation of the classic Tic-Tac-Toe game using Python. Two players take turns marking Xs and Os on a 3x3 grid. The game ends when when one player successfully alings three of their marks horizontally, vertically, or diagonally, or when all cells are filled without a winner, resulting in a draw.

## Features
- Two-player mode
- Command-Line interface
- Automatic win detection for rows, columns, and diagonals
- Dectection of draw when the board is full

## How to Play
1. Clone the respository to your local machine:
   ```bash
    git clone https://github.com/akemii0/tictactoe.git
    ```
2. Navigate to the project directory:
     ```bash
    cd tictactoe
    ```
3. Run the game using Python:
   ```bash
    python3 tictactoe.py
    ```
4. Players take turns entering their move by specifying the row and column numbers (0, 1, or 2). For example, to place a mark in the top-left corner, enter `0` for both the row and column.

5. The game will check after each move if there is a winner or if the board is full (resulting in a draw).

6. The game will announce the winner or declare a draw at the end of the game.
