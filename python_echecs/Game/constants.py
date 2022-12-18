import pygame
import os

Width, Height = 700,700
Rows, Cols = 8,8
Square = Width//Rows

Black = (0,0,0)
White = (255,255,255)
camel = (184, 159, 122)
brown = (106, 86, 57)
Chocolate = (27, 22, 14)



#Black

Black_Knight = pygame.transform.scale(pygame.image.load(os.path.join("Game\images", "bKN.png")), (Square, Square))
Black_King = pygame.transform.scale(pygame.image.load(os.path.join("Game\images", "bK.png")), (Square, Square))
Black_Queen = pygame.transform.scale(pygame.image.load(os.path.join("Game\images", "bQ.png")), (Square, Square))
Black_Bishop = pygame.transform.scale(pygame.image.load(os.path.join("Game\images", "bB.png")), (Square, Square))
Black_Pawn = pygame.transform.scale(pygame.image.load(os.path.join("Game\images", "bP.png")), (Square, Square))
Black_Rook = pygame.transform.scale(pygame.image.load(os.path.join("Game\images", "bR.png")), (Square, Square))

#White
White_Knight = pygame.transform.scale(pygame.image.load(os.path.join("Game\images", "wKN.png")), (Square, Square))
White_King = pygame.transform.scale(pygame.image.load(os.path.join("Game\images", "wK.png")), (Square, Square))
White_Queen = pygame.transform.scale(pygame.image.load(os.path.join("Game\images", "wQ.png")), (Square, Square))
White_Bishop = pygame.transform.scale(pygame.image.load(os.path.join("Game\images", "wB.png")), (Square, Square))
White_Pawn = pygame.transform.scale(pygame.image.load(os.path.join("Game\images", "wp.png")), (Square, Square))
White_Rook = pygame.transform.scale(pygame.image.load(os.path.join("Game\images", "wR.png")), (Square, Square))