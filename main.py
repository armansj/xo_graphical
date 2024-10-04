import random

print("Tic tac toe")

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

game_is_over = True


def display_board(board):
    for i in range(0, len(board), 3):
        print(" ".join(board[i:i + 3]))


display_board(board)

lst = ["X", "O"]
player = random.choice(lst)
computer_choose = "O" if player == "X" else "X"

print(f"You should start the game with {player}")
print(f"Computer will play as {computer_choose}")


def check_winner(board):
    if board[0] == board[1] == board[2] != "-" or \
            board[3] == board[4] == board[5] != "-" or \
            board[6] == board[7] == board[8] != "-" or \
            board[0] == board[3] == board[6] != "-" or \
            board[1] == board[4] == board[7] != "-" or \
            board[2] == board[5] == board[8] != "-" or \
            board[0] == board[4] == board[8] != "-" or \
            board[2] == board[4] == board[6] != "-":
        return True
    return False


def select_room(board, player_selection, player, computer_selection, computer_choose):
    # Player's move
    if board[player_selection] == "-":
        board[player_selection] = player
        if check_winner(board):
            display_board(board)
            print(f"{player} wins!")
            return False
    else:
        print("That spot is already taken, please choose another.")
        return True  # Ask the player to select again

    while board[computer_selection] != "-":
        computer_selection = random.randint(0, 8)

    board[computer_selection] = computer_choose
    print(f"Computer chooses position {computer_selection}")

    if check_winner(board):
        display_board(board)
        print(f"{computer_choose} wins!")
        return False

    display_board(board)
    return True


while game_is_over:
    player_selection = int(input("Enter a number between 0 and 8 for your move: "))

    while player_selection < 0 or player_selection > 8 or board[player_selection] != "-":
        print("Invalid choice. Please choose an empty position between 0 and 8.")
        player_selection = int(input("Enter a number between 0 and 8: "))

    computer_selection = random.randint(0, 8)

    game_is_over = select_room(board, player_selection, player, computer_selection, computer_choose)

    if "-" not in board and game_is_over:
        print("It's a draw!")
        break
