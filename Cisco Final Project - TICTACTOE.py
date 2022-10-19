import random


def display_board(board_num):
    board = f"+-------+-------+-------+\n|       |       |       |\n|   {board_num[0][0]}   |   {board_num[0][1]}   |   " \
            f"{board_num[0][2]}   |\n|       |       |       |\n+-------+-------+-------+\n|       |       |       |\n" \
            f"|   {board_num[1][0]}   |   {board_num[1][1]}   |   {board_num[1][2]}   |\n|       |       |       |" \
            f"\n+-------+-------+-------+\n|       |       |       |\n|   {board_num[2][0]}   |   {board_num[2][1]}   |   " \
            f"{board_num[2][2]}   |\n|       |       |       |\n+-------+-------+-------+"
    print(board)


def enter_move(board_num):
    board_dict = {
        "1": (0, 0),
        "2": (0, 1),
        "3": (0, 2),
        "4": (1, 0),
        "5": (1, 1),
        "6": (1, 2),
        "7": (2, 0),
        "8": (2, 1),
        "9": (2, 2)
    }
    turn = input("Enter your move: ")
    if turn in board_dict:
        player_turn = board_dict.get(turn)
        board_num[player_turn[0]][player_turn[1]] = "O"
    else:
        print('Invalid input! please enter a digit from 1 to 9 to place your "O"')
        display_board(board_num)
        enter_move(board_num)
    return board_num


def make_list_of_free_fields(board_num):
    free_list = []
    for j in range(len(board_num)):
        for k in board_num[j]:
            if k != "X" and k != "O":
                free_list.append(k)
    return free_list


def victory_for(board_num):
    comp_win = ["X", "X", "X"]
    player_win = ["O", "O", "O"]
    if board_num[:][0] == comp_win or board_num[:][1] == comp_win or board_num[:][2] == comp_win or list(
            board_num[0][0] + board_num[1][0] + board_num[2][0]) == comp_win or list(
        board_num[0][1] + board_num[1][1] + board_num[2][1]) == comp_win or list(
        board_num[0][2] + board_num[1][2] + board_num[2][2]) == comp_win or list(
        board_num[0][0] + board_num[1][1] + board_num[2][2]) == comp_win or list(
        board_num[0][2] + board_num[1][1] + board_num[2][0]) == comp_win:
        return 0
    elif board_num[:][0] == player_win or board_num[:][1] == player_win or board_num[:][2] == player_win or list(
            board_num[0][0] + board_num[1][0] + board_num[2][0]) == player_win or list(
        board_num[0][1] + board_num[1][1] + board_num[2][1]) == player_win or list(
        board_num[0][2] + board_num[1][2] + board_num[2][2]) == player_win or list(
        board_num[0][0] + board_num[1][1] + board_num[2][2]) == player_win or list(
        board_num[0][2] + board_num[1][1] + board_num[2][0]) == player_win:
        return 1


def draw_move(board_num):
    # The function draws the computer's move and updates the board.
    board_dict = {
        "1": (0, 0),
        "2": (0, 1),
        "3": (0, 2),
        "4": (1, 0),
        "5": (1, 1),
        "6": (1, 2),
        "7": (2, 0),
        "8": (2, 1),
        "9": (2, 2)
    }
    free_squares = make_list_of_free_fields(board_num)
    computer_turn = random.choice(free_squares)
    computer_turn = board_dict.get(computer_turn)
    print(f"Computer plays square {board_num[computer_turn[0]][computer_turn[1]]}")
    board_num[computer_turn[0]][computer_turn[1]] = "X"
    return board_num


print("Welcome to TIC-TAC-TOE game")
print('\nInstructions: The displayed board has 9 slots, select a digit from 1 to 9 to place your "X" or "O"\n')
board_num = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
display_board(board_num)
print()
your_turn = input("Would you like to play first (y/n)? ")
i = 1
# At each iteration of the while loop, either the player or computer plays their turn
while i < 10:
    # CASE 1: Player starts first
    if your_turn == "y":
        if i % 2 != 0:                              # Player's turn
            board_num = enter_move(board_num)
            display_board(board_num)

        elif i % 2 == 0:                            # Computer's turn
            computer_turn = draw_move(board_num)
            display_board(board_num)

        # Check if player or computer won
        status = victory_for(board_num)
        i = i + 1
        if status == 0:
            print("Computer wins!")
            break
        elif status == 1:
            print("Player wins!")
            break

    # CASE 2: Computer starts first
    else:
        if i % 2 != 0:  # Computer's turn
            board_num = draw_move(board_num)
            display_board(board_num)

        elif i % 2 == 0:  # Player's turn
            computer_turn = enter_move(board_num)
            display_board(board_num)

        # Check if player or computer won
        status = victory_for(board_num)
        i = i + 1
        if status == 0:
            print("Computer wins!")
            break
        elif status == 1:
            print("Player wins!")
            break

if victory_for(board_num) is None:
    print("Tie!")

