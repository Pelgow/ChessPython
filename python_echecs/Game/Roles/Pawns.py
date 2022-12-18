import pygame

from Game.constants import *
from Game.Pieces import *


class Pawn(Piece):
    def __init__(self, Square, image, color, type, row, col):
        super().__init__(Square, image, color, type, row, col)
        self.first_move = True

    def get_available_moves(self, row, col, Board):

        self.clear_available_moves()

        # White
        if self.color == White:
            if row - 1 >= 0:
                if Board[row - 1][col] == 0:
                    self.available_moves.append((row - 1, col))

                if self.first_move:
                    if Board[row - 2][col] == 0:
                        self.available_moves.append((row - 2, col))

                if col - 1 >= 0:
                    if Board[row - 1][col - 1] != 0:
                        piece = Board[row - 1][col - 1]
                        if piece.color != self.color:
                            self.available_moves.append((row - 1, col - 1))

            if col + 1 < len(Board[0]):
                if Board[row - 1][col + 1] != 0:
                    piece = Board[row - 1][col + 1]
                    if piece.color != self.color:
                        self.available_moves.append((row - 1, col + 1))

        # Black
        if self.color == Black:

            if row + 1 < len(Board):
                if Board[row + 1][col] == 0:
                    self.available_moves.append((row + 1, col))

                if self.first_move:
                    if Board[row + 1][col] == 0 and Board[row + 2][col] == 0:
                        self.available_moves.append((row + 2, col))

                if col - 1 >= 0:
                    if Board[row + 1][col - 1] != 0:
                        piece = Board[row + 1][col - 1]
                        if piece.color != self.color:
                            self.available_moves.append((row + 1, col - 1))

            if row + 1 < len(Board) and col + 1 < len(Board[0]):
                if Board[row + 1][col + 1] != 0:
                    piece = Board[row + 1][col + 1]
                    if piece.color != self.color:
                        self.available_moves.append((row + 1, col + 1))

        return self.available_moves
