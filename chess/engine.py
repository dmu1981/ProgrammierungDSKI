import random
from tqdm import tqdm
from util import map_piece_to_character, cell_to_string


DEPTH = 3


class MinMaxArg:
    """ Helper Class for the MinMax Algorithm.
    This class stores the current search depth and whether we are playing as white or black in this stage. 

    Note: You don´t need to implement anything in this case, you can use it in the MinMax Algorithm as you seem fit. 
    """
    def __init__(self, depth=DEPTH, playAsWhite=True):
        """
        Initializes the class using the provided parameters
        """
        self.depth = depth
        self.playAsWhite = playAsWhite

    def next(self):
        """ 
        Provides the next stage of the MinMax Algorithm by reducing the depth by one and toggling playAsWhite
        """
        return MinMaxArg(self.depth - 1, not self.playAsWhite)


class Move:
    """
    Helper class to store an evaluated move for the MinMax Algorithm. 
    This class contains the piece that should be moved as well as the cell it should move into alongside with the evaluation score for this move. 

    Note: You don´t need to implement anything in this case, you can use it in the MinMax Algorithm as you seem fit. 
    """

    def __init__(self, piece, cell, score):
        """
        Constructor initializes the class according to the provided parameters
        """
        self.piece = piece
        self.cell = cell
        self.score = score

    def __str__(self):
        """
        Helper class to turn this move into a neat string representation following the official chess notation guidelines.
        Note: This method does not properly indicate a check "+" or check-mate "#" in the notation as that would require a
        deeper analysis of the resulting board configuration. However, it appends the evaluated score of this move just for reference. 
        """
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

    Iterate over all cells with pieces on them by calling the :py:meth:`iterate_cells_with_pieces <board.Board.iterate_cells_with_pieces>` method. 
    For each piece, retrieve all valid moves by calling the :py:meth:`get_valid_cells <pieces.Piece.get_valid_cells>` method of that piece. 

    In order to evaluate a valid move, first you need to place that piece on the respective cell. Call the :py:meth:`set_cell <board.BoardBase.set_cell>` method 
    to do so. Before doing so, remember the cell the piece is currently placed on as you will need to place it back later.
    Because placing a piece on a new cell could potential hit (and thus remove) an opposing piece currently placed on this cell, 
    you need to remember the piece on the target cell as well. Call :py:meth:`get_cell <board.BoardBase.get_cell>` to retrieve that piece and store it in a variable.

    After the new board configuration is set in place, call the :py:meth:`evaluate <board.Board.evaluate>` method. You can use the 
    :py:class:`Move` class to store the move (piece and target cell) alongside its achieved evaluation score in a list. 

    Restore the original board configuration by placing the piece in its original cell and restoring any potentially removed piece before 
    moving on to the next move or piece. 

    Remember the :py:meth:`evaluate <board.Board.evaluate>` method always evaluates from WHITEs perspective, so a higher evaluation
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

    # Return only the request top amount of moves
    return moves[:maximumNumberOfMoves]


def minMax(board, minMaxArg):
    """
    This method implement the core mini-max search algorithm.
    The minMaxArg contain information about whether we are currently 
    playing as white or black as well as the remaining search depth. 

    If minMaxArg.depth equals 1, no additional moves will be considered and
    the best evaluated move for the current board configuration should be 
    returned. If, however, minMaxArg.depth is greater than 1, for each possible
    move of the current color, all answering moves of the opposite color need 
    to be considered. 

    *HINT*: Start by calling :py:func:`evaluate_all_possible_moves <engine.evaluate_all_possible_moves>`
    with the provided board and minMaxArg in order to receive a list of evaluated moves.
    Note that the list is already sorted and contains only the best possible moves for the current color. 
    This means if white is playing, the returned list will contain the best moves for white to make
    whereas if black is playing, the returned list will contain the best moves for black to make first. 

    You will need to handle the special case that there are no possible moves left,
    meaning the :py:func:`evaluate_all_possible_moves <engine.evaluate_all_possible_moves>`
    method returns an empty list. If there are no possible moves left, this means
    the current color has lost the game. Indicate that by returning an instance of the 
    :py:class:`Move` class where you set the score attribute to a very high or very low value
    (remember: Always think from whites perspective!)

    If the remaining search depth is greater than 1 (minMaxArg.depth > 1),
    iterate over all possible moves. Implement each move by placing the piece in question on the respective cell. 
    Call the :py:meth:`set_cell <board.BoardBase.set_cell>` method 
    to do so. Before doing so, remember the cell the piece is currently placed on as you will need to place it back later.
    Because placing a piece on a new cell could potential hit (and thus remove) an opposing piece currently placed on this cell, 
    you need to remember the piece on the target cell as well. Call :py:meth:`get_cell <board.BoardBase.get_cell>` 
    to retrieve that piece and store it in a variable.

    After the new board configuration is set in place, 
    call the :py:meth:`minMax_cached <engine.minMax_cached>` method
    with the next minMaxArg (call :py:meth:`next <engine.MinMaxArg.next>`)

    Overwrite the current moves score with the result from the recursive call.
    
    Restore the original board configuration by placing the piece in its original cell and restoring any potentially removed piece before 
    moving on to the next move. 

    After all moves and their counter-moves have been evaluated sort the list
    again in the correct order according to the (new) scores. If playing as white
    (minMaxArg.playAsWhite == True), you need to sort in descending order (highest ranked move first)
    whereas if playing as black (minMaxArg.playAsBlack == False), you need to sort
    in ascending order (lowest ranked move first). Use the lists sort method and
    define a proper key function to implement the needed search. 

    In the most basic implementation of the algorithm return the best move after sorting. 

    **NOTE**: You can improve the replayability of your chess engine a bit
    if you add some randomness to the evaluation of moves. For example, you 
    can randomly increment and decrement each evaluation score. Alternatively
    you can return a random move out of the best three instead of simply the best one. 

    Feel free to experiment with this once you have the core algorithm properly implemented. 

    :param board: Reference to the board we need to play on
    :type board: :py:class:`board.Board`
    :param minMaxArg: The combined arguments for the mini-max search algorithm.
    :type minMaxArg: :py:class:`MinMaxArg`
    :return: Return the best move to make in the current situation.
    :rtype: :py:class:`Move`
    """
    # First, get a sorted list of all possible moves and their respective board evaluations
    moves = evaluate_all_possible_moves(board, minMaxArg)

    # If there are no possible moves left, someone has one!
    if not moves:
        return Move(None, None, -500 if minMaxArg.playAsWhite else 500)

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
    """
    Helper function to start the mini-max algorithm.
    """
    return minMax_cached(board, MinMaxArg())

eval_cache = {}
total_hits = 0


def minMax_cached(board, minMaxArg):
    """
    A cached version of the minMax method. This methods caches results
    based on its parameters. If called again with a known board configuration
    and minMaxArgs, the result is taken from the cache instead of repeating
    the mini-max algorithm again. This can save computation time as
    it avoid to repeat evaluations over and over again. 
    """
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
