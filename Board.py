class Board:

    def __init__(self, size):
        self.board = []
        self.count_turns = 0
        self.size = size
        self.win = False
        for i in range(size):
            row = []
            for c in range(size):
                row.append(' - ')
            self.board.append(row)

    # def create_board(self, size):
    #     #list of n lists as rows and columns

    def is_board_filled(self) ->bool:
        #check whether the board still has empty spots
        for row in self.board:
            for item in row:
                if item == ' - ':
                    return False
        return True

    def show_board(self):
        for i, col in enumerate(self.board):
            print(f"    { i }  ", end="")
        print()
        print("",'-------' * len(self.board))
        for i, row in enumerate(self.board):
            print(i, end="")
            for item in row:
                print('|', item, '|', end="")
            print()
            print("",'-------' * len(self.board))

    def get_player(self):
        if self.count_turns % 2 == 0:
            return ' X '
        else:
            return ' O '

    def get_spot(self):
        while True:
            row = input("Pick a row: ")
            col = input("Pick a column: ")
            if row.isdigit() and col.isdigit():
                row = int(row)
                col = int(col)
                if 0 <= row <= self.size-1 and 0 <= col <= self.size-1:
                    if self.board[row][col] == ' - ':
                        return row, col
                    print("This spot has been already filled, pick again - ")
                print("out of range")

    def update_board(self, player, row, col):
        self.board[row][col] = player

    def check_row_win(self, player):
        # check the rows:
        self.win = True
        for row in self.board:
            for item in row:
                if item != player:
                    self.win = False
            if self.win:
                print("row completed!")
                return True

    def check_col_win(self, player):
        for i in range(self.size):
            self.win = True
            for j in range(self.size):
                if self.board[j][i] != player:
                    self.win = False
            if self.win:
                print("column complete!")
                return True

    def check_diagonal_win(self, player):
        self.win = True
        for i in range(self.size):
            if self.board[i][i] != player:
                self.win = False
                break
        if self.win:
            print("diagonal completed!")
            return True
        self.win = True
        for i in range(self.size):
            if self.board[i][self.size - 1 - i] != player:
                self.win = False
                break
        if self.win:
            print("diagonal completed!")
            return True

    def is_win(self, player):
        if self.check_row_win(player) == True:
            print(f"player {player} - you won!")
            return True
        if self.check_col_win(player) == True:
            print(f"player {player} - you won!")
            return True
        if self.check_diagonal_win(player) == True:
            print(f"player {player} - you won!")
            return True

    def is_stuck_row(self):
        # check if in row and col and diagonal there's X and O
        count = 0
        for row in self.board:
            if ' X ' in row and ' O ' in row:
                count += 1
                if count == self.size:
                    return True
        return False

    def is_stuck_col(self):
        columns = []
        for i in range(self.size):
            col = []
            for j in range(self.size):
                col.append(self.board[j][i])
            columns.append(col)
        count = 0
        for col in columns:
            if ' X ' in col and ' O ' in col:
                count += 1
                if count == self.size:
                    return True
        return False

    def is_stuck_diagonal(self):
        diagonal1 = []
        stuck = False
        for j in range(self.size):
            diagonal1.append(self.board[j][j])
        if ' X ' in diagonal1 and ' O ' in diagonal1:
            stuck = True
            if stuck:
                diagonal2 = []
                for j in range(self.size):
                    diagonal2.append(self.board[j][self.size - j - 1])
                if ' X ' in diagonal2 and ' O ' in diagonal2:
                    return True
            return False
# my_board = Board()
# my_board.create_board(3)
# my_board.show_board()
