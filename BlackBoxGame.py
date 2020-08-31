# Author: Erika Tharp
# Date: 08/01/2020
# Description: This program represents a popular game called Black Box Game.
#              The box is  10 x 10 and the boarder is row 0 and 9 and column 0 and 9.
#              The users enter any number (at least 1) of "atoms" anywhere on the box besides the boarder.
#              The users can shoot rays only from the boarder but not from the four corners and guess where the atoms are placed based on how the
#              rays move around the box (hit, reflect, double reflect, and miss).
#              The score starts at 25 and each entry and exit except previously used entries and exits count as 1 which is subtructed from the score.
#              Also, every time the user guess where atom is and if it is incorrect, 5 points are subtructed from the score (previously guessed
#              atoms are not counted).
#              There are four classes that are Board, Atoms, Rays, and BlackBoxGames to be able to play the game.
#              Each class has init methods as well as methods to organize and manipulate data as the users play the game.
#              In BlackBoxGame class, Board, Atoms, and Rays objects are created to keep track of each object's data.


class Board:
    """
    Represents a board to play black box game with a 10 x 10 board and methods to manipulate the board.
    """
    def __init__(self, t_list):
        """
        Takes a list of tuple and create a 10 x 10 board with atoms.
        'b' represents boarder and 'a' represents atom.
        """
        self._board = [
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
            ['b', '', '', '', '', '', '', '', '', 'b'],
            ['b', '', '', '', '', '', '', '', '', 'b'],
            ['b', '', '', '', '', '', '', '', '', 'b'],
            ['b', '', '', '', '', '', '', '', '', 'b'],
            ['b', '', '', '', '', '', '', '', '', 'b'],
            ['b', '', '', '', '', '', '', '', '', 'b'],
            ['b', '', '', '', '', '', '', '', '', 'b'],
            ['b', '', '', '', '', '', '', '', '', 'b'],
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
        ]
        # Call place_atom to update the board with atoms.
        self.place_atom(t_list)

    def place_atom(self, t_list):
        """
        Takes a list of tuples and place atoms in the board accordingly.
        """
        for t in t_list:
            row = t[0]
            col = t[1]
            self._board[row][col] = 'a'

    def get_board(self):
        """ Returns the current board. """
        return self._board


class Atoms:
    """
    Represents a collection of atoms and methods to get and remove atoms.
    """

    def __init__(self, t_list):
        """
        Takes a list of tuples as a parameter to create an Atoms object.
        Also, creates a list to track guessed atoms.
        """
        self._atoms = t_list
        self._guessed_atoms = []

    def get_atoms(self):
        """ Returns atoms left. """
        return self._atoms

    def remove_atom(self, atom):
        """
        Takes atom (tuple) as a parameter and remove atom from ._atoms.
        Returns True if there is an atom in ._atoms and returns False otherwise.
        """
        if atom in self._atoms:
            self._atoms.remove(atom)
            return True
        else:
            return False

    def add_guessed_atoms(self, guess):
        """
        Takes guess (tuple containing row/column) as a parameter and add a new guess to ._guessed_atoms.
        """
        if guess not in self._guessed_atoms:
            self._guessed_atoms.append(guess)

    def get_guessed_atoms(self):
        """ Returns ._guessed_atoms. """
        return self._guessed_atoms


class Rays:
    """
    Represents a collection of entries and exits made by shooting rays and methods add and get those rays.
    """

    def __init__(self):
        """
        Creates a list that will contain tuples of entries and exits.
        """
        self._rays = []

    def get_rays(self):
        """ Returns all entries and exits that are previously visited in a list of tuples. """
        return self._rays

    def add_rays(self, square):
        """ Add a new entries and exits (tuple) to _rays. """
        if square not in self._rays:
            self._rays.append(square)


class BlackBoxGame:
    """
    Represents black box game with a specific ray, board, and atom objects, direction, score and methods to play the game.
    """

    def __init__(self, t_list):
        """
        Takes a list of tuples as a parameter to create a BlackBoxGame object with a ray, board and an atom objects, direction, and score.
        A list of tuples is passed to ._board as well as ._atoms to be used by these objects.
        """
        self._score = 25
        self._direction = ""
        self._board = Board(t_list)
        self._atoms = Atoms(t_list)
        self._rays = Rays()

    def shoot_ray(self, row, col):
        """
        Takes as its parameters the row and column of the border square where the ray originates.
        Return value's data types are boolean, tuple, or None.

        If the chosen row and column designate a corner square or a non-border square, it should return False.
        Otherwise, shoot_ray should return a tuple of the row and column of the exit border square.
        If there is no exit border square (because there was a hit), then shoot_ray should return None.
        """

        # Check a specified location is a corner square or a non-boarder.
        non_corner_boarder_squares = [
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8),
            (1, 0), (1, 9), (2, 0), (2, 9), (3, 0), (3, 9), (4, 0), (4, 9),
            (5, 0), (5, 9), (6, 0), (6, 9), (7, 0), (7, 9), (8, 0), (8, 9),
            (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8)
                           ]
        chosen_r_c = (row, col)
        if chosen_r_c not in non_corner_boarder_squares:
            return False
        # Move ray until it hits an atom or find an exit.
        else:
            # Add the entry to ._rays.
            self._rays.add_rays(chosen_r_c)
            # Check the first move from the boarder.
            current_square = self.first_check_surroundings(row, col)
            # If the first move hits the atom returns None.
            if current_square is None:
                return None
            # The first move is not a hit, so determines whether the first move went forward or was reflection.
            elif current_square is not None:
                row = current_square[0]
                col = current_square[1]
                current_square = self._board.get_board()[row][col]
                # If the first move is reflection, then return the exit square in a tuple. (same as the entry).
                if current_square == 'b':
                    current_square = tuple(current_square)
                    return current_square
            # Case where the first move was successful.
            # Keep checking until exits the board or hits one of the atoms.
            while current_square is not None and current_square != 'b':
                current_square = self.check_surroundings(row, col)
                if current_square is not None:
                    row = current_square[0]
                    col = current_square[1]
                    current_square = self._board.get_board()[row][col]
            if current_square is None:
                return None
            elif current_square is not None and current_square == 'b':
                # Add an exit to ._rays.
                current_square = tuple([row, col])
                self._rays.add_rays(current_square)
                return current_square

    def first_check_surroundings(self, row, col):
        """
        Takes a list representing the current row and column and check its surroundings for the first move from the boarder.
        Returns a current square in a list or None if it hits an atom.
        """
        current_square = []
        board = self._board.get_board()
        self._direction = self.get_direction(row, col)
        # Check three squares (top, middle, and bottom) one column ahead of position.
        # Case where direction is right.
        if self._direction == "right":
            top = board[row-1][col+1]
            middle = board[row][col+1]
            bottom = board[row+1][col+1]
            if top == 'a' or bottom == 'a':
                current_square = [row, col]
                return current_square
            elif middle == 'a':
                return None
            else:
                current_square = [row, col+1]
                return current_square
        # Case where direction is left.
        elif self._direction == "left":
            top = board[row-1][col-1]
            middle = board[row][col-1]
            bottom = board[row+1][col-1]
            if top == 'a' or bottom == 'a':
                current_square = [row, col]
                return current_square
            elif middle == 'a':
                return None
            else:
                current_square = [row, col-1]
                return current_square
        # Case where direction is up.
        elif self._direction == "up":
            left = board[row-1][col-1]
            middle = board[row-1][col]
            right = board[row-1][col+1]
            if left == 'a' or right == 'a':
                current_square = [row, col]
                return current_square
            elif middle == 'a':
                return None
            else:
                current_square = [row-1, col]
                return current_square
        # Case where direction is down.
        elif self._direction == "down":
            left = board[row+1][col-1]
            middle = board[row+1][col]
            right = board[row+1][col+1]
            if left == 'a' or right == 'a':
                current_square = [row, col]
                return current_square
            elif middle == 'a':
                return None
            else:
                current_square = [row+1, col]
                return current_square

    def check_surroundings(self, row, col):
        """
        Takes a list representing the current row and column and check its surroundings.
        Returns a current square in a list or None if it hits an atom.
        """
        current_square = []
        board = self._board.get_board()
        direction = self._direction
        # Check three squares (top, middle, and bottom) one column ahead of position.
        # Case where direction is right.
        if direction == "right":
            top = board[row - 1][col + 1]
            middle = board[row][col + 1]
            bottom = board[row + 1][col + 1]
            if top == 'a' and bottom == 'a':
                current_square = [row, 0]
                return current_square
            elif top == 'a':
                self._direction = "down"
                current_square = [row+1, col]
                return current_square
            elif bottom == 'a':
                self._direction = "top"
                current_square = [row-1, col]
                return current_square
            elif middle == 'a':
                return None
            else:
                current_square = [row, col + 1]
                return current_square
        # Case where direction is left.
        elif self._direction == "left":
            top = board[row - 1][col - 1]
            middle = board[row][col - 1]
            bottom = board[row + 1][col - 1]
            if top == 'a' and bottom == 'a':
                current_square = [row, 9]
                return current_square
            elif top == 'a':
                self._direction = "down"
                current_square = [row+1, col]
                return current_square
            elif bottom == 'a':
                self._direction = "up"
                current_square = [row-1, col]
                return current_square
            elif middle == 'a':
                return None
            else:
                current_square = [row, col - 1]
                return current_square
        # Case where direction is up.
        elif self._direction == "up":
            left = board[row - 1][col - 1]
            middle = board[row - 1][col]
            right = board[row - 1][col + 1]
            if left == 'a' and right == 'a':
                current_square = [9, col]
                return current_square
            elif left == 'a':
                self._direction = "right"
                current_square = [row, col+1]
                return current_square
            elif right == 'a':
                self._direction = "left"
                current_square = [row, col-1]
                return current_square
            elif middle == 'a':
                return None
            else:
                current_square = [row - 1, col]
                return current_square
        # Case where direction is down.
        elif self._direction == "down":
            left = board[row+1][col-1]
            middle = board[row+1][col]
            right = board[row+1][col+1]
            if left == 'a' and right == 'a':
                current_square = [0, col]
                return current_square
            elif left == 'a':
                self._direction = "right"
                current_square = [row, col+1]
                return current_square
            elif right == 'a':
                self._direction = "left"
                current_square = [row, col-1]
                return current_square
            elif middle == 'a':
                return None
            else:
                current_square = [row+1, col]
                return current_square

    def get_direction(self, row, col):
        """
        Takes row and column as parameters and determines which direction ray is going and returns that direction.
        """
        if col == 0:
            self._direction = "right"
        elif col == 9:
            self._direction = "left"
        elif row == 0:
            self._direction = "down"
        elif row == 9:
            self._direction = "up"
        return self._direction

    def guess_atom(self, row, col):
        """
        Takes as parameters a row and column.
        If there is an atom at that location, guess_atom should return True, otherwise it should return False.
        """
        guessed_atom = (row, col)
        # Check if guessed_atom has previously guessed.
        guessed_atoms = self._atoms.get_guessed_atoms()
        if guessed_atom in guessed_atoms:
            previously_guessed = True
        elif guessed_atom not in guessed_atoms:
            previously_guessed = False
        # Add guessed_atom to a list of guessed atoms (tuple).
        self._atoms.add_guessed_atoms(guessed_atom)
        # Case where guessed_atom is at the location of row, column.
        if self._atoms.remove_atom(guessed_atom):
            return True
        # Case where guessed_atom is not at the location of row, column.
        else:
            # Subtracts 5 points from score since the guess is wrong.
            # If the guess is same as previous, then do not subtracts 5 points from score.
            if not previously_guessed:
                self._score -= 5
            return False

    def get_score(self):
        """ Takes no parameter and returns score. """
        num_entry_exit = len(self._rays.get_rays())
        self._score -= num_entry_exit
        return self._score

    def atoms_left(self):
        """ Takes no parameter and returns the number of atoms that haven't been guessed yet. """
        not_guessed_atoms = len(self._atoms.get_atoms())
        return not_guessed_atoms

    def get_board(self):
        """ Get the game board. """
        self._board.get_board()


