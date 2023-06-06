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

        # Test edge cases (literally) to make sure "invalid" is returned correctly.
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

    def test_return_piece_locations(self):
        """Tests the return_piece_locations() method"""

        game = Othello()

        # Test on starting board configuration
        test1_black_start = game.return_piece_locations("black")
        test2_white_start = game.return_piece_locations("white")
        test1_answer = [[4, 5], [5, 4]]
        test2_answer = [[4, 4], [5, 5]]

        self.assertEqual(test1_black_start, test1_answer)
        self.assertEqual(test2_white_start, test2_answer)

        # Add some more pieces to the board
        game._board[1][1] = BLACK
        game._board[2][4] = BLACK
        game._board[3][6] = BLACK
        game._board[4][8] = BLACK
        test3_scattered_black_pieces = game.return_piece_locations("black")
        test3_answer = [[1, 1], [2, 4], [3, 6], [4, 5], [4, 8], [5, 4]]

        game._board[8][1] = WHITE
        game._board[7][6] = WHITE
        game._board[6][2] = WHITE
        game._board[5][7] = WHITE
        test4_scattered_white_pieces = game.return_piece_locations("white")
        test4_answer = [[4, 4], [5, 5], [5, 7], [6, 2], [7, 6], [8, 1]]

        # Test results
        self.assertEqual(test3_scattered_black_pieces, test3_answer)
        self.assertEqual(test4_scattered_white_pieces, test4_answer)

    def test_flip_pieces_all_directions(self):
        """Contains Unit tests for the flip_pieces() method"""

        game = Othello()

        # Generate a board to test white to black token flips in all directions
        capturing_color_locations = [[5, 4], [1, 4], [8, 4], [5, 1], [5, 8], [8, 1], [1, 8], [2, 1], [8, 7]]
        captured_color_locations = [[2, 4], [3, 4], [4, 4], [6, 4], [7, 4], [5, 2], [5, 3], [5, 5], [5, 6], [5, 7],
                                    [7, 2], [6, 3], [4, 5], [3, 6], [2, 7], [3, 2], [4, 3], [4, 4], [6, 5], [7, 6]]
        test1_board = generate_board(capturing_color_locations, captured_color_locations)
        game._board = test1_board

        # Generate the answer board
        test_answer = [[5, 4], [1, 4], [8, 4], [5, 1], [5, 8], [8, 1], [1, 8], [2, 1], [8, 7], [2, 4], [3, 4], [4, 4],
                       [6, 4], [7, 4], [5, 2], [5, 3], [5, 5], [5, 6], [5, 7], [7, 2], [6, 3], [4, 5], [3, 6], [2, 7],
                       [3, 2], [4, 3], [4, 4], [6, 5], [7, 6]]
        test1_answer_board = generate_board(test_answer, [])  # All token locations should be black

        # Flip the tokens and check the results
        print("UNITTEST:: Board configuration before running flip_pieces():")
        game.print_board()
        print("UNITTEST:: Board configuration after running flip_pieces():")
        game.flip_pieces("black", 5, 4)
        game.print_board()
        self.assertEqual(game.get_board(), test1_answer_board)

        # Run the same test with black to white token flips...
        test2_board = generate_board(captured_color_locations, capturing_color_locations)
        game._board = test2_board
        test2_answer_board = generate_board([], test_answer)  # All token locations should be white

        # Flip the tokens and check the results
        print("UNITTEST:: Board configuration before running flip_pieces():")
        game.print_board()
        print("UNITTEST:: Board configuration after running flip_pieces():")
        game.flip_pieces("white", 5, 4)
        game.print_board()
        self.assertEqual(game.get_board(), test2_answer_board)

    def test_return_available_positions(self):
        """Contains unit tests for the return_available_positions() method"""