'''
Created on Mar 30, 2015

@author: Andrea Martire
'''

import Utils, Constants

#Precalculate rook's pseudolegal moves for each cell
def calculateMoves():
    
    rookMoves = {}
    
    for cellIndex in range(0,64):
        row = Utils.getRow(cellIndex)
        col = Utils.getColumn(cellIndex)
        
        #init cell array
        rookMoves[cellIndex] = {}
        rookMoves[cellIndex][Constants.RIGHT] = []
        rookMoves[cellIndex][Constants.UP] = []
        rookMoves[cellIndex][Constants.LEFT] = []
        rookMoves[cellIndex][Constants.DOWN] = []     
        
        #   
        #  -->
        for i in range(1,8-col+1):
            rookMoves[cellIndex][Constants.RIGHT].append(cellIndex + i)
        #   A
        #   I
        for i in range(1,8-row+1):
            rookMoves[cellIndex][Constants.UP].append(cellIndex + 8*i)
        #  
        #  <--
        for i in range(1,col):
            rookMoves[cellIndex][Constants.LEFT].append(cellIndex - i)
        #   I
        #   V
        for i in range(1,row):
            rookMoves[cellIndex][Constants.DOWN].append(cellIndex - 8*i)
        
    return rookMoves

#calculate pieces' moves only once
_rookMoves = calculateMoves()

def rookMoves():
    return _rookMoves

def getMovesArray(cellId):
    movesArray = _rookMoves[cellId][Constants.RIGHT]
    movesArray += _rookMoves[cellId][Constants.UP]
    movesArray += _rookMoves[cellId][Constants.LEFT]
    movesArray += _rookMoves[cellId][Constants.DOWN]
    return movesArray