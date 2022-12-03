from Board import Board

def get_size():
    print()
    print("                 * * * * *   Welcome to the Tic-Tac Toe game!   * * * * * ")
    while True:
        size = input("Insert board size between 3 to 9 (3x3 --> 9x9): ")
        if size.isdigit():
            size = int(size)
            if 3 <= size <= 9:
                return size
        print("wrong insert, please insert again -")

def start_game():
    print()
    print("here is the game board: ")
    print()
    my_board.show_board()
    while True:
        player = my_board.get_player()
        print(f"Player {player} it's your turn!")
        row, col = my_board.get_spot()
        my_board.update_board(player, row, col)
        my_board.show_board()
        win = my_board.is_win(player)
        if win == True:
            break
        if my_board.is_board_filled() == True:
            print("Game over, no winner")
            break
        if my_board.is_stuck_col() == True and my_board.is_stuck_row() == True and my_board.is_stuck_diagonal() == True:
            print("Game is stuck, no winner")
            break
        my_board.count_turns += 1

if __name__ == "__main__":
    size = get_size()
    my_board = Board(size)

    start_game()

    another_game = input("want one more game? y/n ")
    if another_game == 'y':
        size = get_size()
        my_board = Board(size)
        start_game()
    else:
        print("ByeBye")

