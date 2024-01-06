import random


def first_player():
    return random.randint(0, 1)


def change_turn(player):
    return 'X' if player == 'O' else 'O'


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):

        n = len(self.board)

        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if first_player() == 1 else 'O'
        while True:
            print(f"Player {player}'s turn.")

            self.show_board()

            row, col = list(
                map(int, input("Enter a number for a row and a column:").split()))
            print()

            self.fix_spot(row - 1, col - 1, player)

            if self.is_player_win(player):
                print(f"Player {player} has won the game.")
                break

            if self.is_board_filled():
                print("Looks like a draw!")
                break

            player = change_turn(player)

        print()
        self.show_board()


tic_tac_toe = TicTacToe()
tic_tac_toe.start()