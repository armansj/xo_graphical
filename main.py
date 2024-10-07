import random
from guizero import App, Text, PushButton, Box, info

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

lst = ["X", "O"]
player = random.choice(lst)
computer_choose = "O" if player == "X" else "X"
game_is_over = False


def show_winner(winner):
    if winner == "draw":
        info("Game Over", "It's a draw!")
    else:
        info("Game Over", f"{winner} wins!")
    app.destroy()


def check_winner(board):
    # All the possible winning combinations
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


def computer_move():
    global game_is_over
    computer_selection = random.randint(0, 8)

    while board[computer_selection] != "-":
        computer_selection = random.randint(0, 8)

    board[computer_selection] = computer_choose
    buttons[computer_selection].text = computer_choose
    buttons[computer_selection].disable()

    if check_winner(board):
        game_is_over = True
        show_winner(computer_choose)

    if "-" not in board and not game_is_over:
        game_is_over = True
        show_winner("draw")


def player_move(position):
    global game_is_over
    if not game_is_over:
        if board[position] == "-":
            board[position] = player
            buttons[position].text = player
            buttons[position].disable()

            if check_winner(board):
                game_is_over = True
                show_winner(player)
            elif "-" not in board:
                game_is_over = True
                show_winner("draw")
            else:
                computer_move()


app = App("Tic Tac Toe")

Text(app, f"You are {player}. The computer is {computer_choose}.")

buttons = []
grid = Box(app, layout="grid")

for i in range(9):
    button = PushButton(grid, command=player_move, args=[i], text="-", width=4, height=2, grid=[i // 3, i % 3])
    buttons.append(button)

app.display()
