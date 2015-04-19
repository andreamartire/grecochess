'''
Created on 31/mar/2015

@author: Andrea Martire
'''
from gmpy import mpz
import Utils
from Constants import NO_PIECE_CODE

class Move(object):
    type = mpz(0)
    start = -1
    end = -1
    pieceStart = NO_PIECE_CODE
    pieceEnd = NO_PIECE_CODE
    
    def __init__(self, start, end, pieceStart, moveType, pieceEnd=NO_PIECE_CODE):
        self.start = start
        self.end = end
        self.pieceStart = pieceStart
        self.type = typeMap[moveType]
        self.pieceEnd = pieceEnd
        return
    
    def __str__(self):
        if(self.pieceEnd != NO_PIECE_CODE):
            return "(" + str(Utils.getPieceByCode(self.pieceStart)) + "," + str(Utils.getPositionByCellBitArray(self.start)) + "," + str(Utils.getPositionByCellBitArray(self.end)) + "," + bin(self.type) + "," + str(Utils.getPieceByCode(self.pieceEnd)) + ")"
        return "(" + str(Utils.getPieceByCode(self.pieceStart)) + "," + str(Utils.getPositionByCellBitArray(self.start)) + "," + str(Utils.getPositionByCellBitArray(self.end)) + "," + bin(self.type) + ")"

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

