import pygame

from Game.constants import *
from Game.Pieces import *

class Knight(Piece):
    def __init__(self, Square, image,color,type,row,col):
        super().__init__(Square, image,color,type,row,col)

    def get_available_moves(self,row,col,Board):
        self.clear_available_moves()

        if row-2 >= 0 and col+1 < len(Board):
            if Board[row-2][col+1] == 0 or Board[row-2][col+1].color != self.color:
                self.available_moves.append((row-2,col+1))

        if row-1 >= 0 and col+2 < len(Board):
            if Board[row-1][col+2] == 0 or Board[row-1][col+2].color != self.color:
                self.available_moves.append((row-1,col+2))

        if row+1 < len(Board) and col+2 < len(Board):
            if Board[row+1][col+2] == 0 or Board[row+1][col+2].color != self.color:
                self.available_moves.append((row+1,col+2))

        if row+2 < len(Board) and col+1 < len(Board):
            if Board[row+2][col+1] == 0 or Board[row+2][col+1].color != self.color:
                self.available_moves.append((row+2,col+1))

        if row+2 < len(Board) and col-1 >= 0:
            if Board[row+2][col-1] == 0 or Board[row+2][col-1].color != self.color:
                self.available_moves.append((row+2,col-1))

        if row+1 < len(Board) and col-2 >= 0:
            if Board[row+1][col-2] == 0 or Board[row+1][col-2].color != self.color:
                self.available_moves.append((row+1,col-2))


        if row-1 >= 0 and col-2 >= 0:
            if Board[row-1][col-2] == 0 or Board[row-1][col-2].color != self.color:
                self.available_moves.append((row-1,col-2))

        if row-2 >= 0 and col-1 >= 0:
            if Board[row-2][col-1] == 0 or Board[row-2][col-1].color != self.color:
                self.available_moves.append((row-2,col-1))


        return self.available_moves


