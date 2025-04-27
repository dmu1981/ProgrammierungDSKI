from pieces import Pawn, Rook, Bishop, Queen, King, Knight


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


def cell_to_string(cell):
    files = ["a", "b", "c", "d", "e", "f", "g", "h"]
    return files[cell[1]] + str(cell[0] + 1)


class InvalidRowException:
    def __init__(self, cell):
        self.cell = cell


class InvalidColumnException:
    def __init__(self, cell):
        self.cell = cell
