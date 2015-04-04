'''
Created on Mar 30, 2015

@author: Andrea Martire
'''

import Utils, Constants

_whitePawnMoves = {}
_blackPawnMoves = {}
    
#Precalculate white pawn's pseudolegal moves for each cell
def calculateWhitePawnMoves():
    
    for cellIndex in range(0,64):
        row = Utils.getRow(cellIndex)
        col = Utils.getColumn(cellIndex)
        
        startCellBitBoard = Utils.getCellBitArrayById(cellIndex)
        
        #init cell array
        _whitePawnMoves[startCellBitBoard] = {}
    
        if(row > 1):
            #  A
            #   \
            if(row < 8 and col > 1):
                endCellBitBoard = Utils.getCellBitArrayById(cellIndex + 7)
                _whitePawnMoves[startCellBitBoard][Constants.LEFT_UP] = endCellBitBoard
            #  A
            #  i
            if(row < 8):
                endCellBitBoard = Utils.getCellBitArrayById(cellIndex + 8)
                _whitePawnMoves[startCellBitBoard][Constants.UP] = endCellBitBoard 
            #  A
            #  i
            #  i
            if(row == 2):
                endCellBitBoard = Utils.getCellBitArrayById(cellIndex + 8*2)
                _whitePawnMoves[startCellBitBoard][Constants.DOUBLE_UP] = endCellBitBoard   
            #   A
            #  /
            if(row < 8 and col < 8):
                endCellBitBoard = Utils.getCellBitArrayById(cellIndex + 9)
                _whitePawnMoves[startCellBitBoard][Constants.RIGHT_UP] = endCellBitBoard
        
    return _whitePawnMoves

#Precalculate black pawn's pseudolegal moves for each cell
def calculateBlackPawnMoves():
    
    
    for cellIndex in range(0,64):
        row = Utils.getRow(cellIndex)
        col = Utils.getColumn(cellIndex)
        
        startCellBitBoard = Utils.getCellBitArrayById(cellIndex)
        
        #init cell array
        _blackPawnMoves[startCellBitBoard] = {}
        
        if(row < 8):
            #  \
            #   V
            if(row > 1 and col < 8):
                endCellBitBoard = Utils.getCellBitArrayById(cellIndex - 7)
                _blackPawnMoves[startCellBitBoard][Constants.LEFT_UP] = endCellBitBoard
            #  I
            #  V
            if(row > 1):
                endCellBitBoard = Utils.getCellBitArrayById(cellIndex - 8)
                _blackPawnMoves[startCellBitBoard][Constants.UP] = endCellBitBoard
            #  l
            #  l
            #  V
            if(row == 7):
                endCellBitBoard = Utils.getCellBitArrayById(cellIndex - 8*2)
                _blackPawnMoves[startCellBitBoard][Constants.DOUBLE_UP] = endCellBitBoard
            #   /
            #  V
            if(row > 1 and col > 1):
                endCellBitBoard = Utils.getCellBitArrayById(cellIndex - 9)
                _blackPawnMoves[startCellBitBoard][Constants.RIGHT_UP] = endCellBitBoard
    
    return _blackPawnMoves

#calculate pieces' moves only once
_whitePawnMoves = calculateWhitePawnMoves()
_blackPawnMoves = calculateBlackPawnMoves()

def whitePawnMoves():
    return _whitePawnMoves

def blackPawnMoves():
    return _blackPawnMoves

def getMovesArray(cellId, color):
    if(color == Constants.WHITE):
        return _whitePawnMoves[cellId]
    return _blackPawnMoves[cellId]