import random
from pieces import Piece, Pawn, Rook, Bishop, Queen, King, Knight
from tqdm import tqdm

DEPTH = 3
MOVES_PER_DEPTH = [0, 2, 3, 5, 10, 15]

class MinMaxArg:
    def __init__(self, depth=DEPTH, playAsWhite = True):
        self.depth = depth
        self.playAsWhite = playAsWhite

    def next(self):
        return MinMaxArg(self.depth - 1, not self.playAsWhite)
    

def map_piece_to_char(piece):
    if piece is None:
        return None

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

    return c

def cell_to_string(cell):
    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return files[cell[1]] + str(cell[0]+1)

class Move:
    def __init__(self, piece, cell, score):
        self.piece = piece
        self.cell = cell
        self.score = score

    def __str__(self):
        fr = cell_to_string(self.piece.cell)
        to = cell_to_string(self.cell)
        center = "."
        if not self.piece.board.cell_is_valid_and_empty(self.cell):
            center = "x"

        s = map_piece_to_char(self.piece) + fr + center + to
        s += f"({self.score:.2f})"
        return s
    
eval_cache = {}    
total_hits = 0
def retrieve_from_cache(board, depth):
    global eval_cache, total_hits
    
    # Calculate a unique hash code for the current board position and search depth
    hash = str(depth) + board.hash()
    if hash in eval_cache:
        total_hits += 1
        #print(f"Cache hit! Cache has {len(eval_cache.keys())} entries with {total_hits} hits so far")
        return eval_cache[hash]
    
    return None

def add_to_cache(board, depth, score):
    global eval_cache
    # Calculate a unique hash code for the current board position and search depth
    hash = str(depth) + board.hash()
    eval_cache[hash] = score

def evaluate_all_possible_moves(board, minMaxArg):
    # Start with an empty list of moves
    moves = []

    # Iterate all possible moves for current color
    for piece in board.iterate_pieces(minMaxArg.playAsWhite):
      # Get valid moves for current piece
      valid_moves = piece.get_valid_cells()

      # Remember where we came from
      starting_position = piece.cell

      # Iterate all valid cells of this piece
      for cell in valid_moves:
          # Remember if we hit anything
          old_piece = board.get_cell(cell)

          # Make that move
          board.set_cell(cell, piece)

          # Evaluate board position
          score = board.evaluate()

          # Remember this potential move
          moves.append(Move(piece, cell, score))

          # Restore board
          board.set_cell(starting_position, piece)
          board.set_cell(cell, old_piece)

    # Sort moves by score
    moves.sort(key=lambda move: move.score, reverse=minMaxArg.playAsWhite)

    return moves

def minMax(board, minMaxArg):
    # First, get a sorted list of all possible moves and their respective board evaluations
    moves = evaluate_all_possible_moves(board, minMaxArg)

    # If there are no possible moves left, someone has one!
    if not moves:
        return Move(None, None, -500 if minMaxArg.playAsWhite else 500)
        

    # Restrict further analysis to the best 10 moves
    d = DEPTH - minMaxArg.depth + 1
    movesToKeep = MOVES_PER_DEPTH[-d]
    moves = moves[:movesToKeep]
    
    # If there is depth left, see how opponent would behave for potential moves
    if minMaxArg.depth > 1:
      nextMinMax = minMaxArg.next()

      # Go through best 10 moves
      iter = moves
      if minMaxArg.depth == DEPTH:
          iter = tqdm(moves)

      for move in iter:
          if minMaxArg.depth == DEPTH:
              iter.set_description(str(move))

          # Implement move
          starting_position = move.piece.cell
          old_piece = board.get_cell(move.cell)
          board.set_cell(move.cell, move.piece)

          # Try to retrieve evaluation from cache
          score = retrieve_from_cache(board, nextMinMax.depth)
          if score is None:
            # Actually go down the rabbit hole
            bestMove = minMax(board, nextMinMax)
            add_to_cache(board, nextMinMax.depth, bestMove.score)
            score = bestMove.score

          # Overwrite score
          move.score = score

          # Restore board
          board.set_cell(starting_position, move.piece)
          board.set_cell(move.cell, old_piece)          
    
      # Sort moves by score again
      moves.sort(key=lambda move: move.score, reverse=minMaxArg.playAsWhite)

    # If we are down the rabbit hole, always return the best move
    if minMaxArg.depth < DEPTH:
        return moves[0]
    
    # Keep the best moves (minimum 1.0 score less than best move)
    minScore = moves[0].score - 1.0
    moves = [move for move in moves if move.score > minScore]

    # Debug output
    print("Depth: ", minMaxArg.depth, [str(move) for move in moves])
    
    # If there is a guaranteed winning move, never risk that
    if moves[0].score > 250:
        return moves[0]

    # Shuffle and pick a random move    
    random.shuffle(moves)
    return moves[0]

def suggest_move(board):
    minMaxArg = MinMaxArg()
    
    return minMax(board, minMaxArg)