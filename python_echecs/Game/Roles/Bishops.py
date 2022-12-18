import pygame

from Game.constants import *
from Game.Pieces import *

class Bishop(Piece):
    def __init__(self, Square, image,color,type,row,col):
        super().__init__(Square, image,color,type,row,col)

    def get_available_moves(self,row,col,Board):
        self.clear_available_moves()

        row_i = row+1
        col_i = col+1
        while row_i <= 7 and col_i <= 7:
            if Board[row_i][col_i] == 0:
                self.available_moves.append((row_i,col_i))
                row_i += 1
                col_i += 1

            else:
                if Board[row_i][col_i].color != self.color:
                    self.available_moves.append((row_i,col_i))
                    break
                break

        row_i = row-1
        col_i = col-1
        while row_i >= 0 and col_i >= 0:

            if Board[row_i][col_i] == 0:
                self.available_moves.append((row_i,col_i))
                row_i -= 1
                col_i -= 1

            else:
                if Board[row_i][col_i].color != self.color:
                    self.available_moves.append((row_i,col_i))
                    break
                break



        row_i = row-1
        col_i = col+1
        while row_i >= 0 and col_i <= 7:


            if Board[row_i][col_i] == 0:
                self.available_moves.append((row_i, col_i))
                row_i -= 1
                col_i += 1

            else:
                if Board[row_i][col_i].color != self.color:
                    #print("third loop",row_i, col_i)
                    self.available_moves.append((row_i, col_i))
                    break

                break

        row_i = row+1
        col_i = col-1
        while row_i <= 7 and col_i >= 0:

            if Board[row_i][col_i] == 0:
                self.available_moves.append((row_i, col_i))
                row_i += 1
                col_i -= 1
            else:
                if Board[row_i][col_i].color != self.color :
                    self.available_moves.append((row_i, col_i))
                    break

                break

        return self.available_moves


