'''
Created on Mar 31, 2015

@author: Andrea Martire
'''
from gmpy import mpz

#colors
WHITE = 0
BLACK = 1

#pieces
PAWN = 0
KNIGHT = 1
BITSHOP = 2
ROOK = 3
QUEEN = 4
KING = 5

#piece code
NO_PIECE_CODE = mpz(0)
PAWN_CODE = mpz(1)
KNIGHT_CODE = mpz(2)
BITSHOP_CODE = mpz(3)
ROOK_CODE = mpz(4)
QUEEN_CODE = mpz(5)
KING_CODE = mpz(6)

#directions
RIGHT = 0
RIGHT_UP = 1
UP = 2
LEFT_UP = 3
LEFT = 4
LEFT_DOWN = 5
DOWN = 6
RIGHT_DOWN = 7

#only for pawns
DOUBLE_UP = 8
