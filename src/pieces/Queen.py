'''
Created on Mar 30, 2015

@author: Andrea Martire
'''

from pieces import Rook, Bitshop

#calculate pieces' moves only once
_diagonalMoves = Bitshop.bitshopMoves()
_orthogonalMoves = Rook.rookMoves()

def diagonalMoves():
    return _diagonalMoves

def orthogonalMoves():
    return _orthogonalMoves

def calculateMoves():
    _queenMoves = {}
    #merge two dictionaries of dictionaries
    for cellId in range(0,64):
        _queenMoves[cellId] = _diagonalMoves[cellId].copy()
        _queenMoves[cellId].update(_orthogonalMoves[cellId])
    return _queenMoves

_queenMoves = calculateMoves()

def queenMoves():
    return _queenMoves

def getMovesArray(cellId):
    return _queenMoves[cellId]