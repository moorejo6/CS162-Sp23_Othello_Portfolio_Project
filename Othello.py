# Author: Jordan Moore
# GitHub username: moorejo6
# Date: 5/15/23
# Description: TODO: ADD DESCRIPTION
# ---------------------------------------------------------------------------------------------------------------------------

def generate_board():
    """Returns an Othello board with initial black and white pieces set"""

    board = []

    for row in range(10):
        board_row = []
        for column in range(10):
            if (row == 0 or row == 9) or (column == 0 or column == 9):
                board_row.append("*")
            else:
                board_row.append(".")

        print(f"DEBUG:: row {row}: {board_row}")
        board.append(board_row)

    board[4][4] = "O"
    board[5][5] = "O"
    board[4][5] = "X"
    board[5][4] = "X"

    return board


class Player:
    """TODO: ADD DOCSTRING"""

    def __init__(self, name, color):
        self._name = name
        self._color = color  # TODO: handle invalid player color?

    def get_name(self):
        """Returns the player's name"""
        return self._name

    def get_color(self):
        """Returns the player's color"""
        return self._color


class Othello:  # TODO: Check style guide lines for classes
    """TODO: ADD DOCSTRING"""

    def __init__(self):
        self._board = generate_board()

    def get_board(self):
        """Returns the current game board"""
        return self._board

    def print_board(self):
        """TODO: ADD DOCSTRING"""

        for row in range(len(self._board)):
            for column in range(len(self._board[row])):
                print(self._board[row][column], end=" ")
            print("")

    def create_player(self, player_name, color):
        """TODO: ADD DOCSTRING"""

        print("DEBUG:: in Othello.create_player()")

    def return_winner(self):
        """TODO: ADD DOCSTRING"""

        print("DEBUG:: in Othello.return_winner()")



def main():
    game = Othello()
    game.print_board()
    print(len(game.get_board()))


if __name__ == "__main__":
    main()
