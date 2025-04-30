import random
from tqdm import tqdm
from util import map_piece_to_character, cell_to_string


DEPTH = 3
MOVES_PER_DEPTH = [0, 2, 3, 5, 10, 15]


class MinMaxArg:
    def __init__(self, depth=DEPTH, playAsWhite=True):
        self.depth = depth
        self.playAsWhite = playAsWhite

    def next(self):
        return MinMaxArg(self.depth - 1, not self.playAsWhite)


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

        s = map_piece_to_character(self.piece).upper() + fr + center + to
        s += f"({self.score:.2f})"
        return s


def evaluate_all_possible_moves(board, minMaxArg, maximumNumberOfMoves = 10):
    """
    This method must evaluate all possible moves from all pieces of the current color. 
    So if minMaxArg.playAsWhite is True, all possible moves of all white pieces must be evaluated.
    And if minMaxArg.playAsWhite is False, all possible moves of all black pieces must be evaluated. 

    Iterate over all cells with pieces on them by calling the :meth:`board.iterate_cells_with_pieces` method. 
    For each piece, retrieve all valid moves by calling the :meth:piece:get_valid_cells: method of that piece. 

    In order to evaluate a valid move, first you need to place that piece on the respective cell. Call the :meth:`board.set_cell` method 
    to do so. Before doing so, remember the cell the piece is currently placed on as you will need to place it back later.
    Because placing a piece on a new cell could potential hit (and thus remove) an opposing piece currently placed on this cell, 
    you need to remember the piece on the target cell as well. Call :meth:`board.get_cell` to retrieve that piece and store it in a variable.

    After the new board configuration is set in place, call the :meth:`board.evaluate` method. You can use the 
    :class:`Move` class to store the move (piece and target cell) alongside its achieved evaluation score in a list. 

    Restore the original board configuration by placing the piece in its original cell and restoring any potentially removed piece before 
    moving on to the next move or piece. 

    Remember the :meth:`board.evaluate` method always evaluates from WHITEs perspective, so a higher evaluation
    relates to a better position for WHITE. 

    Moves must be sorted with respect o the scalar evaluation according to the minMax scheme. 
    So if minMaxArg.playAsWhite is True, the moves must be sorted in *descending* order, so the best evaluated move for white is in array position 0.
    So if minMaxArg.playAsWhite is False, the moves must be sorted in *ascending* order, so the worst evaluated move for white is in array position 0.

    Use the lists sort method and provide a proper key to the sorting algorithm, such that it sorts the moves according to the achieved score. 
    
    After sorting, a maximum number of moves as provided by the respective parameter must be returned. If there are 
    more moves possible (in most situations there are), only return the top (or worst). Hint: Slice the list after sorting. 
    """
    # Start with an empty list of moves
    moves = []

    # Iterate all possible moves for current color
    for piece in board.iterate_cells_with_pieces(minMaxArg.playAsWhite):
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


eval_cache = {}
total_hits = 0


def minMax_cached(board, minMaxArg):
    global eval_cache, total_hits

    # Calculate a unique hash code for the current board position and search depth
    hash = str(minMaxArg.depth) + board.hash()
    if hash in eval_cache:
        total_hits += 1
        # print(f"Cache hit! Cache has {len(eval_cache.keys())} entries with {total_hits} hits so far")
        return eval_cache[hash]

    # Its not the cache so do the actual evaluation
    bestMove = minMax(board, minMaxArg)

    # Cache it for later
    eval_cache[hash] = bestMove
    return bestMove


def minMax(board, minMaxArg):
    # First, get a sorted list of all possible moves and their respective board evaluations
    moves = evaluate_all_possible_moves(board, minMaxArg)

    # If there are no possible moves left, someone has one!
    if not moves:
        return Move(None, None, -500 if minMaxArg.playAsWhite else 500)

    # Restrict further analysis to the heuristicaly best moves
    d = DEPTH - minMaxArg.depth + 1
    movesToKeep = MOVES_PER_DEPTH[-d]
    moves = moves[:movesToKeep]

    # If there is depth left, see how opponent would behave for potential moves
    if minMaxArg.depth > 1:
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

            # Actually go down the rabbit hole
            bestMove = minMax_cached(board, minMaxArg.next())

            # Overwrite score
            move.score = bestMove.score

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

    # Shuffle and pick a random move
    random.shuffle(moves)
    return moves[0]


def suggest_move(board):
    return minMax_cached(board, MinMaxArg())
