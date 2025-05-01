import numpy as np

class Piece:
    """
    Base class for pieces on the board. 
    
    A piece holds a reference to the board, its color and its currently located cell.
    In this class, you need to implement two methods, the "evaluate()" method and the "get_valid_cells()" method.
    """
    def __init__(self, board, white):
        """
        Constructor for a piece based on provided parameters

        :param board: Reference to the board this piece is placed on
        :type board: :ref:class:`board`
        """
        self.board = board
        self.white = white
        self.cell = None



    def is_white(self):
        """
        Returns whether this piece is white

        :return: True if the piece white, False otherwise
        """
        return self.white

    def can_enter_cell(self, cell):
        """
        Shortcut method to see if a cell on the board can be entered.
        Simply calls :py:meth:`piece_can_enter_cell <board.Board.piece_can_enter_cell>` from the current board class.

        :param cell: The cell to check for. Must be a unpackable (row, col) type.
        :return: True if the provided cell can enter, False otherwise
        """
        return self.board.piece_can_enter_cell(self, cell)

    def can_hit_on_cell(self, cell):
        """
        Shortcut method to see if this piece can hit another piece on a cell.
        Simply calls :py:meth:`piece_can_hit_on_cell <board.Board.piece_can_hit_on_cell>` from the current board class.

        :param cell: The cell to check for. Must be a unpackable (row, col) type.
        :return: True if the piece can hit on the provided cell, False otherwise
        """
        return self.board.piece_can_hit_on_cell(self, cell)

    def evaluate(self):
        """
        **TODO** Implement a meaningful numerical evaluation of this piece on the board.
        This evaluation happens independent of the color as later, values for white pieces will be added and values for black pieces will be substracted. 
        
        **HINT** Making this method *independent* of the pieces color is crucial to get a *symmetric* evaluation metric in the end.
         
        - The pure existance of this piece alone is worth some points. This will create an effect where the player with more pieces on the board will, in sum, get the most points assigned. 
        - Think of other criteria that would make this piece more valuable, e.g. movability or whether this piece can hit other pieces. Value them accordingly.
        
        :return: Return numerical score between -infinity and +infinity. Greater values indicate better evaluation result (more favorable).
        """
        score = self.base_score  # Base value for this piece

        valid_cells = self.get_valid_cells()
        points_per_square = 0.02
        if isinstance(self, Queen):
            points_per_square /= 2 # The queen has such great mobility that we need to reduce her points a bit to compensate

        score += points_per_square * len(
            valid_cells
        )  # Every reachable cell gives 0.01 point (more movability is better)

        threat_score = 0.0
        total_threat = 0
        for cell in valid_cells:
            piece = self.board.get_cell(cell)
            if piece is not None and piece.white != self.white: # There is a threat if we can hit an opposing piece
                threat_score += piece.score_for_threat
                total_threat += 1

        if (
            total_threat > 1
        ):  # We have a fork (at least two pieces threatened at the same time, evaluate that higher)
            threat_score = threat_score * 1.1 + 0.1

        score += 0.1 * threat_score

        return score

    def get_valid_cells(self):
        """
        **TODO** Return a list of **valid** cells this piece can move into. 
        
        A cell is valid if 
          a) it is **reachable**. That is what the :py:meth:`get_reachable_cells` method is for and
          b) after a move into this cell the own king is not (or no longer) in check.

        **HINT**: Use the :py:meth:`get_reachable_cells` method of this piece to receive a list of reachable cells.
        Iterate through all of them and temporarily place the piece on this cell. Then check whether your own King (same color)
        is in check. Use the :py:meth:`is_king_check_cached` method to test for checks. If there is no check after this move, add
        this cell to the list of valid cells. After every move, restore the original board configuration. 
        
        To temporarily move a piece into a new cell, first store its old position (self.cell) in a local variable. 
        The target cell might have another piece already placed on it. 
        Use :py:meth:`get_cell <board.BoardBase.get_cell>` to retrieve that piece (or None if there was none) and store it as well. 
        Then call :py:meth:`set_cell <board.BoardBase.set_cell>` to place this piece on the target cell and test for any checks given. 
        After this, restore the original configuration by placing this piece back into its old position (call :py:meth:`set_cell <board.BoardBase.set_cell>` again)
        and place the previous piece also back into its cell. 
        
        :return: Return True 
        """
        # Start with empty valid cells
        valid_cells = []

        # Get all potential (reachable) cells
        potential_cells = self.get_reachable_cells()

        # Remember our old position
        old_position = self.cell

        # Iterate them
        for cell in potential_cells:
            # Remember the old piece
            old_piece = self.board.get_cell(cell)

            # Place piece here
            self.board.set_cell(cell, self)

            # See if our king is in check
            if not self.board.is_king_check_cached(self.white):
                valid_cells.append(cell)

            # Undo placement
            self.board.set_cell(old_position, self)
            self.board.set_cell(cell, old_piece)

        return valid_cells


class Pawn(Piece):  # Bauer
    def __init__(self, board, white):
        super().__init__(board, white)

        self.score_for_threat = 0.1
        self.base_score = 1

    def get_reachable_cells(self):
        """
        **TODO** Implement the movability mechanik for `pawns <https://de.wikipedia.org/wiki/Bauer_(Schach)>`_. 

        **NOTE**: Here you do not yet need to consider whether your own King would become checked after a move. This will be taken care of by
        the :py:meth:`is_king_check <board.Board.is_king_check>` and :py:meth:`get_valid_cells <pieces.Piece.get_valid_cells>` methods.

        **HINT**: Pawns can move only forward (towards the opposing army). Depening of whether this piece is black of white, this means pawn
        can move only to higher or lower rows. Normally a pawn can only move one cell forward as long as the target cell is not occupied by any other piece. 
        If the pawn is still on its starting row, it can also dash forward and move two pieces at once (as long as the path to that cell is not blocked).
        Pawns can only hit diagonally, meaning they can hit other pieces only the are one cell forward left or one cell forward right from them. 

        You can call :py:meth:`cell_is_valid_and_empty <board.Board.cell_is_valid_and_empty>`, 
        :py:meth:`can_hit_on_cell <pieces.Piece.can_hit_on_cell>` and :py:meth:`can_enter_cell <pieces.Piece.can_enter_cell>` 
        to check for necessary conditions to implement the pawn movability mechanics. 

        **NOTE**: For all you deep chess experts: Hitting `en passant <https://de.wikipedia.org/wiki/En_passant>`_ does not need to be implemented.
        
        :return: A list of reachable cells this pawn could move into.
        """
        # TODO: Implement a method that returns all cells this piece can enter in its next move
        move_dir = np.array([1, 0]) if self.is_white() else np.array([-1, 0])

        potential_cells = []
        potential_cells.append(self.cell + move_dir)

        if self.white and self.cell[0] == 1:
            if self.board.cell_is_valid_and_empty(self.cell + move_dir):
                potential_cells.append(self.cell + move_dir * 2)

        if not self.white and self.cell[0] == 6:
            if self.board.cell_is_valid_and_empty(self.cell + move_dir):
                potential_cells.append(self.cell + move_dir * 2)

        potential_cells = [
            cell for cell in potential_cells if self.board.get_cell(cell) is None
        ]

        d1 = self.cell + move_dir + np.array([0, 1])
        d2 = self.cell + move_dir + np.array([0, -1])

        if self.can_hit_on_cell(d1):
            potential_cells.append(d1)

        if self.can_hit_on_cell(d2):
            potential_cells.append(d2)

        valid_cells = [cell for cell in potential_cells if self.can_enter_cell(cell)]
        return valid_cells


class Rook(Piece):  # Turm
    def __init__(self, board, white):
        super().__init__(board, white)

        self.score_for_threat = 0.3
        self.base_score = 5

    def get_reachable_cells(self):
        """
        **TODO** Implement the movability mechanic for `rooks <https://de.wikipedia.org/wiki/Turm_(Schach)>`_. 

        **NOTE**: Here you do not yet need to consider whether your own King would become checked after a move. This will be taken care of by
        the :py:meth:`is_king_check <board.Board.is_king_check>` and :py:meth:`get_valid_cells <pieces.Piece.get_valid_cells>` methods.

        **HINT**: Rooks can move only horizontally or vertically. They can move an arbitrary amount of cells until blocked by an own piece
        or an opposing piece (which they could hit and then being stopped).

        You can call :py:meth:`cell_is_valid_and_empty <board.Board.cell_is_valid_and_empty>`, 
        :py:meth:`can_hit_on_cell <pieces.Piece.can_hit_on_cell>` and :py:meth:`can_enter_cell <pieces.Piece.can_enter_cell>` 
        to check for necessary conditions to implement the rook movability mechanics. 

        :return: A list of reachable cells this rook could move into.
        """
        # TODO: Implement a method that returns all cells this piece can enter in its next move
        potential_cells = []

        directions = [
            np.array([1, 0]),
            np.array([-1, 0]),
            np.array([0, 1]),
            np.array([0, -1]),
        ]

        # Go through all directions
        for direction in directions:
            # Go into this direction
            for delta in range(1, 8):
                next_cell = self.cell + delta * direction
                potential_cells.append(next_cell)

                if not self.board.cell_is_valid_and_empty(next_cell):
                    break

        valid_cells = [cell for cell in potential_cells if self.can_enter_cell(cell)]
        return valid_cells


class Knight(Piece):  # Springer
    def __init__(self, board, white):
        super().__init__(board, white)

        self.score_for_threat = 0.15
        self.base_score = 3

    def get_reachable_cells(self):
        """
        **TODO** Implement the movability mechanic for `knights <https://de.wikipedia.org/wiki/Springer_(Schach)>`_. 

        **NOTE**: Here you do not yet need to consider whether your own King would become checked after a move. This will be taken care of by
        the :py:meth:`is_king_check <board.Board.is_king_check>` and :py:meth:`get_valid_cells <pieces.Piece.get_valid_cells>` methods.

        **HINT**: Knights can move in a special pattern. They can move two rows up or down and then one column left or right. Alternatively, they can
        move one row up or down and then two columns left or right. They are not blocked by pieces in between. 

        You can call :py:meth:`cell_is_valid_and_empty <board.Board.cell_is_valid_and_empty>`, 
        :py:meth:`can_hit_on_cell <pieces.Piece.can_hit_on_cell>` and :py:meth:`can_enter_cell <pieces.Piece.can_enter_cell>` 
        to check for necessary conditions to implement the rook movability mechanics. 

        :return: A list of reachable cells this knight could move into.
        """
        # TODO: Implement a method that returns all cells this piece can enter in its next move
        potential_cells = []

        moves = [
            np.array([2, 1]),
            np.array([1, 2]),
            np.array([-1, 2]),
            np.array([-2, 1]),
            np.array([-2, -1]),
            np.array([-1, -2]),
            np.array([1, -2]),
            np.array([2, -1]),
        ]

        # Go through all directions
        for direction in moves:
            next_cell = self.cell + direction
            potential_cells.append(next_cell)

        valid_cells = [cell for cell in potential_cells if self.can_enter_cell(cell)]
        return valid_cells


class Bishop(Piece):  # Läufer
    def __init__(self, board, white):
        super().__init__(board, white)

        self.score_for_threat = 0.15
        self.base_score = 3

    def get_reachable_cells(self):
        """
        **TODO** Implement the movability mechanic for `bishop <https://de.wikipedia.org/wiki/L%C3%A4ufer_(Schach)>`_. 

        **NOTE**: Here you do not yet need to consider whether your own King would become checked after a move. This will be taken care of by
        the :py:meth:`is_king_check <board.Board.is_king_check>` and :py:meth:`get_valid_cells <pieces.Piece.get_valid_cells>` methods.

        **HINT**: Bishops can move diagonally an arbitrary amount of cells until blocked.

        You can call :py:meth:`cell_is_valid_and_empty <board.Board.cell_is_valid_and_empty>`, 
        :py:meth:`can_hit_on_cell <pieces.Piece.can_hit_on_cell>` and :py:meth:`can_enter_cell <pieces.Piece.can_enter_cell>` 
        to check for necessary conditions to implement the rook movability mechanics. 

        :return: A list of reachable cells this bishop could move into.
        """
        # TODO: Implement a method that returns all cells this piece can enter in its next move
        potential_cells = []

        directions = [
            np.array([1, 1]),
            np.array([-1, -1]),
            np.array([1, -1]),
            np.array([-1, 1]),
        ]

        # Go through all directions
        for direction in directions:
            # Go into this direction
            for delta in range(1, 8):
                next_cell = self.cell + delta * direction
                potential_cells.append(next_cell)

                if not self.board.cell_is_valid_and_empty(next_cell):
                    break

        # Valid cells are those who can be entered
        valid_cells = [cell for cell in potential_cells if self.can_enter_cell(cell)]
        return valid_cells


class Queen(Piece):  # Königin
    def __init__(self, board, white):
        super().__init__(board, white)

        self.score_for_threat = 0.4
        self.base_score = 9

    def get_reachable_cells(self):
        """
        **TODO** Implement the movability mechanic for the `queen <https://de.wikipedia.org/wiki/Dame_(Schach)>`_. 

        **NOTE**: Here you do not yet need to consider whether your own King would become checked after a move. This will be taken care of by
        the :py:meth:`is_king_check <board.Board.is_king_check>` and :py:meth:`get_valid_cells <pieces.Piece.get_valid_cells>` methods.

        **HINT**: Queens can move horizontally, vertically and diagonally an arbitrary amount of cells until blocked. They combine the movability
        of rooks and bishops. 

        You can call :py:meth:`cell_is_valid_and_empty <board.Board.cell_is_valid_and_empty>`, 
        :py:meth:`can_hit_on_cell <pieces.Piece.can_hit_on_cell>` and :py:meth:`can_enter_cell <pieces.Piece.can_enter_cell>` 
        to check for necessary conditions to implement the rook movability mechanics. 

        :return: A list of reachable cells this queen could move into.
        """
        # TODO: Implement a method that returns all cells this piece can enter in its next move
        potential_cells = []

        directions = [
            np.array([1, 1]),
            np.array([-1, -1]),
            np.array([1, -1]),
            np.array([-1, 1]),
            np.array([1, 0]),
            np.array([-1, 0]),
            np.array([0, 1]),
            np.array([0, -1 ])
        ]

        # Go through all directions
        for direction in directions:
            # Go into this direction
            for delta in range(1, 8):
                next_cell = self.cell + delta * direction
                potential_cells.append(next_cell)

                if not self.board.cell_is_valid_and_empty(next_cell):
                    break

        valid_cells = [cell for cell in potential_cells if self.can_enter_cell(cell)]
        return valid_cells


class King(Piece):  # König
    def __init__(self, board, white):
        super().__init__(board, white)

        self.score_for_threat = 0.5
        self.base_score = 200

    def get_reachable_cells(self):
        """
        **TODO** Implement the movability mechanic for the `king <https://de.wikipedia.org/wiki/K%C3%B6nig_(Schach)>`_. 

        **NOTE**: Here you do not yet need to consider whether your own King would become checked after a move. This will be taken care of by
        the :py:meth:`is_king_check <board.Board.is_king_check>` and :py:meth:`get_valid_cells <pieces.Piece.get_valid_cells>` methods.

        **HINT**: Kings can move horizontally, vertically and diagonally but only one piece at a time.

        You can call :py:meth:`cell_is_valid_and_empty <board.Board.cell_is_valid_and_empty>`, 
        :py:meth:`can_hit_on_cell <pieces.Piece.can_hit_on_cell>` and :py:meth:`can_enter_cell <pieces.Piece.can_enter_cell>` 
        to check for necessary conditions to implement the rook movability mechanics. 

        :return: A list of reachable cells this king could move into.
        """
        # TODO: Implement a method that returns all cells this piece can enter in its next move
        potential_cells = []

        directions = [
            np.array([1, 1]),
            np.array([-1, -1]),
            np.array([1, -1]),
            np.array([-1, 1]),
            np.array([1, 0]),
            np.array([-1, 0]),
            np.array([0, 1]),
            np.array([0, -1])
        ]

        # Go through all directions
        for direction in directions:
            next_cell = self.cell + direction
            potential_cells.append(next_cell)

        valid_cells = [cell for cell in potential_cells if self.can_enter_cell(cell)]
        return valid_cells
