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


class OthelloUnitTests(unittest.TestCase):
    """Contains unit tests for the othello game"""

    def test_create_player(self):
        """Tests the crete_player() method"""

        game = Othello()

        # Create new players
        game.create_player("Test Player", "black")
        game.create_player("Test Player2", "white")
        players = game.get_player_list()

        # Test results
        self.assertEqual(players[0].get_name(), "Test Player")
        self.assertEqual(players[0].get_color(), "black")
        self.assertEqual(players[1].get_name(), "Test Player2")
        self.assertEqual(players[1].get_color(), "white")

        # Overwrite previous players
        game.create_player("new black player", "black")
        game.create_player("new white player", "white")
        players = game.get_player_list()

        # Test results
        self.assertEqual(players[0].get_name(), "new black player")
        self.assertEqual(players[0].get_color(), "black")
        self.assertEqual(players[1].get_name(), "new white player")
        self.assertEqual(players[1].get_color(), "white")

    def test_return_winner(self):
        """Tests the return_winner() method"""

        game = Othello()

        # Test in starting board position
        self.assertEqual(game.return_winner(), "It's a tie")

        # Add some black pieces and test
        game._board[2][2] = BLACK
        game._board[3][3] = BLACK
        self.assertEqual(game.return_winner(), "Winner is black player: Player 1")

        # Add some white pieces and test
        game._board[7][6] = WHITE
        game._board[7][7] = WHITE
        game._board[7][8] = WHITE
        self.assertEqual(game.return_winner(), "Winner is white player: Player 2")

    def test_return_available_positions(self):
        """Contains unit tests for the return_available_positions() method"""

        game = Othello()

        # Test starting locations
        test1_answer = [[6, 5], [4, 3], [3, 4], [5, 6]]
        test2_answer = [[4, 6], [6, 4], [3, 5], [5, 3]]
        self.assertEqual(game.return_available_positions("black"), test1_answer)
        self.assertEqual(game.return_available_positions("white"), test2_answer)

        # Create a new test board for a scenario where it's white's turn to move
        opponent_locations = [[3, 4], [3, 5], [4, 4], [4, 5], [5, 3], [5, 5], [6, 2], [6, 6]]
        active_player_locations = [[3, 6], [4, 3], [5, 4]]
        test3_board = generate_board(opponent_locations, active_player_locations)
        game._board = test3_board

        # Create the answer and test the results
        test3_answer = [[3, 3], [2, 5], [4, 6], [6, 3], [2, 4], [5, 6], [5, 2]]
        print(f"UNITTEST:: test_return_available_positions test 3 board (white to move):")
        game.print_available_positions("white")
        self.assertEqual(game.return_available_positions("white"), test3_answer)

        # Create a new test board for a scenario where it's black's turn to move
        active_player_locations = [[3, 3], [4, 4], [4, 5], [4, 7], [5, 4]]
        opponent_locations = [[3, 7], [4, 6], [5, 5], [6, 5], [7, 5]]
        test4_board = generate_board(active_player_locations, opponent_locations)
        game._board = test4_board

        # Create the answer and test the results
        test4_answer = [[6, 6], [8, 5], [2, 7], [5, 6], [7, 6]]
        print(f"UNITTEST:: test_return_available_positions test 4 board (black to move):")
        game.print_available_positions("black")
        self.assertEqual(game.return_available_positions("black"), test4_answer)

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
        print("UNITTEST test_flip_pieces_all_directions:: Board configuration test 1:")
        game.print_board()
        game.flip_pieces("black", [5, 4])
        game.print_board()
        self.assertEqual(game.get_board(), test1_answer_board)

        # Run the same test with black to white token flips...
        test2_board = generate_board(captured_color_locations, capturing_color_locations)
        game._board = test2_board
        test2_answer_board = generate_board([], test_answer)  # All token locations should be white

        # Flip the tokens and check the results
        print("UNITTEST test_flip_pieces_all_directions:: Board configuration test 2:")
        game.print_board()
        game.flip_pieces("white", [5, 4])
        game.print_board()
        self.assertEqual(game.get_board(), test2_answer_board)

    def test_make_move(self):
        """Tests the make_move() method"""

        game = Othello()

        # Generate a board starting with the first flip pieces test
        player_locations = [[1, 4], [8, 4], [5, 1], [5, 8], [8, 1], [1, 8], [2, 1], [5, 5], [3, 6]]
        opponent_locations = [[2, 4], [3, 4], [4, 4], [6, 4], [7, 4], [5, 2], [5, 6], [5, 7], [7, 2], [6, 3], [4, 5],
                              [2, 7], [3, 2], [4, 3], [4, 4], [6, 5], [7, 6], [8, 7]]
        test1_board = generate_board(player_locations, opponent_locations)
        game._board = test1_board

        # Generate an answer board
        player_locations = [[1, 4], [1, 8], [2, 1], [2, 4], [3, 2], [3, 4], [3, 6], [4, 3], [4, 4], [4, 5],
                            [5, 1], [5, 4], [5, 5], [5, 8], [6, 3], [6, 4], [7, 2], [7, 4], [8, 1], [8, 4]]
        opponent_locations = [[2, 7], [5, 2], [5, 6], [5, 7],  [6, 5], [7, 6], [8, 7]]
        test1_answer = generate_board(player_locations, opponent_locations)

        print(f"UNITTEST test_make_move: Board position test 1, black to place piece at [5,4]: ")
        game.print_board()
        game.make_move("black", [5, 4])
        game.print_board()
        self.assertEqual(game.get_board(), test1_answer)
