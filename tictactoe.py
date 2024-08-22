import random

# Creates an empty board with a 3x3 grid
board = [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Checks if there is a winner
def check_winner(board, player):
    # Checks rows for winners
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Checks columns for winners
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Checks diagonals for winners
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

# Checks if the board is full or not
def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

# Allows the player or computer to make a move on the grid
def make_move(board, player, is_computer=False):
    if is_computer:
        available_moves = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
        move = random.choice(available_moves)
        board[move[0]][move[1]] = player
        print(f"Computer chose: row {move[0]}, column {move[1]}")
    else:
        while True:
            try:
                row = int(input(f"Player {player}, enter row (0, 1, 2): "))
                col = int(input(f"Player {player}, enter column (0, 1, 2): "))
                if board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("This cell is not empty. Please try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please only enter numbers between 0 and 2.")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    computer_player = None
    
    # Asking if the player wants to play against the computer
    play_with_computer = input("Would you like to play against the computer? (yes/no): ").lower() == 'yes'
    if play_with_computer:
        computer_player = "O"
    
    while True:
        print_board(board)
        
        if current_player == computer_player:
            make_move(board, current_player, is_computer=True)
        else:
            make_move(board, current_player)
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("The game is a draw!")
            break
        
        # Switches player
        current_player = "O" if current_player == "X" else "X"

play_game()
