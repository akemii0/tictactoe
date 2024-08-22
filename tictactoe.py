#Creates an empty board with 3x3 grid
board = [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print (" | ".join(row))
        print ("-" * 5) 
        

print_board(board)


#the code below checks if there is a winner
def check_winner(board, player):
    #checks row for winners
    for row in board:
        if all ([cell == player for cell in row]):
            return True
    #checks columns for winners
    for col in range(3):
        if all ([board[row][col] == player for row in range(3)]):
            return True
    #checks diagnols for winners
    if all ([board [i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True 
    return False

#check if the board is full or not
def is_board_full(board):
    return all ([cell != " " for row in board for cell in row])

#code below allows player to make moves on the grid
def make_move(board, player):
    while True:
        try:
            row= int(input(f"Player {player}, enter row (0, 1, 2): "))
            col = int(input(f"Player {player}, enter column (0, 1, 2): "))
            if board [row][col] == " ":
                board[row][col] = player
                break
            else:
                print("This cell is not empty. Please try again. ")
        except (ValueError, IndexError):
            print("Invalid input. Please only enter numbers between 0 and 2")
            


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player= "X"
    
    while True:
        print_board(board)
        make_move(board, current_player)
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins! ")
            break
        elif is_board_full(board):
            print_board(board)
            print("The game is a draw!")
            break
        
        
        #switches player
        current_player = "O" if current_player == "X" else "X"
        
        
        

play_game()