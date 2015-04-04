'''
Created on Mar 30, 2015

@author: Andrea Martire
'''

import Utils, Constants
    
#Precalculate rook's pseudolegal moves for each cell
def calculateMoves():
    
    _rookMoves = {}
    
    for cellIndex in range(0,64):
        row = Utils.getRow(cellIndex)
        col = Utils.getColumn(cellIndex)
        
        startCellBitBoard = Utils.getCellBitArrayById(cellIndex)
        
        #init cell array
        _rookMoves[startCellBitBoard] = {}
        _rookMoves[startCellBitBoard][Constants.RIGHT] = []
        _rookMoves[startCellBitBoard][Constants.UP] = []
        _rookMoves[startCellBitBoard][Constants.LEFT] = []
        _rookMoves[startCellBitBoard][Constants.DOWN] = []     
        
        #   
        #  -->
        for i in range(1,8-col+1):
            endCellBitBoard = Utils.getCellBitArrayById(cellIndex + i)
            _rookMoves[startCellBitBoard][Constants.RIGHT].append(endCellBitBoard)
        #   A
        #   I
        for i in range(1,8-row+1):
            endCellBitBoard = Utils.getCellBitArrayById(cellIndex + 8*i)
            _rookMoves[startCellBitBoard][Constants.UP].append(endCellBitBoard)
        #  
        #  <--
        for i in range(1,col):
            endCellBitBoard = Utils.getCellBitArrayById(cellIndex - i)
            _rookMoves[startCellBitBoard][Constants.LEFT].append(endCellBitBoard)
        #   I
        #   V
        for i in range(1,row):
            endCellBitBoard = Utils.getCellBitArrayById(cellIndex - 8*i)
            _rookMoves[startCellBitBoard][Constants.DOWN].append(endCellBitBoard)
        
    return _rookMoves

_rookMoves = calculateMoves()

def rookMoves():
    return _rookMoves

def getMovesArray(cellId):
    return _rookMoves[cellId]