import unittest
import json
from unittest_prettify.colorize import (
    colorize,
    RED,
)
from board import Board
from pieces import Pawn, Queen, Pawn, Rook, Knight, Bishop, King
from util import cell_to_string

def iterate_pieces(board):
  for row in board.cells:
    for piece in row:
      if piece is None:
        continue
      
      yield piece

def verify_piece_movability(board, piece, groundTruth):
  # If piece is None, just return
  if piece is None:
    return
  
  # Get reachable cells for given piece and turn into a set
  cells = piece.get_reachable_cells()
  

  # Check set equality with ground truth

class TestBoard(unittest.TestCase):
  def setUp(self):
    self.board = Board()
    self.board.reset()

  @colorize(color=RED)
  def test_none_is_not_valid_cell(self):
    """board.is_valid_cell() should return False is called with cell==None"""
    self.assertFalse(self.board.is_valid_cell(None), "None should not be a valid cell!")
    
  @colorize(color=RED) 
  def test_valid_cells_inside(self):
    """board.is_valid_cell() should return True for all cells in range (0..7, 0..7) (64 cells in total)"""
    for row in range(8):
      for col in range(8):
        self.assertTrue(self.board.is_valid_cell((row, col)), f"({row}, {col}) should be a valid cell!")

  @colorize(color=RED) 
  def test_valid_cells_outside(self):
    """board.is_valid_cell() should return False for all cells in range not in (0..7, 0..7)"""
    for row in range(-4, 12):
      for col in range(-4, 12):
        if row >= 0 and row < 8 and col >= 0 and col < 8:
          continue

        self.assertFalse(self.board.is_valid_cell((row, col)), f"({row}, {col}) should not be a valid cell!")

  @colorize(color=RED) 
  def test_cell_is_valid_and_empty(self):
    """board.cell_is_valid_and_empty() should return True for empty cells and False for used cells or invalid cells"""
    for row in range(8): 
      for col in range(8): # Go over all 8 columns
        if row <= 1 or row >= 6: # First two rows and last two rows are not empty
          self.assertFalse(self.board.cell_is_valid_and_empty((row, col)), f"({row}, {col}) should not be empty!")  
        else: # Center six rows are empty
          self.assertTrue(self.board.cell_is_valid_and_empty((row, col)), f"({row}, {col}) should be valid and empty!")

    # Test invalid cells as well
    for row in range(-4, 12):
      for col in range(-4, 12):
        if row >= 0 and row < 8 and col >= 0 and col < 8:
          continue

        self.assertFalse(self.board.is_valid_cell((row, col)), f"({row}, {col}) should not be a valid cell!")

  @colorize(color=RED) 
  def test_piece_can_enter(self):
    """board.cell_is_valid_and_empty() should return True for empty cells"""
    # Start with a white pawn, he can enter all of the 6 top rows but none of the bottom two rows
    piece = Pawn(self.board, True)

    for row in range(8): 
      for col in range(8): # Go over all 8 columns
        if row <= 1: # First two rows are white pieces, pawn cannot enter
          self.assertFalse(self.board.piece_can_enter_cell(piece, (row, col)), f"White pieces should not be able to enter ({row}, {col}) as there is another white piece!")  
        else: # Center six rows are empty
          self.assertTrue(self.board.piece_can_enter_cell(piece, (row, col)), f"White pieces should be able to enter ({row}, {col}) as there is no white piece yet!")  

    # Now do the same for a black pawn
    piece = Pawn(self.board, False)

    for row in range(8): 
      for col in range(8): # Go over all 8 columns
        if row >= 6: # Top two rows are black pieces, pawn cannot enter
          self.assertFalse(self.board.piece_can_enter_cell(piece, (row, col)), f"Black pieces should not be able to enter ({row}, {col}) as there is another black piece!")  
        else: # Center six rows are empty
          self.assertTrue(self.board.piece_can_enter_cell(piece, (row, col)), f"Black pieces should be able to enter ({row}, {col}) as there is no black piece yet!")            

    # Test invalid cells as well
    for row in range(-4, 12):
      for col in range(-4, 12):
        if row >= 0 and row < 8 and col >= 0 and col < 8:
          continue

        self.assertFalse(self.board.is_valid_cell((row, col)), f"({row}, {col}) should not be enterable as it is not a valid cell!")

  @colorize(color=RED) 
  def test_piece_can_hit_on_cell(self):
    """board.cell_is_valid_and_empty() should return True for empty cells"""
    # Start with a white pawn, he can hit all of the 2 top rows but none of the rows below
    piece = Pawn(self.board, True)

    for row in range(8): 
      for col in range(8): # Go over all 8 columns
        if row <= 5: # Everything except top two rows do not contain black pieces
          self.assertFalse(self.board.piece_can_hit_on_cell(piece, (row, col)), f"White pieces should not be able to hit on ({row}, {col}) as there is no black piece!")  
        else: 
          self.assertTrue(self.board.piece_can_hit_on_cell(piece, (row, col)), f"White pieces should be able to hit ({row}, {col}) as there is a black piece!")  

    # Now do the same for a black pawn
    piece = Pawn(self.board, False)

    for row in range(8): 
      for col in range(8): # Go over all 8 columns
        if row >= 2: # Everything but bottom two rows do not contain white pieces
          self.assertFalse(self.board.piece_can_hit_on_cell(piece, (row, col)), f"Black pieces should not be able to hit on ({row}, {col}) as there is no white piece!")  
        else: # Center six rows are empty
          self.assertTrue(self.board.piece_can_hit_on_cell(piece, (row, col)), f"Black pieces should be able to hit on ({row}, {col}) as there is a white piece!")            

    # Test invalid cells as well
    for row in range(-4, 12):
      for col in range(-4, 12):
        if row >= 0 and row < 8 and col >= 0 and col < 8:
          continue

        self.assertFalse(self.board.is_valid_cell((row, col)), f"Should not be able to hit on ({row}, {col}) as it is not a valid cell!")

  @colorize(color=RED) 
  def test_movability(self):
    # Load JSON Test Suite
    with open("movement_test.json", "rt") as f:
      suite = json.load(f)

    # Iterate all test cases
    for testcase in suite["testcases"]:
      # Load the configuration from disk
      self.board.load_from_disk(testcase["configuration"])

      # Iterate all pieces on the board
      # movability = {}
      # for piece in iterate_pieces(self.board):
      #   # Get reachable cells and turn into a set
      #   cells = piece.get_reachable_cells()
      #   cells = [ (int(row), int(col)) for row, col in cells ]

      #   # Add to movability dictionary
      #   key = cell_to_string(piece.cell)
      #   movability[key] = cells
      # print(json.dumps(movability))

      movability = testcase["movability"]

      # Now iterate all pieces and check if their actual movability matches the ground truth
      for piece in iterate_pieces(self.board):
        # Write cell in clear text
        key = cell_to_string(piece.cell)

        # Get ground truth from file, turn into a set
        groundTruth = { (row, col) for row, col in movability[key] }

        # Get actually reachable cells, turn into a set
        actual = { (int(row), int(col)) for row, col in piece.get_reachable_cells() }

        # If they match, all is fine
        if actual == groundTruth:
          continue

        # If not, output a meaningful message
        self.fail(f"Movement of piece {type(piece)} wrongly implemented!")


if __name__ == "__main__":
  unittest.main()