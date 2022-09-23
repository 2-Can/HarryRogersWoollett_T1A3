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


# Change Player


# Reassess Win or Draw


