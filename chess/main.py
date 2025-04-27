from ui import run_game
from board import Board


board = Board()
#board.reset()

board.load_from_disk("66cc6670-f709-4d7e-a9c9-ccad40af2207.board")


run_game(board)
