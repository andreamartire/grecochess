'''
Created on Mar 30, 2015

@author: Andrea Martire
'''

from pieces import Rook, Bitshop
import Constants

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
    movesArray = _queenMoves[cellId][Constants.RIGHT]
    movesArray += _queenMoves[cellId][Constants.RIGHT_UP]
    movesArray += _queenMoves[cellId][Constants.UP]
    movesArray += _queenMoves[cellId][Constants.LEFT_UP]
    movesArray += _queenMoves[cellId][Constants.LEFT]
    movesArray += _queenMoves[cellId][Constants.LEFT_DOWN]
    movesArray += _queenMoves[cellId][Constants.DOWN]
    movesArray += _queenMoves[cellId][Constants.RIGHT_DOWN]
    return movesArray