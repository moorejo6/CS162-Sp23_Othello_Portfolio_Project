# Author: Jordan Moore
# GitHub username: moorejo6
# Date: 5/15/23
# Description: Contains unit tests for the othello.py game
# ---------------------------------------------------------------------------------------------------------------------------

import unittest
from Othello import *

EMPTY = "."
WALL = "*"
BLACK = "X"
WHITE = "O"

def invert_board(board):
    """Inverts the color of the pieces on the board. Used for testing configurations on both colors"""

    for row in range(10):
        for column in range(10):
            if board[row][column] == WHITE:
                board[row][column] = BLACK

            elif board[row][column] == BLACK:
                board[row][column] = WHITE

    return board

class OthelloUnitTests(unittest.TestCase):
    """Contains unit tests for the othello game"""

    def test_flip_pieces__all_directions(self):
        """Contains Unit tests for the flip_pieces() method"""

        print("UNITTEST:: Testing capture in all directions...")
        # Create a new game
        game = Othello()

        # Clear out the board except for the central X piece
        game._board[4][4] = EMPTY
        game._board[4][5] = EMPTY
        game._board[5][5] = EMPTY


        # Add white pieces in all vertical directions
        game._board[1][4] = BLACK
        game._board[2][4] = WHITE
        game._board[3][4] = WHITE
        game._board[4][4] = WHITE
        game._board[6][4] = WHITE
        game._board[7][4] = WHITE
        game._board[8][4] = BLACK

        # Add white pieces in all horizonal directions
        game._board[5][1] = BLACK
        game._board[5][2] = WHITE
        game._board[5][3] = WHITE
        game._board[5][5] = WHITE
        game._board[5][6] = WHITE
        game._board[5][7] = WHITE
        game._board[5][8] = BLACK

        # Add white pieces in all positive diagonal directions
        game._board[8][1] = BLACK
        game._board[7][2] = WHITE
        game._board[6][3] = WHITE
        game._board[4][5] = WHITE
        game._board[3][6] = WHITE
        game._board[2][7] = WHITE
        game._board[1][8] = BLACK

        # Add white pieces in all negative diagonal directions
        game._board[2][1] = BLACK
        game._board[3][2] = WHITE
        game._board[4][3] = WHITE
        game._board[4][4] = WHITE
        game._board[6][5] = WHITE
        game._board[7][6] = WHITE
        game._board[8][7] = BLACK

        # # Save an inverted board to test the white pieces
        # inverted_board = list(invert_board(game.get_board()))

        # Flip them
        print("UNITTEST:: Board configuration before running flip_pieces():")
        game.print_board()

        game.flip_pieces("black", 5, 4)

        print("UNITTEST:: Board configuration after running flip_pieces():")
        game.print_board()



        # # Test flipping white pieces
        # game._board = inverted_board
        # print("UNITTEST:: Board configuration before running flip_pieces():")
        # game.print_board()
        #
        # game.flip_pieces("white", 5, 4)
        #
        # print("UNITTEST:: Board configuration after running flip_pieces():")
        # game.print_board()




