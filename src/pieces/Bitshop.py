'''
Created on Mar 30, 2015

@author: Andrea Martire
'''

import Utils, Constants

#Calculate anti-diagonal distance for bitshop's moves
def antidiagonalDistance(col, row):
    if(row == 1 or col == 8):
        return 0
    elif(row == 2 or col == 7):
        return 1
    elif(row == 3 or col == 6):
        return 2
    elif(row == 4 or col == 5):
        return 3
    elif(row == 5 or col == 4):
        return 4
    elif(row == 6 or col == 3):
        return 5
    elif(row == 7 or col == 2):
        return 6
    else:
        return 7
    
_bitshopMoves = {}

#Precalculate bitshop pseudolegal moves for each cell
def calculateMoves():
    
    for cellIndex in range(0,64):
        row = Utils.getRow(cellIndex)
        col = Utils.getColumn(cellIndex)
        
        startCellBitBoard = Utils.getCellBitArrayById(cellIndex)
        
        #init cell array
        _bitshopMoves[startCellBitBoard] = {}
        _bitshopMoves[startCellBitBoard][Constants.RIGHT_UP] = []
        _bitshopMoves[startCellBitBoard][Constants.LEFT_UP] = []
        _bitshopMoves[startCellBitBoard][Constants.LEFT_DOWN] = []
        _bitshopMoves[startCellBitBoard][Constants.RIGHT_DOWN] = []
        
        #   A
        #  /
        for i in range(1,8-max(row,col)+1):
            endCellBitBoard = Utils.getCellBitArrayById(cellIndex + 9*i)
            _bitshopMoves[startCellBitBoard][Constants.RIGHT_UP].append(endCellBitBoard)
        #  A
        #   \
        for i in range(1,antidiagonalDistance(row,col)+1):
            endCellBitBoard = Utils.getCellBitArrayById(cellIndex + 7*i)
            _bitshopMoves[startCellBitBoard][Constants.LEFT_UP].append(endCellBitBoard)
        #   /
        #  V
        for i in range(1,min(row,col)):
            endCellBitBoard = Utils.getCellBitArrayById(cellIndex - 9*i)
            _bitshopMoves[startCellBitBoard][Constants.LEFT_DOWN].append(endCellBitBoard)
        #  \
        #   V
        for i in range(1,antidiagonalDistance(col,row)+1):
            endCellBitBoard = Utils.getCellBitArrayById(cellIndex - 7*i)
            _bitshopMoves[startCellBitBoard][Constants.RIGHT_DOWN].append(endCellBitBoard)
        
    return _bitshopMoves

#calculate pieces' moves only once
_bitshopMoves = calculateMoves()

def bitshopMoves():
    return _bitshopMoves

def getMovesArray(cellId):
    return _bitshopMoves[cellId]