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


    def flip_pieces(self, color, row, column):
        """TODO: ADD DOCSTRING"""

        player_piece = None
        opponent_piece = None

        if color.lower() == "black":
            player_piece = "X"
            opponent_piece = "O"
        elif color.lower() == "white":
            player_piece = "O"
            opponent_piece = "X"
        else:
            print(f"ERROR:: Color {color} not recognized.")

        self.rec_flip_pieces("north", player_piece, opponent_piece, row, column)
        self.rec_flip_pieces("northeast", player_piece, opponent_piece, row, column)
        self.rec_flip_pieces("east", player_piece, opponent_piece, row, column)
        self.rec_flip_pieces("southeast", player_piece, opponent_piece, row, column)
        self.rec_flip_pieces("south", player_piece, opponent_piece, row, column)
        self.rec_flip_pieces("southwest", player_piece, opponent_piece, row, column)
        self.rec_flip_pieces("west", player_piece, opponent_piece, row, column)
        self.rec_flip_pieces("northwest", player_piece, opponent_piece, row, column)


    def rec_flip_pieces(self, direction, player_piece, opponent_piece, row, column):
        """TODO: ADD DOCSTRING"""

        if direction == "north":
            row -= 1
        elif direction == "northeast":
            row -= 1
            column += 1
        elif direction == "east":
            column += 1
        elif direction == "southeast":
            row += 1
            column += 1
        elif direction == "south":
            row += 1
        elif direction == "southwest":
            row += 1
            column -= 1
        elif direction == "west":
            column -= 1
        elif direction == "northwest":
            row -= 1
            column -= 1
        else:
            print(f"ERROR:: Invalid direction {direction}")

        piece_at_location = self._board[row][column]

        # Base case 1: We reach a wall. No valid flips.
        if piece_at_location == "*":
            return False

        # Base case 2: We reach an empty space. No valid flips
        if piece_at_location == ".":
            return False

        # Base case 3: We reach the current player's piece. Return True
        if piece_at_location == player_piece:
            return True

        # Recursive case: We're following the trail of the opponent's pieces
        if piece_at_location == opponent_piece:

            if self.rec_flip_pieces(direction, player_piece, opponent_piece, row, column):
                self._board[row][column] = player_piece
                return True


def main():
    game = Othello()
    game.print_board()

    # game._board[5][6] = "X"
    game._board[6][6] = "O"
    game._board[7][6] = "O"
    game._board[8][6] = "X"

    game._board[5][1] ="X"
    game._board[5][2] ="O"
    game._board[5][3] ="O"
    game._board[5][4] ="O"
    game._board[4][6] = "O"
    game._board[3][6] = "X"

    game.print_board()
    game._board[5][6] = "X"
    game.flip_pieces("black", 5, 6)
    # game.rec_flip_test("black", "south", 5, 6)
    # game.rec_flip_test("black", "west", 5, 6)
    game.print_board()


if __name__ == "__main__":
    main()
