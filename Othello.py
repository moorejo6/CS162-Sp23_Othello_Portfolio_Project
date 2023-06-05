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
        self._direction_list = ["north", "northeast", "east", "southeast",
                                "south", "southwest", "west", "northwest"]

    def get_board(self):
        """Returns the current game board"""
        return self._board

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

        print("DEBUG:: in Othello.return_winner()")

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
        for direction in self._direction_list:
            self.rec_flip_pieces(direction, player_piece, opponent_piece, row, column)
        # self.rec_flip_pieces("north", player_piece, opponent_piece, row, column)
        # self.rec_flip_pieces("northeast", player_piece, opponent_piece, row, column)
        # self.rec_flip_pieces("east", player_piece, opponent_piece, row, column)
        # self.rec_flip_pieces("southeast", player_piece, opponent_piece, row, column)
        # self.rec_flip_pieces("south", player_piece, opponent_piece, row, column)
        # self.rec_flip_pieces("southwest", player_piece, opponent_piece, row, column)
        # self.rec_flip_pieces("west", player_piece, opponent_piece, row, column)
        # self.rec_flip_pieces("northwest", player_piece, opponent_piece, row, column)

    # Finished first draft 6/2
    def rec_flip_pieces(self, direction, player_piece, opponent_piece, row, column):
        """TODO: ADD DOCSTRING"""

        # Get the value of the adjacent space in the given direction
        adjacent_row, adjacent_column = self.return_adjacent_coordinate(direction, row, column)
        value_at_adjacent_location = self._board[adjacent_row][adjacent_column]

        # Base case 1: We hit a wall. No valid flips.
        if value_at_adjacent_location == "*":
            return False

        # Base case 2: We found an empty space. No valid flips
        if value_at_adjacent_location == ".":
            return False

        # Base case 3: We found the current player's piece.
        #              This indicates that we should flip the pieces we passed over.
        if value_at_adjacent_location == player_piece:
            return True

        # Recursive case: We're following a trail of the opponent's pieces
        if value_at_adjacent_location == opponent_piece:

            # If we eventually find the current player's piece, we should flip the value on the board
            if self.rec_flip_pieces(direction, player_piece, opponent_piece, adjacent_row, adjacent_column):
                self._board[adjacent_row][adjacent_column] = player_piece
                return True
            else:
                return False

    # Finished first draft 6/3. Finished unit tests 6/4
    def return_adjacent_coordinate(self, direction, row, column):
        """Takes three parameters:
        direction - the direction to travel from the starting location
        row, column - The row,column coordinate pair for the starting location

        Purpose: Takes a row,column pair and returns an adjacent coordinate pair in the given direction

        Returns:
            If the adjacent coordinates are within the game board, returns the adjacent coordinates.
            If the adjacent coordinates are in an invalid position, returns the string 'invalid' """

        new_row = -1
        new_column = -1

        if direction.lower() == "north":
            new_row = row - 1
            new_column = column
        elif direction.lower() == "northeast":
            new_row = row - 1
            new_column = column + 1
        elif direction.lower() == "east":
            new_row = row
            new_column = column + 1
        elif direction.lower() == "southeast":
            new_row = row + 1
            new_column = column + 1
        elif direction.lower() == "south":
            new_row = row + 1
            new_column = column
        elif direction.lower() == "southwest":
            new_row = row + 1
            new_column = column - 1
        elif direction.lower() == "west":
            new_row = row
            new_column = column - 1
        elif direction.lower() == "northwest":
            new_row = row - 1
            new_column = column - 1
        else:
            print(f"ERROR in return_adjacent_coordinate:: Invalid direction: {direction}")
            return "invalid"

        if new_row < 0 or new_row > 9:
            print(f"ERROR in return_adjacent_coordinate:: Invalid new_row ({new_row}) in direction {direction}")
            return "invalid"

        if new_column < 0 or new_column > 9:
            print(f"ERROR in return_adjacent_coordinate:: Invalid new_column ({new_column}) in direction {direction}")
            return "invalid"

        return new_row, new_column

    # Finished first draft 6/3
    def return_piece_locations(self, color):
        """Takes one parameter:
                color - The color to look for on the game board

                Purpose: Creates a list of all coordinate locations on the game board that contain a given color piece.
                This provides the starting locations for the return_available_positions() method.

                Returns: A list that contains the coordinate location of every piece of the given color."""

        player_piece = None
        piece_locations = []

        if color.lower() == "black":
            player_piece = "X"
        elif color.lower() == "white":
            player_piece = "O"
        else:
            print(f"ERROR:: Invalid color: {color}")
            return -1

        number_of_rows = len(self._board)
        number_of_columns = len(self._board[0])

        for row in range(number_of_rows):
            for column in range(number_of_columns):
                if self._board[row][column] == player_piece:
                    piece_locations.append([row, column])

        return piece_locations

    def return_available_positions(self, color):
        """TODO: ADD DOCSTRING"""

        print(f"DEBUG:: in return_available_positions")

def misc_tests():
    """FOR DEBUG USE ONLY! TODO: DELETE BEFORE SUBMISSION"""
    game = Othello()
    game.print_board()

    # game._board[5][6] = "X"
    game._board[6][6] = "O"
    game._board[7][6] = "O"
    game._board[8][6] = "X"

    game._board[5][1] = "X"
    game._board[5][2] = "O"
    game._board[5][3] = "O"
    game._board[5][4] = "O"
    game._board[4][6] = "O"
    game._board[3][6] = "X"

    game.print_board()

    white_locations = game.return_piece_locations("white")
    black_locations = game.return_piece_locations("black")
    print(f"DEBUG:: White has {len(white_locations)} pieces at: {white_locations}")
    print(f"DEBUG:: Black has {len(black_locations)} pieces at: {black_locations}")

    game._board[5][6] = "X"
    game.flip_pieces("black", 5, 6)
    # game.rec_flip_test("black", "south", 5, 6)
    # game.rec_flip_test("black", "west", 5, 6)
    game.print_board()

    white_locations = game.return_piece_locations("white")
    black_locations = game.return_piece_locations("black")
    print(f"DEBUG:: White has {len(white_locations)} pieces at: {white_locations}")
    print(f"DEBUG:: Black has {len(black_locations)} pieces at: {black_locations}")

def test_game_loop():
    """FOR DEBUG USE ONLY! TODO: DELETE BEFORE SUBMISSION!"""

    game = Othello()
    user_input = ""
    current_player = "black"

    while user_input != "q":
        game.print_board()
        player_piece, opponent_piece = game.color_to_piece(current_player)
        player_row = int(input(f"{current_player}'s turn. What row do you want to move to? "))
        player_column = int(input("What column do you want to move to? "))

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
