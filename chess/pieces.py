class Piece:
    def __init__(self, board, white):
        self.board = board
        self.white = white
        self.cell = None

    def move_to(self, cell):
        self.board.set_cell(cell, self)

    def is_white(self):
        return self.white

    def is_black(self):
        return not self.white

    def is_same_color(self, this):
        return self.color == this.color

    def is_opponent(self, this):
        return self.color != this.color


class Pawn(Piece):  # Bauer
    def __init__(self, board, white):
        super().__init__(board, white)


class Rook(Piece):  # Turm
    def __init__(self, board, white):
        super().__init__(board, white)


class Knight(Piece):  # Springer
    def __init__(self, board, white):
        super().__init__(board, white)


class Bishop(Piece):  # Läufer
    def __init__(self, board, white):
        super().__init__(board, white)


class Queen(Piece):  # Königin
    def __init__(self, board, white):
        super().__init__(board, white)


class King(Piece):  # König
    def __init__(self, board, white):
        super().__init__(board, white)
