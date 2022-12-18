import pygame

from Game.constants import *
from Game.Pieces import *


class Queen(Piece):
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


        for i in range(row+1, 8):

            if Board[i][col] == 0:

                self.available_moves.append((i,col))
            else:
                if Board[i][col].color != self.color:

                    self.available_moves.append((i,col))
                    break
                else:
                    break

        for j in range(row-1,-1,-1):

            if Board[j][col] == 0:

                self.available_moves.append((j,col))

            else:
                if Board[j][col].color != self.color:

                    self.available_moves.append((j,col))
                    break

                else:

                    break

        for i in range(col+1, 8):
            if Board[row][i] == 0:
                self.available_moves.append((row,i))

            else:
                if Board[row][i].color != self.color:
                    self.available_moves.append((row,i))
                    break

                else:
                    break

        for i in range(col-1, -1,-1):

            if Board[row][i] == 0:
                self.available_moves.append((row,i))

            else:
                if Board[row][i].color != self.color:
                    self.available_moves.append((row,i))
                    break

                else:
                    break

        return self.available_moves



