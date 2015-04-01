'''
Created on 31/mar/2015

@author: Andrea Martire
'''
from gmpy import mpz

#move types
QUIET = 0
DOUBLE_PAWN = 1
KING_CASTLE = 2
QUEEN_CASTLE = 3
CAPTURE = 4
EP_CAPTURE = 5
KNIGHT_PROMOTION = 8
BITSHOP_PROMOTION = 9
ROOK_PROMOTION = 10
QUEEN_PROMOTION = 11
KNIGHT_PROMO_CAPTURE = 12
BITSHOP_PROMO_CAPTURE = 13
ROOK_PROMO_CAPTURE = 14
QUEEN_PROMO_CAPTURE = 15

def createTypeMap():
    _typeMap = {}
    _typeMap[0] = mpz(0)
    _typeMap[1] = mpz(1)
    _typeMap[2] = mpz(2)
    _typeMap[3] = mpz(3)
    _typeMap[4] = mpz(4)
    _typeMap[5] = mpz(5)
    _typeMap[8] = mpz(8)
    _typeMap[9] = mpz(9)
    _typeMap[10] = mpz(10)
    _typeMap[11] = mpz(11)
    _typeMap[12] = mpz(12)
    _typeMap[13] = mpz(13)
    _typeMap[14] = mpz(14)
    _typeMap[15] = mpz(15)
    return _typeMap;

typeMap = createTypeMap()

class Move(object):
    type = mpz(0)
    start = -1
    end = -1

    def __init__(self, start, end, moveType):
        self.start = start
        self.end = end
        self.type = typeMap[moveType]
        return
    
    def __str__(self):
        return "(" + str(self.start) + "," + str(self.end) + "," + bin(self.type) + ")"
    