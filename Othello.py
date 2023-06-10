# Author: Jordan Moore
# GitHub username: moorejo6
# Date: 5/15/23
# Description: TODO: ADD DESCRIPTION
# ---------------------------------------------------------------------------------------------------------------------------

def generate_board(black_token_locations=None, white_token_locations=None):
    """Returns an Othello board with black and white tokens placed at the provided coordinates. If no coordinates are given,
    pieces are placed at their starting location."""

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
    """Represents a player in the Othello game."""

    def __init__(self, name, color):
        self._name = name
        self._color = color

    def get_name(self):
        """Returns the player's name"""
        return self._name

    def get_color(self):
        """Returns the player's color"""
        return self._color


class Othello:  # TODO: Check style guide lines for classes
    """Represents a game of Othello. Contains methods and data members needed to store the game state, make moves for
    the players, update the game state, detect the end of the game, and declare a winner."""

    # -------------------- Init and getter methods -------------------- #

    def __init__(self):
        self._board = generate_board()
        self._player_list = [Player("Player 1", "black"), Player("Player 2", "white")]

        # The coordinate shift represents the changes needed for a (row, column) pair to shift to an adjacent space.
        # There are 8 shifts that represent movement in the 8 cardinal directions: N, NE, E, SE, S, SW, W, NE
        self._coordinate_shift = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

    def get_board(self):
        """Returns the current game board"""
        return self._board

    def get_player_list(self):
        """Returns the player list"""
        return self._player_list

    def get_coordinate_shift(self):
        """Returns the coordinate shift list"""
        return self._coordinate_shift

    # -------------------- Methods listed in the README -------------------- #

    def print_board(self):
        """Prints the current state of the Othello board with row and column numbers. Returns nothing."""

        # Print the column labels and create a counter for the row labels
        print("\n    1 2 3 4 5 6 7 8 ")
        row_num = 0

        for row in range(len(self._board)):

            # Print the row number before each row that represents the playable area of the board
            if row_num == 0 or row_num == 9:
                print(" ", end=" ")
            else:
                print(row_num, end=" ")

            # Print the value in each column and increment the row counter
            for column in range(len(self._board[row])):
                print(self._board[row][column], end=" ")
            print("")
            row_num += 1

        print("")

    def create_player(self, player_name, color):
        """Adds a player to the game's player_list. The black player will be stored in player_list[0] and the white player
        will be stored in player_list[1]."""

        new_player = Player(player_name, color)

        # Assign the new player to the correct index of player_list
        if color == "black":
            self._player_list[0] = new_player
        elif color == "white":
            self._player_list[1] = new_player
        else:
            print(f"ERROR in create_player():: Invalid color {color}")

    def return_winner(self):
        """Finds the total number of pieces each player has on the board and declares the winner.
        Returns the winner_string"""

        # Get the number of black and white pieces on the board
        num_black_pieces = len(self.return_piece_locations("black"))
        num_white_pieces = len(self.return_piece_locations("white"))

        # Get the player objects and initialize the winner_string
        black_player = self._player_list[0]
        white_player = self._player_list[1]
        winner_string = ""

        # Determine the winner and return the winner_string
        if num_black_pieces > num_white_pieces:
            winner_string = "Winner is black player: " + black_player.get_name()

        elif num_white_pieces > num_black_pieces:
            winner_string = "Winner is white player: " + white_player.get_name()

        else:
            winner_string = "It's a tie"

        return winner_string

    # Finished first draft on 6/9
    def return_available_positions(self, color):
        """Returns a list of the (row, column) coordinates for each valid move the player of the given color can make.
        Uses the recursive rec_return_available_positions() method to determine valid move locations."""

        # Get the piece symbols for each player, the piece locations for the given player, and initialize the valid move list
        player_piece, opponent_piece = self.color_to_piece(color)
        player_token_locations = self.return_piece_locations(color)
        valid_move_list = []

        # For every token the player has on the board, search all directions around the token for available moves
        for token_location in player_token_locations:
            for shift in self._coordinate_shift:
                possible_move = self.rec_return_available_positions(token_location, shift, player_piece, opponent_piece)

                # A possible move is added to the list only if it isn't None and isn't already in the valid_move_list
                if possible_move is not None and possible_move not in valid_move_list:
                    valid_move_list.append(possible_move)

        return valid_move_list

    def make_move(self, color, piece_position):
        """Places a piece of the given color at the given location and updates the board as necessary. Uses the flip_pieces()
        method to determine which of the opponent's pieces need to be flipped over. Returns the updated game board."""

        # Get the piece symbol for the given color
        player_piece, opponent_piece = self.color_to_piece(color)

        # Place the player's piece on the board at the given location and flip the opponent's pieces as necessary
        self._board[piece_position[0]][piece_position[1]] = player_piece
        self.flip_pieces(color, piece_position)

        return self._board

    def play_game(self, player_color, piece_position):
        """TODO: ADD DOCSTRING"""

        if self.game_is_over():
            num_black_pieces = len(self.return_piece_locations("black"))
            num_white_pieces = len(self.return_piece_locations("white"))

            print("Game is ended white piece:", num_white_pieces, "black piece:", num_black_pieces)
            return self.return_winner()

        else:
            player_valid_moves = self.return_available_positions(player_color)

            if piece_position in player_valid_moves:
                self.make_move(player_color, piece_position)

                if self.game_is_over:
                    num_black_pieces = len(self.return_piece_locations("black"))
                    num_white_pieces = len(self.return_piece_locations("white"))

                    print("Game is ended white piece:", num_white_pieces, "black piece:", num_black_pieces)
                    return self.return_winner()

            else:
                print("Here are the valid moves:", player_valid_moves)
                return "Invalid move"

    # -------------------- Helper methods -------------------- #

    def color_to_piece(self, color):
        """Takes the given color and returns the symbols that represent that player's color and the opponent's color."""

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

    def return_piece_locations(self, color):
        """Returns a list of all coordinate locations on the game board that contain a given color piece"""

        # Get the piece symbol for the given color and create a list to hold the coordinate locations of found pieces
        player_piece, opponent_piece = self.color_to_piece(color)
        piece_locations = []

        # Get the length of the board's rows and columns (not necessary, but it looks nicer in the for loops)
        number_of_rows = len(self._board)
        number_of_columns = len(self._board[0])

        # Iterate through the board and add the coordinates of found pieces to the locations list
        for row in range(number_of_rows):
            for column in range(number_of_columns):
                if self._board[row][column] == player_piece:
                    piece_locations.append([row, column])

        return piece_locations

    def print_available_positions(self, color):
        """Used for testing. Prints the board with available moves shown as an equals sign."""

        # Get the list of all valid moves for the given color
        valid_moves = self.return_available_positions(color)

        # Get the length of the board's rows and columns (not necessary, but it looks nicer in the for loops)
        board_row_length = len(self._board)
        board_column_length = len(self._board[0])

        # If the valid moves list isn't empty, add an "=" at each location to show an available move
        if valid_moves != []:
            for move in valid_moves:
                self._board[move[0]][move[1]] = "="

        self.print_board()

        # Time to clean up. Loop through the board and remove the symbol we added.
        for row in range(board_row_length):
            for column in range(board_column_length):
                if self._board[row][column] == "=":
                    self._board[row][column] = "."

    def flip_pieces(self, color, piece_position):
        """Starting from the given coordinate pair, this method will check for and perform valid flip moves in
        all 8 adjacent directions using the recursive rec_flip_pieces() method."""

        # Get the pieces that represent the player and their opponent's colors
        player_piece, opponent_piece = self.color_to_piece(color)

        # Check every direction for valid pieces to flip
        for shift in self._coordinate_shift:
            self.rec_flip_pieces(piece_position, shift, player_piece, opponent_piece)

    def rec_flip_pieces(self, piece_position, shift, player_piece, opponent_piece):
        """Recursively finds valid pieces to flip and flips them."""

        # Get the coordinates and value of the adjacent space in the given direction
        adjacent_space = [piece_position[0] + shift[0], piece_position[1] + shift[1]]
        adjacent_value = self._board[adjacent_space[0]][adjacent_space[1]]

        # Base case 1: We hit a wall. No valid flips.
        if adjacent_value == "*":
            return False

        # Base case 2: We found an empty space. No valid flips
        if adjacent_value == ".":
            return False

        # Base case 3: We found the current player's piece.
        #              This indicates that we should flip the pieces we passed over.
        if adjacent_value == player_piece:
            return True

        # Recursive case: We're following a trail of the opponent's pieces
        if adjacent_value == opponent_piece:

            # If we eventually find the current player's piece, we should flip the value on the board
            if self.rec_flip_pieces(adjacent_space, shift, player_piece, opponent_piece):
                self._board[adjacent_space[0]][adjacent_space[1]] = player_piece
                return True
            else:
                return False

    def rec_return_available_positions(self, current_location, shift, player_piece, opponent_piece, previous_value=None):
        """Recursively finds valid move locations for the player of the given color. Returns a list with coordinates of
        all valid move locations."""

        # Get the coordinates and value of the adjacent space in the given direction
        adjacent_space = [current_location[0] + shift[0], current_location[1] + shift[1]]
        adjacent_value = self._board[adjacent_space[0]][adjacent_space[1]]

        # Base case 1: We hit a wall. Not a valid move.
        if adjacent_value == "*":
            return None

        # Base case 2: We found the current player's piece. Not a valid move
        if adjacent_value == player_piece:
            return None

        # Base case 3: We found an empty space but this is the first call to rec_return_available_positions() in this
        #              direction (indicated by previous_value = None). This space is adjacent to our starting piece and
        #              is not a valid move.
        if adjacent_value == "." and previous_value is None:
            return None

        # Base case 4: We found an empty space on a subsequent recursive call. This is a valid move.
        if adjacent_value == "." and previous_value is not None:
            return adjacent_space

        # Recursive case: We're following a trail of the opponent's pieces
        if adjacent_value == opponent_piece:
            return self.rec_return_available_positions(adjacent_space, shift, player_piece, opponent_piece, adjacent_value)

    def game_is_over(self):
        """TODO: ADD DOCSTRING"""

        black_valid_moves = self.return_available_positions("black")
        white_valid_moves = self.return_available_positions("white")

        if black_valid_moves == [] and white_valid_moves == []:
            return True

        else:
            return False


def game_loop():
    """TODO: ADD DOCSTRING"""

    game = Othello()

    print("~~~~~~~~~~ OTHELLO ~~~~~~~~~~")
    print("\nWelcome to Othello!\n")

    playing = True
    current_player = "black"

    while playing:

        game.print_available_positions(current_player)
        valid_moves = game.return_available_positions(current_player)

        valid_input = False

        while not valid_input:

            try:
                player_row = int(input(f"{current_player}'s turn. What row do you want to move to? "))
                player_column = int(input("What column do you want to move to? "))
                player_input = [player_row, player_column]

                if player_input in valid_moves:
                    valid_input = True
                    game.play_game(current_player, player_input)
                elif valid_moves == []:
                    print("No moves available for", current_player)
                    valid_input = True
                else:
                    print("Invalid input. Valid moves are:", valid_moves)

            except ValueError:
                print("Invalid input. No value entered.")
                pass

        if current_player == "black":
            current_player = "white"
        else:
            current_player = "black"

        if len(game.return_available_positions("black")) == 0 and len(game.return_available_positions("white")) == 0:
            playing = False


def main():
    # test_game_loop()
    game_loop()


if __name__ == "__main__":
    main()
