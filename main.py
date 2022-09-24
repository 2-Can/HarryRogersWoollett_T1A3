# imports


# Global Variables

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

current_player = "X"
winner = None
game_running = True

# Display the gameboard
def print_board(board):
    """Prints the gameboard

    Args:
        board (_type_): _description_
    """    
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Receive player input
def player_input(board):
    inp = int(input("Please enter a number between 1 and 9: "))    
    if board[inp-1] == "-":
        board[inp-1] = current_player
    else:
        print("Sorry, that position is already occupied.")
        
# Assess Win or Draw
def check_row(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def check_column(board):
    global winner
    if board[0] == board [3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board [4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board [5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def check_draw(board):
    global game_running
    if "-" not in board:
        print_board(board)
        print("It's a draw!")
        game_running = False

def check_win():
    global game_running
    if check_row(board) or check_column(board) or check_diagonal(board):
        print(f"{current_player}, you win!")
        game_running = False


# Change Player
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


# CPU Opponent

# Reassess Win or Draw

while game_running:
    print_board(board)
    player_input(board)

# ASCII end screen

# Print result to txt file


# Tests
