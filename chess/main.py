import numpy as np
from pieces import Piece, Pawn, Rook, Bishop, Queen, King, Knight
from ui import run_game


class InvalidRowException:
    def __init__(self, cell):
        self.cell = cell


class InvalidColumnException:
    def __init__(self, cell):
        self.cell = cell


def map_piece_to_character(piece):
    if piece is None:
        return "."

    c = None
    if isinstance(piece, Pawn):
        c = "P"
    if isinstance(piece, Rook):
        c = "R"
    if isinstance(piece, Knight):
        c = "N"
    if isinstance(piece, Bishop):
        c = "B"
    if isinstance(piece, Queen):
        c = "Q"
    if isinstance(piece, King):
        c = "K"

    if piece.is_white():
        return c

    return c.lower()


class Board:
    def __init__(self):
        self.cells = [[None for _ in range(8)] for _ in range(8)]

    def __str__(self):
        return "\n".join(
            [
                " ".join([map_piece_to_character(cell) for cell in row])
                for row in reversed(self.cells)
            ]
        )
    
    def iterate_pieces(self, white):
        for row in self.cells:
            for cell in row:
                if cell is None:
                    continue
                
                if cell.white == white:
                    yield cell

    def evaluate(self):
        score = 0
        
        # Iterate all white pieces and add score
        for piece in self.iterate_pieces(True):
            score += piece.evaluate()

        # Iterate all white pieces and substract score
        for piece in self.iterate_pieces(False):
            score -= piece.evaluate()

        return score


    def is_valid_cell(self, cell):
        # TODO: Return True if the given cell is valid, meaning it exists on the board.
        # Special case: Handle cell is None properly!
        if cell is None:
            return False

        row, col = cell
    
        if row < 0 or row >= 8:
            return False

        if col < 0 or col >= 8:
            return False
      
        return True
    
    def cell_is_valid_and_empty(self, cell):
        # TODO: Return True if the given cell is valid and there is no piece place on it currently
        if not self.is_valid_cell(cell):
            return False
        
        other_piece = self.get_cell(cell)
        if other_piece is None:
            return True
        
        return False

    def piece_can_enter_cell(self, piece, cell):
        # TODO: Return True if the given cell can be entered by the given piece.
        # Note: The cell must be valid and, if there is already a piece, it must be from the opposing color
        if not self.is_valid_cell(cell):
            return False

        other_piece = self.get_cell(cell)
        if other_piece is None:
            return True
        
        if other_piece.white != piece.white:
            return True

        return False 
    
    def piece_can_hit_on_cell(self, piece, cell):
        # TODO: Return True if the given piece can hit an opponent piece on the given cell
        # Note: The cell must be valid and there *must* be a piece of opposing color on the cell
        if not self.is_valid_cell(cell):
            return False

        other_piece = self.get_cell(cell)
        if other_piece is None:
            return False
        
        if other_piece.white != piece.white:
            return True

        return False 

    def get_cell(self, cell):
        if cell is None:
            return None

        row, col = cell

        if row < 0 or row >= 8:
            raise InvalidRowException(row, col)

        if col < 0 or col >= 8:
            raise InvalidColumnException(row, col)

        return self.cells[row][col]
    
    def get_cell_or_none(self, cell):
        try:
            return self.get_cell(self, cell)
        except:
            return None

    def set_cell(self, cell, piece):
        row, col = cell

        if row < 0 or row >= 8:
            raise InvalidRowException(row, col)

        if col < 0 or col >= 8:
            raise InvalidColumnException(row, col)

        if piece is not None:
            if piece.cell is not None:
                self.set_cell(piece.cell, None)

            piece.cell = (row, col)

        self.cells[row][col] = piece

    def reset(self):
        # Pawns
        for col in range(8):
            self.set_cell(np.array([1, col]), Pawn(self, True))
            self.set_cell(np.array([6, col]), Pawn(self, False))

        # Rooks
        self.set_cell(np.array([0, 0]), Rook(self, True))
        self.set_cell(np.array([0, 7]), Rook(self, True))
        self.set_cell(np.array([7, 0]), Rook(self, False))
        self.set_cell(np.array([7, 7]), Rook(self, False))

        # Knights
        self.set_cell(np.array([0, 1]), Knight(self, True))
        self.set_cell(np.array([0, 6]), Knight(self, True))
        self.set_cell(np.array([7, 1]), Knight(self, False))
        self.set_cell(np.array([7, 6]), Knight(self, False))

        # Bishops
        self.set_cell(np.array([0, 2]), Bishop(self, True))
        self.set_cell(np.array([0, 5]), Bishop(self, True))
        self.set_cell(np.array([7, 2]), Bishop(self, False))
        self.set_cell(np.array([7, 5]), Bishop(self, False))

        # Queen
        self.set_cell(np.array([0, 3]), Queen(self, True))
        self.set_cell(np.array([7, 3]), Queen(self, False))

        # King
        self.set_cell(np.array([0, 4]), King(self, True))
        self.set_cell(np.array([7, 4]), King(self, False))


board = Board()
board.reset()

run_game(board)