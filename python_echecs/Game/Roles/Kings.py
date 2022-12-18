import pygame

from Game.constants import *
from Game.Pieces import *

class King(Piece):
    def __init__(self,Square, image,color,type,row,col):
        super().__init__(Square, image,color,type,row,col)




    def get_available_moves(self,row,col,Board):
        self.clear_available_moves()

        if row-1 >= 0:
            if Board[row-1][col] == 0 or Board[row-1][col].color != self.color:
                self.available_moves.append((row-1,col))

        if row-1 >= 0 and col+1 < len(Board):
            if Board[row-1][col+1] == 0 or Board[row-1][col+1].color != self.color:
                self.available_moves.append((row-1,col+1))

        if col+1 < len(Board):
            if Board[row][col+1] == 0 or Board[row][col+1].color != self.color:
                self.available_moves.append((row,col+1))

        if row+1 < len(Board) and col+1 < len(Board):
            if Board[row+1][col+1] == 0 or Board[row+1][col+1].color != self.color:
                self.available_moves.append((row+1,col+1))

        if row+1 < len(Board):
            if Board[row+1][col] == 0 or Board[row+1][col].color != self.color:
                self.available_moves.append((row+1,col))

        if row+1 < len(Board) and col-1 >= 0:
            if Board[row+1][col-1] == 0 or Board[row+1][col-1].color != self.color:
                self.available_moves.append((row+1,col-1))

        if col-1 >= 0:
            if Board[row][col-1] == 0 or Board[row][col-1].color != self.color:
                self.available_moves.append((row,col-1))

        if row-1 >= 0 and col-1 >= 0:
            if Board[row-1][col-1] == 0 or Board[row-1][col-1].color != self.color:
                self.available_moves.append((row-1, col-1))


        return self.available_moves
