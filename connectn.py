"""

Write a program to implement the game connect-n. Connect-n is like Connect-4 but the size of the board the number
of pieces in a row needed to win are user parameters. If you have never played Connect-4 before you can play it here:
 https://www.mathsisfun.com/games/connect4.html. The basic gist of the game is that each player takes a turn dropping one of
 their pieces into a column. Pieces land on top of pieces already played in that column. Each player is trying to get n pieces in
 a row either veritcally, horizontally or diagonally. The game ends if either player gets n pieces in a row or the board becomes full.


"""

def main():
    is_player_one = True
    board = []

    rows_columns_win_dependency = get_game_attributes()
    num_of_rows = rows_columns_win_dependency[0]
    num_of_columns = rows_columns_win_dependency[1]
    number_of_pieces_in_a_row_to_win =  rows_columns_win_dependency[2]

    make_empty_board(num_of_rows, num_of_columns, number_of_pieces_in_a_row_to_win)

    board = create_list(num_of_rows, num_of_columns, board)
    board.reverse()



    play_connectn(num_of_rows, num_of_columns, number_of_pieces_in_a_row_to_win, board, is_player_one)




def play_connectn(num_of_rows, num_of_columns, number_of_pieces_in_a_row_to_win, board, is_player_one):

    while not is_game_over():

        while True:
            player_move = get_move(num_of_columns)
            if is_valid_move():
                break
            #adding break for right now
            break


        #the below is the method that is causing board to return none
        board = update_board(board, player_move, is_player_one)

        display_board(num_of_rows, num_of_columns, board)


        # check winner






def update_board(board, player_move, is_player_one) -> list:
    #this method is under the assumption that the move entered is valid and there is room in that column
    #^ might change and might wanna place that check in this method and handle the error with an exception

    #left off on this method try to add the update here







def is_valid_move() -> bool:

    # add counter to see if there is even any room on the board
    pass



def get_move(num_of_columns) -> int:
    #this returns a valid player move
    #not fully done yet because u need to check if the column is full first, prob need more info
    #use is valid move to help with above comment
    #there are some problems with this method -> LIKE WHEN you enter the max column it gives an error

    while True:
        move = input("Enter the column you want to play in: ")

        if not is_int_greater_than_0(move):
            continue
        else:
            move = int(move)

        if 0 <= move or move <= num_of_columns - 1:
            return move

        else:
            print("check2")
            continue






















def is_game_over() -> bool:
    if game_won() or is_tie_game():
        pass



def game_won() -> bool:
    game_checker = False
    if row_win():
        game_checker = True
    elif col_win():
        game_checker = True
    elif diag_win():
        game_checker = True
    else:
        pass




def row_win() -> bool:
    pass


def col_win() -> bool:
    pass


def diag_win() -> bool:
    diag_win_checker = False
    if right_diag_win():
        diag_win_checker = True
    elif left_diag_win():
        diag_win_checker = True

    return diag_win_checker


def right_diag_win() -> bool:
    pass


def left_diag_win() -> bool:
    pass


def is_tie_game() -> bool:
    #check to see if there are any astericks in board
    pass







def create_list(num_of_rows, num_of_columns, board) -> list:
    # creates a list of astericks, basically the same thing as make empty board but in list form

    for i in range(num_of_columns):
        board.append([])

    for column in board:
        for row in range(num_of_rows + 1):
            column.append("*")

    return board





def display_board(num_of_rows, num_of_columns, board) -> None:
    print(board)
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

if __name__ == "__main__":
    main()
    #create_list(5,6,[])
