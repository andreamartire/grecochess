'''
Created on Mar 30, 2015

@author: Andrea Martire
'''

import Utils, Constants

#Precalculate white pawn's pseudolegal moves for each cell
def calculateWhitePawnMoves():
    
    whitePawnMoves = {}
    
    for cellIndex in range(0,64):
        row = Utils.getRow(cellIndex)
        col = Utils.getColumn(cellIndex)
        
        #init cell array
        whitePawnMoves[cellIndex] = {}
        whitePawnMoves[cellIndex][Constants.RIGHT_UP] = []
        whitePawnMoves[cellIndex][Constants.UP] = []
        whitePawnMoves[cellIndex][Constants.LEFT_UP] = []
    
        if(row > 1):
            #  A
            #   \
            if(row < 8 and col > 1):
                whitePawnMoves[cellIndex][Constants.LEFT_UP] +=[cellIndex + 7]
            #  A
            #  i
            if(row < 8):
                whitePawnMoves[cellIndex][Constants.UP] += [cellIndex + 8]
            #  A
            #  i
            #  i
            if(row == 2):
                whitePawnMoves[cellIndex][Constants.UP] += [cellIndex + 8*2]    
            #   A
            #  /
            if(row < 8 and col < 8):
                whitePawnMoves[cellIndex][Constants.RIGHT_UP] += [cellIndex + 9]
        
    return whitePawnMoves

#Precalculate black pawn's pseudolegal moves for each cell
def calculateBlackPawnMoves():
    
    blackPawnMoves = {}
    
    for cellIndex in range(0,64):
        row = Utils.getRow(cellIndex)
        col = Utils.getColumn(cellIndex)
        
        #init cell array
        blackPawnMoves[cellIndex] = {}
        blackPawnMoves[cellIndex][Constants.RIGHT_UP] = []
        blackPawnMoves[cellIndex][Constants.UP] = []
        blackPawnMoves[cellIndex][Constants.LEFT_UP] = []
        
        if(row < 8):
            #  \
            #   V
            if(row > 1 and col < 8):
                blackPawnMoves[cellIndex][Constants.LEFT_UP].append(cellIndex - 7)
            #  I
            #  V
            if(row > 1):
                blackPawnMoves[cellIndex][Constants.UP].append(cellIndex - 8)
            #  l
            #  l
            #  V
            if(row == 7):
                blackPawnMoves[cellIndex][Constants.UP].append(cellIndex - 8*2)  
            #   /
            #  V
            if(row > 1 and col > 1):
                blackPawnMoves[cellIndex][Constants.RIGHT_UP].append(cellIndex - 9)
    
    return blackPawnMoves

#calculate pieces' moves only once
_whitePawnMoves = calculateWhitePawnMoves()
_blackPawnMoves = calculateBlackPawnMoves()

def whitePawnMoves():
    return _whitePawnMoves

def blackPawnMoves():
    return _blackPawnMoves

def getWhiteMovesArray(cellId):
    movesArray = _whitePawnMoves[cellId][Constants.RIGHT_UP]
    movesArray += _whitePawnMoves[cellId][Constants.UP]
    movesArray += _whitePawnMoves[cellId][Constants.LEFT_UP]
    return movesArray

def getBlackMovesArray(cellId):
    movesArray = _blackPawnMoves[cellId][Constants.RIGHT_UP]
    movesArray += _blackPawnMoves[cellId][Constants.UP]
    movesArray += _blackPawnMoves[cellId][Constants.LEFT_UP]
    return movesArray