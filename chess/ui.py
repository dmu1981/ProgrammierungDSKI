import pygame
from pieces import Piece, Pawn, Rook, Bishop, Queen, King, Knight


class UIState:
    def __init__(self):
        self.mouse_over_cell = None
        self.dragging = False
        self.selected_cell = None
        self.valid_cells = None

        pass


def load_sprites():
    return {
        "ROOK_WHITE": pygame.image.load(
            "sprites/100x100_rookwhite.png"
        ).convert_alpha(),
        "ROOK_BLACK": pygame.image.load(
            "sprites/100x100_rookblack.png"
        ).convert_alpha(),
        "KNIGHT_WHITE": pygame.image.load(
            "sprites/100x100_knightwhite.png"
        ).convert_alpha(),
        "KNIGHT_BLACK": pygame.image.load(
            "sprites/100x100_knightblack.png"
        ).convert_alpha(),
        "BISHOP_WHITE": pygame.image.load(
            "sprites/100x100_bishopwhite.png"
        ).convert_alpha(),
        "BISHOP_BLACK": pygame.image.load(
            "sprites/100x100_bishopblack.png"
        ).convert_alpha(),
        "QUEEN_WHITE": pygame.image.load(
            "sprites/100x100_queenwhite.png"
        ).convert_alpha(),
        "QUEEN_BLACK": pygame.image.load(
            "sprites/100x100_queenblack.png"
        ).convert_alpha(),
        "KING_WHITE": pygame.image.load(
            "sprites/100x100_kingwhite.png"
        ).convert_alpha(),
        "KING_BLACK": pygame.image.load(
            "sprites/100x100_kingblack.png"
        ).convert_alpha(),
        "PAWN_WHITE": pygame.image.load(
            "sprites/100x100_pawnwhite.png"
        ).convert_alpha(),
        "PAWN_BLACK": pygame.image.load(
            "sprites/100x100_pawnblack.png"
        ).convert_alpha(),
    }


def map_piece_to_sprite_tag(piece):
    if piece is None:
        return None

    c = None
    if isinstance(piece, Pawn):
        c = "PAWN"
    if isinstance(piece, Rook):
        c = "ROOK"
    if isinstance(piece, Knight):
        c = "KNIGHT"
    if isinstance(piece, Bishop):
        c = "BISHOP"
    if isinstance(piece, Queen):
        c = "QUEEN"
    if isinstance(piece, King):
        c = "KING"

    if piece.is_white():
        return c + "_WHITE"

    return c + "_BLACK"


def draw_checker_pattern(screen, uiState):
    COLOR_WHITE = (240, 220, 190)
    COLOR_BLACK = (160, 110, 95)

    screen.fill(COLOR_WHITE)

    # Draw check board
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 1:
                continue

            x = col * 100
            y = 700 - row * 100
            pygame.draw.rect(screen, COLOR_BLACK, pygame.Rect(x, y, 100, 100))

    # Draw valid cells
    if uiState.valid_cells is not None:
       for cell in uiState.valid_cells:
           row, col = cell
           x = col * 100 + 50
           y = 700 - row * 100 + 50
           pygame.draw.circle(screen, (196, 196, 196), (x, y), 35)
            

    # Highlight cell if any
    if uiState.dragging:
        row, col = uiState.selected_cell
        x = col * 100
        y = 700 - row * 100
        pygame.draw.rect(screen, (128, 0, 0), pygame.Rect(x, y, 100, 100), 3)

    if uiState.mouse_over_cell is not None:
        row, col = uiState.mouse_over_cell
        x = col * 100
        y = 700 - row * 100
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, 100, 100), 3)

    if uiState.dragging:
        row, col = uiState.mouse_over_cell
        xFrom = col * 100 + 50
        yFrom = 700 - row * 100 + 50
        row, col = uiState.selected_cell
        xTo = col * 100 + 50
        yTo = 700 - row * 100 + 50
        pygame.draw.line(screen, (255, 0, 0), (xFrom, yFrom), (xTo, yTo), 3)


def draw_board(screen, sprites, board):
    for row in range(8):
        for col in range(8):
            piece = board.get_cell((row, col))
            if piece is not None:
                tag = map_piece_to_sprite_tag(piece)
                sprite_to_draw = sprites[tag]

                x = col * 100
                y = 700 - row * 100
                screen.blit(sprite_to_draw, (x, y - 5))


def get_cell_under_mouse(uiState):
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())

    x, y = [int(v // 100) for v in mouse_pos]
    if x >= 0 and y >= 0 and x <= 7 and y <= 7:
        uiState.mouse_over_cell = (7 - y, x)
    else:
        uiState.mouse_over_cell = None

    return uiState


def run_game(board):
    # Initialize Pygame
    pygame.init()

    # Set up the game window
    screen = pygame.display.set_mode((800, 800))

    sprites = load_sprites()

    pygame.display.set_caption("Hello Pygame")

    # Game loop
    running = True
    uiState = UIState()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                piece = board.get_cell(uiState.mouse_over_cell)
                if piece:
                    uiState.dragging = True
                    uiState.valid_cells = piece.get_valid_cells()
                    uiState.selected_cell = uiState.mouse_over_cell

            if event.type == pygame.MOUSEBUTTONUP and uiState.dragging:
                uiState.dragging = False
                
                if uiState.selected_cell != uiState.mouse_over_cell:
                    for valid_cell in uiState.valid_cells:
                        if uiState.mouse_over_cell[0] == valid_cell[0] and\
                           uiState.mouse_over_cell[1] == valid_cell[1]:
                          
                          piece = board.get_cell(uiState.selected_cell)
                          piece.move_to(uiState.mouse_over_cell)

                          eval = board.evaluate()
                          print(f"White score: {eval:.4f}")
                
                uiState.valid_cells = None

        draw_checker_pattern(screen, uiState)
        draw_board(screen, sprites, board)

        uiState = get_cell_under_mouse(uiState)

        # Flip the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
