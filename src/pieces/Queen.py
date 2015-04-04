'''
Created on Mar 30, 2015

@author: Andrea Martire
'''

from pieces import Rook, Bitshop
import Utils

#calculate pieces' moves only once
_diagonalMoves = Bitshop.bitshopMoves()
_orthogonalMoves = Rook.rookMoves()

def diagonalMoves():
    return _diagonalMoves

def orthogonalMoves():
    return _orthogonalMoves

_queenMoves = {}
    
def calculateMoves():
    #merge two dictionaries of dictionaries
    for cellId in range(0,64):
        cellBitBoard = Utils.getCellBitArrayById(cellId)
        _queenMoves[cellBitBoard] = _diagonalMoves[cellBitBoard].copy()
        _queenMoves[cellBitBoard].update(_orthogonalMoves[cellBitBoard])
    return _queenMoves

_queenMoves = calculateMoves()

def queenMoves():
    return _queenMoves

def getMovesArray(cellId):
    return _queenMoves[cellId]