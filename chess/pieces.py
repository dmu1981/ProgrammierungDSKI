import numpy as np

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
    
    def get_valid_cells(self):
        raise NotImplementedError()
    
    def can_enter_cell(self, cell):
        return self.board.piece_can_enter_cell(self, cell)
    
    def can_hit_on_cell(self, cell):
        return self.board.piece_can_hit_on_cell(self, cell)
        

class Pawn(Piece):  # Bauer
    def __init__(self, board, white):
        super().__init__(board, white)

    def get_valid_cells(self):
        move_dir = np.array([1, 0]) if self.is_white() else np.array([-1, 0])
        
        potential_cells = []
        potential_cells.append(self.cell + move_dir)
        
        if self.white and self.cell[0] == 1:
            potential_cells.append(self.cell + move_dir * 2)

        if not self.white and self.cell[0] == 6:
            potential_cells.append(self.cell + move_dir * 2)

        potential_cells = [cell for cell in potential_cells if self.board.get_cell(cell) is None]

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

    def get_valid_cells(self):
        potential_cells = []

        directions = [
            np.array([ 1,  0]),
            np.array([-1,  0]),
            np.array([ 0,  1]),
            np.array([ 0, -1]),
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

    def get_valid_cells(self):
        potential_cells = []

        moves = [
            np.array([ 2, 1]),
            np.array([ 1, 2]),
            np.array([-1, 2]),
            np.array([-2, 1]),
            np.array([-2,-1]),
            np.array([-1,-2]),
            np.array([ 1,-2]),
            np.array([ 2,-1]),
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

    def get_valid_cells(self):
        potential_cells = []

        directions = [
            np.array([ 1,  1]),
            np.array([-1, -1]),
            np.array([ 1, -1]),
            np.array([-1,  1]),
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

    def get_valid_cells(self):
        potential_cells = []

        directions = [
            np.array([ 1,  1]),
            np.array([-1, -1]),
            np.array([ 1, -1]),
            np.array([-1,  1]),
            np.array([ 1,  0]),
            np.array([-1,  0]),
            np.array([ 0,  1]),
            np.array([ 0, -1]),
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

    def get_valid_cells(self):
        potential_cells = []

        directions = [
            np.array([ 1,  1]),
            np.array([-1, -1]),
            np.array([ 1, -1]),
            np.array([-1,  1]),
            np.array([ 1,  0]),
            np.array([-1,  0]),
            np.array([ 0,  1]),
            np.array([ 0, -1]),
                  ]
        
        # Go through all directions
        for direction in directions:
          next_cell = self.cell + direction
          potential_cells.append(next_cell)

        valid_cells = [cell for cell in potential_cells if self.can_enter_cell(cell)]
        return valid_cells
