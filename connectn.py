"""

Write a program to implement the game connect-n. Connect-n is like Connect-4 but the size of the board the number
of pieces in a row needed to win are user parameters. If you have never played Connect-4 before you can play it here:
 https://www.mathsisfun.com/games/connect4.html. The basic gist of the game is that each player takes a turn dropping one of
 their pieces into a column. Pieces land on top of pieces already played in that column. Each player is trying to get n pieces in
 a row either veritcally, horizontally or diagonally. The game ends if either player gets n pieces in a row or the board becomes full.


"""

def main():
    get_game_attributes()












def get_game_attributes() -> list:
    #returns a list of the game attributes such as num of rows,columns and how many pieces in a row to win
    rows_columns_win_depedency = []
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

    rows_columns_win_depedency.append(number_of_rows)
    rows_columns_win_depedency.append(number_of_columns)
    rows_columns_win_depedency.append(number_of_pieces_in_a_row_to_win)

    return rows_columns_win_depedency


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