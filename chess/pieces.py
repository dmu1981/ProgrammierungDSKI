import numpy as np

class Piece:
    """
    Base class for pieces on the board. 
    
    A piece holds a reference to the board, its color and its currently located cell.
    In this class, you need to implement two methods, the "evaluate()" method and the "get_valid_cells()" method.
    """
    def __init__(self, board, white):
        self.board = board
        self.white = white
        self.cell = None

    def is_white(self):
        return self.white

    def can_enter_cell(self, cell):
        return self.board.piece_can_enter_cell(self, cell)

    def can_hit_on_cell(self, cell):
        return self.board.piece_can_hit_on_cell(self, cell)

    def evaluate(self):
        score = self.base_score  # Base value for this piece

        valid_cells = self.get_valid_cells()
        points_per_square = 0.01
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

        score += threat_score

        return score

    def get_valid_cells(self):
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
