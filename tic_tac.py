import random


# define the function that prints the board
def print_board():
    print(f'{board[1]} | {board[2]} | {board[3]}')
    print('---------')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print('---------')
    print(f'{board[7]} | {board[8]} | {board[9]}')


def available(sel):
    return board[sel] != "X" and board[sel] != 'O' and sel != 0


def own(sel):
    return board[sel] == 'O' and sel != 0


board = ['', '1', '2', '3', '4', '5', '6', '7', '8', '9', ]
lines = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
square = 0
turns = 0
winner = ""

while turns < 9 and winner == "":
    print_board()

    # get new square to fill
    while square == 0:
        try:
            square = int(input('Your turn to play - Pick a square: '))
            if 0 < square < 10:
                pass
            else:
                square = 0

        except ValueError:
            square = 0

    # mark the square chosen
    if available(square):
        board[square] = "X"
        square = 0

    # Computer to play
    computer_turn = True

    for item in lines:
        if (own(item[0]) and own(item[1]) and not own(item[2]) and available(item[2]) and computer_turn or
                own(item[0]) and not own(item[1]) and own(item[2]) and available(item[1]) and computer_turn or
                not own(item[0]) and own(item[1]) and own(item[2]) and available(item[0]) and computer_turn):
            board[item[0]] = "O"
            board[item[1]] = "O"
            board[item[2]] = "O"
            turns += 1
            computer_turn = False

    for item in lines:
        if (not own(item[0]) and not available(item[0]) and
                not own(item[1]) and not available(item[1])
                and available(item[2]) and computer_turn):
            board[item[2]] = "O"
            turns += 1
            computer_turn = False

        if (not own(item[1]) and not available(item[1]) and
                not own(item[2]) and not available(item[2])
                and available(item[0]) and computer_turn):
            board[item[0]] = "O"
            turns += 1
            computer_turn = False

        if (not own(item[2]) and not available(item[2]) and
                not own(item[0]) and not available(item[0])
                and available(item[1]) and computer_turn):
            board[item[1]] = "O"
            turns += 1
            computer_turn = False

    while computer_turn:
        random_square = random.randint(1, 9)
        if available(random_square):
            board[random_square] = "O"
            turns += 1
            computer_turn = False

    if turns > 4:  # if  less than 4 box filled no winner can exist
        # Checks for a winner
        for item in lines:
            if board[item[0]] == board[item[1]] and board[item[1]] == board[item[2]]:
                winner = board[item[0]]

        if winner != "":
            print_board()
            print(f'The winner is {winner}')

        elif turns == 9:
            print_board()
            print("The game is a draw - No winner this time")
