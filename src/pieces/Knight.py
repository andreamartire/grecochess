'''
Created on Mar 30, 2015

@author: Andrea Martire
'''

import Utils
    
_knightMoves = {}

#Precalculate knight's pseudolegal moves for each cell
def calculateMoves():
        
    for cellIndex in range(0,64):
        row = Utils.getRow(cellIndex)
        col = Utils.getColumn(cellIndex)
        
        startCellBitBoard = Utils.getCellBitArrayById(cellIndex)
        
        #init cell array
        _knightMoves[startCellBitBoard] = []
        
        #   I
        #   I
        # __I 
        #
        if(row > 2 and col > 1):
            endCellBitBoard = Utils.getCellBitArrayById(cellIndex - 17)
            _knightMoves[startCellBitBoard].append(endCellBitBoard)
        # I
        # I
        # I__
        #
        if(row > 2 and col < 8):
            endCellBitBoard = Utils.getCellBitArrayById(cellIndex - 15)
            _knightMoves[startCellBitBoard].append(endCellBitBoard)
        # ____
        # I
        #
        if(row > 1 and col > 2):
            endCellBitBoard = Utils.getCellBitArrayById(cellIndex - 10)
            _knightMoves[startCellBitBoard].append(endCellBitBoard)
        # ____
        #    I
        #
        if(row > 1 and col < 7):
            endCellBitBoard = Utils.getCellBitArrayById(cellIndex - 6)
            _knightMoves[startCellBitBoard].append(endCellBitBoard)
        #    
        # ___I
        #
        if(row < 8 and col < 7):
            endCellBitBoard = Utils.getCellBitArrayById(cellIndex + 10)
            _knightMoves[startCellBitBoard].append(endCellBitBoard)
        #    
        # I___
        #
        if(row < 8 and col > 2):
            endCellBitBoard = Utils.getCellBitArrayById(cellIndex + 6)
            _knightMoves[startCellBitBoard].append(endCellBitBoard)
        # ___
        # I 
        # I 
        # I
        if(row < 7 and col < 8):
            endCellBitBoard = Utils.getCellBitArrayById(cellIndex + 17)
            _knightMoves[startCellBitBoard].append(endCellBitBoard)
        # ___
        #   I 
        #   I 
        #   I
        if(row < 7 and col > 1):
            endCellBitBoard = Utils.getCellBitArrayById(cellIndex + 15)
            _knightMoves[startCellBitBoard].append(endCellBitBoard)
    return _knightMoves

#calculate pieces' moves only once
_knightMoves = calculateMoves()

def getMovesArray(cellId):
    return _knightMoves[cellId]
