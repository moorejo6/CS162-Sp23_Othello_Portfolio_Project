def generate_board():
    """Takes no parameters.

    Purpose: Generates a 2d list that represents an 8x8 Othello board with an outside border and black and white pieces
    placed in their initial positions. This is used by the Othello class's __init__() method to create a new game board.

    Returns: The generated 2d list"""

    pass


class Player:
    """Represents a player of the game. Each player has a color (black or white) and a name."""

    def __init__(self, name, color):
        """Takes two parameters:
        name - The name of the player
        color - The color of the player's pieces

        Purpose: Initializes Player object with a player's name and color. All data members are private.

        Returns: nothing"""

        pass

    def get_name(self):
        """Getter method for the player's name"""
        pass

    def get_color(self):
        """Getter method for the player's color"""
        pass


class Othello:
    """Represents the game of Othello. Contains all necessary methods needed to play the game"""

    def __init__(self):
        """Takes no parameters.

        Purpose: Initializes a new instance of an othello game. Creates a new game board using the generate_gameboard()
        method and initializes all necessary data members. All data members are private.

        Returns: nothing"""

        pass

    def print_board(self):
        """Takes no parameters.

        Purpose: Prints the current state of the game board to the python console.

        Returns: nothing"""

        pass

    def create_player(self, player_name, color):
        """Takes two parameters:
        player_name - The name of the new player
        color - The color the new player will play as

        Purpose: Creates a new player for the game and adds it to the Othello object's player list.

        Returns: nothing."""

        pass

    def return_winner(self):
        """Takes no parameters

        Purpose: Determines the winner of the game and creates a string declaring the name and color of the winner or
        declares a tie if the game is tied.

        Returns: The string declaring the winner of the game (or that the game is a tie)"""

        pass

    def return_available_positions(self, color):
        """Takes one parameter:
        color - The color to check valid moves for

        Purpose: Takes a color and determines which coordinates on the game board are valid moves for that color. Uses the
        get_piece_locations() helper method.

        Returns: A list containing the coordinates of all valid moves"""

        pass

    def make_move(self, color, piece_position):
        """Takes two parameters:
        color - The color to make a move for
        piece_position - The position to place the new piece

        Purpose: Places a piece of the given color at the given position. Then updates the game board using helper functions
        to determine which pieces need to be flipped. Uses the flip_pieces() helper method.

        Returns: The updated game board"""

        pass

    def play_game(self, player_color, piece_position):
        """Takes two parameters:
        player_color - the color of the player that is moving
        piece_position - the position the player is trying to move to

        Purpose: Handles player movement, verifying that the player's move is valid, updating the game board, and determining
        the end of the game. makes use of the make_move(), return_available_positions(), and return_winner() methods.

        Returns:
        If the player's move is invalid, returns the string 'Invalid move' and prints a list of valid moves.
        If the move is valid, updates the game board and returns nothing.
        If the game has ended, prints the number of pieces each player has on the board and calls return_winner()"""

        pass

    def piece_locations(self, color):
        """Takes one parameter:
        color - The color to look for on the game board

        Purpose: Creates a list of all coordinate locations on the game board that contain a given color piece.
        This provides the starting locations for the return_available_positions() method.

        Returns: A list that contains the coordinate location of every piece of the given color."""

        pass

    def flip_pieces(self, piece_location):
        """Takes one parameter:
        piece_location - The location of the piece that was just placed on the board

        Purpose: Starting from the piece_location, determines which pieces on the board need to be flipped and flips them

        Returns: nothing."""

        pass
