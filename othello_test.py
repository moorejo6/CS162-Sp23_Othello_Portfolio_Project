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

    new_board = list(board)

    for row in range(10):
        for column in range(10):
            if new_board[row][column] == WHITE:
                new_board[row][column] = BLACK

            elif new_board[row][column] == BLACK:
                new_board[row][column] = WHITE

    return new_board


class OthelloUnitTests(unittest.TestCase):
    """Contains unit tests for the othello game"""

    def test_color_to_piece(self):
        """Tests the color_to_piece() method"""

        game = Othello()
        test_1_black, test_1_white = game.color_to_piece("black")
        test_2_white, test_2_black = game.color_to_piece("white")
        test_3_none1, test_3_none2 = game.color_to_piece("purple")

        self.assertTrue(test_1_black, BLACK)
        self.assertTrue(test_1_white, WHITE)
        self.assertTrue(test_2_white, WHITE)
        self.assertTrue(test_2_black, BLACK)
        self.assertIsNone(test_3_none1)
        self.assertIsNone(test_3_none2)

    def test_return_adjacent_coordinate(self):
        """Tests the return_adjacent_coordinate() method"""

        game = Othello()

        # Test basic functionality at center of board and verify output
        self.assertTrue(game.return_adjacent_coordinate("north", 5, 5), (4, 5))
        self.assertTrue(game.return_adjacent_coordinate("northeast", 5, 5), (4, 6))
        self.assertTrue(game.return_adjacent_coordinate("east", 5, 5), (5, 6))
        self.assertTrue(game.return_adjacent_coordinate("southeast", 5, 5), (6, 6))
        self.assertTrue(game.return_adjacent_coordinate("south", 5, 5), (6, 5))
        self.assertTrue(game.return_adjacent_coordinate("southwest", 5, 5), (6, 4))
        self.assertTrue(game.return_adjacent_coordinate("west", 5, 5), (5, 4))
        self.assertTrue(game.return_adjacent_coordinate("northwest", 5, 5), (4, 4))

        # Test edge cases (literally) to make sure "invalid" is returned correctly
        # Test the edges of the board first. We need to test the corners separately
        for row in range(len(game.get_board())):
            for column in range(len(game.get_board()[0])):

                # If we're at the top edge of the board, all northward directions should be invalid.
                if row == 0 and (0 < column < 9):
                    for direction in game.get_direction_list():
                        if direction == "north" or direction == "northeast" or direction == "northwest":
                            self.assertEqual(game.return_adjacent_coordinate(direction, row, column), "invalid")
                        else:
                            self.assertNotEqual(game.return_adjacent_coordinate(direction, row, column), "invalid")

                # If we're at the bottom edge of the board, all southward directions should be invalid
                if row == 9 and (0 < column < 9):
                    for direction in game.get_direction_list():
                        if direction == "south" or direction == "southeast" or direction == "southwest":
                            self.assertEqual(game.return_adjacent_coordinate(direction, row, column), "invalid")
                        else:
                            self.assertNotEqual(game.return_adjacent_coordinate(direction, row, column), "invalid")

                # If we're at the left edge of the board, all westward directions should be invalid
                if column == 0 and (0 < row < 9):
                    for direction in game.get_direction_list():
                        if direction == "west" or direction == "southwest" or direction == "northwest":
                            self.assertEqual(game.return_adjacent_coordinate(direction, row, column), "invalid")
                        else:
                            self.assertNotEqual(game.return_adjacent_coordinate(direction, row, column), "invalid")

                # If we're at the right edge of the board, all eastward directions should be invalid
                if column == 9 and (0 < row < 9):
                    for direction in game.get_direction_list():
                        if direction == "east" or direction == "southeast" or direction == "northeast":
                            self.assertEqual(game.return_adjacent_coordinate(direction, row, column), "invalid")
                        else:
                            self.assertNotEqual(game.return_adjacent_coordinate(direction, row, column), "invalid")

        # Test NE corner
        row, column = 0, 9
        for direction in game.get_direction_list():
            # The only valid spaces should be to the south, southwest, and west
            if direction == "south" or direction == "southwest" or direction == "west":
                self.assertNotEqual(game.return_adjacent_coordinate(direction, row, column), "invalid")
            else:
                self.assertEqual(game.return_adjacent_coordinate(direction, row, column), "invalid")

        # Test SE corner
        row, column = 9, 9
        for direction in game.get_direction_list():
            # The only valid spaces should be to the north, northwest, and west
            if direction == "north" or direction == "northwest" or direction == "west":
                self.assertNotEqual(game.return_adjacent_coordinate(direction, row, column), "invalid")
            else:
                self.assertEqual(game.return_adjacent_coordinate(direction, row, column), "invalid")

        # Test SW corner
        row, column = 9, 0
        for direction in game.get_direction_list():
            # The only valid spaces should be to the north, northeast, and east
            if direction == "north" or direction == "northeast" or direction == "east":
                self.assertNotEqual(game.return_adjacent_coordinate(direction, row, column), "invalid")
            else:
                self.assertEqual(game.return_adjacent_coordinate(direction, row, column), "invalid")

        # Test NW corner
        row, column = 0, 0
        for direction in game.get_direction_list():
            # The only valid spaces should be to the south, southeast, and east
            if direction == "south" or direction == "southeast" or direction == "east":
                self.assertNotEqual(game.return_adjacent_coordinate(direction, row, column), "invalid")
            else:
                self.assertEqual(game.return_adjacent_coordinate(direction, row, column), "invalid")


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

        # Save an inverted board to test the white pieces
        # inverted_board = invert_board(game.get_board())
        # print(type(inverted_board))
        # print(type(game.get_board()))

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




