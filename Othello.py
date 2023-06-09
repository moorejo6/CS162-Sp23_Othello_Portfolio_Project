# Author: Jordan Moore
# GitHub username: moorejo6
# Date: 5/15/23
# Description: TODO: ADD DESCRIPTION
# ---------------------------------------------------------------------------------------------------------------------------

def generate_board(black_token_locations=None, white_token_locations=None):
    """Returns an Othello board with black and white tokens placed at the provided coordinates. If no coordinates are given,
    pieces are placed at their starting location"""

    board = []

    # If no black token locations were passed into the function, use the starting token locations
    if black_token_locations is None:
        black_token_locations = [[4, 5], [5, 4]]

    # If no white token locations were passed into the function, use the starting token locations
    if white_token_locations is None:
        white_token_locations = [[4, 4], [5, 5]]

    # Generate the borders and empty spaces of the board
    for row in range(10):
        board_row = []
        for column in range(10):
            if (row == 0 or row == 9) or (column == 0 or column == 9):
                board_row.append("*")
            else:
                board_row.append(".")
        board.append(board_row)

    # Place the black tokens on the board
    for token in black_token_locations:
        board[token[0]][token[1]] = "X"

    # Place the white tokens on the board
    for token in white_token_locations:
        board[token[0]][token[1]] = "O"

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
        self._direction_list = ["north", "northeast", "east", "southeast", "south", "southwest", "west", "northwest"]
        self._coordinate_shift = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
        self._player_list = []

    def get_board(self):
        """Returns the current game board"""
        return self._board

    def get_direction_list(self):
        """Returns the direction list"""
        return self._direction_list

    def get_player_list(self):
        """Returns the player list"""
        return self._player_list

    def print_board(self):
        """Prints the current state of the Othello board. Returns nothing."""

        for row in range(len(self._board)):
            for column in range(len(self._board[row])):
                print(self._board[row][column], end=" ")
            print("")

    def create_player(self, player_name, color):
        """TODO: ADD DOCSTRING"""

        print("DEBUG:: in Othello.create_player()")

    def return_winner(self):
        """TODO: ADD DOCSTRING"""

        num_black_pieces = len(self.return_piece_locations("black"))
        num_white_pieces = len(self.return_piece_locations("white"))
        black_player = self._player_list[0]
        white_player = self._player_list[1]
        winner_string = ""

        if num_black_pieces > num_white_pieces:
            winner_string = "Winner is black player: " + black_player.get_name()

        elif num_white_pieces > num_black_pieces:
            winner_string = "Winner is white player: " + white_player.get_name()

        else:
            winner_string = "It's a tie"

        return winner_string

    # Finished first draft 6/4. Unit Tests implemented 6/4
    def color_to_piece(self, color):
        """Takes one parameter:
        color - The color of the current players piece

        Purpose: Translates the player color into strings that represent the player and opponent's pieces.

        Returns two strings: one of the current player's pieces and another representing the opponent's pieces """

        player_piece = None
        opponent_piece = None

        if color.lower() == "black":
            player_piece = "X"
            opponent_piece = "O"
        elif color.lower() == "white":
            player_piece = "O"
            opponent_piece = "X"
        else:
            print(f"ERROR in Othello.color_to_piece:: Invalid color: {color}")

        return player_piece, opponent_piece

    # Finished first draft 6/2
    def flip_pieces(self, color, row, column):
        """Takes three parameters:
        color - The color of the current players pieces
        row, column - the row,column coordinate pair for the staring location.

        Purpose: Starting from the given coordinate pair, this method will check for and perform valid flip moves in
        all 8 cardinal directions

        Returns: nothing"""

        player_piece, opponent_piece = self.color_to_piece(color)

        # Check every direction for valid pieces to flip
        for shift in self._coordinate_shift:
            self.rec_flip_pieces(shift, player_piece, opponent_piece, row, column)

    # Finished first draft 6/2
    def rec_flip_pieces(self, shift, player_piece, opponent_piece, row, column):
        """TODO: ADD DOCSTRING"""

        # Get the value of the adjacent space in the given direction

        adj_row = row + shift[0]
        adj_column = column + shift[1]
        adj_value = self._board[adj_row][adj_column]

        # Base case 1: We hit a wall. No valid flips.
        if adj_value == "*":
            return False

        # Base case 2: We found an empty space. No valid flips
        if adj_value == ".":
            return False

        # Base case 3: We found the current player's piece.
        #              This indicates that we should flip the pieces we passed over.
        if adj_value == player_piece:
            return True

        # Recursive case: We're following a trail of the opponent's pieces
        if adj_value == opponent_piece:

            # If we eventually find the current player's piece, we should flip the value on the board
            if self.rec_flip_pieces(shift, player_piece, opponent_piece, adj_row, adj_column):
                self._board[adj_row][adj_column] = player_piece
                return True
            else:
                return False

    # Finished first draft 6/3
    def return_piece_locations(self, color):
        """Takes one parameter:
        color - The color to look for on the game board

        Purpose: Creates a list of all coordinate locations on the game board that contain a given color piece.
        This provides the starting locations for the return_available_positions() method.

        Returns: A list that contains the coordinate location of every piece of the given color."""

        player_piece, opponent_piece = self.color_to_piece(color)
        piece_locations = []

        number_of_rows = len(self._board)
        number_of_columns = len(self._board[0])

        for row in range(number_of_rows):
            for column in range(number_of_columns):
                if self._board[row][column] == player_piece:
                    piece_locations.append([row, column])

        return piece_locations

    def return_available_positions(self, color):
        """TODO: ADD DOCSTRING"""

        player_piece, opponent_piece = self.color_to_piece(color)
        player_token_locations = self.return_piece_locations(color)
        valid_move_list = []

        # For every token the player has on the board, search all directions around the token for available moves
        for token in player_token_locations:
            for shift in self._coordinate_shift:

                possible_move = self.rec_return_available_positions(shift, player_piece, opponent_piece, token[0], token[1])

                if possible_move is not None and possible_move not in valid_move_list:
                    valid_move_list.append(possible_move)

        return valid_move_list

    def rec_return_available_positions(self, shift, player_piece, opponent_piece, row, column, value=None):
        """TODO: ADD DOCSTRING"""

        adj_row = row + shift[0]
        adj_column = column + shift[1]
        adj_value = self._board[adj_row][adj_column]

        # Base case 1: We hit a wall. Not a valid move.
        if adj_value == "*":
            return None

        # Base case 2: We found an empty space. This indicates a valid position to move.
        if adj_value == "." and value is not None:
            return [adj_row, adj_column]

        # Base case 3: We found the current player's piece. Not a valid move
        if adj_value == player_piece:
            return None

        # Recursive case: We're following a trail of the opponent's pieces
        if adj_value == opponent_piece:
            return self.rec_return_available_positions(shift, player_piece, opponent_piece, adj_row, adj_column, adj_value)


def test_game_loop():
    """FOR DEBUG USE ONLY! TODO: DELETE BEFORE SUBMISSION!"""

    game = Othello()
    board_row_length = len(game.get_board())
    board_column_length = len(game.get_board()[0])
    user_input = ""
    current_player = "black"

    while True:

        player_piece, opponent_piece = game.color_to_piece(current_player)
        valid_moves = game.return_available_positions(current_player)

        if valid_moves != []:
            for move in valid_moves:
                game._board[move[0]][move[1]] = "+"
        game.print_board()

        for row in range(board_row_length):
            for column in range(board_column_length):
                if game._board[row][column] == "+":
                    game._board[row][column] = "."

        print(f"{current_player} has {len(game.return_piece_locations(current_player))} tokens on the board")
        print(f"{len(valid_moves)} moves are available: {valid_moves}")

        player_row = None
        player_column = None
        valid_move = False

        while not valid_move:
            player_row = int(input(f"{current_player}'s turn. What row do you want to move to? "))
            player_column = int(input("What column do you want to move to? "))

            if [player_row, player_column] in valid_moves:
                valid_move = True
            else:
                print(f"({player_row}, {player_column}) is an invalid move. Valid moves are:")
                print(valid_moves)

        game._board[player_row][player_column] = player_piece
        game.flip_pieces(current_player, player_row, player_column)

        if current_player == "black":
            current_player = "white"
        else:
            current_player = "black"


def main():
    test_game_loop()


if __name__ == "__main__":
    main()
