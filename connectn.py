"""

Write a program to implement the game connect-n. Connect-n is like Connect-4 but the size of the board the number
of pieces in a row needed to win are user parameters. If you have never played Connect-4 before you can play it here:
 https://www.mathsisfun.com/games/connect4.html. The basic gist of the game is that each player takes a turn dropping one of
 their pieces into a column. Pieces land on top of pieces already played in that column. Each player is trying to get n pieces in
 a row either veritcally, horizontally or diagonally. The game ends if either player gets n pieces in a row or the board becomes full.
"""
def main():
    is_first_player = True
    board = []

    rows_columns_win_dependency = get_game_attributes()
    num_of_rows = rows_columns_win_dependency[0]
    num_of_columns = rows_columns_win_dependency[1]
    number_of_pieces_in_a_row_to_win =  rows_columns_win_dependency[2]

    make_empty_board(num_of_rows, num_of_columns, number_of_pieces_in_a_row_to_win)

    board = create_list(num_of_rows, num_of_columns, board)

    play_connectn(num_of_rows, num_of_columns, number_of_pieces_in_a_row_to_win, board, is_first_player)

def play_connectn(num_of_rows, num_of_columns, number_of_pieces_in_a_row_to_win, board, is_first_player):
    while True:
        while True:
            player_move = get_move(num_of_columns)
            if not is_column_full(board, player_move, num_of_rows):
                break

        column_position = spot_in_column(board, num_of_rows, player_move)

        update_board(board, player_move, is_first_player, column_position)

        display_board(num_of_rows, num_of_columns, board)

        player = ""
        if is_first_player == True:
            player = "1"
        else:
            player = "2"

        if game_won(board, number_of_pieces_in_a_row_to_win, num_of_rows, num_of_columns):
            print("Player",player,"won!")
            break
        elif is_tie_game(board):
            print("Tie Game")
            break

        is_first_player = not is_first_player

def update_board(board, player_move, is_first_player, column_position) -> list:
    game_piece = ""

    if is_first_player:
        game_piece = "X"
    else:
        game_piece = "O"

    board[column_position][player_move] = game_piece
    return board

def display_board(num_of_rows, num_of_columns, board) -> None:
    print("  ", end="")
    for i in range(num_of_columns):
        print(i, end=" ")
    print("")
    current_row = num_of_rows - 1
    for x in range(num_of_rows):
        print(current_row, end=" ")

        for item in board[x]:
            print(item, end = " ")
        print("")
        current_row -= 1

def is_column_full(board, player_move, num_of_rows) -> bool:
    is_full = False

    for i in range(num_of_rows - 1 , -1, -1):
        if board[i][player_move] == "*":
            return is_full
    return True

def spot_in_column(board, num_of_rows, player_move) -> int:
    #return the row in which is open
    for i in range(num_of_rows -1, -1, -1):
        if board[i][player_move] == "*":
            return i

def get_move(num_of_columns) -> int:
    #this returns a valid player move

    while True:
        move = input("Enter the column you want to play in: ")

        if not is_int(move):
            continue
        else:
            move = int(move)

        if 0 <= move or move <= num_of_columns - 1:
            return move
        else:
            continue

def game_won(board, number_of_pieces_in_a_row_to_win, num_of_rows, num_of_columns) -> bool:
    game_checker = False
    if row_win(board, number_of_pieces_in_a_row_to_win):
        game_checker = True
    elif col_win(board, number_of_pieces_in_a_row_to_win, num_of_rows, num_of_columns):
        game_checker = True
    elif diag_win(board, number_of_pieces_in_a_row_to_win, num_of_rows, num_of_columns):
        game_checker = True

    return game_checker

def row_win(board, number_of_pieces_in_a_row_to_win) -> bool:
    to_win = number_of_pieces_in_a_row_to_win
    did_win = False

    for row in board:
        checker = 0
        for pos in row:
            if pos == "X":
                checker += 1
            if checker == to_win:
                did_win = True
    for row in board:
        checker = 0
        for pos in row:
            if pos == "O":
                checker += 1
            if checker == to_win:
                did_win = True

    return did_win

def col_win(board, number_of_pieces_in_a_row_to_win, num_of_rows, num_of_columns) -> bool:
    to_win = number_of_pieces_in_a_row_to_win
    did_win = False

    for col in range(num_of_columns):
        checker = 0
        for i in range(num_of_rows - 1, -1, -1):
            if board[i][col] == "X":
                checker +=1
            if checker == to_win:
                did_win = True

    for col in range(num_of_columns):
        checker = 0
        for i in range(num_of_rows - 1, -1, -1):
            if board[i][col] == "O":
                checker +=1
            if checker == to_win:
                did_win = True
    return did_win


def diag_win(board, number_of_pieces_in_a_row_to_win, num_of_rows, num_of_columns) -> bool:
    diag_win_checker = False
    if right_diag_win(board, number_of_pieces_in_a_row_to_win, num_of_rows, num_of_columns):
        diag_win_checker = True
    elif left_diag_win(board, number_of_pieces_in_a_row_to_win, num_of_rows, num_of_columns):
        diag_win_checker = True

    return diag_win_checker


def right_diag_win(board, number_of_pieces_in_a_row_to_win, num_of_rows, num_of_columns) -> bool:
    did_win = False

    for row in range(num_of_rows -1, -1, -1):
        for col in range(num_of_columns):
            checker = 0
            n = 1
            if board[row][col] == "X":
                checker += 1
                while checker < number_of_pieces_in_a_row_to_win:
                    if board[row - n][col + n] == "X":
                        checker +=1
                        n += 1
                    else:
                        break
                if checker == number_of_pieces_in_a_row_to_win:
                    did_win = True
                    break
        if did_win == True:
            break

    for row in range(num_of_rows -1, -1, -1):
        for col in range(num_of_columns):
            checker = 0
            n = 1
            if board[row][col] == "O":
                checker += 1
                while checker < number_of_pieces_in_a_row_to_win:
                    if board[row - n][col + n] == "O":
                        checker +=1
                        n += 1
                    else:
                        break
                if checker == number_of_pieces_in_a_row_to_win:
                    did_win = True
                    break
        if did_win == True:
            break

    return did_win

def left_diag_win(board, number_of_pieces_in_a_row_to_win, num_of_rows, num_of_columns) -> bool:
    did_win = False

    for row in range(num_of_rows - 1, -1, -1):
        for col in range(num_of_columns):
            checker = 0
            n = 1
            if board[row][col] == "X":
                checker += 1
                while checker < number_of_pieces_in_a_row_to_win:
                    if board[row - n][col - n] == "X":
                        checker += 1
                        n += 1
                    else:
                        break
                if checker == number_of_pieces_in_a_row_to_win:
                    did_win = True
                    break
        if did_win == True:
            break

    for row in range(num_of_rows - 1, -1, -1):
        for col in range(num_of_columns):
            checker = 0
            n = 1
            if board[row][col] == "O":
                checker += 1
                while checker < number_of_pieces_in_a_row_to_win:
                    if board[row - n][col - n] == "O":
                        checker += 1
                        n += 1
                    else:
                        break
                if checker == number_of_pieces_in_a_row_to_win:
                    did_win = True
                    break
        if did_win == True:
            break

    return did_win




def is_tie_game(board) -> bool:
    is_tie = True
    for row in range(len(board)):
        for pos in board[row]:
            if pos == "*":
                is_tie = False
    return is_tie

def create_list(num_of_rows, num_of_columns, board) -> list:
    # creates a list of astericks, basically the same thing as make empty board but in list form
    for i in range(num_of_rows):
        board.append([])

    for column in board:
        for row in range(num_of_columns):
            column.append("*")

    return board

def make_empty_board(num_of_rows, num_of_columns, number_of_pieces_in_a_row_to_win) -> None:
    #creates an empty connectn board
    print("  ", end = "")
    for i in range(num_of_columns):

        print(i, end=" ")
    print("")
    current_row = num_of_rows - 1
    for i in range(num_of_rows):
        print(current_row, end= " ")

        for x in range(num_of_columns):
            print("*", end = " ")

        print("")

        current_row -= 1

def get_game_attributes() -> list:
    #returns a list of the game attributes such as num of rows,columns and how many pieces in a row to win
    rows_columns_win_dependency = []
    while True:
        number_of_rows = input("Enter the number of rows: ")

        if not is_int_greater_than_0(number_of_rows):
            continue
        else:
            number_of_rows = int(number_of_rows)
        break

    while True:
        number_of_columns = input("Enter the number of columns: ")

        if not is_int_greater_than_0(number_of_columns):
            continue
        else:
            number_of_columns = int(number_of_columns)
        break

    while True:
        number_of_pieces_in_a_row_to_win = input("Enter the number of pieces in a row to win: ")

        if not is_int_greater_than_0(number_of_pieces_in_a_row_to_win):
            continue
        else:
            number_of_pieces_in_a_row_to_win = int(number_of_pieces_in_a_row_to_win)

        break

    rows_columns_win_dependency.append(number_of_rows)
    rows_columns_win_dependency.append(number_of_columns)
    rows_columns_win_dependency.append(number_of_pieces_in_a_row_to_win)

    return rows_columns_win_dependency

def is_int_greater_than_0(number) -> bool:
    #checks if user input is int greater than 0
    try:
        int(number)
    except ValueError:
        return False
    number = int(number)

    if number > 0:
        return True
    else:
        return False

def is_int(number):
    try:
        int(number)
    except ValueError:
        return False
    return True

if __name__ == "__main__":
    main()