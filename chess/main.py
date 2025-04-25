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

    def get_cell(self, cell):
        if cell is None:
            return None

        row, col = cell

        if row < 0 or row >= 8:
            raise InvalidRowException(row, col)

        if col < 0 or col >= 8:
            raise InvalidColumnException(row, col)

        return self.cells[row][col]

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
            self.set_cell((1, col), Pawn(self, True))
            self.set_cell((6, col), Pawn(self, False))

        # Rooks
        self.set_cell((0, 0), Rook(self, True))
        self.set_cell((0, 7), Rook(self, True))
        self.set_cell((7, 0), Rook(self, False))
        self.set_cell((7, 7), Rook(self, False))

        # Knights
        self.set_cell((0, 1), Knight(self, True))
        self.set_cell((0, 6), Knight(self, True))
        self.set_cell((7, 1), Knight(self, False))
        self.set_cell((7, 6), Knight(self, False))

        # Bishops
        self.set_cell((0, 2), Bishop(self, True))
        self.set_cell((0, 5), Bishop(self, True))
        self.set_cell((7, 2), Bishop(self, False))
        self.set_cell((7, 5), Bishop(self, False))

        # Queen
        self.set_cell((0, 3), Queen(self, True))
        self.set_cell((7, 3), Queen(self, False))

        # King
        self.set_cell((0, 4), King(self, True))
        self.set_cell((7, 4), King(self, False))


board = Board()
board.reset()

run_game(board)
